'''Sets up global variables and functions'''
#from pymol import cmd
import Tkinter as tk
import urllib2
import os
import time
import random
import platform
from ProMol.version import VERSION, ALG_VERSION, USE_JESS
# The algorithm version number constant was still at 1.0, so
# I believe it would be more meaningful to report the version of ProMOL
# in the CSV file, rather than a separately tracked and difficult-to-
# maintain algorithm version.  If anything else were to be included,
# I would suggest a motif library version number.  -Kip

PLATFORM = platform.system()
PROMOL_DIR_PATH = os.path.dirname(__file__)
MASTERFILE_URL = 'ftp://ftp.wwpdb.org/pub/pdb/derived_data/pdb_entry_type.txt' # For random PDB selection
MOTIFS = {} # Empty dictionary to replace shelve-based database
# searchSet was unnecessary and has been removed
# hidmotif used to be a list box containing the query PDB associated with a result
# Now I am using a list of tuples containing the PDB entry and the result
# and calling it matchpairs: format is (query, result) for results and (query, query)
# for headers
matchpairs = []

LAST_USED_DIR = os.path.expanduser('~/') # needed to load locally stored files
root = tk.Tk() # sets up root for IntVar()
using_db = False
full_run = tk.IntVar()

# Determine the location of the user data directory
# We create the following folder structure underneath
# the BASIL user data directory (which is also created if it does
# not exist):
# .../ProMol/CSV (for automatically generated CSV files, not usually
#                 exported ones)
# .../ProMol/PDBDownloads (we pass this to calls to fetch() so it caches PDB files
#                          here and not in root of the user's home directory)
# .../ProMol/UserMotifs (motifs that are saved from the Motif Maker are placed here,
#                        not always so with exported ones)
try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
if PLATFORM == 'Windows':
    OFFSITE = os.path.join(HOME, 'Documents', 'BASIL', 'ProMol')
elif PLATFORM == 'Darwin':
    OFFSITE = os.path.join(HOME, 'Library', 'Application Support', 'BASIL',
        'ProMol')
else:
    OFFSITE = os.path.join(HOME, '.basil', 'ProMol')
PDBFOLDER = 'PDBDownloads'
CSVFOLDER = 'CSV'
RESULTFOLDER = 'Results'
DIRS = ('UserMotifs', PDBFOLDER, CSVFOLDER,RESULTFOLDER)#changed folder name to UserMotifs for clarity
if not os.path.isdir(OFFSITE):
    os.makedirs(OFFSITE)
for DIR in DIRS:
    DIR = os.path.join(OFFSITE, DIR)
    if not os.path.isdir(DIR):
        os.mkdir(DIR)
FETCH_PATH = os.path.join(OFFSITE, PDBFOLDER)
CSV_PATH = os.path.join(OFFSITE, CSVFOLDER)
RESULTFOLDER = os.path.join(OFFSITE, RESULTFOLDER)

#has to import this after FETCH_PATH is initializes as promolobjects uses that
from ProMol.promolobjects import Protein

# This acts as a place to stash the kitchen sink as fields added later
class PROMOLGUI:
    pass
    
GUI = PROMOLGUI()
SELE = 'All'

# Pick up the PROMOL_JESS environment variable

GUI.jess={}
if 'PROMOL_JESS' in os.environ:
    USE_JESS=True
else:
    USE_JESS=False

# I think this keeps track of the colors in the custom color chooser in EZ-Viz
NEWCOLOR = 0
def incnewcolor():
    global NEWCOLOR
    tmp = NEWCOLOR
    NEWCOLOR += 1
    return tmp

AminoMenuList = ('', 'ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly',
    'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr',
    'val')

# The amino hash table that is created by this code acts as a way to put any
# representation of an amino acid in and get any representation out.
# The resulting dictionary contains the following keys:
# - Lowercase full amino acid names
# - Three letter abbreviations
# - One letter abbreviations
# Accessing AminoHashTable[x] where x is any of these will return another
# dictionary, which contains the following keys:
# - 'l' (for 'long'): maps to the amino acid's full name
# - The number 3: maps to the amino acid's three letter abbreviation
# - The number 1: maps to the amino acid's one letter abbreviation
# - The number 0: maps to the amino acid's entry in AminoNumberList
#                 (more documentation on that coming soon)
# - If the amino acid can be considered functionally similar to another,
#   the other amino acid's three letter abbreviation can be accessed via
#   the key 's'.

