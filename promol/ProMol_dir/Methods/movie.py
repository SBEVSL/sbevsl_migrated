from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
Pmw.initialise()

def rotate_y(*args):
    cmd.mset()
    cmd.mset('1', '180')
    cmd.util.mroll('1', '180', '1')
    cmd.mplay()
cmd.extend('rotate', rotate_y)


# Movie to show locations of each of the chains in the molecule
#does not run on external pdbs - Brett
def highlight_chains(*args):
    
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    update()

    colors = ['blue', 'orange', 'silver', 'green', 'yellow',
                     'purple', 'brightorange', 'lightblue', 'lightorange',
                     'pink', 'forest', 'firebrick', 'paleyellow', 'salmon',
                     'ruby', 'wheat', 'lightmagenta', 'nitblue']
    
    numChains = len(self.p.chains)
    numFrames = (numChains*200)+70
    cmd.mset('1', numFrames)
    cmd.do('mdo 1: color red, all; hide cartoon, all')
    cmd.orient()
    cmd.mview('store', '1')
    
    colorCount = 0
    frameCount = 1
    '''CHECK THIS'''
    for i in self.p.chains.keys():
        cmd.orient('chain ' + i)
        cmd.mview('store', frameCount+59)
        cmd.mview('store', frameCount+115)
        self.flash_chain(i, frameCount+59, 'red', colors[colorCount])
        cmd.orient()
        cmd.turn('x', '270')
        cmd.turn('y', '180')
        cmd.mview('store', frameCount+150)
        cmd.mview('store', frameCount+170)
        colorCount += 1
        frameCount += 200
        if(frameCount > numFrames-100):
            cmd.orient()
        cmd.do('mdo '+str(numFrames)+': mstop')
    cmd.mview('store', (numChains*200)+70)
    cmd.mview('interpolate')
    cmd.show('ribbon')
    #cmd.show('surface')
    cmd.color('red', 'all')
    #cmd.set('transparency', '0.75', 'all')
    #cmd.set('cartoon_transparency', '0.0', 'all')
cmd.extend('highlight_chains', highlight_chains)

# flash the chains on and off, eventually changing the color
# (utilized by the highlight_chains method)
def flash_chain(self, chainID, frame, initialColor, afterColor):
     cmd.do('mdo ' + str(frame)+': show cartoon, chain ' + str(chainID))
     cmd.do('mdo '+str(frame+7)+': color '+afterColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+14)+': color '+initialColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+21)+': color '+afterColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+28)+': color '+initialColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+35)+': color '+afterColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+42)+': color '+initialColor+', chain '+
        str(chainID))
     cmd.do('mdo '+str(frame+49)+': color '+afterColor+', chain '+
        str(chainID))

