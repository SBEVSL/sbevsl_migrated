from pymol import cmd
from urllib import urlretrieve
import Tkinter as tk
import os
import math
import platform
import cPickle
PLATFORM = platform.system()
Tabs = {}
SELE = 'all'
script = 0
PROMOL_DIR_PATH = os.path.dirname(__file__)
try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
if PLATFORM == 'Windows':
    OFFSITE = os.path.join(os.environ['AppData'],'SBEVSL','ProMol')
elif PLATFORM == 'Darwin':
    OFFSITE = os.path.join(HOME,'Library','Application Support','SBEVSL','ProMol')
else:
    OFFSITE = os.path.join(HOME,'.sbevsl','ProMol')
DIRS = ('Motifs',)
if not os.path.isdir(OFFSITE):
    os.makedirs(OFFSITE)
for DIR in DIRS:
    DIR = os.path.join(OFFSITE,DIR)
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

def motifstore(folder,motdir):
    for motfile in motdir:
        func = motfile[0:-3]
        MOTIFS[func] = {}
        MOTIFS[func]['path'] = os.path.join(folder,motfile)
        tmpf = open(MOTIFS[func]['path'])
        hexf = ''
        i = 0
        for line in tmpf:
            hexf = ''.join([hexf,line])
            if line[0:3] == "'''":
                i+=1
                continue
            if i != 1:
                if line[0:3] != 'cmd' and line != '':
                    del MOTIFS[func]
                    tmpf.close()
                    break
            if line[0:4] == 'FUNC':
                funccheck = line.split(':')[1][0:-1]
                if func != funccheck:
                    del MOTIFS[func]
                    tmpf.close()
                    break
                continue
            if line[0:3] == 'PDB':
                pdbcheck = line.split(':')[1][0:-1]
                if func.split('_')[1] != pdbcheck:
                    del MOTIFS[func]
                    tmpf.close()
                    break
                MOTIFS[func]['pdb'] = pdbcheck
                continue
            if line[0:2] == 'EC':
                preec = func.split('_')
                ec = '.'.join((preec[2],preec[3],preec[4],preec[5]))
                eccheck = line.split(':')[1][0:-1]
                if ec != eccheck:
                    del MOTIFS[func]
                    tmpf.close()
                    break
                MOTIFS[func]['ec'] = eccheck
                continue
            if line[0:4] == 'RESI':
                resi = line.split(':')[1][0:-1]
                if resi == '':
                    del MOTIFS[func]
                    tmpf.close()
                    break
                MOTIFS[func]['resi'] = resi.split(',')
                continue

MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH,'Motifs')
USRMOTIFSFOLDER = os.path.join(OFFSITE,'Motifs')
MOTIFS = {}
#try:
#    MOTIFS = cPickle.load(open(os.path.join(OFFSITE,'motifs.pkl'),'r'))
#except (IOError,TypeError):
motifstore(MOTIFSFOLDER,os.listdir(MOTIFSFOLDER))
motifstore(USRMOTIFSFOLDER,os.listdir(USRMOTIFSFOLDER))
#    try:
#        cPickle.dump(MOTIFS,open(os.path.join(OFFSITE,'motifs.pkl'),'w'))
#    except (IOError,TypeError):
#        pass
            
splash = tk.PhotoImage(file = os.path.join(PROMOL_DIR_PATH,'splashmol.gif'))

AminoMenuList = ('','ala','arg','asn','asp','cys','gln','glu','gly','his','ile',
    'leu','lys','met','phe','pro','ser','thr','trp','tyr','val')
#Amino Acid Lists
AminoLongList = ('alanine','arginine','asparagine','aspartate','cysteine',
    'glutamine','glutamate','glycine','histidine','isoleucine','leucine',
    'lysine','methionine','phenylalanine','proline','serine','threonine',
    'tryptophan','tyrosine','valine')
