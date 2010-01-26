from pymol import cmd
import Tkinter as tk
import Pmw
import linecache
import random
import os
import urllib2
import time
from tkFileDialog import askopenfilename
from tkSimpleDialog import askstring
from tkMessageBox import showinfo
from tkMessageBox import showerror
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods import motifcoded as motcod
from pmg_tk.startup.remote_pdb_load import remote


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
    try:
        if len(tag) == 0:
            print 'No selection for double click'
        if tag in motcod.motifs.keys():
            motcod.MotifCaller(motcod.motifs[tag]['function'])
    except:
        showinfo('Alert', 'There is no motif there')

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

def resetrange():
    pglob.Tabs['motifs']['delta'].set(1)

def setcusmotif():
    a = []
    for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
        a.append(object)
    motifdrop.setlist(a)

def runcusmotif():
        a = ['']
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        motif = motifdrop.getcurselection()
        for item in motif:
            tag = item
        try:
             for i in range(1, 100, 1):
                if a[i] in tag:
                    cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[i])
        except:
            pass

def motifchecker():
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
        group['tag_text'] = 'Cancelling Search. Please Wait.'
        root.update()

    def start():
        startbutton['state'] = DISABLED
        cancelbutton['state'] = NORMAL
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
                print 'Motif Checker Cancelled by User at %.2s percent completion.'%(bar)
                group['tag_text'] = 'Press Start to Begin Search'
                root.update()
                break
            group['tag_text'] = 'Searching... %.2s Percent Complete'%(bar)
            status.SetProgressPercent(bar)
            root.update()
            if exact == None:
                continue
            function = motcod.motifs[motif]['function']
            if motcod.MotifCaller(function,False):
                cmd.do('count_atoms %s'%(function))#need to sync pymol/promol threads
                x = ModBounds(cmd.count_atoms(function),exact,upper,lower)
                if x != '0':
                    found.append('%s-%s'%(x,motif))
            cmd.do('delete %s'%(function))

        print 'Motif Finder completed with %s results.'%(len(found))
        cmd.orient('all')
        found.sort()
        pglob.Tabs['motifs']['motifbox'].setlist(found)
        cmd.show('cartoon', 'all')
        cmd.color('white', 'all')
        root.withdraw()

    root = tk.Tk()
    root.title('Motif Finder')
    group = Pmw.Group(root, tag_text='Press Start to Begin Search')
    group.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky = tk.NW)
    interior = group.interior()
    status = pglob.ProgressBar(interior,10,200,0,0,2)
    startbutton = tk.Button(interior, width = 12, text = 'Start', command=start)
    startbutton.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
    cancelbutton = tk.Button(interior, width = 12, text = 'Cancel', command=cancel)
    cancelbutton.grid(row=1, column=1, padx=1, pady=1, sticky = tk.NW)
    cancelbutton['state'] = DISABLED
    
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

def randomized():
    cmd.delete('all')
    lineFile = os.path.join(pglob.PROMOL_DIR_PATH,'pdb_entry_type.txt')
    while os.path.exists(lineFile):
        expiration = (os.path.getmtime(lineFile)+864000)
        if expiration <= time.time():
            os.remove(lineFile)
        else:
            lines = sum([1 for line in lineFile])
            pdbCode = linecache.getline(lineFile,random.randint(1, lines))[0:4]
            remote(pdbCode)
            break
    else:
        InHandle = urllib2.urlopen('ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt')
        OutHandle = open(lineFile,'w')
        for line in InHandle:
            OutHandle.write(line)
        OutHandle.close
        randomized()

cmd.extend('randomized',randomized)

