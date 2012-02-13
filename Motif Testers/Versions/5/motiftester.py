# Line-by-line tester for ProMOL Motifs
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

def __init__(argument):
    '''This function is patterned after ProMol/__init__.py.
    It adds the tester to the PyMOL plugins menu...'''
    argument.menuBar.addmenuitem('Plugin', 'command', label = 'ProMOL Motif Tester', command = launchTester)

def printGreeting():
    printOutput('ProMOL Motif Tester')
    printOutput('By Cyprian Corwin at SBEVSL')
    printOutput('This plugin for PyMOL will run Python-based ProMOL')
    printOutput('motif scripts line by line, interactively or in batch')
    printOutput('mode, and allow the user to see the effects of each line.')

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

def printOutputToFile(theFile, string='', newLine = True):
    '''This outputs to a file instead of the text box.'''
    whatToWrite = string + ('\n' * newLine)
    theFile.write(whatToWrite)

def printOutputToScreen(string='', newLine = True):
    '''This adds the specified string and an optional newline to the end
    of the text box.  This replaced print statements when console output
    failed to work inside of PyMOL.'''
    entryWidget.insert(tk.END, string)
    if newLine:
        entryWidget.insert(tk.END, '\n')
    entryWidget.see(tk.END)

def writingToFile():
    '''This checks a global file object to see whether we are writing
    to a file.  It returns False if the object is not a file or does not exist.'''
    try:
        retVal = (type(fileWeAreUsing) == file)
    except NameError:
        retVal = False
    return retVal
        
def printOutput(string='', newLine=True):
    '''This prints output to whichever mechanism we are using.'''
    if writingToFile():
        # Access the global file object.
        printOutputToFile(fileWeAreUsing, string, newLine)
    else:
        printOutputToScreen(string, newLine)

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

def runLine(line, precisionFactor):
    '''This runs the line in an environment with d set to
    the precision factor.'''
    exec line in {'d': precisionFactor, 'cmd':cmd}

def printPyMOLState():
    '''This displays the total number of selections and objects in the
    PyMOL window, as well as the total number of atoms, and then lists
    each object and how many atoms it contains.  If there are fewer
    than 25 individual residues present, they will be listed; otherwise,
    if there are fewer than 25 KINDS of residues present, they will be
    listed; in either case the number of atoms involved is displayed.
    In addition, for nonempty selections that are either jessatom#
    selections with fewer than 10 atoms, or a final motif (determined
    by the presence of an underscore in the name) with any number of
    atoms, the individual atoms will be listed.'''
    selections = cmd.get_names('all')
    printOutput()
    printOutput('Current PyMOL state:')
    printOutput('There are currently {0} PyMOL objects containing a total of {1} atoms:'.format(len(selections), cmd.count_atoms()))
    for selection in selections:
        stored.residueDictionary = dict()
        residueDictionary = stored.residueDictionary
        cmd.iterate(selection, 'stored.residueDictionary[(resn, resi)] = (stored.residueDictionary[(resn, resi)] + 1) if (resn, resi) in stored.residueDictionary else 1')
        if len(residueDictionary) < 25:
            residueList = ', '.join(['{0} on {1} {2}'.format(residueDictionary[pair], pair[0], pair[1]) for pair in residueDictionary])
        else: # Just summarize, combine different copies of the same residue
            glossOver = dict()
            resCount = dict()
            for pair in residueDictionary:
                glossOver[pair[0]] = (glossOver[pair[0]] + residueDictionary[pair]) if pair[0] in glossOver else residueDictionary[pair]
                resCount[pair[0]] = (resCount[pair[0]] + 1) if pair[0] in resCount else 1
            if len(glossOver) < 25:
                residueList = ', '.join(['{0} total on {1} x {2}'.format(glossOver[resName], resCount[resName], resName) for resName in glossOver])
            else: # Still too long, just count them!
                residueList = 'too many to list'
        # Print atom list for jessatoms up to 10 atoms long and final motifs (containing underscores)
        # But only if they're not empty
        selectDetail = '    {0}: {1} atoms ({2})'.format(selection, cmd.count_atoms(selection), residueList)
        listingAtoms = cmd.count_atoms(selection) > 0 and (((cmd.count_atoms(selection) < 11) and selection.startswith('jessatom')) or ('_' in selection))
        printOutput()
        printOutput(selectDetail, newLine = not listingAtoms)
        if listingAtoms:
            printOutput(' (atoms listed below):')
            printOutput('Residue Name\t\tResidue Index\t\tAtom Name\t\tElement')
            stored.atomLines = list()
            cmd.iterate(selection, 'stored.atomLines.append("{0}\t\t{1}\t\t{2}\t\t{3}".format(resn, resi, name, elem))')
            for atomLine in stored.atomLines:
                printOutput(atomLine)
    printOutput()

