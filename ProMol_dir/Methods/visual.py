from pymol import cmd, util
from pmg_tk.startup.ProMol_dir import promolglobals as pglob

def show_dna_rna():
    pglob.update()
    objects = cmd.get_names('all')
    cmd.set('cartoon_ring_mode' , '1')
    if 'nucleic_acid' in objects:
        if 'protein' in objects:
            cmd.show('cartoon', 'protein')
            cmd.color('gray60', 'protein')
        if 'ligands' in objects:
            cmd.show('spheres', 'ligands')
            cmd.set('sphere_transparency', '0.4', 'ligands')
            cmd.set('sphere_scale', '0.4', 'ligands')
            cmd.color('orange', 'ligands')
        cmd.show('cartoon', 'nucleic_acid')
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
    pglob.update()
    cmd.hide('all')
    if cartoon == 'putty':
        try:
            cmd.show('spheres', 'ligands')
            cmd.color('orange', 'ligands')
            cmd.show('cartoon', 'protein')
            cmd.cartoon('putty', 'protein')
            cmd.color("red", "ss h")
            cmd.color("yellow", "ss s")
            cmd.color("cyan", "ss l+\'\'")
            cmd.show('sticks', 'nucleic_acid')
            cpknucleic()
        except:
            showinfo('Error', 'Putty is not supported by this version of PyMol')
    else:
        cmd.set('cartoon_ring_mode' , '1')
        cmd.show('cartoon', 'all')
        cmd.hide('ligands')
        cmd.show('spheres', 'ligands')
        cmd.color("red", "ss h")
        cmd.color("yellow", "ss s")
        cmd.color("cyan", "ss l+\'\'")

# show hetero atoms
def show_hetero():
    pglob.update()
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        if 'protein' in objects:
            cmd.show('cartoon', 'protein')
            cmd.set('cartoon_transparency', '0.7', 'protein')
        if 'nucleic_acid' in objects:
            cmd.set('cartoon_ring_mode', '1')
            cmd.show('cartoon', 'nucleic_acid')
            cmd.set('cartoon_transparency', '0.7', 'nucleic_acid')
            cmd.color('cyan', 'nucleic_acid')
        cmd.show('spheres', 'ligands')
        cmd.set('sphere_transparency', '0.1', 'ligands')
        cmd.show("sticks", "ligands around 6'")
        cmd.set('stick_radius', '0.3', 'ligands around 6')
        cmd.color('orange', 'ligands')
        cmd.select("interaction", "ligands around 6'")
        cpkinteraction()
        cmd.set('stick_transparency', '0.1', 'interaction')
        cmd.disable('interaction')
    else:
        showinfo("Error", "There are no hetero atoms in this molecule.")
cmd.extend('show_hetero', show_hetero)

# ball and stick view
def ball_and_stick():
    pglob.update()
    objects = cmd.get_names('all')
    cmd.set("stick_radius", "0.1", "all")
    cmd.set("sphere_scale", "0.3", "all")
    if 'protein' in objects:
        cmd.show('spheres', 'protein')
        cmd.show('sticks', 'protein')
        cpkprotein()
    if 'nucleic_acid' in objects:
        cmd.set('cartoon_ring_mode', '1')
        cmd.show('cartoon', 'resn a+g+c+t+u')
        cmd.show('spheres', 'resn a+g+c+t+u')
        cmd.show('sticks', 'resn a+g+c+t+u')
        cpknucleic()
    if 'ligands' in objects:
        cmd.show('spheres', 'ligands')
        cmd.color('orange', 'ligands')
cmd.extend('ball_and_stick', ball_and_stick)

def surface_view(surface = None):
    '''
    Show the surface of the molecule in different representations
    '''
    pglob.update()
    util.cbc()
    cmd.do('hide all')
    if surface == 'dot':
        cmd.do('set dot_density, 3')
        cmd.do('show lines, all')
        cmd.do('show dots, all')
    elif surface == 'mesh':
        cmd.do('set mesh_quality, 3')
        cmd.do("show stick, all")
        cmd.do("show mesh, all")
    elif surface == 'sphere':
        cmd.do('set sphere_scale, 0.5, all')
        cmd.do('show spheres, all')
        cmd.do('show surface, all')
        cmd.do('set transparency, 0.5, all')
    elif surface == 'stick':
        cmd.do('show stick, all')
        cmd.do('show surface, all')
        cmd.do('set transparency, 0.5, all')
    elif surface == 'toon':
        cmd.do('set cartoon_smooth_loops, 0')
        cmd.do('show cartoon, all')
        cmd.do('show surface, all')
        cmd.do('set transparency, 0.5, all')
    else:
        cmd.do('show surface, all')
