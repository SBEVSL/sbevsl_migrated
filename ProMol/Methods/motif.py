from pymol import cmd
from pymol import stored
import Tkinter as tk
import Pmw
import os
import re
import time
import math
from tkFileDialog import asksaveasfile, askdirectory, askopenfile
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
import Tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
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
    d = float(glb.GUI.motifs['delta'].get())
    if camera:
        glb.deletemotif()
        glb.update()
    try:
        if execfile(glb.MOTIFS[motif]['path']) != False:
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


def doubleClickMotif(event):
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
    selectionList = glb.GUI.motifs['motifbox'].curselection()
    if len(selectionList) == 0:
        return
    motif = int(selectionList[0])

    #added 2/19, edited 3/8
   
    if glb.GUI.motifs['motifbox'].size() > len(glb.matchpairs):
        motifString = ""
        index = 0
        if motif <= (numResultsOfEachQuery[0]*5)+2:
            print "i=" + repr(0)
            index = int(math.floor((motif+3)/5))
            motifString = glb.matchpairs[index][1]
            print "motif =" + repr(motif)
            print "motifstring=" + motifString
        else:
            current1 = 0
            for i in range(0,pdbsl):
                print "i=" + repr(i)
                print "motif =" + repr(motif)
                current2 = current1 + (numResultsOfEachQuery[i]*5)+2
                print "numResultsOfEachQuery[i]*5=" + repr(numResultsOfEachQuery[i]*5)
                print "current1=" + repr(current1)
                print "current2=" + repr(current2)
                if motif <= current2 and motif > current1:
                        print "i=" + repr(i)
                        if numResultsOfEachQuery[i] != 0:
                            index = int(math.floor((motif+((i+1)*3))/5))  #3/18/12
                        else:
                            index = int(math.floor((motif+((i+1)*3)+1)/5)) 
                        print "index=" + repr(index)
                        motifString = glb.matchpairs[index][1]
                        print "motifstring=" + motifString
                        break
                current1 = current2
          
          
    else:
        motifString = glb.matchpairs[motif][1]
    ###


        
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

    #added 2/19
    if glb.GUI.motifs['motifbox'].size() > len(glb.matchpairs):
        queryPDBCode = glb.matchpairs[index][0]
    else:
        queryPDBCode = glb.matchpairs[motif][0]
    ###

        
    cmd.reinitialize()
    motifColor = glb.GUI.motifs['motifcolor']['bg']
    queryColor = glb.GUI.motifs['querycolor']['bg']
    if glb.GUI.motifs['align'].get() == 0 or motifPDBCode == queryPDBCode:
        cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)
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
            
            querySubsetName = 'match_in_{0}'.format(queryPDBCode)
            # Actually renames the query protein matching subset
            # because the selection named after the motif contains the matching subset
            # of atoms on the query protein given to us by the motif
            cmd.select(querySubsetName, motifName)
            cmd.hide('everything', 'all')
            cmd.fetch(motifPDBCode, async=0, path=glb.FETCH_PATH)
            # Removed cartoon show command
            # Create named subset of matching result protein atoms
            motifSubsetName = 'match_in_{0}'.format(motifPDBCode)
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
    with asksaveasfile(initialfile=defaultfile, defaultextension='.csv', filetypes=[('Comma Separated Value files','*.csv'), ('All files','*.*')], title='Export Motif Finder Results As...') as outhandle:

        firstFile = True # include the first header only
        for partialCSVFile in CSVMergeInfo['partial files']:

            with open(os.path.join(glb.CSV_PATH, partialCSVFile), 'rU') as inhandle:
                lineIndex = 0
                for eachLine in inhandle:
                    lineIndex = lineIndex + 1
                    if firstFile or (lineIndex > INDIVIDUAL_CSV_HEADER_LENGTH):
                       outhandle.write(eachLine)
            firstFile = False
            outhandle.write('\n\n')

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
    csv = ['Motif Finder Results,,Generated by ProMOL version {0}'.format(glb.VERSION),
    'Search started at {0},,Precision factor: {1},,Algorithm version: {2}'.format(time.asctime(searchStartTime), precisionFactor, glb.ALG_VERSION),
    '"Motif set: {0}"'.format(motifSet.longDescription),
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
            key = '{0}{1}'.format(resn,resi)
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
        csv[line] += ',{0}'.format(notFoundMotif)
        line += 1

    csvfile = "\n".join(csv)
    with open(os.path.join(glb.CSV_PATH, partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime)), 'w') as csvhandle:
        csvhandle.write(csvfile)

# Create uniform timestamp for CSV filenames
def generateCSVTimeString(searchStartTime):
    return time.strftime('%b_%d_%Y_%H%M_%Z', searchStartTime)