#Amino Acid Lists
AminoLongList = ('alanine', 'arginine', 'asparagine', 'aspartate', 'cysteine',
    'glutamine', 'glutamate', 'glycine', 'histidine', 'isoleucine', 'leucine',
    'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine',
    'tryptophan', 'tyrosine', 'valine', 'calcium', 'molybdenum',
    'molybdenum4', 'magnesium', 'zinc', 'manganese', 'sodium',
    'hemes','b12','cub','fes','hea','mos','cua','fco','sf4','f3s','fe2','cfm',
    'clf','hec','cob','c2o','pcd','4mo', 'f43', '3co', 'cobalt', 'nickle', 'iron', 'copper','copper1','copper2')
AminoList = ('ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his',
    'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val', 
    'ca', 'mo', '4mo', 'mg', 'zn', 'mn', 'na', 'hem','b12','cub','fes','mos',
    'hea','cua','fco','sf4','f3s','fe2','cfm','clf','hec','cob','c2o','pcd','4mo','f43','3co',
    'co', 'ni', 'fe', 'cu','cu1','cu2')
AminoShortList = ('a', 'r', 'n', 'd', 'c', 'q', 'e', 'g', 'h', 'i', 'l', 'k',
    'm', 'f', 'p', 's', 't', 'w', 'y', 'v', 'ca', 'mo', '4mo', 
    'mg', 'zn', 'mn', 'na', 'hem','b12','cub','fes','mos','hea','cua','fco',
    'sf4','f3s','fe2','cfm','clf','hec','cob','c2o','pcd','4mo','f43','3co', 'co', 'ni', 'fe', 'cu','cu1','cu2')
AminoSubsList = {
        3:'glu',
        6:'asp',
        5:'asn',
        2:'gln',
        15:'thr',
        16:'ser'
    }
AminoNumberList = (5, 11, 8, 8, 6, 9, 9, 4, 10, 8, 8, 9, 8, 11, 7, 6, 7, 14, 12,
    7, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51)

AminoHashTable = {}
for i in range(0, 53):
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

# DNASTR and RNASTR are used in populate()
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
# The following dictionaries map atomic symbols to RGB color values
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
# MOTIFSFOLDER is the location of the built-in motifs
# USRMOTIFSFOLDER is the location of user-generated motifs
# MOTIFSAFOLDER is the location of MRB's 37K motifs
# OLDMOTIFDIR is the location of the old style motifs after they have been created
# ALLMOTIFFOLDERS is the list of all the motif folders, add to here any more folders created

MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs')
USRMOTIFSFOLDER = os.path.join(OFFSITE, 'UserMotifs')
MOTIFSAFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs_A')
OLDMOTIFDIR = os.path.join(PROMOL_DIR_PATH,'Old_Motifs')
ALLMOTIFFOLDERS = []
for fldr in [MOTIFSFOLDER,USRMOTIFSFOLDER,MOTIFSAFOLDER]:
    if os.path.exists(fldr):
        ALLMOTIFFOLDERS.append(fldr)

# This function reads motif files from the specified folder(s),
# performs some rudimentary validation (mostly on their headers),
# and adds information about them (including
# header fields and file system location) to the MOTIFS dictionary.