cmd.extend('surface_view', surface_view)

# show the polarities of the molecule
def view_polarity():
    pglob.update()
    objects = cmd.get_names('all')
    if 'protein' in objects:
        cmd.show('surface', 'protein')
    cmd.color('red', 'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
    cmd.color('blue', 'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
    cmd.show('spheres', 'het')
    cmd.color('green', 'het')
    cmd.set('cartoon_ring_mode' , '1')
    cmd.show('cartoon', 'resn a+g+c+t+u')
    cpknucleic()
    showinfo('Info', 'Red = Hydrophobic\nBlue = Hydrophilic')
cmd.extend('solubility', view_polarity)

# aromatics view
def color_aromatics():
    pglob.update()
    cmd.hide('all')
    cmd.show('cartoon', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.color('aquamarine', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+'+
        'TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.set('cartoon_transparency', '0.6', 'resn GLY+PRO+ALA+VAL+LEU+ILE+'+
        'MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.show('cartoon', 'resn t+u+g+c+a')
    cmd.color('aquamarine', 'resn u+g+c+a+t')
    cmd.set('cartoon_transparency', '0.6', 'resn a+u+c+t+g')
    cmd.select('aromatics', 'resn phe+tyr+trp+his')
    cmd.color('red', 'aromatics')
    cmd.show('sticks', 'aromatics and (!name c+n+o)')
    cmd.set('stick_radius', '0.4', 'all')
    cmd.delete('aromatics')
cmd.extend('color_aromatics', color_aromatics)

def show_charged():
    pglob.update()
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

def stick_toon(*args):
    pglob.update()
    cmd.hide('all')
    cmd.show('lines')
    cmd.create('cartoon', 'all')
    cmd.show('cartoon', 'cartoon')
    cmd.color('salmon', 'cartoon')
    cmd.color('cyan', 'resn a+t+u+g+c')
cmd.extend('stick_and_cartoon', stick_toon)

def rovingstickers(*args):
    cmdRovStick = ' '
    
    try:
        cmdRovStick = float(args[0])
    except:
        pass
    try:
        self = args[0]
    except:
        print 'Usage: roving_stick # (# is value between 0 and 20)'
    
    pglob.update()
    
    
    cmd.hide('everything')
    cmd.remove("hydro")
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("stick_radius", 0.3)
    
    try:
        cmd.set("roving_sticks", rovingradius2.get())
    except:
        cmd.set("roving_sticks", cmdRovStick)
    cmd.set("roving_polar_contacts", 8)
    cpkprotein()
    cpknucleic()
    cpkligands()
cmd.extend('roving_stick', rovingstickers)

def rovinglines(*args):
    cmdRovLine = ''
    print len(args)
    #This next construction looks strange, I know, but this way it executes
    #the default settings if the user does not specifiy range!
    #Don't Worry. I plan on fixing this.
    try:
        cmdRovLine = float(args[0])
    except:
        pass
    try:
        self = args[0]
    except:
        print 'Usage: roving_line # (# is value between 0 and 20)'
    
    pglob.update()
    
    
    cmd.hide('everything')
    cmd.remove("hydro")
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_sticks", 0)
    try:
        cmd.set('roving_lines', rovingradius2.get())
    except:
        cmd.set('roving_lines', cmdRovLine)
        cmd.set("roving_polar_contacts", 8)
    cpkprotein()
    cpknucleic()
    cpkligands()
cmd.extend('roving_line', rovinglines)

def rovingballstick(*args):
    cmdRovBall = ''
    
    try:
        cmdRovBall = float(args[0])
    except:
        pass
    try:
        self = args[0]
    except:
        print 'Usage: roving_ballstick # (# is value between 0 and 20)'
    pglob.update()
    cmd.hide('everything')
    cmd.remove("hydro")
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    try:
        cmd.set('roving_sticks', rovingradius2.get())
    except:
        cmd.set('roving_sticks', cmdRovBall)
        cmd.set("roving_polar_contacts", 8)
    try:
        cmd.set('roving_spheres', rovingradius2.get())
    except:
        cmd.set('roving_spheres', cmdRovBall)
        cmd.set('sphere_transparency', '0.2')
        cmd.set("stick_radius", "0.1", "all")
        cmd.set("sphere_scale", "0.3", "all")
    cpkprotein()
    cpknucleic()
    cpkligands()
cmd.extend('roving_ballstick', rovingballstick)


def rovingspheres(*args):
    cmdRovSphere = ''
    
    try:
        cmdRovSphere = float(args[0])
    except:
        pass
    try:
        self = args[0]
    except:
        print 'Usage: roving_sphere # (# is value between 0 and 20)'
    
    pglob.update()
    
    cmd.hide('everything')
    cmd.remove("hydro")
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    try:
        cmd.set('roving_spheres', rovingradius2.get())
    except:
        cmd.set('roving_spheres', cmdRovSphere)
        cmd.set("roving_polar_contacts", 8)
        cmd.set('sphere_transparency', '0.2')
        cmd.set('sphere_scale', '0.8', 'all')
    cpkprotein()
    cpknucleic()
    cpkligands()
cmd.extend('roving_sphere', rovingspheres)

def chain_contact(*args):
    try:
        self = args[0]
    except:
        pass
    
    cmd.hide('everything')
    cmd.show('mesh', 'all')
    cmd.color('gray40', 'all')
    cmd.select("Chain-A", "chain A")
    checkforchain()
    cmd.orient()
    objects = cmd.get_names('all')
    chainpulllist = []
    
    if 'Chain-A' in objects:
        chainpulllist.append('Chain-A')
    
    if len(chainpulllist) >1:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[1])
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[0])
    if len(chainpulllist) >2:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[2])
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[2])
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[0])
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[1])
    if len(chainpulllist) >3:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[3])
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[3])
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[3])
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[0])
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[1])
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[2])
    if len(chainpulllist) >4:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[4])
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[4])
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[4])
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[4])
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[0])
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[1])
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[2])
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[3])
    if len(chainpulllist) >5:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[5])
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[5])
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[5])
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[5])
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[5])
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[0])
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[1])
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[2])
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[3])
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[4])
cmd.extend('chain_contact', chain_contact)


