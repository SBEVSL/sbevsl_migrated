from pymol import cmd, util, preset
from pmg_tk.startup.ProMol import promolglobals as glb
from tkColorChooser import askcolor
from tkMessageBox import showinfo,showerror

def pre_surface_view(tag):
    if tag == 'Surface':
        surface_view()
    elif tag == 'Surface on Cartoon':
        surface_view('toon')
    elif tag == 'Surface on Sticks':
        surface_view('stick')
    elif tag == 'Surface on Spheres':
        surface_view('sphere')
    elif tag == 'Mesh on Sticks':
        surface_view('mesh')
    elif tag == 'Dots on Lines':
        surface_view('dot')

def pre_cartoon_view(tag):
    if tag == 'Cartoon':
        cartoon_view()
    elif tag == 'Putty':
        cartoon_view('putty')
    elif tag == 'Lines on Cartoon':
        stick_toon()
    elif tag == 'Color by Chain':
        util.cbc()

def preres(tag):
    if tag == 'Aromatics':
        color_aromatics()
    elif tag == 'Show Charged':
        show_charged()
    elif tag == 'Solubility':
        view_polarity()

def prerov(tag):
    if tag == 'Roving Sticks':
        rovingstickers()
    elif tag == 'Roving Ball&Sticks':
        rovingballstick()
    elif tag == 'Roving Spheres':
        rovingspheres()
    elif tag == 'Roving Lines':
        rovinglines()

def preele(tag):
    if tag == 'Mesh on Ribbon':
        mesh_ribbon()
    elif tag == 'Dots on Sticks':
        dot_sticks()
    elif tag == 'Surface on Lines':
        surfinglines()

def premisc(tag):
    if tag == 'Hetero Atoms':
        show_hetero()
    elif tag == 'Chain Contacts':
        chain_contact()
    elif tag == 'DNA & RNA':
        show_dna_rna()
    elif tag == 'CPK':
        glb.procolor()
    elif tag == 'Ball & Stick':
        ball_and_stick()

# Show/Hide Water
def show_hide_water(tag):
    if tag == 'Show':
        cmd.show('(resn HOH)')
        cmd.show('spheres', '(resn HOH)')
    else:
        cmd.hide('(resn HOH)')

# Coloring on Selection
def color_sel(tag):
    if tag == 'Red':
        cmd.color('red', glb.SELE)
    elif tag == 'Green':
        cmd.color('green', glb.SELE)
    elif tag == 'Orange':
        cmd.color('orange', glb.SELE)
    elif tag == 'Yellow':
        cmd.color('yellow', glb.SELE)
    elif tag == 'Blue':
        cmd.color('blue', glb.SELE)
    elif tag == 'Violet':
        cmd.color('violet', glb.SELE)
    elif tag == 'CPK':
        glb.procolor(selection=glb.SELE, show_selection='sticks',
            color_selection='cpk', show_all=None)
    elif tag == 'Other':
        color = askcolor(title = "Selection Color Chooser")
        clr = str(color[1])
        newcolor = 'newcolor%s' % glb.incnewcolor()
        if clr != None:
            cmd.set_color(newcolor,
                ([int(n, 16) for n in (clr[1:3], clr[3:5], clr[5:7])]))
            cmd.color(newcolor, glb.SELE)

# change background colors
def bgcolor_switch(tag):
    if tag == 'Black':
        cmd.bg_color('black')
    elif tag == 'White':
        cmd.bg_color('white')
    elif tag == 'Grey':
        cmd.bg_color('grey')
    elif tag == 'Other':
        color = askcolor(title = "Background Color Chooser")
        clr = str(color[1])
        newcolor = 'newcolor%s' % glb.incnewcolor()
        if clr != None:
            cmd.set_color(newcolor,
                ([int(n, 16) for n in (clr[1:3], clr[3:5], clr[5:7])]))
            cmd.bg_color(newcolor)

