# Selection analyzer for ProMOL Motifs
# Plugin for PyMOL
# By Cyprian Corwin, January 2012
# Copyright 2012 Rochester Institute of Technology
# Created by Cyprian Corwin (cwc4619@rit.edu <mailto:cwc4619@rit.edu>)
# Licensed under the GPL License
# 
#  work supported in part by the SBEVSL project at
#  Dowling College and at Rochester Institute of Technology under
#  Grant Number R15GM078077 from the National Institute Of General
#  Medical Sciences. The content is solely the responsibility of the
#  authors and does not necessarily represent the official views of
#  the National Institute Of General Medical Sciences or the National
#  Institutes of Health.
# 
# /**********************************************************************
#  *                                                                    *
#  * YOU MAY REDISTRIBUTE THIS COMPONENT UNDER THE TERMS OF THE GPL     *
#  *                                                                    *
#  **********************************************************************/
# 
# /*************************** GPL NOTICES ******************************
#  *                                                                    *
#  * This program is free software; you can redistribute it and/or      *
#  * modify it under the terms of the GNU General Public License as     *
#  * published by the Free Software Foundation; either version 2 of     *
#  * (the License, or (at your option) any later version.               *
#  *                                                                    *
#  * This program is distributed in the hope that it will be useful,    *
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of     *
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      *
#  * GNU General Public License for more details.                       *
#  *                                                                    *
#  * You should have received a copy of the GNU General Public License  *
#  * along with this program; if not, write to the Free Software        *
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA           *
#  * 02111-1307  USA                                                    *
#  *                                                                    *
#  **********************************************************************/


FILES_PER_GROUP = 10
import os.path
from os import listdir
import tokenize
from pymol import cmd
from pymol import stored
import Tkinter as tk
import time
import pmg_tk.startup.ProMol.version as promolversion
import pmg_tk.startup.ProMol.Methods.proutils as proutils
greeting = ['ProMOL Motif Tester and Summarizer Version 12',
    'By Cyprian Corwin at SBEVSL',
    'This plugin for PyMOL will run Python-based ProMOL',
    'motif scripts in batch mode, and generate a',
    'detailed breakdown of each final result at a point',
    'just after its final selection was just created,',
    'plus a summary and analysis of all the motifs',
    'in an additional file.']


# Format for tabulation dictionary:
# Keys are base filenames
# Values are motif run entry tuples

# Format for motif run entry tuples (actually ended up being lists)
# INDEX     MEANING
# 0         Base filename
# 1         # final residues (total for all chains)
# 2         # kinds of residues (total for all chains)
# 3         # final atoms
# 4         # res. sel. not in LOCI
# 5         # res. in LOCI not sel.
# 6         Levenshtein distance information list
# 7         # chains (not including All Chains)
# 8         length of RESI header
# 9         # of types of residues selected but not in RESI header or its subs
# 10        True if displayed

# Format for Levenshtein distance information list:
# [Levenshtein distance entry tuple 1, Levenshtein distance entry tuple
#  2, Levenshtein distance entry tuple 3, ...]

# Format for Levenshtein distance entry tuples:
# (Levenshtein distance, All chains concatenated (Boolean), RESI header substitution (Boolean))

defaultDatabase = dict()

def getUppercaseSubs(uppercaseResidueList):
    '''Returns substitutions in upper case and accepts the original
    sequence in upper case as well.'''
    lowercaseResidueList = [residue.lower() for residue in uppercaseResidueList]
    lowercaseSubsList = proutils.createsubs(lowercaseResidueList)
    uppercaseSubsList = [[residue.upper() for residue in subsSubList] for subsSubList in lowercaseSubsList]
    return uppercaseSubsList
    
def getDatabaseComponent(motifFile, database):
    '''Returns tabulationDictionary value for a motif given by its
    selection name, filename, or full pathname.  If it doesn't exist,
    it is first created as an 11-element list with index 0 set to the
    motif selection name and everything else set to None.'''
    baseName = os.path.splitext(os.path.basename(motifFile))[0]
    return database.setdefault(baseName, [baseName] + ([None] * 10))
    
def createDatabaseGetFunction(database):
    '''Returns a one-argument version of getDatabaseComponent
    that only accepts a motif filename argument and always accesses
    the database passed into createDatabaseGetFunction.'''
    return lambda motifFile: getDatabaseComponent(motifFile, database)

def __init__(argument):
    '''This function is patterned after ProMol/__init__.py.
    It adds the tester to the PyMOL plugins menu...'''
    argument.menuBar.addmenuitem('Plugin', 'command', label = 'ProMOL Motif Tester', command = launchTester)    

def enterCallback(event):
    '''This is called when the Return key is pressed by the user while
    editing the text box.  It actually doesn't really matter what we
    set the waitingForEnter variable to, but setting it here makes the
    call to wait_variable() in getInput() return.'''
    waitingForEnter.set(0)

