from pymol import cmd
from pymol import stored
from urllib import urlretrieve
import Tkinter as tk
import Pmw
import linecache
import random
import os
import re
import tempfile
import time
from tkFileDialog import asksaveasfile, askdirectory
from tkSimpleDialog import askstring
from tkMessageBox import showinfo, showerror, askyesno
from pmg_tk.startup.ProMol import promolglobals as pglob
from pmg_tk.startup.ProMol.remote_pdb_load import fetch

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
        for motif in pglob.MOTIFS.keys():
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

#def custom motif dropdown selection

def set_motifA(tag):
    cmd.deselect()
    mA = tag

def set_motifB(tag):
    cmd.deselect()
    mB = tag

def set_motifC(tag):
    cmd.deselect()
    mC = tag

def set_motifD(tag):
    cmd.deselect()
    mD = tag
 
 #def custom motif dropdown selection
def set_motifAA(tag):
    cmd.deselect()
    mAA = tag

def set_motifAB(tag):
    cmd.deselect()
    mAB = tag

def set_motifAC(tag):
    cmd.deselect()
    mAC = tag

def set_motifAD(tag):
    cmd.deselect()
    mAD = tag

#Custom motif functions

def bimotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        cmd.select('AA', 'resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.select('BB', 'resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.select('motif', 'byres AA | byres BB')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A and B')

def trimotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        mC = mC
        cmd.select('AA', 'resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.select('BB', 'resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.select('CC', 'resn %s within %s of resn %s'%(mC, selB.get(), mB))
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, and C')

def quadmotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mA = mA
        mB = mB
        mC = mC
        mD = mD
        cmd.select('AA', 'resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.select('BB', 'resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.select('CC', 'resn %s within %s of resn %s'%(mC, selB.get(), mB))
        cmd.select('DD', 'resn %s within %s of resn %s'%(mD, selC.get(), mC))
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
        cmd.delete('DD')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, C, and D')

def Abimotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        cmd.select('AA', 'resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('BB', 'resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('motif', 'byres AA | byres BB')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A and B')

def Atrimotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        mAC = mAC
        cmd.select('AA1', 'resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA', 'byres AA1 and byres AA2')
        cmd.select('BB1', 'resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB', 'byres BB1 and byres BB2')
        cmd.select('CC1', 'resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
        cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
        cmd.select('CC', 'byres CC1 and byres CC2')
        cmd.select('motif', 'byres AA | byres BB | byres CC')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
    except:
        showinfo('Alert',
            'You must select an amino acid for menus A, B, and C')

def Aquadmotif():
    try:
        update()
        objects = cmd.get_names('all')
        cmd.delete('motif')
        cmd.hide('everything')
        mAA = mAA
        mAB = mAB
        mAC = mAC
        mAD = mAD
        cmd.select('AA1', 'resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA3', 'resn %s within %s of resn %s'%(mAA, selAD.get(), mAD))
        cmd.select('AA', 'byres AA1 and byres AA2 and byres AA3')
        cmd.select('BB1', 'resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB3', 'resn %s within %s of resn %s'%(mAB, selBD.get(), mAD))
        cmd.select('BB', 'byres BB1 and byres BB2 and byres BB3')
        cmd.select('CC1', 'resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
        cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
        cmd.select('CC3', 'resn %s within %s of resn %s'%(mAC, selCD.get(), mAD))
        cmd.select('CC', 'byres CC1 and byres CC2 and byres CC3')
        cmd.select('DD1', 'resn %s within %s of resn %s'%(mAD, selAD.get(), mAA))
        cmd.select('DD2', 'resn %s within %s of resn %s'%(mAD, selBD.get(), mAB))
        cmd.select('DD3', 'resn %s within %s of resn %s'%(mAD, selCD.get(), mAC))
        cmd.select('DD', 'byres DD1 and byres DD2 and byres DD3')
        cmd.select('motif', 'byres AA | byres BB | byres CC | byres DD')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'motif')
        cmd.set('stick_radius', '0.5')
        cpkmotif()
        cmd.orient('motif')
        cmd.deselect()
        cmd.delete('AA')
        cmd.delete('BB')
        cmd.delete('CC')
        cmd.delete('DD')
    except:
        showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')

#reset the range sliders
def resetmotif():
    selA.set(4.0)
    selB.set(4.0)
    selC.set(4.0)
    selAB.set(4.0)
    selAC.set(4.0)
    selAD.set(4.0)
    selBC.set(4.0)
    selBD.set(4.0)
    selCD.set(4.0)

def MotifCaller(motif, camera=True):
    d = float(pglob.GUI['motifs']['delta'].get())
    if camera:
        pglob.deletemotif()
        pglob.update()
    try:
        if execfile(pglob.MOTIFS[motif]['path']) != False:
            if motif not in cmd.get_names('all'):
                raise Warning
            if cmd.count_atoms(motif) == 0:
                raise Warning
            if camera:
                pglob.procolor(motif, show_all='cartoon',color_all='gray')
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

def dbckmotif(event):
    '''allows user to click on motif search field items and run the motif function'''
    motif = pglob.GUI['motifs']['motifbox'].curselection()[0]
    tag = pglob.GUI['motifs']['motifbox'].get(motif).split('-')
    pdb = pglob.GUI['motifs']['hidmotif'].get(motif)
    cmd.reinitialize()
    fetch(pdb)
    if len(tag) == 2 and tag[1] in pglob.MOTIFS:
        MotifCaller(tag[1])
    else:
        pglob.update()

def export2ods():
    pass

def export2csv():
    csv = ['PDB Entry,PDB Homologue,Motifs,Rank,Residues',
        ',,,,Chain,Name,Number']
    motifs = pglob.GUI['motifs']['motifbox'].get(0,tk.END)
    pdbs = pglob.GUI['motifs']['hidmotif'].get(0,tk.END)
    lastpdb = None
    motifl = 0
    motifsl = len(motifs)
    while motifl < motifsl:
        try:
            motif = motifs[motifl].split('-')[1]
        except IndexError:
            motifl += 1
            continue
        pdb = pdbs[motifl]
        x = pglob.GUI['motifs']['csvprep'][pdb][motif]['x']
        pf = pglob.GUI['motifs']['csvprep'][pdb][motif]['pf']
        pdbstr = '%s@PF%s'%(pdb,pf)
        if 'hom' in pglob.GUI['motifs']['csvprep'][pdb][motif]:
            hom = '%s@PF%s'%(pglob.GUI['motifs']['csvprep'][pdb][motif]['hom'],pf)
        else:
            hom = ''
        residues = pglob.GUI['motifs']['csvprep'][pdb][motif]['res']
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
        motifl += 1
    csvfile = "\n".join(csv)
    csvhandle = asksaveasfile(initialfile='motiffinder.csv',defaultextension='.csv',
        filetypes=[('CSV','*.csv')],title='Export Motif Finder Results As...')
    if csvhandle != None:
        csvhandle.write(csvfile)
        csvhandle.close()

def motifcancel():
    pglob.GUI['motifs']['cancel'] = True

def motifchecker():
    pglob.GUI['motifs']['cancel'] = False
    pglob.GUI['motifs']['motifbox'].delete(0,tk.END)
    pglob.GUI['motifs']['hidmotif'].delete(0,tk.END)
    pglob.GUI['motifs']['csvprep'] = {}
    pglob.GUI['motifs']['cancelbutton']['state'] = tk.NORMAL
    pglob.GUI['motifs']['delta']['state'] = tk.DISABLED
    pglob.GUI['motifs']['csv']['state'] = tk.DISABLED
    pglob.GUI['motifs']['findmotif']['state'] = tk.DISABLED
    pglob.GUI['motifs']['multipdb']['state'] = tk.DISABLED
    pdbs = pglob.GUI['motifs']['multipdb'].get(1.0,'1.end').split(',')
    pdbsl = len(pdbs)
    if pdbsl == 1 and pdbs[0] == '':
        showerror('No PDB Entered',"Enter a PDB or a comma separated list of PDB's to search")
        pglob.GUI['motifs']['delta']['state'] = tk.NORMAL
        pglob.GUI['motifs']['findmotif']['state'] = tk.NORMAL
        pglob.GUI['motifs']['multipdb']['state'] = tk.NORMAL
        pglob.GUI['motifs']['cancelbutton']['state'] = tk.DISABLED
        return False
    
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
            nn = 0
            for c in tup:
                if c in ('asp','glu','asn','gln','thr','ser'):
                    nn += 1
            if nn == 0:
                return [None]
            n = 2**nn
            r = len(tup)
            matrix = [[None]*r for i in range(n)]
            ii = 0
            for i in tup:
                h = 2**(ii+1)               
                if 's' in pglob.AminoHashTable[i]:
                    for g in range(n/h):
                        for j in range(h):
                            matrix[g+(j*(n/h))][ii] = j%2 and pglob.AminoHashTable[i]['s'] or i
                else:
                    for g in range(n):
                        matrix[g][ii] = i
                ii += 1
            return matrix

        last = None
        ordered = []
        orderedchain = {}
        bannedchain = []
        stored.motif = []
        editdist = []
        cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
        residues = pglob.MOTIFS[motif]['resi']
        residuesl = len(residues)*2
        pglob.GUI['motifs']['csvprep'][pdb][motif] = {}
        pglob.GUI['motifs']['csvprep'][pdb][motif]['res'] = []
        for iteration in stored.motif:
            if last != iteration:
                last = iteration
                pglob.GUI['motifs']['csvprep'][pdb][motif]['res'].append(iteration)
                ordered.append(iteration[1].lower())
                if iteration[0] not in orderedchain:
                    if iteration[0] not in bannedchain:
                        orderedchain[iteration[0]] = []
                    else:
                        continue
                orderedchain[iteration[0]].append(iteration[1].lower())
                if residuesl < len(orderedchain[iteration[0]]):
                    bannedchain.append(iteration[0])
                    del orderedchain[iteration[0]]
        if len(orderedchain) == 0 and residuesl < len(ordered):
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
        pglob.GUI['motifs']['csvprep'][pdb][motif]['x'] = mini<maxi and '%s/%s'%(mini,maxi) or mini
        pglob.GUI['motifs']['csvprep'][pdb][motif]['pf'] = pglob.GUI['motifs']['delta'].get()
        return pglob.GUI['motifs']['csvprep'][pdb][motif]['x']

    lasto = 0.0
    founds = {}
    foundso = []
    for pdb in pdbs:
        if pglob.GUI['motifs']['cancel'] == True:
            pglob.GUI['motifs']['single']['text'] = 'Click Start to begin'
            pglob.GUI['motifs']['overall']['text'] = 'Cancelled... %.3s%% Complete'%baro
            pglob.GUI['motifs']['single'].update()
            break
        found = []
        last = 0.0
        keys = pglob.MOTIFS.keys()
        keysL = len(keys)-1
        keysLo = keysL*len(pdbs)
        pglob.GUI['motifs']['csvprep'][pdb] = {}
        cmd.reinitialize()
        fetchresult = fetch(pdb,True)
        if fetchresult != '':
            founds[pdb] = ['    %s'%fetchresult]
            lasto += keysL
            pglob.GUI['motifs']['singlestatus'].SetProgressPercent(100)
            pglob.GUI['motifs']['overallstatus'].SetProgressPercent((lasto/keysLo)*100)
            continue
        cmd.hide('everything', 'all')
        cmd.remove("all and hydro")
        
        for motif in keys:
            if motif == 'errors':
                continue
            last += 1
            lasto += 1
            bar = (last/keysL)*100
            baro = (lasto/keysLo)*100
            if pglob.GUI['motifs']['cancel'] == True:
                break
            if len(str(bar).split('.')[0]) < 3:
                pglob.GUI['motifs']['single']['text'] = 'Searching... %.2s%% Complete'%(bar)
            else:
                pglob.GUI['motifs']['single']['text'] = '%.3s%% Complete'%(bar)
            if len(str(baro).split('.')[0]) < 3:
                pglob.GUI['motifs']['overall']['text'] = 'Overall... %.2s%% Complete'%(baro)
            else:
                pglob.GUI['motifs']['overall']['text'] = '%.3s%% Complete'%(baro)
            pglob.GUI['motifs']['singlestatus'].SetProgressPercent(bar)
            pglob.GUI['motifs']['overallstatus'].SetProgressPercent(baro)
            pglob.GUI['motifs']['single'].update()
            if MotifCaller(motif,False):
                x = count(motif,pdb)
                if x != None:
                    motifStr = '    %s-%s'%(x,motif)
                    found.append(motifStr)
            cmd.delete(motif)
        found.sort()
        founds[pdb] = found
    
    for f in founds:
        foundso.extend([f])
        foundso.extend(founds[f])
    pglob.GUI['motifs']['single']['text'] = 'Click Start to begin'
    pglob.GUI['motifs']['overall']['text'] = 'Motif Finder finished with %s results.'%(len(foundso)-len(pdbs))
    cmd.orient('all')
    for foundo in foundso:
        if len(foundo) == 4:
            pdb = foundo
        pglob.GUI['motifs']['motifbox'].insert(tk.END,foundo)
        pglob.GUI['motifs']['hidmotif'].insert(tk.END,pdb)
    cmd.show('cartoon', 'all')
    cmd.color('gray', 'all')
    pglob.GUI['motifs']['csv']['state'] = tk.NORMAL
    pglob.GUI['motifs']['findmotif']['state'] = tk.NORMAL
    pglob.GUI['motifs']['delta']['state'] = tk.NORMAL
    pglob.GUI['motifs']['multipdb']['state'] = tk.NORMAL
    pglob.GUI['motifs']['cancelbutton']['state'] = tk.DISABLED

def randompdb():
    cmd.reinitialize()
    lineFile = pglob.pathmaker('pdb_entry_type.txt',root=pglob.OFFSITE)
    while os.path.exists(lineFile):
        expiration = (os.path.getmtime(lineFile)+864000)
        if expiration <= time.time():
            os.remove(lineFile)
        else:
            lines = sum([1 for line in lineFile])
            pdbCode = linecache.getline(lineFile,random.randint(1, lines))[0:4]
            fetch(pdbCode)
            break
    else:
        urlretrieve('ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt',
            lineFile)
        randompdb()
    pglob.update()
cmd.extend('randompdb',random)
        
def makemotif(mode):
    pglob.GUI['motif_maker']['file'] = None
    pglob.GUI['motif_maker']['wait'] = []
    pglob.GUI['motif_maker']['motif'] = []
    pglob.GUI['motif_maker']['resnstr'] = {}
    pf = pglob.GUI['motif_maker']['pf'].get()
    pdb = pglob.GUI['motif_maker']['pdb'].get().lower()
    ecen = pglob.GUI['motif_maker']['ec'].get()
    resn = {}
    resi = {}
    backbone = {}
    chain = {}
    
    excepLoop = 0
    exceptions = ''
    cmd.reinitialize()
    
    if mode == 3:
        for i in range(1,11):
            pglob.GUI['motif_maker']['resn'][i].delete(0,tk.END)
            pglob.GUI['motif_maker']['resi'][i].delete(0,tk.END)
            pglob.GUI['motif_maker']['chain'][i].delete(0,tk.END)
            if pglob.GUI['motif_maker']['backbone'][i].get() == 'On':
                pglob.GUI['motif_maker']['backbone'][i].invoke('buttonup')
        pglob.GUI['motif_maker']['pdb'].delete(0,tk.END)
        pglob.GUI['motif_maker']['ec'].delete(0,tk.END)
        pglob.GUI['motif_maker']['pf'].delete(0,tk.END)
        pglob.GUI['motif_maker']['pf'].insert(0,'2.00')
        return True
    
    def press(event,y):
        oldg = pglob.GUI['motif_maker']['maker'].grid_location(0,event.y)[1]+1
        newg = pglob.GUI['motif_maker']['maker'].grid_location(0,event.y+y)[1]+1
        i = pglob.GUI['motif_maker']['neworder'][oldg]
        try:
            h = pglob.GUI['motif_maker']['neworder'][newg]
        except KeyError:
            return False
        pglob.GUI['motif_maker']['canvas'].move('row%s'%i,0,y)
        pglob.GUI['motif_maker']['canvas'].move('row%s'%h,0,-y)
        pglob.GUI['motif_maker']['neworder'][newg] = i
        pglob.GUI['motif_maker']['neworder'][oldg] = h
            
    def pressup(event):
        press(event,-22)

    def pressdown(event):
        press(event,22)
    
    def release(event):
        pass
    
    def write(string=None,**options):
        if string != None:
            pglob.GUI['motif_maker']['motif'].append(string)
        if 'open' in options:
            if mode == 0 or mode == 4:
                pglob.GUI['motif_maker']['motif'] = []
            if mode == 1:
                if os.path.exists(pglob.pathmaker((name,'.py'),root=pglob.USRMOTIFSFOLDER)) or os.path.exists(pglob.pathmaker((name,'.py'),root=pglob.MOTIFSFOLDER)):
                    answer = askyesno('Motif Exist', 
                    'A motif has already been made for EC:%s on PDB:%s.\n'%(ec,pdb)+
                    'Are you sure you want to replace it?')
                    if answer == False:
                        return False
                pglob.GUI['motif_maker']['file'] = open(pglob.pathmaker((name,'.py'),root=pglob.USRMOTIFSFOLDER), 'wb')
            if mode == 2:
                pref = askdirectory(initialdir=pglob.HOME)
                if os.access(pref,os.W_OK | os.X_OK):
                    if os.path.exists(pglob.pathmaker('Motifs',(name,'.py'),root=pref)):
                        answer = askyesno('Motif Exist', 
                        'This file exist at this location.\n'+
                        'Are you sure you want to replace it?')
                        if answer == False:
                            return False
                    pglob.GUI['motif_maker']['file'] = open(pglob.pathmaker((name,'.py'),root=pref), 'wb')
                else:
                    showerror('Access Denied','You do not have access to write to this folder.')
                    return False
        if 'close' in options:
            if mode == 4:
                if pglob.GUI['motif_maker']['radio'].get() == 1:
                    cmd.reinitialize()
                    fetch(pglob.GUI['motif_maker']['testpdb'].get())
                    pglob.update()
                elif pglob.GUI['motif_maker']['radio'].get() == 2:
                    randompdb()
            if mode == 0 or mode == 4:
                d = 1
                lines = ''.join(pglob.GUI['motif_maker']['motif']).split('\n')
                for line in lines:
                    if line != '':
                        eval(line)
                pglob.procolor(name, show_all='cartoon', color_all='gray')
                cmd.orient(name)
                cmd.deselect()
            else:
                pglob.GUI['motif_maker']['file'].writelines(pglob.GUI['motif_maker']['motif'])
                pglob.GUI['motif_maker']['file'].close()
                if mode == 1:
                    pglob.motifstore(pglob.USRMOTIFSFOLDER)
        return True

    def addresn(x,y,z):
        if z not in pglob.GUI['motif_maker']['resnstr']:
            pglob.GUI['motif_maker']['resnstr'][z] = {}
        pglob.GUI['motif_maker']['resnstr'][z][y] = x
        return x
    
    def getresnstr():
        alphanum = lambda k:[(lambda t:(t.isdigit() and [int(t)] or [t])[0])(c) for c in re.split('([0-9]+)',k)]
        for i in pglob.GUI['motif_maker']['resnstr']:
            keys = pglob.GUI['motif_maker']['resnstr'][i].keys()
            keys.sort(lambda x,y:cmp(alphanum(x),alphanum(y)))
            resn = []
            for key in keys:
                resn.append(pglob.GUI['motif_maker']['resnstr'][i][key])
            pglob.GUI['motif_maker']['resnstr'][i] = resn
        keys = pglob.GUI['motif_maker']['resnstr'].keys()
        keys.sort()
        resn = []
        for key in keys:
            for i in pglob.GUI['motif_maker']['resnstr'][key]:
                resn.append(i)
        return ','.join(resn)
    
    def acceptresn(x,y,z):
        if len(x) == 0:
            return ''
        try:
            x = x.lower()
            newresn = pglob.AminoHashTable[x][3]
        except KeyError:
            return None
        return addresn(newresn,y,z)
    exceptions += '%s%s'%(fetch(pdb,True),'\n')
    pglob.update()
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
        g = pglob.GUI['motif_maker']['curorder'][i]
        resi[g] = pglob.GUI['motif_maker']['resi'][g].get()
        backbone[g] = pglob.GUI['motif_maker']['backbone'][g].get()
        chain[g] = pglob.GUI['motif_maker']['chain'][g].get()
        resn[g] = acceptresn(pglob.GUI['motif_maker']['resn'][g].get(),resi[g],chain[g])
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
    if exceptions != '':
        showerror('Error', 'The following errors have occurred:\n'+exceptions)
    else:
        if mode >= 5 and mode < 6:
            if mode == 5:
                for i in range(1,11):
                    pglob.GUI['motif_maker']['resn'][i]['state'] = tk.DISABLED
                    pglob.GUI['motif_maker']['resi'][i]['state'] = tk.DISABLED
                    pglob.GUI['motif_maker']['chain'][i]['state'] = tk.DISABLED
                    pglob.GUI['motif_maker']['backbone'][i]['state'] = tk.DISABLED
                    pglob.GUI['motif_maker']['canvas'].itemconfigure('resn%s'%pglob.GUI['motif_maker']['neworder'][i],
                        text=pglob.GUI['motif_maker']['resn'][i].get())
                    pglob.GUI['motif_maker']['canvas'].itemconfigure('chain%s'%pglob.GUI['motif_maker']['neworder'][i],
                        text=pglob.GUI['motif_maker']['chain'][i].get())
                    pglob.GUI['motif_maker']['canvas'].itemconfigure('resi%s'%pglob.GUI['motif_maker']['neworder'][i],
                        text=pglob.GUI['motif_maker']['resi'][i].get())
                    pglob.GUI['motif_maker']['canvas'].itemconfigure('back%s'%pglob.GUI['motif_maker']['neworder'][i],
                        text=pglob.GUI['motif_maker']['backbone'][i].get())
                pglob.GUI['motif_maker']['canvas'].grid()
                pglob.GUI['motif_maker']['canvas'].tag_bind('up','<Button-1>', pressup)
                pglob.GUI['motif_maker']['canvas'].tag_bind('down','<Button-1>', pressdown)
                pglob.GUI['motif_maker']['canvas'].bind('<ButtonRelease-1>', release)
                pglob.GUI['motif_maker']['test'].grid_remove()
                pglob.GUI['motif_maker']['save'].grid_remove()
                pglob.GUI['motif_maker']['export'].grid_remove()
                pglob.GUI['motif_maker']['clear'].grid_remove()
                pglob.GUI['motif_maker']['order'].grid_remove()
                pglob.GUI['motif_maker']['extest'] = tk.DISABLED
                pglob.GUI['motif_maker']['done'].grid()
                pglob.GUI['motif_maker']['recommend'].grid()
                pglob.GUI['motif_maker']['cancel'].grid()
            if mode > 5:
                if mode == 5.2:
                    residuecounts = {}
                    for i in range(1,11):
                        h = pglob.GUI['motif_maker']['resn'][i].get()
                        if h == '':
                            continue
                        cmd.select(h,'resn %s'%h)
                        residuecounts[cmd.count_atoms(h)/pglob.AminoHashTable[h][0]] = i
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
                        i = pglob.GUI['motif_maker']['neworder'][order]
                        h = pglob.GUI['motif_maker']['neworder'][g]
                        if i == h: 
                            continue
                        event.y = (i)*22
                        y = (g-i)*22
                        press(event,y)
                    print pglob.GUI['motif_maker']['neworder']

                for i in range(1,11):
                    pglob.GUI['motif_maker']['resn'][i]['state'] = tk.NORMAL
                    pglob.GUI['motif_maker']['resi'][i]['state'] = tk.NORMAL
                    pglob.GUI['motif_maker']['chain'][i]['state'] = tk.NORMAL
                    pglob.GUI['motif_maker']['backbone'][i]['state'] = 'readonly'
                    if mode != 5.3:
                        pglob.GUI['motif_maker']['resn'][i].delete(0,tk.END)
                        pglob.GUI['motif_maker']['resi'][i].delete(0,tk.END)
                        pglob.GUI['motif_maker']['chain'][i].delete(0,tk.END)
                        if pglob.GUI['motif_maker']['backbone'][i].get() == 'On':
                            pglob.GUI['motif_maker']['backbone'][i].invoke('buttonup')
                        pglob.GUI['motif_maker']['resn'][i].insert(0,pglob.GUI['motif_maker']['canvas'].itemcget('resn%s'%pglob.GUI['motif_maker']['neworder'][i],"text"))
                        pglob.GUI['motif_maker']['resi'][i].insert(0,pglob.GUI['motif_maker']['canvas'].itemcget('resi%s'%pglob.GUI['motif_maker']['neworder'][i],"text"))
                        pglob.GUI['motif_maker']['chain'][i].insert(0,pglob.GUI['motif_maker']['canvas'].itemcget('chain%s'%pglob.GUI['motif_maker']['neworder'][i],"text"))
                        if pglob.GUI['motif_maker']['backbone'][i].get() != pglob.GUI['motif_maker']['canvas'].itemcget('back%s'%pglob.GUI['motif_maker']['neworder'][i],"text"):
                            pglob.GUI['motif_maker']['backbone'][i].invoke('buttonup')
                pglob.GUI['motif_maker']['canvas'].grid_remove()
                pglob.GUI['motif_maker']['canvas'].tag_unbind('up','<Button-1>')
                pglob.GUI['motif_maker']['canvas'].tag_unbind('down','<Button-1>')
                pglob.GUI['motif_maker']['canvas'].unbind('<ButtonRelease-1>')
                pglob.GUI['motif_maker']['test'].grid()
                pglob.GUI['motif_maker']['save'].grid()
                pglob.GUI['motif_maker']['export'].grid()
                pglob.GUI['motif_maker']['clear'].grid()
                pglob.GUI['motif_maker']['order'].grid()
                pglob.GUI['motif_maker']['extest'] = tk.NORMAL
                pglob.GUI['motif_maker']['done'].grid_remove()
                pglob.GUI['motif_maker']['recommend'].grid_remove()
                pglob.GUI['motif_maker']['cancel'].grid_remove()
            return True
        
        name = 'P_%s_%s'%(pdb,ec)
        write("'''\n")
        write("FUNC:%s\n"%(name))
        write("PDB:%s\n"%(pdb))
        write("EC:%s\n"%(ec.replace('_','.')))
        write("RESI:%s\n"%(getresnstr()))
        write("'''\n")
        if write(open=True) == False:
            return False
        atomlist = {}
        ### backbone off aka just side chains from beta carbon onwards
        atomlist[0] = {'ala':('CB'),
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
            g = pglob.GUI['motif_maker']['curorder'][i]
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
        if mode == 1:
            print '%s Amino Acid Motif `%s` Saved To Motifs Folder\n'%(len(resnlist)-1,name)
        if mode == 2:
            print '%s Amino Acid Motif `%s` Exported\n'%(len(resnlist)-1,name)
