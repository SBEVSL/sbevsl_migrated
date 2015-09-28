from pymol import cmd
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.visual import *
from tkMessageBox import showinfo
import Pmw
Pmw.initialise()

def premovie(tag):
    if tag == 'Build Protein':
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

def rotate_y():
    cmd.mset()
    cmd.mset('1', '180')
    cmd.util.mroll('1', '180', '1')
    cmd.mplay()
cmd.extend('rotate', rotate_y)


# Movie to show locations of each of the chains in the molecule
#does not run on external pdbs - Brett
def highlight_chains():
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    glb.update()

    colors = ['blue', 'orange', 'silver', 'green', 'yellow',
                     'purple', 'brightorange', 'lightblue', 'lightorange',
                     'pink', 'forest', 'firebrick', 'paleyellow', 'salmon',
                     'ruby', 'wheat', 'lightmagenta', 'nitblue']
    
    chains = []
    numChains = 0
    objects = cmd.get_names('all')
    for obj in objects:
        split = obj.split('Chain-')
        if len(split) == 2:
            chains.append(split[1])
            numChains += 1
    numFrames = (numChains*200)+70
    cmd.mset('1', numFrames)
    cmd.mdo(1,'color red, all; hide cartoon, all')
    cmd.orient()
    cmd.mview('store', '1')
    
    colorCount = 0
    frameCount = 1

    for i in chains:
        cmd.orient('chain ' + i)
        cmd.mview('store', frameCount+59)
        cmd.mview('store', frameCount+115)
        flash_chain(i, frameCount+59, 'red', colors[colorCount])
        cmd.orient()
        cmd.turn('x', '270')
        cmd.turn('y', '180')
        cmd.mview('store', frameCount+150)
        cmd.mview('store', frameCount+170)
        colorCount += 1
        frameCount += 200
        if(frameCount > numFrames-100):
            cmd.orient()
        cmd.mdo(numFrames,'mstop')
    cmd.mview('store', (numChains*200)+70)
    cmd.mview('interpolate')
    cmd.show('ribbon')
    cmd.color('red', 'all')
cmd.extend('highlight_chains', highlight_chains)

# flash the chains on and off, eventually changing the color
# (utilized by the highlight_chains method)
def flash_chain(chainID, frame, initialColor, afterColor):
     cmd.mdo(frame, 'show cartoon, chain %s'%chainID)
     cmd.mdo(frame+7, 'color %s, chain %s'%(afterColor,chainID))
     cmd.mdo(frame+14, 'color %s, chain %s'%(initialColor,chainID))
     cmd.mdo(frame+21, 'color %s, chain %s'%(afterColor,chainID))
     cmd.mdo(frame+28, 'color %s, chain %s'%(initialColor,chainID))
     cmd.mdo(frame+35, 'color %s, chain %s'%(afterColor,chainID))
     cmd.mdo(frame+42, 'color %s, chain %s'%(initialColor,chainID))
     cmd.mdo(frame+49, 'color %s, chain %s'%(afterColor,chainID))