def initializeGUI():
    '''This creates the graphical user interface.  This plugin was first
    written for a text-based interface, but when it was first run inside
    of PyMOL, it was discovered that calls to raw_input() immediately
    raised EOFError.  Not wanting to discard and rewrite the interface
    to be fully graphical, I created a GUI window to support the existing
    text-based interactions with the user.  It's not perfect (editing
    anything before the end of the prompt would probably result in
    malfunctions when requesting input), but it seems to work well
    enough.
    
    Here, we create a scroll bar, a text area, and a window to hold them;
    link the text area and the scroll bar; and set up the mechanism by
    which getInput can wait for Return to be pressed.'''
    global waitingForEnter
    global entryWidget
    tester = tk.Toplevel()
    tester.minsize(300, 300)
    tester.title('ProMOL Motif Tester')
    entryScroll = tk.Scrollbar(tester, orient=tk.VERTICAL)
    entryWidget = tk.Text(tester, yscrollcommand=entryScroll.set)
    entryScroll.configure(command=entryWidget.yview)
    entryWidget.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
    entryScroll.grid(row=0, column=1, sticky=tk.N+tk.S)
    tester.rowconfigure(0, weight=1)
    tester.columnconfigure(0, weight=1)
    waitingForEnter = tk.IntVar()
    waitingForEnter.set(0)
    entryWidget.bind('<Return>', enterCallback)

def launchTester():
    '''This is the entry point that gets called when the user selects
    the plugin from the PyMOL Plugins Menu.'''
    initializeGUI()
    setup()

def printToScreen(string='', newLine = True):
    '''This adds the specified string and an optional newline to the end
    of the text box.  This replaced print statements when console output
    failed to work inside of PyMOL.'''
    entryWidget.insert(tk.END, str(string))
    if newLine:
        entryWidget.insert(tk.END, '\n')
    entryWidget.see(tk.END)

def printOutput(string='', newLine = True, fileObject = None):
    '''Prints the output to fileObject, unless fileObject is None.  In
    that case, display it in the text box.'''
    if fileObject == None:
        printToScreen(string, newLine)
    else:
        fileObject.write(str(string) + ('\n' * newLine))

def getInput(prompt=''):
    '''This replaced calls to raw_input which failed inside of PyMOL.
    First, we output the prompt string and stay on the same line.
    Then, we move the insertion point to the end of the text.
    Setting waitingForEnter to 1 is probably not necessary, but it does
    help to think of a value of 1 meaning that the plugin is waiting on
    input, whereas a value of 0 means it is not.  wait_variable() is a
    standard Tk method that waits for a Tk variable object to change,
    which in this case happens in enterCallback() when the user presses
    Enter or Return.  Then, we go 2 lines up from the end mark (it
    appears to be on a virtual 'line' by itself, and going up 1 line
    just gets us to the newly added blank newline), and return everything
    from the end of the prompt to the end of the line.  I was using
    tk.INSERT instead of tk.END, which only requires going up 1 line, but
    when I switched to having the prompt and the user entry on the same
    line and specifically cutting out the prompt, I changed it.'''
    printOutput(prompt, newLine = False)
    entryWidget.mark_set(tk.INSERT, entryWidget.index(tk.END))
    waitingForEnter.set(1)
    entryWidget.wait_variable(waitingForEnter)
    ei = entryWidget.index(tk.END)
    # Get the line above the newly added newline, starting after the prompt.
    returnValue = str(entryWidget.get('{0} -2 lines linestart +{1} chars'.format(ei, len(prompt)), '{0} -2 lines lineend'.format(ei)))
    return returnValue

def printGreeting(fileObject = None):
    '''Prints the multi-line greeting to a file or,
    if no file is specified, the screen.'''
    for line in greeting:
        printOutput(line, fileObject = fileObject)

def askYesNo(prompt):
    '''This asks the user a yes or no question.
    When the user enters something starting with Y or N, case insensitive,
    it returns True for yes or False for no.'''
    acceptableInput = {'Y', 'y', 'N', 'n'}
    userReply = [None]
    while userReply[0] not in acceptableInput:
        userReply = getInput('{0} (Y/N):'.format(prompt))
        # Default is yes
        if len(userReply) == 0:
            userReply = 'Y'
            printOutput('[Defaulting to yes]')
    return (userReply[0] in {'Y', 'y'})

def selectFromMenu(prompt, options):
    '''This asks the user to select from a list of
    options by entering a number.  The prompt is repeated
    until an option within range is entered.  It returns
    the index of the selected option.'''
    # Present the user with a one-based list but return the zero-based
    # list index
    # This generates a set of the form {'1'...'n'} where n is the
    # number of options available
    acceptableInput = set(map(str, range(len(options) + 1))) - {'0'}
    userReply = None
    while userReply not in acceptableInput:
        printOutput(prompt)
        # zbi stands for zero-based index
        for zbi, opt in enumerate(options):
            printOutput('{0}: {1}'.format(zbi + 1, opt))
        userReply = getInput('Enter selection (1-{0}):'.format(len(options)))
    selectedIndex = int(userReply) - 1
    printOutput('You selected: {0}'.format(options[selectedIndex]))
    return selectedIndex