def show_dna_rna():
    glb.update()
    objects = cmd.get_names('all')
    cmd.set('cartoon_ring_mode' , '1')
    if 'dna' in objects or 'rna' in objects:
        if 'protein' in objects:
            cmd.show('cartoon', 'protein')
            cmd.color('gray60', 'protein')
        if 'ligands' in objects:
            cmd.show('spheres', 'ligands')
            cmd.set('sphere_transparency', '0.4', 'ligands')
            cmd.set('sphere_scale', '0.4', 'ligands')
            cmd.color('orange', 'ligands')
        if 'dna' in objects:
            cmd.show('cartoon', 'dna')
        if 'rna' in objects:
            cmd.show('cartoon', 'rna')
        cmd.color('lightblue', 'resn a')
        cmd.color('orange', 'resn c')
        cmd.color('salmon', 'resn g')
        cmd.color('palegreen', 'resn t')
        cmd.color('paleyellow', 'resn u')
        showinfo('Nucleic Acid Key',
        'Adenine = light blue\nCytosine = orange\n'+
        'Guanine = salmon red\nThymine = light green\n'+
        'Uracil = light yellow')
    else:
        showinfo("Error", "There is no DNA or RNA in this molecule.")
cmd.extend('show_dna_rna', show_dna_rna)


# default view
def cartoon_view(cartoon=None):
    glb.update()
    cmd.hide('all')
    objects = cmd.get_names('all')
    if 'protein' in objects:
        cmd.show('cartoon', 'protein')
    cmd.color("red", "ss h")
    cmd.color("yellow", "ss s")
    cmd.color("cyan", "ss l+\'\'")
    if 'ligands' in objects:
        glb.procolor('ligands','spheres','orange',None)
    if 'dna' in objects:
        glb.procolor('dna','sticks','cpk',None)
    if 'rna' in objects:
        glb.procolor('rna','sticks','cpk',None)
    if cartoon == 'putty':
        try:
            cmd.cartoon('putty', 'protein')
        except:
            showinfo('Error', 'Putty is not supported by this version of PyMol')
    else:
        cmd.set('cartoon_ring_mode' , '1')

# show hetero atoms
def show_hetero():
    glb.update()
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        if 'protein' in objects:
            cmd.show('cartoon', 'protein')
            cmd.set('cartoon_transparency', '0.7', 'protein')
        if 'dna' in objects:
            glb.procolor('dna','sticks','cpk',None)
        if 'rna' in objects:
            glb.procolor('rna','sticks','cpk',None)
        glb.procolor('ligands around 6','sticks','cpk','cartoon')
        glb.procolor('ligands','spheres','orange',None)
        cmd.set('sphere_transparency', '0.1', 'ligands')
        cmd.set('stick_radius', '0.3', 'ligands around 6')
        cmd.set('stick_transparency', '0.1', 'ligands around 6')
    else:
        showinfo("Error", "There are no hetero atoms in this molecule.")
cmd.extend('show_hetero', show_hetero)

# ball and stick view
def ball_and_stick():
    glb.update()
    preset.ball_and_stick('all')
cmd.extend('ball_and_stick', ball_and_stick)

def surface_view(surface = None):
    '''
    Show the surface of the molecule in different representations
    '''
    glb.update()
    util.cbc()
    cmd.hide('all')
    if surface == 'dot':
        cmd.set('dot_density',1)
        cmd.show('lines','all')
        cmd.show('dots','all')
    elif surface == 'mesh':
        cmd.set('mesh_quality',3)
        cmd.show('stick','all')
        cmd.show('mesh','all')
    elif surface == 'sphere':
        cmd.set('sphere_scale',0.5,'all')
        cmd.show('spheres','all')
        cmd.show('surface','all')
        cmd.set('transparency',0.5,'all')
    elif surface == 'stick':
        cmd.show('stick','all')
        cmd.show('surface','all')
        cmd.set('transparency',0.5,'all')
    elif surface == 'toon':
        cmd.set('cartoon_smooth_loops', 0)
        cmd.show('cartoon','all')
        cmd.show('surface','all')
        cmd.set('transparency',0.5,'all')
    else:
        cmd.show('surface','all')
cmd.extend('surface_view', surface_view)