def runum():#run all the motifs and count the atoms n the Motifs folder
        
        a = ['']
        entz.delete(0,1000)
        entz.insert(0,0)
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        skipping =True
        list  = []
        while skipping:
            
            z = int(entz.get()) + 1
            entz.delete(0,1000)
            entz.insert(0,z)
            try:
                cmd.set("suspend_updates",1,quiet=1)
                time.sleep(1)#rate limiter
                cmd.delete('Motif')
                cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[z])
                cmd.set("suspend_updates",0,quiet=1)
                time.sleep(1)#rate limiter
                
                r = cmd.count_atoms('Motif')
                entcount.delete(0,100)
                entcount.insert(0,r)
                
                
                time.sleep(1)
                if len(entcount.get())==1:
                       list.append(entcount.get()+'        '+a[z])
                if len(entcount.get())==2:
                       list.append(entcount.get()+'       '+a[z])
                if len(entcount.get())==3:
                       list.append(entcount.get()+'      '+a[z])
            
            
            except:
                cmd.set("suspend_updates",0,quiet=1)
                skipping = False
                motifdrop.setlist(list)
                list.sort()

def loadmotifer():
    try:
        ###mRN = motif resn number aka number of residues in motif
        premRN = askstring('Motif Maker','How many residues are in your motif?\n'
                                          +'Please enter a number >= 2 and <=10.\n')
        if premRN == None:
            raise Exception
        else:
            mRN = int(premRN)
        if mRN < 2 or mRN > 10:
            raise ValueError
        
        def populate_chain_list():
            items=[]
            items.append('')
            for letter in pglob.AlphaSequence:
                if cmd.count_atoms("chain "+letter) > 0:
                    items.append(letter)
            items.sort()
            for i in range(1,mRN+1):
                chain[i].setitems(items)
        
        def makemotif():
            try:
                exception = False
                excepLoop = 0
                exceptions = ''
                skip = {}
                skip[0] = 0
                for i in range(1,mRN+1):
                    skip[i] = False
                    if resn[i].getvalue() == '' and resi[i].get() != '':
                        exception = True
                        exceptions += 'Please enter a residue for residue %s\n'%(i)
                    elif resn[i].getvalue() != '' and resi[i].get() == '':
                        exception = True
                        exceptions += 'Please enter a number for residue %s\n'%(i)
                    elif resn[i].getvalue() == '' and resi[i].get() == '':
                        ### this gives us the ability to skip whole blocks
                        skip[i] = True
                        skip[0] += 1
                    else:
                        excepLoop +=1
                        if chain[i].getvalue() == '':
                            exception = True
                            exceptions += 'Please select a chain for residue %s\n.'%(i)
                        elif resn[i].getvalue() == "gly" and backbone[i].getvalue() == "Off":
                            exception = True
                            exceptions += 'Please turn on the backbone for glycine residue %s\n'%(i)
                        elif cmd.count_atoms(chain[i].getvalue()+'/'+resn[i].getvalue()+'`'+resi[i].get()+'/') == 0:
                            exception = True
                            exceptions += 'There is no '+resn[i].getvalue()+' at number '+resi[i].get()+' on chain '+chain[i].getvalue()+'.\n'
                if excepLoop < 2:
                    exception = True
                    exceptions += 'Motifs require that 2 or more residues be entered.'
                if exception == True:
                    
                    showinfo('Error', 'The following errors have occurred:\n'+exceptions)
                    interior.mainloop()
                else:
                    cmd.remove('resn HOH')
                    
                    Q = asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                    if Q == None:
                        interior.mainloop()
                    f=open(Q, 'w')
                    f.write("######################################################################\n")
                    f.write("### This motif uses shortened selection algebra and property selectors\n")
                    f.write("### + = and\n")
                    f.write("### w. = within\n")
                    f.write("### br. = byres\n")
                    f.write("### r. = resn\n")
                    f.write("### n. = name\n")
                    f.write("### e. = elem\n")
                    f.write("######################################################################\n")
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
                    
                    numOfi = 0
                    for i in range(1,mRN+1):
                        if skip[i] == False:
                            resnlist.append(resn[i].getvalue())
                            resilist.append(resi[i].get())
                            resnlistf.append(resn[i].getvalue()+('i'*(numOfi)))
                            chainlist.append(chain[i].getvalue())
                            bonelist.append(backbone[i].getvalue())
                            numOfi += 1
                    
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
                        try:
                            try:
                                a = 0
                                e += 1
                                ### select stuff explained later on
                                selectlimit = 200
                                selectstart = 1 ### where to start selection
                                selectlimiter = 1 ### limit defined as a/200
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
                                    try:
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
                                                try:
                                                    c += 1
                                                    
                                                    ### Okay lets get the distance between our atoms in our selected amino acids.
                                                    r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+bList[b],chainlist[d]+'/'+resilist[d]+'/'+cList[c])
                                                    ### The precision factor
                                                    ### The ranger is the slider that is moved.
                                                    ### r is set by the get_distance above.
                                                    g = '%.2f' %(float(r) + float(ranger1.get()))
                                                    
                                                    a += 1
                                                    
                                                    ### apparently pymol cannot handle over a number
                                                    ### between 248 and 264 selections at one time.
                                                    ### This fixes that by making sure we do not pass
                                                    ### "selectlimit" selections at one time.
                                                    if float(selectlimiter) < (float(a)/float(selectlimit)):
                                                        f.write("cmd.select('"+resnlistf[e]+str(selectlimiter*selectlimit)+"','")
                                                        for i in range(selectstart,a):
                                                            if i==(a-1):
                                                                f.write("br. "+resnlistf[e]+str(i)+"')\n")
                                                            else:
                                                                f.write("br. "+resnlistf[e]+str(i)+" and ")
                                                        f.write("cmd.delete('")
                                                        for i in range(selectstart,a):
                                                            if i==(a-1):
                                                                pass
                                                            elif i==(a-2):
                                                                f.write(resnlistf[e]+str(i)+"')\n")
                                                            else:
                                                                f.write(resnlistf[e]+str(i)+"+")
                                                        selectextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+' and '
                                                        deleteextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+'+'
                                                        selectlimiter += 1
                                                        selectstart += selectlimit
                                                    
                                                    ### e > d is all the combinations of residues
                                                    ### that would already have one of the residues
                                                    ### found in the motif, therefore the second
                                                    ### amino acid does not need an r. (resn)
                                                    ### property selection, as it is already a selection.
                                                    if e > d:
                                                        f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and '+resnlistf[d]+'"%('+g+'))\n')
                                                        continue
                                                    else:
                                                       f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and r. '+resnlist[d]+'"%('+g+'))\n')
                                                       continue
                                                except:
                                                    pass
                                    except:
                                        pass
                            except:
                                pass
                        finally:
                            f.write('cmd.select("'+resnlistf[e]+'","')
                            if selectextra != '':
                                f.write(selectextra)
                            for i in range(selectstart,a+1):
                                if i==a:
                                    f.write('br. '+resnlistf[e]+str(i)+'")\n')
                                else:
                                    f.write('br. '+resnlistf[e]+str(i)+' and ')
                            f.write('cmd.delete("')
                            if deleteextra != '':
                                f.write(deleteextra)
                            for i in range(selectstart,a+1):
                                if i==a:
                                    f.write(resnlistf[e]+str(i)+'")\n')
                                else:
                                    f.write(resnlistf[e]+str(i)+'+')
                
                resnlistfstr = ""
                for i in range(1,resnlen+1):
                    if i == resnlen:
                        resnlistfstr += resnlistf[i]
                    else:
                        resnlistfstr += resnlistf[i]+'+'
                
                f.write("cmd.select('Motif','%s')\n"%(resnlistfstr))
                f.write("cmd.delete('%s')\n"%(resnlistfstr))
                f.write('cmd.hide("everything","all")\n')
                f.write('cmd.show("cartoon", "all")\n')
                f.write('cmd.set("cartoon_transparency","0.5", "all")\n')
                f.write('cmd.show("sticks","Motif")\n')
                f.write('cmd.color("grey","all")\n')
                f.write('cmd.color("oxygen","(e. O+Motif)")\n')
                f.write('cmd.color("nitrogen","(e. N+Motif)")\n')
                f.write('cmd.color("sulfur","(e. S+Motif)")\n')
                f.write('cmd.color("hydrogen","(e. H+Motif)")\n')
                f.write('cmd.color("white","(e. C+Motif)")\n')
                f.write('cmd.deselect()\n')
                f.write('cmd.orient("Motif")\n')
                
                print '%s Amino Acid Motif Written \n\n\n\n'%(len(resnlist)-1)
                f.close()
                interior.mainloop()
            except:
                pass
        
        root = tk.Tk()
        root.title('Motif Maker')
        group = Pmw.Group(root, tag_text='Motif Maker')#And a new group
        group.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky = tk.NW)
        interior = group.interior()
        
        resn = {}
        for i in range(1,mRN+1):
            resn[i] = Pmw.OptionMenu(interior,labelpos = tk.W,
                                        label_text = 'Residue %s:'%(i),
                                        items = pglob.AminoMenuList,
                                        menubutton_width = 8)
            resn[i].grid(row = (i-1), column =0)
        
        lent = {}
        for i in range(1,mRN+1):
            lent[i] = tk.Label(interior, text = 'Number:')
            lent[i].grid(row = (i-1), column = 1)
        
        resi = {}
        for i in range(1,mRN+1):
            resi[i] = tk.Entry(interior, width = 8)
            resi[i].grid(row = (i-1), column = 2)
        
        backbone = {}
        for i in range(1,mRN+1):
            backbone[i] = Pmw.OptionMenu(interior,labelpos = tk.W,
                                         label_text = 'BackBone:',
                                         items = ('Off', 'On'),
                                         menubutton_width = 8)
            backbone[i].grid(row = (i-1), column = 3)
        
        chain = {}
        for i in range(1,mRN+1):
            chain[i] = Pmw.OptionMenu(interior,labelpos =  tk.W,
                                          label_text = 'Chain %s:'%(i),
                                          items = (''),
                                          menubutton_width = 8)
            chain[i].grid(row=(i-1), column=4)
        
        but1 = tk.Button(interior, text = 'Make Motif', width = 10, command = makemotif)
        but1.grid(row =mRN, column = 3, sticky = tk.SE)
        
        popbtn = tk.Button(interior, text = 'Chain Info', width = 10, command = populate_chain_list)
        popbtn.grid(row = mRN, column = 4, sticky = tk.SE)
        
        framerange = tk.Frame(interior)
        framerange.grid(row=mRN, column=0,columnspan = 3, sticky = tk.E)
        ballrange = Pmw.Balloon(interior)
        ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault = 2')
        ranger1 = tk.Scale(framerange, width =8,
                        troughcolor="#ffffff",
                        length="160",
                        orient="horizontal",
                        resolution="0.1",
                        to="4.0")
        ranger1.grid(row=5, column=1,columnspan = 4, sticky = tk.E)
        ranger1.set(2)
        
        labrange = tk.Label(interior, text='Precision Factor:')
        labrange.grid(row=mRN, column=0, sticky = tk.SW)
        
        group = Pmw.Group(root, tag_text = 'Run Motif')
        group.grid(row=1, column=1, padx=2, pady=2, sticky = tk.W)
        interior = group.interior()
        
        def getmotif():
            
            f = askopenfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
            if f == None:
                interior.mainloop()
            else:
                cmd.do('run '+f+'')
                interior.mainloop()
        openbtn = tk.Button(interior, text= 'Open Motif', command = getmotif)
        openbtn.grid()
    
    #---------------------Show residues around active site---------------#
        def motifoption(tag):
                if tag=='Surface Pocket':
                    objects = cmd.get_names('all')
                    cmd.set('transparency', '0.5', 'all')
                    if 'Motif' in objects:
                        cmd.show('surface', 'all')
                        cmd.hide('cartoon', 'all')
                        cmd.color('white', '!Motif ')
                elif tag=='Polar Contacts':
                        try:
                            objects = cmd.get_names('all')
                            cmd.dist("Motif_polar_conts","Motif","Motif",quiet=1,mode=2,label=0,reset=1)
                            cmd.enable(mot+"_polar_conts")
                        except:
                            pass
                        
                        if 'Adjacent' in objects:
                            cmd.dist('Adjacent_polar_conts','Adjacent','Adjacent',quiet=1,mode=2,label=0,reset=1)
                        if 'substrate' in objects:
                            cmd.dist("Motif_around_polar_conts","Motif","(byobj (Motif)) and (not (Motif))",quiet=1,mode=2,label=0,reset=1)
                            cmd.enable("Motif_around_polar_conts")
                elif tag=='Hide Contacts':
                    objects = cmd.get_names('all')
                    try:
                          try:
                            cmd.delete("Motif_polar_conts")
                          except:
                            pass
                          if 'Adjacent' in objects:
                            cmd.delete('Adjacent_polar_conts')
                          if 'substrate' in objects:
                            cmd.delete("substrate_polar_conts")
                    except:
                          
                          showinfo('Alert', "No motif polar contacts to hide")
                elif tag=='Show Substrate':
                    try:
                      cmd.select('substrate', 'byres het within 7 of  Motif')
                      objects = cmd.get_names('all')
                      xp = cmd.index('substrate')
                      np  = len(xp)
                      if(np < 1):
                          cmd.delete('substrate')
                      if 'substrate' in objects:
                          cmd.show('sticks', 'substrate')
                          cmd.deselect()
                          cmd.color("oxygen","(elem O and substrate)")
                          cmd.color("nitrogen","(elem N and substrate)")
                          cmd.color("sulfur","(elem S and substrate)")
                          cmd.color("hydrogen","(elem H and substrate)")
                          cmd.color("white","(elem C and substrate)")
                    except:
                        
                        showinfo('Alert', "No substrate found")
                elif tag=='Show label':
                 objects = cmd.get_names('all')
                 try:
                              cmd.label('''(name ca+C1*+C1' and (byres(Motif)))''','''"%s-%s"%(resn,resi)''')
                              if 'Adjacent' in objects:
                                     cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''','''"%s-%s"%(resn,resi)''')
                 except:
                            
                            showinfo('Alert', "Select a motif first")
                elif tag=='Hide Label':
                    objects = cmd.get_names('all')
                    try:
                          cmd.label("Motif","''")
                          if 'Adjacent' in objects:
                              cmd.label('byres Adjacent',"''")
                    except:
                            
                            showinfo('Alert', "No motif labels to hide")
                elif tag=='Hide Substrate':
                                  try:
                                    cmd.hide('sticks', 'substrate')
                                  except:
                                    
                                    showinfo('Alert', "No substrate selected")
        stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos = 'w',
                    items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                    menubutton_width = 8, command=motifoption)
        stereo.grid(row=0,column=3,sticky = tk.NW)
        
        group = Pmw.Group(root, tag_text='Adjacent')
        group.grid(row=1, column=0, padx=2, pady=2, sticky = tk.W)
        
        interior = group.interior()
        framesela = tk.Frame(interior)
        framesela.grid(row=0, column=0, columnspan = 2, padx=0, pady=0, sticky = tk.N)
        ballsela = Pmw.Balloon(interior)
        ballsela.bind(framesela, 'Within # Angstroms')
        selA = tk.Scale(framesela, width = 8)
        selA.configure(troughcolor="#ffffff")
        selA.configure(length="130")
        selA.configure(orient="horizontal")
        selA.configure(resolution="0.2")
        selA.configure(to="10.0")
        selA.grid(row=0, column=0, columnspan= 2, padx=0, pady=0, sticky = tk.N)
        selA.set(5.0)
        frameadj = tk.Frame(interior)
        frameadj.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
        balladj = Pmw.Balloon(interior)
        balladj.bind(frameadj, 'Display residues adjacent to motif')
        

        showround = tk.Button(frameadj, width = 12, text = 'Adjacent', command = roundres)
        showround.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
        showround.bind('<Button-1>', roundres)
        

        delres = tk.Button(interior, width = 14, text = 'Delete Adjacent', command = resdel)
        delres.grid(row=1, column=1, padx=1, pady=1, sticky = tk.NW)
        delres.bind('<Button-1>', resdel)
    
    except ValueError:
        
        showinfo('Error', 'Please enter a number greater than or equal to 2.\n'
                                                        +'Please enter a number less than or equal to 10.')
        loadmotifer()