def displaySelectionBreakdown(motifFilename, database, of = None):
    '''This displays information about the atoms and residues
    in named PyMOL selections.  It requires the motif filename,
    as well as the output file object or None.'''
    # mret stands for Motif Run Entry Tuple
    mret = createDatabaseGetFunction(database)
    # mret is now a function
    motifName = os.path.splitext(os.path.basename(motifFilename))[0]
    selections = cmd.get_names('all')
    printOutput(fileObject = of)
    printOutput('Selections present after motif finished:', fileObject = of)
    printOutput('{0} PyMOL objects containing a total of {1} atoms:'.format(len(selections), cmd.count_atoms()), fileObject = of)
    for selection in selections:
        stored.residueDictionary = dict()
        residueDictionary = stored.residueDictionary
        cmd.iterate(selection, 'stored.residueDictionary[(chain, resn, resi)] = (stored.residueDictionary[(chain, resn, resi)] + 1) if (chain, resn, resi) in stored.residueDictionary else 1')
        # Just summarize, combine different copies of the same residue
        # glossOver and resCount now use (chain, resn) as keys
        glossOver = dict()
        resCount = dict()
        for pair in residueDictionary:
            # glossOver[(chain, resn)] maps to the total number of atoms on all copies of residue "resn" on chain "chain"
            glossOver[(pair[0], pair[1])] = (glossOver[(pair[0], pair[1])] + residueDictionary[pair]) if (pair[0], pair[1]) in glossOver else residueDictionary[pair]
            # resCount[(chain, resn)] maps to the number of copies of residue "resn" on chain "chain"
            resCount[(pair[0], pair[1])] = (resCount[(pair[0], pair[1])] + 1) if (pair[0], pair[1]) in resCount else 1
        residueList = ', '.join(['{0} total on {1} x {2} (chain {3})'.format(glossOver[(resChain, resName)], resCount[(resChain, resName)], resName, resChain) for resChain, resName in sorted(glossOver)])
        # Print full atom list for all nonempty selections
        selectDetail = '    {0}: {1} atoms ({2})'.format(selection, cmd.count_atoms(selection), residueList)
        listingAtoms = (cmd.count_atoms(selection) > 0)
        printOutput(fileObject = of)
        printOutput(selectDetail, newLine = not listingAtoms, fileObject = of)
        if listingAtoms:
            printOutput(' (atoms listed below):', fileObject = of)
            printOutput('CHAIN\t\tRESI\t\tRESN\t\tNAME\t\tELEM', fileObject = of)
            stored.atomLines = list()
            cmd.iterate(selection, 'stored.atomLines.append("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}".format(chain, resi, resn, name, elem))')
            for atomLine in stored.atomLines:
                printOutput(atomLine, fileObject = of)
        # Populate tabulation dictionary
        if selection.lower() == motifName.lower(): # Should not be necessary, but some motifs misbehaved!
            mret(motifName)[3] = cmd.count_atoms(selection) # Number of selected atoms
            mret(motifName)[1] = len(residueDictionary) # Total number of selected residues
            mret(motifName)[2] = len(set([triple[1] for triple in residueDictionary])) # Number of kinds of residues
            mret(motifName)[7] = len(set([triple[0] for triple in residueDictionary])) # Number of chains
    printOutput(fileObject = of)