def loadMotifs(folders):
    # This contains the error list.  It used to be inside the motif dictionary.
    global motifErrors
    motifErrors = []
    for motdir in folders:
        # Get the file list in each specified folder
        motfiles = os.listdir(motdir)
        for motfile in motfiles:
            # So it doesn't report an error based on the indexing files
            if motfile=='ecindexing.txt' or motfile=='pfamindexing.txt':
                continue
            # If a file has an unexpected extension, reject it
            # Currently, the motifs are PDB files (but that may
            # change)
            if not motfile.endswith('.pdb'):
                #motifErrors.append('Error: Encountered unexpected filename extension with motif {0} in {1}; skipping file.'.format(motfile, motdir))
                motifErrors.append('Error: Encountered unexpected filename extension with motif %s in %s; skipping file.'%(motfile, motdir))
                continue
            # Strip the '.pdb' extension off the filename to get the motif's name
            func = motfile[0:-4]
            # The following lines check to see if an entry for this motif already exists in the dictionary.
            # If not, it creates one.  This is probably a remnant of the code designed to work with
            # the persistent motif database, which might already contain things from previous
            # program runs before we load any motifs.  That is gone now, and motif information
            # is loaded at every startup.
            # This should probably be changed to REJECT duplicate motifs with the same name
            # rather than overwriting their attributes in the dictionary one by one as this appears
            # to allow doing.  This could occur if two folders were passed into loadMotifs()
            # (either at the same time or in separate calls) which each contained a file with
            # the same name.
            if func not in MOTIFS:
                MOTIFS[func] = None
            MOTIFS[func] = Protein()
            MOTIFS[func].readMotifFile(os.path.join(motdir, motfile))
            
    # I removed the following even though it said not to:
    # MOTIFS.switchwriteback() # DO NOT UNREMOVE!!
    # Switchwriteback was written incorrectly anyway (with == instead of = (x2))
    # Check the API for shelve.open and see what the writeback argument
    # does.  I think it is not what the author of switchwriteback() thought.
    # Refreshing at runtime will be better than using shelve for now. -Kip
    # MOTIFS is no longer a shelf-based database class but a simple dictionary.

# This will run immediately when promolglobals gets imported.
loadMotifs(ALLMOTIFFOLDERS)

# Check if the indexing files are the most recently modified files in the
# respective motif folders, and if not, make new indexing files
def makeIndexFiles(folders):
    for folder in folders:
        if not os.path.exists(os.path.join(folder,'ecindexing.txt'))                                 \
           or not os.path.exists(os.path.join(folder,'pfamindexing.txt'))                            \
           or os.path.getmtime(folder)>os.path.getmtime(os.path.join(folder,'ecindexing.txt'))    \
           or os.path.getmtime(folder)>os.path.getmtime(os.path.join(folder,'pfamindexing.txt')):
            #create file dictionary
            ecdict = dict()
            pfamdict = dict()

            for fl in os.listdir(folder):
                fl = fl.rsplit('.',1)[0]
                if len(fl.split('_'))>1:
                    ec = fl.split('_')[0]
                    if ec not in ecdict.keys():
                        ecdict[ec] = set()
                    ecdict[ec].add(fl)
                    pfam = fl.split('_')[1]
                    if pfam not in pfamdict.keys():
                        pfamdict[pfam] = set()
                    pfamdict[pfam].add(fl)

            #make index files
            ecindfl = open(os.path.join(folder,'ecindexing.txt'),'w+')
            for ec in ecdict:
                ecnums = ec.split('.')
                for num in ecnums:
                    ecindfl.write(num + '\t')
                ecindfl.write(','.join(ecdict[ec]) + '\n')
            ecindfl.close()

            pfamindfl = open(os.path.join(folder,'pfamindexing.txt'),'w+')
            for pfam in pfamdict:
                pfamindfl.write(pfam + '\t' + ','.join(pfamdict[pfam]) + '\n')
            pfamindfl.close()