#does not run on external pdbs
def ligandZoom(self):
    try:
        cmd.mstop()
        cmd.mclear()
        cmd.mset()
        q = 360
        ids = self.p.idList
        if len(ids) == 0:
            showinfo("Ligand Zoom", "This PDB file contains no ligands")
        else:
            objects = cmd.get_names('all')
            update()
            ids.sort()
            numFrames = 600+(335*(len(ids)))
            cmd.deselect()
            cmd.do('bg_color white')
            cmd.cartoon('tube', 'all')
            cmd.mset('1', numFrames)
            cmd.do('mdo 1: show cartoon, all; hide cartoon, resn a+t+c+g;'+
                ' show sticks, resn a+t+c+g;')
            cmd.reset()
            cmd.do('turn x, 180')
            cmd.orient()
            cmd.mview('store', '1')
            cmd.do('turn y, 180')
            cmd.mview('store', '120')
            cmd.mview('store', '150')
            cmd.do('turn y, 180')
            cmd.mview('store', '240')
            cmd.mview('store', '270')
            for i in range(len(ids)):
                color_cpk(' and (byres (ligands and '+ids[i]+')around 5)')
                color_cpk(' and ligands')
                cmd.orient('(ligands and '+ids[i]+')around 7')
                cmd.mview('store', str(q))
                cmd.do('mdo '+str((q+1))+':set sphere_transparency, 0.1, '+
                    'ligands; set cartoon_transparency, 0.9, all; '+
                    'show spheres, (ligands and '+ids[i]+'); '+
                    'show sticks, (ligands and '+ids[i]+');')
                cmd.mview('store', str(q+10))
                cmd.do('mdo '+str((q+11))+':set sphere_transparency, 0.2,'+
                    ' ligands;')
                cmd.mview('store', str(q+20))
                cmd.do('mdo '+str((q+21))+':set sphere_transparency, 0.3,'+
                    ' ligands;')
                cmd.mview('store', str(q+30))
                cmd.do('mdo '+str((q+31))+':set sphere_transparency, 0.4,'+
                    ' ligands;')
                cmd.mview('store', str(q+40))
                cmd.do('mdo '+str((q+41))+':set sphere_transparency, 0.5,'+
                    ' ligands;')
                cmd.mview('store', str(q+50))
                cmd.do('mdo '+str((q+51))+':show sticks, '+
                    '(byres (ligands and '+ids[i]+')around 1);')
                cmd.mview('store', str(q+60))
                cmd.do('mdo '+str((q+61))+':show sticks, '+
                    '(byres (ligands and '+ids[i]+')around 2);')
                cmd.mview('store', str(q+70))
                cmd.do('mdo '+str((q+71))+':show sticks, '+
                    '(byres (ligands and '+ids[i]+')around 3);')
                cmd.mview('store', str(q+80))
                cmd.do('mdo '+str((q+81))+':show sticks, '+
                    '(byres (ligands and '+ids[i]+')around 4);')
                cmd.mview('store', str(q+81))
                cmd.do('turn y, 180')
                cmd.mview('store', str(q+125))
                cmd.mview('store', str(q+150))
                cmd.do('mdo '+str((q+151))+
                    ': set cartoon_transparency, 0, all;')
                cmd.reset()
                cmd.orient()
                cmd.mview('store', str(q+215))
                cmd.mview('store', str(q+255))
                if i == (len(ids)-1):
                    cmd.reset()
                    cmd.orient()
                    cmd.do('turn x, 180')
                    cmd.mview('store', str(numFrames))
                else:
                    cmd.mview('store', str(q+335))
                    q = q+335
            
            cmd.do('mdo '+str(numFrames)+': hide spheres, ligands; '+
                'hide sticks, ligands around 4; label ligands, \' \'')
            cmd.do('mdo '+str(numFrames)+': mstop')
            cmd.mview('interpolate')
            cmd.rewind()
    except:
        showinfo('Error', 'You must open the PDB file through Pro-MOL')

cmd.extend('ligand_zoom', ligandZoom)
 #fixed to work on externally loaded pdbs by Brett and Charlie
def growProtein(*args):
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    
    try:
        self = args[0]
        update()
    except:
        pass
    
    objects = cmd.get_names('all')
    
    if 'protein' in objects:
        
        cmd.bg_color('black')
        
        # create the objects to be used in this movie
        cmd.create('helix', 'ss h and protein')
        cmd.create('sheets', 'ss s and protein')
        cmd.create('surface', objects[0])
        
        cmd.mset('1', '1400')
        
        # dna and rna will be represented as sticks
        # to make them stand out from the protein
        if 'dna' in objects:
            cmd.show('sticks', 'dna')
            cpknucleic()
        
        if 'rna' in objects:
            cmd.show('sticks', 'rna')
            cmd.show('spheres', 'rna')
            cmd.set('sphere_scale', '0.4', 'rna')
            color_cpk(' & rna')
        
        # coloring the protein and secondary structures
        cmd.color('white', 'protein')
        cmd.color('purple', 'helix')
        cmd.color('teal', 'sheets')
        
        cmd.cartoon('loop', 'protein')
        cmd.cartoon('automatic', 'helix')
        cmd.cartoon('automatic', 'sheets')
        cmd.show('cartoon', 'protein')

        
        
        #cmd.do('mdo 1: hide cartoon, helix; hide cartoon, sheets;')
        cmd.util.mrock('2', '200', '90', '1', '1')
        cmd.do('mdo 201: show cartoon, helix;')
        cmd.util.mrock('202', '400', '90', '1', '1')
        cmd.do('mdo 401: show cartoon, sheets;')
        cmd.util.mrock('402', '600', '90', '1', '1')
        if 'ligands' in objects:
            cmd.color('hotpink', 'ligands')
            cmd.do('mdo 600: show spheres, ligands; show sticks, ligands;'+
                ' set sphere_transparency = 0.5, ligands;')
        cmd.util.mroll('601', '800', '1', axis = "x")
        cmd.color('blue', 'surface')
        cmd.mview('store', '800')
        cmd.do('turn z, 180')
        cmd.mview('store' , '1000')
        cmd.do('turn z, 180')
        cmd.do('mdo 800: show surface, surface; '+
            'set transparency = 0.8, surface;')
        cmd.do('mdo 850: set transparency = 0.7, surface;')
        cmd.do('mdo 900: set transparency = 0.6, surface;')
        cmd.do('mdo 950: set transparency = 0.5, surface;')
        cmd.do('mdo 1000: set transparency = 0.4, surface;')
        cmd.do('mdo 1050: set transparency = 0.3, surface;')
        cmd.do('mdo 1100: set transparency = 0.2, surface;')
        cmd.do('mdo 1150: set transparency = 0.1, surface;')
        cmd.do('mdo 1200: set transparency = 0.0, surface;')
        cmd.mview('store', '1200')
        cmd.util.mrock('1201', '1399', '180', '1', '1')
        cmd.hide('everything', 'surface')
        cmd.hide('everything', 'helix')
        cmd.hide('everything', 'sheets')
        cmd.reset()
        cmd.orient()
        cmd.do('mdo 1400: hide everything, all; show cartoon, protein;')
        cmd.do('mdo 1400: mstop')
        cmd.mview('interpolate')
        cmd.rewind()