def compareResultToHeader(motifFilename, database, of = None):
    # mret stands for Motif Run Entry Tuple
    mret = createDatabaseGetFunction(database)
    # mret is now a function

    # Read header
    # resiHeader will be a list of residue abbreviation strings
    resiHeader = None
    # lociHeader will be a dictionary
    # mapping chains to lists of residue indices as strings
    lociHeader = None
    with open(motifFilename, 'rU') as linelist:
        haveRESI = False
        haveLOCI = False
        
        for line in linelist:
            # stripped is line to uppercase with no newline or
            # whitespace
            # Strip it twice to remove them no matter the order
            # (without the second strip('\n'), a newline inside
            # whitespace would not be stripped; without the first
            # one, whitespace inside a newline would not be stripped;
            # by "inside" I mean "before" if we're at the end of the
            # string)
            stripped = line.strip('\n').strip().strip('\n').upper()
            if stripped.startswith('RESI:'):
                haveRESI = True
                resiHeader = stripped[5:].split(',')
            elif stripped.startswith('LOCI:'):
                haveLOCI = True
                semiSplit = filter((lambda item: len(item) > 0), stripped[5:].split(';'))
                hyphenSplit = [item.split('-') for item in semiSplit]
                # hyphenSplit is now [[chain 1, residue index list string 1], ...]
                separateDicts = [{item[0]: item[1].split(',')} for item in hyphenSplit]
                # separateDicts is what we want but with each chain in its own dictionary
                lociHeader = dict()
                for eachDict in separateDicts:
                    lociHeader.update(eachDict)
            if haveRESI and haveLOCI:
                break
                
    # lociResult is the same format as lociHeader
    # but resiResult is a dictionary mapping chains to residue lists
    resiResult = {'All chains': list()}
    lociResult = dict()
    # atomAttributes will be a list of dictionaries mapping attributes
    # to values
    atomAttributes = list()
    stored.atomAttributes = atomAttributes
    finalSelection = os.path.splitext(os.path.basename(motifFilename))[0]
    # Added for misbehaving motifs
    wellBehaved = True
    if finalSelection not in cmd.get_names('all'):
        wellBehaved = False
        finalSelection = finalSelection.upper()
    # If that doesn't work, now we're desparate!
    if finalSelection not in cmd.get_names('all'):
        wellBehaved = False # Probably redundant
        fsCandidates = [anyName for anyName in cmd.get_names('all') if '_' in anyName]
        finalSelection = fsCandidates[0] if len(fsCandidates) > 0 else None
    # There is only one None object so 'is' and '==' should be equivalent
    if finalSelection is not None:
        cmd.iterate(finalSelection, 'stored.atomAttributes.append({"chain": chain, "resi": resi, "resn": resn})')
    # This list SHOULD be already sorted by resi order (and probably other things too)
    # This algorithm should look familiar from count() in ProMOL's motif.py
    previousResidue = None
    # THE COMMENT BELOW IS VERY IMPORTANT TO UNDERSTAND!!!
    # To PyMOL (unlike ProMOL motifs), RESN (not RESI) is residue name and RESI is residue index (not name)
    for atom in atomAttributes:
        if not (atom == previousResidue):
            if atom['chain'].upper() not in resiResult:
                resiResult[atom['chain'].upper()] = list()
            if atom['chain'].upper() not in lociResult:
                lociResult[atom['chain'].upper()] = list()
            # I know this LOOKS wrong, but see comment above!
            resiResult[atom['chain'].upper()].append(atom['resn'])
            resiResult['All chains'].append(atom['resn'])
            # Now do the loci result
            lociResult[atom['chain'].upper()].append(atom['resi'])
            previousResidue = atom
    residueTypesSelected = set([atom['resn'] for atom in atomAttributes])
    printOutput('Comparison of results to headers:', fileObject = of)
    if haveLOCI:
        printOutput('LOCI attribute comparison:', fileObject = of)
        # Flatten to a list of tuples
        flatLociHeader = list()
        for lChain in lociHeader:
            for locus in lociHeader[lChain]:
                flatLociHeader.append((lChain, locus))
                
        flatLociResult = list()
        for lChain in lociResult:
            for locus in lociResult[lChain]:
                flatLociResult.append((lChain, locus))

        lociHeaderSet = set(flatLociHeader)
        lociResultSet = set(flatLociResult)
        printOutput('Motif header LOCI: {0}'.format(lociHeader), fileObject = of)
        printOutput('Selection result residue indices: {0}'.format(lociResult), fileObject = of)
        printOutput('{0} common indices: {1}'.format(len(lociHeaderSet.intersection(lociResultSet)), sorted(list(lociHeaderSet.intersection(lociResultSet)))), fileObject = of)
        printOutput('{0} header LOCI were not selected by the motif algebra: {1}'.format(len(lociHeaderSet - lociResultSet), sorted(list(lociHeaderSet - lociResultSet))), fileObject = of)
        mret(motifFilename)[5] = len(lociHeaderSet - lociResultSet)
        printOutput('The motif selected atoms from {0} residues not specified in the LOCI header: {1}'.format(len(lociResultSet - lociHeaderSet), sorted(list(lociResultSet - lociHeaderSet))), fileObject = of)
        mret(motifFilename)[4] = len(lociResultSet - lociHeaderSet)
    else:
        printOutput('Unable to compare LOCI attribute to selection, as it was not found in the header!', fileObject = of)
        
    printOutput(fileObject = of)
    if haveRESI:
        printOutput('RESI attribute comparison:', fileObject = of)
        printOutput('Motif header RESI: {0}'.format(resiHeader), fileObject = of)
        printOutput('Ultimately selected residue names (resn) by chain:', fileObject = of)
        printOutput('(resi attribute is actually numbers, so its use', fileObject = of)
        printOutput('in the motif headers for names may be a misnomer)', fileObject = of)
        printOutput('{0}'.format(resiResult), fileObject = of)
        wouldMatch = any([(2 * len(resiHeader) > len(resiResult[eachChain])) for eachChain in resiResult])
        mret(motifFilename)[10] = wouldMatch if wellBehaved else '{0}, but improperly named final selection would cause rejection anyway.'.format(wouldMatch)
        listOfSubLists = getUppercaseSubs(resiHeader)
        flatSubsList = list()
        for subList in listOfSubLists:
            flatSubsList.extend(subList)
        subsSet = set(flatSubsList) # Should include original header
        mret(motifFilename)[9] = len(residueTypesSelected - subsSet)
        mret(motifFilename)[8] = len(resiHeader)
        
        if wouldMatch:
            printOutput('If my calculations are correct, this result WOULD be displayed by ProMOL', fileObject = of)
            printOutput('because at least one of the above chains (including "All") was less than', fileObject = of)
            printOutput('twice as long as the RESI motif header (see above).', fileObject = of)
        else:
            printOutput('If my calculations are correct, this result WOULD NOT be displayed by ProMOL', fileObject = of)
            printOutput('because all of the above chains were at least twice as long as the RESI', fileObject = of)
            printOutput('motif header (see above).', fileObject = of)
        if not wellBehaved:
            printOutput('However, that doesn\'t matter.  This motif would immediately be discarded by ProMOL')
            printOutput('because it generates an improperly named selection!')
        printOutput('Levenshtein distances as calculated by the proutils module of ProMOL', fileObject = of)
        printOutput('version {0} (algorithm version {1}):'.format(promolversion.VERSION, promolversion.ALG_VERSION), fileObject = of)
        ldil = list() # For tabulationDictionary
        for eachChain in sorted(resiResult):
            printOutput('\tRESI header to {0}: {1}'.format(eachChain, proutils.levenshteinDistance(resiHeader, resiResult[eachChain])), fileObject = of)
            ldil.append((proutils.levenshteinDistance(resiHeader, resiResult[eachChain]), (eachChain == 'All chains'), False))
            if os.path.basename(motifFilename).startswith('J'):
                printOutput('\tRESI header substitutions to {0}:'.format(eachChain), fileObject = of)
                for variation in getUppercaseSubs(resiHeader):
                    printOutput('\t\t{0}: {1}'.format(variation, proutils.levenshteinDistance(variation, resiResult[eachChain])), fileObject = of)
                    ldil.append((proutils.levenshteinDistance(variation, resiResult[eachChain]), (eachChain == 'All chains'), True))
            else:
                printOutput('Not a J set motif, no substitutions required.', fileObject = of)
        printOutput('All of these, as well as the distances from each substitution permutation', fileObject = of)
        printOutput('of the RESI header to each chain, are searched for the minimum and maximum,', fileObject = of)
        printOutput('which is reported by ProMOL as a range (as of ProMOL r160).', fileObject = of)
        mret(motifFilename)[6] = ldil
    else:
        printOutput('Unable to compare RESI attribute to selection, as it was not found in the header!', fileObject = of)

