'''Sets up global variables and functions'''
from pymol import cmd
import Tkinter as tk
import urllib2
import shelve
import os
import math
import time
import linecache
import random
import platform
VERSION = '4.1rc2'
PLATFORM = platform.system()
PROMOL_DIR_PATH = os.path.dirname(__file__)
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
DIRS = ('Motifs', )
if not os.path.isdir(OFFSITE):
    os.makedirs(OFFSITE)
for DIR in DIRS:
    DIR = os.path.join(OFFSITE, DIR)
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

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

Photos = {}
for x in AminoList:
    x = x.upper()
    for y in ('3D', '2D'):
        Photos["%s%s" % (x, y)] = tk.PhotoImage(
            file = os.path.join(PROMOL_DIR_PATH, 'AminoPics', x+y+'.gif'))
del x, y
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

class PERSISTENT:
    '''Presistent storage'''
    def __init__(self, filename, arg=None, writeback=False, **keywds):
        self.writeback = writeback
        self.dictlen = 'len'.encode("hex")
        self.dictkey = 'key'.encode("hex")
        self.filename = os.path.join(OFFSITE, '%s.db' % filename)
        try:
            self.dict = shelve.open(self.filename)
        except:
            os.remove(self.filename)
            self.dict = shelve.open(self.filename)
        self.dictkeys = []
        if self.dictkey not in self.dict:
            self.dict[self.dictkey] = []
        else:
            self.dictkeys = self.dict[self.dictkey]
        if self.dictlen not in self.dict:
            self.dict[self.dictlen] = 0
        self._update(arg, keywds)

    def clear(self):
        for key in self.dictkeys:
            self.__delitem__(key, False)
        self.dictkeys = []
        self.dict[self.dictkey] = []
        self.dict[self.dictlen] = 0

    def get(self, key, default=None):
        if key in self.dictkeys:
            return self.__getitem__(key)
        else:
            return default

    def setdefault(self, key, default=None):
        if key in self.dictkeys:
            return self.__getitem__(key)
        else:
            self.__setitem__(key, default)
            return default

    def pop(self, key, *args):
        if key in self.dictkeys:
            temp = self.__getitem__(key)
            self.__delitem__(key)
            return temp
        else:
            if len(args) != 0:
                return args[0]
            raise KeyError

    def popitem(self):
        temp = (self.dictkeys[0], self.__getitem__(self.dictkeys[0]))
        self.__delitem__(self.dictkeys[0])
        return temp

    def copy(self):
        return self._temp()

    def keys(self):
        return self.dictkeys

    def iterkeys(self):
        for key in self.dictkeys:
            yield key

    def values(self):
        templist = []
        for key in self.dictkeys:
            templist.append(self.__getitem__(key))
        return templist

    def itervalues(self):
        for key in self.dictkeys:
            yield self.__getitem__(key)

    def items(self):
        templist = []
        for key in self.dictkeys:
            templist.append((key, self.__getitem__(key)))
        return templist

    def iteritems(self):
        for key in self.dictkeys:
            yield (key, self.__getitem__(key))

    def has_key(self, item):
        return self.__contains__(item)

    def switchwriteback(self):
        self._close()
        if self.writeback == False:
            self.writeback == True
            self.dict = shelve.open(self.filename, writeback=True)
        else:
            self.writeback == False
            self.dict = shelve.open(self.filename)

    def sync(self):
        self.dict.sync()

    def _close(self):
        self.dict.close()

    def _merge(self, mapping):
        for key in mapping.keys():
            self.__setitem__(key, mapping[key])

    def _merge_other(self, seq):
        for pair in seq:
            if len(pair) != 2:
                raise ValueError("{0!r} doesn't have a length of 2".format(
                    pair))
            self.__setitem__(pair[0], pair[1])

    def _update(self, arg, keywds):
        if arg:
            if isinstance(arg, type({})):
                self._merge(arg)
            else:
                self._merge_other(arg)
        if keywds:
            self._merge(keywds)

    def update(self, arg=None, **keywds):
        self._update(arg, keywds)

    def _temp(self):
        temp = {}
        for key in self.dictkeys:
            temp[key] = self.__getitem__(key)
        return temp

    def _convert_key(self, key):
        if type(key).__name__ == 'int' or type(key).__name__ == 'long':
            return hex(key)
        if type(key).__name__ == 'float':
            return key.hex()
        return key

    def _unconvert_key(self, key):
        try:
            return int(key, 0)
        except TypeError:
            return float.fromhex(key)
        except ValueError:
            return key

    def __copy__(self):
        return self._temp()

    def __deepcopy__(self):
        return self._temp()

    def __str__(self):
        return str(self._temp())

    def __len__(self):
        return self.dict[self.dictlen]

    def __setitem__(self, key, value):
        if key not in self.dictkeys:
            self.dict[self.dictlen] += 1
            self.dictkeys.append(key)
            self.dict[self.dictkey] = self.dictkeys
        self.dict[self._convert_key(key)] = value

    def __getitem__(self, key):
        if key in [self.dictkey, self.dictlen]:
            raise KeyError
        return self.dict[self._convert_key(key)]

    def __delitem__(self, key, attr=True):
        if key in [self.dictkey, self.dictlen]:
            raise KeyError
        del self.dict[self._convert_key(key)]
        if attr:
            self.dictkeys.remove(key)
            self.dict[self.dictkey] = self.dictkeys
            self.dict[self.dictlen] -= 1

    def __contains__(self, key):
        if key in self.dictkeys:
            return True
        return False

    def __iter__(self):
        for key in self.dictkeys:
            yield key


