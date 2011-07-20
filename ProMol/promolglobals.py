'''Sets up global variables and functions'''
from pymol import cmd
import Tkinter as tk
import urllib2
import os
import math
import time
import linecache
import random
import platform
from Tkinter import *

VERSION = '4.2 Release Candidate 2'
ALG_VERSION = '1.0' #added by Alex
PLATFORM = platform.system()
PROMOL_DIR_PATH = os.path.dirname(__file__)
MASTERFILE_URL = 'ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt' # For random PDB selection
MOTIFS = {} # Empty dictionary to replace shelve-based database
searchSet = [] # Replaces MOTIFS' keysUsed, actually a list

try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
if PLATFORM == 'Windows':
    OFFSITE = os.path.join(os.environ['AppData'], 'SBEVSL', 'ProMol')
elif PLATFORM == 'Darwin':
    OFFSITE = os.path.join(HOME, 'Library', 'Application Support', 'SBEVSL',
        'ProMol')
else:
    OFFSITE = os.path.join(HOME, '.sbevsl', 'ProMol')
PDBFOLDER = 'PDBDownloads'
DIRS = ('UserMotifs', PDBFOLDER)#changed folder name to UserMotifs for clarity
if not os.path.isdir(OFFSITE):
    os.makedirs(OFFSITE)
for DIR in DIRS:
    DIR = os.path.join(OFFSITE, DIR)
    if not os.path.isdir(DIR):
        os.mkdir(DIR)
FETCH_PATH = os.path.join(OFFSITE, PDBFOLDER)
class PROMOLGUI:pass
GUI = PROMOLGUI()
SELE = 'All'
NEWCOLOR = 0
def incnewcolor():
    tmp = NEWCOLOR
    NEWCOLOR += 1
    return tmp

AminoMenuList = ('', 'ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly',
    'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr',
    'val')
#Amino Acid Lists
AminoLongList = ('alanine', 'arginine', 'asparagine', 'aspartate', 'cysteine',
    'glutamine', 'glutamate', 'glycine', 'histidine', 'isoleucine', 'leucine',
    'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine',
    'tryptophan', 'tyrosine', 'valine')
AminoList = ('ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his',
    'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val')
AminoShortList = ('a', 'r', 'n', 'd', 'c', 'q', 'e', 'g', 'h', 'i', 'l', 'k',
    'm', 'f', 'p', 's', 't', 'w', 'y', 'v')
AminoSubsList = {
        3:'glu',
        6:'asp',
        5:'asn',
        2:'gln',
        15:'thr',
        16:'ser'
    }
AminoNumberList = (5, 11, 8, 8, 6, 9, 9, 4, 10, 8, 8, 9, 8, 11, 7, 6, 7, 14, 12,
    7)

AminoLongHashTable = {}
AminoHashTable = {}
AminoShortHashTable = {}
for i in range(0, 20):
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
del i