def processMotifSnapshot(motifFilename, database, fileObject = None):
    '''Outputs selection breakdowns, atom listings, and header comparisons
    to fileObject (None for user interface on screen).  Also adds
    an entry to database for the result.'''
    displaySelectionBreakdown(motifFilename, database, fileObject)
    compareResultToHeader(motifFilename, database, fileObject)

def runLine(line, precisionFactor):
    '''This runs the line in an environment with d set to
    the precision factor.'''
    exec line in {'d': precisionFactor, 'cmd':cmd}

def runUntil(motifFilename, precisionFactor, stopCondition, runBeforeStopping):
    '''This uses the Python token parser to extract logical lines of
    Python code from the motif file.  Just splitting at newlines would
    not be sufficient, since a logical line must be executed as a whole
    and can span multiple newline-separated physical lines in the actual
    file.  However, the tokenizer outputs individual tokens.  The tokens
    include the entire logical line they are from, but since there will
    be many tokens per line, just iterating through the tokens would
    result in each logical line being run multiple times.  After poring
    over output from the tokenizer, I determined that taking the logical
    lines from the first token, plus all tokens immediately following
    a NEWLINE token (not the NL constant, which separates PHYSICAL
    lines), except the end-of-file token, should be sufficient to
    acquire a list of logical lines from the file.  This function returns
    a generator that returns an ordered pair of the form
    (physical line number, line text) at each stopping point.
    motifFilename must be the full path of the motif;
    precisionFactor is the precision factor to feed to the motif;
    stopAfter must be a function taking one
    argument, the current logical line, that returns True if execution
    should stop at this line; runBeforeStopping, if True, means that
    the line will be run before yielding when stopCondition returns
    True; if False, the line will be run after.'''
    with open(motifFilename, 'rU') as motifFile:
        # Run first token's logical line, and the logical line after
        # every NEWLINE (NOT every NL!) unless it is end of file
        # This should execute every logical line exactly once
        # Token type is index 0, logical line is index 4
        # Token[2][0] is starting physical line number
        # Tokens are 5-element tuples
        runNextTokensLogicalLine = True
        for eachToken in tokenize.generate_tokens(motifFile.readline):
            if runNextTokensLogicalLine and not tokenize.ISEOF(eachToken[0]):
                # Consider eachToken[4] as the next logical line
                if runBeforeStopping:
                    runLine(eachToken[4], precisionFactor)
                if stopCondition(eachToken[4]):
                    yield (eachToken[2][0], eachToken[4])
                if not runBeforeStopping:
                    runLine(eachToken[4], precisionFactor)
            # This must stay outside the if!  Otherwise, if it ever
            # went False, it could never get back.
            runNextTokensLogicalLine = (eachToken[0] == tokenize.NEWLINE)

def runMotifWithPause(motifFilename, precisionFactor, showWhenDone, database, fileObject = None):
    cmd.window('hide')
    pauses = runUntil(motifFilename, precisionFactor, (lambda line: (('cmd.select(' in line) and ('_' in line))), True)
    morePauses = True
    alreadyPaused = False
    while morePauses:
        try:
            thisPause = pauses.next()
            printOutput('Paused after line {0}'.format(thisPause[0]), fileObject = fileObject)
            printOutput('Line text: {0}'.format(thisPause[1]), fileObject = fileObject, newLine = not thisPause[1].endswith('\n'))
            if alreadyPaused:
                printOutput('WARNING: We already paused in this motif.', fileObject = fileObject)
                printOutput('The first pause was the one used for the snapshot', fileObject = fileObject)
                printOutput('(both here and in the analysis file).', fileObject = fileObject)
                printOutput('Skipping a repeat call to processMotifSnapshot().', fileObject = fileObject)
            else:
                printOutput('Taking motif snapshot before continuing.  We are', fileObject = fileObject)
                printOutput('partway through the motif, but now is when we will', fileObject = fileObject)
                printOutput('analyze PyMOL\'s state (before the motif can clean up).', fileObject = fileObject)
                processMotifSnapshot(motifFilename, database, fileObject)
            alreadyPaused = True
        except StopIteration:
            morePauses = False
    # End of while loop
    if showWhenDone:
        cmd.window('show')
    printOutput('Finished running motif {0} with precision factor {1}.'.format(motifFilename, precisionFactor), fileObject = fileObject)

def validFiles(motifPath):
    '''Returns a list of the unqualified filenames in the specified directory
    for which os.path.isfile() returns True.'''
    # Valid directory found
    rawFilenames = os.listdir(motifPath)
    # Only list valid files
    filenames = filter((lambda file: os.path.isfile(os.path.join(motifPath, file))), rawFilenames)
    return filenames
    
def anyValidFiles(motifPath):
    '''Returns true if any files in the specified directory are valid
    as determined by os.path.isfile().'''
    return len(validFiles(motifPath)) > 0
    