# Makes ec and pfam dictionaries based on the index file in motif folders
def makeIndexDicts(folders):
    global ECDICT
    ECDICT = dict()
    global PFAMDICT
    PFAMDICT = dict()
    for folder in folders:
        ecindex = open(os.path.join(folder,'ecindexing.txt'),'r')
        pfamindex = open(os.path.join(folder,'pfamindexing.txt'),'r')
        for ln in ecindex.readlines():
            spltln = ln.strip().split('\t')
            if spltln[0]=='N/A':
                ECDICT[spltln[0]] = set(spltln[1].split(','))
                continue
            if spltln[0] not in ECDICT.keys():
                ECDICT[spltln[0]] = dict()
            if spltln[1] not in ECDICT[spltln[0]].keys():
                ECDICT[spltln[0]][spltln[1]] = dict()
            if spltln[2] not in ECDICT[spltln[0]][spltln[1]].keys():
                ECDICT[spltln[0]][spltln[1]][spltln[2]] = dict()
            if spltln[3] not in ECDICT[spltln[0]][spltln[1]][spltln[2]].keys():
                ECDICT[spltln[0]][spltln[1]][spltln[2]][spltln[3]] = set(spltln[4].split(','))
            #ECDICT[spltln[0]][spltln[1]][spltln[2]][spltln[3]].add(spltln[4].split(','))
        for ln in pfamindex.readlines():
            spltln = ln.strip().split('\t')
            PFAMDICT[spltln[0]] = set(spltln[1].split(','))

makeIndexFiles(ALLMOTIFFOLDERS)
makeIndexDicts(ALLMOTIFFOLDERS)

# This clears out loaded motif information and reloads built-in and user motifs.
# This function is not called from within ProMOL currently, but can be called
# by the user by typing "reset_motif_database" at the PyMOL command line.
def reset_motif_database():
    global MOTIFS
    MOTIFS.clear() # This should still work because dictionaries have such a method
    del MOTIFS
    MOTIFS = {}
    loadMotifs(ALLMOTIFFOLDERS)
#Not necessary with no reliance on pymol
#cmd.extend('reset_motif_database', reset_motif_database)

# This is a convoluted way of making a pathname.  It is only called from the
# motif maker (albeit 4 times) and should be replaced with simple concatenation
# for adding file extensions and calls to os.path.join()
def pathmaker(*args, **options):
    newargs = [PROMOL_DIR_PATH]
    if 'root' in options:
        newargs = [options['root']]
    for x in args:
        if type(x).__name__ == 'tuple':
            x = ''.join(x)
        newargs.append(x)
    return os.sep.join(newargs)

# This is called with no arguments from update() and is also executed when
# the user selects from the Reset menu on the View Options tab (it is passed
# in as the constructor to that option menu).  It should be noted that calls
# to update() will not currently reset any of the things that can be reset
# from within that option menu.  If this is a mistake, then to fix it,
# each branch of the if would have to be changed from 'if tag == X' to
# something like 'if (tag == X) or (len(tag) == 0)'.
# This function can also be called by the user at the PyMOL command line.
# This is unnecessary when not using PyMOL
##def defaults(tag = ''):
##    if tag == 'cartoon':
##        cmd.set('cartoon_rect_length', '1.4', 'all')
##        cmd.set('cartoon_oval_length', '1.4', 'all')
##        cmd.set('cartoon_rect_width', '0.3', 'all')
##        cmd.set('cartoon_oval_width', '0.3', 'all')
##        cmd.set('cartoon_tube_radius', '0.5', 'all')
##        cmd.set('cartoon_transparency', '0.0', 'all')
##        cmd.cartoon('automatic', glb.SELE)
##        GUI.view['toonWidth'].set('1.4')
##        GUI.view['toonThickness'].set('0.3')
##        GUI.view['cartoonTransparency'].set('0.0')
##        GUI.view['toonTubeRadius'].set('0.5')
##        GUI.view['ribbonTypes'].invoke(0)
##    elif tag == 'spheres':
##        cmd.set('sphere_scale', '0.7', 'all')
##        cmd.set('sphere_transparency', '0.0', 'all')
##        GUI.view['sphereScale'].set('0.7')
##        GUI.view['sphereTransparency'].set('0.0')
##    elif tag == 'sticks':
##        cmd.set('stick_radius', '0.2', 'all')
##        cmd.set('stick_transparency', '0.0', 'all')
##        GUI.view['stickRadius'].set('0.2')
##        GUI.view['stickTransparency'].set('0.0')
##    elif tag == 'surface':
##        cmd.set('transparency', '0.0', 'all')
##        GUI.view['surfaceTransparency'].set('0.0')
##    elif tag == 'ambient':
##        cmd.set('ambient', '0.25', 'all')
##        GUI.view['ambientLight'].set('0.25')
##    cmd.delete('surface')
##    cmd.delete('mesh1')
##    cmd.delete('cartoon')
##    cmd.delete('helix')
##    cmd.delete('sheets')
##    cmd.delete('sticks')
##    cmd.delete('rov_1')
##    cmd.delete('rov_m1')
##    cmd.delete('map1')
##    cmd.delete('sphere1')
##    cmd.delete('rov_pc')
##    cmd.delete('rov_s1')
##    cmd.set("roving_detail", 0)
##    cmd.set("roving_origin", 0)
##    cmd.set("roving_sticks", 0)
##    cmd.set('roving_spheres', 0)
##    cmd.set("roving_polar_contacts", 0)
##    cmd.set('roving_lines', 0)
##    cmd.set('roving_isosurface', 0)
##    cmd.set('transparency', '0.0', 'all')
##    cmd.set('cartoon_transparency', '0.0', 'all')
##    cmd.set('sphere_transparency', '0.0', 'all')
##    cmd.set('stick_transparency', '0.0', 'all')
##    cmd.set('sphere_scale', '0.7', 'all')
##    cmd.set('stick_radius', '0.2', 'all')
##    cmd.cartoon('automatic', 'all')
### Make this available from the PyMOL command line
##cmd.extend('defaults', defaults)