def show_cpk(*args):
    try:
        self = args[0]
        pglob.update()
    except:
        pass
    objects = cmd.get_names('all')
    
    
    
    cmd.set("sphere_scale", "0.7", "all")
    cmd.show('spheres', 'all')
cmd.extend('show_cpk', show_cpk)

    #-----------Electron Density Presets----------------#

def mesh_ribbon(self):
    try:
        try:
            cmd.hide('everything')
            cmd.isomesh('map1', 'map', contour1.get())
        except:
            try:
                cmd.set("suspend_updates", 1, quiet = 1)
                cmd.remove("hydro")
                cmd.map_new('map', "gaussian", "0.75", 'all')
                cmd.set("suspend_updates", 0, quiet = 1)
                cmd.refresh()
                cmd.isomesh('map1', 'map', '1')
            except:        
                showinfo("Error", 'No PDB is present')
            cmd.show('ribbon', 'all')
        cmd.show('lines', 'all')
        cmd.color('red', 'all')
        cmd.color('purpleblue', 'map1')
    except:
        cmd.show('lines', 'all')
        showinfo('Alert', 'Protein must be present')
cmd.extend('mesh_ribbon', mesh_ribbon)

def dot_sticks(*args):
    try:
        cmd.hide('everything')
        try:
            cmd.set("suspend_updates", 1, quiet = 1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map', "gaussian", "0.75", 'all')
            cmd.isodot("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates", 0, quiet = 1)
            cmd.refresh()
            cmd.isodot('map1', 'map', '1')
        except:
            showinfo("Error", 'No PDB is present')
        cmd.show('sticks', 'all')
        cmd.color('blue', 'all')
        cmd.color('red', 'map1')
    except:
        cmd.show('lines', 'all')
        showinfo('Alert', 'Protein must be present')
        cmd.extend('dot_sticks', dot_sticks)

def surfinglines(*args):
    
    try:
        cmd.hide('everything')
        pglob.update()
        
        
        
        try:
            cmd.remove("hydro")
            cmd.map_new('map', "gaussian", "0.75", 'all')
            cmd.isosurface('map1', 'map', '1')
            cmd.show('lines', 'all')
            cpkprotein()
            cpkligands()
            cpknucleic()
            cmd.color('white', 'elem c')
            cmd.color('orange', "map1")
            cmd.set('transparency', '0.4')
            cmd.set('ambient', '0.45')
        except:
            cmd.show('lines', 'all')
            showinfo("Error", 'No PDB is present')
    except:
        cmd.show('lines', 'all')
        showinfo('Alert', 'Protein must be present')
cmd.extend('surfinglines', surfinglines)

def color_cpk(str ):
    color_cpk()

# Attempt to simulate the default PyMOL colorings
def color_default(self):
    cmd.color("green", "elem C")
    cmd.color("red", "elem O")
    cmd.color("blue", "elem N")

# Show ligands as spheres
def space_fill_ligand(self):
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
        cmd.do('show everything')
    else:
        cmd.do('hide everything')
        for item in list:
            rep1.invoke(item)
        for item in list2:
            rep2.invoke(item)

# Show individual representations
def show_rep(tag):
    try:
        sel = sel
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
            cmd.show('(resn HOH)')
            cmd.show('spheres', '(resn HOH)')
        elif tag == 'Ball and Stick':
            cmd.set('sphere_scale', '0.35', sel)
            cmd.show('spheres', sel)
            cmd.show('sticks', sel)
        elif tag == 'Polar Contacts':
            cmd.dist(sel+"_polar_conts", sel, sel, quiet = 1, mode = 2, label = 0,
                reset = 1)
            cmd.enable(sel+"1CHO_polar_conts")        
    except:
        showinfo('Error', 'Update Selection!')


# Hide individual representations
def hide_rep(tag):
    try:
        sel = sel
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
 
 
 #-------------Version 2--------------#

# Set selection of atoms
#     - initial selection is 'all'
def set_sel(tag):
    cmd.deselect()
    c = re.compile("^Chain")
    if tag == 'All':
            sel = 'all'
    elif tag == 'protein':
            sel = 'protein'
    elif tag == 'nucleic_acid':
            sel = 'nucleic_acid'
    elif tag == 'ligands':
            sel = 'ligands'
    elif tag == 'heme':
            sel = 'heme'
    elif tag == 'Chain-A':
        sel = ('Chain-A')
    elif tag == 'Chain-A':
        sel = ('Chain-A')
    elif tag == 'Chain-B':
        sel = ('Chain-B')
    elif tag == 'Chain-C':
        sel = ('Chain-C')
    elif tag == 'Chain-D':
        sel = ('Chain-D')
    elif tag == 'Chain-E':
        sel = ('Chain-E')
    elif tag == 'Chain-F':
        sel = ('Chain-F')
    elif tag == 'Chain-G':
        sel = ('Chain-G')
    elif tag == 'Chain-H':
        sel = ('Chain-H')
    elif tag == 'Chain-I':
        sel = ('Chain-I')
    elif tag == 'Chain-J':
        sel = ('Chain-J')
    elif tag == 'Chain-K':
        sel = ('Chain-K')
    elif tag == 'Chain-L':
        sel = ('Chain-L')
    elif tag == 'Chain-M':
        sel = ('Chain-M')
    elif tag == 'Chain-N':
        sel = ('Chain-N')
    elif tag == 'Chain-O':
        sel = ('Chain-O')
    elif tag == 'Chain-P':
        sel = ('Chain-P')
    elif tag == 'Chain-Q':
        sel = ('Chain-Q')
    elif tag == 'Chain-R':
        sel = ('Chain-R')
    elif tag == 'Chain-S':
        sel = ('Chain-S')
    elif tag == 'Chain-T':
        sel = ('Chain-T')
    elif tag == 'Chain-U':
        sel = ('Chain-U')
    elif tag == 'Chain-V':
        sel = ('Chain-V')
    elif tag == 'Chain-W':
        sel = ('Chain-W')
    elif tag == 'Chain-X':
        sel = ('Chain-X')
    elif tag == 'Chain-Y':
        sel = ('Chain-Y')
    elif tag == 'Chain-Z':
        sel = ('Chain-Z')
    elif tag == 'Not Selected':
        try:
            cmd.select('selection', '!sele')
            cmd.deselect()
            sel = 'selection'
        except:
            showinfo("Error", 'No selection has been made')
    elif tag == 'hydrophobic':
        sel = 'hydrophobic'
    elif tag == 'hydrophilic':
        sel = 'hydrophilic'
    elif tag == 'acidic':
        sel = 'acidic'
    elif tag == 'basic':
        sel = 'basic'

# Set selection of atoms
#     - initial selection is 'all'

def set_sel1(tag):
    cmd.deselect()
    c = re.compile("^Chain")
    if tag == 'All':
            sel1 = 'all'
    elif tag == 'protein':
            sel1 = 'protein'
    elif tag == 'nucleic_acid':
            sel1 = 'nucleic_acid'
    elif tag == 'ligands':
            sel1 = 'ligands'
    elif tag == 'heme':
            sel1 = 'heme'
    elif tag == 'Chain-A':
        sel1 = ('Chain-A')
    elif tag == 'Chain-A':
        sel1 = ('Chain-A')
    elif tag == 'Chain-B':
        sel1 = ('Chain-B')
    elif tag == 'Chain-C':
        sel1 = ('Chain-C')
    elif tag == 'Chain-D':
        sel1 = ('Chain-D')
    elif tag == 'Chain-E':
        sel1 = ('Chain-E')
    elif tag == 'Chain-F':
        sel1 = ('Chain-F')
    elif tag == 'Chain-G':
        sel1 = ('Chain-G')
    elif tag == 'Chain-H':
        sel1 = ('Chain-H')
    elif tag == 'Chain-I':
        sel1 = ('Chain-I')
    elif tag == 'Chain-J':
        sel1 = ('Chain-J')
    elif tag == 'Chain-K':
        sel1 = ('Chain-K')
    elif tag == 'Chain-L':
        sel1 = ('Chain-L')
    elif tag == 'Chain-M':
        sel1 = ('Chain-M')
    elif tag == 'Chain-N':
        sel1 = ('Chain-N')
    elif tag == 'Chain-O':
        sel1 = ('Chain-O')
    elif tag == 'Chain-P':
        sel1 = ('Chain-P')
    elif tag == 'Chain-Q':
        sel1 = ('Chain-Q')
    elif tag == 'Chain-R':
        sel1 = ('Chain-R')
    elif tag == 'Chain-S':
        sel1 = ('Chain-S')
    elif tag == 'Chain-T':
        sel1 = ('Chain-T')
    elif tag == 'Chain-U':
        sel1 = ('Chain-U')
    elif tag == 'Chain-V':
        sel1 = ('Chain-V')
    elif tag == 'Chain-W':
        sel1 = ('Chain-W')
    elif tag == 'Chain-X':
        sel1 = ('Chain-X')
    elif tag == 'Chain-Y':
        sel1 = ('Chain-Y')
    elif tag == 'Chain-Z':
        sel1 = ('Chain-Z')
    elif tag == 'Not Selected':
            cmd.select('selection', '!sele')
            cmd.deselect()
            sel1 = 'selection'
    elif tag == 'hydrophobic':
            sel1 = 'hydrophobic'
    elif tag == 'hydrophilic':
            sel1 = 'hydrophilic'
    elif tag == 'acidic':
            sel1 = 'acidic'
    elif tag == 'basic':
            sel1 = 'basic'

#preset menubar link functions

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
        color_by_chain()

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
        show_cpk()
    elif tag == 'Ball & Stick':
        ball_and_stick()

def premovie(tag):
    if tag == 'Ligand Zoom':
        ligandZoom()
    elif tag == 'Build Protein':
        growProtein()
    elif tag == 'Highlight Chains':
        highlight_chains()
    elif tag == 'Rotate':
        rotate_y()
    elif tag == 'Chain Pull':
        chain_pull()
    elif tag == 'Ligand Pull':
        Ligand_Pull()
    elif tag == 'Surface to Stick':
        surface_stick()
    elif tag == 'Surface to Cartoon':
        surface_cartoon()
    elif tag == 'Play':
        play()
    elif tag == 'Stop':
        stop()
    elif tag == 'Rewind':
        rewind()

def set_cmd_type(tag):
    '''
    Tell our command line what type of commands to read
    '''
    if tag == 'PyMOL':
        commandLine.setvalue('Enter PyMOL Commands Here')
        cmdType = 'PyMOL'
    else:
        commandLine.setvalue('Enter Chime Commands Here')
        cmdType = 'Chime'

def command_line(self):
    '''
    Read commands from command line
    '''
    try:
        command = commandLine.getvalue()
        if cmdType == 'PyMOL':
            cmd.do(command)
            commandLine.clear()
        else:
            converter.parseIt(command, commandLine, output)
    except:
        showinfo('Error',
            'Invalid command or you must load the PDB through Pro-MOL')

# Coloring on Selection
def color_sel(tag):
    try:
        sel = sel
        if tag == 'Red':
                cmd.color('red', sel)
        elif tag == 'Green':
                cmd.color('green', sel)
        elif tag == 'Orange':
                cmd.color('orange', sel)
        elif tag == 'Yellow':
                cmd.color('yellow', sel)
        elif tag == 'Blue':
                cmd.color('blue', sel)
        elif tag == 'Violet':
                cmd.color('violet', sel)
        elif tag == 'CPK':
                cmd.color("oxygen", "(elem O and "+sel+")")
                cmd.color("nitrogen", "(elem N and "+sel+")")
                cmd.color("sulfur", "(elem S and "+sel+")")
                cmd.color("hydrogen", "(elem H and "+sel+")")
                cmd.color("gray", "(elem C and "+sel+")")
        elif tag == 'Other':
                color = askcolor(parent = int,
                    title = "Selection Color Chooser")
                colorArray = []
                if color[0] != None:
                        list = color[0]
                        print list
                        for each in list:
                                z = (each/255.0)
                                val = repr(z)
                                colorArray.append(val)
                        cmd.set_color('newcolor', colorArray)
                        cmd.color('newcolor', sel)
    except:
        showinfo('Error', 'Update Selection!')
        
def stereo_switch(tag):
    if tag == 'Off':
        cmd.stereo('off')
    elif tag == 'Quad':
        cmd.stereo('off')
        cmd.stereo('cross')
        cmd.stereo('quadbuffer')
        cmd.stereo('on')
    elif tag == 'Cross-Eye':
        cmd.stereo('off')
        cmd.stereo('cross')
        cmd.stereo('on')
    else:
        cmd.stereo('off')
        cmd.stereo('walleye')
        cmd.stereo('on')

# change background colors
def bgcolor_switch(tag):
    if tag == 'Black':
        cmd.do('bg_color black')
    elif tag == 'White':
        cmd.do('bg_color white')
    elif tag == 'Grey':
        cmd.do('bg_color grey')
    elif tag == 'Other':
        color = askcolor(parent = int, title = "Background Color Chooser")
        colorArray = []
        if color[0] != None:
            list = color[0]
            print list
            for each in list:
                z = (each/255.0)
                val = repr(z)
                colorArray.append(val)
            cmd.set_color('newcolor', colorArray)
            cmd.do('bg_color newcolor')
    else:
             do_nothing()

# change the color space
def cspace_switch(tag):
    if tag == 'PyMOL':
        cmd.space('pymol')
    elif tag == 'Publications':
        cmd.space('rgb')
    else:
        cmd.space('cmyk')

# hide/show interface
def hide_interface(tag):
    if tag == 'Show':
        cmd.set('internal_gui', '1')
    else:
        cmd.set('internal_gui', '0')
# Show/Hide Water
def show_hide_water(tag):
    if tag == 'Show':
        cmd.show('(resn HOH)')
        cmd.show('spheres', '(resn HOH)')
    else:
        cmd.hide('(resn HOH)')
def ambient_update(event):#----Go to here
    cmd.set("ambient", asca.get())