AminoList = ('ala','arg','asn','asp','cys','gln','glu','gly','his','ile','leu',
    'lys','met','phe','pro','ser','thr','trp','tyr','val')
AminoShortList = ('a','r','n','d','c','q','e','g','h','i','l','k','m','f','p',
    's','t','w','y','v')
AminoSubsList = {
        3:'glu',
        6:'asp',
        5:'asn',
        2:'gln',
        15:'thr',
        16:'ser'
    }
AminoNumberList = (5,11,8,8,6,9,9,4,10,8,8,9,8,11,7,6,7,14,12,7)

AminoLongHashTable = {}
AminoHashTable = {}
AminoShortHashTable = {}
for i in range(0,20):
    AminoHashTable[AminoLongList[i]] = {}
    AminoHashTable[AminoList[i]] = {}
    AminoHashTable[AminoShortList[i]] = {}

    AminoHashTable[AminoLongList[i]]['l'] = AminoLongList[i]
    AminoHashTable[AminoList[i]]['l'] = AminoLongList[i]
    AminoHashTable[AminoShortList[i]]['l'] = AminoLongList[i]

    AminoHashTable[AminoLongList[i]][3] = AminoList[i]
    AminoHashTable[AminoList[i]][3] = AminoList[i]
    AminoHashTable[AminoShortList[i]][3] = AminoList[i]

    AminoHashTable[AminoLongList[i]][1] = AminoShortList[i]
    AminoHashTable[AminoList[i]][1] = AminoShortList[i]
    AminoHashTable[AminoShortList[i]][1] = AminoShortList[i]
    
    AminoHashTable[AminoLongList[i]][0] = AminoNumberList[i]
    AminoHashTable[AminoList[i]][0] = AminoNumberList[i]
    AminoHashTable[AminoShortList[i]][0] = AminoNumberList[i]
    
    if i in AminoSubsList:
        AminoHashTable[AminoLongList[i]]['s'] = AminoSubsList[i]
        AminoHashTable[AminoList[i]]['s'] = AminoSubsList[i]
        AminoHashTable[AminoShortList[i]]['s'] = AminoSubsList[i]

Photos = {}
for x in AminoList:
    x = x.upper()
    for y in ('3D', '2D'):
        Photos["%s%s" % (x, y)] = tk.PhotoImage(
            file = os.path.join(PROMOL_DIR_PATH,'AminoPics',x+y+'.gif'))
#/*=====================*//*==========================================*/
#/*   DNA Nucleotides   *//*  DNA Nucleotides PDB Revision, Jul 2007  */
#/*=====================*//*==========================================*/
DNA = ("A", "C", "G", "T","DA", "DC", "DG", "DT","DI")
DNASTR = '+'.join(DNA)
#/*===================*/
#/*  RNA Nucleotides  */
#/*===================*/
RNA = ("U", "I", "1MA",
       "5MC", "OMC", "1MG", "2MG",
       "M2G", "7MG", "OMG", "YG",
       "H2U", "5MU", "PSU")
RNASTR = '+'.join(RNA)
#A - Z
AlphaSequence = [ "%c" % (x) for x in range(ord('A'), ord('Z')+1)]
#a - z
alphasequence = [ "%c" % (x) for x in range(ord('a'), ord('z')+1)]
#the original CPK plastic models developed by Corey, Pauling and Kultun
CPKDict = {
      "H":"[1.000,1.000,1.000]","He":"[1.000, 0.753, .796]",
     "Li":"[.698, .133, .133]",  "B":"[0, 1.000, 0]",
     "Cl":"[0, 1.000, 0]",       "C":"[.784, .784, .784]",
      "N":"[.561, .561, 1.000]", "O":"[1.000, 0, 0]",
      "F":"[.855, .647, .125]", "Si":"[.855, .647, .125]",
     "Au":"[.855, .647, .125]", "Na":"[0, 0, 1.000]",
     "Mg":"[.133, 139, .133]",  "Al":"[.502, .502, .565]",
     "Ca":"[.502, .502, .565]", "Ti":"[.502, .502, .565]",
     "Cr":"[.502, .502, .565]", "Mn":"[.502, .502, .565]",
     "Ag":"[.502, .502, .565]",  "P":"[1.000, .647, 0]",
     "Fe":"[1.000, .647, 0]",   "Ba":"[1.000, .647, 0]",
      "S":"[1.000, 1.000, 0]",  "Ni":"[.647, .165, .165]",
     "Cu":"[.647, .165, .165]", "Zn":"[.647, .165, .165]",
     "Br":"[.647, .165, .165]",  "I":"[.627, .125, .941]",
    "UNK":"[1.000, .078, .576]"}