# This does not empty the motif information dictionary like reset_motif_database(),
# but instead deletes any named PyMOL selections named after any of the currently
# known motifs in the database.
def deletemotif():
    for motif in MOTIFS:
        cmd.delete('%s'%(motif))
#cmd.extend('deletemotif', deletemotif)

#not necessary without pymol
##def show_as(show, selection):
##    '''`as` is a reserved word as of python 2.6
##    pymol used cmd.as before this and
##    had to change to cmd.show_as'''
##    try:
##        cmd.show_as(show, selection)
##    except AttributeError:
##        getattr(cmd, 'as')(show, selection)

# This function can color selections and everything else, too, using either
# colors defined in PyMOL or CPK model coloring, and show desired representations
# of both the selection and the entire structure while leaving everything else
# hidden.  The selection argument specifies what selection to color and show
# when dealing with the selection; show_selection specifies what representations
# of that selection to show; color_selection specifies what color to use for the
# selection, or CPK coloring (the default); show_all specifies what representations
# of everything to show; color_all specifies what color to color everything (or
# CPK); cpknew is a boolean that specifies whether to use the old or new CPK color
# dictionary.  In most cases (whenever show_all is not None), all objects will
# be hidden so only the specified representations of the selection and the
# structure as a whole will be shown.  None can be passed in for either
# show_selection or show_all, but if it is passed in for show_all, all currently
# visible objects will remain visible in their currently displayed representations
# in addition to showing any new representatons of the selection.  This may or may
# not be what was intended.  In any case, to work around this and hide everything
# first anyway without then showing at least one representation of all objects,
# it looks like the caller may be able to pass in the empty tuple for show_all
# instead of None.  When specifying CPK coloring, the argument to color_selection
# or color_all must be either not specified explicitly (the default is CPK) or
# be the string 'cpk' in lower case.

