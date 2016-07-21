##from pymol import cmd
##from pymol import stored
import Tkinter as tk
import os
import re
import time
import math
import commands
import csv
from tkFileDialog import asksaveasfile, askdirectory, askopenfile, asksaveasfilename
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
from treewidgets import widget, node, texttree
from treewidgets.constants import *
import tkFileDialog
import ProMol.promolglobals as glb
import ProMol.promolobjects as promolobjects
import ProMol.Methods.proutils as proutils
import ProMol.Methods.motifset as motifset
import client
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
pdbsl = 0

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
                cmd.set('sphere_scale','0.15','substrate')
                cmd.show('spheres', 'substrate')
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
                cmd.set('sphere_scale','0.15','substrate')
                cmd.show('spheres', 'substrate')
                cmd.deselect()
                cpksubstrate()
    except:
        showinfo('Alert', "No substrate found")

def hidesubstrate():
    try:
        cmd.hide('sticks', 'substrate')
        cmd.hide('spheres', 'substrate')
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
            else:
                num_residues = cmd.count_atoms("name ca and " + motif)
                if num_residues < 2:
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
    querynode = ancs[1] # we want the query name, which is the 2nd ancestor... EC# is the first

    print motifString
    
    # The next three ifs added by Kip to prevent crash when double clicking header
    # One might have sufficed unless something unexpected ends up in motifbox
    
    if not motifString.startswith(' '):
        return

    savefilename = asksaveasfilename(defaultextension='.pdb',initialdir=glb.RESULTFOLDER)
    if savefilename=='': #in case user hits cancel
        return
    glb.RESULTFOLDER = os.path.dirname(savefilename) #in case user wants it elsewhere from default, don't have to go back and find the folder again
    result = glb.matchpairs[(querynode.getName(),motifString)]
    result.writeMotif(savefilename)
    
##    tag = motifString.split(': ')
##    if len(tag) != 2:
##        return
##    motifName = tag[1]
##    secondsplit = motifName.split('_')
##    if len(secondsplit) < 2:
##        return
##    motifPDBCode = secondsplit[1] # tpdb
##    queryPDBCode = querynode.getName()
##    
##    cmd.reinitialize()
##    motifColor = glb.GUI.motifs['motifcolor']['bg']
##    queryColor = glb.GUI.motifs['querycolor']['bg']
##    if glb.GUI.motifs['align'].get() == 0 or motifPDBCode == queryPDBCode:
##        cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)#accessing pdb file
##        if motifName in glb.MOTIFS:
##            
##            MotifCaller(motifName)
##            
##            querySubsetName = 'matching_subset'
##            # Actually renames the query protein matching subset
##            # because the selection named after the motif contains the matching subset
##            # of atoms on the query protein given to us by the motif
##            cmd.select(querySubsetName, motifName)
##            # I hope this is OK to delete
##            cmd.delete(motifName)
##            cmd.set_color('matchcolor',
##                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
##            cmd.color('matchcolor', 'matching_subset')
##        else:
##            glb.update()
##    else:      
##        if motifName in glb.MOTIFS:
##            cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)
##            cmd.hide('everything', 'all')
##            
##            # Run the motif
##            MotifCaller(motifName)
##            
##            #querySubsetName = 'match_in_{0}'.format(queryPDBCode)
##            querySubsetName = 'match_in_%s'%(queryPDBCode)
##            # Actually renames the query protein matching subset
##            # because the selection named after the motif contains the matching subset
##            # of atoms on the query protein given to us by the motif
##            cmd.select(querySubsetName, motifName)
##            cmd.hide('everything', 'all')
##            cmd.fetch(motifPDBCode, async=0, path=glb.FETCH_PATH)
##            # Removed cartoon show command
##            # Create named subset of matching result protein atoms
##            #motifSubsetName = 'match_in_{0}'.format(motifPDBCode)
##            motifSubsetName = 'match_in_%s'%(motifPDBCode)
##            cmd.select(motifSubsetName, '%s and (%s)' % (motifPDBCode,
##                glb.MOTIFS[motifName]['loci']))
##            # Do final display
##            cmd.hide('everything', 'all')
##            cmd.bg_color('white')
##            cmd.show('sticks', motifSubsetName)
##            cmd.show('spheres',motifSubsetName)
##            cmd.set('sphere_scale','0.15',motifSubsetName)
##            cmd.show('sticks', querySubsetName)
##            cmd.show('spheres',querySubsetName)
##            cmd.set('sphere_scale','0.15',querySubsetName)
##            # Removed ineffective cmd.color of matching subset
##
##            #aligns and gets the rmsd of the alignment by all atoms
##            data1 = cmd.align(motifSubsetName, querySubsetName)#edited 2/19
##            cmd.set_color('motifColor',
##                ([int(n, 16) for n in (motifColor[1:3], motifColor[3:5], motifColor[5:7])]))
##            cmd.set_color('queryColor',
##                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
##            cmd.color('motifColor', motifPDBCode)
##            cmd.color('queryColor', queryPDBCode)
##            cmd.orient(motifSubsetName)           
##
##            #added 2/19
##            if glb.GUI.motifs['rmsd'].get() != 0:
##                print repr(data1[6]) + " residues were aligned and " + repr(data1[1]) + " atoms."
##                print "rmsd of the alignment using all atoms = " + repr(data1[0]) #added         
##                #aligns and gets the rmsd of the alignment by C alpha atoms
##                cmd.select(querySubsetName, motifName+" and name ca")#added
##                cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
##                glb.MOTIFS[motifName]['loci'], "ca"))#added
##                data2 = cmd.align(motifSubsetName, querySubsetName)#added
##                print repr(data2[6]) + " residues were aligned and " + repr(data2[1]) + " atoms."
##                print "rmsd of the alignment using ca atoms = " + repr(data2[0]) #added
##
##                #aligns and gets the rmsd of the alignment by C alpha and C beta atoms
##                cmd.select(querySubsetName, motifName+" and name ca,cb")#edited
##                cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
##                glb.MOTIFS[motifName]['loci'], "ca,cb"))#edited
##                data3 = cmd.align(motifSubsetName, querySubsetName)#edited
##                print repr(data3[6]) + " residues were aligned and " + repr(data3[1]) + " atoms."
##                print "rmsd of the alignment using ca and cb atoms = " + repr(data3[0]) #added
##            ###
##
##    
##            
##            # I hope this is OK to delete
##            cmd.delete(motifName)
##            # Added by Kip to show both proteins in subsets
##            glb.populate()

def exportAllResults():
    defaultfile = fullCSVFilename(CSVMergeInfo['motif set short description'], CSVMergeInfo['start time'])
    #with asksaveasfile(initialfile=defaultfile, defaultextension='.csv', filetypes=[('Comma Separated Value files','*.csv'), ('All files','*.*')], title='Export Motif Finder Results As...') as outhandle:
    outhandle =  asksaveasfile(initialfile=defaultfile, defaultextension='.csv', filetypes=[('Comma Separated Value files','*.csv'), ('All files','*.*')], title='Export Motif Finder Results As...')
    if outhandle==None: #prevents ProMol from freaking out if user hits cancel after selecting export CSV file
        return
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
    ecchoice1 = glb.GUI.motifs['ec1'].get()
    if ecchoice1 == '' or int(ecchoice1) == 0:
        ecchoice1 = ''
        glb.GUI.motifs['ec1'].set('')
        glb.GUI.motifs['ec2'].set('')
        glb.GUI.motifs['ec2button'].config(state = DISABLED)
        glb.GUI.motifs['ec3'].set('')
        glb.GUI.motifs['ec3button'].config(state = DISABLED)
        glb.GUI.motifs['ec4'].set('')
        glb.GUI.motifs['ec4button'].config(state = DISABLED)
    ecchoice2 = glb.GUI.motifs['ec2'].get()
    if ecchoice2 == '' or int(ecchoice2) == 0:
        ecchoice2 = ''
        glb.GUI.motifs['ec2'].set('')
        glb.GUI.motifs['ec2button'].config(state = DISABLED)
        glb.GUI.motifs['ec3'].set('')
        glb.GUI.motifs['ec3button'].config(state = DISABLED)
        glb.GUI.motifs['ec4'].set('')
        glb.GUI.motifs['ec4button'].config(state = DISABLED)
    ecchoice3 = glb.GUI.motifs['ec3'].get()
    if ecchoice3 == '' or int(ecchoice3) == 0:
        ecchoice3 = ''
        glb.GUI.motifs['ec3'].set('')
        glb.GUI.motifs['ec3button'].config(state = DISABLED)
        glb.GUI.motifs['ec4'].set('')
        glb.GUI.motifs['ec4button'].config(state = DISABLED)
    ecchoice4 = glb.GUI.motifs['ec4'].get()
    if ecchoice4 == '' or int(ecchoice4) == 0:
        ecchoice4 = ''
        glb.GUI.motifs['ec4'].set('')
        glb.GUI.motifs['ec4button'].config(state = DISABLED)
    ecchoices = [ecchoice1, ecchoice2, ecchoice3, ecchoice4]
    pfamchoice = glb.GUI.motifs['pfam'].get().replace(' ','-').upper()
    motifchecker(selectedSet, rmsdchoice, ecchoices, pfamchoice)