#CPKNew Based off the original CPK plastic models
CPKNewDict = {
      "H":"[1.000,1.000,1.000]","He":"[1.000, 0.753, .796]",
     "Li":"[.698, .129, .129]",  "B":"[0, 1.000, 0]",
     "Cl":"[0, 1.000, 0]",       "C":"[.827, .827, .827]",
      "N":"[.529, .808, .922]",  "O":"[1.000, 0, 0]",
      "F":"[.855, .647, .125]", "Si":"[.855, .647, .125]",
     "Au":"[.855, .647, .125]", "Na":"[0, 0, 1.000]",
     "Mg":"[.133, 139, .133]",  "Al":"[.412, .412, .412]",
     "Ca":"[.412, .412, .412]", "Ti":"[.412, .412, .412]",
     "Cr":"[.412, .412, .412]", "Mn":"[.412, .412, .412]",
     "Ag":"[.412, .412, .412]",  "P":"[1.000, .667, 0]",
     "Fe":"[1.000, .667, 0]",   "Ba":"[1.000, .667, 0]",
      "S":"[1.000, 1.000, 0]",  "Ni":"[.502, .157, .157]",
     "Cu":"[.502, .157, .157]", "Zn":"[.502, .157, .157]",
     "Br":"[.502, .157, .157]",  "I":"[.627, .125, .941]",
    "UNK":"[1.000, .086, .569]"}

def pathmaker(*args,**options):
    newargs = [PROMOL_DIR_PATH]
    if 'root' in options:
        newargs = [options['root']]
    for x in args:
        if type(x).__name__ == 'tuple':
            x = ''.join(x)
        newargs.append(x)
    return os.sep.join(newargs)

def defaults(tag = ''):
    if tag == 'cartoon':
        cmd.set('cartoon_rect_length', '1.4', 'all')
        cmd.set('cartoon_oval_length', '1.4', 'all')
        cmd.set('cartoon_rect_width', '0.3', 'all')
        cmd.set('cartoon_oval_width', '0.3', 'all')
        cmd.set('cartoon_tube_radius', '0.5', 'all')
        cmd.set('cartoon_transparency', '0.0', 'all')
        cmd.cartoon('automatic', sel1)
        toonWidth.set('1.4')
        toonThickness.set('0.3')
        cartoonTransparency.set('0.0')
        toonTubeRadius.set('0.5')
        ribbonTypes.invoke(0)
    elif tag == 'spheres':
        cmd.set('sphere_scale', '0.7', 'all')
        cmd.set('sphere_transparency', '0.0', 'all')
        sphereScale.set('0.7')
        sphereTransparency.set('0.0')
    elif tag == 'sticks':
        cmd.set('stick_radius', '0.2', 'all')
        cmd.set('stick_transparency', '0.0', 'all')
        stickRadius.set('0.2')
        stickTransparency.set('0.0')
    elif tag == 'surface':
        cmd.set('transparency', '0.0', 'all')
        surfaceTransparency.set('0.0')
    elif tag == 'ambient':
        cmd.set('ambient', '0.25', 'all')
        asca.set('0.25')
    cmd.delete('surface')
    cmd.delete('mesh1')
    cmd.delete('cartoon')
    cmd.delete('helix')
    cmd.delete('sheets')
    cmd.delete('sticks')
    cmd.delete('rov_1')
    cmd.delete('rov_m1')
    cmd.delete('map1')
    cmd.delete('sphere1')
    cmd.delete('rov_pc')
    cmd.delete('rov_s1')
    cmd.set("roving_detail", 0)
    cmd.set("roving_origin", 0)
    cmd.set("roving_sticks", 0)
    cmd.set('roving_spheres', 0)
    cmd.set("roving_polar_contacts", 0)
    cmd.set('roving_lines', 0)
    cmd.set('roving_isosurface', 0)
    cmd.set('transparency', '0.0', 'all')
    cmd.set('cartoon_transparency', '0.0', 'all')
    cmd.set('sphere_transparency', '0.0', 'all')
    cmd.set('stick_transparency', '0.0', 'all')
    cmd.set('sphere_scale', '0.7', 'all')
    cmd.set('stick_radius', '0.2', 'all')
    cmd.cartoon('automatic', 'all')