def growProtein():
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    
    glb.update()
    
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
            glb.procolor('dna','sticks','cpk',None)
        
        if 'rna' in objects:
            glb.procolor('rna','sticks','cpk',None)
        
        # coloring the protein and secondary structures
        cmd.color('white', 'protein')
        cmd.color('purple', 'helix')
        cmd.color('teal', 'sheets')
        
        cmd.cartoon('loop', 'protein')
        cmd.cartoon('automatic', 'helix')
        cmd.cartoon('automatic', 'sheets')
        cmd.hide('all')
        cmd.show('cartoon', 'protein')
        
        #cmd.mdo(1,'hide cartoon, helix; hide cartoon, sheets;')
        cmd.util.mrock('2', '200', '90', '1', '1')
        cmd.mdo(201,'show cartoon, helix;')
        cmd.util.mrock('202', '400', '90', '1', '1')
        cmd.mdo(401,'show cartoon, sheets;')
        cmd.util.mrock('402', '600', '90', '1', '1')
        if 'ligands' in objects:
            cmd.color('hotpink', 'ligands')
            cmd.mdo(600, 'show spheres, ligands; show sticks, ligands;'+
                ' set sphere_transparency = 0.5, ligands;')
        cmd.util.mroll('601', '800', '1', axis = "x")
        cmd.color('blue', 'surface')
        cmd.mview('store', '800')
        cmd.turn('z', 180)
        cmd.mview('store' , '1000')
        cmd.turn('z', 180)
        cmd.mdo(800, 'show surface, surface; '+
            'set transparency = 0.8, surface;')
        cmd.mdo(850,'set transparency = 0.7, surface;')
        cmd.mdo(900,'set transparency = 0.6, surface;')
        cmd.mdo(950,'set transparency = 0.5, surface;')
        cmd.mdo(1000,'set transparency = 0.4, surface;')
        cmd.mdo(1050,'set transparency = 0.3, surface;')
        cmd.mdo(1100,'set transparency = 0.2, surface;')
        cmd.mdo(1150,'set transparency = 0.1, surface;')
        cmd.mdo(1200,'set transparency = 0.0, surface;')
        cmd.mview('store', '1200')
        cmd.util.mrock('1201', '1399', '180', '1', '1')
        cmd.hide('everything', 'surface')
        cmd.hide('everything', 'helix')
        cmd.hide('everything', 'sheets')
        cmd.reset()
        cmd.orient()
        cmd.mdo(1400,'hide everything, all; show cartoon, protein;')
        cmd.mdo(1400,'mstop')
        cmd.mview('interpolate')
        cmd.rewind()
cmd.extend('build_protein', growProtein)

def surface_cartoon():
    glb.update()
    cmd.mstop()
    cmd.mclear()
    cmd.mset('1', '60')
    cmd.hide('everything')
    objects = cmd.get_names('all')
    glb.procolor(None,show_all=('cartoon','surface'))
    cmd.set("cartoon_fancy_helices", "1")
    cmd.set("cartoon_fancy_sheets", "1")
    cmd.mdo(1,'set transparency = 0.75, all;')
    cmd.mdo(2,'set transparency = 0.7, all;')
    cmd.mdo(3,'set transparency = 0.65, all;')
    cmd.mdo(4,'set transparency = 0.6, all;')
    cmd.mdo(5,'set transparency = 0.55, all;')
    cmd.mdo(6,'set transparency = 0.5, all;')
    cmd.mdo(7,'set transparency = 0.45, all;')
    cmd.mdo(8,'set transparency = 0.4, all;')
    cmd.mdo(9,'set transparency = 0.35, all;')
    cmd.mdo(10,'set transparency = 0.3, all;')
    cmd.mdo(11,'set transparency = 0.25, all;')
    cmd.mdo(12,'set transparency = 0.2, all;')
    cmd.mdo(13,'set transparency = 0.15, all;')
    cmd.mdo(14,'set transparency = 0.1, all;')
    cmd.mdo(15,'set transparency = 0.05, all;')
    cmd.mdo(16,'set transparency = 0, all;')
    cmd.mdo(17,'set transparency = 0, all;')
    cmd.mdo(19,'set transparency = 0, all;')
    cmd.mdo(20,'set transparency = 0, all;')
    cmd.mdo(21,'set transparency = 0, all;')
    cmd.mdo(22,'set transparency = 0, all;')
    cmd.mdo(23,'set transparency = 0, all;')
    cmd.mdo(24,'set transparency = 0, all;')
    cmd.mdo(25,'set transparency = 0, all;')
    cmd.mdo(26,'set transparency = 0, all;')
    cmd.mdo(27,'set transparency = 0, all;')
    cmd.mdo(28,'set transparency = 0, all;')
    cmd.mdo(29,'set transparency = 0.05, all;')
    cmd.mdo(30,'set transparency = 0.1, all;')
    cmd.mdo(31,'set transparency = 0.15, all;')
    cmd.mdo(32,'set transparency = 0.2, all;')
    cmd.mdo(33,'set transparency = 0.25, all;')
    cmd.mdo(34,'set transparency = 0.3, all;')
    cmd.mdo(35,'set transparency = 0.35, all;')
    cmd.mdo(36,'set transparency = 0.4, all;')
    cmd.mdo(37,'set transparency = 0.45, all;')
    cmd.mdo(38,'set transparency = 0.5, all;')
    cmd.mdo(39,'set transparency = 0.55, all;')
    cmd.mdo(40,'set transparency = 0.6, all;')
    cmd.mdo(41,'set transparency = 0.65, all;')
    cmd.mdo(42,'set transparency = 0.7, all;')
    cmd.mdo(43,'set transparency = 0.75, all;')
    cmd.mdo(44,'set transparency = 0.8, all;')
    cmd.mdo(45,'set transparency = 0.85, all;')
    cmd.mdo(46,'set transparency = 0.9, all;')
    cmd.mdo(47,'set transparency = 0.9, all;')
    cmd.mdo(48,'set transparency = 0.9, all;')
    cmd.mdo(49,'set transparency = 0.85, all;')
    cmd.mdo(50,'set transparency = 0.85, all;')
    cmd.mdo(51,'set transparency = 0.85, all;')
    cmd.mdo(52,'set transparency = 0.85, all;')
    cmd.mdo(53,'set transparency = 0.85, all;')
    cmd.mdo(54,'set transparency = 0.85, all;')
    cmd.mdo(55,'set transparency = 0.85, all;')
    cmd.mdo(56,'set transparency = 0.85, all;')
    cmd.mdo(57,'set transparency = 0.85, all;')
    cmd.mdo(58,'set transparency = 0.85, all;')
    cmd.mdo(59,'set transparency = 0.85, all;')
    cmd.mdo(60,'set transparency = 0.8, all;')