cmd.extend('build_protein', growProtein)


    
    
    #---------Version 2--------#

#--------Haven't you seeen my MOVIES!-----------
#surface over cartoon movie
def surface_cartoon(*args):
    
    try:
        self = args[0]
        update()
    except:
        pass
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    cmd.mset('1', '60')
    cmd.hide('everything')
    objects = cmd.get_names('all')
    cmd.create('surface', 'all')
    cmd.create('cartoon', 'all')
    cmd.show('cartoon', 'cartoon')
    cmd.show('surface', 'surface')
    cmd.color('grey', 'surface')
    cmd.color('red', 'elem O')
    cmd.color('blue', 'elem N')
    cmd.set("cartoon_fancy_helices", "1")
    cmd.set("cartoon_fancy_sheets", "1")
    cmd.do('mdo 1: set transparency = 0.75, surface;')
    cmd.do('mdo 2: set transparency = 0.7, surface;')
    cmd.do('mdo 3: set transparency = 0.65, surface;')
    cmd.do('mdo 4: set transparency = 0.6, surface;')
    cmd.do('mdo 5: set transparency = 0.55, surface;')
    cmd.do('mdo 6: set transparency = 0.5, surface;')
    cmd.do('mdo 7: set transparency = 0.45, surface;')
    cmd.do('mdo 8: set transparency = 0.4, surface;')
    cmd.do('mdo 9: set transparency = 0.35, surface;')
    cmd.do('mdo 10: set transparency = 0.3, surface;')
    cmd.do('mdo 11: set transparency = 0.25, surface;')
    cmd.do('mdo 12: set transparency = 0.2, surface;')
    cmd.do('mdo 13: set transparency = 0.15, surface;')
    cmd.do('mdo 14: set transparency = 0.1, surface;')
    cmd.do('mdo 15: set transparency = 0.05, surface;')
    cmd.do('mdo 16: set transparency = 0, surface;')
    cmd.do('mdo 17: set transparency = 0, surface;')
    cmd.do('mdo 19: set transparency = 0, surface;')
    cmd.do('mdo 20: set transparency = 0, surface;')
    cmd.do('mdo 21: set transparency = 0, surface;')
    cmd.do('mdo 22: set transparency = 0, surface;')
    cmd.do('mdo 23: set transparency = 0, surface;')
    cmd.do('mdo 24: set transparency = 0, surface;')
    cmd.do('mdo 25: set transparency = 0, surface;')
    cmd.do('mdo 26: set transparency = 0, surface;')
    cmd.do('mdo 27: set transparency = 0, surface;')
    cmd.do('mdo 28: set transparency = 0, surface;')
    cmd.do('mdo 29: set transparency = 0.05, surface;')
    cmd.do('mdo 30: set transparency = 0.1, surface;')
    cmd.do('mdo 31: set transparency = 0.15, surface;')
    cmd.do('mdo 32: set transparency = 0.2, surface;')
    cmd.do('mdo 33: set transparency = 0.25, surface;')
    cmd.do('mdo 34: set transparency = 0.3, surface;')
    cmd.do('mdo 35: set transparency = 0.35, surface;')
    cmd.do('mdo 36: set transparency = 0.4, surface;')
    cmd.do('mdo 37: set transparency = 0.45, surface;')
    cmd.do('mdo 38: set transparency = 0.5, surface;')
    cmd.do('mdo 39: set transparency = 0.55, surface;')
    cmd.do('mdo 40: set transparency = 0.6, surface;')
    cmd.do('mdo 41: set transparency = 0.65, surface;')
    cmd.do('mdo 42: set transparency = 0.7, surface;')
    cmd.do('mdo 43: set transparency = 0.75, surface;')
    cmd.do('mdo 44: set transparency = 0.8, surface;')
    cmd.do('mdo 45: set transparency = 0.85, surface;')
    cmd.do('mdo 46: set transparency = 0.9, surface;')
    cmd.do('mdo 47: set transparency = 0.9, surface;')
    cmd.do('mdo 48: set transparency = 0.9, surface;')
    cmd.do('mdo 49: set transparency = 0.85, surface;')
    cmd.do('mdo 50: set transparency = 0.85, surface;')
    cmd.do('mdo 51: set transparency = 0.85, surface;')
    cmd.do('mdo 52: set transparency = 0.85, surface;')
    cmd.do('mdo 53: set transparency = 0.85, surface;')
    cmd.do('mdo 54: set transparency = 0.85, surface;')
    cmd.do('mdo 55: set transparency = 0.85, surface;')
    cmd.do('mdo 56: set transparency = 0.85, surface;')
    cmd.do('mdo 57: set transparency = 0.85, surface;')
    cmd.do('mdo 58: set transparency = 0.85, surface;')
    cmd.do('mdo 59: set transparency = 0.85, surface;')
    cmd.do('mdo 60: set transparency = 0.8, surface;')
