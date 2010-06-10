from pymol import cmd, util
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from tkMessageBox import showinfo

def show_dna_rna():
    pglob.update()
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
    pglob.update()
    cmd.hide('all')
    objects = cmd.get_names('all')
    cmd.show('cartoon', 'protein')
    cmd.color("red", "ss h")
    cmd.color("yellow", "ss s")
    cmd.color("cyan", "ss l+\'\'")
    if 'ligands' in objects:
        pglob.procolor('lignads','spheres','orange',None)
    if 'dna' in objects:
        pglob.procolor('dna','sticks','cpk',None)
    if 'rna' in objects:
        pglob.procolor('rna','sticks','cpk',None)
    if cartoon == 'putty':
        try:
            cmd.cartoon('putty', 'protein')
        except:
            showinfo('Error', 'Putty is not supported by this version of PyMol')
    else:
        cmd.set('cartoon_ring_mode' , '1')

# show hetero atoms
def show_hetero():
    pglob.update()
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        if 'protein' in objects:
            cmd.show('cartoon', 'protein')
            cmd.set('cartoon_transparency', '0.7', 'protein')
        if 'dna' in objects:
            pglob.procolor('dna','sticks','cpk',None)
        if 'rna' in objects:
            pglob.procolor('rna','sticks','cpk',None)
        pglob.procolor('ligands around 6','sticks','cpk','cartoon')
        pglob.procolor('ligands','spheres','orange',None)
        cmd.set('sphere_transparency', '0.1', 'ligands')
        cmd.set('stick_radius', '0.3', 'ligands around 6')
        cmd.set('stick_transparency', '0.1', 'ligands around 6')
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
        pglob.procolor('protein',('spheres','sticks'),'cpk',None)
    if 'dna' in objects:
        pglob.procolor('dna',('sticks','cartoon','spheres'),'cpk',None)
    if 'rna' in objects:
        pglob.procolor('rna',('sticks','cartoon','spheres'),None)
    if 'ligands' in objects:
        pglob.procolor('ligands','spheres','oragne',None)
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
    cmd.show('cartoon', 'resn %s'%(pglob.DNASTR))
    pglob.procolor(pglob.DNASTR,'cartoon','cpk',None)
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
    cmd.show('cartoon', 'resn %s'%(pglob.DNASTR))
    cmd.color('aquamarine', 'resn %s'%(pglob.DNASTR))
    cmd.set('cartoon_transparency', '0.6', 'resn %s'%(pglob.DNASTR))
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

def stick_toon():
    pglob.update()
    cmd.hide('all')
    cmd.show('lines')
    cmd.create('cartoon', 'all')
    cmd.show('cartoon', 'cartoon')
    cmd.color('salmon', 'cartoon')
    cmd.color('cyan', 'resn a+t+u+g+c')
cmd.extend('stick_and_cartoon', stick_toon)

def rovingstickers():
    pglob.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("stick_radius", 0.3)
    cmd.set("roving_polar_contacts", 8)
    cmd.set("roving_sticks", pglob.Tabs['ez_viz']['roving'].get())
cmd.extend('roving_stick', rovingstickers)

def rovinglines():
    pglob.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_sticks", 0)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('roving_lines', pglob.Tabs['ez_viz']['roving'].get())
cmd.extend('roving_line', rovinglines)

def rovingspheres(): 
    pglob.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('sphere_transparency', '0.2')
    cmd.set('sphere_scale', '0.8', 'all')
    cmd.set('roving_spheres', pglob.Tabs['ez_viz']['roving'].get())
cmd.extend('roving_sphere', rovingspheres)

def rovingballstick():
    pglob.update()
    cmd.hide('everything')
    cmd.set("roving_detail", 1)
    cmd.set("roving_origin", 1)
    cmd.set("roving_polar_contacts", 8)
    cmd.set('sphere_transparency', '0.2')
    cmd.set("sphere_scale", "0.3", "all")
    cmd.set('roving_spheres', pglob.Tabs['ez_viz']['roving'].get())
    cmd.set("stick_radius", 0.3)
    cmd.set("roving_polar_contacts", 8)
    cmd.set("roving_sticks", pglob.Tabs['ez_viz']['roving'].get())
cmd.extend('roving_ballstick', rovingballstick)

def chain_contact():
    def chain_contact_loop(c,skip,chainPullList):
        d = 0
        l = c + 1
        while len(chainPullList) > l and (26-d) >= 0:
            cmd.do('sele chain_contact,'+chainPullList[d]+' w. 5 of '+
                    chainPullList[c+1]+',enable=0,quiet=1,merge=1')
            cmd.do('sele chain_contact,'+chainPullList[c+1]+' w. 5 of '+
                    chainPullList[d]+',enable=0,quiet=1,merge=1')
            d += 1
            l += 1
            while d == (c+1) or d in skip:
                d += 1
    pglob.update()
    cmd.hide('everything')
    cmd.show('mesh', 'all')
    cmd.color('gray40', 'all')
    objects = cmd.get_names('all')
    chainPullList = []
    for i in cmd.get_chains(quiet=1):
        if(i.islower()):
            chainPullList.append('Chain-'+i+i)
            continue
        chainPullList.append('Chain-'+i)
    c = 0
    skip = []
    while c < (len(chainPullList)-1) and c < 26:
        skip.append(c+1)
        chain_contact_loop(c,skip,chainPullList)
        c += 1
    pglob.procolor('chain_contact','mesh','cpk',None)
    cmd.do('delete chain_contact')
    return chainPullList
cmd.extend('chain_contact',chain_contact)
cmd.extend('chain_contact', chain_contact)

    #-----------Electron Density Presets----------------#

def mesh_ribbon():
    cmd.hide('everything')
    pglob.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    cmd.enable('map')
    pglob.procolor(None,show_all=('lines','ribbon'),color_all='red')
    cmd.isomesh('map1', 'map', '1')
    cmd.color('purple','map1')
cmd.extend('mesh_ribbon', mesh_ribbon)

def dot_sticks():
    cmd.hide('everything')
    pglob.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    cmd.enable('map')
    cmd.isodot("map1", "map", 9999.0, 'all')
    cmd.isodot('map1', 'map', '1')

def surfinglines():
    cmd.hide('everything')
    pglob.update()
    cmd.map_new('map', "gaussian", "0.75", 'all')
    cmd.enable('map')
    pglob.procolor(None,show_all='lines')
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
        cmd.do('show everything')
    else:
        cmd.do('hide everything')
        for item in list:
            rep1.invoke(item)
        for item in list2:
            rep2.invoke(item)

# Show individual representations
def show_rep(tag):
    print pglob.SELE
    try:
        sel = pglob.SELE
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
        sel = pglob.SELE
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