cmd.extend('surface_cartoon', surface_cartoon)
    
def surface_stick():
    '''surface over stick movie'''
    glb.update()
    cmd.mstop()
    cmd.mclear()
    cmd.mset()
    cmd.mset('1', '60')
    glb.procolor(None,show_all=('sticks','surface'))
    cmd.mdo(1,'set transparency = 0.75, all;')
    cmd.mdo(2,'set transparency = 0.7, all;')
    cmd.mdo(3,'set transparency = 0.65, all;')
    cmd.mdo(4,'set transparency = 0.6, all;')
    cmd.mdo(5,'set transparency = 0.55, all;')
    cmd.mdo(6,'set transparency = 0.5, all;')
    cmd.mdo(7,'set transparency = 0.45, all;')
    cmd.mdo(8,'set transparency = 0.4, all;')
    cmd.mdo(9,'set transparency = 0.35, all;')
    cmd.mdo(10,'set transparency = 0.3, all;')
    cmd.mdo(11,'set transparency = 0.25, all;')
    cmd.mdo(12,'set transparency = 0.2, all;')
    cmd.mdo(13,'set transparency = 0.15, all;')
    cmd.mdo(14,'set transparency = 0.1, all;')
    cmd.mdo(15,'set transparency = 0.05, all;')
    cmd.mdo(16,'set transparency = 0, all;')
    cmd.mdo(17,'set transparency = 0, all;')
    cmd.mdo(19,'set transparency = 0, all;')
    cmd.mdo(20,'set transparency = 0, all;')
    cmd.mdo(21,'set transparency = 0, all;')
    cmd.mdo(22,'set transparency = 0, all;')
    cmd.mdo(23,'set transparency = 0, all;')
    cmd.mdo(24,'set transparency = 0, all;')
    cmd.mdo(25,'set transparency = 0, all;')
    cmd.mdo(26,'set transparency = 0, all;')
    cmd.mdo(27,'set transparency = 0, all;')
    cmd.mdo(28,'set transparency = 0, all;')
    cmd.mdo(29,'set transparency = 0.05, all;')
    cmd.mdo(30,'set transparency = 0.1, all;')
    cmd.mdo(31,'set transparency = 0.15, all;')
    cmd.mdo(32,'set transparency = 0.2, all;')
    cmd.mdo(33,'set transparency = 0.25, all;')
    cmd.mdo(34,'set transparency = 0.3, all;')
    cmd.mdo(35,'set transparency = 0.35, all;')
    cmd.mdo(36,'set transparency = 0.4, all;')
    cmd.mdo(37,'set transparency = 0.45, all;')
    cmd.mdo(38,'set transparency = 0.5, all;')
    cmd.mdo(39,'set transparency = 0.55, all;')
    cmd.mdo(40,'set transparency = 0.6, all;')
    cmd.mdo(41,'set transparency = 0.65, all;')
    cmd.mdo(42,'set transparency = 0.7, all;')
    cmd.mdo(43,'set transparency = 0.75, all;')
    cmd.mdo(44,'set transparency = 0.8, all;')
    cmd.mdo(45,'set transparency = 0.85, all;')
    cmd.mdo(46,'set transparency = 0.9, all;')
    cmd.mdo(47,'set transparency = 0.9, all;')
    cmd.mdo(48,'set transparency = 0.9, all;')
    cmd.mdo(49,'set transparency = 0.85, all;')
    cmd.mdo(50,'set transparency = 0.85, all;')
    cmd.mdo(51,'set transparency = 0.85, all;')
    cmd.mdo(52,'set transparency = 0.85, all;')
    cmd.mdo(53,'set transparency = 0.85, all;')
    cmd.mdo(54,'set transparency = 0.85, all;')
    cmd.mdo(55,'set transparency = 0.85, all;')
    cmd.mdo(56,'set transparency = 0.85, all;')
    cmd.mdo(57,'set transparency = 0.85, all;')
    cmd.mdo(58,'set transparency = 0.85, all;')
    cmd.mdo(59,'set transparency = 0.85, all;')
    cmd.mdo(60,'set transparency = 0.8, all;')