cmd.extend('surface_cartoon', surface_cartoon)
    
    #surface over stick movie
def surface_stick(*args):
    
    try:
        self = args[0]
        update()
    except:
        pass
    cmd.mstop()
    cmd.mclear()
    cmd.mset('1', '60')
    cmd.hide('everything')
    objects = cmd.get_names('all')
    cmd.create('surface', 'all')
    cmd.create('sticks', 'all')
    cmd.show('sticks', 'sticks')
    color_cpk('& sticks')
    cmd.show('surface', 'surface')
    cmd.color('grey', 'surface')
    cmd.color('red', 'elem O')
    cmd.color('blue', 'elem N')
    cmd.do('mdo 1: set transparency = 0.75, surface;')
    cmd.do('mdo 2: set transparency = 0.7, surface;')
    cmd.do('mdo 3: set transparency = 0.65, surface;')
    cmd.do('mdo 4: set transparency = 0.6, surface;')
    cmd.do('mdo 5: set transparency = 0.55, surface;')
    cmd.do('mdo 6: set transparency = 0.5, surface;')
    cmd.do('mdo 7: set transparency = 0.45, surface;')
    cmd.do('mdo 8: set transparency = 0.4, surface;')
    cmd.do('mdo 9: set transparency = 0.35, surface;')
    cmd.do('mdo 10: set transparency = 0.3, surface;')
    cmd.do('mdo 11: set transparency = 0.25, surface;')
    cmd.do('mdo 12: set transparency = 0.2, surface;')
    cmd.do('mdo 13: set transparency = 0.15, surface;')
    cmd.do('mdo 14: set transparency = 0.1, surface;')
    cmd.do('mdo 15: set transparency = 0.05, surface;')
    cmd.do('mdo 16: set transparency = 0, surface;')
    cmd.do('mdo 17: set transparency = 0, surface;')
    cmd.do('mdo 19: set transparency = 0, surface;')
    cmd.do('mdo 20: set transparency = 0, surface;')
    cmd.do('mdo 21: set transparency = 0, surface;')
    cmd.do('mdo 22: set transparency = 0, surface;')
    cmd.do('mdo 23: set transparency = 0, surface;')
    cmd.do('mdo 24: set transparency = 0, surface;')
    cmd.do('mdo 25: set transparency = 0, surface;')
    cmd.do('mdo 26: set transparency = 0, surface;')
    cmd.do('mdo 27: set transparency = 0, surface;')
    cmd.do('mdo 28: set transparency = 0, surface;')
    cmd.do('mdo 29: set transparency = 0.05, surface;')
    cmd.do('mdo 30: set transparency = 0.1, surface;')
    cmd.do('mdo 31: set transparency = 0.15, surface;')
    cmd.do('mdo 32: set transparency = 0.2, surface;')
    cmd.do('mdo 33: set transparency = 0.25, surface;')
    cmd.do('mdo 34: set transparency = 0.3, surface;')
    cmd.do('mdo 35: set transparency = 0.35, surface;')
    cmd.do('mdo 36: set transparency = 0.4, surface;')
    cmd.do('mdo 37: set transparency = 0.45, surface;')
    cmd.do('mdo 38: set transparency = 0.5, surface;')
    cmd.do('mdo 39: set transparency = 0.55, surface;')
    cmd.do('mdo 40: set transparency = 0.6, surface;')
    cmd.do('mdo 41: set transparency = 0.65, surface;')
    cmd.do('mdo 42: set transparency = 0.7, surface;')
    cmd.do('mdo 43: set transparency = 0.75, surface;')
    cmd.do('mdo 44: set transparency = 0.8, surface;')
    cmd.do('mdo 45: set transparency = 0.85, surface;')
    cmd.do('mdo 46: set transparency = 0.9, surface;')
    cmd.do('mdo 47: set transparency = 0.9, surface;')
    cmd.do('mdo 48: set transparency = 0.9, surface;')
    cmd.do('mdo 49: set transparency = 0.85, surface;')
    cmd.do('mdo 50: set transparency = 0.85, surface;')
    cmd.do('mdo 51: set transparency = 0.85, surface;')
    cmd.do('mdo 52: set transparency = 0.85, surface;')
    cmd.do('mdo 53: set transparency = 0.85, surface;')
    cmd.do('mdo 54: set transparency = 0.85, surface;')
    cmd.do('mdo 55: set transparency = 0.85, surface;')
    cmd.do('mdo 56: set transparency = 0.85, surface;')
    cmd.do('mdo 57: set transparency = 0.85, surface;')
    cmd.do('mdo 58: set transparency = 0.85, surface;')
    cmd.do('mdo 59: set transparency = 0.85, surface;')
    cmd.do('mdo 60: set transparency = 0.8, surface;')