def askForPath(prompt='Type or paste path to motif library: '):
    '''This repeatedly asks for a path until a
    valid directory is entered.  This was generalized by adding
    an additional prompt argument.'''
    readPathAgain = True
    while readPathAgain:
        motifPath = getInput(prompt)
        if os.path.exists(motifPath):
            motifPath = os.path.realpath(os.path.abspath(motifPath))
            readPathAgain = not os.path.isdir(motifPath)
            if readPathAgain:
                printOutput('Path was invalid or not a directory.  Please try again.')
    return motifPath

def askForValidPath(prompt='Type or paste path to motif library: '):
    '''This repeatedly asks for a path until a valid directory
    containing one or more regular files is entered.'''
    motifPath = askForPath()
    while not anyValidFiles(motifPath):
        printOutput('No files in that directory.')
        motifPath = askForPath()
    return motifPath

def selectFile(motifPath, returnFullPath = True):
    '''This presents a paged menu allowing the user to select a file
    from the given path by displaying them in groups of 10 (or whatever
    the value of FILES_PER_GROUP is).'''
    if anyValidFiles(motifPath):
        filenames = validFiles(motifPath)
        filenames.sort()
        # This is a list comprehension that takes a list of filenames and groups them into sublists of FILES_PER_GROUP each
        # (the last page may have fewer)
        groups = [filenames[offset:(offset + FILES_PER_GROUP)] for offset in range(len(filenames))[::FILES_PER_GROUP]]
        fileSelected = False
        motifToRun = None
        groupIndex = 0
        while not fileSelected:
            printOutput('Displaying page {0} of {1}:'.format(groupIndex + 1, len(groups)))
            for key, motif in enumerate(groups[groupIndex]):
                printOutput('{0}: {1}'.format(key, motif))
            printOutput('p: Previous page')
            printOutput('n: Next page')
            userInput = None
            acceptableInput = set(['p', 'n'] + [repr(num) for num in range(len(groups[groupIndex]))])
            while userInput not in acceptableInput:
                userInput = getInput('Enter selection: ').lower()
            if userInput == 'p':
                groupIndex = groupIndex - 1 if groupIndex > 0 else len(groups) - 1
            elif userInput == 'n':
                groupIndex = groupIndex + 1 if groupIndex < len(groups) - 1 else 0
            else:
                shortFilename = groups[groupIndex][int(userInput)]
                motifToRun = os.path.join(motifPath, shortFilename) if returnFullPath else shortFilename
                fileSelected = True
        return motifToRun
    else:
        return None
        
def loadPDBIntoPyMOL(code, fileObject):
    '''This announces and then carries out an attempt to reset PyMOL and
    then load a structure specified in the argument.'''
    printOutput('Attempting to load {0} in PyMOL.'.format(code), fileObject = fileObject)
    cmd.reinitialize()
    cmd.fetch(code, async=0)

def askPDB():
    '''This one-liner asks for a PDB code to run against.  It currently
    does no validation.'''
    return getInput('PDB code to run against?')

def printPrecisionFactor(precisionFactor):
    '''This announces the precision factor as specified in the argument.'''
    printOutput('Precision factor \'d\' will be {0}'.format(precisionFactor))
    printOutput('(If this isn\'t what you entered, conversion to floating point failed.)')

def askPrecisionFactor():
    '''This repeatedly asks the user for a precision factor until a
    valid floating-point number is entered.'''
    # Just to make sure Python doesn't think precisionFactor might be
    # undefined by the end of the function
    precisionFactor = None
    goodFloat = False
    while not goodFloat:
        dString = getInput('Precision factor (as entered in motif finder)?')
        goodFloat = True
        try:
            precisionFactor = float(dString)
        except ValueError:
            printOutput('Not a valid floating-point number.')
            goodFloat = False
    printPrecisionFactor(precisionFactor)
    return precisionFactor
    