MOTIFS = PERSISTENT('motifs')
MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs')
USRMOTIFSFOLDER = os.path.join(OFFSITE, 'Motifs')
def motifstore(*args):
    MOTIFS.switchwriteback()#!!DO NOT REMOVE
    if len(MOTIFS) > 0:
        for filecheck in MOTIFS:
            if filecheck == 'errors':
                continue
            if not os.path.isfile(MOTIFS[filecheck]['path']):
                del MOTIFS[filecheck]

    find = ('FUNC', 'PDB', 'EC', 'RESI', 'LOCI')
    MOTIFS['errors'] = []
    for motdir in args:
        motfiles = os.listdir(motdir)
        for motfile in motfiles:
            found = []
            func = motfile[0:-3]
            if func not in MOTIFS or 'mtime' not in MOTIFS[func]:
                MOTIFS[func] = {}
                MOTIFS[func]['mtime'] = None
            MOTIFS[func]['path'] = os.path.join(motdir, motfile)
            if MOTIFS[func]['mtime'] == os.path.getmtime(MOTIFS[func]['path']):
                continue
            MOTIFS[func]['mtime'] = os.path.getmtime(MOTIFS[func]['path'])
            tmpf = open(MOTIFS[func]['path'], 'rbU')
            i = 0
            for line in tmpf:
                if line[0:3] == "'''":
                    i += 1
                    continue
                if i == 1:
                    if line[0:4] == 'FUNC':
                        if 'FUNC' in found:
                            MOTIFS['errors'].append('Warning: Motif `%s` included an extra `FUNC` attribute, which was ignored.'%(MOTIFS[func]['path']))
                            MOTIFS[func]['mtime'] = 0
                            continue
                        found.append('FUNC')
                        funccheck = line.split(':')[1][0:-1]
                        if func != funccheck:
                            MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `FUNC` attribute.'%(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            tmpf.close()
                            break
                        continue
                    if line[0:3] == 'PDB':
                        if 'PDB' in found:
                            MOTIFS['errors'].append('Warning: Motif `%s` included an extra `PDB` attribute, which was ignored.'%(MOTIFS[func]['path']))
                            MOTIFS[func]['mtime'] = 0
                            continue
                        found.append('PDB')
                        pdbcheck = line.split(':')[1][0:-1].lower()
                        if func.split('_')[1].lower() != pdbcheck:
                            MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `PDB` attribute.'%(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            tmpf.close()
                            break
                        MOTIFS[func]['pdb'] = pdbcheck
                        continue
                    if line[0:2] == 'EC':
                        if 'EC' in found:
                            MOTIFS['errors'].append('Warning: Motif `%s` included an extra `EC` attribute, which was ignored.'%(MOTIFS[func]['path']))
                            MOTIFS[func]['mtime'] = 0
                            continue
                        found.append('EC')
                        preec = func.split('_')
                        ec = '.'.join((preec[2], preec[3], preec[4], preec[5]))
                        eccheck = line.split(':')[1][0:-1]
                        if ec != eccheck:
                            MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `EC` attribute.'%(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            tmpf.close()
                            break
                        MOTIFS[func]['ec'] = eccheck
                        continue
                    if line[0:4] == 'RESI':
                        if 'RESI' in found:
                            MOTIFS['errors'].append('Warning: Motif `%s` included an extra `RESI` attribute, which was ignored.'%(MOTIFS[func]['path']))
                            MOTIFS[func]['mtime'] = 0
                            continue
                        found.append('RESI')
                        resi = line.split(':')[1][0:-1].lower()
                        if resi == '':
                            MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `RESI` attribute.'%(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            tmpf.close()
                            break
                        MOTIFS[func]['resi'] = resi.split(',')
                        continue
                    if line[0:4] == 'LOCI':
                        if 'LOCI' in found:
                            MOTIFS['errors'].append('Warning: Motif `%s` included an extra `LOCI` attribute, which was ignored.'%(MOTIFS[func]['path']))
                            MOTIFS[func]['mtime'] = 0
                            continue
                        found.append('LOCI')
                        loci = line.split(':')[1][0:-1].split(';')
                        if len(loci) == 1:
                            MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to an incorrect `LOCI` attribute.'%(MOTIFS[func]['path']))
                            del MOTIFS[func]
                            tmpf.close()
                            break
                        selection = ''
                        for loc in loci:
                            if loc == '':
                                continue
                            chain, numbers = loc.split('-')
                            nums = 'resi %s' % ' or resi '.join(numbers.split(','))
                            if selection == '':
                                selection = '(chain %s and (%s))' % (chain, nums)
                            else:
                                selection = '%s or (chain %s and (%s))' % (selection, chain, nums)
                        MOTIFS[func]['loci'] = selection
                        continue
                if line[0:3] != 'cmd' and line != '':
                    MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to potential mallicious code.'%(MOTIFS[func]['path']))
                    del MOTIFS[func]
                    tmpf.close()
                    break
            if func in MOTIFS and len(find) != len(found):
                MOTIFS['errors'].append('Error: Motif `%s` could not be loaded due to missing required attributes.'%(MOTIFS[func]['path']))
                del MOTIFS[func]
            tmpf.close()
    MOTIFS.switchwriteback()#!!DO NOT REMOVE
