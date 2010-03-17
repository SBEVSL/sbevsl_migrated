from pymol import cmd
import Tkinter as tk
import os
import math
import platform
PLATFORM = platform.system()

Photos = None
script = 0
AminoMenuList = None
AminoList = None
AlphaSequence = None
alphaSequence = None
Tabs = {}
try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
try:
    PYMOL_PATH = os.environ['PYMOL_PATH']
except KeyError:
    PYMOL_PATH = '.'
if PLATFORM == 'Windows' or PLATFORM == 'Darwin':
    PROMOL_PATH = os.path.join(PYMOL_PATH,'modules','pmg_tk','startup')
    PROMOL_DIR_PATH = os.path.join(PROMOL_PATH,'ProMol_dir')
else:
    PROMOL_PATH = os.path.join(PYMOL_PATH.split(os.sep+'pymol')[0],'pmg_tk','startup')
    PROMOL_DIR_PATH = os.path.join(PROMOL_PATH,'ProMol_dir')

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
AminoLongHashTable = {}
AminoHashTable = {}
AminoShortHashTable = {}
for i in range(0,20):
    AminoLongHashTable[AminoList[i]] = AminoLongList[i]
    AminoLongHashTable[AminoShortList[i]] = AminoLongList[i]
for i in range(0,20):
    AminoHashTable[AminoLongList[i]] = AminoList[i]
    AminoHashTable[AminoShortList[i]] = AminoList[i]
for i in range(0,20):
    AminoShortHashTable[AminoLongList[i]] = AminoShortList[i]
    AminoShortHashTable[AminoList[i]] = AminoShortList[i]

Photos = {}
for x in AminoList:
    x = x.upper()
    for y in ('3D', '2D'):
        Photos["%s%s" % (x, y)] = tk.PhotoImage(
            file = os.path.join(PROMOL_DIR_PATH,'AminoPics',x+y+'.gif'))

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

def pathmaker(*args):
    newargs = [x for x in args]
    newargs.insert(0,PROMOL_DIR_PATH)
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

def checkforchain():
    objects = cmd.get_names('all')
    for letter in AlphaSequence:
        chain = 'Chain-'+letter
        if chain in objects:
            if(len(cmd.index(chain)) < 1):
                cmd.delete(chain)
    # if 'Chain-' '' in objects:
    #         if(len(cmd.index('Chain-' '')) < 1):
    #             cmd.delete('Chain-' '')
cmd.extend('checkforchain', checkforchain)

def deletemotif():
    cmd.delete('p-loop')
    cmd.delete('serineprotease')
    cmd.delete('lactamase')
    cmd.delete('superoxide')
    cmd.delete('metalloprotease')
    cmd.delete('tyrophos')
    cmd.delete('carbonicanhydrase')
    cmd.delete('paplike')
    cmd.delete('Zinc_finger')
    cmd.delete('Aminotransferase')
    cmd.delete('fucoseisomerase')
    cmd.delete('Ligase')
    cmd.delete('o-glycosyl')
    cmd.delete('glu_amidotransferase')
    cmd.delete('Peroxidase')
    cmd.delete('carboncarbon')
    cmd.delete('Tkinase')
    cmd.delete('TrioseIsomerase')
    cmd.delete('alcoholdehyd')
    cmd.delete('Cis-trans')
    cmd.delete('aldoreductase')
    cmd.delete('NAD-reductase')
    cmd.delete('NAD-reductase2')
    cmd.delete('chondroitinase')
    cmd.delete('Hyaluronate_Lyase')
    cmd.delete('deacetylase')
    cmd.delete('p-loop')
    cmd.delete('adenylatekinase')
    cmd.delete('SRC-Kinase')
    cmd.delete('Cyclin_Kinase')
    cmd.delete('Serotonin_transferase')
    cmd.delete('actase')
    cmd.delete('Exonuclease3')
    cmd.delete('Citrate_Synth')
    cmd.delete('hhal')
    cmd.delete('betaine_dehydrogenase')
