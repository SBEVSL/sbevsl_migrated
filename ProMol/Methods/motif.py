from pymol import cmd
from pymol import stored
import Tkinter as tk
import Pmw
import os
import re
import time
import math
import tkFileDialog
from shutil import copy
from tkFileDialog import asksaveasfile, askdirectory, askopenfile, askopenfilename
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
from pmg_tk.startup.treewidgets import widget, node, texttree
from pmg_tk.startup.treewidgets.constants import *
import Tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
import pmg_tk.startup.ProMol.load_csa_lit as lib
import pmg_tk.startup.ProMol.Methods.proutils as proutils
import pmg_tk.startup.ProMol.Methods.motifset as motifset
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
pdbsl = 0
Pmw.initialise()

#motif options
def motifoption(tag):
    if tag == 'Surface Pocket':
        surfmotifer()
    elif tag == 'Polar Contacts':
        motifcontact()
    elif tag == 'Hide Contacts':
        hidecontact()
    elif tag == 'Show Substrate':
        showsubstrate()
    elif tag == 'Show label':
        labelmotif()
    elif tag == 'Hide Label':
        dellabel()
    elif tag == 'Hide Substrate':
        hidesubstrate()

#Show binding pocket
def surfmotifer():
    objects = cmd.get_names('all')
    cmd.set('transparency', '0.5', 'all')
    try:
        adjacent = ''
        cmd.show('surface', 'all')
        cmd.hide('cartoon', 'all')
        if 'Adjacent' in objects:
            adjacent = ' and !Adjacent'
        for motif in glb.MOTIFS:
            if motif in objects:
                cmd.color('white', '!%s%s'%(motif,adjacent))
        cpksubstrate()
        cmd.orient('all')
    except:
        showinfo('Alert', 'You must select a motif')

