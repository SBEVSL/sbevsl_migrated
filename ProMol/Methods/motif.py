from pymol import cmd
from pymol import stored
import Tkinter as tk
import Pmw
import os
import re
import time
import subprocess
from tkFileDialog import asksaveasfile, askdirectory, askopenfile
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
import Tkinter as tk
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
    motifString = glb.matchpairs[motif][1]
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
    queryPDBCode = glb.matchpairs[motif][0] # pdb
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
            cmd.align(motifSubsetName, querySubsetName)
            cmd.set_color('motifColor',
                ([int(n, 16) for n in (motifColor[1:3], motifColor[3:5], motifColor[5:7])]))
            cmd.set_color('queryColor',
                ([int(n, 16) for n in (queryColor[1:3], queryColor[3:5], queryColor[5:7])]))
            cmd.color('motifColor', motifPDBCode)
            cmd.color('queryColor', queryPDBCode)
            cmd.orient(motifSubsetName)
            # I hope this is OK to delete
            cmd.delete(motifName)
            # Added by Kip to show both proteins in subsets
            glb.populate()

def export2ods():
    pass

def viewExistingCSV():
    if (glb.PLATFORM == 'Windows'):
        try:
            os.startfile(os.path.normpath(os.path.relpath(glb.CSV_PATH)))
        finally:
            pass
    elif (glb.PLATFORM == 'Darwin'):
        try:
            subprocess.call(['open', glb.CSV_PATH])
        finally:
            pass
    else:
        try:
            # I learned about xdg-open from having to configure my SVN client
            # to open files in their default editor (the RapidSVN documentation)
            subprocess.call(['xdg-open', glb.CSV_PATH])
        except OSError:
            try:
                subprocess.call(['gnome-open', glb.CSV_PATH])
            except OSError:
                try:
                    subprocess.call(['nautilus', '--no-default-window', '--no-desktop', glb.CSV_PATH])
                finally:
                    pass
    
def combineCSV():
    pass

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
    glb.matchpairs = []
    glb.GUI.motifs['csvprep'] = {}
    glb.GUI.motifs['cancelbutton']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.DISABLED
    glb.GUI.motifs['combine']['state'] = tk.DISABLED
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
    
    glb.GUI.motifs['single']['text'] = 'Starting search...'
    glb.GUI.motifs['overall']['text'] = 'Starting search...'
    glb.GUI.motifs['singlestatus'].SetProgressPercent(0.0)
    glb.GUI.motifs['overallstatus'].SetProgressPercent(0.0)
    glb.GUI.motifs['single'].update()
    for pdbIndex in range(len(pdbs)):
        pdb = pdbs[pdbIndex]
        
        # Deleted founds initializer
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
            glb.GUI.motifs['single']['text'] = '{0} ({1} of {2}): {3}% complete'.format(pdb, pdbIndex + 1, len(pdbs), int(bar))
            glb.GUI.motifs['overall']['text'] = 'Overall: {0}% complete'.format(int(baro))
            glb.GUI.motifs['singlestatus'].SetProgressPercent(bar)
            glb.GUI.motifs['overallstatus'].SetProgressPercent(baro)
            glb.GUI.motifs['single'].update()

        # If cancelled, break out of outer loop too
        if glb.GUI.motifs['cancel']:
            break
        found.sort()
        glb.matchpairs.append((pdb, pdb))
        for result in found:
            glb.matchpairs.append((pdb, result))

        # Export CSV file automatically
        # To-do: Combine this with the other CSV code and/or reimplement using Python's CSV library
        csv = ['PDB Entry,PDB Homologue,Motifs Found,Rank,Residues,,,,Motifs Not Found', #added Alg version and not found columns
        ',,,,Chain,Name,Number']
        allMotifs = []
        pdbMotifs = []
        motifSet = glb.searchSet #MODIFIED for subset of motifs
        for item in motifSet:
            if item == 'errors':
                continue
            allMotifs.append(item)
        lastpdb = None
        fillFrom = 2
        for result in found:
            # This should no longer fail regularly because query PDB entry
            # headers are no longer in the mix.  I removed the try because
            # I want to know if something goes wrong. -Kip
            motif = result.split('-')[1]
            
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
        # Fix for if there are absolutely no matches: make room for not found list
        # Before I rewrote the bigger loop it created an infinite loop because pdbfnl
        # (the not found list loop index) was never incremented, causing ProMol to hang
        # because the inner lines for loop was never run (fillFrom and len(csv) were both 2)
        # That for loop is now gone; now, without this while loop, it would cause
        # an IndexError instead (csv[2] with csv of length 2) -Kip
        notFoundList = list(set(allMotifs) - set(pdbMotifs)) # motifs not found for this structure = all motifs - motifs found for this structure
        notFoundList.sort()
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
        with open(os.path.join(glb.CSV_PATH,'motiffinder_{0}_{1}_{2}.csv'.format(pdb, setName, stamp)), 'w') as csvhandle:
            csvhandle.write(csvfile)

    # I patched this code because lengtho - len(pdbs) was not returning the proper number of results.
    # -Kip
    numberOfResults = len(glb.matchpairs)
    for query, motif in glb.matchpairs:
        glb.GUI.motifs['motifbox'].insert(tk.END, motif)
        if query == motif:
            numberOfResults -= 1
    
    if not glb.GUI.motifs['cancel']:
        glb.GUI.motifs['single']['text'] = 'Click Start to begin'
        glb.GUI.motifs['overall']['text'] = 'Motif Finder finished with {0} results.'.format(numberOfResults)
    cmd.orient('all')
    
    cmd.show('cartoon', 'all')
    cmd.color('gray', 'all')
    glb.GUI.motifs['combine']['state'] = tk.NORMAL
    glb.GUI.motifs['findmotif']['state'] = tk.NORMAL
    glb.GUI.motifs['delta']['state'] = tk.NORMAL
    glb.GUI.motifs['multipdb']['state'] = tk.NORMAL
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
            
        
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
        glb.GUI.motif_maker['file'] = open(glb.pathmaker((self.name,'.py'),root=glb.USRMOTIFSFOLDER), 'wb')
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
            glb.GUI.motif_maker['file'] = open(glb.pathmaker((self.name,'.py'),root=pref), 'wb')
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
                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlistf[d],g))
                            else:
                                self.buildMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlist[d],g))
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