#/*=====================*//*==========================================*/
#/*   DNA Nucleotides   *//*  DNA Nucleotides PDB Revision, Jul 2007  */
#/*=====================*//*==========================================*/
DNA = ("A", "C", "G", "T", "DA", "DC", "DG", "DT", "DI")
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
del x
#a - z
alphasequence = [ "%c" % (x) for x in range(ord('a'), ord('z')+1)]
del x
#the original CPK plastic models developed by Corey, Pauling and Kultun
CPKDict = {
      "H":"[1.000, 1.000, 1.000]", "He":"[1.000, 0.753, .796]",
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
      "H":"[1.000, 1.000, 1.000]", "He":"[1.000, 0.753, .796]",
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

# Deleted persistent database class

MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs')
USRMOTIFSFOLDER = os.path.join(OFFSITE, 'UserMotifs')

def loadMotifs(*folders):
    find = ('FUNC', 'PDB', 'EC', 'RESI', 'LOCI')
    MOTIFS['errors'] = []
    for motdir in folders:
        motfiles = os.listdir(motdir)
        for motfile in motfiles:
            if not motfile.endswith('.py'):
                MOTIFS['errors'].append('Error: Encountered unexpected filename extension with motif {0} in {1}; skipping file.'.format(motfile, motdir))
                continue
            found = []
            func = motfile[0:-3]
            if func not in MOTIFS:
                MOTIFS[func] = {}
            MOTIFS[func]['path'] = os.path.join(motdir, motfile)
            with open(MOTIFS[func]['path'], 'rbU') as motifFile:
                i = 0
                for line in motifFile:
                    if line[0:3] == "'''":
                        i += 1
                        continue
                    if i == 1:
                        if len(line.split(':')) < 2:
                            MOTIFS['errors'].append('Error: Motif `{0}` was missing a colon in one of its header lines.'.format(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            break
                        if line[0:4] == 'FUNC':
                            if 'FUNC' in found:
                                MOTIFS['errors'].append('Warning: Motif `%s` included an extra `FUNC` attribute, which was ignored.'%(MOTIFS[func]['path']))
                                continue
                            found.append('FUNC')
                            funccheck = line.split(':')[1][0:-1]
                            if func != funccheck:
                                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `FUNC` attribute.'%(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # Unnecessary to close the file using with
                                break
                            continue
                        if line[0:3] == 'PDB':
                            if 'PDB' in found:
                                MOTIFS['errors'].append('Warning: Motif `%s` included an extra `PDB` attribute, which was ignored.'%(MOTIFS[func]['path']))
                                continue
                            found.append('PDB')
                            pdbcheck = line.split(':')[1][0:-1].lower()
                            if func.split('_')[1].lower() != pdbcheck:
                                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `PDB` attribute.'%(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # Not necessary to close file using with
                                break
                            MOTIFS[func]['pdb'] = pdbcheck
                            continue
                        if line[0:2] == 'EC':
                            if 'EC' in found:
                                MOTIFS['errors'].append('Warning: Motif `%s` included an extra `EC` attribute, which was ignored.'%(MOTIFS[func]['path']))
                                continue
                            found.append('EC')
                            preec = func.split('_')
                            if len(preec) < 6:
                                MOTIFS['errors'].append('Error: Motif {0} did not have enough components in its EC number.'.format(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # No need to close
                                break
                            ec = '.'.join((preec[2], preec[3], preec[4], preec[5]))
                            eccheck = line.split(':')[1][0:-1]
                            if ec != eccheck:
                                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `EC` attribute.'%(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # No need to close
                                break
                            MOTIFS[func]['ec'] = eccheck
                            continue
                        if line[0:4] == 'RESI':
                            if 'RESI' in found:
                                MOTIFS['errors'].append('Warning: Motif `%s` included an extra `RESI` attribute, which was ignored.'%(MOTIFS[func]['path']))
                                continue
                            found.append('RESI')
                            resi = line.split(':')[1][0:-1].lower()
                            if resi == '':
                                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `RESI` attribute.'%(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # No need to close
                                break
                            MOTIFS[func]['resi'] = resi.split(',')
                            continue
                        if line[0:4] == 'LOCI':
                            if 'LOCI' in found:
                                MOTIFS['errors'].append('Warning: Motif `%s` included an extra `LOCI` attribute, which was ignored.'%(MOTIFS[func]['path']))
                                continue
                            found.append('LOCI')
                            loci = line.split(':')[1][0:-1].split(';')
                            if len(loci) == 1: # Highly suspect equality check
                                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `LOCI` attribute.'%(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                # No need to close
                                break
                            selection = ''
                            # Added by Cyprian Corwin to prevent crash on bad loci (it happened to us)
                            badLoci = False # Needed to break out twice
                            for loc in loci:
                                if loc == '':
                                    continue
                                splitlist = loc.split('-')
                                if len(splitlist) == 2:
                                    chain, numbers = splitlist
                                else:
                                    badLoci = True
                                    break
                                nums = 'resi %s' % ' or resi '.join(numbers.split(','))
                                if selection == '':
                                    selection = '(chain %s and (%s))' % (chain, nums)
                                else:
                                    selection = '%s or (chain %s and (%s))' % (selection, chain, nums)
                            if badLoci:
                                MOTIFS['errors'].append('Error: Motif `{0}` could not be loaded due to an incorrect `LOCI` attribute.'.format(MOTIFS[func]['path']))
                                del MOTIFS[func]
                                break
                            MOTIFS[func]['loci'] = selection
                            continue
                    if line[0:4] != 'cmd.' and line != '':
                        MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to potential malicious code.'%(MOTIFS[func]['path']))
                        del MOTIFS[func]
                        # Unnecessary to close
                        break
                if func in MOTIFS and len(find) != len(found):
                    MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to missing required attributes.'%(MOTIFS[func]['path']))
                    del MOTIFS[func]
                # End with
    # I removed the following even though it said not to:
    # MOTIFS.switchwriteback() # DO NOT UNREMOVE!!
    # Switchwriteback was written incorrectly anyway (with == instead of = (x2))
    # Check the API for shelve.open and see what the writeback argument
    # does.  I think it is not what the author of switchwriteback() thought.
    # Refreshing at runtime will be better than using shelve for now. -Kip

loadMotifs(MOTIFSFOLDER, USRMOTIFSFOLDER) #add all folders here

def reset_motif_database():
    global MOTIFS
    MOTIFS.clear() # This should still work because dictionaries have such a method
    del MOTIFS
    MOTIFS = {}
    loadMotifs(MOTIFSFOLDER, USRMOTIFSFOLDER)
cmd.extend('reset_motif_database', reset_motif_database)

def pathmaker(*args, **options):
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
        cmd.cartoon('automatic', glb.SELE)
        GUI.view['toonWidth'].set('1.4')
        GUI.view['toonThickness'].set('0.3')
        GUI.view['cartoonTransparency'].set('0.0')
        GUI.view['toonTubeRadius'].set('0.5')
        GUI.view['ribbonTypes'].invoke(0)
    elif tag == 'spheres':
        cmd.set('sphere_scale', '0.7', 'all')
        cmd.set('sphere_transparency', '0.0', 'all')
        GUI.view['sphereScale'].set('0.7')
        GUI.view['sphereTransparency'].set('0.0')
    elif tag == 'sticks':
        cmd.set('stick_radius', '0.2', 'all')
        cmd.set('stick_transparency', '0.0', 'all')
        GUI.view['stickRadius'].set('0.2')
        GUI.view['stickTransparency'].set('0.0')
    elif tag == 'surface':
        cmd.set('transparency', '0.0', 'all')
        GUI.view['surfaceTransparency'].set('0.0')
    elif tag == 'ambient':
        cmd.set('ambient', '0.25', 'all')
        GUI.view['asca'].set('0.25')
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
    for motif in MOTIFS:
        cmd.delete('%s'%(motif))
cmd.extend('deletemotif', deletemotif)

def show_as(show, selection):
    '''`as` is a reserved word as of python 2.6
    pymol used cmd.as before this and
    had to change to cmd.show_as'''
    try:
        cmd.show_as(show, selection)
    except AttributeError:
        getattr(cmd, 'as')(show, selection)

def procolor(selection=None, show_selection='sticks', color_selection='cpk',
        show_all=('sticks', 'spheres'), color_all='cpk', cpknew=False):
    '''Color in CPK or CPKnew
    Needs the CPK DICTs defined above.'''
    def cpk(cpknew, selection):
        colorIndex = {}
        for i in cmd.get_color_indices():
            k, v = i
            colorIndex[k] = v
        if cpknew:
            cpk = CPKNewDict
            suffix = 'cpknew'
        else:
            cpk = CPKDict
            suffix = 'cpk'
        for k in cpk:
            color = '%s%s' % (k, suffix)
            if color not in colorIndex:
                cmd.set_color(color, cpk[k])
        unk = 'not e. '
        for k in cpk:
            if k != 'UNK':
                cmd.color('%s%s' % (k, suffix), 'e. %s & (%s)'%(k, selection))
                unk = '%s%s+' % (unk, k)
        cmd.color('UNK%s'%(suffix), '(%s) & (%s)' % (unk[:-1], selection))
    def show(selection, toshow, tocolor, cpknew):
        if type(toshow).__name__ == 'tuple':
            for show in toshow:
                cmd.show('%s' % (show), '%s' % (selection))
        else:
            cmd.show('%s' % (toshow), '%s' % (selection))
        if tocolor == 'cpk':
            cpk(cpknew, selection)
        else:
            cmd.color('%s' % (tocolor), '%s' % (selection))
    if show_all != None:
        cmd.hide('everything', 'all')
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
    for letter in cmd.get_chains():
        chain = 'Chain-%s'%(letter)
        cmd.select(chain, "chain %s"%(letter))
        cmd.disable(chain)
    objects = cmd.get_names('all')
    for obj in objects:
        try:
            if(len(cmd.index(obj)) < 1):
                cmd.delete(obj)
        except:
            cmd.delete(obj)
    objects = cmd.get_names('all')
    items = ['All', ]
    for obj in objects:
        items.append(obj)
        if obj in ['protein', 'dna', 'rna']:
            items.append('not %s' % obj)
    try:
        GUI.ez_viz['selection_menu']['menu'].delete(0, tk.END)
        GUI.view['advanced_selection_menu']['menu'].delete(0, tk.END)
        for item in items:
            GUI.ez_viz['selection_menu']['menu'].add_command(label=item,
                command=tk._setit(GUI.ez_viz['selection'], item, set_selection))
            GUI.view['advanced_selection_menu']['menu'].add_command(label=item,
                command=tk._setit(GUI.view['advanced_selection'], item, 
                    set_selection))
    except AttributeError:
        pass
cmd.extend('populate', populate)

def update():
    defaults()
    populate()
    cmd.orient('all')
cmd.extend('update', update)

def randompdb():
    # Adapted from pdbstore function (removed)
    cmd.reinitialize()
    database = []
    masterfile = None
    try:
        masterfile = urllib2.urlopen(MASTERFILE_URL)
        for pdbline in masterfile:
            database.append(pdbline.split('\t')[0])
    finally:
        if (masterfile):
            masterfile.close()
    if (len(database) > 0):
        cmd.fetch(random.choice(database), async=0, path=FETCH_PATH)
        update()
cmd.extend('randompdb',randompdb)

def set_selection(tag='all'):
    global SELE
    GUI.ez_viz['selection'].set(tag)
    GUI.view['advanced_selection'].set(tag)
    SELE = tag
           
class ProgressBar:
    def __init__(self, Parent, Height=10, Width=100, Row=0, Column=0, Span=1,
                 ForegroundColor="black", BackgroundColor=None):
        self.Height=Height
        self.Width=Width
        self.BarCanvas = tk.Canvas(Parent,
            width=Width, height=Height,
            background=BackgroundColor, borderwidth=1,
            relief=tk.SUNKEN)
        self.BarCanvas.grid(row=Row, column=Column, columnspan=Span, padx=5,
            pady=2)
        self.RectangleID=self.BarCanvas.create_rectangle(0, 0, 0, Height,
            fill=ForegroundColor)
    def SetProgressPercent(self, NewLevel):
        self.BarCanvas.coords(self.RectangleID, 0, 0,
            (max(0, min(100, math.floor(NewLevel)))/100.0)*self.Width,
            self.Height)