cmd.extend('surface_stick', surface_stick)
    
    
    #movie that pulls ligands out of    and puts them back in
def Ligand_Pull():
    glb.update()
    cmd.mstop()
    cmd.mclear()
    cmd.mset('1', '442')
    cmd.hide('everything')
    cmd.remove('resn HOH')
    cmd.color('green', 'all')
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        cmd.set('stick_radius', '0.3')
        glb.procolor('ligands around 6','sticks','cpk','cartoon')
        glb.procolor('ligands','spheres','orange',None)
        cmd.set("cartoon_fancy_helices", "1")
        cmd.set("cartoon_fancy_sheets", "1")
        cmd.set('cartoon_transparency', '0.5')
        cmd.zoom()
        cmd.orient()
        cmd.mdo(1,'orient')
        cmd.mdo(2,'translate [2,0,0],ligands;')
        cmd.mdo(3,'translate [2,0,0],ligands;')
        cmd.mdo(4,'translate [2,0,0],ligands;')
        cmd.mdo(5,'translate [2,0,0],ligands;')
        cmd.mdo(6,'translate [2,0,0],ligands;')
        cmd.mdo(7,'translate [2,0,0],ligands;')
        cmd.mdo(8,'translate [2,0,0],ligands;')
        cmd.mdo(9,'translate [2,0,0],ligands;')
        cmd.mdo(10,'translate [2,0,0],ligands;')
        cmd.mdo(11,'translate [2,0,0],ligands;')
        cmd.mdo(12,'translate [2,0,0],ligands;')
        cmd.mdo(13,'translate [2,0,0],ligands;')
        cmd.mdo(14,'translate [2,0,0],ligands;')
        cmd.mdo(15,'translate [2,0,0],ligands;')
        cmd.mdo(16,'translate [2,0,0],ligands;')
        cmd.mdo(17,'translate [2,0,0],ligands;')
        cmd.mdo(18,'translate [2,0,0],ligands;')
        cmd.mdo(19,'translate [2,0,0],ligands;')
        cmd.mdo(20,'translate [2,0,0],ligands;')
        cmd.mdo(21,'translate [2,0,0],ligands;')
        cmd.mdo(22,'translate [2,0,0],ligands;')
        cmd.mdo(23,'translate [2,0,0],ligands;')
        cmd.mdo(24,'translate [2,0,0],ligands;')
        cmd.mdo(25,'translate [2,0,0],ligands;')
        cmd.mdo(26,'translate [2,0,0],ligands;')
        cmd.mdo(27,'translate [2,0,0],ligands;')
        cmd.mdo(28,'translate [2,0,0],ligands;')
        cmd.mdo(29,'translate [2,0,0],ligands;')
        cmd.mdo(30,'translate [2,0,0],ligands;')
        cmd.mdo(31,'translate [2,0,0],ligands;')
        cmd.mdo(32,'translate [2,0,0],ligands;')
        cmd.mdo(33,'translate [2,0,0],ligands;')
        cmd.mdo(34,'translate [2,0,0],ligands;')
        cmd.mdo(35,'translate [2,0,0],ligands;')
        cmd.mdo(36,'translate [2,0,0],ligands;')
        cmd.mdo(37,'translate [2,0,0],ligands;')
        cmd.mdo(38,'translate [2,0,0],ligands;')
        cmd.mdo(39,'translate [2,0,0],ligands;')
        cmd.mdo(40,'translate [2,0,0],ligands;')
        cmd.mdo(41,'translate [2,0,0],ligands;')
        cmd.mdo(42,'orient')
        cmd.util.mroll('42','222','1')
        cmd.mdo(223,'translate [-2,0,0],ligands;')
        cmd.mdo(224,'translate [-2,0,0],ligands;')
        cmd.mdo(225,'translate [-2,0,0],ligands;')
        cmd.mdo(226,'translate [-2,0,0],ligands;')
        cmd.mdo(227,'translate [-2,0,0],ligands;')
        cmd.mdo(228,'translate [-2,0,0],ligands;')
        cmd.mdo(229,'translate [-2,0,0],ligands;')
        cmd.mdo(230,'translate [-2,0,0],ligands;')
        cmd.mdo(231,'translate [-2,0,0],ligands;')
        cmd.mdo(232,'translate [-2,0,0],ligands;')
        cmd.mdo(233,'translate [-2,0,0],ligands;')
        cmd.mdo(234,'translate [-2,0,0],ligands;')
        cmd.mdo(235,'translate [-2,0,0],ligands;')
        cmd.mdo(236,'translate [-2,0,0],ligands;')
        cmd.mdo(237,'translate [-2,0,0],ligands;')
        cmd.mdo(238,'translate [-2,0,0],ligands;')
        cmd.mdo(239,'translate [-2,0,0],ligands;')
        cmd.mdo(240,'translate [-2,0,0],ligands;')
        cmd.mdo(241,'translate [-2,0,0],ligands;')
        cmd.mdo(242,'translate [-2,0,0],ligands;')
        cmd.mdo(243,'translate [-2,0,0],ligands;')
        cmd.mdo(244,'translate [-2,0,0],ligands;')
        cmd.mdo(245,'translate [-2,0,0],ligands;')
        cmd.mdo(246,'translate [-2,0,0],ligands;')
        cmd.mdo(247,'translate [-2,0,0],ligands;')
        cmd.mdo(248,'translate [-2,0,0],ligands;')
        cmd.mdo(249,'translate [-2,0,0],ligands;')
        cmd.mdo(250,'translate [-2,0,0],ligands;')
        cmd.mdo(251,'translate [-2,0,0],ligands;')
        cmd.mdo(252,'translate [-2,0,0],ligands;')
        cmd.mdo(253,'translate [-2,0,0],ligands;')
        cmd.mdo(254,'translate [-2,0,0],ligands;')
        cmd.mdo(255,'translate [-2,0,0],ligands;')
        cmd.mdo(256,'translate [-2,0,0],ligands;')
        cmd.mdo(257,'translate [-2,0,0],ligands;')
        cmd.mdo(258,'translate [-2,0,0],ligands;')
        cmd.mdo(259,'translate [-2,0,0],ligands;')
        cmd.mdo(260,'translate [-2,0,0],ligands;')
        cmd.mdo(261,'translate [-2,0,0],ligands;')
        cmd.mdo(262,'translate [-2,0,0],ligands;')
        cmd.mdo(263,'orient')
        cmd.util.mroll('264','442','1')
    else:
        showinfo('No ligands','There are no ligands in this PDB.')