cmd.extend('surface_stick', surface_stick)
    
    
    #movie that pulls ligands out of    and puts them back in
def Ligand_Pull(*args):
    try:
        update()
    except:
        pass
    cmd.mstop()
    cmd.mclear()
    cmd.mset('1', '442')
    cmd.hide('everything')
    cmd.remove('resn HOH')
    cmd.color('green', 'all')
    objects = cmd.get_names('all')
    cmd.select('Bad', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+'+
        'BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c'+
        '+t+u+HOH+MSE')
    cmd.select("ligand", "!Bad")
    cmd.hide("everything", "ligand")
    cmd.show("spheres", "ligand")
    cmd.show("sticks", "ligand around 6'")
    cmd.set('stick_radius', '0.3', 'ligand around 6')
    cmd.color('orange', 'ligand')
    cmd.select("interaction", "ligand around 6'")
    cpkinteraction()
    cmd.delete('interaction')
    cmd.delete("Bad")
    cmd.show('cartoon', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+'+
        'HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+'+
        'BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c'+
        '+t+u+HOH+MSE')
    cmd.set("cartoon_fancy_helices", "1")
    cmd.set("cartoon_fancy_sheets", "1")
    cmd.set('cartoon_transparency', '0.5')
    cmd.zoom()
    cmd.orient()
    cmd.do('mdo 1: orient')
    cmd.do('mdo 2: translate [2,0,0],ligand;')
    cmd.do('mdo 3: translate [2,0,0],ligand;')
    cmd.do('mdo 4: translate [2,0,0],ligand;')
    cmd.do('mdo 5: translate [2,0,0],ligand;')
    cmd.do('mdo 6: translate [2,0,0],ligand;')
    cmd.do('mdo 7: translate [2,0,0],ligand;')
    cmd.do('mdo 8: translate [2,0,0],ligand;')
    cmd.do('mdo 9: translate [2,0,0],ligand;')
    cmd.do('mdo 10: translate [2,0,0],ligand;')
    cmd.do('mdo 11: translate [2,0,0],ligand;')
    cmd.do('mdo 12: translate [2,0,0],ligand;')
    cmd.do('mdo 13: translate [2,0,0],ligand;')
    cmd.do('mdo 14: translate [2,0,0],ligand;')
    cmd.do('mdo 15: translate [2,0,0],ligand;')
    cmd.do('mdo 16: translate [2,0,0],ligand;')
    cmd.do('mdo 17: translate [2,0,0],ligand;')
    cmd.do('mdo 18: translate [2,0,0],ligand;')
    cmd.do('mdo 19: translate [2,0,0],ligand;')
    cmd.do('mdo 20: translate [2,0,0],ligand;')
    cmd.do('mdo 21: translate [2,0,0],ligand;')
    cmd.do('mdo 22: translate [2,0,0],ligand;')
    cmd.do('mdo 23: translate [2,0,0],ligand;')
    cmd.do('mdo 24: translate [2,0,0],ligand;')
    cmd.do('mdo 25: translate [2,0,0],ligand;')
    cmd.do('mdo 26: translate [2,0,0],ligand;')
    cmd.do('mdo 27: translate [2,0,0],ligand;')
    cmd.do('mdo 28: translate [2,0,0],ligand;')
    cmd.do('mdo 29: translate [2,0,0],ligand;')
    cmd.do('mdo 30: translate [2,0,0],ligand;')
    cmd.do('mdo 31: translate [2,0,0],ligand;')
    cmd.do('mdo 32: translate [2,0,0],ligand;')
    cmd.do('mdo 33: translate [2,0,0],ligand;')
    cmd.do('mdo 34: translate [2,0,0],ligand;')
    cmd.do('mdo 35: translate [2,0,0],ligand;')
    cmd.do('mdo 36: translate [2,0,0],ligand;')
    cmd.do('mdo 37: translate [2,0,0],ligand;')
    cmd.do('mdo 38: translate [2,0,0],ligand;')
    cmd.do('mdo 39: translate [2,0,0],ligand;')
    cmd.do('mdo 40: translate [2,0,0],ligand;')
    cmd.do('mdo 41: translate [2,0,0],ligand;')
    cmd.do('mdo 42: orient')
    cmd.util.mroll('42','222','1')
    cmd.do('mdo 223: translate [-2,0,0],ligand;')
    cmd.do('mdo 224: translate [-2,0,0],ligand;')
    cmd.do('mdo 225: translate [-2,0,0],ligand;')
    cmd.do('mdo 226: translate [-2,0,0],ligand;')
    cmd.do('mdo 227: translate [-2,0,0],ligand;')
    cmd.do('mdo 228: translate [-2,0,0],ligand;')
    cmd.do('mdo 229: translate [-2,0,0],ligand;')
    cmd.do('mdo 230: translate [-2,0,0],ligand;')
    cmd.do('mdo 231: translate [-2,0,0],ligand;')
    cmd.do('mdo 232: translate [-2,0,0],ligand;')
    cmd.do('mdo 233: translate [-2,0,0],ligand;')
    cmd.do('mdo 234: translate [-2,0,0],ligand;')
    cmd.do('mdo 235: translate [-2,0,0],ligand;')
    cmd.do('mdo 236: translate [-2,0,0],ligand;')
    cmd.do('mdo 237: translate [-2,0,0],ligand;')
    cmd.do('mdo 238: translate [-2,0,0],ligand;')
    cmd.do('mdo 239: translate [-2,0,0],ligand;')
    cmd.do('mdo 240: translate [-2,0,0],ligand;')
    cmd.do('mdo 241: translate [-2,0,0],ligand;')
    cmd.do('mdo 242: translate [-2,0,0],ligand;')
    cmd.do('mdo 243: translate [-2,0,0],ligand;')
    cmd.do('mdo 244: translate [-2,0,0],ligand;')
    cmd.do('mdo 245: translate [-2,0,0],ligand;')
    cmd.do('mdo 246: translate [-2,0,0],ligand;')
    cmd.do('mdo 247: translate [-2,0,0],ligand;')
    cmd.do('mdo 248: translate [-2,0,0],ligand;')
    cmd.do('mdo 249: translate [-2,0,0],ligand;')
    cmd.do('mdo 250: translate [-2,0,0],ligand;')
    cmd.do('mdo 251: translate [-2,0,0],ligand;')
    cmd.do('mdo 252: translate [-2,0,0],ligand;')
    cmd.do('mdo 253: translate [-2,0,0],ligand;')
    cmd.do('mdo 254: translate [-2,0,0],ligand;')
    cmd.do('mdo 255: translate [-2,0,0],ligand;')
    cmd.do('mdo 256: translate [-2,0,0],ligand;')
    cmd.do('mdo 257: translate [-2,0,0],ligand;')
    cmd.do('mdo 258: translate [-2,0,0],ligand;')
    cmd.do('mdo 259: translate [-2,0,0],ligand;')
    cmd.do('mdo 260: translate [-2,0,0],ligand;')
    cmd.do('mdo 261: translate [-2,0,0],ligand;')
    cmd.do('mdo 262: translate [-2,0,0],ligand;')
    cmd.do('mdo 263: orient')
    cmd.util.mroll('264','442','1')