# Create appropriate filenames for CSV files
def partialCSVFilename(pdb, motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    return 'motiffinder_partial_{0}_{1}_{2}.csv'.format(pdb, motifSetName, stamp)

def fullCSVFilename(motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    return 'motiffinder_{0}_{1}.csv'.format(motifSetName, stamp)

def count(motif,pdb):
    last = None
    ordered = []
    orderedchain = {}
    bannedchain = []
    stored.motif = []
    editdist = []
    
    
    cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
    residues = glb.MOTIFS[motif]['resi']
    residuesl = len(residues)*2
    glb.GUI.motifs['csvprep'][pdb][motif] = {}
    glb.GUI.motifs['csvprep'][pdb][motif]['res'] = []
    for iteration in stored.motif:
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
    glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
    # Removed storage of precision factor as it is the same for the entire search
    return glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange']

def motifchecker(setChoice, rmsdchoice):
    global CSVMergeInfo
    glb.GUI.motifs['cancel'] = False
    glb.GUI.motifs['motifbox'].delete(0,tk.END)
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

  
    global numResultsOfEachQuery #added 3/8
    for pdbIndex in range(len(pdbs)):
        rmsds = []
        pdb = pdbs[pdbIndex]
        # Deleted founds initializer
        pdb = pdb.strip()
        found = []
        last = 0.0
        keysL = len(keys)
        if keysL == 0:
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
            # Check for cancellation and break out of inner loop
            if glb.GUI.motifs['cancel']:
                glb.GUI.motifs['single']['text'] = 'Click Start to begin'
                glb.GUI.motifs['overall']['text'] = 'Search cancelled at {0}%'.format(int(baro))
                break
                
            # List of motif loading errors is no longer stored inside motif dictionary

            # Determine whether or not we have a match
            if MotifCaller(motif,False):
                ldr = count(motif,pdb)
                if ldr != None:
                    motifStr = '    {0}: {1}'.format(ldr, motif)
                    found.append(motifStr)
            cmd.delete(motif)
            
            # Update progress bars
            # Calling update() on GUI widgets from here may not be thread safe
            # We will try to fix as soon as possible
            
            last += 1
            lasto += 1
            bar = (last/keysL)*100
            baro = (lasto/keysLo)*100
            glb.GUI.motifs['single']['text'] = '{0} ({1} of {2}): {3}% complete'.format(pdb, pdbIndex + 1, len(pdbs), int(bar))
            glb.GUI.motifs['overall']['text'] = 'Overall: {0}% complete'.format(int(baro))
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
                        return
                    motifPDBCode = secondsplit[1] # tpdb (pdb of result)
                    cmd.reinitialize()
                    cmd.fetch(queryCode, async=0, path=glb.FETCH_PATH)
                    cmd.hide('everything', 'all')
                    MotifCaller(tag[1])
                    rmsds = proutils.getRMSD(motifName, queryCode, motifPDBCode)#
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

    # I patched this code because lengtho - len(pdbs) was not returning the proper number of results.
    # -Kip
    numberOfResults = len(glb.matchpairs)
    
    oldpdb = ""
    #edited 2/19
    if rmsdchoice is 1:
        for query, motif in glb.matchpairs:
            
            if query != oldpdb:
                glb.GUI.motifs['motifbox'].insert(tk.END, "\n")
                glb.GUI.motifs['motifbox'].insert(tk.END, query)
            oldpdb = query
            tag = motif.split(': ')
          
            if len(tag) > 1:
                motifName = tag[1]
                glb.GUI.motifs['motifbox'].insert(tk.END, motif)
                #fixed errors 2/26
                if len(glb.GUI.motifs['csvprep'][query][motifName]['rmsd']) > 0:
                    glb.GUI.motifs['motifbox'].insert(tk.END, "       atoms      rmsd ")
                    glb.GUI.motifs['motifbox'].insert(tk.END, "       all           " + repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][0], 4)))
                    glb.GUI.motifs['motifbox'].insert(tk.END, "       ca           " + repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][1], 4)))
                    glb.GUI.motifs['motifbox'].insert(tk.END, "       cb & ca   " + repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][2], 4)))
            if query == motif:
                numberOfResults -= 1
    else:
        for query, motif in glb.matchpairs:
            glb.GUI.motifs['motifbox'].insert(tk.END, motif)
        # The new matchpairs collection of ordered pairs
        # contains, in each element, the query PDB code and
        # the matching motif, in that order.  Header lines are
        # indicated by an entry with both parts containing
        # the query PDB code.
            if query == motif:
                numberOfResults -= 1
    ###
    
    cmd.orient('all')
    cmd.show('cartoon', 'all')
    cmd.color('gray', 'all')
    if not glb.GUI.motifs['cancel']:
        glb.GUI.motifs['single']['text'] = 'Click Start to begin'
        glb.GUI.motifs['overall']['text'] = 'Motif Finder finished with {0} results.'.format(numberOfResults)
    
    if numberOfResults > 0:
        glb.GUI.motifs['exportButton']['state'] = tk.NORMAL
        
    # The rest of these should be outside the if
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.NORMAL
    glb.GUI.motifs['multipdb']['state'] = tk.NORMAL
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
    
    # Show the PyMOL viewer window
    cmd.window('show')

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
            self.exceptions += 'Could not fetch {0}'.format(self.pdb)
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
        if self.makeMotifWrapper(self.openMotifForTesting, self.closeMotifForTesting):
            print 'Motif {0} with {1} amino acids was run.'.format(self.name, self.numberOfAcids)
            return True
        else:
            return False

    # Replaces makemotif(1)
    def saveMotif(self):
        if self.makeMotifWrapper(self.openMotifForSaving, self.closeMotifForSaving):
            print 'Motif {0} saved to user motifs folder with {1} amino acids.'.format(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    # Replaces makemotif(2)
    def exportMotif(self):
        if self.makeMotifWrapper(self.openMotifForExporting, self.closeMotifForExporting):
            print 'Motif {0} exported with {1} amino acids.'.format(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    # Fault-tolerant wrapper
    def makeMotifWrapper(self, openFunction, closeFunction):
        retVal = False
        try:
            retVal = self.makeMotifCore(openFunction, closeFunction)
        except IOError as problem:
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
                           'val':('CB','CG1','CG2')}
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