# show the polarities of the molecule
def view_polarity():
    glb.update()
    objects = cmd.get_names('all')
    if 'protein' in objects:
        cmd.show('surface', 'protein')
    cmd.color('red', 'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
    cmd.color('blue', 'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
    cmd.show('spheres', 'het')
    cmd.color('green', 'het')
    cmd.set('cartoon_ring_mode' , '1')
    if 'dna' in objects:
        cmd.show('cartoon', 'resn %s'%(glb.DNASTR))
        glb.procolor(glb.DNASTR,'cartoon','cpk',None)
    showinfo('Info', 'Red = Hydrophobic\nBlue = Hydrophilic')
cmd.extend('solubility', view_polarity)

# aromatics view
def color_aromatics():
    glb.update()
    cmd.hide('all')
    cmd.show('cartoon', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.color('aquamarine', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+'+
        'TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.set('cartoon_transparency', '0.6', 'resn GLY+PRO+ALA+VAL+LEU+ILE+'+
        'MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.show('cartoon', 'resn %s'%(glb.DNASTR))
    cmd.color('aquamarine', 'resn %s'%(glb.DNASTR))
    cmd.set('cartoon_transparency', '0.6', 'resn %s'%(glb.DNASTR))
    cmd.select('aromatics', 'resn phe+tyr+trp+his')
    cmd.color('red', 'aromatics')
    cmd.show('sticks', 'aromatics and (!name c+n+o)')
    cmd.set('stick_radius', '0.4', 'all')
    cmd.delete('aromatics')
cmd.extend('color_aromatics', color_aromatics)

def show_charged():
    glb.update()
    objects = cmd.get_names('all')
    cmd.hide('all')
    cmd.show('cartoon', 'all')
    cmd.color('gray', 'all')
    cmd.select('pos', 'resn arg+lys+his')
    cmd.show('sticks', 'pos and !name c+n+o')
    cmd.color('marine', 'pos')
    cmd.delete('pos')
    cmd.select('neg', 'resn glu+asp')
    cmd.show('sticks', 'neg and !name c+n+o')
    cmd.color('red', 'neg')
    cmd.delete('neg')
    cmd.set('cartoon_smooth_loops', '0')
    if 'protein' in objects:
        showinfo('Charge Info', 'Blue = Positively charged Amino Acids\n'+
            'Red = Negatively charged Amino Acids')
cmd.extend('show_charged', show_charged)

def stick_toon():
    glb.update()
    cmd.hide('all')
    cmd.show('lines')
    cmd.create('cartoon', 'all')
    cmd.show('cartoon', 'cartoon')
    cmd.color('salmon', 'cartoon')
    cmd.color('cyan', 'resn a+t+u+g+c')
cmd.extend('stick_and_cartoon', stick_toon)

def rovingstickers():
    glb.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("stick_radius", 0.3)
    cmd.set("roving_polar_contacts", 8)
    cmd.set("roving_sticks", glb.GUI.ez_viz['roving'].get())
cmd.extend('roving_stick', rovingstickers)

def rovinglines():
    glb.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_sticks", 0)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('roving_lines', glb.GUI.ez_viz['roving'].get())
cmd.extend('roving_line', rovinglines)

def rovingspheres(): 
    glb.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('sphere_transparency', '0.2')
    cmd.set('sphere_scale', '0.8', 'all')
    cmd.set('roving_spheres', glb.GUI.ez_viz['roving'].get())
cmd.extend('roving_sphere', rovingspheres)

def rovingballstick():
    glb.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('sphere_transparency', '0.2')
    cmd.set("sphere_scale", "0.3", "all")
    cmd.set('roving_spheres', glb.GUI.ez_viz['roving'].get())
    cmd.set("stick_radius", 0.3)
    cmd.set("roving_polar_contacts", 8)
    cmd.set("roving_sticks", glb.GUI.ez_viz['roving'].get())
cmd.extend('roving_ballstick', rovingballstick)

def chain_contact():
    def chain_contact_loop(c,skip,chainPullList):
        d = 0
        l = c + 1
        while len(chainPullList) > l and (26-d) >= 0:
            cmd.select('chain_contact','%s w. 5 of %s'%(chainPullList[d],chainPullList[c+1]),enable=0,quiet=1,merge=1)
            cmd.select('chain_contact','%s w. 5 of %s'%(chainPullList[c+1],chainPullList[d]),enable=0,quiet=1,merge=1)
            d += 1
            l += 1
            while d == (c+1) or d in skip:
                d += 1
    glb.update()
    cmd.hide('everything')
    cmd.show('mesh', 'all')
    cmd.color('gray40', 'all')
    objects = cmd.get_names('all')
    chainPullList = []
    for i in cmd.get_chains(quiet=1):
        chainPullList.append('Chain-'+i)
    if len(chainPullList) < 2:
        showinfo('Notice','There needs to be two or more chains to run this functions.')
        return False
    c = 0
    skip = []
    while c < (len(chainPullList)-1) and c < 26:
        skip.append(c+1)
        chain_contact_loop(c,skip,chainPullList)
        c += 1
    glb.procolor('chain_contact','mesh','cpk',None)
    cmd.delete('chain_contact')
    return chainPullList
cmd.extend('chain_contact',chain_contact)
    #-----------Electron Density Presets----------------#

def mesh_ribbon():
    cmd.hide('everything')
    glb.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    glb.procolor(None,show_all=('lines','ribbon'),color_all='red')
    cmd.isomesh('map1', 'map', '1')
    cmd.color('purple','map1')
cmd.extend('mesh_ribbon', mesh_ribbon)

def dot_sticks():
    cmd.hide('everything')
    glb.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    cmd.isodot("map1", "map", 9999.0, 'all')
    cmd.isodot('map1', 'map', '1')

def surfinglines():
    cmd.hide('everything')
    glb.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    glb.procolor(None,show_all='lines')
    cmd.isosurface('map1', 'map', '1')
    cmd.color('orange', "map1")
    cmd.set('transparency', '0.4')
    cmd.set('ambient', '0.45')
cmd.extend('surfinglines', surfinglines)

# Show ligands as spheres
def space_fill_ligand():
    cmd.select('Bad', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+'+
        'BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c'+
        '+t+u+HOH+MSE')
    cmd.select("ligand", "!Bad")
    cmd.hide("everything", "ligand")
    cmd.show("spheres", "ligand")
    cmd.delete("Bad")
    cpkligands()
    cmd.deselect()

# Show/Hide ALL representations
def show_all(tag):
    list = rep1.getvalue()
    list2 = rep2.getvalue()
    if tag == 'Show all':
        rep1.invoke('Lines')
        rep1.invoke('Sticks')
        rep1.invoke('Ribbons')
        rep1.invoke('Cartoon')
        rep2.invoke('Dots')
        rep2.invoke('Spheres')
        rep2.invoke('Mesh')
        rep2.invoke('Surface')
        
        for item in list:
            rep1.invoke(item)
        for item in list2:
            rep2.invoke(item)
        cmd.show('everything')
    else:
        cmd.hide('everything')
        for item in list:
            rep1.invoke(item)
        for item in list2:
            rep2.invoke(item)

# Show individual representations
def show_rep(tag):
    try:
        sel = glb.SELE
        if tag == 'Lines':
            cmd.show('lines', sel)
        elif tag == 'Sticks':
            cmd.show('sticks', sel)
        elif tag == 'Ribbons':
            cmd.show('ribbon', sel)
        elif tag == 'Cartoon':
            cmd.show('cartoon', sel)
        elif tag == 'Dots':
            cmd.show('dots', sel)
        elif tag == 'Spheres':
            cmd.show('spheres', sel)
        elif tag == 'Mesh':
            cmd.show('mesh', sel)
        elif tag == 'Surface':
            cmd.show('surface', sel)
        elif tag == 'Water':
            cmd.show('spheres', '(resn HOH)')
        elif tag == 'Ball and Stick':
            preset.ball_and_stick(sel)
        elif tag == 'Polar Contacts':
            cmd.dist(sel+"_polar_conts", sel, sel, quiet = 1, mode = 2, label = 0,
                reset = 1)
            cmd.enable(sel+"1CHO_polar_conts")        
    except:
        showinfo('Error', 'Update Selection!')


# Hide individual representations
def hide_rep(tag):
    try:
        sel = glb.SELE
        if tag == 'Lines':
            cmd.hide('lines', sel)
        elif tag == 'Sticks':
            cmd.hide('sticks', sel)
        elif tag == 'Ribbons':
            cmd.hide('ribbon', sel)
        elif tag == 'Cartoon':
            cmd.hide('cartoon', sel)
        elif tag == 'Dots':
            cmd.hide('dots', sel)
        elif tag == 'Spheres':
            cmd.hide('spheres', sel)
        elif tag == 'Mesh':
            cmd.hide('mesh', sel)
        elif tag == 'Surface':
            cmd.hide('surface', sel)
        elif tag == 'Water':
            cmd.hide('(resn HOH)')
        elif tag == 'Everything':
            cmd.hide('everything', sel)
        elif tag == 'Ball and Stick':
            cmd.hide('spheres', sel)
            cmd.hide('sticks', sel)
        elif tag == 'Polar Contacts':
            cmd.delete(sel+"_polar_conts")
    except:
        showinfo('Error', 'Update Selection!')