motifstore(MOTIFSFOLDER, USRMOTIFSFOLDER)

def reset_motif_database():
    global MOTIFS
    MOTIFS.clear()
    del MOTIFS
    MOTIFS = PERSISTENT('motifs')
    motifstore(MOTIFSFOLDER, USRMOTIFSFOLDER)
cmd.extend('reset_motif_database', reset_motif_database)

PDBENTRIES = PERSISTENT('pdbentries')
def pdbstore():
    if 'pdbentries' not in PDBENTRIES or 'expire' not in PDBENTRIES:
        PDBENTRIES['pdbentries'] = {}
        PDBENTRIES['expire'] = time.time()-864001
        oldfile = os.path.join(OFFSITE, 'pdb_entry_type.txt')
        if os.path.exists(oldfile):
            os.remove(oldfile)
    if (PDBENTRIES['expire']+864000) <= time.time():
        PDBENTRIES['expire'] = time.time()
        PDBENTRIES.switchwriteback()
        pdbliness = urllib2.urlopen('ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt')
        for pdbline in pdbliness:
            pdb = pdbline.split('	')[0]
            if pdb in PDBENTRIES['pdbentries']:
                continue
            PDBENTRIES['pdbentries'][pdb] = None
        pdbliness.close()
        PDBENTRIES.switchwriteback()
pdbstore()

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
        #this avoids the syntax error in 2.6 and above
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
    cmd.reinitialize()
    pdbCode = random.choice(PDBENTRIES['pdbentries'].keys())
    fetch(pdbCode)
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

# Copyright Notice
# ================
# 
# The PyMOL Plugin source code [below this point] is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
# 
# ----------------------------------------------------------------------
# This PyMOL Plugin is Copyright (C) 2004 by Charles Moad <cmoad@indiana.edu>
# 
#                        All Rights Reserved
# 
# Permission to use, copy, modify, distribute, and distribute modified
# versions of this software and its documentation for any purpose and
# without fee is hereby granted, provided that the above copyright
# notice appear in all copies and that both the copyright notice and
# this permission notice appear in supporting documentation, and that
# the name(s) of the author(s) not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
# 
# THE AUTHOR(S) DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.  IN
# NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------

import tkSimpleDialog
import tkMessageBox
import sys, zlib

def fetch(pdbCode,passerrors=False):
    try:
        if len(pdbCode) > 4:
            raise SyntaxError
        url = pdbCode.join(('http://www.rcsb.org/pdb/cgi/export.cgi/',
            '.pdb.gz?format=PDB&pdbId=','&compression=gz'))
        pdbUrl = urllib2.urlopen(url)
        pdbFile = pdbUrl.read()
        pdbUrl.close()
        if pdbFile.find('.ent',0,30) == 17:
            cutsite = 22
        else:
            cutsite = 10
        cmd.read_pdbstr(zlib.decompress(pdbFile[cutsite:], -zlib.MAX_WBITS),
            pdbCode)
        return ''
    except zlib.error:
        url = pdbCode.join(('http://www.rcsb.org/pdb/cgi/export.cgi/',
            '.pdb?format=PDB&pdbId=',''))
        pdbUrl = urllib2.urlopen(url)
        cmd.read_pdbstr(pdbUrl.read(), pdbCode)
        pdbUrl.close()
    except (urllib2.HTTPError,SyntaxError):
        if passerrors == False:
            tkMessageBox.showerror('Invalid Code',
                'You entered an invalid pdb code: %s'%(pdbCode))
        else:
            return 'You entered an invalid pdb code: %s'%(pdbCode)
    except urllib2.URLError:
        if passerrors == False:
            tkMessageBox.showerror('Connection Error',
                'Please check your internet connection.\n')
        else:
            return 'Please check your internet connection.'
    #except:
        #print "Unexpected error:", sys.exc_info()[0]

def PDBDialog(app):
    pdbCode = tkSimpleDialog.askstring('PDB Loader Service',
        'Please enter a 4-digit pdb code:',parent=app.root)
    if pdbCode:
        fetch(pdbCode)
#cmd.extend('fetch', fetch)