cmd.extend('ligand_pull',Ligand_Pull)


#movie that pulls protein chains apart and shows interaction, then puts them together again
def chain_pull(*args):
    try:
        self = args[0]
        update()
    except:
        pass
    cmd.mstop()
    cmd.mclear()
    cmd.mset('1', '373')
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
        cmd.do('mdo 2: translate [0,0,0],'+chainpulllist[0]+';')
        cmd.do('mdo 3: translate [50,0,0],'+chainpulllist[1]+';')
        cmd.do('mdo 183: translate [0,0,0],'+chainpulllist[0]+';')
        cmd.do('mdo 184: translate [-50,0,0],'+chainpulllist[1]+'; zoom all;')
    if len(chainpulllist) >2:
        cmd.do('mdo 4: translate [0,50,0],'+chainpulllist[2]+';')
        cmd.do('mdo 185: translate [0,-50,0],'+chainpulllist[2]+'; zoom all;')
    if len(chainpulllist) >3:
        cmd.do('mdo 5: translate [0,0,50],'+chainpulllist[3]+';')
        cmd.do('mdo 186: translate [0,0,-50],'+chainpulllist[3]+'; zoom all;')
    if len(chainpulllist) >4:
        cmd.do('mdo 6: translate [-50,0,0],'+chainpulllist[4]+';')
        cmd.do('mdo 187: translate [50,0,0],'+chainpulllist[4]+'; zoom all;')
    if len(chainpulllist) >5:
        cmd.do('mdo 7: translate [0,-50,0],'+chainpulllist[5]+';')
        cmd.do('mdo 188: translate [0,50,0],'+chainpulllist[5]+'; zoom all;')
    if len(chainpulllist) >6:
        cmd.do('mdo 8: translate [0,-50,0],'+chainpulllist[5]+';')
        cmd.do('mdo 189: translate [0,0,50],'+chainpulllist[6]+'; zoom all;')
    if len(chainpulllist) >7:
        cmd.do('mdo 9: translate [0,0,-50],'+chainpulllist[6]+';')
        cmd.do('mdo 190: translate [50,0,-50],'+chainpulllist[7]+'; zoom all;')
    if len(chainpulllist) >8:
        cmd.do('mdo 10: translate [-50,0,50],'+chainpulllist[7]+';')
        cmd.do('mdo 191: translate [-50,0,-50],'+chainpulllist[8]+'; zoom all;')
    if len(chainpulllist) >9:
        cmd.do('mdo 11: translate [50,0,50],'+chainpulllist[8]+';')
        cmd.do('mdo 192: translate [50,0,50],'+chainpulllist[9]+'; zoom all;')    
    if len(chainpulllist) >10:
        cmd.do('mdo 12: translate [50,0,-50],'+chainpulllist[10]+';')
        cmd.do('mdo 193: translate [-50,0,50],'+chainpulllist[10]+'; zoom all;')
    cmd.do('mdo 13: zoom all')
    cmd.util.mroll('14', '181', '1')
    cmd.util.mroll('194', '373', '1')

