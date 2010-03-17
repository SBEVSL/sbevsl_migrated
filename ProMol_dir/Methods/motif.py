from pymol import cmd
from pymol import stored
import Tkinter as tk
import Pmw
import linecache
import random
import os
import urllib2
import time
from tkFileDialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkSimpleDialog import askstring
from tkMessageBox import showinfo
from tkMessageBox import showerror
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods import motifcoded as motcod
from pmg_tk.startup.ProMol_dir.remote_pdb_load import fetch

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
        for motif in motcod.motifs.keys():
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

#after appending motif to motif search field allows user to click on it
#and run the motif function

def allmotif():
    motif = pglob.Tabs['motifs']['motifbox'].getcurselection()
    for item in motif:
        tag = item[2:]
    if len(tag) == 0:
        print 'No selection for double click'
    if tag in motcod.motifs.keys():
        motcod.MotifCaller(motcod.motifs[tag]['function'])

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
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
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
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
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
        cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
        cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
        cmd.do('sel DD, resn %s within %s of resn %s'%(mD, selC.get(), mC))
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
        cmd.do('sel AA, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.do('sel BB, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
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
        cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA', 'byres AA1 and byres AA2')
        cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB', 'byres BB1 and byres BB2')
        cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
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
        cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
        cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
        cmd.select('AA3', 'resn %s within %s of resn %s'%(mAA, selAD.get(), mAD))
        cmd.select('AA', 'byres AA1 and byres AA2 and byres AA3')
        cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
        cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
        cmd.select('BB3', 'resn %s within %s of resn %s'%(mAB, selBD.get(), mAD))
        cmd.select('BB', 'byres BB1 and byres BB2 and byres BB3')
        cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
        cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
        cmd.select('CC3', 'resn %s within %s of resn %s'%(mAC, selCD.get(), mAD))
        cmd.select('CC', 'byres CC1 and byres CC2 and byres CC3')
        cmd.do('sel DD1, resn %s within %s of resn %s'%(mAD, selAD.get(), mAA))
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

def setcusmotif():
    a = []
    for object in os.listdir(pglob.pathmaker('Motifs')):
        a.append(object)
    motifdrop.setlist(a)

def runcusmotif():
        a = ['']
        for object in os.listdir(pglob.pathmaker('Motifs')):
            a.append(object)
        motif = motifdrop.getcurselection()
        for item in motif:
            tag = item
        try:
             for i in range(1, 100, 1):
                if a[i] in tag:
                    cmd.run(pglob.pathmaker('Motifs',a[i]))
        except:
            pass

def toggleMultiState():
    mode = pglob.Tabs['motifs']['mode'].get()
    text = pglob.Tabs['motifs']['multipdbtxt']
    if mode == 0:
        pglob.Tabs['motifs']['multipdb'].delete(1.0, tk.END)
        pglob.Tabs['motifs']['multipdb'].insert(tk.END, text)
        pglob.Tabs['motifs']['multipdb']['state'] = tk.DISABLED
        return True
    pglob.Tabs['motifs']['multipdb']['state'] = tk.NORMAL
    pglob.Tabs['motifs']['multipdb'].delete(1.0, tk.END)
    return True

def export2csv():
    csv = ['PDB Entry,PDB Homologue,Motifs,Rank,Residues',
        ',,,,Chain,Name,Num']
    motifs = pglob.Tabs['motifs']['motifbox'].get()
    first = True
    for motif in motifs:
        x = pglob.Tabs['motifs']['csvprep'][motif]['x']
        pf = pglob.Tabs['motifs']['csvprep'][motif]['pf']
        pdb = '%s@PF%s'%(pglob.Tabs['motifs']['csvprep'][motif]['pdb'],pf)
        if 'hom' in pglob.Tabs['motifs']['csvprep'][motif]:
            hom = '%s@PF%s'%(pglob.Tabs['motifs']['csvprep'][motif]['hom'],pf)
        else:
            hom = ''
        residues = pglob.Tabs['motifs']['csvprep'][motif]['res']
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
            if first == True:
                csv.append('%s,%s,%s,%s,%s,%s,%s'%(pdb,hom,motif[2:],x,chain,resn,resi))
                first = False
                continue
            if motifline == True:
                csv.append(',,%s,%s,%s,%s,%s'%(motif[2:],x,chain,resn,resi))
                motifline = False
                continue
            csv.append(',,,,%s,%s,%s'%(chain,resn,resi))
    csvfile = "\n".join(csv)
    csvhandle = asksaveasfile(initialfile='%s.csv'%(pdb),defaultextension='.csv',
        filetypes=[('CSV','*.csv')],title='Export Motif Finder Results As...')
    if csvhandle != None:
        csvhandle.write(csvfile)
        csvhandle.close()
        
def motifchecker():
    mode = pglob.Tabs['motifs']['mode'].get()
    pglob.Tabs['motifs']['motifbox'].setlist(())
    pglob.Tabs['motifs']['csvprep'] = {}
    pglob.Tabs['motifs']['delta']['state'] = tk.DISABLED
    pglob.Tabs['motifs']['csv']['state'] = tk.DISABLED
    pglob.Tabs['motifs']['findmotif']['state'] = tk.DISABLED
    def iterate4export(function,x,motif):
        last = None
        export = []
        stored.iterate = []
        cmd.iterate(function, 'stored.iterate.append((chain,resn,resi))')
        for iteration in stored.iterate:
            if last != iteration:
                export.append(iteration)
            last = iteration
        pglob.Tabs['motifs']['csvprep'][motif] = {}
        pglob.Tabs['motifs']['csvprep'][motif]['x'] = x
        pglob.Tabs['motifs']['csvprep'][motif]['pf'] = pglob.Tabs['motifs']['delta'].get()
        pglob.Tabs['motifs']['csvprep'][motif]['pdb'] = cmd.get_names().pop()
        pglob.Tabs['motifs']['csvprep'][motif]['res'] = export

    def ModBounds(x, exact, upper=None, lower=None):
        if x != 0 and x % exact == 0:
            return '1'
        elif upper != None and lower != None:
            upStatic = upper
            lowStatic = lower
            while x > lower:
                if x < upper:
                    return '2'
                upper += upStatic
                lower += lowStatic
        return '0'

    def cancel():
        pglob.Tabs['motifs']['cancel'] = True
        pglob.Tabs['motifs']['findmotif']['state'] = tk.NORMAL
        root.withdraw()

    def start():
        startbutton['state'] = tk.DISABLED
        cancelbutton['state'] = tk.NORMAL
        pglob.Tabs['motifs']['cancel'] = False
        group['tag_text'] = 'Searching... 0 Percent Complete'
        cmd.hide('everything', 'all')
        cmd.remove("all and hydro")
        found = []
        keys = motcod.motifs.keys()
        keysL = len(keys)
        last = 0.0
    
        for motif in keys:
            exact = motcod.motifs[motif]['exact']
            upper = motcod.motifs[motif]['upper']
            lower = motcod.motifs[motif]['lower']
            
            last += 1
            bar = (last/keysL)*100
            if pglob.Tabs['motifs']['cancel'] == True:
                print 'Motif Checker Cancelled by User at %.3s percent completion.'%(bar)
                group['tag_text'] = 'Press Start to Begin Search'
                root.update()
                break
            group['tag_text'] = 'Searching... %.3s%% Complete'%(bar)
            status.SetProgressPercent(bar)
            root.update()
            if exact == None:
                continue
            function = motcod.motifs[motif]['function']
            if motcod.MotifCaller(function,False):
                x = ModBounds(cmd.count_atoms(function),exact,upper,lower)
                if x != '0':
                    motifStr = '%s-%s'%(x,motif)
                    found.append(motifStr)
                    iterate4export(function,x,motifStr)
            cmd.delete(function)

        print 'Motif Finder finished with %s results.'%(len(found))
        cmd.orient('all')
        if len(found) != 0:
            found.sort()
            pglob.Tabs['motifs']['motifbox'].setlist(found)
            pglob.Tabs['motifs']['csv']['state'] = tk.NORMAL
        cmd.show('cartoon', 'all')
        cmd.color('gray', 'all')
        root.withdraw()
        pglob.Tabs['motifs']['findmotif']['state'] = tk.NORMAL
        pglob.Tabs['motifs']['delta']['state'] = tk.NORMAL
    
    root = tk.Tk()
    root.title('Motif Finder')
    root.protocol('WM_DELETE_WINDOW', cancel)
    group = Pmw.Group(root, tag_text='Press Start to Begin Search')
    group.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky=tk.NW)
    interior = group.interior()
    status = pglob.ProgressBar(interior,10,200,0,0,2)
    startbutton = tk.Button(interior, width=12, text='Start', command=start)
    startbutton.grid(row=1, column=0, padx=1, pady=1, sticky=tk.NW)
    cancelbutton = tk.Button(interior, width=12, text='Cancel', command=cancel)
    cancelbutton.grid(row=1, column=1, padx=1, pady=1, sticky=tk.NW)
    cancelbutton['state'] = tk.DISABLED
    