def cancelSetChoice():#action of the cancel button
    glb.GUI.motifs['root'].withdraw()
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL

## Used to set EC input boxes to be enabled/disabled as user inputs numbers.
#  @param event Keyboard event.
#  @param maxNum Maximum value that the EC number can have.
#  @param nextBoxes The rest of the boxes following the current input box.
#
#  Utility function
def checkEC(event, maxNum, nextBoxes):
    # if arrow keys were pressed, do nothing
    if event.keysym == 'Right' or event.keysym == 'Left' or event.keysym == 'Up' or event.keysym == 'Down':
        return
    
    input = event.widget.get()
    
    # if content was deleted, disable next boxes
    if event.keysym == 'BackSpace' and len(input) == 0:
        for box in nextBoxes:
            box.delete(0, END)
            box.config(state = DISABLED)
    
    if len(input) > 0:
        # if current input is invalid, erase it
        if not input.isdigit() or int(input) < 1 or int(input) > maxNum:
            event.widget.delete(0, END)
            for box in nextBoxes:
                box.delete(0, END)
                box.config(state = DISABLED)
            return
        # if input is valid, let next box be enabled
        nextBoxes[0].config(state = NORMAL)
        if maxNum == 6: # if this is the first EC box, there are only 6 options
            nextBoxes[0].focus()
        if len(input) == 2: # if not first box, shift focus to next box when there are two digits
            nextBoxes[0].focus()

def commandrb1():
    if glb.GUI.motifs['varPset'].get() == 1:
      glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x1)
    else:
      glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x1)