##def procolor(selection=None, show_selection='sticks', color_selection='cpk',
##        show_all=('sticks', 'spheres'), color_all='cpk', cpknew=False):
##    # This nested function takes two arguments:
##    # cpknew is a boolean specifying whether to use the new CPK
##    # dictionary (CPKNewDict) rather than the original (CPKDict);
##    # selection is the PyMOL selection to color.
##    '''Color in CPK or CPKnew
##    Needs the CPK DICTs defined above.'''
##    def cpk(cpknew, selection):
##        # Get the existing color indices from PyMOL
##        colorIndex = {}
##        for i in cmd.get_color_indices():
##            k, v = i
##            colorIndex[k] = v
##        # Select the right CPK dictionary
##        if cpknew:
##            cpk = CPKNewDict
##            suffix = 'cpknew'
##        else:
##            cpk = CPKDict
##            suffix = 'cpk'
##        # Iterate through the colors in the selected CPK dictionary
##        for k in cpk:
##            # Create a hopefully unique name for each color by concatenating
##            # its name in the dictionary with a suffix specifying which dictionary
##            # it came from
##            color = '%s%s' % (k, suffix)
##            # If PyMOL doesn't know about any of them, tell it
##            if color not in colorIndex:
##                cmd.set_color(color, cpk[k])
##        unk = 'not e. '
##        for k in cpk:
##            if k != 'UNK':
##                # Assuming ampersands mean "and" to PyMOL's selection algebra,
##                # this line tells PyMOL to use each color in the dictionary,
##                # again identified by its concatenated name (the first argument),
##                # to color all atoms in the selection passed to cpk() whose
##                # elemental symbols match the color's key in the dictionary
##                # (the abbreviation 'e.' in PyMOL's selection algebra can mean
##                # one of two things; in this case, it stands for "element symbol")
##                cmd.color('%s%s' % (k, suffix), 'e. %s & (%s)'%(k, selection))
##                # This builds a string of the format 'not e. A+B+C+D+...', where
##                # A, B, C, and D are element symbols.  Presumably, the intent is
##                # to build a selection containing all atoms that don't have a
##                # color defined for them in the dictionary.  I don't have any
##                # reason to believe it doesn't work, but I don't know for sure.
##                unk = '%s%s+' % (unk, k)
##        # This strips the trailing plus off of the resulting string and colors all
##        # atoms that both match it and are in the selection passed into cpk()
##        # with the unknown color 'UNK' in the dictonary.
##        cmd.color('UNK%s'%(suffix), '(%s) & (%s)' % (unk[:-1], selection))
##    # This second nested function colors the specified selection in the
##    # specified way and shows the specified representations of it
##    # toshow is the representation or tuple of representations; tocolor is either
##    # a color defined in PyMOL or 'cpk'; cpknew specifies whether to use the new
##    # or old CPK color dictionary
##    def show(selection, toshow, tocolor, cpknew):
##        # This turns on display of the representation(s) of the selection argument
##        # specified in the toshow argument.  If toshow is a single representation,
##        # just show it; if it is a tuple of representations, show each of them.
##        if type(toshow).__name__ == 'tuple':
##            for show in toshow:
##                cmd.show('%s' % (show), '%s' % (selection))
##        else:
##            cmd.show('%s' % (toshow), '%s' % (selection))
##        # If the tocolor argument specifies CPK coloring (by being equal to the
##        # string 'cpk'), run the CPK coloring function; otherwise, treat the
##        # tocolor argument as a previously defined color name in PyMOL and color
##        # the selection that way
##        if tocolor == 'cpk':
##            cpk(cpknew, selection)
##        else:
##            cmd.color('%s' % (tocolor), '%s' % (selection))
##    # We're back in the main body of procolor() now, for the first time
##    # The body of this if will execute unless None (the python null value)
##    # was passed in as the show_all argument
##    if show_all != None:
##        # First, hide everything
##        # Since this call to cmd.hide is inside the if, passing None to the
##        # show_all argument of procolor will only color the specified selection
##        # but won't hide already shown representations.  So, to color and show just
##        # the selection specified while leaving everything else hidden, the caller
##        # would need to pass in the empty tuple as the show_all argument to
##        # procolor().
##        cmd.hide('everything', 'all')
##        # Then, run the nested function show() to color all objects or atoms the
##        # way we want them.
##        show('all', show_all, color_all, cpknew)
##    # If a non-None selection was passed in (the default value is None, if not
##    # explicitly specified), color it the way the caller wants as well
##    if selection != None:
##        show(selection, show_selection, color_selection, cpknew)
### Make the above functionality available from the PyMOL command line.  I'm not
### sure whether that will allow passing any arguments in; it might just always
### use the defaults when called in this way.
##cmd.extend('procolor', procolor)
##
### This is called from within update()
##def populate():
##    # Create named selections automatically
##    cmd.select('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
##        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
##    cmd.select('dna', 'resn %s'%(DNASTR))
##    cmd.select('rna', 'resn %s'%(RNASTR))
##    cmd.select('hydrophobic', 'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
##    cmd.select('hydrophilic', 'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
##    cmd.select('acidic', 'resn ASP+GLU')
##    cmd.select('basic', 'resn ARG+HIS+LYS')
##    cmd.select('ligands', 'het')
##    cmd.select('heme', 'resn hem')
##    cmd.select('b12', 'resn b12')
##    cmd.select('cub', 'resn cub')
##    cmd.select('fes', 'resn fes')
##    cmd.select('mos', 'resn mos')
##    cmd.select('hea', 'resn hea')
##    cmd.select('cua', 'resn cua')
##    cmd.select('fco', 'resn fco')
##    cmd.select('sf4', 'resn sf4')
##    cmd.select('f3s', 'resn f3s')
##    cmd.select('fe2', 'symbol fe')
##    cmd.select('cfm', 'resn cfm')
##    cmd.select('clf', 'resn clf')
##    cmd.select('hec', 'resn hec')
##    cmd.select('cob', 'resn cob')
##    cmd.select('c2o', 'resn c2o')
##    cmd.select('pcd', 'resn pcd')
##    cmd.select('f43', 'resn f43')
##    cmd.select('sodium', 'symbol na')
##    cmd.select('zinc', 'symbol zn')
##    cmd.select('3co', 'symbol co')
##    cmd.select('Cobalt', 'symbol co')
##    cmd.select('Nickle', 'symbol ni')
##    cmd.select('Iron', 'symbol fe')
##    cmd.select('Copper', 'symbol cu')
##    cmd.select('Manganese', 'symbol mn')
##    cmd.select('Magnesium', 'symbol mg')
##    cmd.select('4mo', 'symbol mo')
##    cmd.select('Molybdenum', 'symbol mo')
##    cmd.select('calcium', 'symbol ca')
##    # Then turn them off
##    cmd.disable('ca')
##    cmd.disable('mo')
##    cmd.disable('4mo')
##    cmd.disable('mg')
##    cmd.disable('mn')
##    cmd.disable('cu')
##    cmd.disable('fe')
##    cmd.disable('ni')
##    cmd.disable('co')
##    cmd.disable('3co')
##    cmd.disable('zn')
##    cmd.disable('na')
##    cmd.disable('f43')
##    cmd.disable('pcd')
##    cmd.disable('c2o')
##    cmd.disable('cob')
##    cmd.disable('hec')
##    cmd.disable('clf')
##    cmd.disable('cfm')
##    cmd.disable('fe2')
##    cmd.disable('f3s')
##    cmd.disable('sf4')
##    cmd.disable('fco')
##    cmd.disable('cua')
##    cmd.disable('hea')
##    cmd.disable('mos')
##    cmd.disable('fes')
##    cmd.disable('cub')
##    cmd.disable('b12')
##    cmd.disable('heme')
##    cmd.disable('ligands')
##    cmd.disable('basic')
##    cmd.disable('acidic')
##    cmd.disable('hydrophilic')
##    cmd.disable('hydrophobic')
##    cmd.disable('dna')
##    cmd.disable('rna')
##    cmd.disable('protein')
##    # Create named selections for each chain, and leave them off by default
##    for letter in cmd.get_chains():
##        if letter=="":
##            letter="\"\""
##        chain = 'Chain-%s'%(letter)
##        cmd.select(chain, "chain %s"%(letter))
##        cmd.disable(chain)
##    # Delete any selections (or other objects) that contain no atoms
##    objects = cmd.get_names('all')
##    for obj in objects:
##        try:
##            if(len(cmd.index(obj)) < 1):
##                cmd.delete(obj)
##        except:
##            cmd.delete(obj)
##    # See what's left
##    objects = cmd.get_names('all')
##    # Create a list containing all the remaining objects, plus "All".
##    # If there's any protein, dna, or rna, add selections representing
##    # their negation (everything else) to the list too
##    items = ['All', ]
##    for obj in objects:
##        items.append(obj)
##        if obj in ['protein', 'dna', 'rna']:
##            items.append('not %s' % obj)
##    # Add everything in that list as an option in the EZ-Viz and View Options
##    # selection menus.  _setit is an internal TkInter class, not sure
##    # exactly why its constructor is being called here (it deals with option
##    # menu commands though, so it kind of makes sense).
##    try:
##        GUI.ez_viz['selection_menu']['menu'].delete(0, tk.END)
##        GUI.view['advanced_selection_menu']['menu'].delete(0, tk.END)
##        for item in items:
##            GUI.ez_viz['selection_menu']['menu'].add_command(label=item,
##                command=tk._setit(GUI.ez_viz['selection'], item, set_selection))
##            GUI.view['advanced_selection_menu']['menu'].add_command(label=item,
##                command=tk._setit(GUI.view['advanced_selection'], item, 
##                    set_selection))
##    except AttributeError:
##        pass
### Make the functionality available from the PyMOL command line
##cmd.extend('populate', populate)
##
### Calls defaults() and populate() (defined earlier in this file), and
### rotates everything to line up with the 3D axes
##def update():
##    defaults()
##    populate()
##    cmd.orient('all')
### Make available from the PyMOL command line
##cmd.extend('update', update)
##
# This function runs when the Random PDB button is clicked.  Before 4.2,
# it fetched the list of PDB entries from the Internet only once, then stashed
# the information in the PDB entry persistent database.  This was a second
# instance of the class used for the motif database before it was changed to a
# dictionary.  That class had problems, so both instances were removed.  Now,
# it is fetched every time the button is clicked.  That is probably not an
# improvement, since the file in question is rather large (over a 3G cellular
# data connection, clicking this button will block everything for somewhere
# between a few seconds to a couple of minutes).  This should probably be
# fetched once per program run (or even once per week), then stored locally.
# Whether a file download should run on and block the GUI thread is another
# issue.
def randompdb():
    # Adapted from pdbstore function (removed)
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
        randomPDB = Protein()
        randomPDB.getPDB(random.choice(database))
        return randomPDB
    return False