cmd.extend('chain_pull', chain_pull)

#movie controls
def play(self):
    cmd.mplay()

def stop(self):
    cmd.mstop()

def rewind(self):
    cmd.mstop()
    cmd.rewind()
 
 #Ray Trace Frames
def do_ray(self, r, state):
     
     if state:
         if askyesno('Ray Trace Frames', 'Enabling this feature may '+
                      'slow own the playback of your movie significantly. '+
                      'Are you sure that you want to proceed?'):
             cmd.set('ray_trace_frames', '1')
         else:
             self.ray.invoke('Ray Trace Frames')
     else:
         cmd.set('ray_trace_frames', '0')

def cacheframe(self, r, state):
    if state:
        cmd.set('cache_frames', '0')
    else:
        cmd.set('cache_frames', '1')

def loadframe(event):
    a = int(entl.get()) + 1
    entl.delete(0,100000)
    entl.insert(0,a)
    if int(entl.get())<2:
        if askyesno('Load Frames', 'Click yes to load in discrete mode'):
            file = askopenfilename(defaultextension=entfilex.get(), initialdir=pglob.pathmaker('Movies',name_mov.get()))
            if len(file) > 0:
                cmd.load(file, "mov", entl.get(), discrete=1)
        else:
            file = askopenfilename(defaultextension=entfilex.get(), initialdir=pglob.pathmaker('Movies',name_mov.get()))
            if len(file)>0:
                cmd.load(file, "mov", entl.get())
    else:
        file = askopenfilename(defaultextension=entfilex.get(), initialdir=pglob.pathmaker('Movies',name_mov.get()))
        if len(file)>0:
            cmd.load(file, "mov", entl.get())
    pglob.Tabs['movie_maker']['tab'].mainloop()
    