def runLineByLine(motifFilename, precisionFactor, batchMode = False):
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
    acquire a list of logical lines from the file.'''
    with open(motifFilename, 'rU') as motifFile:
        # Run first token's logical line, and the logical line after
        # every NEWLINE (NOT every NL!) unless it is end of file
        # This should execute every logical line exactly once
        # Token type is index 0, logical line is index 4
        # Token[2][0] is starting physical line number
        # Tokens are 5-element tuples
        printOutput('Running {0}...'.format(motifFilename))
        # If we're in batch mode, hide the PyMOL viewer before starting
        # the entire thing and only show it again after all lines are
        # finished.  If we're in interactive, apparently hiding and
        # showing doesn't usually work over such a short time frame.
        if batchMode:
            cmd.window('hide')
        runNextTokensLogicalLine = True
        for eachToken in tokenize.generate_tokens(motifFile.readline):
            if runNextTokensLogicalLine and not tokenize.ISEOF(eachToken[0]):
                printPyMOLState()
                printOutput('Next logical line (starting on line {0}):'.format(eachToken[2][0]))
                # Don't print two newlines
                printOutput(eachToken[4], newLine = (not eachToken[4].endswith('\n')))
                if batchMode or askYesNo('Run this line now?'):
                    runLine(eachToken[4], precisionFactor)
                    # See above comment
                else:
                    printOutput('Motif execution terminated early by user.')
                    break
            runNextTokensLogicalLine = (eachToken[0] == tokenize.NEWLINE)
        # See above comment
        if batchMode:
            cmd.window('show')
        printOutput('Finished running motif {0} with precision factor {1}.'.format(motifFilename, precisionFactor))
        printPyMOLState()

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
    
def askForPath():
    '''This repeatedly asks for the path to a motif library until a
    valid directory is entered.  This could be generalized by allowing
    an additional prompt argument.'''
    readPathAgain = True
    while readPathAgain:
        motifPath = getInput('Type or paste path to motif library: ')
        if os.path.exists(motifPath):
            motifPath = os.path.realpath(os.path.abspath(motifPath))
            readPathAgain = not os.path.isdir(motifPath)
            if readPathAgain:
                printOutput('Path was invalid or not a directory.  Please try again.')
    return motifPath

def askForValidPath():
    '''This repeatedly asks for the path to a motif library until a
    valid directory containing one or more regular files is entered.'''
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
        
def loadPDBIntoPyMOL(code):
    '''This announces and then carries out an attempt to reset PyMOL and
    then load a structure specified in the argument.'''
    printOutput('Attempting to load {0} in PyMOL.'.format(code))
    cmd.reinitialize()
    cmd.fetch(code, async=0)

def askPDB():
    '''This one-liner asks for a PDB code to run against.  It currently
    does no validation.'''
    return getInput('PDB code to run against?')

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
    return precisionFactor
    
def printPrecisionFactor(precisionFactor):
    '''This announces the precision factor as specified in the argument.'''
    printOutput('Precision factor \'d\' will be {0}'.format(precisionFactor))
    printOutput('(If this isn\'t what you entered, conversion to floating point failed.)')

def interactive():
    '''This performs an interactive motif run loop similar to version 4.'''
    readPathAgain = True
    doAnotherFile = True
    motifPath = None
    while doAnotherFile:
        if readPathAgain:
            motifPath = askForValidPath()
        motifToRun = selectFile(motifPath)
        # File selected
        # Set up PyMOL context the motif expects
        PDBEntry = askPDB()
        loadPDBIntoPyMOL(PDBEntry)
        precisionFactor = askPrecisionFactor()
        printPrecisionFactor(precisionFactor)
        runForSure = askYesNo('Are you sure you want to run {0} now?'.format(motifToRun))
        if runForSure:
            runLineByLine(motifToRun, precisionFactor)
        doAnotherFile = askYesNo('Run another motif?')
        readPathAgain = (not askYesNo('Reuse folder path?')) if doAnotherFile else False
        
def batch():
    '''This allows the user to run a batch mode motif analysis for file
    output, with way too many options.  This function is way too long,
    and may be partially untested.'''
    global fileWeAreUsing
    singlePDBEntry = None
    singleShortMotif = None
    runningOnly1PDB = False
    motifPath = askForValidPath()
    multiple = askYesNo('Run multiple motifs?')
    # Points to function that returns a boolean given a motif filename
    whetherToRun = None
    # Points to function that returns a PDB code given a motif filename
    whatToRunAgainst = None
    multipleOutputFiles = False
    outputPath = None
    outputFilename = None
    if multiple:
        # Run multiple motifs
        multipleOutputFiles = askYesNo('Place each motif run in its own file?')        
        runAll = askYesNo('Run ALL motifs in this folder?')
        if runAll:
            # Run ALL files
            whetherToRun = lambda motif: True
        else:
            # Run multiple files filtered by a custom lambda
            printOutput('Enter a Python lambda expression that will return')
            printOutput('True or False given the unqualified (without the')
            printOutput('full path) filename of the motif as its single')
            printOutput('argument.  (For example, for the J set only,')
            printOutput('you could use:')
            printOutput('lambda motif: motif.startswith(\'J\')')
            printOutput('Please be careful!  Test your expression first')
            printOutput('in a Python interpreter if you\'re not sure.')
            l = getInput('Lambda expression: ')
            whetherToRun = eval(l)
        runAgainstMultiple = not askYesNo('Use the same query structure for all motifs?')
        if runAgainstMultiple:
            # Run multiple or all files, against multiple PDB codes
            toEachTheirOwn = askYesNo('Run each motif against the structure on which it is based?')
            if toEachTheirOwn:
                # Run multiple or all files, against themselves
                # Extract the PDB code from the motif filename
                whatToRunAgainst = lambda motif: motif.split('_')[1]
            else:
                # Run multiple or all files, against a custom query PDB code
                # returned by a user lambda expression
                printOutput('Enter a Python lambda expression that will return')
                printOutput('a 4-character query PDB code given the unqualified')
                printOutput('(without the full path) filename of')
                printOutput('a motif to run against it as its single')
                printOutput('argument.  For example, selecting above')
                printOutput('to run each motif against its own structure')
                printOutput('would be equivalent to entering:')
                printOutput('lambda motif: motif.split(\'_\')')
                printOutput('Please be careful!  Test your expression first')
                printOutput('in a Python interpreter if you\'re not sure.')
                l = getInput('Lambda expression: ')
                whatToRunAgainst = eval(l)
        else:
            runningOnly1PDB = True
            # Run multiple or all motifs, against a single PDB query code
    else:
        # Run a single motif against a single PDB code
        # There should also be a way to run a given motif against
        # multiple PDB codes, but that's too much to do now
        singleShortMotif = selectFile(motifPath, returnFullPath = False)
        whetherToRun = (lambda motif: motif == singleShortMotif)
        runningOnly1PDB = True
    if runningOnly1PDB:
        singlePDBEntry = askPDB()
        whatToRunAgainst = lambda motif: singlePDBEntry
    assert(not(whatToRunAgainst == None))
    assert(not(whetherToRun == None))
    printOutput('The next question applies to all motifs.')
    precisionFactor = askPrecisionFactor()
    outputPath = getInput('Type or paste path to folder in which to place output file(s):')
    if multipleOutputFiles:
        printOutput('Files will be named appropriately and placed in this folder.')
        printOutput('If any files are already present with the same names, they')
        printOutput('will be overwritten.  This is your LAST CHANCE to cancel!')
    else:
        outputFilename = getInput('Type or paste filename for output (no path please):')
    
    shortMotifsToRun = filter(whetherToRun, validFiles(motifPath))
    printOutput('Preparing to run {0} motifs.'.format(len(shortMotifsToRun)))
    if askYesNo('Proceed?'):
        if multipleOutputFiles:
            for shortMotifFilename in shortMotifsToRun:
                outputFilename = 'motif_{0}_against_query_{1}.txt'.format(shortMotifFilename.split('.')[0], whatToRunAgainst(shortMotifFilename))
                fullOutputPath = os.path.join(outputPath, outputFilename)
                printOutput('Attempting to open {0} for writing a single motif.'.format(fullOutputPath))
                try:
                    with open(fullOutputPath, 'w') as outfile:
                        fileWeAreUsing = outfile
                        # After the above assignment, printOutput() calls should
                        # go to the file instead of the screen
                        printGreeting()
                        printOutput('Output file generated {0}'.format(time.asctime()))
                        printOutput('This file contains output for a single motif,')
                        printOutput('which was loaded from {0}.'.format(motifPath))
                        printOutput('Motif file: {0}'.format(shortMotifFilename))
                        printOutput('Query structure: {0}'.format(whatToRunAgainst(shortMotifFilename)))
                        loadPDBIntoPyMOL(whatToRunAgainst(shortMotifFilename))
                        printOutput('Precision factor is {0}.'.format(precisionFactor))
                        runLineByLine(os.path.join(motifPath, shortMotifFilename), precisionFactor, batchMode = True)
                        fileWeAreUsing = None
                    printOutput('Finished writing to file.')
                finally:
                    fileWeAreUsing = None
        else:
            assert('outputFilename' in dir())
            assert(not (outputFilename == None))
            fullOutputPath = os.path.join(outputPath, outputFilename)
            printOutput('Attempting to open {0} for writing.'.format(fullOutputPath))
            try:
                with open(fullOutputPath, 'w') as outfile:
                    fileWeAreUsing = outfile
                    # After the above assignment, printOutput() calls should
                    # go to the file instead of the screen
                    printGreeting()
                    printOutput('Output file generated {0}'.format(time.asctime()))
                    printOutput('This file contains output for {0} motifs.'.format(len(shortMotifsToRun)))
                    printOutput('All motifs were loaded from {0}'.format(motifPath))
                    for shortMotifFilename in shortMotifsToRun:
                        printOutput('-' * 30)
                        printOutput('Motif file: {0}'.format(shortMotifFilename))
                        printOutput('Query structure: {0}'.format(whatToRunAgainst(shortMotifFilename)))
                        loadPDBIntoPyMOL(whatToRunAgainst(shortMotifFilename))
                        printOutput('Precision factor is {0}.'.format(precisionFactor))
                        runLineByLine(os.path.join(motifPath, shortMotifFilename), precisionFactor, batchMode = True)
                    fileWeAreUsing = None
                printOutput('Finished writing to file.')
            finally:
                fileWeAreUsing = None

def setup():
    '''This function asks for setup information from the user and then
    runs the selected motif against the selected structure in one of two
    modes.  Much of the original body of this function was moved into
    interactive().'''

    global fileWeAreUsing
    fileWeAreUsing = None
    
    printGreeting()
    printOutput('If you just press Enter, yes/no questions will')
    printOutput('default to yes.  Please be careful not to delete or')
    printOutput('edit the prompts or anything on previous lines.')
    printOutput('Do you wish to write one or more motifs to a file')
    printOutput('without user interaction (batch mode)?')
    userChoseBatchMode = askYesNo('Select Yes for batch or No for interactive')
    userSelectedFunction = batch if userChoseBatchMode else interactive
    userSelectedFunction()
    printOutput('Finished.')
    # Finished
