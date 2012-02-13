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

def printOutput(string='', newLine = True):
    '''This adds the specified string and an optional newline to the end
    of the text box.  This replaced print statements when console output
    failed to work inside of PyMOL.'''
    entryWidget.insert(tk.END, string)
    if newLine:
        entryWidget.insert(tk.END, '\n')
    entryWidget.see(tk.END)

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
    each object and how many atoms it contains.'''
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
        selectDetail = '    {0}: {1} atoms ({2})'.format(selection, cmd.count_atoms(selection), residueList)
        printOutput()
        printOutput(selectDetail)
    printOutput()

def runLineByLine(motifFilename, precisionFactor):
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
        runNextTokensLogicalLine = True
        for eachToken in tokenize.generate_tokens(motifFile.readline):
            if runNextTokensLogicalLine and not tokenize.ISEOF(eachToken[0]):
                printPyMOLState()
                printOutput('Next logical line (starting on line {0}):'.format(eachToken[2][0]))
                # Don't print two newlines
                printOutput(eachToken[4], newLine = (not eachToken[4].endswith('\n')))
                if askYesNo('Run this line now?'):
                    runLine(eachToken[4], precisionFactor)
                else:
                    printOutput('Motif execution terminated early by user.')
                    break
            runNextTokensLogicalLine = (eachToken[0] == tokenize.NEWLINE)
        printOutput('Finished running motif {0} with precision factor {1}.'.format(motifFilename, precisionFactor))
        printPyMOLState()
                
def setup():
    '''This function asks for setup information from the user and then
    runs the selected motif against the selected structure.  Requested
    information includes the path to the motif directory, which motif
    to run, what structure to run it against, and the precision factor
    to feed to the motif.  There are several loops in this function.
    The outer while loop (doAnotherFile) executes as long as the user
    says they want to try another motif, following a (successful or
    unsuccessful) attempt.  The inner while loop near the top
    (readPathAgain) executes until the user selects a valid directory.
    The lower inner while loop (not fileSelected) facilitates a
    multi-page motif menu generated from the file listing in the
    selected directory (written before it became clear a GUI would be
    needed anyway).'''
    printOutput('ProMOL Motif Tester')
    printOutput('By Cyprian Corwin at SBEVSL')
    printOutput('This plugin for PyMOL will run Python-based ProMOL')
    printOutput('motif scripts interactively, line by line, and allow')
    printOutput('the user to see the effects of each line.')
    printOutput('If you just press Enter, yes/no questions will')
    printOutput('default to yes.  Please be careful not to delete or')
    printOutput('edit the prompts or anything on previous lines.')
    
    readPathAgain = True
    doAnotherFile = True
    motifPath = None
    while doAnotherFile:
        
        while readPathAgain:
            motifPath = getInput('Type or paste path to motif library: ')
            if os.path.exists(motifPath):
                motifPath = os.path.realpath(os.path.abspath(motifPath))
                readPathAgain = not os.path.isdir(motifPath)
                if readPathAgain:
                    printOutput('Path was invalid or not a directory.  Please try again.')
        
        # Valid directory found
        rawFilenames = os.listdir(motifPath)
        # Only list valid files
        filenames = filter((lambda file: os.path.isfile(os.path.join(motifPath, file))), rawFilenames)
        if len(filenames) > 0:
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
                    motifToRun = os.path.join(motifPath, groups[groupIndex][int(userInput)])
                    fileSelected = True
            
            # File selected
            # Set up PyMOL context the motif expects
            PDBEntry = getInput('PDB code to run against?')
            printOutput('Attempting to load {0} in PyMOL.'.format(PDBEntry))
            cmd.reinitialize()
            cmd.fetch(PDBEntry, async=0)
            goodFloat = False
            while not goodFloat:
                dString = getInput('Precision factor (as entered in motif finder)?')
                goodFloat = True
                try:
                    precisionFactor = float(dString)
                except ValueError:
                    goodFloat = False
            printOutput('Precision factor \'d\' will be {0}'.format(precisionFactor))
            printOutput('(If this isn\'t what you entered, conversion to floating point failed.)')
            runForSure = askYesNo('Are you sure you want to run {0} now?'.format(motifToRun))
            if runForSure:
                runLineByLine(motifToRun, precisionFactor)
            doAnotherFile = askYesNo('Run another motif?')
            readPathAgain = (not askYesNo('Reuse folder path?')) if doAnotherFile else False
        else:
            printOutput('No files in that directory.')
            doAnotherFile = askYesNo('Try another folder?')
            readPathAgain = doAnotherFile
    
    # Finished