def printAnalysis(precisionFactor, outputPath, database):
    '''Analyze the results of the batch run.'''
    # mret stands for Motif Run Entry Tuple
    mret = createDatabaseGetFunction(database)
    # mret is now a function
    
    # Recapitulation
    # Format for motif run entry tuples (they start out as lists)
    # INDEX     MEANING
    # 0         Base filename
    # 1         # final residues (total for all chains)
    # 2         # kinds of residues (total for all chains)
    # 3         # final atoms
    # 4         # res. sel. not in LOCI
    # 5         # res. in LOCI not sel.
    # 6         Levenshtein distance information list
    # 7         # chains (not including All Chains)
    # 8         length of RESI header
    # 9         # of types of residues selected but not in RESI header or its subs
    # 10        True if displayed
    # Format for Levenshtein distance entry tuples:
    # (Levenshtein distance, All chains concatenated (Boolean), RESI header substitution (Boolean))

    # Define criteria list
    def filteredLevList(motifFilename, allChainConcatenationAllowed, subsAllowed):
        '''Return just Levenshtein distances for a given motif.
        If allChainConcatenationAllowed is True, Levenshtein distances will be
        included regardless of whether their index 1 element is True (meaning it is
        a concatenation of all chains) or False (meaning it is an individual chain);
        otherwise, only distances from tuples whose index 1 element is False will be
        included.
        If subsAllowed is True, Levenshtein distances will be included regardless of
        whether their index 2 element is True (meaning it represents a matchup between
        a substitution of the RESI header) or False (meaning it used the verbatim
        header); otherwise, only distances from tuples whose index 2 element is False
        will be included.'''
        startingList = mret(motifFilename)[6]
        allChainsFilter = (lambda tup: True) if allChainConcatenationAllowed else (lambda tup: not tup[1])
        subsFilter = (lambda tup: True) if subsAllowed else (lambda tup: not tup[2])
        compositeFilter = lambda tup: (allChainsFilter(tup) and subsFilter(tup))
        return [tup[0] for tup in filter(compositeFilter, startingList)]
        
    fll = filteredLevList
    # Returns True if filtered Levenshtein list is not empty
    fllNE = lambda m, b1, b2: len(fll(m, b1, b2)) > 0
    # Returns a customized one-argument function that determines
    # Levenshtein distance eligibility based on the specified
    # boolean values
    def levElig(b1, b2):
        return (lambda m: fllNE(m, b1, b2))

    # Criterion format:
    # (Description, eligibility function, key function)
    criteria = [('Total number of selected residues (all chains)', lambda m: True, lambda m: mret(m)[1]),
                ('Number of different residue types (all chains)', lambda m: True, lambda m: mret(m)[2]),
                ('Total number of atoms (all chains)', lambda m: True, lambda m: mret(m)[3]),
                ('Total number of chains', lambda m: True, lambda m: mret(m)[7]),
                ('Mean number of atoms per chain', lambda m: mret(m)[7] > 0, lambda m: float(mret(m)[3]) / float(mret(m)[7])),
                ('Mean number of residues per chain', lambda m: mret(m)[7] > 0, lambda m: float(mret(m)[1]) / float(mret(m)[7])),
                ('Mean number of atoms per residue', lambda m: mret(m)[1] > 0, lambda m: float(mret(m)[3]) / float(mret(m)[1])),
                ('Extra residues selected but not specified by LOCI', lambda m: True, lambda m: mret(m)[4]),
                ('Extra residues specified by LOCI but not selected', lambda m: True, lambda m: mret(m)[5]),
                ('Total number of extra residues (both types)', lambda m: True, lambda m: mret(m)[4] + mret(m)[5]),
                ('Max Levenshtein distance (individual chains only; no subs)', levElig(False, False), lambda m: max(fll(m, False, False))),
                ('Min Levenshtein distance (individual chains only; no subs)', levElig(False, False), lambda m: min(fll(m, False, False))),
                ('Max Levenshtein distance (any or all chains allowed; no subs)', levElig(True, False), lambda m: max(fll(m, True, False))),
                ('Min Levenshtein distance (any or all chains allowed; no subs)', levElig(True, False), lambda m: min(fll(m, True, False))),
                ('Max Levenshtein distance (individual chains only; subs allowed)', levElig(False, True), lambda m: max(fll(m, False, True))),
                ('Min Levenshtein distance (individual chains only; subs allowed)', levElig(False, True), lambda m: min(fll(m, False, True))),
                ('Max Levenshtein distance (any or all chains allowed; subs allowed) (like ProMOL does it)',
                levElig(True, True), lambda m: max(fll(m, True, True))),
                ('Min Levenshtein distance (any or all chains allowed; subs allowed) (like ProMOL does it)',
                levElig(True, True), lambda m: min(fll(m, True, True))),
                ('(Max Levenshtein distance) over (number of chains) (any or all chains allowed; subs allowed)',
                lambda m: (fllNE(m, True, True) and (mret(m)[7] > 0)), lambda m: float(max(fll(m, True, True))) / float(mret(m)[7])),
                ('Length of RESI header', lambda m: mret(m)[8] != None, lambda m: mret(m)[8]),
                ('Length of selection modulo length of RESI header', lambda m: (mret(m)[8] != None) and (mret(m)[8] > 0), lambda m: mret(m)[1] % mret(m)[8]),
                ('Length of selection over length of RESI header', lambda m: (mret(m)[8] != None) and (mret(m)[8] > 0), lambda m: float(mret(m)[1]) / float(mret(m)[8])),
                ('Number of selected residue types not specified in RESI header or its substitutions', lambda m: mret(m)[9] != None, lambda m: mret(m)[9]),
                ('Inclusion in ProMOL result list', lambda m: mret(m)[10] != None, lambda m: mret(m)[10])]
                
    with open(os.path.join(outputPath, 'analysis.txt'), 'w') as summaryFile:
        # Just to save me typing ", fileObject = summaryFile" over and over again!
        p = lambda string: printOutput(string, fileObject = summaryFile)
        printGreeting(summaryFile)
        p('ANALYSIS FILE')
        p('Generated {0}'.format(time.asctime()))
        p('Analysis follows of the {0} motif runs captured in'.format(len(database)))
        p('the files in this folder (this file was originally located in')
        p(outputPath + ').')
        p('A precision factor of {0} was fed to the motifs.'.format(precisionFactor))
        p('The motifs\' rankings in each of {0}'.format(len(criteria)))
        p('categories follows.  Please note that although these are sorted in')
        p('ascending order, lowest is not always necessarily best in every case.')
        # Keys that, at least once, haven't qualified
        keysThatHaveEverNotQualified = set()
        for criterion in criteria:
            p('=' * 30)
            p('Category:')
            p(criterion[0])
            qualifyingKeys = filter(criterion[1], database) # Should work even with a dict
            disqualifiedSet = set(database.keys()) - set(qualifyingKeys)
            p('{0} of the {1} motif runs qualified for this ranking.'.format(len(qualifyingKeys), len(database)))
            p('Results that failed to qualify:')
            p(disqualifiedSet)
            p('...')
            # Take advantage of stable sort to avoid random ordering
            # within keys that share the same value
            rankedVersion = sorted(qualifyingKeys)
            rankedVersion.sort(key=criterion[2])
            p('Values in this category:')
            for eachMotif in rankedVersion:
                p('{0}: {1}'.format(eachMotif, criterion[2](eachMotif)))
            p('That\'s the end of the information relating to the following category:')
            p(criterion[0])
            keysThatHaveEverNotQualified.update(disqualifiedSet)
        p('=' * 30)
        p('That\'s the end of the rankings.')
        p('{0} motif runs failed to qualify, at least once.  They are:'.format(len(keysThatHaveEverNotQualified)))
        p(keysThatHaveEverNotQualified)
        p('End of file.')
        