cmd.extend('defaults', defaults)

def deletemotif():
    pass
cmd.extend('deletemotif', deletemotif)

def procolor(selection=None,show_selection='sticks',color_selection='cpk',
        show_all=('sticks','spheres'),color_all='cpk',cpknew=False):
    def cpk(cpkkit,selection):
        unk = 'not e. '
        cpk,suffix = cpkkit
        for k in cpk:
            if k != 'UNK':
                cmd.color('%s%s'%(k,suffix),'(e. %s & %s)'%(k,selection))
                unk += '%s+'%(k)
        cmd.color('UNK%s'%(suffix),'((%s) & %s)'%(unk[:-1],selection))
    def setcolors(cpknew):
        colorIndex = {}
        for i in cmd.get_color_indices():
            k,v = i
            colorIndex[k] = v
        if cpknew:
            cpk = CPKNewDict
            suffix = 'cpknew'
        else:
            cpk = CPKDict
            suffix = 'cpk'
        for k in cpk:
            color = '%s%s'%(k,suffix)
            if color not in colorIndex:
                cmd.set_color(color,cpk[k])
        return cpk,suffix
    def show(selection,toshow,tocolor,cpknew):
        if type(toshow).__name__ == 'tuple':
            for show in toshow:
                cmd.show('%s'%(show),'%s'%(selection))
        else:
            cmd.show('%s'%(toshow),'%s'%(selection))
        if tocolor == 'cpk':
            cpk(setcolors(cpknew),selection)
        else:
            cmd.color('%s'%(tocolor),'%s'%(selection))
    if show_all != None:
        cmd.hide('everything','all')
        show('all', show_all, color_all, cpknew)
    if selection != None:
        show(selection, show_selection, color_selection, cpknew)
cmd.extend('procolor', procolor)