def commandrb2():
    if glb.GUI.motifs['varJset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x2)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x2)
def commandrb3():
    if glb.GUI.motifs['varNset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x4)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x4)
def commandrb4():
    if glb.GUI.motifs['var'].get() != 0:
        # all implies all the sets
        glb.GUI.motifs['controls']['rb1'].select()
        if glb.USE_JESS:
            glb.GUI.motifs['controls']['rb2'].select()
        #glb.GUI.motifs['controls']['rb3'].select()
        glb.GUI.motifs['controls']['rb5'].select()
        glb.GUI.motifs['controls']['rbA'].select()
        glb.GUI.motifs['controls']['rbB'].select()
        glb.GUI.motifs['controls']['rbC'].select()
        glb.GUI.motifs['controls']['rbD'].select()
    else:
        # all implies all the sets
        glb.GUI.motifs['controls']['rb1'].deselect()
        if glb.USE_JESS:
            glb.GUI.motifs['controls']['rb2'].deselect()
        #glb.GUI.motifs['controls']['rb3'].deselect()
        glb.GUI.motifs['controls']['rb5'].deselect()
        glb.GUI.motifs['controls']['rbA'].deselect()
        glb.GUI.motifs['controls']['rbB'].deselect()
        glb.GUI.motifs['controls']['rbC'].deselect()
        glb.GUI.motifs['controls']['rbD'].deselect()
def commandrb5():
    if glb.GUI.motifs['varUset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x10)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x10)
def commandrbA():
    if glb.GUI.motifs['varAset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x20)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x20)
def commandrbB():
    if glb.GUI.motifs['varMset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x40)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x40)
def commandrbC():
    if glb.GUI.motifs['varRset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x80)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x80)
def commandrbD():
    if glb.GUI.motifs['varFset'].get() == 1:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()|0x100)
    else:
        glb.GUI.motifs['var'].set(glb.GUI.motifs['var'].get()&~0x100)


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
    glb.GUI.motifs['varPset'] = IntVar()
    if glb.USE_JESS:
        glb.GUI.motifs['varJset'] = IntVar()
    #glb.GUI.motifs['varNset'] = IntVar()
    glb.GUI.motifs['varUset'] = IntVar()
    glb.GUI.motifs['varAset'] = IntVar()
    glb.GUI.motifs['varMset'] = IntVar()
    glb.GUI.motifs['varRset'] = IntVar()
    glb.GUI.motifs['varFset'] = IntVar()


    #added 2/19
    glb.GUI.motifs['varrmsd'] = IntVar()
    ###
    
##    glb.GUI.motifs['controls'] = {}
##    
##    glb.GUI.motifs['controls']['rb1'] = Checkbutton(glb.GUI.motifs['root'], text="P set", variable = glb.GUI.motifs['varPset'], height = 2, command = commandrb1)
##    if glb.USE_JESS:
##        glb.GUI.motifs['controls']['rb2'] = Checkbutton(glb.GUI.motifs['root'], text="J set", variable = glb.GUI.motifs['varJset'], height = 2, command = commandrb2)
##    #rb3 = Checkbutton(glb.GUI.motifs['root'], text="N set (NMR)", variable = glb.GUI.motifs['varNset'], height = 2, command = commandrb3)
##    glb.GUI.motifs['controls']['rb4'] = Checkbutton(glb.GUI.motifs['root'], text="All Motifs", variable = glb.GUI.motifs['var'], onvalue = 0xF7, height = 2, command = commandrb4)
##    glb.GUI.motifs['controls']['rb5'] = Checkbutton(glb.GUI.motifs['root'], text="User Motifs", variable = glb.GUI.motifs['varUset'], height = 2, command = commandrb5)
##    glb.GUI.motifs['controls']['rbA'] = Checkbutton(glb.GUI.motifs['root'], text="A set", variable = glb.GUI.motifs['varAset'], height = 2, command = commandrbA)
##    glb.GUI.motifs['controls']['rbB'] = Checkbutton(glb.GUI.motifs['root'], text="Metal Amino", variable = glb.GUI.motifs['varMset'], height = 2, command = commandrbB)
##    glb.GUI.motifs['controls']['rbC'] = Checkbutton(glb.GUI.motifs['root'], text="Metal Other", variable = glb.GUI.motifs['varRset'], height = 2, command = commandrbC)
##    glb.GUI.motifs['controls']['rbD'] = Checkbutton(glb.GUI.motifs['root'], text="Pfam Motifs", variable = glb.GUI.motifs['varFset'], height = 2, command = commandrbD)


    #added 2/19
    rb6 = Radiobutton(glb.GUI.motifs['root'], text="Yes (will take longer)", variable = glb.GUI.motifs['varrmsd'], value = 1,  height = 2)
    rb7 = Radiobutton(glb.GUI.motifs['root'], text="No", variable = glb.GUI.motifs['varrmsd'], value = 2, height = 2)

    spacelabel = Label(glb.GUI.motifs['root'], text="")
    rmsdlabel = Label(glb.GUI.motifs['root'], text="Calculate RMSD?")
    ###




##    glb.GUI.motifs['controls']['rb4'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rb5'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rb1'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rbA'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rbB'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rbC'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rbD'].pack(anchor = W)
##    if glb.USE_JESS:
##        glb.GUI.motifs['controls']['rb2'].pack(anchor = W)
##    #glb.GUI.motifs['controls']['rb3'].pack(anchor = W)
##    glb.GUI.motifs['controls']['rb4'].select()#added 2/19 (default button)
##    commandrb4();


    #added 2/19
    spacelabel.pack(anchor = W)
    rmsdlabel.pack(anchor = W)
    rb6.pack(anchor = W)
    rb7.pack(anchor = W)
    rb7.select()
    ###
    
    #########################################################################
    ##  EC NUMBER                                                          ##
    #########################################################################
    # create Entry boxes for EC numbers. All are disabled except for first box (to start)
    EClabel = Label(glb.GUI.motifs['root'], text="\nLimit results by EC number")
    ECLabel1 = Label(glb.GUI.motifs['root'], text="EC Number: ")
    EC1 = Entry(glb.GUI.motifs['root'], state=NORMAL, textvariable = glb.GUI.motifs['ec1'], width=1)
    ECLabel2 = Label(glb.GUI.motifs['root'], text=".")
    EC2 = Entry(glb.GUI.motifs['root'], state=DISABLED, textvariable = glb.GUI.motifs['ec2'], width=2)
    ECLabel3 = Label(glb.GUI.motifs['root'], text=".")
    EC3 = Entry(glb.GUI.motifs['root'], state=DISABLED, textvariable = glb.GUI.motifs['ec3'], width=2)
    ECLabel4 = Label(glb.GUI.motifs['root'], text=".")
    EC4 = Entry(glb.GUI.motifs['root'], state=DISABLED, textvariable = glb.GUI.motifs['ec4'], width=2)

    glb.GUI.motifs['ec1button'] = EC1
    glb.GUI.motifs['ec2button'] = EC2
    glb.GUI.motifs['ec3button'] = EC3
    glb.GUI.motifs['ec4button'] = EC4

    if glb.GUI.motifs['ec2'].get != '':
        EC2.config(state = NORMAL)
    if glb.GUI.motifs['ec3'].get != '':
        EC3.config(state = NORMAL)
    if glb.GUI.motifs['ec4'].get != '':
        EC4.config(state = NORMAL)

    EClabel.pack(anchor = W)
    ECLabel1.pack(side=LEFT)
    EC1.pack(side=LEFT)
    ECLabel2.pack(side=LEFT)
    EC2.pack(side=LEFT)
    ECLabel3.pack(side=LEFT)
    EC3.pack(side=LEFT)
    ECLabel4.pack(side=LEFT)
    EC4.pack(side=LEFT)
    # bind function to the release of a key: we want to activate 2nd box iff there is valid text in first box
    # lambda lets there be an additional argument to the checkEC function
    EC1.bind('<KeyRelease>', lambda event: checkEC(event, 6, [EC2, EC3, EC4]))
    EC2.bind('<KeyRelease>', lambda event: checkEC(event, 99, [EC3, EC4]))
    EC3.bind('<KeyRelease>', lambda event: checkEC(event, 99, [EC4]))

    #Pfam name search
    PfamLabel = Label(glb.GUI.motifs['root'], text="\nLimit results by Pfam Family")
    PfamLabel1 = Label(glb.GUI.motifs['root'], text="Pfam Accession Number: ")
    PfamName = Entry(glb.GUI.motifs['root'], state=NORMAL, textvariable = glb.GUI.motifs['pfam'], width=12)

    PfamLabel.pack(anchor = W)
    PfamLabel1.pack(anchor = W)
    PfamName.pack(anchor = W)
    
    frame = Frame(glb.GUI.motifs['root'], width=150, height=350, bd=1)
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

    print "prepping export"
    csv = []
    csv.append('%s_meta'%(pdb))
    csv.append('PDBID,Version,Date,PF,MotifSets,motifcount')
    csv.append('%s,%s,%s,%s,%s,%d'%(pdb,glb.VERSION,time.asctime(searchStartTime),precisionFactor,motifSet.longDescription,len(found)))
    csv.append('')
    """
    metaLine = 'Motif Finder Results,,Generated by ProMOL version %s' %(glb.VERSION) +

    
    csv = ['Motif Finder Results,,Generated by ProMOL version %s'%(glb.VERSION),
    'Search started at %s,,Precision factor: %s,,Algorithm version: %s'%(time.asctime(searchStartTime), precisionFactor, glb.ALG_VERSION),
    '"Motif set: %s"'%(motifSet.longDescription),"""
    csv.append('%s_results'%(pdb))
    csv.append('PDB Entry,set,MotifTemplate,ec1,ec2,ec3,ec4,Edit Distance Range, RMSD_total, RMSD_alpha_beta, RMSD_alpha,r1,r2,r3,r4,r5')
 
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
        motif = result.strip()
        
        #ldr = resultdb[motif]['levdistrange']

        #added 2/19
        if rmsdState == True:
            motifrmsds = resultdb[motif]['rmsd']
        else:
            motifrmsds = [-1,-1,-1]
        
        pfam = resultdb[motif].pfam
        residues = resultdb[motif].residues
        ec = resultdb[motif].ec
        tmp = ec.split('.')
        same = {}
        motifline = True
        for residue in residues:
            chain = residue[0]
            resn = residue[1]
            resi = residue[2]

            #concatinates the chain, residue, and position in protein
            res = residue[0] +"-"+residue[1]+"-"+residue[2]

            key = '%s%s'%(resn,resi)
            
            #motif split into set, template, and ec numbers. seperate column for each
            moti = motif.split('_')
            moti.pop(1)
            mot = ","
            for m in moti:
            	mot += m + "," 
            
            motif += mot
            for m in tmp:
            	motif += m +","
            mot = mot[:-2]
            
            if lastpdb != pdb:
            	csv.append('%s,%s"%s",%s,%f,%f,%f,%s'%(str(pdb),motif,pfam,str(ldr),round(float(motifrmsds[0]),4),round(float(motifrmsds[1]),4),round(float(motifrmsds[2]),4),res))
            	lastpdb = pdb
            	motifline = False
            	continue
            if motifline:
            	csv.append('%s,%s"%s",%s,%f,%f,%f,%s'%(str(pdb),motif,pfam,str(ldr),round(float(motifrmsds[0]),4),round(float(motifrmsds[1]),4),round(float(motifrmsds[2]),4),res))
            	motifline = False
            	continue
            csv[-1] += ',%s'%(res)

        pdbMotifs.add(motif)
        
    csvfile = "\n".join(csv)
    fname = partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime)
    csvhandle = open(os.path.join(glb.CSV_PATH,fname),'w')
    try:
	csvhandle.__enter__() 
        csvhandle.write(csvfile)
    finally:
        csvhandle.__exit__()
	
    print glb.CSV_PATH + "/" + fname
    print "read"
    if glb.using_db:
	print "in method"
	client.main('u',os.path.join(glb.CSV_PATH,fname))

# Create uniform timestamp for CSV filenames
def generateCSVTimeString(searchStartTime):
    return time.strftime('%b_%d_%Y_%H%M_%Z', searchStartTime)

# Create appropriate filenames for CSV files
def partialCSVFilename(pdb, motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    #return 'motiffinder_partial_{0}_{1}_{2}.csv'.format(pdb, motifSetName, stamp)
    return '%s_%s_%s.csv'%(pdb, motifSetName, stamp)

def fullCSVFilename(motifSetName, searchStartTime):
    stamp = generateCSVTimeString(searchStartTime)
    #return 'motiffinder_{0}_{1}.csv'.format(motifSetName, stamp)
    return '%s_%s.csv'%(motifSetName, stamp)

# This method is used for calculating levenshtein distance, but for the purposes
# of the stand-alone version of promol, only looking for exact matches. Even if
# substitutions were implimented, it would be a relatively simple matter of
# just checking which residues were different. In terms of missing residues,
# that would be a bit more difficult to implement. I am just going to comment
# this method out for now, and just have exact matches for results for now.
##def count(motif,pdb):
##    last = None
##    ordered = []
##    orderedchain = {}
##    bannedchain = []
##    stored.motif = []
##    editdist = []
##    
##    
##    cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
##    residues = glb.MOTIFS[motif]['resi']
##    residuesl = len(residues)*2
##    glb.GUI.motifs['csvprep'][pdb][motif] = {}
##    glb.GUI.motifs['csvprep'][pdb][motif]['res'] = []
##    for iteration in stored.motif:
##        if last != iteration:
##            last = iteration
##            glb.GUI.motifs['csvprep'][pdb][motif]['res'].append(iteration)
##            ordered.append(iteration[1].lower())
##            if iteration[0] not in orderedchain:
##                if iteration[0] not in bannedchain:
##                    orderedchain[iteration[0]] = []
##                else:
##                    continue
##            orderedchain[iteration[0]].append(iteration[1].lower())
##            if residuesl <= len(orderedchain[iteration[0]]):
##                bannedchain.append(iteration[0])
##                del orderedchain[iteration[0]]
##    if len(orderedchain) == 0 and residuesl <= len(ordered):
##        return None
##    substitutions = [None]
##    if motif[0] == 'J':
##        for c in ('asp','glu','asn','gln','thr','ser'):
##            if c in residues:
##                substitutions = proutils.createsubs(residues)
##                break
##    for chain in orderedchain:
##        editdist.append(proutils.levenshteinDistance(residues,orderedchain[chain]))
##        for sub in substitutions:
##            if sub == None:
##                break
##            editdist.append(proutils.levenshteinDistance(sub,orderedchain[chain]))
##    editdist.append(proutils.levenshteinDistance(residues,ordered))
##    for sub in substitutions:
##        if sub == None:
##            break
##        editdist.append(proutils.levenshteinDistance(sub,ordered))
##    mini = min(editdist)
##    maxi = max(editdist)
##    #print "motif ",motif," mini ",mini," maxi ",maxi
##    if (residuesl < 6 and mini > 0) or (residuesl < 12 and mini > 1) or (residuesl < 18 and mini > 2) or mini > 3:
##        return None
##    #glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
##    glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '%s-%s'%(mini,maxi) if mini<maxi else mini
##    # Removed storage of precision factor as it is the same for the entire search
##    return glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange']

def motifchecker(setChoice, rmsdchoice, ecchoices, pfamchoice):
    global CSVMergeInfo
    glb.GUI.motifs['cancel'] = False
    #glb.GUI.motifs['motifbox'].delete(0,tk.END)
    glb.matchpairs = {}
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
    #cmd.window('hide')
    
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
    
    keys = set()

    print not glb.full_run
    
    if not glb.full_run or not glb.using_db:
    	if ecchoices[0] != '':
            if ecchoices[1] != '':
                if ecchoices[2] != '':
                    if ecchoices[3] != '':
                        keys |= glb.ECDICT[ecchoices[0]][ecchoices[1]][ecchoices[2]][ecchoices[3]]
                    else:
                        for fourthec in glb.ECDICT[ecchoices[0]][ecchoices[1]][ecchoices[2]].keys():
                            keys |= glb.ECDICT[ecchoices[0]][ecchoices[1]][ecchoices[2]][fourthec]
                else:
                    for thirdec in glb.ECDICT[ecchoices[0]][ecchoices[1]].keys():
                        for fourthec in glb.ECDICT[ecchoices[0]][ecchoices[1]][thirdec].keys():
                            keys |= glb.ECDICT[ecchoices[0]][ecchoices[1]][thirdec][fourthec]
            else:
                for secondec in glb.ECDICT[ecchoices[0]].keys():
                    for thirdec in glb.ECDICT[ecchoices[0]][secondec].keys():
                        for fourthec in glb.ECDICT[ecchoices[0]][secondec][thirdec].keys():
                            keys |= glb.ECDICT[ecchoices[0]][secondec][thirdec][fourthec]
        else:
            for firstec in glb.ECDICT.keys():
                if firstec=='N/A':
                    keys |= glb.ECDICT[firstec]
                    continue
                for secondec in glb.ECDICT[firstec].keys():
                    for thirdec in glb.ECDICT[firstec][secondec].keys():
                        for fourthec in glb.ECDICT[firstec][secondec][thirdec].keys():	
                            keys |= glb.ECDICT[firstec][secondec][thirdec][fourthec]
    else:
    	keys = set(glb.MOTIFS.keys())
    	
    if pfamchoice!='':
        keys &= glb.PFAMDICT[pfamchoice]
    # This is a Python list comprehension
    #keys = set([motifName for motifName in glb.MOTIFS.keys() if setselection(motifName)])

    #4/29 added
    glb.GUI.motifs['tt'].destroy()#removes current tree displaying past results
    glb.GUI.motifs['tt'] = texttree.TextTree(glb.GUI.motifs['motifbox'],funcs={'showContent':showContent})#create new tree
    glb.GUI.motifs['tt'].pack(expand=YES,fill=BOTH)
    
  
    global numResultsOfEachQuery #added 3/8
    for pdbIndex in range(len(pdbs)):
        rmsds = []
        pdb = pdbs[pdbIndex]
        # Deleted founds initializer
        pdb = pdb.strip()
        found = {}
        last = 0.0
        keysL = len(keys)
        if keysL == 0:
            break
        keysLo = keysL*len(pdbs)
        glb.GUI.motifs['csvprep'][pdb] = {}
        try:
            queryProt = promolobjects.Protein()
            queryProt.getPDB(pdb)
        except IOError:
            print "could not obtain %s due to connection error"%(pdb)
            continue
        
        inDB = False
        if glb.using_db:
            if not glb.full_run:
                inDB = client.main('q',os.path.join(glb.CSV_PATH,pdb))
    
        motifs = []
        if inDB:
            with open(os.path.join(glb.CSV_PATH,pdb+".csv"), 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    motifs.append(row[1])
                keys = motifs[1:]
                keysL = len(motifs)-1

        if keysL == 0:
            break
        keysLo = keysL*len(pdbs)
        
        for motif in keys:
            # Check for cancellation and break out of inner loop
            if glb.GUI.motifs['cancel']:
                glb.GUI.motifs['single']['text'] = 'Click Start to begin'
                #glb.GUI.motifs['overall']['text'] = 'Search cancelled at {0}%'.format(int(baro))
                glb.GUI.motifs['overall']['text'] = 'Search cancelled at %s%%'%(int(baro))
                break

            motifProt = glb.MOTIFS[motif]
            
            d = float(glb.GUI.motifs['delta'].get())
            queryMatch = queryProt.searchMotif(motifProt,d)
            if queryMatch!=False:
                motifStr = '    %s'%(motif)
                try:
                    proutils.align(motifProt,queryMatch)
                except ValueError:
                    print 'Motif %s appears to have an incorrect number of atoms in a residue, RMSD won\'t work correctly for it'%(motif)
                found[motifStr] = queryMatch
            last += 1
            lasto += 1
            bar = (last/keysL)*100
            baro = (lasto/keysLo)*100
            glb.GUI.motifs['single']['text'] = '%s (%s of %s): %s%% complete'%(pdb, pdbIndex + 1, len(pdbs), int(bar))
            glb.GUI.motifs['overall']['text'] = 'Overall: %s%% complete'%(int(baro))
            glb.GUI.motifs['singlestatus'].SetProgressPercent(bar)
            glb.GUI.motifs['overallstatus'].SetProgressPercent(baro)
            glb.GUI.motifs['single'].update()

        # If cancelled, break out of outer loop too
        if glb.GUI.motifs['cancel']:
            break
        foundMotifs = list(found.keys())
        foundMotifs.sort()
        numResultsOfEachQuery.append(len(found))#added 3/8
        # Header line entry: both elements are the query PDB code
        #glb.matchpairs.append((pdb, pdb))
        rmsdState=False#added 2/19
        for result in foundMotifs:
            glb.matchpairs[(pdb, result)] = found[result]
            
            #added 2/19
            if rmsdchoice is 1:
                rmsdState = True
                motifName = result.strip()
                #if len(tag) > 1:
                motif = glb.MOTIFS[motifName]                   
                queryCode = pdb
                #cmd.reinitialize()
                #cmd.fetch(queryCode, async=0, path=glb.FETCH_PATH)
                #cmd.hide('everything', 'all')
                #MotifCaller(tag[1])
                try:
                    rmsd = proutils.getRMSD(motif, found[result])
                    #data1 = cmd.align('match_in_%s'%(motifPDBCode), 'match_in_%s'%(queryCode))
                    #score = proutils.score(data1[0],proutils.levenshteinDistance(motifPDBCode,queryCode),data1[6])
                except Exception,e:
                    print e
                    rmsd = -1
                    #data1 = cmd.align('match_in_%s'%(motifPDBCode), 'match_in_%s'%(queryCode))
                    #score = proutils.score(data1[0],proutils.levenshteinDistance(motifPDBCode,queryCode),data1[6])
                glb.GUI.motifs['csvprep'][pdb][motifName] = {}
                glb.GUI.motifs['csvprep'][pdb][motifName]['rmsd'] = rmsd
                glb.GUI.motifs['csvprep'][pdb][motifName]['pfam'] = glb.MOTIFS[motifName].pfam
                glb.GUI.motifs['csvprep'][pdb][motifName]['ec'] = glb.MOTIFS[motifName].ec
                #glb.GUI.motifs['csvprep'][pdb][motifName]['score'] = score
                   
                #count1 = count1+1
                #rmsdBar=(float(count1)/(len(pdbs)+len(found)-1))*100
                #glb.GUI.motifs['rmsdstatus'].SetProgressPercent(rmsdBar)
                #glb.GUI.motifs['rmsdlabel']['text'] = 'RMSD: {0}% complete'.format(int(rmsdBar))

        # Export the single-PDB CSV file
        setName = "CDB_motifs" # could probably be more specific once there are more motifs, but this should do for now
        motifSet = motifset.MotifSet(setName, setName, keys)
        if glb.using_db:
            if not inDB:
        	if glb.full_run:
                    exportCSVResults(searchStartTime, glb.GUI.motifs['delta'].get(), motifSet, pdb, found, glb.GUI.motifs['csvprep'][pdb], rmsdState)
        if len(CSVMergeInfo) == 0:
            CSVMergeInfo['motif set short description'] = setName
            CSVMergeInfo['start time'] = searchStartTime
            CSVMergeInfo['partial files'] = list()
        CSVMergeInfo['partial files'].append(partialCSVFilename(pdb, motifSet.shortDescription, searchStartTime))

    # I patched this code because lengtho - len(pdbs) was not returning the proper number of results.
    # -Kip
    numberOfResults = len(glb.matchpairs.keys())
    
    oldpdb = ""
    struct = {}
    #edited 2/19
    #if rmsdchoice is 1:
    struct['type'] = 'Document'
    struct['name'] = 'Results'
    struct['properties'] = NP_ROOT|NP_ALLOW_CHILDREN|NP_AUTOBUILD
    struct['children']=[]
    i = -1
        
    for query, motif in glb.matchpairs.keys():
        if query != oldpdb:
            j = -1
            struct['children'].append({'type':'Section','name':query,'children':[]}) 
            i=i+1
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #1','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #2','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #3','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #4','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #5','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'EC #6','children':[]})
            struct['children'][i]['children'].append({'type':'Subsection','name':'No EC Class','children':[]})
            
        oldpdb = query
        motifname = motif.strip()
        
        tokens = glb.MOTIFS[motifname].ec.split('.')
##            try:
##                subsection = int(tokens[2])
##            except:
##                #Pfam designation
##                subsection = 7
        if str.isdigit(tokens[0]):
            subsection = int(tokens[0])
        else:
            subsection = 7
        struct['children'][i]['children'][subsection-1]['children'].append({'type':'Subsection','name':motif,'children':[]})
        j=len(struct['children'][i]['children'][subsection-1]['children'])-1

        struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'EC #:  '+ glb.MOTIFS[motifname].ec})
        struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'PFAM #:  '+ glb.MOTIFS[motifname].pfam})
        
        if rmsdchoice is 1:
            try:
                struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'RMSD All:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifname]['rmsd'], 4))})
##                if len(glb.GUI.motifs['csvprep'][query][motifName]['rmsd']) > 0:
##                    struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'RMSD All:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][0], 4))})
##                if len(glb.GUI.motifs['csvprep'][query][motifName]['rmsd']) > 1:
##                    struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'RMSD alpha:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][1], 4))})
##                if len(glb.GUI.motifs['csvprep'][query][motifName]['rmsd']) > 2:
##                    struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'RMSD alpha & beta:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['rmsd'][2], 4))})
##                    if len(glb.GUI.motifs['csvprep'][query][motifName]['score']) > 0:
##                        struct['children'][i]['children'][subsection-1]['children'][j]['children'].append({'type':'Subsection','name':'Score:  '+ repr(round(glb.GUI.motifs['csvprep'][query][motifName]['score'], 4))})
            except:
                print "indexing error at i = ", i, ", j = ", j, ", subsection = ", subsection
             
        if query == motif:
            numberOfResults -= 1
            
    
        # The new matchpairs collection of ordered pairs
        # contains, in each element, the query PDB code and
        # the matching motif, in that order.  Header lines are
        # indicated by an entry with both parts containing
        # the query PDB code.
    ###
    
    
    
    glb.GUI.motifs['tt'].showTree(struct,DT_TWSTRUCT,-1,
        props=NP_AUTOBUILD|NP_ALLOW_CHILDREN,
        state=NS_EXPANDED)#add nodes from struct to the tree
    
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
    #cmd.window('show')

# Refactored motif maker

class MotifMaker:
    
    def __init__(self):
        pass

    # Maybe this should go in init()
    # But this is the initial refactoring from procedural code
    def doCommonSetup(self):
        glb.GUI.motif_maker['file'] = ''
        glb.GUI.motif_maker['wait'] = []
        glb.GUI.motif_maker['motif'] = promolobjects.Protein()
        glb.GUI.motif_maker['order'] = []
        self.pf = float(glb.GUI.motif_maker['pf'].get())
        self.pdb = glb.GUI.motif_maker['pdb'].get().upper()
        self.ecen = glb.GUI.motif_maker['ec'].get()
        self.pfam = glb.GUI.motif_maker['pfam'].get().upper()
##        urlfl = urllib2.urlopen('http://www.rcsb.org/pdb/rest/hmmer?structureId=' + fl.split('_')[1])
##        xmldt = urlfl.read()
##        urlfl.close()
##        pfamAccs = set()
##        for e in xmldt.split():
##            if re.match("pfamAcc=",e)!=None:
##                pfamAccs.add(e.split('"',1)[1].split('.',1)[0])
##        if lstPfams==[]:
##            self.pfam = ("N/A\n")
##        else:
##            for el in lstPfams[:-1]:
##                self.pfam += (el + ',')
##            self.pfam += lstPfams[-1]
##        lstPfams = list(pfamAccs)
        self.resn = {}
        self.resi = {}
        #self.backbone = {}
        self.chain = {}
        self.excepLoop = 0
        self.exceptions = ''
        self.ec = ''
        self.name = ''
        self.skip = {}
        self.numberOfAcids = 0
        self.fullPDB = promolobjects.Protein()
        #cmd.reinitialize()
        
    # replaces makemotif(3)
    def clear(self):
        self.doCommonSetup()
        self.resetRows()
        glb.GUI.motif_maker['pf'].delete(0,tk.END)
        glb.GUI.motif_maker['pf'].insert(0,'1.00')
        glb.GUI.motif_maker['pdb'].delete(0,tk.END)
        glb.GUI.motif_maker['ec'].delete(0,tk.END)
        glb.GUI.motif_maker['pfam'].delete(0,tk.END)

        
    def resetRows(self):
        for i in range(1,11):
            glb.GUI.motif_maker['resn'][i].delete(0,tk.END)
            glb.GUI.motif_maker['resi'][i].delete(0,tk.END)
            glb.GUI.motif_maker['chain'][i].delete(0,tk.END)
            #if glb.GUI.motif_maker['backbone'][i].get() == 'On':
            #    glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
        
    # replaces write(string != None)
    def buildMotif(self, string):
        glb.GUI.motif_maker['motif'].append(string)
    
    # Replaces write(open=True) with mode = 0 or 4
    def openMotifForTesting(self):
        return True
        
    # Replaces write(open=True) with mode = 1
    def openMotifForSaving(self):
        if os.path.exists(glb.pathmaker((self.name,'.pdb'),root=glb.USRMOTIFSFOLDER)) or    \
           os.path.exists(glb.pathmaker((self.name,'.pdb'),root=glb.MOTIFSFOLDER)):
            answer = askyesno('Motif Exists', 
            'A motif has already been made for PDB:%s.\n'%(self.pdb)+
            'Are you sure you want to replace it?')
            if answer == False:
                 return False
        glb.GUI.motif_maker['file'] = glb.pathmaker((self.name,'.pdb'),root=glb.USRMOTIFSFOLDER)
        return True
        
    # Replaces write(open=True) with mode=2
    def openMotifForExporting(self):
        pref = askdirectory(initialdir=glb.HOME)
        if os.access(pref,os.W_OK | os.X_OK):
            if os.path.exists(glb.pathmaker('Motifs',(self.name,'.pdb'),root=pref)):
                answer = askyesno('Motif Exists', 
                'This file exists at this location.\n'+
                'Are you sure you want to replace it?')
                if answer == False:
                    return False
            glb.GUI.motif_maker['file'] = glb.pathmaker((self.name,'.pdb'),root=pref)
        else:
            showerror('Access Denied','You do not have access to write to this folder.')
            return False
        return True

    # Replaces write(close=True) with mode=0 or 4
    def closeMotifForTesting(self):
        testProtein = None
        if glb.GUI.motif_maker['radio'].get() == 0:
            testProtein = promolobjects.Protein()
            testProtein.getPDB(self.pdb)
        if glb.GUI.motif_maker['radio'].get() == 1:
##            cmd.reinitialize()
##            cmd.fetch(glb.GUI.motif_maker['testpdb'].get(), async=0, path=glb.FETCH_PATH)
##            glb.update()
            testProtein = promolobjects.Protein()
            testProtein.getPDB(glb.GUI.motif_maker['testpdb'].get())
        elif glb.GUI.motif_maker['radio'].get() == 2:
            testProtein = glb.randompdb()
            if testProtein==False:
                print 'Unable to get random pdb'
                return False
        
##        lines = ''.join().split('\n')
##        for line in lines:
##            if line != '':
##                eval(line)
##        glb.procolor(self.name, show_all='cartoon', color_all='gray')
##        cmd.select('matching_subset', self.name)
##        # I think here it's OK to delete the motif name
##        cmd.delete(self.name)
##        cmd.orient('matching_subset')
##        matchMakerColor = glb.GUI.motif_maker['matchcolor']['bg']
##        cmd.set_color('matchmakercolor',
##            ([int(n, 16) for n in (matchMakerColor[1:3], matchMakerColor[3:5], matchMakerColor[5:7])]))
##        cmd.color('matchmakercolor', 'matching_subset')
##        cmd.deselect()
        if testProtein.searchMotif(glb.GUI.motif_maker['motif'],self.pf)!=False:
            showinfo(message='Found motif in %s'%(testProtein.name))
        else:
            showinfo(message='Did not find motif in %s'%(testProtein.name))
        return True
        
    # Replaces write(close=True) with mode=2
    def closeMotifForExporting(self):
        if glb.GUI.motif_maker['file'] != '':
           glb.GUI.motif_maker['motif'].writeMotif(glb.pathmaker((self.name,'.pdb'),root=glb.USRMOTIFSFOLDER))
        else:
            print 'No file written'
        return True
            
    # Replaces write(close=True) with mode=1
    def closeMotifForSaving(self):
        self.closeMotifForExporting()
        glb.loadMotifs([glb.USRMOTIFSFOLDER])
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
        #tempBone = glb.GUI.motif_maker['backbone'][startingRow].get()
        swapRow = startingRow - 1 if up else startingRow + 1
        glb.GUI.motif_maker['resn'][startingRow].delete(0, tk.END)
        glb.GUI.motif_maker['chain'][startingRow].delete(0, tk.END)
        glb.GUI.motif_maker['resi'][startingRow].delete(0, tk.END)
        
        glb.GUI.motif_maker['resn'][startingRow].insert(tk.END, glb.GUI.motif_maker['resn'][swapRow].get())
        glb.GUI.motif_maker['chain'][startingRow].insert(tk.END, glb.GUI.motif_maker['chain'][swapRow].get())
        glb.GUI.motif_maker['resi'][startingRow].insert(tk.END, glb.GUI.motif_maker['resi'][swapRow].get())
        #if tempBone != glb.GUI.motif_maker['backbone'][swapRow].get():
        #    glb.GUI.motif_maker['backbone'][startingRow].invoke('buttonup')
        
        glb.GUI.motif_maker['resn'][swapRow].delete(0, tk.END)
        glb.GUI.motif_maker['chain'][swapRow].delete(0, tk.END)
        glb.GUI.motif_maker['resi'][swapRow].delete(0, tk.END)
        
        glb.GUI.motif_maker['resn'][swapRow].insert(tk.END, tempResn)
        glb.GUI.motif_maker['chain'][swapRow].insert(tk.END, tempChain)
        glb.GUI.motif_maker['resi'][swapRow].insert(tk.END, tempResi)
        #if tempBone != glb.GUI.motif_maker['backbone'][swapRow].get():
        #    glb.GUI.motif_maker['backbone'][swapRow].invoke('buttonup')
            
        glb.GUI.motif_maker['selection'].set(swapRow)
        self.updateMoveButtonState()
        
    # Depends on doCommonSetup() already being called
    # Returns false if input was bad
    def validateInput(self):
        try:
            self.fullPDB.getPDB(self.pdb)
        except IOError:
            self.exceptions += 'Could not fetch %s'%(self.pdb)
        #cmd.fetch(self.pdb, async=0, path=glb.FETCH_PATH)
        #if (self.pdb not in cmd.get_names('all')) or (cmd.count_atoms(self.pdb) == 0):
        #    #self.exceptions += 'Could not fetch {0}'.format(self.pdb)
        #    self.exceptions += 'Could not fetch %s'%(self.pdb)
        #glb.update()
        if self.ecen=='' or self.pfam=='':
            self.exceptions += 'Please give an EC code and a Pfam/Uniprot accession number'
        elif self.ecen!='':
            preecs = self.ecen.split(',')
            for preec in preecs:
                try:
                    eclist = preec.split('.')
                    ec1,ec2,ec3,ec4 = eclist
                except ValueError:
                    self.exceptions += 'Please enter a correct EC code with 4 numbers with periods.\n'
                    continue
                else:
                    if len(ec1) != 1 or int(ec1) < 1 or int(ec1) > 7:
                        self.exceptions += 'The first number in an EC code has to be >= 1 and <= 7.\n'
                    if len(ec2) > 2 or len(ec2) < 1:
                        self.exceptions += 'The second number in an EC code has to be at most two digits.\n'
                    if len(ec3) > 2 or len(ec3) < 1:
                        self.exceptions += 'The third number in an EC code has to be at most two digits.\n'
                    if len(ec4) > 3 or len(ec4) < 1:
                        self.exceptions += 'The fourth number in an EC code has to be at most three digits.\n'
            self.ec = self.ecen.replace(' ','')
        else: #pfam given, but no ec
            self.ec = 'N/A'
        if self.pfam=='': #ec given but no pfam given (technically will do this if neither ec or pfam given, but doesn't matter because the motif won't save)
            self.pfam = 'N/A'
        else:
            for el in self.pfam.split(','):
                if re.search('^PF\d{5}$',el)==None and re.search('^[A-Z]\d{5}$',el)==None:
                    self.exceptions += 'Please give a Pfam accession number in the format PF##### or Uniprot number in the format of [LETTER]#####\n'
                    break
        glb.GUI.motif_maker['motif'].name = self.pdb
        glb.GUI.motif_maker['motif'].ec = self.ec
        glb.GUI.motif_maker['motif'].pfam = self.pfam.upper()
        glb.GUI.motif_maker['motif'].uniprot = self.pfam
        glb.GUI.motif_maker['motif'].residues = []
        self.skip = {}
        self.skip[0] = 0
        for i in range(1,11):
            # The old way of storing what order they were in is too complicated
            # This will try to set it once in the GUI and forget it
            g = i
            self.resi[g] = glb.GUI.motif_maker['resi'][g].get().strip()
            #self.backbone[g] = glb.GUI.motif_maker['backbone'][g].get()
            self.chain[g] = glb.GUI.motif_maker['chain'][g].get().strip().upper()
            self.resn[g] = self.acceptresn(glb.GUI.motif_maker['resn'][g].get().strip(),self.chain[g],self.resi[g]).upper()
            self.skip[g] = False
            if self.resn[g] == '' and self.resi[g] == '' and self.chain[g] == '':
                ### this gives us the ability to skip whole blocks
                self.skip[g] = True
                self.skip[0] += 1
            elif self.resn[g] != '' and self.resi[g] != '' and self.chain[g] != '':
                if self.resn[g] == None:
                    self.exceptions += 'Residue %s is not recongnized.\n'%(g)
##                elif cmd.count_atoms('%s/%s`%s/'%(self.chain[g],self.resn[g],self.resi[g])) == 0:
##                    self.exceptions += 'There is no %s at number %s on chain %s.\n'%(self.resn[g],self.resi[g],self.chain[g])
                #elif self.resn[g] == 'gly' and self.backbone[g] == 'Off':
                #    self.exceptions += 'Please turn on the backbone for glycine residue %s\n'%(g)
                noResidue = True
                for residue in self.fullPDB.residues:
                    if residue.name==self.resn[g] and residue.index==int(self.resi[g]) and residue.chain==self.chain[g]:
                        noResidue = False
                        residue.distances = {}
                        glb.GUI.motif_maker['motif'].residues.append(residue)
                if noResidue:
                    self.exceptions += 'There is no %s at number %s on chain %s.\n'%(self.resn[g],self.resi[g],self.chain[g])
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
        for res in glb.GUI.motif_maker['motif'].residues:
            for other in glb.GUI.motif_maker['motif'].residues:
                if res==other:
                    continue
                res.distances[other] = res.CACoordinates.distanceTo(other.CACoordinates)

        self.numberOfAcids = len(glb.GUI.motif_maker['motif'].residues)
        return True

    # Replaces makemotif(5.2)
    # Does not work properly: deletes additional rows beyond the first
    # containing the same amino acid even at different positions or on
    # different chains
##    def recommendOrder(self):
##        self.doCommonSetup()
##        if self.validateInput():
##            residuecounts = {}
##            for i in range(1,11):
##                h = glb.GUI.motif_maker['resn'][i].get()
##                if h == '':
##                    continue
##                cmd.select(h,'resn %s'%h)
##                residuecounts[cmd.count_atoms(h)/glb.AminoHashTable[h][0]] = i
##                cmd.delete(h)
##            keys = residuecounts.keys()
##            keys.sort()
##            residueorder = []
##            for key in keys:
##                residueorder.append(residuecounts[key])
##            print residueorder
##            
##            # I hope this is what the order means
##            # I take it residueorder[newRowIndex] = oldRowIndex
##            # The reordering calculation code above was added by a previous
##            # developer
##            newList = []
##            for oldRowIndex in residueorder:
##                currentRow = {}
##                for field in ('resn', 'chain', 'resi'):#, 'backbone'):
##                    currentRow[field] = glb.GUI.motif_maker[field][oldRowIndex].get()
##                newList.append(currentRow)
##            
##            self.resetRows()
##            
##            for newRowIndex in range(len(newList)):
##                currentRow = newList[newRowIndex]
##                for field in ('resn', 'chain', 'resi'):
##                    glb.GUI.motif_maker[field][newRowIndex + 1].delete(0, tk.END)
##                    glb.GUI.motif_maker[field][newRowIndex + 1].insert(tk.END, currentRow[field])
##                #if currentRow['backbone'] != glb.GUI.motif_maker['backbone'][newRowIndex + 1].get():
##                #    glb.GUI.motif_maker['backbone'][newRowIndex + 1].invoke('buttonup')
        
    # Replaces makemotif(0) and makemotif(4)
    def testMotif(self):
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
##        finally:
##            if glb.GUI.motif_maker['file'] != '':
##                if not glb.GUI.motif_maker['file'].closed:
##                    glb.GUI.motif_maker['file'].close()
        return retVal
    
    # Replaces most of makemotif(0, 1, 2, 4)
    # But don't call directly!
    def makeMotifCore(self, openFunction, closeFunction):
        self.doCommonSetup()
        if self.validateInput():
            self.name = '%s_%s_%s'%(self.ec,self.pfam,self.pdb)
##            self.buildMotif("'''\n")
##            self.buildMotif("FUNC:%s\n"%(self.name))
##            self.buildMotif("PDB:%s\n"%(self.pdb))
##            self.buildMotif("EC:%s\n"%(self.ec))
##            self.buildMotif("PFAM:%s\n"%(self.pfam))
##            self.buildMotif("RESI:%s\n"%(self.getresnstr()))
##            self.buildMotif("LOCI:%s\n"%(self.getlocistr()))
##            self.buildMotif("'''\n")
            if not openFunction():
                return False
            atomlist = {}
            ### backbone off aka just side chains from beta carbon onwards
##            atomlist[0] = {'ala':('CB',), # First comma added by Kip to make it a tuple
##                           'arg':('CB','CG','CD','NE','CZ','NH1','NH2'),
##                           'asn':('CB','CG','OD1','ND2'),
##                           'asp':('CB','CG','OD1','OD2'),
##                           'cys':('CB','SG'),
##                           'gln':('CB','CG','CD','OE1','NE2'),
##                           'glu':('CB','CG','CD','OE1','OE2'),
##                           'gly':(),
##                           'his':('CB','CG','ND1','CD2','CE1','NE2'),
##                           'ile':('CB','CG1','CG2','CD1'),
##                           'leu':('CB','CG','CD1','CD2'),
##                           'lys':('CB','CG','CD','CE','NZ'),
##                           'met':('CB','CG','SD','CE'),
##                           'phe':('CB','CG','CD1','CD2','CE1','CE2','CZ'),
##                           'pro':('CB','CG','CD'),
##                           'ser':('CB','OG'),
##                           'thr':('CB','OG1','CG2'),
##                           'trp':('CB','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'),
##                           'tyr':('CB','CG','CD1','CD2','CE1','CE2','CZ','OH'),
##                           'val':('CB','CG1','CG2'),
##                           'ca':('CA',),
##                           'mo':('MO',),
##                           '4mo':('MO',),
##                           'mg':('MG',),
##                           'zn':('ZN',),
##                           'mn':('MN',),
##                           'na':('NA',),
##                           'hem':('FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','C3B','C4B','CMB','CAB','CBB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D'),
##                           'b12':('CO','N21','N22','N23','N24','C1','C20','C2','C25','C26','C27','O28','N29','C3','C30','C31','C32','O34','N33','C4','C5','C35','C6','C7','C36','C37','C38','O39','N40','C8','C41','C42','C43','O44','N45','C9','C10','C11','C12','C46','C47','C13','C48','C49','C50','O51','N52','C14','C15','C53','C16','C17','C54','C55','C56','C57','O58','N59','C18','C60','C61','O63','N62','C19','C1P','C2P','C3P','O3','O4','O5','P','O2','C3R','C2R','O7R','C1R','O6R','C4R','C5R','O8R','N1B','C8B','C2B','N3B','C9B','C4B','C5B','C5M','C6B','C6M','C7B'),
##                           'cub':('C3Z','C2Z','C1Z','NZ','CU','MO','S','CZ','OM2','C4Z','OM1'),
##                           'fes':('FE1','FE2','S1','S2'),
##                           'mos':('MO','S','O1','O2'),
##                           'hea':('FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','OMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','C3B','C4B','CMB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D','C11','O11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27','FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','OMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','CMB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26','C27'),
##                           'cua':('CU1','CU2'),
##                           'fco':('FE','C1','N1','C2','N2','C3','O3'),
##                           'sf4':('FE1','FE2','FE3','FE4','S1','S2','S3','S4'),
##                           'f3s':('FE1','FE3','FE4','S1','S2','S3','S4'),
##                           'f43':('NI','NA','CHA','C1A','C2A','C3A','C4A','C5A','C6A','O7A','N8A','C9A','CAA','CBA','CCA','ODA','OEA','NB','CHB','C1B','C2B','C3B','C4B','N5B','C6B','O7B','C8B','C9B','CAB','CBB','CCB','ODB','OEB','NC','CHC','C1C','C2C','C3C','C4C','C5C','C6C','O7C','O8C','C8C','C9C','CAC','OBC','OCC','ND','CHD','C1D','C2D','C3D','C4D','C5D','C6D','C7D','O8D','C9D','CAD','OBD','OCD'),
##                           'fe2':('FE',),
##                           'cfm':('FE1','FE2','FE3','FE4','FE5','FE6','FE7','MO1','S1A','S4A','S3A','S2A','S1B','S2B','S3B','S4B','S5'),
##                           'clf':('FE1','FE2','FE3','FE4','S1','S2A','S4A','S3A','FE5','FE6','FE7','FE8','S2B','S3B','S4B'),
##                           'hec':('FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','C3B','C4B','CMB','CAB','CBB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D'),
##                           'cob':('CO','N21','N22','N23','N24','C1','C20','C2','C25','C26','C27','O28','N29','C3','C30','C31','C32','O34','N33','C4','C5','C35','C6','C7','C36','C37','C38','O39','N40','C8','C41','C42','C43','O44','N45','C9','C10','C11','C12','C46','C47','C13','C48','C49','C50','O51','N52','C14','C15','C53','C16','C17','C54','C55','C56','C57','O58','N59','C18','C60','C61','O63','N62','C19','C1P','C2P','C3P','O3','O4','O5','P','O2','C3R','C2R','O7R','C1R','O6R','C4R','C5R','O8R','N1B','C8B','C2B','N3B','C9B','C4B','C5B','C5M','C6B','C6M','C7B','C1A'),
##                           'c2o':('CU2','CU3','O1'),
##                           'pcd':('N1','C2','N3','C4','C5','C6','O2','N4','C1','C2D','O2','C3','C4D','O4D','O3','C5','O5','PA','O1A','O2A','O3A','PB','O1B','O2B','O3B','C10','C9','C8','S8','C7','S7','C6','C7','O9','N5','C4A','N8','C4B','N1','C2','N2','N3','C4','O4','MO','OR1','OM2','OM1'),
##                           '3co':('CO',),
##                           'co':('CO',),
##                           'ni':('NI',),
##                           'fe':('FE',),
##                           'cu':('CU',)}
##            atomlist[1] = ('O','C','CA','N')### backbone on
##            resnlist = ['']### residue list
##            resnlistf = ['']### residue list with appended 'i', making them unique
##            resilist = ['']### residue id list. Based on sequence number.
##            chainlist = ['']### chain list
###            bonelist = ['']### backbone list
##            
##            numOfi = {}
##            for i in range(1,11):
##                # This is the second place this was changed:
##                # From:
##                # g = glb.GUI.motif_maker['curorder'][i]
##                # To:
##                g = i
##                if not self.skip[g]:
##                    if self.resn[g] not in numOfi:
##                        numOfi[self.resn[g]] = 0
##                    resnlist.append(self.resn[g])
##                    resilist.append(self.resi[g])
##                    resnlistf.append(self.resn[g]+('i'*(numOfi[self.resn[g]])))
##                    chainlist.append(self.chain[g])
##                    #bonelist.append(self.backbone[g])
##                    numOfi[self.resn[g]] += 1
##            
##            ### This loop will increment through the amino acids. The amino acid we are looking
##            ### at right now is specified by the e variable. The a variable will count the
##            ### number of times it is compared to the carbons in the other amino acids. And is
##            ### used later on to print the "byres" and select line, and delete line below.
##            resnlen = (len(resnlist)-1)
##            e = 0
##            while e < resnlen:
##                a = 0
##                e += 1
##                ### select stuff explained later on
##                selectlimit = 50
##                selectstart = 1 ### where to start selection
##                selectlimiter = 1 ### limit defined as a/selectlimit
##                selectextra = [] ### add to selection at the end
##                deleteextra = [] ### add to deletion at the end
##                
##                #if bonelist[e] == 'Off':###just sidechains
##                #    bList=atomlist[0][resnlist[e]]
##                #else:### sidechain with backbone
##                #    bList=atomlist[0][resnlist[e]]+atomlist[1]
##                
##                ### This loop will increment through the amino acids that we want
##                ### to compare to the amino acid we want to find. The amino acid
##                ### being compared is specified by the d variable.
##                # d is also a variable used in closeMotifForTesting(), but
##                # the fact that it has gone out of and back into scope
##                # shouldn't matter here (they used to be in the same function)
##                
##                d = 0
##                while d < resnlen:
##                    d += 1
##                    ### The following line: compare amino acids
##                    ### If they are the same, then lets increment one.
##                    if resnlistf[e] == resnlistf[d]:
##                        d += 1
##                        if d > resnlen:
##                            continue
##                    
##                    #if bonelist[d] == 'Off':###just sidechains
##                    #    cList=atomlist[0][resnlist[d]]
##                    #else:### sidechain with backbone
##                    #    cList=atomlist[0][resnlist[d]]+atomlist[1]
##                    
##                    ### This loop increments through all the carbons
##                    ### in the amino acid we want to find.
##                    for eachB in bList:
##                        if cmd.count_atoms(chainlist[e]+'/'+resilist[e]+'/'+eachB) != 1:
##                            continue
##                        ### This loop increments through all the carbons
##                        ### in the other amino acids that we are want to
##                        ### compare with.
##                        for eachC in cList:
##                            if cmd.count_atoms(chainlist[d]+'/'+resilist[d]+'/'+eachC) != 1:
##                                continue
##                            ### Gets the distance between our atoms in our selected amino acids.
##                            r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+eachB,chainlist[d]+'/'+resilist[d]+'/'+eachC)
##                            ### The precision factor
##                            ### The ranger is the slider that is moved.
##                            ### r is set by the get_distance above.
##                            g = '%.2f' %(float(r) + float(self.pf))
##                            
##                            a += 1
##                            
##                            ### apparently pymol cannot handle over a number
##                            ### between 248 and 264 selections at one time.
##                            ### This fixes that by making sure we do not pass
##                            ### "selectlimit" selections at one time.
##                            if float(selectlimiter) < (float(a)/float(selectlimit)):
##                                self.buildMotif("cmd.select('%s%s',' "%(resnlistf[e],(selectlimiter*selectlimit)))
##                                for i in range(selectstart,a):
##                                    if i==(a-1):
##                                        self.buildMotif("br. %s%s')\n"%(resnlistf[e],i))
##                                    else:
##                                        self.buildMotif("br. %s%s&"%(resnlistf[e],i))
##                                for i in range(selectstart,a):
##                                    if i==(a-1):
##                                        pass
##                                    else:
##                                        self.buildMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
##                                selectextra.append('%s%s&'%(resnlistf[e],(selectlimiter*selectlimit)))
##                                deleteextra.append("cmd.delete('%s%s')\n"%(resnlistf[e],(selectlimiter*selectlimit)))
##                                selectlimiter += 1
##                                selectstart += selectlimit
##                            
##                            ### e > d is all the combinations of residues
##                            ### that would already have one of the residues
##                            ### found in the motif, therefore the second
##                            ### amino acid does not need an r. (resn)
##                            ### property selection, as it is already a selection.
##                            if e > d:
##                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlistf[d],g))
##                            else:
##                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlist[d],g))
##                self.buildMotif("cmd.select('%s',' "%(resnlistf[e]))
##                if selectextra != []:
##                    self.buildMotif(''.join(selectextra))
##                for i in range(selectstart,a+1):
##                    if i==a:
##                        self.buildMotif("br. %s%s')\n"%(resnlistf[e],i))
##                    else:
##                        self.buildMotif('br. %s%s&'%(resnlistf[e],i))
##                for x in deleteextra:
##                    self.buildMotif(x)
##                for i in range(selectstart,a+1):
##                    self.buildMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
##        
##            resnlistfstr = ""
##            for i in range(1,resnlen+1):
##                if i == resnlen:
##                    resnlistfstr += resnlistf[i]
##                else:
##                    resnlistfstr += resnlistf[i]+'|'
##        
##            self.buildMotif("cmd.select('%s', '%s')\n"%(self.name,resnlistfstr))
##            for i in range(1,resnlen+1):
##                self.buildMotif("cmd.delete('%s')\n"%(resnlistf[i]))
##            self.numberOfAcids = len(resnlist) - 1
            if closeFunction():
                return True
            return False