def batch(inputPath, outputPath, precisionFactor, shortMotifsToRun, whatToRunAgainst, database):
    database.clear()
    for shortMotifFilename in shortMotifsToRun:
        outputFilename = 'motif_{0}_against_query_{1}.txt'.format(os.path.splitext(shortMotifFilename)[0], whatToRunAgainst(shortMotifFilename))
        fullOutputPath = os.path.join(outputPath, outputFilename)
        printOutput('Attempting to open {0} for writing a single motif.'.format(fullOutputPath))
        with open(fullOutputPath, 'w') as outfile:
            printGreeting(outfile)
            printOutput('Output file generated {0}'.format(time.asctime()), fileObject = outfile)
            printOutput('This file contains output for a single motif,', fileObject = outfile)
            printOutput('which was loaded from {0}.'.format(inputPath), fileObject = outfile)
            printOutput('Motif file: {0}'.format(shortMotifFilename), fileObject = outfile)
            printOutput('Query structure: {0}'.format(whatToRunAgainst(shortMotifFilename)), fileObject = outfile)
            loadPDBIntoPyMOL(whatToRunAgainst(shortMotifFilename), fileObject = outfile)
            printOutput('Precision factor is {0}.'.format(precisionFactor), fileObject = outfile)
            runMotifWithPause(os.path.join(inputPath, shortMotifFilename), precisionFactor, False, database, outfile)
        printOutput('Finished writing to file.')
    printAnalysis(precisionFactor, outputPath, database)
    cmd.window('show')

def setup():
    '''This function asks for setup information from the user and then
    runs the motifs against their own structures.'''
    printGreeting()
    inputPath = askForValidPath()
    shortMotifsInFolder = validFiles(inputPath)
    # Determine which motifs to run
    modes = ('Run all motifs in folder', 'Specify one or more filenames in a list', 'Specify custom Python filter function')
    whichMode = selectFromMenu('Which motifs do you want to run?', modes)
    if whichMode == 0:
        shortMotifsToRun = shortMotifsInFolder
    elif whichMode == 1:
        printOutput('Please list filenames with extensions but not paths,')
        userListString = getInput('separated by commas: ')
        # The extra first argument to a method when called like a function
        # is always self (the recipient of the message)
        # Calling str.strip(self) is like calling self.strip()
        # There is another argument that this doesn't use
        # (Calling str.strip(self, chars) is like calling self.strip(chars))
        # In this case, it should default to whitespace
        unfilteredUserList = map(str.strip, userListString.split(','))
        unfilteredUserSet = set(unfilteredUserList)
        numberInvalid = len(unfilteredUserSet - set(shortMotifsInFolder))
        printOutput('{0} of those {1} items were not present in the folder.'.format(numberInvalid, len(unfilteredUserSet)))
        printOutput('They will be removed.')
        shortMotifsToRun = list(unfilteredUserSet.intersection(set(shortMotifsInFolder)))
    else:
        # whichMode == 2
        # Run multiple files filtered by a custom lambda
        printOutput('Enter a Python lambda expression that will return')
        printOutput('True or False given the unqualified (without the')
        printOutput('full path) filename of the motif as its single')
        printOutput('argument.  (For example, for the J set only,')
        printOutput('you could use:')
        printOutput('lambda motif: motif.startswith(\'J\')')
        printOutput('Please be careful!  Test your expression first')
        printOutput('in a Python interpreter if you\'re not sure.')
        printOutput('Alternatively, enter the name of an existing')
        printOutput('Python function taking one argument.')
        l = None
        while not callable(l):
            l = eval(getInput('Filter function: '))
        shortMotifsToRun = filter(l, shortMotifsInFolder)
    # End of if ladder for which motifs to run
    
    # Determine what to run them against
    modes = ('Run each motif against its own structure', 'Run all motifs against the same structure')
    whichMode = selectFromMenu('What do you want to run them against?', modes)
    if whichMode == 0:
        # Pull out PDB code and run against each motif's own structure
        whatToRunAgainst = lambda filename: filename.split('_')[1]
    else:
        # whichMode = 1
        againstPDB = getInput('Please enter the PDB code to run motifs against: ')
        whatToRunAgainst = lambda filename: againstPDB
    # End of if ladder for what to run motifs against
    
    outputPath = askForPath('Type or paste path to folder in which to place output file(s): ')
    precisionFactor = askPrecisionFactor()
    printOutput('Preparing to run {0} motifs.'.format(len(shortMotifsToRun)))
    if askYesNo('Proceed?'):
        batch(inputPath, outputPath, precisionFactor, shortMotifsToRun, whatToRunAgainst, defaultDatabase)
        printOutput('Finished running {0} motifs.'.format(len(shortMotifsToRun)))
        if askYesNo('Would you like to see the raw ranking database?'):
            printOutput(defaultDatabase)
    else:
        printOutput('Cancelled.')
    printOutput('Motif tester finished.')
    # Finished