cmd.extend('ligand_pull',Ligand_Pull)


def chain_pull():
   cmd.mstop
   cmd.mclear
   coor = { 2:'[0,0,0]',      3:'[75,0,0]',     4:'[0,75,0]',
            5:'[0,0,75]',     6:'[-75,0,0]',    7:'[0,-75,0]',
            8:'[0,0,-75]',    9:'[75,75,0]',   10:'[-75,-75,0]',
           11:'[0,75,75]',   12:'[0,-75,-75]', 13:'[75,0,75]',
           14:'[-75,0,-75]', 15:'[75,75,75]',  16:'[-75,-75,-75]',
           17:'[75,-75,0]',  18:'[-75,75,0]',  19:'[0,75,-75]',
           20:'[0,-75,75]',  21:'[75,0,-75]',  22:'[-75,0,75]',
           23:'[75,75,-75]', 24:'[75,-75,75]', 25:'[-75,75,75]',
           26:'[-75,-75,75]',27:'[75,-75,-75]',28:'[-75,-75,-75]'}
   chainPullList = chain_contact()
   if chainPullList == False:
       return False
   chainPullLen = len(chainPullList)
   frames = 1+chainPullLen+172+chainPullLen+172
   cmd.mset('1','%s'%frames)

   i = chainPullLen+2
   for h in range(2,i):
       print 'translate %s,%s'%(coor[h],chainPullList[h-2])
       cmd.mdo(h,'translate %s,%s'%(coor[h],chainPullList[h-2]))
   cmd.mdo(i,'zoom all')
   util.mroll(i+1,i+171,1)
   i += 172
   for g in range(i,chainPullLen+i):
       c = coor[(g-i)+2].replace('7','-7').replace('--','-')
       cmd.mdo(g,'translate %s,%s'%(c,chainPullList[g-i]))
   g = chainPullLen+i
   cmd.mdo(g,'zoom all')
   util.mroll(g+1,g+171,1)
   
