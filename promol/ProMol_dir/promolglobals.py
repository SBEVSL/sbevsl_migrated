from pymol import cmd
import Tkinter as tk
import os

Photos = None
script = 0
AminoMenuList = None
AminoList = None
AlphaSequence = None
alphaSequence = None
Tabs = {}

try:
    PYMOL_PATH = os.environ['PYMOL_PATH']+os.sep
except KeyError:
    PYMOL_PATH = '.'+os.sep
PROMOL_PATH = "%smodules" % (PYMOL_PATH)+os.sep+"pmg_tk"+os.sep+"startup"+os.sep
PROMOL_DIR_PATH = "%sProMol_dir%s" % (PROMOL_PATH, os.sep)

splash = tk.PhotoImage(file = "%ssplashmol.gif" % (PROMOL_DIR_PATH))

#Amino Acid Abbre List for Menus
AminoMenuList = ('', 'ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 
    'gly', 'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp',
    'tyr', 'val')
#Amino Acid Array for validation
AminoList = ('ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly',
    'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr',
    'val')

Photos = {}
for x in AminoList:
    for y in ('3D', '2D'):
        Photos["%s%s" % (x, y)] = tk.PhotoImage(file = "%sAminoPics%s%s%s.gif"
            % (PROMOL_DIR_PATH, os.sep, x, y))

#A - Z
AlphaSequence = [ "%c" % (x) for x in range(ord('A'), ord('Z')+1)]
#a - z
alphasequence = [ "%c" % (x) for x in range(ord('a'), ord('z')+1)]

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

def color_cpk(str):
    cmd.color("carbgray", "(elem C)" + str )
    cmd.color("red", "elem O" + str )
    cmd.color("white", "elem H" + str )
    cmd.color("nitblue", "elem N" + str )
    cmd.color("sulfyellow", "elem S" + str )
    cmd.color("phosorange", "elem P+Fe+Ba" + str )
    cmd.color("green", "elem Cl+B" + str )
    cmd.color("brown", "elem Br+Zn+Cu+Ni" + str )
    cmd.color("blue", "elem Na" + str )
    cmd.color("forest", "elem Mg" + str )
    cmd.color("darkgray", "elem Ca+Mn+Al+Ti+Cr+Ag" + str )
    cmd.color("goldenrod", "elem Au+F+Si" + str)
    cmd.color("ipurple", "elem I" + str)
    cmd.color("firebrick", "elem Li" + str)
    cmd.color("helpink", "elem He" + str)

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