def populate():
    cmd.select('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.select('dna', 'resn %s'%(DNASTR))
    cmd.select('rna', 'resn %s'%(RNASTR))
    cmd.select('hydrophobic', 'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
    cmd.select('hydrophilic', 'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
    cmd.select('acidic', 'resn ASP+GLU')
    cmd.select('basic', 'resn ARG+HIS+LYS')
    cmd.select('ligands', 'het')
    cmd.select('heme', 'resn hem')
    cmd.disable('heme')
    cmd.disable('ligands')
    cmd.disable('basic')
    cmd.disable('acidic')
    cmd.disable('hydrophilic')
    cmd.disable('hydrophobic')
    cmd.disable('dna')
    cmd.disable('rna')
    cmd.disable('protein')
    for letter in AlphaSequence:
        chain = 'Chain-%s'%(letter)
        cmd.select(chain, "chain %s"%(letter))
        if(len(cmd.index(chain)) < 1):
            cmd.delete(chain)
    #cmd.select("Chain-' '", "chain ' '")
    # if 'Chain-' '' in objects:
    #         if(len(cmd.index('Chain-' '')) < 1):
    #             cmd.delete('Chain-' '')
    objects = cmd.get_names('all')
    for obj in objects:
        try:
            if(len(cmd.index(obj)) < 1):
                cmd.delete(obj)
        except:
            cmd.delete(obj)
    objects = cmd.get_names('all')
    items = []
    items.append('All')
    items.append('Selected')
    items.append('Not Selected')
    for obj in objects:
        items.append(obj)
    Tabs['ez_viz']['selection'].configure(command = None)
    Tabs['view']['advanced_selection'].configure(command = None)
    Tabs['ez_viz']['selection'].setitems(items)
    Tabs['view']['advanced_selection'].setitems(items)
    Tabs['ez_viz']['selection'].configure(command = set_selection)
    Tabs['view']['advanced_selection'].configure(command = set_selection)
cmd.extend('populate', populate)

def update():
    defaults()
    populate()
    cmd.remove('resn HOH')
    cmd.orient('all')
cmd.extend('update', update)

def set_selection(tag='all'):
    global SELE
    Tabs['ez_viz']['selection'].setvalue(tag)
    Tabs['view']['advanced_selection'].setvalue(tag)
    if tag == 'Not Selected':
        SELE = '!sele'
    elif tag == 'Selected':
        SELE = 'sele'
    else:
        SELE = tag

class ProgressBar:
    def __init__(self, Parent, Height=10, Width=100, Row=0, Column=0, Span=1,
                 ForegroundColor=None, BackgroundColor=None, Progress=0):
        self.Height=Height
        self.Width=Width
        self.BarCanvas = tk.Canvas(Parent,
            width=Width,height=Height,
            background=BackgroundColor,borderwidth=1,
            relief=tk.SUNKEN)
        if (BackgroundColor):
            self.BarCanvas["backgroundcolor"]=BackgroundColor
        self.BarCanvas.grid(row=Row,column=Column,columnspan=Span,padx=5,pady=2)
        self.RectangleID=self.BarCanvas.create_rectangle(0,0,0,Height)
        if (ForegroundColor==None):
            ForegroundColor="black"
        self.BarCanvas.itemconfigure(self.RectangleID,fill=ForegroundColor)
        self.SetProgressPercent(Progress)        
    def SetProgressPercent(self,NewLevel):
        self.Progress = math.floor(NewLevel)
        self.Progress = min(100,self.Progress)
        self.Progress = max(0,self.Progress) 
        self.DrawProgress()
    def DrawProgress(self):
        ProgressPixel=(self.Progress/100.0)*self.Width
        self.BarCanvas.coords(self.RectangleID,
            0,0,ProgressPixel,self.Height)
    def GetProgressPercent(self):
        return self.Progress

## {{{ http://code.activestate.com/recipes/285264/ (r1)
# ---------------------------------------------------------
# natsort.py: Natural string sorting.
# ---------------------------------------------------------

# By Seo Sanghyeon.  Some changes by Connelly Barnes.

def natcmp(a, b):
    "Natural string comparison, case sensitive."
    def natsort_key(s):
        "Used internally to get a tuple by which s is sorted."
        def try_int(s):
            "Convert to integer if possible."
            try: return int(s)
            except: return s
        import re
        return map(try_int, re.findall(r'(\d+|\D+)', s))
    return cmp(natsort_key(a), natsort_key(b))

def natcmpi(a, b):
    "Natural string comparison, ignores case."
    return natcmp(a.lower(), b.lower())

def natsort(seq, cmp=natcmp):
    "In-place natural string sort."
    seq.sort(cmp)

def natsorted(seq, cmp=natcmp):
    "Returns a copy of seq, sorted by natural string sort."
    import copy
    temp = copy.copy(seq)
    natsort(temp, cmp)
    return temp