cmd.extend('chain_pull', chain_pull)

#movie controls
def play():
    cmd.mplay()

def stop():
    cmd.mstop()

def rewind():
    cmd.mstop()
    cmd.rewind()
 
 #Ray Trace Frames
def do_ray( r, state):
     
     if state:
         if askyesno('Ray Trace Frames', 'Enabling this feature may '+
                      'slow own the playback of your movie significantly. '+
                      'Are you sure that you want to proceed?'):
             cmd.set('ray_trace_frames', '1')
         else:
             ray.invoke('Ray Trace Frames')
     else:
         cmd.set('ray_trace_frames', '0')

def cacheframe( r, state):
    if state:
        cmd.set('cache_frames', '0')
    else:
        cmd.set('cache_frames', '1')

# loadframe isn't being used by anything except movie_maker which was removed.
# There is a question as to whether calling askopenfilename without importing it
# will fail.  Anyway, it references movie_maker, which is gone, so it would have
# already failed in Maddy's version anyway.
# Those reasons are why we commented it out.
#def loadframe(event):
#    file = askopenfilename(defaultextension=entfilex.get(), initialdir=glb.HOME)
#    if len(file)>0:
#        cmd.load(file, "mov", entl.get())
#    glb.GUI.movie_maker['tab'].mainloop()
    
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
        cmd.mset("1 -%s"%fent.get())
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