#polar contacts
def motifcontact():
    objects = cmd.get_names('all')
    try:        
        try:
            cmd.dist(mot+"_polar_conts", mot, mot, quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(mot+"_polar_conts")
        except:
            cmd.dist("motif_polar_conts", "motif", "motif", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.dist('Adjacent_polar_conts', 'Adjacent', 'Adjacent',
                quiet = 1, mode = 2, label = 0, reset = 1)
        if 'substrate' in objects:
            cmd.dist(mot+"_around_polar_conts", mot,
                "(byobj ("+mot+")) and (not ("+mot+"))", quiet = 1,
                mode = 2, label = 0, reset = 1)
            cmd.enable(mot+"_around_polar_conts")
    except:
        showinfo('Alert', "Select a motif first")

def hidecontact():
    objects = cmd.get_names('all')
    try:
        try:
            cmd.delete(mot+"_polar_conts")
        except:
            cmd.delete("motif_polar_conts")
        if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
        if 'substrate' in objects:
            cmd.delete(mot+"_around"+"_polar_conts")
    except:
        showinfo('Alert', "No motif polar contacts to hide")

def showsubstrate():
    try:
        try:
            cmd.select('substrate', 'byres het within 7 of '+mot)
            objects = cmd.get_names('all')
            xp = cmd.index('substrate')
            np    = len(xp)
            if(np < 1):
                cmd.delete('substrate')
            if 'substrate' in objects:
                cmd.show('sticks', 'substrate')
                cmd.deselect()
                cpksubstrate()
        except:
            cmd.select('substrate', 'byres het within 7 of motif')
            objects = cmd.get_names('all')
            xp = cmd.index('substrate')
            np    = len(xp)
            if(np < 1):
                cmd.delete('substrate')
            if 'substrate' in objects:
                cmd.show('sticks', 'substrate')
                cmd.deselect()
                cpksubstrate()
    except:
        showinfo('Alert', "No substrate found")

def hidesubstrate():
    try:
        cmd.hide('sticks', 'substrate')
    except:
        showinfo('Alert', "No substrate selected")

#Labels
def dellabel():
    objects = cmd.get_names('all')
    try:
        try:
            cmd.label(mot, "''")
        except:
            cmd.label("motif", "''")
        if 'Adjacent' in objects:
            cmd.label('byres Adjacent', "''")
    except:
        showinfo('Alert', "No motif labels to hide")

def labelmotif():
    objects = cmd.get_names('all')
    try:
        try:
            cmd.label('''(name ca+C1*+C1' and (byres('''+mot+''')))''',
                '''"%s-%s"%(resn, resi)''')
        except:
            cmd.label('''(name ca+C1*+C1' and (byres(motif)))''',
                '''"%s-%s"%(resn, resi)''')
        if 'Adjacent' in objects:
            cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''',
                '''"%s-%s"%(resn, resi)''')
    except:
        showinfo('Alert', "Select a motif first")

def MotifCaller(motif, camera=True):
    path = folder = "C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\Motifs\\"
    d = float(glb.GUI.motifs['delta'].get())
    if camera:
        glb.deletemotif()
        glb.update()
    try:
        #print "here: ",str(glb.MOTIFS[motif]['path'])
        if execfile(glb.MOTIFS[motif]['path']) != False:
        #if execfile(path+motif+".py") != False:
            if (motif not in cmd.get_names('all')) or (cmd.count_atoms(motif) == 0):
                raise Warning
            if camera:
                glb.procolor(motif, show_all='cartoon',color_all='gray')
                cmd.orient(motif)
                cmd.deselect()
        else:
            raise Warning
    except Warning:
        if camera:
            showinfo('Not Found', 'The selected motif did not return a result.')
        print "motif NOT found, return false..."
        return False
    else:
        return True

def changecolor(event):
    color = askcolor(title='Select a Color', color=event.widget['bg'])
    if color[1] != None:
        event.widget['bg'] = color[1]

def togglealign():
    if glb.GUI.motifs['align'].get() == 0:
        glb.GUI.motifs['queryColorLabel'].configure(text='Match Color')
        glb.GUI.motifs['motifColorLabel'].grid_remove()
        glb.GUI.motifs['motifcolor'].grid_remove()
    else:
        glb.GUI.motifs['queryColorLabel'].configure(text='Query Color')
        glb.GUI.motifs['motifColorLabel'].grid()
        glb.GUI.motifs['motifcolor'].grid()


def showContent(node):
  
    '''allows user to click on motif search field items
    and run the motif function'''
    # motifString is raw result string listed in results box
    # motifName is full name of motif found by ProMol
    # However, the atoms in the selection with that name
    # are actually on the query protein because that's
    # what the motifs give us
    # motifPDBCode is PDB code for motif found by ProMol
    # The selection with that name is truly the result protein
    # queryPDBCode is PDB code for query that yielded the result
    # The selection with that name is truly the query protein
    # motifSubsetName is the matching subset of the result protein motifPDBCode
    # motifName is the matching subset of the query protein queryPDBCode

    motif = 1
    motifString = node.getName()
    ancs = node.ancestors()
    querynode = ancs[0]
    
    # The next three ifs added by Kip to prevent crash when double clicking header
    # One might have sufficed unless something unexpected ends up in motifbox
    
    if not motifString.startswith(' '):
        return
    tag = motifString.split(': ')
    if len(tag) != 2:
        return
    motifName = tag[1]
    secondsplit = motifName.split('_')
    if len(secondsplit) < 2:
        return
    motifPDBCode = secondsplit[1] # tpdb
    queryPDBCode = querynode.getName()
        
    cmd.reinitialize()
    motifColor = glb.GUI.motifs['motifcolor']['bg']
    queryColor = glb.GUI.motifs['querycolor']['bg']
    if glb.GUI.motifs['align'].get() == 0 or motifPDBCode == queryPDBCode:
        cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)#accessing pdb file
        if motifName in glb.MOTIFS:
            MotifCaller(motifName)
            
            querySubsetName = 'matching_subset'
            # Actually renames the query protein matching subset
            # because the selection named after the motif contains the matching subset
            # of atoms on the query protein given to us by the motif
            cmd.select(querySubsetName, motifName)
            # I hope this is OK to delete
            cmd.delete(motifName)
            cmd.set_color('matchcolor',
                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
            cmd.color('matchcolor', 'matching_subset')
        else:
            glb.update()
    else:      
        if motifName in glb.MOTIFS:
            cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)
            cmd.hide('everything', 'all')
            
            # Run the motif
            MotifCaller(motifName)
            
            #querySubsetName = 'match_in_{0}'.format(queryPDBCode)
            querySubsetName = 'match_in_%s'%(queryPDBCode)
            # Actually renames the query protein matching subset
            # because the selection named after the motif contains the matching subset
            # of atoms on the query protein given to us by the motif
            cmd.select(querySubsetName, motifName)
            cmd.hide('everything', 'all')
            cmd.fetch(motifPDBCode, async=0, path=glb.FETCH_PATH)
            # Removed cartoon show command
            # Create named subset of matching result protein atoms
            #motifSubsetName = 'match_in_{0}'.format(motifPDBCode)
            motifSubsetName = 'match_in_%s'%(motifPDBCode)
            cmd.select(motifSubsetName, '%s and (%s)' % (motifPDBCode,
                glb.MOTIFS[motifName]['loci']))
            # Do final display
            cmd.hide('everything', 'all')
            cmd.show('sticks', motifSubsetName)
            cmd.show('sticks', querySubsetName)
            # Removed ineffective cmd.color of matching subset

            #aligns and gets the rmsd of the alignment by all atoms
            data1 = cmd.align(motifSubsetName, querySubsetName)#edited 2/19
            cmd.set_color('motifColor',
                ([int(n, 16) for n in (motifColor[1:3], motifColor[3:5], motifColor[5:7])]))
            cmd.set_color('queryColor',
                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
            cmd.color('motifColor', motifPDBCode)
            cmd.color('queryColor', queryPDBCode)
            cmd.orient(motifSubsetName)           

            #added 2/19
            if glb.GUI.motifs['rmsd'].get() != 0:
                print repr(data1[6]) + " residues were aligned and " + repr(data1[1]) + " atoms."
                print "rmsd of the alignment using all atoms = " + repr(data1[0]) #added         
                #aligns and gets the rmsd of the alignment by C alpha atoms
                cmd.select(querySubsetName, motifName+" and name ca")#added
                cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
                glb.MOTIFS[motifName]['loci'], "ca"))#added
                data2 = cmd.align(motifSubsetName, querySubsetName)#added
                print repr(data2[6]) + " residues were aligned and " + repr(data2[1]) + " atoms."
                print "rmsd of the alignment using ca atoms = " + repr(data2[0]) #added

                #aligns and gets the rmsd of the alignment by C alpha and C beta atoms
                cmd.select(querySubsetName, motifName+" and name ca,cb")#edited
                cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
                glb.MOTIFS[motifName]['loci'], "ca,cb"))#edited
                data3 = cmd.align(motifSubsetName, querySubsetName)#edited
                print repr(data3[6]) + " residues were aligned and " + repr(data3[1]) + " atoms."
                print "rmsd of the alignment using ca and cb atoms = " + repr(data3[0]) #added
            ###

    
            
            # I hope this is OK to delete
            cmd.delete(motifName)
            # Added by Kip to show both proteins in subsets
            glb.populate()

def exportAllResults():
    defaultfile = fullCSVFilename(CSVMergeInfo['motif set short description'], CSVMergeInfo['start time'])
    #with asksaveasfile(initialfile=defaultfile, defaultextension='.csv', filetypes=[('Comma Separated Value files','*.csv'), ('All files','*.*')], title='Export Motif Finder Results As...') as outhandle:
    outhandle =  asksaveasfile(initialfile=defaultfile, defaultextension='.csv', filetypes=[('Comma Separated Value files','*.csv'), ('All files','*.*')], title='Export Motif Finder Results As...')
    try:
        outhandle.__enter__()
        firstFile = True # include the first header only
        for partialCSVFile in CSVMergeInfo['partial files']:

            #with open(os.path.join(glb.CSV_PATH, partialCSVFile), 'rU') as inhandle:
            inhandle =  open(os.path.join(glb.CSV_PATH, partialCSVFile), 'rU')
            try:
                inhandle.__enter__()
                lineIndex = 0
                for eachLine in inhandle:
                    lineIndex = lineIndex + 1
                    if firstFile or (lineIndex > INDIVIDUAL_CSV_HEADER_LENGTH):
                       outhandle.write(eachLine)
            finally:
                inhandle.__exit__()
            firstFile = False
            outhandle.write('\n\n')

    finally:
        outhandle.__exit__()

def motifcancel():
    glb.GUI.motifs['cancel'] = True

def storeSetChoice(): #stores button value, action of the select button
    glb.GUI.motifs['root'].withdraw()
    selectedSet = glb.GUI.motifs['var'].get()
    rmsdchoice = glb.GUI.motifs['varrmsd'].get()
    motifchecker(selectedSet, rmsdchoice)

def cancelSetChoice():#action of the cancel button
    glb.GUI.motifs['root'].withdraw()
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL

def setChoiceDialogBox(): #creates buttons on the dialog box that pops up when the user selects the start button in motif finder
    pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
    global pdbsl
    pdbsl = len(pdbs)
    if pdbsl == 1 and pdbs[0] == '':#moved from motifchecker
        showerror('No PDB Entered',"Enter a PDB or a comma separated list of PDB's to search")
        glb.GUI.motifs['delta']['state'] = tk.NORMAL
        glb.GUI.motifs['findmotif']['state'] = tk.NORMAL
        glb.GUI.motifs['multipdb']['state'] = tk.NORMAL
        glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
        return False

    glb.GUI.motifs['findmotif']['state'] = tk.DISABLED

    for w in glb.GUI.motifs['root'].children.values():
        w.destroy()
   
    glb.GUI.motifs['var'] = IntVar()

    #added 2/19
    glb.GUI.motifs['varrmsd'] = IntVar()
    ###
    
    rb1 = Radiobutton(glb.GUI.motifs['root'], text="P set", variable = glb.GUI.motifs['var'], value = 1,  height = 2)
    rb2 = Radiobutton(glb.GUI.motifs['root'], text="J set", variable = glb.GUI.motifs['var'], value = 2, height = 2)
    #rb3 = Radiobutton(glb.GUI.motifs['root'], text="N set (NMR)", variable = glb.GUI.motifs['var'], value = 3, height = 2)
    rb4 = Radiobutton(glb.GUI.motifs['root'], text="All Motifs", variable = glb.GUI.motifs['var'], value = 4, height = 2)
    rb5 = Radiobutton(glb.GUI.motifs['root'], text="User Motifs", variable = glb.GUI.motifs['var'], value = 5, height = 2)

    #added 2/19
    rb6 = Radiobutton(glb.GUI.motifs['root'], text="Yes (will take longer)", variable = glb.GUI.motifs['varrmsd'], value = 1,  height = 2)
    rb7 = Radiobutton(glb.GUI.motifs['root'], text="No", variable = glb.GUI.motifs['varrmsd'], value = 2, height = 2)

    spacelabel = Label(glb.GUI.motifs['root'], text="")
    rmsdlabel = Label(glb.GUI.motifs['root'], text="Calculate RMSD?")
    ###




    rb4.pack(anchor = W)
    rb4.select()#added 2/19 (default button)
    rb5.pack(anchor = W)
    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    #rb3.pack(anchor = W)

    #added 2/19
    spacelabel.pack(anchor = W)
    rmsdlabel.pack(anchor = W)
    rb6.pack(anchor = W)
    rb7.pack(anchor = W)
    rb7.select()
    ###
    
    frame = Frame(glb.GUI.motifs['root'], width=200, height=250, bd=1)
    frame.pack()
    
    selectButton = Button(frame, text='Select', command = storeSetChoice).pack()
    cancelButton = Button(frame, text='Cancel', command = cancelSetChoice).pack()
    glb.GUI.motifs['root'].update()
    glb.GUI.motifs['root'].deiconify()
    glb.GUI.motifs['root'].mainloop()

# Creates a horizontal line suitable for CSV export
def headerFromCharacter(character, delimiter=',', columnwidth=10, columns=8):
    return ('"' + character*columnwidth + '"' + delimiter) * columns
    
# The same as split() but leaves portions enclosed in quotes intact
# I originally wrote this with the default delimiter as a comma
# but changed it to be more in line with the standard split() method
# of strings
def splitRespectingQuotes(inputString, delimiter=' ', quote='"'):
    resultList = []
    insideQuotes = False
    # The next block starts at one position after the last splittable comma
    # The first block starts at 0 (= -1 + 1)
    lastCommaOutsideQuotes = -1
    commaIndex = inputString.find(delimiter)
    quoteIndex = inputString.find(quote)
    # Iterate while there's something left to find
    while (commaIndex > -1) or (quoteIndex > -1):
        # Find the leftmost comma or quote if both are present;
        # if not, take the one that's not -1
        # At least one of them isn't
        currentPointOfInterest = min(commaIndex, quoteIndex) if min(commaIndex, quoteIndex) > -1 else max(commaIndex, quoteIndex)
        # Next point of interest is not -1 because loop condition would have been false
        if inputString[currentPointOfInterest] == quote:
            # Toggle whether we split on the following comma(s)
            insideQuotes = not insideQuotes
        else:
            assert inputString[currentPointOfInterest] == delimiter
            if not insideQuotes:
                # Split
                # The resulting token shouldn't include either the last comma or this one
                # The start point of a slice is included but the end point is not
                resultList.append(inputString[(lastCommaOutsideQuotes + 1):currentPointOfInterest])
                lastCommaOutsideQuotes = currentPointOfInterest
        # Prepare for next loop iteration
        commaIndex = inputString.find(delimiter, currentPointOfInterest + 1)
        quoteIndex = inputString.find(quote, currentPointOfInterest + 1)
    # After loop finishes, add the rest of the string as the last token
    resultList.append(inputString[(lastCommaOutsideQuotes + 1):])
    return resultList

# Exports the CSV file for a single query protein
# motifSet must be a MotifSet object, not a native Python set
# resultdb should usually be glb.GUI.motifs['csvprep'][pdb]
def exportCSVResults(searchStartTime, precisionFactor, motifSet, pdb, found, resultdb, rmsdState):
    # Export CSV file automatically
    # Include the algorithm version now, as well
    # This pulls it from promolglobals.py, which in turn pulls it from version.py
    # The motif set name is on a line by itself because future versions may someday
    # include long descriptions for custom motif sets
    # There is a blank column between long strings in the header so that
    # the user, if they want to, can shrink the columns and there will be
    # room for the strings to span multiple columns if their spreadsheet
    # software supports it.

    #edited 2/19 (RMSDs in header added)
    #csv = ['Motif Finder Results,,Generated by ProMOL version {0}'.format(glb.VERSION),
    #'Search started at {0},,Precision factor: {1},,Algorithm version: {2}'.format(time.asctime(searchStartTime), precisionFactor, glb.ALG_VERSION),
    #'"Motif set: {0}"'.format(motifSet.longDescription),
    csv = ['Motif Finder Results,,Generated by ProMOL version %s'%(glb.VERSION),
    'Search started at %s,,Precision factor: %s,,Algorithm version: %s'%(time.asctime(searchStartTime), precisionFactor, glb.ALG_VERSION),
    '"Motif set: %s"'%(motifSet.longDescription),
    headerFromCharacter('='),
    'PDB Entry,Motifs Found,Edit Distance Range, RMSD ALL, RMSD CA & CB, RMSD CA, Residues,,,,Motifs Not Found',
    ',,,,,,Chain,Name,Number',
    headerFromCharacter('=')]
    pdbMotifs = set()
    allMotifs = motifSet.motifs
    lastpdb = None
    # Changed from 2. -Kip
    fillFrom = INDIVIDUAL_CSV_HEADER_LENGTH
    # The following loop iterates once for each motif found
    for result in found:
        # This should no longer fail regularly because query PDB entry
        # headers are no longer in the mix.  I removed the try because
        # I want to know if something goes wrong. -Kip
        motif = result.split(': ')[1]
        
        ldr = resultdb[motif]['levdistrange']

        #added 2/19
        if rmsdState == True:
            motifrmsds = resultdb[motif]['rmsd']
        else:
            motifrmsds = [-1,-1,-1]
        ###


        
        # Remove precision factor from every PDB entry listing.
        # It is the same for all of them. -Kip

        # Homologue functionality was unimplemented and was wasting
        # an entire column in the CSV, so I removed it. -Kip

        residues = resultdb[motif]['res']
        same = {}
        motifline = True
        for residue in residues:
            chain = residue[0]
            resn = residue[1]
            resi = residue[2]
            key = '%s%s'%(resn,resi)
            if key in same:
                line = same[key]
                s = splitRespectingQuotes(csv[line], ',')
                # Strip out any existing quotes around the chain list
                # (to avoid adding them again)
                # I think there will be quotes if there is more than one
                # chain in the list
                csv[line] = '%s,%s,%s,"%s, %s",%s,%s'%(s[0],s[1],s[2],s[3].strip('"'),chain,s[4],s[5])
                continue
            same[key] = len(csv)
            if lastpdb != pdb:
                #edited 2/19
                csv.append('%s,%s,"%s","%s","%s","%s",%s,%s,%s'%(pdb,motif,ldr,round(motifrmsds[0],4),round(motifrmsds[1],4),round(motifrmsds[2],4),chain,resn,resi))
                lastpdb = pdb
                motifline = False
                continue
            if motifline:
                #edited 2/19
                csv.append(',%s,"%s","%s","%s","%s",%s, %s,%s'%(motif,ldr,round(motifrmsds[0],4),round(motifrmsds[1],4),round(motifrmsds[2],4),chain,resn,resi))
                motifline = False
                continue
            csv.append(',,,,,,%s,%s,%s'%(chain,resn,resi))
        pdbMotifs.add(motif)
    # Fix for if there are absolutely no matches: make room for not found list
    # Before I rewrote the bigger loop it created an infinite loop because pdbfnl
    # (the not found list loop index) was never incremented, causing ProMol to hang
    # because the inner lines for loop was never run (fillFrom and len(csv) were both 2)
    # That for loop is now gone; now, without this while loop, it would cause
    # an IndexError instead (csv[2] with csv of length 2) -Kip
    notFoundList = list(allMotifs - pdbMotifs) # motifs not found for this structure = all motifs - motifs found for this structure
    notFoundList.sort()
    while len(csv) < fillFrom + min(20, len(notFoundList)):
        csv.append(',,,,,')
    line = fillFrom
    wrapped = False
    for notFoundMotif in notFoundList: # Add motifs not found for this structure
        if (line >= len(csv)): # Start over at the top
            line = fillFrom
            wrapped = True
            # Extend headers
            csv[3] += headerFromCharacter('=', columns=1)
            csv[6] += headerFromCharacter('=', columns=1)
        if not wrapped:
            csv[line] += ',' # Don't spread out the results to the right so much if they wrap
        #csv[line] += ',{0}'.format(notFoundMotif)
        csv[line] += ',%s'%(notFoundMotif)
        line += 1

    csvfile = "\n".join(csv)
    #with open(os.path.join(glb.CSV_PATH, partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime)), 'w') as csvhandle:
    csvhandle = open(os.path.join(glb.CSV_PATH, partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime)), 'w')
    try:
        csvhandle.__enter__() 
        csvhandle.write(csvfile)
    finally:
        csvhandle.__exit__()

# Create uniform timestamp for CSV filenames
def generateCSVTimeString(searchStartTime):
    return time.strftime('%b_%d_%Y_%H%M_%Z', searchStartTime)

# Create appropriate filenames for CSV files
def partialCSVFilename(pdb, motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    #return 'motiffinder_partial_{0}_{1}_{2}.csv'.format(pdb, motifSetName, stamp)
    return 'motiffinder_partial_%s_%s_%s.csv'%(pdb, motifSetName, stamp)

def fullCSVFilename(motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    #return 'motiffinder_{0}_{1}.csv'.format(motifSetName, stamp)
    return 'motiffinder_%s_%s.csv'%(motifSetName, stamp)

def count(motif,pdb):
    #print motif ### !!!
    last = None
    ordered = []
    orderedchain = {}
    bannedchain = []
    stored.motif = []
    editdist = []
    
    cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
    #print stored.motif ### !!!
    residues = glb.MOTIFS[motif]['resi']
    #print residues ### !!!
    residuesl = len(residues)*2
    glb.GUI.motifs['csvprep'][pdb][motif] = {}
    glb.GUI.motifs['csvprep'][pdb][motif]['res'] = []
    count = 1 ### !!!
    for iteration in stored.motif:
        #print 'iteration ', count, ' : ', iteration ### !!!
        count += 1 ### !!!
        if last != iteration:
            last = iteration
            glb.GUI.motifs['csvprep'][pdb][motif]['res'].append(iteration)
            ordered.append(iteration[1].lower())
            if iteration[0] not in orderedchain:
                if iteration[0] not in bannedchain:
                    orderedchain[iteration[0]] = []
                else:
                    continue
            orderedchain[iteration[0]].append(iteration[1].lower())
            if residuesl <= len(orderedchain[iteration[0]]):
                bannedchain.append(iteration[0])
                del orderedchain[iteration[0]]
    if len(orderedchain) == 0 and residuesl <= len(ordered):
        return None
    substitutions = [None]
    if motif[0] == 'J':
        for c in ('asp','glu','asn','gln','thr','ser'):
            if c in residues:
                substitutions = proutils.createsubs(residues)
                break
    for chain in orderedchain:
        editdist.append(proutils.levenshteinDistance(residues,orderedchain[chain]))
        for sub in substitutions:
            if sub == None:
                break
            editdist.append(proutils.levenshteinDistance(sub,orderedchain[chain]))
    editdist.append(proutils.levenshteinDistance(residues,ordered))
    for sub in substitutions:
        if sub == None:
            break
        editdist.append(proutils.levenshteinDistance(sub,ordered))
    mini = min(editdist)
    maxi = max(editdist)
    #glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
    glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '%s-%s'%(mini,maxi) if mini<maxi else mini
    # Removed storage of precision factor as it is the same for the entire search
    return glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange']

def automateMotifChecker():

    filelist_n0 = ["U_132l_3_2_1_17.py",
                "U_135l_3_2_1_17.py",
                "U_1lz1_3_2_1_17.py"]
    
    filelist_n0_1 = ["U_1a4s_1_2_1_8.py"]

    filelist_n1 = ["U_132l_3_2_1_17.py",
                "U_135l_3_2_1_17.py",
                "U_1lz1_3_2_1_17.py",
                "U_2eql_3_2_1_17.py",
                "U_1a0j_3_4_21_4.py",
                "U_1a4s_1_2_1_8.py",
                "U_1a50_4_2_1_20.py",
                "U_1a65_1_10_3_2.py",
                "U_1a69_2_4_2_1.py",
                "U_1a7u_1_11_1_10.py",
                "U_1a8q_1_11_1_10.py",
                "U_1a8s_1_11_1_10.py",
                "U_1a95_2_4_2_22.py",
                "U_1aam_2_6_1_1.py",
                "U_1abr_3_2_2_22.py",
                "U_1afr_1_14_19_2.py",
                "U_1afw_2_3_1_16.py",
                "U_1agy_3_1_1_-.py",
                "U_1aj0_2_5_1_15.py",
                "U_1aj8_4_1_3_7.py",
                "U_1akd_1_14_15_1.py",
                "U_1akm_2_1_3_3.py",
                "U_1ako_3_1_11_2.py",
                "U_1ald_4_1_2_13.py",
                "U_1alk_3_1_3_1.py",
                "U_1am2_5_99_1_3.py",
                "U_1am5_3_4_23_1.py",
                "U_1amy_3_2_1_1.py",
                "U_1apt_3_4_23_20.py",
                "U_1apx_1_11_1_11.py",
                "U_1aq0_3_2_1_73.py",
                "U_1aq2_4_1_1_49.py",
                "U_1aql_3_1_1_13.py",
                "U_1arz_1_3_1_26.py",
                "U_1aui_3_1_3_16.py",
                "U_1auo_3_1_1_1.py",
                "U_1ay4_2_6_1_57.py",
                "U_1azw_3_4_11_5.py",
                "U_1azy_2_4_2_4.py",
                "U_1b02_2_1_1_45.py",
                "U_1b2m_3_1_27_3.py",
                "U_1b5d_2_1_2_8.py",
                "U_1b65_3_4_11_19.py",
                "U_1b6g_3_8_1_5.py",
                "U_1b6t_2_7_7_3.py",
                "U_1b73_5_1_1_3.py",
                "U_1b8g_4_4_1_14.py",
                "U_1b93_4_2_3_3.py",
                "U_1bbs_3_4_23_15.py",
                "U_1be1_5_4_99_1.py"]
    filelist_n2 = ["U_1bf2_3_2_1_68.py",
                "U_1bg0_2_7_3_3.py",
                "U_1bg6_1_5_1_28.py",
                "U_1bhg_3_2_1_31.py",
                "U_1bmt_2_1_1_13.py",
                "U_1bol_3_1_27_1.py",
                "U_1boo_2_1_1_113.py",
                "U_1bp2_3_1_1_4.py",
                "U_1bqc_3_2_1_78.py",
                "U_1brm_1_2_1_11.py",
                "U_1bs0_2_3_1_47.py",
                "U_1bs9_3_1_1_6.py",
                "U_1bsj_3_5_1_88.py",
                "U_1btl_3_5_2_6.py",
                "U_1bvv_3_2_1_8.py",
                "U_1bwd_2_1_4_2.py",
                "U_1bwz_5_1_1_7.py",
                "U_1bzc_3_1_3_48.py",
                "U_1c2t_2_1_2_2.py",
                "U_1c4x_3_7_1_8.py",
                "U_1c82_4_2_2_1.py",
                "U_1c9u_1_1_5_2.py",
                "U_1ca3_4_2_1_1.py",
                "U_1cb8_4_2_2_5.py",
                "U_1cbg_3_2_1_21.py",
                "U_1cd5_3_5_99_6.py",
                "U_1cde_2_1_2_2.py",
                "U_1cdg_2_4_1_19.py",
                "U_1cel_3_2_1_91.py",
                "U_1cf2_1_2_1_59.py",
                "U_1cg2_3_4_17_11.py",
                "U_1cgk_2_3_1_74.py",
                "U_1chd_3_1_1_61.py",
                "U_1ci8_3_1_1_1.py",
                "U_1cm0_7_0_0_0.py",
                "U_1cms_3_4_23_4.py",
                "U_1cns_3_2_1_14.py",
                "U_1coy_1_1_3_6.py",
                "U_1cqg_4_2_99_18.py",
                "U_1cqq_2_7_7_48.py",
                "U_1ct9_6_3_5_4.py",
                "U_1ctn_3_2_1_14.py",
                "U_1cv2_3_8_1_5.py",
                "U_1cvr_3_4_22_37.py",
                "U_1cwy_2_4_1_25.py",
                "U_1d1q_3_1_3_2.py",
                "U_1d2t_3_1_3_2.py",
                "U_1d4c_1_3_99_1.py",
                "U_1d5r_3_1_3_67.py"]
    filelist_n3 = ["U_1d6m_5_99_1_2.py",
                "U_1d6o_5_2_1_8.py",
                "U_1d7r_4_1_1_64.py",
                "U_1d8c_2_3_3_9.py",
                "U_1d8h_3_1_3_33.py",
                "U_1daa_2_6_1_21.py",
                "U_1dae_6_3_3_3.py",
                "U_1db3_4_2_1_47.py",
                "U_1dbt_4_1_1_23.py",
                "U_1dd8_2_3_1_41.py",
                "U_1de3_3_1_27_10.py",
                "U_1de6_5_3_1_14.py",
                "U_1dhp_4_2_1_52.py",
                "U_1dhr_1_5_1_34.py",
                "U_1di1_4_2_3_9.py",
                "U_1djl_1_6_1_2.py",
                "U_1dki_7_0_0_0.py",
                "U_1dli_1_1_1_22.py",
                "U_1dnk_3_1_21_1.py",
                "U_1dpg_1_1_1_49.py",
                "U_1dub_4_2_1_17.py",
                "U_1dve_1_14_99_3.py",
                "U_1dxe_4_1_2_20.py",
                "U_1dzr_5_1_3_13.py",
                "U_1e2a_2_7_1_69.py",
                "U_1e2t_2_3_1_118.py",
                "U_1e3v_5_3_3_1.py",
                "U_1eag_3_4_23_24.py",
                "U_1ebf_1_1_1_3.py",
                "U_1ec9_4_2_1_40.py",
                "U_1ecf_2_4_2_14.py",
                "U_1ecl_5_99_1_2.py",
                "U_1ecx_7_0_0_0.py",
                "U_1eed_3_4_23_22.py",
                "U_1eej_5_3_4_1.py",
                "U_1ef8_4_1_1_41.py",
                "U_1eh5_3_1_2_22.py",
                "U_1eh6_2_1_1_63.py",
                "U_1ei5_3_4_11_19.py",
                "U_1eix_4_1_1_23.py",
                "U_1elq_7_0_0_0.py",
                "U_1els_4_2_1_11.py",
                "U_1emd_1_1_1_37.py",
                "U_1eq2_5_1_3_20.py",
                "U_1esc_3_1_1_-.py",
                "U_1evy_1_1_1_8.py",
                "U_1exp_3_2_1_8.py",
                "U_1eyi_3_1_3_11.py",
                "U_1eyp_5_5_1_6.py"]
    filelist_n4 = ["U_1f2d_4_1_99_4.py",
                "U_1f7u_6_1_1_19.py",
                "U_1f8m_4_1_3_1.py",
                "U_1fcb_1_1_2_3.py",
                "U_1fcq_3_2_1_35.py",
                "U_1fdy_4_1_3_3.py",
                "U_1fgh_4_2_1_3.py",
                "U_1fhl_3_2_1_89.py",
                "U_1fnb_1_18_1_2.py",
                "U_1fob_3_2_1_89.py",
                "U_1foh_1_14_13_7.py",
                "U_1fr8_2_4_1_38.py",
                "U_1fy2_3_4_13_21.py",
                "U_1g0d_2_3_2_13.py",
                "U_1g6t_2_5_1_19.py",
                "U_1g99_2_7_2_1.py",
                "U_1ga8_2_4_1_44.py",
                "U_1gal_1_1_3_4.py",
                "U_1gcb_3_4_22_40.py",
                "U_1gcu_1_3_1_24.py",
                "U_1gdh_1_1_1_29.py",
                "U_1geq_4_2_1_20.py",
                "U_1gim_6_3_4_4.py",
                "U_1glo_3_4_22_27.py",
                "U_1gog_1_1_3_9.py",
                "U_1gox_1_1_3_15.py",
                "U_1gpr_2_7_1_69.py",
                "U_1gq8_3_1_1_11.py",
                "U_1grc_2_1_2_2.py",
                "U_1gz6_1_1_1_35.py",
                "U_1h7o_4_2_1_24.py",
                "U_1hfs_3_4_24_17.py",
                "U_1hka_2_7_6_3.py",
                "U_1hpl_3_1_1_3.py",
                "U_1hrk_4_99_1_1.py",
                "U_1hxq_2_7_7_12.py",
                "U_1hy3_2_8_2_4.py",
                "U_1hzd_4_1_2_18.py",
                "U_1hzf_3_4_21_43.py",
                "U_1i78_3_4_21_87.py",
                "U_1inp_3_1_3_57.py",
                "U_1iph_1_11_1_6.py",
                "U_1j49_1_1_1_28.py",
                "U_1j7g_3_1_-_-.py",
                "U_1jdw_2_1_4_1.py",
                "U_1jh6_3_1_4_-.py",
                "U_1jkm_7_0_0_0.py",
                "U_1jof_5_5_1_5.py",
                "U_1k30_2_3_1_15.py",
                "U_1k32_3_4_21_-.py",
                "U_1kas_2_3_1_41.py"]
    filelist_n5 = ["U_1kfu_3_4_22_53.py",
                "U_1kfx_3_4_22_53.py",
                "U_1kp2_6_3_4_5.py",
                "U_1kra_3_5_1_5.py",
                "U_1kzh_2_7_1_90.py",
                "U_1kzl_2_5_1_9.py",
                "U_1l1l_1_17_4_2.py",
                "U_1l6p_1_8_1_8.py",
                "U_1l7q_3_1_1_1.py",
                "U_1l9x_3_4_19_9.py",
                "U_1lam_3_4_11_1.py",
                "U_1lcb_2_1_1_45.py",
                "U_1ldm_1_1_1_27.py",
                "U_1ljl_1_20_4_1.py",
                "U_1m53_5_4_99_11.py",
                "U_1mbb_1_1_1_158.py",
                "U_1mek_5_3_4_1.py",
                "U_1mka_4_2_1_60.py",
                "U_1mla_2_3_1_39.py",
                "U_1moq_2_6_1_16.py",
                "U_1mpp_3_4_23_23.py",
                "U_1mpx_3_1_1_43.py",
                "U_1mpy_1_13_11_2.py",
                "U_1mrq_1_3_1_20.py",
                "U_1muc_5_5_1_1.py",
                "U_1myr_3_2_3_1.py",
                "U_1naa_1_1_99_18.py",
                "U_1nba_3_5_1_59.py",
                "U_1nln_3_4_22_39.py",
                "U_1nlu_3_4_21_100.py",
                "U_1nmw_5_2_1_8.py",
                "U_1nu3_3_3_2_8.py",
                "U_1nw9_7_0_0_0.py",
                "U_1nww_3_3_2_8.py",
                "U_1nzy_3_8_1_6.py",
                "U_1odt_3_1_1_41.py",
                "U_1ofg_1_1_99_28.py",
                "U_1og1_2_4_2_31.py",
                "U_1ok4_4_1_2_13.py",
                "U_1onr_2_2_1_2.py",
                "U_1opm_1_14_17_3.py",
                "U_1ord_4_1_1_17.py",
                "U_1otg_5_3_3_10.py",
                "U_1oya_1_6_99_1.py",
                "U_1oyg_2_4_1_10.py",
                "U_1p4n_2_3_2_10.py",
                "U_1p7m_3_2_2_20.py",
                "U_1pa9_3_1_3_48.py",
                "U_1pad_3_4_22_2.py",
                "U_1pd2_5_3_99_2.py"]
    filelist_n6 = ["U_1pfq_3_4_14_5.py",
                "U_1pgs_3_5_1_52.py",
                "U_1pii_4_1_1_48.py",
                "U_1pja_3_1_2_22.py",
                "U_1pjb_1_4_1_1.py",
                "U_1pjh_5_3_3_8.py",
                "U_1pkn_2_7_1_40.py",
                "U_1pnl_3_5_1_11.py",
                "U_1pnt_3_1_3_2.py",
                "U_1pow_1_2_3_3.py",
                "U_1pp4_3_1_1_-.py",
                "U_1ps9_1_3_1_34.py",
                "U_1ptd_4_6_1_13.py",
                "U_1pyl_3_1_4_8.py",
                "U_1pym_5_4_2_9.py",
                "U_1qam_2_1_1_48.py",
                "U_1qaz_3_5_1_45.py",
                "U_1qba_3_2_1_52.py",
                "U_1qe3_3_1_1_-.py",
                "U_1qfe_4_2_1_10.py",
                "U_1qfm_3_4_21_26.py",
                "U_1qfn_1_17_4_1.py",
                "U_1qgn_4_2_99_9.py",
                "U_1qhf_5_4_2_1.py",
                "U_1qho_3_2_1_133.py",
                "U_1qk2_3_2_1_91.py",
                "U_1qq5_3_8_1_2.py",
                "U_1qrz_3_4_21_7.py",
                "U_1qx3_3_4_22_-.py",
                "U_1r4z_3_1_1_3.py",
                "U_1ra2_1_5_1_3.py",
                "U_1rba_4_1_1_39.py",
                "U_1rk2_2_7_1_15.py",
                "U_1rne_3_4_23_15.py",
                "U_1rpt_3_1_3_2.py",
                "U_1rpx_5_1_3_1.py",
                "U_1rql_7_0_0_0.py",
                "U_1rtf_3_4_21_68.py",
                "U_1rtu_3_1_27_4.py",
                "U_1s3i_1_5_1_6.py",
                "U_1s9c_4_2_1_-.py",
                "U_1sca_3_4_21_62.py",
                "U_1ses_6_1_1_11.py",
                "U_1smn_3_1_30_2.py",
                "U_1snn_5_4_99_-.py",
                "U_1snz_5_1_3_3.py",
                "U_1stc_2_7_1_37.py",
                "U_1std_4_2_1_94.py",
                "U_1szd_3_5_1_-.py",
                "U_1szj_1_2_1_12.py"]
    filelist_n7 = ["U_1tah_3_1_1_3.py",
                "U_1tde_1_8_1_9.py",
                "U_1teh_1_1_1_1.py",
                "U_1thg_3_1_1_3.py",
                "U_1tht_2_3_1_-.py",
                "U_1tph_5_3_1_1.py",
                "U_1tyf_3_4_21_92.py",
                "U_1tys_2_1_1_45.py",
                "U_1tz3_3_6_1_26.py",
                "U_1u5u_4_2_1_92.py",
                "U_1uae_2_5_1_7.py",
                "U_1uag_6_3_2_9.py",
                "U_1uch_3_4_19_12.py",
                "U_1uf7_3_5_1_77.py",
                "U_1uk7_3_7_1_9.py",
                "U_1un1_2_4_1_207.py",
                "U_12as_6_3_1_1.py",
                "U_1uok_3_2_1_10.py",
                "U_1v0e_3_2_1_129.py",
                "U_1v0y_3_1_4_4.py",
                "U_1vao_1_1_3_38.py",
                "U_1vas_3_1_25_1.py",
                "U_1vie_1_5_1_3.py",
                "U_1vom_7_0_0_0.py",
                "U_1vr7_4_1_1_50.py",
                "U_1vzz_5_3_3_1.py",
                "U_1wd8_3_5_3_15.py",
                "U_1wnw_1_14_99_3.py",
                "U_1x9y_3_4_22_-.py",
                "U_1xqw_3_4_11_5.py",
                "U_1xtc_2_4_2_36.py",
                "U_1xyz_3_2_1_8.py",
                "U_1ybv_1_1_1_252.py",
                "U_1ysc_3_4_16_5.py",
                "U_1ytw_3_1_3_48.py",
                "U_1z9h_5_3_99_3.py",
                "U_1zio_2_7_4_3.py",
                "U_1zoi_3_1_-_-.py",
                "U_1zrz_2_7_1_37.py",
                "U_1zym_2_7_3_9.py",
                "U_2a86_6_3_2_1.py",
                "U_2abk_4_2_99_18.py",
                "U_2ace_3_1_1_7.py",
                "U_2acy_3_6_1_7.py",
                "U_2adm_2_1_1_72.py",
                "U_2apr_3_4_23_21.py"]
    filelist_n8 = ["U_2ayh_3_2_1_73.py",
                "U_2bif_3_1_3_46.py",
                "U_2bkr_3_4_22_-.py",
                "U_2bx4_2_7_7_48.py",
                "U_2cnd_1_7_1_1.py",
                "U_2cpo_1_11_1_10.py",
                "U_2cpu_3_2_1_1.py",
                "U_2dhn_4_1_2_25.py",
                "U_2dln_6_3_2_4.py",
                "U_2ebn_3_2_1_96.py",
                "U_2f61_3_2_1_45.py",
                "U_2f9z_3_1_1_61.py",
                "U_2gsa_5_4_3_8.py",
                "U_2hgs_6_3_2_3.py",
                "U_2isd_3_1_4_11.py",
                "U_2jcw_1_15_1_1.py",
                "U_2jxr_3_4_23_25.py",
                "U_2lip_3_1_1_3.py",
                "U_2nac_1_2_1_2.py",
                "U_2nmt_2_3_1_97.py",
                "U_2pda_1_2_7_1.py",
                "U_2pfl_2_3_1_54.py",
                "U_2phk_2_7_1_38.py",
                "U_2pia_1_-_-_-.py",
                "U_2plc_4_6_1_13.py",
                "U_2pth_3_1_1_29.py",
                "U_2rnf_3_1_-_-.py",
                "U_2thi_2_5_1_2.py",
                "U_2tmd_1_5_8_2.py",
                "U_2tps_2_5_1_3.py",
                "U_2xis_5_3_1_5.py",
                "U_2ypn_2_5_1_61.py",
                "U_3cla_2_3_1_28.py",
                "U_3csm_5_4_99_5.py",
                "U_3eca_3_5_1_1.py",
                "U_3nos_1_14_13_39.py",
                "U_3pva_3_5_1_11.py",
                "U_5cox_1_14_99_1.py",
                "U_5enl_4_2_1_11.py",
                "U_5fit_3_6_1_29.py",
                "U_5rsa_3_1_27_5.py",
                "U_7odc_4_1_1_17.py",
                "U_8pch_3_4_22_16.py"]

    filelist_p1_1 = ["P_1chd_3_1_1_61.py"]

    filelist_p1 = ["P_12as_6_3_1_1.py",
            "P_1a2f_1_11_1_5.py",
            "P_1a30_3_1_26_4.py",
            "P_1a9t_2_4_2_1.py",
            "P_1afr_1_14_19_2.py",
            "P_1ahy_2_6_1_1.py",
            "P_1ajo_3_2_1_73.py",
            "P_1ajz_2_5_1_15.py",
            "P_1ak9_3_4_21_62.py",
            "P_1ako_3_1_11_2.py",
            "P_1apy_3_5_1_26.py",
            "P_1aug_3_4_19_3.py",
            "P_1aur_3_1_1_1.py",
            "P_1aw5_4_2_1_24.py",
            "P_1b0p_1_2_7_1.py",
            "P_1b31_3_2_1_8.py",
            "P_1b3r_3_3_1_1.py",
            "P_1b73_5_1_1_3.py",
            "P_1bcs_3_4_16_6.py",
            "P_1bgg_3_2_1_21.py",
            "P_1bk7_3_1_27_1.py",
            "P_1brl_1_14_14_3.py",
            "P_1bwr_3_1_1_47.py",
            "P_1c1h_4_99_1_1.py",
            "P_1c8v_4_2_1_20.py",
            "P_1cf3_1_1_3_4.py",
            "P_1cg4_6_3_4_4.py",
            "P_1chd_3_1_1_61.py",
            "P_1cns_3_2_1_14.py",
            "P_1cnz_1_1_1_85.py",
            "P_1csi_2_3_3_1.py",
            "P_1cy8_5_99_1_2.py",
            "P_1d5l_1_11_1_7.py",
            "P_1d8h_3_1_3_33.py",
            "P_1daa_2_6_1_21.py",
            "P_1dah_6_3_3_3.py",
            "P_1dbr_2_4_2_22.py",
            "P_1dcp_4_2_1_96.py",
            "P_1dd8_2_3_1_41.py",
            "P_1de5_5_3_1_14.py",
            "P_1dg9_3_1_3_2.py",
            "P_1diz_3_2_2_21.py",
            "P_1dj9_2_3_1_47.py",
            "P_1djq_1_5_8_2.py"]
    filelist_p2 = ["P_1dlu_2_3_1_9.py",
            "P_1dvj_4_1_1_23.py",
            "P_1e2m_2_7_1_21.py",
            "P_1e7d_3_1_22_4.py",
            "P_1ecg_2_4_2_14.py",
            "P_1egv_4_2_1_28.py",
            "P_1ei9_3_1_2_22.py",
            "P_1ez2_3_1_8_1.py",
            "P_1ezr_3_2_2_1.py",
            "P_1f17_1_1_1_35.py",
            "P_1f61_4_1_3_1.py",
            "P_1f6d_5_1_3_14.py",
            "P_1fm7_5_5_1_6.py",
            "P_1foh_1_14_13_7.py",
            "P_1fp8_2_4_1_25.py",
            "P_1frz_3_5_99_6.py",
            "P_1ftq_2_4_1_1.py",
            "P_1fva_1_8_4_6.py",
            "P_1fwa_3_5_1_5.py",
            "P_1g99_2_7_2_1.py",
            "P_1ga8_2_4_1_44.py",
            "P_1ghr_3_2_1_73.py",
            "P_1gk2_4_3_1_3.py",
            "P_1gpi_3_2_1_91.py",
            "P_1gpk_3_1_1_7.py",
            "P_1gy0_2_4_2_31.py",
            "P_1h16_2_3_1_54.py",
            "P_1h1y_5_1_3_1.py",
            "P_1h2x_3_4_21_26.py",
            "P_1hl2_4_1_3_3.py",
            "P_1i1e_3_4_24_69.py",
            "P_1i2r_2_2_1_2.py",
            "P_1iov_6_3_2_4.py",
            "P_1j96_1_3_1_20.py",
            "P_1jf9_4_2_1_24.py",
            "P_1jz6_3_2_1_23.py",
            "P_1k9z_3_1_3_7.py",
            "P_1kcw_1_16_3_1.py",
            "P_1kdn_2_7_4_6.py",
            "P_1kfw_3_2_1_14.py",
            "P_1kkt_3_2_1_113.py",
            "P_1ko0_4_1_1_20.py",
            "P_1kuv_2_3_1_87.py",
            "P_1kwb_1_13_11_39.py",
            "P_1l1n_2_7_7_48.py"]
    filelist_p3 = ["P_1lcp_3_4_11_1.py",
            "P_1lt3_2_4_2_36.py",
            "P_1mbb_1_1_1_158.py",
            "P_1mqf_1_11_1_6.py",
            "P_1n68_1_10_3_2.py",
            "P_1n7n_4_2_2_1.py",
            "P_1n7n_4_2_2_5.py",
            "P_1n8p_4_4_1_1.py",
            "P_1naw_2_5_1_7.py",
            "P_1ndw_3_5_4_4.py",
            "P_1nhc_3_2_1_15.py",
            "P_1njs_2_1_2_2.py",
            "P_1nkh_2_4_1_38.py",
            "P_1npx_1_11_1_1.py",
            "P_1nv2_3_1_3_11.py",
            "P_1nwc_1_2_1_11.py",
            "P_1o2u_3_4_21_4.py",
            "P_1oc6_3_2_1_91.py",
            "P_1od1_3_4_23_22.py",
            "P_1opm_1_14_17_3.py",
            "P_1orv_3_4_14_5.py",
            "P_1os1_4_1_1_49.py",
            "P_1oyc_1_6_99_1.py",
            "P_1p7t_2_3_3_9.py",
            "P_1pfk_2_7_1_11.py",
            "P_1pgp_1_1_1_44.py",
            "P_1pj3_1_1_1_38.py",
            "P_1pjb_1_4_1_1.py",
            "P_1pno_1_6_1_2.py",
            "P_1pow_1_2_3_3.py",
            "P_1pyd_4_1_1_1.py",
            "P_1pzp_3_5_2_6.py",
            "P_1q2o_1_14_13_39.py",
            "P_1qfe_4_2_1_10.py",
            "P_1qj5_2_6_1_62.py",
            "P_1ql0_3_1_30_2.py",
            "P_1qnf_4_1_99_3.py",
            "P_1qnt_2_1_1_63.py",
            "P_1qpq_2_4_2_19.py",
            "P_1qq5_3_8_1_2.py",
            "P_1qtq_6_1_1_18.py",
            "P_1que_1_18_1_2.py",
            "P_1rab_2_1_3_2.py",
            "P_1s2i_2_4_2_6.py",
            "P_1sry_6_1_1_11.py"]
    filelist_p4 = ["P_1t4c_2_8_3_16.py",
            "P_1ueh_2_5_1_31.py",
            "P_1uou_2_4_2_4.py",
            "P_1upu_2_4_2_9.py",
            "P_1vas_3_1_25_1.py",
            "P_1xic_5_3_1_5.py",
            "P_2ald_4_1_2_13.py",
            "P_2dnj_3_1_21_1.py",
            "P_2f3g_2_7_1_69.py",
            "P_2had_3_8_1_5.py",
            "P_2nac_1_2_1_2.py",
            "P_2pth_3_1_1_29.py",
            "P_2tps_2_5_1_3.py",
            "P_2uag_6_3_2_9.py",
            "P_3cox_1_1_3_6.py",
            "P_3csm_5_4_99_5.py",
            "P_3fit_3_6_1_29.py",
            "P_3lip_3_1_1_3.py",
            "P_4hoh_3_1_27_3.py",
            "P_5csm_5_4_99_5.py",
            "P_5mdh_1_1_1_37.py",
            "P_5rsa_3_1_27_5.py",
            "P_5yas_4_1_2_39.py",
            "P_6enl_4_2_1_11.py",
            "Pab_1ah3_1_1_1_21.py",
            "Pab_1b8f_4_3_1_3.py",
            "Pab_1cjw_2_3_1_87.py",
            "Pab_1csc_4_1_3_7.py",
            "Pab_1edd_3_8_1_5.py",
            "Pab_1g9r_2_4_1_44.py",
            "Pab_1hdq_3_4_17_1.py",
            "Pab_1jz7_3_2_1_31.py",
            "Pab_1nyy_3_5_2_6.py",
            "Pab_1qgy_1_18_1_2.py",
            "Pab_4pfk_2_7_1_11.py",
            "Pfa_1csi_2_3_3_1.py",
            "Pfa_1ga8_2_4_1_44.py",
            "Pfa_1gk2_4_3_1_3.py",
            "Pfa_1j96_1_3_1_20.py",
            "Pfa_1jz6_3_2_1_23.py",
            "Pfa_1kuv_2_3_1_87.py",
            "Pfa_1pfk_2_7_1_11.py",
            "Pfa_1pzp_3_5_2_6.py",
            "Pfa_1que_1_18_1_2.py",
            "Pfa_1rab_2_1_3_2.py",
            "Pfa_2ctb_3_4_17_1.py",
            "Pfa_2had_3_8_1_5.py"]                
            
    reportfile = open(glb.pathmaker(('report','.txt'),root=glb.AUTOMOTIFSFOLDER), 'w')
    rmsdfile = open(glb.pathmaker(('rmsd','.txt'),root=glb.AUTOMOTIFSFOLDER), 'w')
    
    #filelist = filelist_n0
    #filelist = filelist_n0_1
    #filelist = filelist_n1
    #filelist = filelist_n2
    #filelist = filelist_n3
    #filelist = filelist_n4
    #filelist = filelist_n5
    #filelist = filelist_n6
    #filelist = filelist_n7
    #filelist = filelist_n8
    
    #filelist = filelist_p1
    #filelist = filelist_p2
    #filelist = filelist_p3
    #filelist = filelist_p4
    
    filelist = filelist_p1_1
    
    for i in range(len(filelist)):
        print '  running ',i+1," out of ",len(filelist)
        #path = glb.AUTOMOTIFSFOLDER+"\\"
        #path = glb.tempfolder+"\\"
        #path = "C:\Users\Mik\AppData\Roaming\SBEVSL\ProMol\temp\\"
        #path = "C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\Motifs\\"
        current_file = filelist[i]
        
        #folder = glb.USRMOTIFSFOLDER
        #folder = "C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\Motifs\\"
        #for the_file in os.listdir(folder):
        #    file_path = os.path.join(folder, the_file)
        #try:
        #    os.unlink(file_path)
        #except Exception, e:
        #    print e

        #try:
        #copy(path+current_file, "C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\Motifs\\")
        #glb.reset_user_motif_database()
        #except:
        #    continue
        
        id = current_file.split("_")[1]
        generated_homolog_list = lib.getH3(id)
        existing_homolog_list = lib.get_existing_homologs(id)
        non_homolog_list = lib.getNonHomologs(id)
        
        this_list = generated_homolog_list
        #this_list = existing_homolog_list
        #this_list = non_homolog_list
        
        if this_list is None:
            continue
        else:
            pdb_str = ""
            for pdb in this_list:
                pdb_str = pdb_str + pdb + ","
            
            glb.GUI.motifs['multipdb'].insert(END, pdb_str[0:-1])
            #c = motifchecker(5, 1, rmsdfile)
            c = motifchecker(1, 1, rmsdfile, current_file.split(".")[0])
            write_report(reportfile, id, c, len(this_list), pdb_str[0:-1])
            glb.GUI.motifs['multipdb'].delete(1.0, END)
            #os.remove(glb.USRMOTIFSFOLDER+"\\"+current_file)
        
    reportfile.close()
    rmsdfile.close()

def write_report(reportfile, id, c, n, pdb_str):
    reportfile.write('>' + '\t' + id + '\t' + str(c) + '\t' + str(n) + '\t' + pdb_str + '\n')
        
#def motifchecker(setChoice, rmsdchoice, reportfile, motifname):
def motifchecker(setChoice, rmsdchoice):
    #print '  in motifchecker'
    print setChoice,", ",rmsdchoice
    t1 = time.clock()
    global CSVMergeInfo
    glb.GUI.motifs['cancel'] = False
    #glb.GUI.motifs['motifbox'].delete(0,tk.END)
    glb.matchpairs = []
    CSVMergeInfo = {}
    glb.GUI.motifs['csvprep'] = {}
    glb.GUI.motifs['cancelbutton']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.DISABLED
    glb.GUI.motifs['exportButton']['state'] = tk.DISABLED
    glb.GUI.motifs['multipdb']['state'] = tk.DISABLED
    pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
    pdbsl = len(pdbs)
    lasto = 0.0
    
    # Hide the PyMOL viewer window
    # This not only increases the search speed, sometimes significantly,
    # but also may prevent the user from accidently interfering with
    # automatic selections
    cmd.window('hide')
    
    # Use the start time instead of the end time because:
    # - Want headers of all CSVs in the same search to be identical
    #   so that when they are combined no information is lost
    # - Don't know when the search will finish when the first CSV
    #   is written unless there is only one PDB code in the query box
    # This is a struct_time
    searchStartTime = time.localtime()
    
    # Initialize the progress bars
    # This call to update() may not be thread safe
    
    glb.GUI.motifs['single']['text'] = 'Starting search...'
    glb.GUI.motifs['overall']['text'] = 'Starting search...'
    #glb.GUI.motifs['rmsdlabel']['text'] = 'Starting search...' #added 2/20
    glb.GUI.motifs['singlestatus'].SetProgressPercent(0.0)
    glb.GUI.motifs['overallstatus'].SetProgressPercent(0.0)
    #glb.GUI.motifs['rmsdstatus'].SetProgressPercent(0.0)#added 2/20
    glb.GUI.motifs['single'].update()
    
    # Only define the search set once now, instead of
    # doing it inside the loop
    # This code will be replaced with something better soon anyway
    # But for now, I have rewritten it to be a little more concise
    sets = {1: ('P_Set', lambda key: key[0] == 'P'),
    2: ('J_Set', lambda key: key[0] == 'J'),
    3: ('N_Set', lambda key: key[0] == 'N'),
    4: ('All', lambda key: True),
    5: ('U_Set', lambda key: key[0] == 'U')}
    setName = sets[setChoice][0]
    # This is a Python list comprehension
    keys = set([motifName for motifName in glb.MOTIFS.keys() if sets[setChoice][1](motifName)])
    #keys = set([motifname])
    #these_keys = []
    #these_keys.append(motifname)
    #print "keys: ",str(keys)
    #print "these_keys: ",str(these_keys)
    #4/29 added
    glb.GUI.motifs['tt'].destroy()#removes current tree displaying past results
    glb.GUI.motifs['tt'] = texttree.TextTree(glb.GUI.motifs['motifbox'],funcs={'showContent':showContent})#create new tree
    glb.GUI.motifs['tt'].pack(expand=YES,fill=BOTH)
    c_ = 0
    global numResultsOfEachQuery #added 3/8
    print "length of pdbs: ",len(pdbs)
    for pdbIndex in range(len(pdbs)):
        rmsds = []
        pdb = pdbs[pdbIndex]
        # Deleted founds initializer
        pdb = pdb.strip()
        print "  checking for pdbIndex ",pdbIndex,"\t",pdb
        found = []
        last = 0.0
        keysL = len(keys)
        #keysL = len(these_keys)
        if keysL == 0:
            print ' keysL == 0'
            break
        keysLo = keysL*len(pdbs)
        glb.GUI.motifs['csvprep'][pdb] = {}
        cmd.reinitialize()
        cmd.fetch(pdb, async=0, path=glb.FETCH_PATH)
        if (pdb not in cmd.get_names('all')) or (cmd.count_atoms(pdb) == 0):
            lasto += keysL
            glb.GUI.motifs['singlestatus'].SetProgressPercent(100)
            glb.GUI.motifs['overallstatus'].SetProgressPercent((lasto/keysLo)*100)
            continue
        cmd.hide('everything', 'all')
        cmd.remove("all and hydro")
        
        for motif in keys:
        #for motif in these_keys:
            print "     checking motif ",str(motif)
            # Check for cancellation and break out of inner loop
            if glb.GUI.motifs['cancel']:
                glb.GUI.motifs['single']['text'] = 'Click Start to begin'
                #glb.GUI.motifs['overall']['text'] = 'Search cancelled at {0}%'.format(int(baro))
                glb.GUI.motifs['overall']['text'] = 'Search cancelled at %s%%'%(int(baro))
                break
                
            # List of motif loading errors is no longer stored inside motif dictionary

            # Determine whether or not we have a match
            here = True
            if MotifCaller(motif,False):
            #if here:
                ldr = count(motif,pdb)
                if ldr != None:
                    c_ += 1
                    #motifStr = '    {0}: {1}'.format(ldr, motif)
                    motifStr = '    %s: %s'%(ldr, motif)
                    found.append(motifStr)
            cmd.delete(motif)
            
            # Update progress bars
            # Calling update() on GUI widgets from here may not be thread safe
            # We will try to fix as soon as possible
            
            last += 1
            lasto += 1
            bar = (last/keysL)*100
            baro = (lasto/keysLo)*100
            #glb.GUI.motifs['single']['text'] = '{0} ({1} of {2}): {3}% complete'.format(pdb, pdbIndex + 1, len(pdbs), int(bar))
            #glb.GUI.motifs['overall']['text'] = 'Overall: {0}% complete'.format(int(baro))
            glb.GUI.motifs['single']['text'] = '%s (%s of %s): %s%% complete'%(pdb, pdbIndex + 1, len(pdbs), int(bar))
            glb.GUI.motifs['overall']['text'] = 'Overall: %s%% complete'%(int(baro))
            glb.GUI.motifs['singlestatus'].SetProgressPercent(bar)
            glb.GUI.motifs['overallstatus'].SetProgressPercent(baro)
            glb.GUI.motifs['single'].update()

        # If cancelled, break out of outer loop too
        if glb.GUI.motifs['cancel']:
            break
        found.sort()
        numResultsOfEachQuery.append(len(found))#added 3/8
        # Header line entry: both elements are the query PDB code
        glb.matchpairs.append((pdb, pdb))
        rmsdState=False#added 2/19
        for result in found:
            glb.matchpairs.append((pdb, result))
            
            #added 2/19
            if rmsdchoice is 1:
                rmsdState = True
                tag = result.split(': ')
                if len(tag) > 1:
                    motifName = tag[1]                    
                    queryCode = pdb
                    secondsplit = motifName.split('_')
                    if len(secondsplit) < 2:
                        return c_
                    motifPDBCode = secondsplit[1] # tpdb (pdb of result)
                    cmd.reinitialize()
                    cmd.fetch(queryCode, async=0, path=glb.FETCH_PATH)
                    cmd.hide('everything', 'all')
                    MotifCaller(tag[1])
                    try:
                        rmsds = proutils.getRMSD(motifName, queryCode, motifPDBCode)
                        rmsd_str = ""
                        for value in rmsds:
                            rmsd_str = rmsd_str + str(value) + '\t'
                        reportfile.write(motifName+ "\t" + queryCode + "\t" + rmsd_str + "\n")
                    except:
                        rmsds=[-1,-1,-1]
                    glb.GUI.motifs['csvprep'][pdb][motifName]['rmsd'] = rmsds
                   
                #count1 = count1+1
                #rmsdBar=(float(count1)/(len(pdbs)+len(found)-1))*100
                #glb.GUI.motifs['rmsdstatus'].SetProgressPercent(rmsdBar)
                #glb.GUI.motifs['rmsdlabel']['text'] = 'RMSD: {0}% complete'.format(int(rmsdBar))
                        
        # Export the single-PDB CSV file
        motifSet = motifset.MotifSet(setName, setName, keys)
        exportCSVResults(searchStartTime, glb.GUI.motifs['delta'].get(), motifSet, pdb, found, glb.GUI.motifs['csvprep'][pdb], rmsdState)
        if len(CSVMergeInfo) == 0:
            CSVMergeInfo['motif set short description'] = setName
            CSVMergeInfo['start time'] = searchStartTime
            CSVMergeInfo['partial files'] = list()
        CSVMergeInfo['partial files'].append(partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime))

    # I patched this code because lengtho - len(pdbs) was not returning the proper number of results.
    # -Kip
    numberOfResults = len(glb.matchpairs)
    
    oldpdb = ""
    struct = {}
    #edited 2/19
    #if rmsdchoice is 1:
    struct['type'] = 'Document'
    struct['name'] = 'Results'
    struct['properties'] = NP_ROOT|NP_ALLOW_CHILDREN|NP_AUTOBUILD
    struct['children']=[]
    i = -1
        
    if rmsdchoice is 1: 
        for query, motif in glb.matchpairs:
            
            if query != oldpdb:
                j = -1
                struct['children'].append({'type':'Section','name':query,'children':[]}) 
                i=i+1
            oldpdb = query
            tag = motif.split(': ')
             
            if len(tag) > 1:
                motifName = tag[1]
                struct['children'][i]['children'].append({'type':'Subsection','name':motif,'children':[]})
                j=j+1
                if len(glb.GUI.motifs['csvprep'][query][motifName]['rmsd']) > 0:
                    struct['children'][i]['children'][j]['children'].append({'type':'Subsection','name':'RMSD All:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][0], 4))})
                    struct['children'][i]['children'][j]['children'].append({'type':'Subsection','name':'RMSD alpha:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][1], 4))})
                    struct['children'][i]['children'][j]['children'].append({'type':'Subsection','name':'RMSD alpha & beta:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][2], 4))})
                 
            if query == motif:
                numberOfResults -= 1
            
            
    else:
        for query, motif in glb.matchpairs:
            if query != oldpdb:
                j = -1
                struct['children'].append({'type':'Section','name':query,'children':[]}) 
               
                i=i+1
            oldpdb = query
            tag = motif.split(': ')
             
            if len(tag) > 1:
                motifName = tag[1]
                struct['children'][i]['children'].append({'type':'Subsection','name':motif,'children':[]})
                j=j+1
        # The new matchpairs collection of ordered pairs
        # contains, in each element, the query PDB code and
        # the matching motif, in that order.  Header lines are
        # indicated by an entry with both parts containing
        # the query PDB code.
            if query == motif:
                numberOfResults -= 1
    ###
    
    
    
    glb.GUI.motifs['tt'].showTree(struct,DT_TWSTRUCT,-1,
        props=NP_AUTOBUILD|NP_ALLOW_CHILDREN,
        state=NS_EXPANDED)#add nodes from struct to the tree
    
    #cmd.reset() # changed from cmd.orient('all')
    #cmd.show('cartoon', 'all')
    #cmd.color('gray', 'all')
    if not glb.GUI.motifs['cancel']:
        glb.GUI.motifs['single']['text'] = 'Click Start to begin'
        #glb.GUI.motifs['overall']['text'] = 'Motif Finder finished with {0} results.'.format(numberOfResults)
        glb.GUI.motifs['overall']['text'] = 'Motif Finder finished with %s results.'%(numberOfResults)
    
    if numberOfResults > 0:
        glb.GUI.motifs['exportButton']['state'] = tk.NORMAL
        
    # The rest of these should be outside the if
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.NORMAL
    glb.GUI.motifs['multipdb']['state'] = tk.NORMAL
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
    
    # Show the PyMOL viewer window
    cmd.window('show')

    print(time.clock() - t1)
    return c_
    
    
# Refactored motif maker

class MotifMaker:
    
    def __init__(self):
        pass

    # Maybe this should go in init()
    # But this is the initial refactoring from procedural code
    def doCommonSetup(self):
        glb.GUI.motif_maker['file'] = None
        glb.GUI.motif_maker['wait'] = []
        glb.GUI.motif_maker['motif'] = []
        glb.GUI.motif_maker['order'] = []
        self.pf = glb.GUI.motif_maker['pf'].get()
        self.pdb = glb.GUI.motif_maker['pdb'].get().lower()
        self.ecen = glb.GUI.motif_maker['ec'].get()
        self.resn = {}
        self.resi = {}
        self.backbone = {}
        self.chain = {}
        self.excepLoop = 0
        self.exceptions = ''
        self.ec = ''
        self.name = ''
        self.skip = {}
        self.numberOfAcids = 0
        cmd.reinitialize()
        
    # replaces makemotif(3)
    def clear(self):
        self.doCommonSetup()
        self.resetRows()
        glb.GUI.motif_maker['pf'].delete(0,tk.END)
        glb.GUI.motif_maker['pf'].insert(0,'2.00')
        glb.GUI.motif_maker['pdb'].delete(0,tk.END)
        glb.GUI.motif_maker['ec'].delete(0,tk.END)

        
    def resetRows(self):
        for i in range(1,11):
            glb.GUI.motif_maker['resn'][i].delete(0,tk.END)
            glb.GUI.motif_maker['resi'][i].delete(0,tk.END)
            glb.GUI.motif_maker['chain'][i].delete(0,tk.END)
            if glb.GUI.motif_maker['backbone'][i].get() == 'On':
                glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
        
    # replaces write(string != None)
    def buildMotif(self, string):
        glb.GUI.motif_maker['motif'].append(string)
    
    # Replaces write(open=True) with mode = 0 or 4
    def openMotifForTesting(self):
        glb.GUI.motif_maker['motif'] = []
        return True
        
    # Replaces write(open=True) with mode = 1
    def openMotifForSaving(self):
        if os.path.exists(glb.pathmaker((self.name,'.py'),root=glb.USRMOTIFSFOLDER)) or os.path.exists(glb.pathmaker((self.name,'.py'),root=glb.MOTIFSFOLDER)):
            answer = askyesno('Motif Exists', 
            'A motif has already been made for EC:%s on PDB:%s.\n'%(self.ec,self.pdb)+
            'Are you sure you want to replace it?')
            if answer == False:
                 return False
        glb.GUI.motif_maker['file'] = open(glb.pathmaker((self.name,'.py'),root=glb.USRMOTIFSFOLDER), 'w')
        return True
        
    # Replaces write(open=True) with mode=2
    def openMotifForExporting(self):
        pref = askdirectory(initialdir=glb.HOME)
        if os.access(pref,os.W_OK | os.X_OK):
            if os.path.exists(glb.pathmaker('Motifs',(self.name,'.py'),root=pref)):
                answer = askyesno('Motif Exists', 
                'This file exists at this location.\n'+
                'Are you sure you want to replace it?')
                if answer == False:
                    return False
            glb.GUI.motif_maker['file'] = open(glb.pathmaker((self.name,'.py'),root=pref), 'w')
        else:
            showerror('Access Denied','You do not have access to write to this folder.')
            return False
        return True

    # Replaces write(close=True) with mode=0 or 4
    def closeMotifForTesting(self):
        if glb.GUI.motif_maker['radio'].get() == 1:
            cmd.reinitialize()
            cmd.fetch(glb.GUI.motif_maker['testpdb'].get(), async=0, path=glb.FETCH_PATH)
            glb.update()
        elif glb.GUI.motif_maker['radio'].get() == 2:
            glb.randompdb()

        d = 1
        
        lines = ''.join(glb.GUI.motif_maker['motif']).split('\n')
        for line in lines:
            if line != '':
                eval(line)
        glb.procolor(self.name, show_all='cartoon', color_all='gray')
        cmd.select('matching_subset', self.name)
        # I think here it's OK to delete the motif name
        cmd.delete(self.name)
        cmd.orient('matching_subset')
        matchMakerColor = glb.GUI.motif_maker['matchcolor']['bg']
        cmd.set_color('matchmakercolor',
            ([int(n, 16) for n in (matchMakerColor[1:3], matchMakerColor[3:5], matchMakerColor[5:7])]))
        cmd.color('matchmakercolor', 'matching_subset')
        cmd.deselect()
        return True
        
    # Replaces write(close=True) with mode=2
    def closeMotifForExporting(self):
        if glb.GUI.motif_maker['file'] != None:
            glb.GUI.motif_maker['file'].writelines(glb.GUI.motif_maker['motif'])
            glb.GUI.motif_maker['file'].close()                        
        else:
            print 'No file written'
        return True
            
    # Replaces write(close=True) with mode=1
    def closeMotifForSaving(self):
        self.closeMotifForExporting()
        glb.loadMotifs(glb.USRMOTIFSFOLDER)
        return True
        
    def getlocistr(self):
        locistr = ''
        tmpdict = {}
        for item in glb.GUI.motif_maker['order']:
            if item[1] not in tmpdict:
                tmpdict[item[1]] = []
            tmpdict[item[1]].append(item[2])
        for chain in tmpdict:
            locistr = '%s%s-%s;' % (locistr, chain.lower(), ','.join(tmpdict[chain]))
        return locistr
    
    def getresnstr(self):
        tmplist = []
        for item in glb.GUI.motif_maker['order']:
            tmplist.append(item[0])
        return ','.join(tmplist)
    
    def addresn(self,x,y,z):
        glb.GUI.motif_maker['order'].append((x, y, z))
        try:
            glb.GUI.motif_maker['order'].sort(key=lambda item: (item[1],int(item[2])))
        except TypeError:
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(int(x[2]), int(y[2])))
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(x[1], y[1]))
        return x
    
    def acceptresn(self,x,y,z):
        if len(x) == 0:
            return ''
        try:
            x = x.lower()
            newresn = glb.AminoHashTable[x][3]
        except KeyError:
            return None
        return self.addresn(newresn,y,z)
        
    # Row reordering functionality
    def updateMoveButtonState(self):
        glb.GUI.motif_maker['moveup'].configure(state = (tk.NORMAL if glb.GUI.motif_maker['selection'].get() > 1 else tk.DISABLED))
        glb.GUI.motif_maker['movedown'].configure(state = (tk.NORMAL if glb.GUI.motif_maker['selection'].get() < 10 else tk.DISABLED))

    def moveRow(self, up):
        startingRow = glb.GUI.motif_maker['selection'].get()
        tempResn = glb.GUI.motif_maker['resn'][startingRow].get()
        tempChain = glb.GUI.motif_maker['chain'][startingRow].get()
        tempResi = glb.GUI.motif_maker['resi'][startingRow].get()
        tempBone = glb.GUI.motif_maker['backbone'][startingRow].get()
        swapRow = startingRow - 1 if up else startingRow + 1
        glb.GUI.motif_maker['resn'][startingRow].delete(0, tk.END)
        glb.GUI.motif_maker['chain'][startingRow].delete(0, tk.END)
        glb.GUI.motif_maker['resi'][startingRow].delete(0, tk.END)
        
        glb.GUI.motif_maker['resn'][startingRow].insert(tk.END, glb.GUI.motif_maker['resn'][swapRow].get())
        glb.GUI.motif_maker['chain'][startingRow].insert(tk.END, glb.GUI.motif_maker['chain'][swapRow].get())
        glb.GUI.motif_maker['resi'][startingRow].insert(tk.END, glb.GUI.motif_maker['resi'][swapRow].get())
        if tempBone != glb.GUI.motif_maker['backbone'][swapRow].get():
            glb.GUI.motif_maker['backbone'][startingRow].invoke('buttonup')
        
        glb.GUI.motif_maker['resn'][swapRow].delete(0, tk.END)
        glb.GUI.motif_maker['chain'][swapRow].delete(0, tk.END)
        glb.GUI.motif_maker['resi'][swapRow].delete(0, tk.END)
        
        glb.GUI.motif_maker['resn'][swapRow].insert(tk.END, tempResn)
        glb.GUI.motif_maker['chain'][swapRow].insert(tk.END, tempChain)
        glb.GUI.motif_maker['resi'][swapRow].insert(tk.END, tempResi)
        if tempBone != glb.GUI.motif_maker['backbone'][swapRow].get():
            glb.GUI.motif_maker['backbone'][swapRow].invoke('buttonup')
            
        glb.GUI.motif_maker['selection'].set(swapRow)
        self.updateMoveButtonState()
        
    # Depends on doCommonSetup() already being called
    # Returns false if input was bad
    def validateInput(self):
        cmd.fetch(self.pdb, async=0, path=glb.FETCH_PATH)
        if (self.pdb not in cmd.get_names('all')) or (cmd.count_atoms(self.pdb) == 0):
            #self.exceptions += 'Could not fetch {0}'.format(self.pdb)
            self.exceptions += 'Could not fetch %s'%(self.pdb)
        glb.update()
        preecs = self.ecen.split(',')
        for preec in preecs:
            try:
                eclist = preec.split('.')
                ec1,ec2,ec3,ec4 = eclist
            except ValueError:
                self.exceptions += 'Please enter a correct EC code with periods.\n'
            else:
                if len(ec1) != 1 or int(ec1) < 1 or int(ec1) > 7:
                    self.exceptions += 'The first number in an EC code has to be >= 1 and <= 7.\n'
                if len(ec2) > 2 or len(ec2) < 1:
                    self.exceptions += 'The second number in an EC code has to be at most two digits.\n'
                if len(ec3) > 2 or len(ec3) < 1:
                    self.exceptions += 'The third number in an EC code has to be at most two digits.\n'
                if len(ec4) > 3 or len(ec4) < 1:
                    self.exceptions += 'The fourth number in an EC code has to be at most three digits.\n'
        self.ec = self.ecen.replace('.','_').replace(',','_').replace(' ','')
        self.skip = {}
        self.skip[0] = 0
        for i in range(1,11):
            # The old way of storing what order they were in is too complicated
            # This will try to set it once in the GUI and forget it
            g = i
            self.resi[g] = glb.GUI.motif_maker['resi'][g].get().strip()
            self.backbone[g] = glb.GUI.motif_maker['backbone'][g].get()
            self.chain[g] = glb.GUI.motif_maker['chain'][g].get().strip()
            self.resn[g] = self.acceptresn(glb.GUI.motif_maker['resn'][g].get().strip(),self.chain[g],self.resi[g])
            self.skip[g] = False
            if self.resn[g] == '' and self.resi[g] == '' and self.chain[g] == '':
                ### this gives us the ability to skip whole blocks
                self.skip[g] = True
                self.skip[0] += 1
            elif self.resn[g] != '' and self.resi[g] != '' and self.chain[g] != '':
                if self.resn[g] == None:
                    self.exceptions += 'Residue %s is not recongnized.\n'%(g)
                elif cmd.count_atoms('%s/%s`%s/'%(self.chain[g],self.resn[g],self.resi[g])) == 0:
                    self.exceptions += 'There is no %s at number %s on chain %s.\n'%(self.resn[g],self.resi[g],self.chain[g])
                elif self.resn[g] == 'gly' and self.backbone[g] == 'Off':
                    self.exceptions += 'Please turn on the backbone for glycine residue %s\n'%(g)
                self.excepLoop +=1
            else:    
                if self.resn[g] == '':
                    self.exceptions += 'Please enter a residue for residue %s\n'%(g)
                if self.resi[g] == '':
                    self.exceptions += 'Please enter a number for residue %s\n'%(g)
                if self.chain[g] == '':
                    self.exceptions += 'Please select a chain for residue %s\n.'%(g)
                self.excepLoop +=1
        if self.excepLoop < 2:
            # exception = True
            self.exceptions += 'Motifs require that 2 or more residues be entered.'
        if self.exceptions != '' and self.exceptions != '\n':
            showerror('Error', 'The following errors have occurred:\n'+self.exceptions)
            return False
        return True

    # Replaces makemotif(5.2)
    # Does not work properly: deletes additional rows beyond the first
    # containing the same amino acid even at different positions or on
    # different chains
    def recommendOrder(self):
        self.doCommonSetup()
        if self.validateInput():
            residuecounts = {}
            for i in range(1,11):
                h = glb.GUI.motif_maker['resn'][i].get()
                if h == '':
                    continue
                cmd.select(h,'resn %s'%h)
                residuecounts[cmd.count_atoms(h)/glb.AminoHashTable[h][0]] = i
                cmd.delete(h)
            keys = residuecounts.keys()
            keys.sort()
            residueorder = []
            for key in keys:
                residueorder.append(residuecounts[key])
            print residueorder
            
            # I hope this is what the order means
            # I take it residueorder[newRowIndex] = oldRowIndex
            # The reordering calculation code above was added by a previous
            # developer
            newList = []
            for oldRowIndex in residueorder:
                currentRow = {}
                for field in ('resn', 'chain', 'resi', 'backbone'):
                    currentRow[field] = glb.GUI.motif_maker[field][oldRowIndex].get()
                newList.append(currentRow)
            
            self.resetRows()
            
            for newRowIndex in range(len(newList)):
                currentRow = newList[newRowIndex]
                for field in ('resn', 'chain', 'resi'):
                    glb.GUI.motif_maker[field][newRowIndex + 1].delete(0, tk.END)
                    glb.GUI.motif_maker[field][newRowIndex + 1].insert(tk.END, currentRow[field])
                if currentRow['backbone'] != glb.GUI.motif_maker['backbone'][newRowIndex + 1].get():
                    glb.GUI.motif_maker['backbone'][newRowIndex + 1].invoke('buttonup')
        
    # Replaces makemotif(0) and makemotif(4)
    def testMotif(self):
        print 'Testing motif from MotifMaker'
        if self.makeMotifWrapper(self.openMotifForTesting, self.closeMotifForTesting):
            #print 'Motif {0} with {1} amino acids was run.'.format(self.name, self.numberOfAcids)
            print 'Motif %s with %s amino acids was run.'%(self.name, self.numberOfAcids)
            return True
        else:
            return False

    # Replaces makemotif(1)
    def saveMotif(self):
        if self.makeMotifWrapper(self.openMotifForSaving, self.closeMotifForSaving):
            #print 'Motif {0} saved to user motifs folder with {1} amino acids.'.format(self.name, self.numberOfAcids)
            print 'Motif %s saved to user motifs folder with %s amino acids.'%(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    # Replaces makemotif(2)
    def exportMotif(self):
        if self.makeMotifWrapper(self.openMotifForExporting, self.closeMotifForExporting):
            #print 'Motif {0} exported with {1} amino acids.'.format(self.name, self.numberOfAcids)
            print 'Motif %s exported with %s amino acids.'%(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    # Fault-tolerant wrapper
    def makeMotifWrapper(self, openFunction, closeFunction):
        retVal = False
        try:
            retVal = self.makeMotifCore(openFunction, closeFunction)
        except IOError, problem:
            print problem
        finally:
            if glb.GUI.motif_maker['file'] != None:
                if not glb.GUI.motif_maker['file'].closed:
                    glb.GUI.motif_maker['file'].close()
        return retVal
    
    # Replaces most of makemotif(0, 1, 2, 4)
    # But don't call directly!
    def makeMotifCore(self, openFunction, closeFunction):
        self.doCommonSetup()
        if self.validateInput():
            self.name = 'U_%s_%s'%(self.pdb,self.ec)
            self.buildMotif("'''\n")
            self.buildMotif("FUNC:%s\n"%(self.name))
            self.buildMotif("PDB:%s\n"%(self.pdb))
            self.buildMotif("EC:%s\n"%(self.ec.replace('_','.')))
            self.buildMotif("RESI:%s\n"%(self.getresnstr()))
            self.buildMotif("LOCI:%s\n"%(self.getlocistr()))
            self.buildMotif("'''\n")
            if not openFunction():
                return False
            atomlist = {}
            ### backbone off aka just side chains from beta carbon onwards
            atomlist[0] = {'ala':('CB',), # First comma added by Kip to make it a tuple
                           'arg':('CB','CG','CD','NE','CZ','NH1','NH2'),
                           'asn':('CB','CG','OD1','ND2'),
                           'asp':('CB','CG','OD1','OD2'),
                           'cys':('CB','SG'),
                           'gln':('CB','CG','CD','OE1','NE2'),
                           'glu':('CB','CG','CD','OE1','OE2'),
                           'gly':(),
                           'his':('CB','CG','ND1','CD2','CE1','NE2'),
                           'ile':('CB','CG1','CG2','CD'),
                           'leu':('CB','CG','CD1','CD2'),
                           'lys':('CB','CG','CD','CE','NZ'),
                           'met':('CB','CG','SD','CE'),
                           'phe':('CB','CG','CD1','CD2','CE1','CE2','CZ'),
                           'pro':('CB','CG','CD'),
                           'ser':('CB','OG'),
                           'thr':('CB','OG1','CG2'),
                           'trp':('CB','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'),
                           'tyr':('CB','CG','CD1','CD2','CE1','CE2','CZ','OH'),
                           'val':('CB','CG1','CG2'),
                           'mg':('MG',),
                           'zn':('ZN',),
                           'mn':('MN',),
                           'na':('NA',),
                           'hem':('FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','C3B','C4B','CMB','CAB','CBB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D'),
                           'co':('CO',),
                           'ni':('NI',),
                           'fe':('FE',),
                           'cu':('CU',)}
            atomlist[1] = ('O','C','CA','N')### backbone on
            resnlist = ['']### residue list
            resnlistf = ['']### residue list with appended 'i', making them unique
            resilist = ['']### residue id list. Based on sequence number.
            chainlist = ['']### chain list
            bonelist = ['']### backbone list
            
            numOfi = {}
            for i in range(1,11):
                # This is the second place this was changed:
                # From:
                # g = glb.GUI.motif_maker['curorder'][i]
                # To:
                g = i
                if not self.skip[g]:
                    if self.resn[g] not in numOfi:
                        numOfi[self.resn[g]] = 0
                    resnlist.append(self.resn[g])
                    resilist.append(self.resi[g])
                    resnlistf.append(self.resn[g]+('i'*(numOfi[self.resn[g]])))
                    chainlist.append(self.chain[g])
                    bonelist.append(self.backbone[g])
                    numOfi[self.resn[g]] += 1
            
            ### This loop will increment through the amino acids. The amino acid we are looking
            ### at right now is specified by the e variable. The a variable will count the
            ### number of times it is compared to the carbons in the other amino acids. And is
            ### used later on to print the "byres" and select line, and delete line below.
            resnlen = (len(resnlist)-1)
            e = 0
            while e < resnlen:
                a = 0
                e += 1
                ### select stuff explained later on
                selectlimit = 50
                selectstart = 1 ### where to start selection
                selectlimiter = 1 ### limit defined as a/selectlimit
                selectextra = [] ### add to selection at the end
                deleteextra = [] ### add to deletion at the end
                
                if bonelist[e] == 'Off':###just sidechains
                    bList=atomlist[0][resnlist[e]]
                else:### sidechain with backbone
                    bList=atomlist[0][resnlist[e]]+atomlist[1]
                
                ### This loop will increment through the amino acids that we want
                ### to compare to the amino acid we want to find. The amino acid
                ### being compared is specified by the d variable.
                # d is also a variable used in closeMotifForTesting(), but
                # the fact that it has gone out of and back into scope
                # shouldn't matter here (they used to be in the same function)
                
                d = 0
                while d < resnlen:
                    d += 1
                    ### The following line: compare amino acids
                    ### If they are the same, then lets increment one.
                    if resnlistf[e] == resnlistf[d]:
                        d += 1
                        if d > resnlen:
                            continue
                    
                    if bonelist[d] == 'Off':###just sidechains
                        cList=atomlist[0][resnlist[d]]
                    else:### sidechain with backbone
                        cList=atomlist[0][resnlist[d]]+atomlist[1]
                    
                    ### This loop increments through all the carbons
                    ### in the amino acid we want to find.
                    for eachB in bList:
                        ### This loop increments through all the carbons
                        ### in the other amino acids that we are want to
                        ### compare with.
                        for eachC in cList:
                            ### Gets the distance between our atoms in our selected amino acids.
                            r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+eachB,chainlist[d]+'/'+resilist[d]+'/'+eachC)
                            ### The precision factor
                            ### The ranger is the slider that is moved.
                            ### r is set by the get_distance above.
                            g = '%.2f' %(float(r) + float(self.pf))
                            
                            a += 1
                            
                            ### apparently pymol cannot handle over a number
                            ### between 248 and 264 selections at one time.
                            ### This fixes that by making sure we do not pass
                            ### "selectlimit" selections at one time.
                            if float(selectlimiter) < (float(a)/float(selectlimit)):
                                self.buildMotif("cmd.select('%s%s',' "%(resnlistf[e],(selectlimiter*selectlimit)))
                                for i in range(selectstart,a):
                                    if i==(a-1):
                                        self.buildMotif("br. %s%s')\n"%(resnlistf[e],i))
                                    else:
                                        self.buildMotif("br. %s%s&"%(resnlistf[e],i))
                                for i in range(selectstart,a):
                                    if i==(a-1):
                                        pass
                                    else:
                                        self.buildMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
                                selectextra.append('%s%s&'%(resnlistf[e],(selectlimiter*selectlimit)))
                                deleteextra.append("cmd.delete('%s%s')\n"%(resnlistf[e],(selectlimiter*selectlimit)))
                                selectlimiter += 1
                                selectstart += selectlimit
                            
                            ### e > d is all the combinations of residues
                            ### that would already have one of the residues
                            ### found in the motif, therefore the second
                            ### amino acid does not need an r. (resn)
                            ### property selection, as it is already a selection.
                            if e > d:
                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlistf[d],g))
                            else:
                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlist[d],g))
                self.buildMotif("cmd.select('%s',' "%(resnlistf[e]))
                if selectextra != []:
                    self.buildMotif(''.join(selectextra))
                for i in range(selectstart,a+1):
                    if i==a:
                        self.buildMotif("br. %s%s')\n"%(resnlistf[e],i))
                    else:
                        self.buildMotif('br. %s%s&'%(resnlistf[e],i))
                for x in deleteextra:
                    self.buildMotif(x)
                for i in range(selectstart,a+1):
                    self.buildMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
        
            resnlistfstr = ""
            for i in range(1,resnlen+1):
                if i == resnlen:
                    resnlistfstr += resnlistf[i]
                else:
                    resnlistfstr += resnlistf[i]+'|'
        
            self.buildMotif("cmd.select('%s', '%s')\n"%(self.name,resnlistfstr))
            for i in range(1,resnlen+1):
                self.buildMotif("cmd.delete('%s')\n"%(resnlistf[i]))
            self.numberOfAcids = len(resnlist) - 1
            closeFunction()
            return True