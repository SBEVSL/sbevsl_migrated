from pymol import cmd
from pymol import stored
import Tkinter as tk
import Pmw
import os
import re
import time
from tkFileDialog import asksaveasfile, askdirectory, askopenfile
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
from pmg_tk.startup.ProMol import promolglobals as glb


#print dir(motcod)
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

def togglealign(event):
    if glb.GUI.motifs['align'].get() == 0:
        glb.GUI.motifs['querycolor']['relief'] = tk.SUNKEN
        glb.GUI.motifs['motifcolor']['relief'] = tk.SUNKEN
        glb.GUI.motifs['querycolor'].unbind("<ButtonRelease-1>")
        glb.GUI.motifs['motifcolor'].unbind("<ButtonRelease-1>")
    else:
        glb.GUI.motifs['querycolor']['relief'] = tk.RAISED
        glb.GUI.motifs['motifcolor']['relief'] = tk.RAISED
        glb.GUI.motifs['querycolor'].bind("<ButtonRelease-1>", changecolor)
        glb.GUI.motifs['motifcolor'].bind("<ButtonRelease-1>", changecolor)

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
    motif = glb.GUI.motifs['motifbox'].curselection()[0]
    motifString = glb.GUI.motifs['motifbox'].get(motif)
    # The next three ifs added by Kip to prevent crash when double clicking header
    # One might have sufficed unless something unexpected ends up in motifbox
    if not motifString.startswith(' '):
        return
    tag = motifString.split('-')
    if len(tag) != 2:
        return
    motifName = tag[1]
    secondsplit = motifName.split('_')
    if len(secondsplit) < 2:
        return
    motifPDBCode = secondsplit[1] # tpdb
    queryPDBCode = glb.GUI.motifs['hidmotif'].get(motif) # pdb
    cmd.reinitialize()
    if glb.GUI.motifs['align'].get() == 0 or motifPDBCode == queryPDBCode:
        cmd.fetch(queryPDBCode, async=0, path=glb.FETCH_PATH)
        if motifName in glb.MOTIFS:
            MotifCaller(motifName)
            
            querySubsetName = 'match_in_{0}'.format(queryPDBCode)
            # Actually renames the query protein matching subset
            # because the selection named after the motif contains the matching subset
            # of atoms on the query protein given to us by the motif
            cmd.select(querySubsetName, motifName)
        else:
            glb.update()
    else:      
        if motifName in glb.MOTIFS:
            motifColor = glb.GUI.motifs['motifcolor']['bg']
            queryColor = glb.GUI.motifs['querycolor']['bg']
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
            cmd.align(motifSubsetName, querySubsetName)
            cmd.set_color('motifColor',
                ([int(n, 16) for n in (motifColor[1:3], motifColor[3:5], motifColor[5:7])]))
            cmd.set_color('queryColor',
                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
            cmd.color('motifColor', motifPDBCode)
            cmd.color('queryColor', queryPDBCode)
            cmd.orient(motifSubsetName)
            # Added by Kip to show both proteins in subsets
            glb.populate()

def export2ods():
    pass

#Replaced this csv making function with my own
def export2csv():
    csv = ['PDB Entry,PDB Homologue,Motifs Found,Rank,Residues,,,, Motifs Not Found', #added Alg version and not found columns
        ',,,,Chain,Name,Number']
    motifs = glb.GUI.motifs['motifbox'].get(0,tk.END)
    pdbs = glb.GUI.motifs['hidmotif'].get(0,tk.END)
    lastpdb = None
    pdbMotifs = [] #motifs found for a given target
    allMotifs = [] #will contain the names of all motifs being used
    motifSet = glb.searchSet #MODIFIED for subset of motifs
    for item in motifSet:
        if item == 'errors':
            continue
        allMotifs.append(item)
    motifl = 0 #length of found motif list entered into csv
    resl = 0 #non-motif lines
    motifsl = len(motifs) #length of total found motif list to be entered
    fillFrom = 2 #line at which motifs not found start to be entered
    single = True #only one structure t/f
    while motifl < motifsl:
        try:
            motif = motifs[motifl].split('-')[1]
        except IndexError:
            motifl += 1
            continue
        pdb = pdbs[motifl]
        x = glb.GUI.motifs['csvprep'][pdb][motif]['x']
        pf = glb.GUI.motifs['csvprep'][pdb][motif]['pf']
        pdbstr = '%s@PF%s'%(pdb,pf)
        if 'hom' in glb.GUI.motifs['csvprep'][pdb][motif]:
            hom = '%s@PF%s'%(glb.GUI.motifs['csvprep'][pdb][motif]['hom'],pf)
        else:
            hom = ''
        residues = glb.GUI.motifs['csvprep'][pdb][motif]['res']
        same = {}
        motifline = True
        for residue in residues:
            chain = residue[0]
            resn = residue[1]
            resi = residue[2]
            key = '%s%s'%(resn,resi)
            if key in same:
                line = same[key]
                s = csv[line].split(',')
                csv[line] = '%s,%s,%s,%s,%s&%s,%s,%s'%(s[0],s[1],s[2],s[3],s[4],chain,s[5],s[6])
                continue
            resl += 1
            same[key] = len(csv)
            if lastpdb != pdb:
                if lastpdb != None:
                    pdbnfl = 0 #motifs not found entered for this structure
                    pdbmnf = list(set(allMotifs) - set(pdbMotifs)) # motifs not found for this structure = all motifs - motifs found for this structure
                    while pdbnfl < len(pdbmnf):  # Add motifs not found for this structure
                        for line in range(fillFrom, len(csv)):
                            if pdbnfl >= len(pdbmnf):
                                break
                            csv[line] += ',,%s'%(pdbmnf[pdbnfl])
                            pdbnfl += 1
                    fillFrom += resl
                    resl = 0
                    pdbMotifs = []
                    single = False
                csv.append('%s,%s,%s,[%s],%s,%s,%s'%(pdbstr,hom,motif,x,chain,resn,resi))
                lastpdb = pdb
                motifline = False
                continue
            if motifline == True:
                csv.append(',,%s,[%s],%s,%s,%s'%(motif,x,chain,resn,resi))
                motifline = False
                continue
            csv.append(',,,,%s,%s,%s'%(chain,resn,resi))
        if not motif in pdbMotifs:
            pdbMotifs.append(motif)
        motifl += 1
    pdbnfl = 0 #motifs not found entered for this structure
    pdbmnf = list(set(allMotifs) - set(pdbMotifs)) # motifs not found for this structure = all motifs - motifs found for this structure
    while pdbnfl < len(pdbmnf):  # Add motifs not found for this structure
        for line in range(fillFrom, len(csv)):
            if pdbnfl >= len(pdbmnf):
                break
            csv[line] += ',,%s'%(pdbmnf[pdbnfl])
            pdbnfl += 1
    csv.append('Precision Factor: %s'%(glb.GUI.motifs['delta'].get()))
    csv.append('Algorithm Version: %s'%(glb.ALG_VERSION))
    csvfile = "\n".join(csv)
    with asksaveasfile(initialfile='motiffinder.csv',defaultextension='.csv',
    filetypes=[('CSV','*.csv')],title='Export Motif Finder Results As...') as csvhandle:
        csvhandle.write(csvfile)

def motifcancel():
    glb.GUI.motifs['cancel'] = True

def storeSetChoice(): #stores button value, action of the select button
    glb.GUI.motifs['root'].withdraw()
    selectedSet = glb.GUI.motifs['var'].get()
    motifchecker(selectedSet)

def cancelSetChoice():#action of the cancel button
    glb.GUI.motifs['root'].withdraw()
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL

def setChoiceDialogBox(): #creates buttons on the dialog box that pops up when the user selects the start button in motif finder
    pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
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
    rb1 = Radiobutton(glb.GUI.motifs['root'], text="P set", variable = glb.GUI.motifs['var'], value = 1,  height = 2)
    rb2 = Radiobutton(glb.GUI.motifs['root'], text="J set", variable = glb.GUI.motifs['var'], value = 2, height = 2)
    #rb3 = Radiobutton(glb.GUI.motifs['root'], text="N set (NMR)", variable = glb.GUI.motifs['var'], value = 3, height = 2)
    rb4 = Radiobutton(glb.GUI.motifs['root'], text="All Motifs", variable = glb.GUI.motifs['var'], value = 4, height = 2)
    rb5 = Radiobutton(glb.GUI.motifs['root'], text="User Motifs", variable = glb.GUI.motifs['var'], value = 5, height = 2)

    rb4.pack(anchor = W)
    rb5.pack(anchor = W)
    rb1.pack(anchor = W)
    rb2.pack(anchor = W)
    #rb3.pack(anchor = W)
    
    frame = Frame(glb.GUI.motifs['root'], width=200, height=250, bd=1)
    frame.pack()
    
    selectButton = Button(frame, text='Select', command = storeSetChoice).pack()
    cancelButton = Button(frame, text='Cancel', command = cancelSetChoice).pack()
    glb.GUI.motifs['root'].update()
    glb.GUI.motifs['root'].deiconify()
    glb.GUI.motifs['root'].mainloop()


          
def motifchecker(setChoice):
    glb.GUI.motifs['cancel'] = False
    glb.GUI.motifs['motifbox'].delete(0,tk.END)
    glb.GUI.motifs['hidmotif'].delete(0,tk.END)
    glb.GUI.motifs['csvprep'] = {}
    glb.GUI.motifs['cancelbutton']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.DISABLED
    glb.GUI.motifs['csv']['state'] = tk.DISABLED
    glb.GUI.motifs['multipdb']['state'] = tk.DISABLED
    pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
    pdbsl = len(pdbs)
    
    def LevenshteinDistance(x,y):
        w,h = len(x)+1,len(y)+1
        #x+1 rows and y+1 columns
        matrix = [ [None]*h for i in range(w) ]
        for i in range(w):
            matrix[i][0] = i
        for j in range(h):
            matrix[0][j] = j
        for j in range(1,h):
            for i in range(1,w):
                if x[i-1] == y[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    #deletion,insertion,substitution
                    matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,
                        matrix[i-1][j-1]+1)
        return matrix[w-1][h-1] #edit distance
    
    def count(motif,pdb):
        def createsubs(tup):
            matrix = [[]]
            for acid in tup:
                newMatrix = []
                for subList in matrix:
                    identical = subList[:] # Slice copy as shown on http://docs.python.org/tutorial/controlflow.html section 4.2
                    identical.append(acid)
                    newMatrix.append(identical)
                    if 's' in glb.AminoHashTable[acid]:
                        substituted = subList[:]
                        substituted.append(glb.AminoHashTable[acid]['s'])
                        newMatrix.append(substituted)
                matrix = newMatrix
            return matrix
            # End of nested function

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
                    substitutions = createsubs(residues)
                    break
        for chain in orderedchain:
            editdist.append(LevenshteinDistance(residues,orderedchain[chain]))
            for sub in substitutions:
                if sub == None:
                    break
                editdist.append(LevenshteinDistance(sub,orderedchain[chain]))
        editdist.append(LevenshteinDistance(residues,ordered))
        for sub in substitutions:
            if sub == None:
                break
            editdist.append(LevenshteinDistance(sub,ordered))
        mini = min(editdist)
        maxi = max(editdist)
        glb.GUI.motifs['csvprep'][pdb][motif]['x'] = mini<maxi and '%s/%s'%(mini,maxi) or mini
        glb.GUI.motifs['csvprep'][pdb][motif]['pf'] = glb.GUI.motifs['delta'].get()
        return glb.GUI.motifs['csvprep'][pdb][motif]['x']

    lasto = 0.0
    
    # Initialize the progress bars
    # This call to update() may not be thread safe
    
    glb.GUI.motifs['single']['text'] = 'Searching... 0% Complete'
    glb.GUI.motifs['overall']['text'] = 'Overall... 0% Complete'
    glb.GUI.motifs['singlestatus'].SetProgressPercent(0.0)
    glb.GUI.motifs['overallstatus'].SetProgressPercent(0.0)
    glb.GUI.motifs['single'].update()
    for pdb in pdbs:
        founds = {}
        foundso = []
        pdb = pdb.strip()
        found = []
        last = 0.0
        keys = []
        if setChoice == 4:
            keys = glb.MOTIFS.keys() #gets all motifs that have been loaded in MOTIFS
            setName = 'All'
        else:
            allKeys = glb.MOTIFS.keys() #gets all motifs that have been loaded in MOTIFS
            if setChoice == 1:
                for key in allKeys:
                    if key[0] == 'P': #gets the motifs that begin with 'P'
                        keys.append(key)
                        setName = 'P_Set'
            if setChoice == 2:
                for key in allKeys:
                    if key[0] == 'J': #gets the motifs that begin with 'J'
                        keys.append(key)
                        setName = 'J_Set'
            if setChoice == 3:
                for key in allKeys:
                    if key[0] == 'N': #gets the motifs that begin with 'N'
                        keys.append(key)
                        setName = 'N_Set'
            if setChoice == 5:
                for key in allKeys:
                    if key[0] == 'U': #gets the motifs that begin with 'U'
                        keys.append(key)
                        setName = 'U_Set'
                        
        glb.searchSet = keys #Alex added, modified by Kip
        # I changed the following lines up to the break statement.  Hopefully it's right now. -Kip
        keysL = len(keys)
        if 'errors' in keys:
            # Don't count it
            keysL = keysL - 1
        if keysL == 0:
            break
        keysLo = keysL*len(pdbs)
        glb.GUI.motifs['csvprep'][pdb] = {}
        cmd.reinitialize()
        cmd.fetch(pdb, async=0, path=glb.FETCH_PATH)
        if (pdb not in cmd.get_names('all')) or (cmd.count_atoms(pdb) == 0):
            founds[pdb] = ['Could not fetch {0}'.format(pdb)] # Apparently never used anyway
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
                glb.GUI.motifs['overall']['text'] = 'Cancelled... {0}% Complete'.format(int(baro))
                break
                
            # List of motif loading errors is currently stored inside motif dictionary
            if motif == 'errors':
                continue
            
            # Determine whether or not we have a match
            if MotifCaller(motif,False):
                x = count(motif,pdb)
                if x != None:
                    motifStr = '    %s-%s'%(x,motif)
                    found.append(motifStr)
            cmd.delete(motif)
            
            # Update progress bars
            # Calling update() on GUI widgets from here may not be thread safe
            # We will try to fix as soon as possible
            
            last += 1
            lasto += 1
            bar = (last/keysL)*100
            baro = (lasto/keysLo)*100
            glb.GUI.motifs['single']['text'] = 'Searching... {0}% Complete'.format(int(bar))
            glb.GUI.motifs['overall']['text'] = 'Overall... {0}% Complete'.format(int(baro))
            glb.GUI.motifs['singlestatus'].SetProgressPercent(bar)
            glb.GUI.motifs['overallstatus'].SetProgressPercent(baro)
            glb.GUI.motifs['single'].update()

        # If cancelled, break out of outer loop too
        if glb.GUI.motifs['cancel']:
            break
        found.sort()
        founds[pdb] = found

        # This loop only iterates once per outer loop
        # It is unnecessary and will be removed in the next major release
        for f in founds:
            foundso.extend([f])
            foundso.extend(founds[f])

        for foundo in foundso:
            # pdb keeps track of the last query code in the list
            # before the current indented results (foundo)
            # pdb is the query that yielded the result foundo
            if len(foundo) == 4:
                pdb = foundo
            glb.GUI.motifs['motifbox'].insert(tk.END,foundo)
            glb.GUI.motifs['hidmotif'].insert(tk.END,pdb)

        # Export CSV file automatically
        # To-do: Combine this with the other CSV code and/or reimplement using Python's CSV library
        csv = ['PDB Entry,PDB Homologue,Motifs Found,Rank,Residues,,,,Motifs Not Found', #added Alg version and not found columns
        ',,,,Chain,Name,Number']
        motifs = foundso
        allMotifs = []
        pdbMotifs = []
        motifSet = glb.searchSet #MODIFIED for subset of motifs
        for item in motifSet:
            if item == 'errors':
                continue
            allMotifs.append(item)
        lastpdb = None
        fillFrom = 2
        motifl = 0
        motifsl = len(motifs)
        while motifl < motifsl:
            try:
                motif = motifs[motifl].split('-')[1]
            except IndexError:
                motifl += 1
                continue
            
            x = glb.GUI.motifs['csvprep'][pdb][motif]['x']
            pf = glb.GUI.motifs['csvprep'][pdb][motif]['pf']
            pdbstr = '%s@PF%s'%(pdb,pf)
            if 'hom' in glb.GUI.motifs['csvprep'][pdb][motif]:
                hom = '%s@PF%s'%(glb.GUI.motifs['csvprep'][pdb][motif]['hom'],pf)
            else:
                hom = ''
            residues = glb.GUI.motifs['csvprep'][pdb][motif]['res']
            same = {}
            motifline = True
            for residue in residues:
                chain = residue[0]
                resn = residue[1]
                resi = residue[2]
                key = '%s%s'%(resn,resi)
                if key in same:
                    line = same[key]
                    s = csv[line].split(',')
                    csv[line] = '%s,%s,%s,%s,%s&%s,%s,%s'%(s[0],s[1],s[2],s[3],s[4],chain,s[5],s[6])
                    continue
                same[key] = len(csv)
                if lastpdb != pdb:
                    csv.append('%s,%s,%s,[%s],%s,%s,%s'%(pdbstr,hom,motif,x,chain,resn,resi))
                    lastpdb = pdb
                    motifline = False
                    continue
                if motifline == True:
                    csv.append(',,%s,[%s],%s,%s,%s'%(motif,x,chain,resn,resi))
                    motifline = False
                    continue
                csv.append(',,,,%s,%s,%s'%(chain,resn,resi))
            if not motif in pdbMotifs:
                pdbMotifs.append(motif)
            motifl += 1
        # Fix for if there are absolutely no matches: make room for not found list
        # Before I rewrote the bigger loop it created an infinite loop because pdbfnl
        # (the not found list loop index) was never incremented, causing ProMol to hang
        # because the inner lines for loop was never run (fillFrom and len(csv) were both 2)
        # That for loop is now gone; now, without this while loop, it would cause
        # an IndexError instead (csv[2] with csv of length 2) -Kip
        notFoundList = list(set(allMotifs) - set(pdbMotifs)) # motifs not found for this structure = all motifs - motifs found for this structure
        while len(csv) < fillFrom + min(20, len(notFoundList)):
            csv.append(',,,,,,')
        line = fillFrom
        wrapped = False
        for notFoundMotif in notFoundList: # Add motifs not found for this structure
            if (line >= len(csv)): # Start over at the top
                line = fillFrom
                wrapped = True
            if not wrapped:
                csv[line] += ',' # Don't spread out the results to the right so much if they wrap
            csv[line] += ',{0}'.format(notFoundMotif)
            line += 1
        csv.append('Precision Factor: %s'%(glb.GUI.motifs['delta'].get()))
        csv.append('Algorithm Version: %s'%(glb.ALG_VERSION))

        csvfile = "\n".join(csv)
        stamp = time.ctime()
        stamp = stamp.split()
        stamp = stamp[1] + '_' + stamp[2] + '_' + stamp[4]
        with open(os.path.join(glb.OFFSITE,'motiffinder_{0}_{1}_{2}.csv'.format(pdb, setName, stamp)), 'w') as csvhandle:
            csvhandle.write(csvfile)

    # I patched this code because lengtho - len(pdbs) was not returning the proper number of results.
    # -Kip
    numberOfResults = 0
    for result in glb.GUI.motifs['motifbox'].get(0, tk.END):
        if result.startswith(' '): # Motif results are indented
           numberOfResults += 1
    
    if not glb.GUI.motifs['cancel']:
        glb.GUI.motifs['single']['text'] = 'Click Start to begin'
        glb.GUI.motifs['overall']['text'] = 'Motif Finder finished with {0} results.'.format(numberOfResults)
    cmd.orient('all')
    
    cmd.show('cartoon', 'all')
    cmd.color('gray', 'all')
    glb.GUI.motifs['csv']['state'] = tk.NORMAL
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.NORMAL
    glb.GUI.motifs['multipdb']['state'] = tk.NORMAL
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
            
        
def makemotif(mode):
    glb.GUI.motif_maker['file'] = None
    glb.GUI.motif_maker['wait'] = []
    glb.GUI.motif_maker['motif'] = []
    glb.GUI.motif_maker['order'] = []
    pf = glb.GUI.motif_maker['pf'].get()
    pdb = glb.GUI.motif_maker['pdb'].get().lower()
    ecen = glb.GUI.motif_maker['ec'].get()
    resn = {}
    resi = {}
    backbone = {}
    chain = {}
    
    excepLoop = 0
    exceptions = ''
    cmd.reinitialize()
    
    if mode == 3:
        for i in range(1,11):
            glb.GUI.motif_maker['resn'][i].delete(0,tk.END)
            glb.GUI.motif_maker['resi'][i].delete(0,tk.END)
            glb.GUI.motif_maker['chain'][i].delete(0,tk.END)
            if glb.GUI.motif_maker['backbone'][i].get() == 'On':
                glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
        glb.GUI.motif_maker['pdb'].delete(0,tk.END)
        glb.GUI.motif_maker['ec'].delete(0,tk.END)
        glb.GUI.motif_maker['pf'].delete(0,tk.END)
        glb.GUI.motif_maker['pf'].insert(0,'2.00')
        return True
    
    def press(event,y):
        oldg = glb.GUI.motif_maker['maker'].grid_location(0,event.y)[1]+1
        newg = glb.GUI.motif_maker['maker'].grid_location(0,event.y+y)[1]+1
        i = glb.GUI.motif_maker['neworder'][oldg]
        try:
            h = glb.GUI.motif_maker['neworder'][newg]
        except KeyError:
            return False
        glb.GUI.motif_maker['canvas'].move('row%s'%i,0,y)
        glb.GUI.motif_maker['canvas'].move('row%s'%h,0,-y)
        glb.GUI.motif_maker['neworder'][newg] = i
        glb.GUI.motif_maker['neworder'][oldg] = h
            
    def pressup(event):
        press(event,-22)

    def pressdown(event):
        press(event,22)
    
    def release(event):
        pass
        
  
    def write(string=None,**options):
        if string != None:
            glb.GUI.motif_maker['motif'].append(string)
        if 'open' in options:
            if mode == 0 or mode == 4:
                glb.GUI.motif_maker['motif'] = []
            if mode == 1:
                if os.path.exists(glb.pathmaker((name,'.py'),root=glb.USRMOTIFSFOLDER)) or os.path.exists(glb.pathmaker((name,'.py'),root=glb.MOTIFSFOLDER)):
                    answer = askyesno('Motif Exists', 
                    'A motif has already been made for EC:%s on PDB:%s.\n'%(ec,pdb)+
                    'Are you sure you want to replace it?')
                    if answer == False:
                         return False
                glb.GUI.motif_maker['file'] = open(glb.pathmaker((name,'.py'),root=glb.USRMOTIFSFOLDER), 'wb')
            if mode == 2:
                pref = askdirectory(initialdir=glb.HOME)
                if os.access(pref,os.W_OK | os.X_OK):
                    if os.path.exists(glb.pathmaker('Motifs',(name,'.py'),root=pref)):
                        answer = askyesno('Motif Exists', 
                        'This file exists at this location.\n'+
                        'Are you sure you want to replace it?')
                        if answer == False:
                            return False
                    glb.GUI.motif_maker['file'] = open(glb.pathmaker((name,'.py'),root=pref), 'wb')
                else:
                    showerror('Access Denied','You do not have access to write to this folder.')
                    return False
        if 'close' in options:
            if mode == 4:
                if glb.GUI.motif_maker['radio'].get() == 1:
                    cmd.reinitialize()
                    cmd.fetch(glb.GUI.motif_maker['testpdb'].get(), async=0, path=glb.FETCH_PATH)
                    glb.update()
                elif glb.GUI.motif_maker['radio'].get() == 2:
                    glb.randompdb()
            if mode == 0 or mode == 4:
                d = 1
                lines = ''.join(glb.GUI.motif_maker['motif']).split('\n')
                for line in lines:
                    if line != '':
                        eval(line)
                glb.procolor(name, show_all='cartoon', color_all='gray')
                cmd.orient(name)
                cmd.deselect()
            else:
                if glb.GUI.motif_maker['file'] != None:
                    glb.GUI.motif_maker['file'].writelines(glb.GUI.motif_maker['motif'])
                    glb.GUI.motif_maker['file'].close()
                    if mode == 1:
                        glb.loadMotifs(glb.USRMOTIFSFOLDER)
                        
                else:
                    print 'No file written'
        return True
    
                    
    def getlocistr():
        locistr = ''
        tmpdict = {}
        for item in glb.GUI.motif_maker['order']:
            if item[1] not in tmpdict:
                tmpdict[item[1]] = []
            tmpdict[item[1]].append(item[2])
        for chain in tmpdict:
            locistr = '%s%s-%s;' % (locistr, chain.lower(), ','.join(tmpdict[chain]))
        return locistr
    
    def getresnstr():
        tmplist = []
        for item in glb.GUI.motif_maker['order']:
            tmplist.append(item[0])
        return ','.join(tmplist)
    
    def addresn(x,y,z):
        glb.GUI.motif_maker['order'].append((x, y, z))
        try:
            glb.GUI.motif_maker['order'].sort(key=lambda item: (item[1],int(item[2])))
        except TypeError:
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(int(x[2]), int(y[2])))
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(x[1], y[1]))
        return x
    
    def acceptresn(x,y,z):
        if len(x) == 0:
            return ''
        try:
            x = x.lower()
            newresn = glb.AminoHashTable[x][3]
        except KeyError:
            return None
        return addresn(newresn,y,z)
    
    cmd.fetch(pdb, async=0, path=glb.FETCH_PATH)
    if (pdb not in cmd.get_names('all')) or (cmd.count_atoms(pdb) == 0):
        exceptions += 'Could not fetch {0}'.format(pdb)
    glb.update()
    preecs = ecen.split(',')
    for preec in preecs:
        try:
            eclist = preec.split('.')
            ec1,ec2,ec3,ec4 = eclist
        except ValueError:
            exceptions += 'Please enter a correct EC code with periods.\n'
        else:
            if len(ec1) != 1 or int(ec1) < 1 or int(ec1) > 7:
                exceptions += 'The first number in an EC code has to be >= 1 and <= 7.\n'
            if len(ec2) > 2 or len(ec2) < 1:
                exceptions += 'The second number in an EC code has to be at most two digits.\n'
            if len(ec3) > 2 or len(ec3) < 1:
                exceptions += 'The third number in an EC code has to be at most two digits.\n'
            if len(ec4) > 3 or len(ec4) < 1:
                exceptions += 'The fourth number in an EC code has to be at most three digits.\n'
    ec = ecen.replace('.','_').replace(',','_').replace(' ','')
    skip = {}
    skip[0] = 0
    for i in range(1,11):
        g = glb.GUI.motif_maker['curorder'][i]
        resi[g] = glb.GUI.motif_maker['resi'][g].get().strip()
        backbone[g] = glb.GUI.motif_maker['backbone'][g].get()
        chain[g] = glb.GUI.motif_maker['chain'][g].get().strip()
        resn[g] = acceptresn(glb.GUI.motif_maker['resn'][g].get().strip(),chain[g],resi[g])
        skip[g] = False
        if resn[g] == '' and resi[g] == '' and chain[g] == '':
            ### this gives us the ability to skip whole blocks
            skip[g] = True
            skip[0] += 1
        elif resn[g] != '' and resi[g] != '' and chain[g] != '':
            if resn[g] == None:
                exceptions += 'Residue %s is not recongnized.\n'%(g)
            elif cmd.count_atoms('%s/%s`%s/'%(chain[g],resn[g],resi[g])) == 0:
                exceptions += 'There is no %s at number %s on chain %s.\n'%(resn[g],resi[g],chain[g])
            elif resn[g] == 'gly' and backbone[g] == 'Off':
                exceptions += 'Please turn on the backbone for glycine residue %s\n'%(g)
            excepLoop +=1
        else:    
            if resn[g] == '':
                exceptions += 'Please enter a residue for residue %s\n'%(g)
            if resi[g] == '':
                exceptions += 'Please enter a number for residue %s\n'%(g)
            if chain[g] == '':
                exceptions += 'Please select a chain for residue %s\n.'%(g)
            excepLoop +=1
    if excepLoop < 2:
        exception = True
        exceptions += 'Motifs require that 2 or more residues be entered.'
    if exceptions != '' and exceptions != '\n':
        showerror('Error', 'The following errors have occurred:\n'+exceptions)
    else:
        if mode >= 5 and mode < 6:
            if mode == 5:
                for i in range(1,11):
                    glb.GUI.motif_maker['resn'][i]['state'] = tk.DISABLED
                    glb.GUI.motif_maker['resi'][i]['state'] = tk.DISABLED
                    glb.GUI.motif_maker['chain'][i]['state'] = tk.DISABLED
                    glb.GUI.motif_maker['backbone'][i]['state'] = tk.DISABLED
                    glb.GUI.motif_maker['canvas'].itemconfigure('resn%s' % glb.GUI.motif_maker['neworder'][i],
                        text=glb.GUI.motif_maker['resn'][i].get())
                    glb.GUI.motif_maker['canvas'].itemconfigure('chain%s' % glb.GUI.motif_maker['neworder'][i],
                        text=glb.GUI.motif_maker['chain'][i].get())
                    glb.GUI.motif_maker['canvas'].itemconfigure('resi%s' % glb.GUI.motif_maker['neworder'][i],
                        text=glb.GUI.motif_maker['resi'][i].get())
                    glb.GUI.motif_maker['canvas'].itemconfigure('back%s' % glb.GUI.motif_maker['neworder'][i],
                        text=glb.GUI.motif_maker['backbone'][i].get())
                glb.GUI.motif_maker['canvas'].grid()
                glb.GUI.motif_maker['canvas'].tag_bind('up','<Button-1>', pressup)
                glb.GUI.motif_maker['canvas'].tag_bind('down','<Button-1>', pressdown)
                glb.GUI.motif_maker['canvas'].bind('<ButtonRelease-1>', release)
                glb.GUI.motif_maker['test'].grid_remove()
                glb.GUI.motif_maker['save'].grid_remove()
                glb.GUI.motif_maker['export'].grid_remove()
                glb.GUI.motif_maker['clear'].grid_remove()
                glb.GUI.motif_maker['order'].grid_remove()
                glb.GUI.motif_maker['extest'] = tk.DISABLED
                glb.GUI.motif_maker['done'].grid()
                glb.GUI.motif_maker['recommend'].grid()
                glb.GUI.motif_maker['cancel'].grid()
            if mode > 5:
                if mode == 5.2:
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
                    class fakeevent:
                        pass
                    event = fakeevent()
                    g = 0
                    for order in residueorder:
                        g += 1
                        i = glb.GUI.motif_maker['neworder'][order]
                        h = glb.GUI.motif_maker['neworder'][g]
                        if i == h: 
                            continue
                        event.y = (i)*22
                        y = (g-i)*22
                        press(event,y)
                    print glb.GUI.motif_maker['neworder']

                for i in range(1,11):
                    glb.GUI.motif_maker['resn'][i]['state'] = tk.NORMAL
                    glb.GUI.motif_maker['resi'][i]['state'] = tk.NORMAL
                    glb.GUI.motif_maker['chain'][i]['state'] = tk.NORMAL
                    glb.GUI.motif_maker['backbone'][i]['state'] = 'readonly'
                    if mode != 5.3:
                        glb.GUI.motif_maker['resn'][i].delete(0,tk.END)
                        glb.GUI.motif_maker['resi'][i].delete(0,tk.END)
                        glb.GUI.motif_maker['chain'][i].delete(0,tk.END)
                        if glb.GUI.motif_maker['backbone'][i].get() == 'On':
                            glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
                        glb.GUI.motif_maker['resn'][i].insert(0,glb.GUI.motif_maker['canvas'].itemcget('resn%s'%glb.GUI.motif_maker['neworder'][i],"text"))
                        glb.GUI.motif_maker['resi'][i].insert(0,glb.GUI.motif_maker['canvas'].itemcget('resi%s'%glb.GUI.motif_maker['neworder'][i],"text"))
                        glb.GUI.motif_maker['chain'][i].insert(0,glb.GUI.motif_maker['canvas'].itemcget('chain%s'%glb.GUI.motif_maker['neworder'][i],"text"))
                        if glb.GUI.motif_maker['backbone'][i].get() != glb.GUI.motif_maker['canvas'].itemcget('back%s'%glb.GUI.motif_maker['neworder'][i],"text"):
                            glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
                glb.GUI.motif_maker['canvas'].grid_remove()
                glb.GUI.motif_maker['canvas'].tag_unbind('up','<Button-1>')
                glb.GUI.motif_maker['canvas'].tag_unbind('down','<Button-1>')
                glb.GUI.motif_maker['canvas'].unbind('<ButtonRelease-1>')
                glb.GUI.motif_maker['test'].grid()
                glb.GUI.motif_maker['save'].grid()
                glb.GUI.motif_maker['export'].grid()
                glb.GUI.motif_maker['clear'].grid()
                glb.GUI.motif_maker['order'].grid()
                glb.GUI.motif_maker['extest'] = tk.NORMAL
                glb.GUI.motif_maker['done'].grid_remove()
                glb.GUI.motif_maker['recommend'].grid_remove()
                glb.GUI.motif_maker['cancel'].grid_remove()
            return True
        
        name = 'U_%s_%s'%(pdb,ec)
        write("'''\n")
        write("FUNC:%s\n"%(name))
        write("PDB:%s\n"%(pdb))
        write("EC:%s\n"%(ec.replace('_','.')))
        write("RESI:%s\n"%(getresnstr()))
        write("LOCI:%s\n"%(getlocistr()))
        write("'''\n")
        if write(open=True) == False:
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
            g = glb.GUI.motif_maker['curorder'][i]
            if skip[g] == False:
                if resn[g] not in numOfi:
                    numOfi[resn[g]] = 0
                resnlist.append(resn[g])
                resilist.append(resi[g])
                resnlistf.append(resn[g]+('i'*(numOfi[resn[g]])))
                chainlist.append(chain[g])
                bonelist.append(backbone[g])
                numOfi[resn[g]] += 1
        
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
                blen = (len(bList)-1)
                clen = (len(cList)-1)
                b = -1
                while b < blen:
                    b += 1
                    ### This loop increments through all the carbons
                    ### in the other amino acids that we are want to
                    ### compare with.
                    c = -1
                    while c < clen:
                        c += 1
                        
                        ### Okay lets get the distance between our atoms in our selected amino acids.
                        r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+bList[b],chainlist[d]+'/'+resilist[d]+'/'+cList[c])
                        ### The precision factor
                        ### The ranger is the slider that is moved.
                        ### r is set by the get_distance above.
                        g = '%.2f' %(float(r) + float(pf))
                        
                        a += 1
                        
                        ### apparently pymol cannot handle over a number
                        ### between 248 and 264 selections at one time.
                        ### This fixes that by making sure we do not pass
                        ### "selectlimit" selections at one time.
                        if float(selectlimiter) < (float(a)/float(selectlimit)):
                            write("cmd.select('%s%s',' "%(resnlistf[e],(selectlimiter*selectlimit)))
                            for i in range(selectstart,a):
                                if i==(a-1):
                                    write("br. %s%s')\n"%(resnlistf[e],i))
                                else:
                                    write("br. %s%s&"%(resnlistf[e],i))
                            for i in range(selectstart,a):
                                if i==(a-1):
                                    pass
                                else:
                                    write("cmd.delete('%s%s')\n"%(resnlistf[e],i))
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
                            write("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlistf[d],g))
                        else:
                            write("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlist[d],g))
            write("cmd.select('%s',' "%(resnlistf[e]))
            if selectextra != []:
                write(''.join(selectextra))
            for i in range(selectstart,a+1):
                if i==a:
                    write("br. %s%s')\n"%(resnlistf[e],i))
                else:
                    write('br. %s%s&'%(resnlistf[e],i))
            for x in deleteextra:
                write(x)
            for i in range(selectstart,a+1):
                write("cmd.delete('%s%s')\n"%(resnlistf[e],i))
    
        resnlistfstr = ""
        for i in range(1,resnlen+1):
            if i == resnlen:
                resnlistfstr += resnlistf[i]
            else:
                resnlistfstr += resnlistf[i]+'|'
    
        write("cmd.select('%s', '%s')\n"%(name,resnlistfstr))
        for i in range(1,resnlen+1):
            write("cmd.delete('%s')\n"%(resnlistf[i]))
        write(close=True)
    
        if mode == 0:
            print '%s Amino Acid Motif `%s` Run\n'%(len(resnlist)-1,name)
        if mode == 1:#changed to "Saved to User Motifs Folder"
            print '%s Amino Acid Motif `%s` Saved To User Motifs Folder\n'%(len(resnlist)-1,name)
        if mode == 2:
            print '%s Amino Acid Motif `%s` Exported\n'%(len(resnlist)-1,name)