def gotoframe(event):
    try:
        cmd.frame(gotoent.get())
    except:

        showinfo('Alert!', 'You need to enter the frame number')
        interior.mainloop()

def mping(event):
    cmd.mpng(name_mov.get(), first=0, last=0 )

def clearram(event):
    cmd.mclear()
    
def makmovie(event):
    try:
        cmd.mset("1 -"+ fent.get())
        scriptent.delete(0,100000000)
        scriptent.insert(0,0)
    except:
        showinfo('Alert!', 'Enter the amount of frames to be in the movie')
        interior.mainloop()
        
def movsetx(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "move x," + entmx.get())
def movsety(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "move y," + entmy.get())
def movsetz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "move z," + entmz.get())
def tursetx(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "turn x," + enttx.get())
def tursety(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "turn y," + entty.get())
def tursetz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "turn z," + enttz.get())
def tursetz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(),  "turn z," + enttz.get())
def movsetxyz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(), "move x, %s; move y, %s; move z, %s" % (entmx.get(),entmy.get(),entmz.get()))
def tursetxyz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(), "turn x, %s; turn y, %s; turn z, %s" % (enttx.get(),entty.get(),enttz.get()))
def tursetxyzmovsetxyz(event):
    a = int(scriptent.get()) +1
    scriptent.delete(0,100000)
    scriptent.insert(0,a)
    cmd.mdo( scriptent.get(), "turn x, %s; turn y, %s; turn z, %s; move x, %s; move y, %s; move z, %s" % (enttx.get(),entty.get(),enttz.get(),entmx.get(),entmy.get(),entmz.get()))
     #------Masking and protecting functions, prevents manipulation-----
    #------of specified selections, although protect function not------
    #------well documented, and for advanced users only------------
def maskedman(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.mask(maskent.get())
    except:


        showinfo("Error", 'That object is not present')
    interior.mainloop()

def unmaskedman(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.unmask(maskent.get())
    except:


        showinfo("Error", 'That object is not present')
    interior.mainloop()
def maskallexcept(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.mask('All')
        cmd.unmask(maskent.get())
    except:


        showinfo("Error", 'That object is not present')
    interior.mainloop()
cmd.extend('maskallexcept',maskallexcept)
def protectallexcept(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.protect('All')
        cmd.deprotect(maskent.get())
    except:


        showinfo("Error", 'That object is not present')
    interior.mainloop()
def protectme(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.protect(maskent.get())
    except:


        showinfo("Error", 'That object is not present')
    interior.mainloop()
def deprotectme(event):
    try:
      if len(maskent.get()) < 1:


        showinfo("Error", 'Please enter the name of an object.')
        interior.mainloop()
      else:
        cmd.deprotect(maskent.get())
    except:
        showinfo("Error", 'That object is not present')
    interior.mainloop()