def resdel(event):
    try:
        objects = cmd.get_names('all')
        cmd.hide('sticks', '!'+mot)
        cmd.color('white', '!'+mot)
        if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
        if 'Adjacent' in objects:
            cmd.label('byres Adjacent',"''")
        cmd.delete('Adjacent')
    except:

        showinfo('Alert', 'You must load a motif first')
        interior.mainloop()

def roundres(event):
    try:
        cmd.hide('sticks', '!'+mot)
        cmd.color('white', '!'+mot)
        cmd.select('Adjacent', 'byres '+mot+' around %s'%(selA.get()))
        cmd.show('sticks', 'Adjacent')
        cmd.color('orange', 'Adjacent')
        util.cnc('Adjacent')
        cmd.remove('hydro')
        cmd.deselect()
    except:
        
        showinfo('Alert', 'You must load a motif first')
        interior.mainloop()

def randompdb():
    cmd.delete('all')
    lineFile = pglob.pathmaker('pdb_entry_type.txt')
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
        InHandle = urllib2.urlopen('ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt')
        OutHandle = open(lineFile,'w')
        for line in InHandle:
            OutHandle.write(line)
        OutHandle.close
        randompdb()

cmd.extend('randompdb',random)
        
def makemotif():
    pglob.Tabs['motif_maker']['resnnum'] = {}
    pf = pglob.Tabs['motif_maker']['pf'].get()
    pdb = pglob.Tabs['motif_maker']['pdb'].get()
    ec = pglob.Tabs['motif_maker']['ec'].get()
    resn = {}
    resi = {}
    backbone = {}
    chain = {}
    
    def addresn(resn):
        if resn in pglob.Tabs['motif_maker']['resnnum']:
            pglob.Tabs['motif_maker']['resnnum'][resn] += 1
            return resn
        pglob.Tabs['motif_maker']['resnnum'][resn] = 1
        return resn
    
    def getresnnum():
        resnstr = []
        for resn in pglob.Tabs['motif_maker']['resnnum']:
            if pglob.Tabs['motif_maker']['resnnum'][resn] == 1:
                resnstr.append(resn)
                continue
            resnstr.append('%s of %s'%(pglob.Tabs['motif_maker']['resnnum'][resn],resn))
        return ','.join(resnstr)
    
    def acceptresn(resn):
        if len(resn) == 0:
            return ''
        try:
            if len(resn) == 3:
                if resn in pglob.AminoList:
                    return resn
                raise KeyError
            newresn = pglob.AminoHashTable[resn]
        except KeyError:
            return None
        return newresn
    
    excepLoop = 0
    exceptions = ''
    cmd.reinitialize()
    exceptions += fetch(pdb,True)
    try:
        ectuple = ec.split('.')
        ec1,ec2,ec3,ec4 = ectuple
    except ValueError:
        exceptions += 'Please enter a correct EC number with periods.\n'
    else:
        if len(ec1) != 1 or int(ec1) < 1 or int(ec1) > 7:
            exceptions += 'The first EC number has to be >= 1 and <= 7.\n'
        if len(ec2) > 2 or len(ec2) < 1:
            exceptions += 'The second EC number has to be at most two digits.\n'
        if len(ec3) > 2 or len(ec3) < 1:
            exceptions += 'The third EC number has to be at most two digits.\n'
        if len(ec4) > 3 or len(ec4) < 1:
            exceptions += 'The fourth EC number has to be at most three digits.\n'
    
    skip = {}
    skip[0] = 0
    for i in range(1,11):
        resn[i] = acceptresn(pglob.Tabs['motif_maker']['resn'][i].get())
        resi[i] = pglob.Tabs['motif_maker']['resi'][i].get()
        backbone[i] = pglob.Tabs['motif_maker']['backbone'][i].get()
        chain[i] = pglob.Tabs['motif_maker']['chain'][i].get()
        skip[i] = False
        if resn[i] == '' and resi[i] == '' and chain[i] == '':
            ### this gives us the ability to skip whole blocks
            skip[i] = True
            skip[0] += 1
        elif resn[i] != '' and resi[i] != '' and chain[i] != '':
            if resn[i] == None:
                exceptions += 'Residue %s is not recongnized.\n'%(i)
            elif cmd.count_atoms('%s/%s`%s/'%(chain[i],resn[i],resi[i])) == 0:
                exceptions += 'There is no %s at number %s on chain %s.\n'%(resn[i],resi[i],chain[i])
            elif resn[i] == 'gly' and backbone[i] == 'Off':
                exceptions += 'Please turn on the backbone for glycine residue %s\n'%(i)
            excepLoop +=1
        else:    
            if resn[i] == '':
                exceptions += 'Please enter a residue for residue %s\n'%(i)
            if resi[i] == '':
                exceptions += 'Please enter a number for residue %s\n'%(i)
            if chain[i] == '':
                exceptions += 'Please select a chain for residue %s\n.'%(i)
            excepLoop +=1
    if excepLoop < 2:
        exception = True
        exceptions += 'Motifs require that 2 or more residues be entered.'
    if exceptions != '':
        showerror('Error', 'The following errors have occurred:\n'+exceptions)
    else:
        cmd.remove('resn HOH')
        
        name = 'P_%s_%s_%s_%s_%s'%(pdb,ec1,ec2,ec3,ec4)
        f=open(pglob.pathmaker('Motifs',name), 'w')
        f.write("def %s(d):\n"%(name))
        f.write("    '''")
        f.write("    FUNC:%s"%(name))
        f.write("    PDB:%s"%(pdb))
        f.write("    EC:%s"%(ec))
        f.write("    RESI:%s"%(getresnnum()))
        f.write("    '''")
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
            if skip[i] == False:
                if resn[i] not in numOfi:
                    numOfi[resn[i]] = 0
                resnlist.append(resn[i])
                resilist.append(resi[i])
                resnlistf.append(resn[i]+('i'*(numOfi[resn[i]])))
                chainlist.append(chain[i])
                bonelist.append(backbone[i])
                numOfi[resn[i]] += 1
        
        ### This loop will increment through the amino acids. The amino acid we are looking
        ### at right now is specified by the e variable. The a variable will count the
        ### number of times it is compared to the carbons in the other amino acids. And is
        ### used later on to print the "byres" and select line, and delete line below.
        ### NOTE:
        ### Because we are able to skip a whole block, mRN is not used beyond this point,
        ### instead resnlen is used as it gives a more accurate picture of the motif.
        resnlen = (len(resnlist)-1)
        e = 0
        while e < resnlen:
            a = 0
            e += 1
            ### select stuff explained later on
            selectlimit = 50
            selectstart = 1 ### where to start selection
            selectlimiter = 1 ### limit defined as a/selectlimit
            selectextra = '' ### add to selection at the end
            deleteextra = '' ### add to deletion at the end
            
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
                            f.write("    cmd.select('%s%s','"%(resnlistf[e],(selectlimiter*selectlimit)))
                            for i in range(selectstart,a):
                                if i==(a-1):
                                    f.write("br. %s%s')\n"%s(resnlistf[e],i))
                                else:
                                    f.write("br. %s%s&"%s(resnlistf[e],i))
                            f.write()
                            for i in range(selectstart,a):
                                if i==(a-1):
                                    pass
                                else:
                                    f.write("    cmd.delete('%s%s')\n"%s(resnlistf[e],i))
                            selectextra += '%s%s&'%(resnlistf[e],(selectlimiter*selectlimit))
                            deleteextra += "    cmd.delete('%s%s')\n"%(resnlistf[e],(selectlimiter*selectlimit))
                            selectlimiter += 1
                            selectstart += selectlimit
                        
                        ### e > d is all the combinations of residues
                        ### that would already have one of the residues
                        ### found in the motif, therefore the second
                        ### amino acid does not need an r. (resn)
                        ### property selection, as it is already a selection.
                        if e > d:
                            f.write("    cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlistf[d],g))
                        else:
                            f.write("    cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%(d*%s))\n"%(resnlistf[e],a,bList[b],resnlist[e],cList[c],resnlistf[d],g))
            f.write("    cmd.select('%s','"%(resnlistf[e]))
            if selectextra != '':
                f.write(selectextra)
            for i in range(selectstart,a+1):
                if i==a:
                    f.write("br. %s%s')\n"%(resnlistf[e],i))
                else:
                    f.write('br. %s%s&'%(resnlistf[e],i))
            if deleteextra != '':
                f.write(deleteextra)
            for i in range(selectstart,a+1):
                f.write("    cmd.delete('%s%s')\n"%(resnlistf[e],i))
    
        resnlistfstr = ""
        for i in range(1,resnlen+1):
            if i == resnlen:
                resnlistfstr += resnlistf[i]
            else:
                resnlistfstr += resnlistf[i]+'|'
    
        f.write("    cmd.select('%s','%s')\n"%(name,resnlistfstr))
        for i in range(1,resnlen+1):
            f.write("    cmd.delete('%s')\n"%(resnlistf[i]))
        f.write("    return {'motif':'%s'}"%(name))
    
        print '%s Amino Acid Motif Written \n\n\n\n'%(len(resnlist)-1)
        f.close()