### Makes this functionality available from the PyMOL command line
##cmd.extend('randompdb',randompdb)
##
### This appears to be called when the EZ-Viz or View Options selection menus
### are used.  See the end of populate(), above.
##def set_selection(tag='all'):
##    global SELE
##    GUI.ez_viz['selection'].set(tag)
##    GUI.view['advanced_selection'].set(tag)
##    SELE = tag

# This replaces the old progress bars which were not scalable.  This class uses
# two labels side by side and adjusts their relative sizing weights to display
# progress.
class ScalableProgressBar:
    def __init__(self, parent):
        self.widget = tk.Frame(parent)
        self.leftPortion = tk.Label(self.widget, background='black')
        self.rightPortion = tk.Label(self.widget, background='white')
        self.leftPortion.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        self.rightPortion.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
        self.setProgressPercent(0)
    def getWidget(self):
        return self.widget
    def setProgressPercent(self, newLevel):
        # Don't let either weight be zero
        # Weights will go from 1 to 99,999
        multiplier = 1000

        # If weights are zero it means something different, so to show
        # 0% or 100%, just weight the labels evenly so each is half the width
        # of the progress bar, but color them either both white or both black
        maxWeight = multiplier * 100
        leftWeight = int(newLevel * multiplier)
        someOfEach = (0 < leftWeight < maxWeight)
        self.widget.columnconfigure(0, weight=leftWeight if someOfEach else 1)
        self.widget.columnconfigure(1, weight=maxWeight - leftWeight if someOfEach else 1)
        self.leftPortion.configure(background = 'black' if leftWeight > 0 else 'white')
        self.rightPortion.configure(background = 'white' if leftWeight < maxWeight else 'black')
    # I wanted to name the progress setting method starting with a lowercase
    # but this is here for backwards compatibility with the old class
    def SetProgressPercent(self, newLevel):
        self.setProgressPercent(newLevel)