cmd.extend('deletemotif', deletemotif)

def deleteEmpty():
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        if(len(cmd.index('ligands')) < 1):
            cmd.delete('ligands')
    if 'nucleic_acid' in objects:
        if(len(cmd.index('nucleic_acid')) < 1):
            cmd.delete('nucleic_acid')
    if 'protein' in objects:
        if(len(cmd.index('protein')) < 1):
            cmd.delete('protein')
    if 'hydrophilic' in objects:
        if(len(cmd.index('hydrophilic')) < 1):
            cmd.delete('hydrophilic')
    if 'hydrophobic' in objects:
        if(len(cmd.index('hydrophobic')) < 1):
            cmd.delete('hydrophobic')
    if 'acidic' in objects:
        if(len(cmd.index('acidic')) < 1):
            cmd.delete('acidic')
    if 'basic' in objects:
        if(len(cmd.index('basic')) < 1):
            cmd.delete('basic')
    if 'heme' in objects:
        if(len(cmd.index('heme')) < 1):
            cmd.delete('heme')
cmd.extend('deleteEmpty', deleteEmpty)

def procolor(selection=None,
        show_selection='sticks',
        color_selection='cpk',
        show_all=('sticks','spheres'),
        color_all='cpk',
        cpknew=False):
    cmd.do('hide everything, all')
    def cpk(cpkkit,selection):
        unk = 'not e. '
        cpk,suffix = cpkkit
        for k in cpk:
            if k != 'UNK':
                cmd.do('color '+k+suffix+',(e. '+k+' & '+selection+')')
                unk += ''+k+'+'
        cmd.do('color UNK'+suffix+',(('+unk[:-1]+') & '+selection+')')
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
            if k+suffix not in colorIndex:
                cmd.do('set_color '+k+suffix+','+cpk[k])
        return cpk,suffix
    def show(selection,toshow,tocolor,cpknew):
        if type(toshow).__name__ == 'tuple':
            for show in toshow:
                cmd.do('show %s, %s'%(show,selection))
        else:
            cmd.do('show %s, %s'%(toshow,selection))
        if tocolor == 'cpk':
            cpk(setcolors(cpknew),selection)
        else:
            cmd.do('color %s, %s'%(tocolor,selection))
    if show_all != None:
        show('all', show_all, color_all, cpknew)
    if selection != None:
        show(selection, show_selection, color_selection, cpknew)
cmd.extend('procolor', procolor)

def populate():
    objects = cmd.get_names('all')
    cmd.select('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.select('nucleic_acid', 'resn a+t+g+c+u')
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
    cmd.disable('nucleic_acid')
    cmd.disable('protein')
    for letter in AlphaSequence:
        cmd.select("Chain-" + letter, "chain " + letter)
    #cmd.select("Chain-' '", "chain ' '")
    checkforchain()
    items = []
    objects = cmd.get_names('all')
    items.append('All')
    items.append('Not Selected')
    if 'protein' in objects:
        items.append('protein')
    if 'nucleic_acid' in objects:
        items.append('nucleic_acid')
    if 'hydrophobic' in objects:
        items.append('hydrophobic')
    if 'hydrophilic' in objects:
        items.append('hydrophilic')
    if 'acidic' in objects:
        items.append('acidic')
    if 'basic' in objects:
        items.append('basic')
    if 'ligands' in objects:
        items.append('ligands')
    if 'heme' in objects:
        items.append('heme')
    for letter in AlphaSequence:
        if 'Chain-' + letter in objects:
            items.append('Chain-' + letter)
    items.sort()
    #selection.setitems(items)
    Tabs['view']['advanced_selection'].setitems(items)
cmd.extend('populate', populate)

def update():
    defaults()
    populate()
    cmd.remove('resn HOH')
    deleteEmpty()
    cmd.orient('all')
cmd.extend('update', update)

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
