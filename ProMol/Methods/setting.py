from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
Pmw.initialise()

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

def ambient_update():
    cmd.set("ambient", glb.GUI.view['ambientLight'].get())

# Set Cartoon Thickness
def cartoon_thickness():
    glb.populate()
    value = glb.GUI.view['toonThickness'].get()
    cmd.set('cartoon_rect_width', value, glb.SELE) # strands
    cmd.set('cartoon_oval_width', value, glb.SELE) # helices

# Set Cartoon Width
def cartoon_width():
    glb.populate()
    value = glb.GUI.view['toonWidth'].get()
    cmd.set('cartoon_rect_length', value, glb.SELE) # strands
    cmd.set('cartoon_oval_length', value, glb.SELE) # helices

# Set Cartoon Transparency
def cartoon_transparency():
    glb.populate()
    amount = glb.GUI.view['cartoonTransparency'].get()
    cmd.set('cartoon_transparency', amount, glb.SELE)

# Set Cartoon Tube Radius
def cartoon_tube_radius():
    glb.populate()
    value = glb.GUI.view['toonTubeRadius'].get()
    cmd.set('cartoon_tube_radius', value, glb.SELE) # strands

#Set Ribbon Type
def ribType(tag):
    try:
        glb.populate()
        if tag == 'Skip':
            cmd.cartoon('skip', glb.SELE)
        elif tag == 'Automatic':
            cmd.cartoon('automatic', glb.SELE)
        elif tag == 'Oval':
            cmd.cartoon('oval', glb.SELE)
        elif tag == 'Tube':
            cmd.cartoon('tube', glb.SELE)
        elif tag == 'Rectangle':
            cmd.cartoon('rectangle', glb.SELE)
        elif tag == 'Loop':
            cmd.cartoon('loop', glb.SELE)
        elif tag == 'Arrow':
            cmd.cartoon('arrow', glb.SELE)
        elif tag == 'Dumbbell':
            cmd.cartoon('dumbbell', glb.SELE)
        elif tag == 'Putty':
            cmd.cartoon('putty', glb.SELE)
    except:
        showinfo('Error', 'Drop down menu is set to an invalid selection\n'+
            'You may need to update selections')

#------------------------------------------#
#                 Sphere Functions             #
#------------------------------------------#
# Set Sphere Transparency
def sphere_transparency():
    glb.populate()
    amount = glb.GUI.view['sphereTransparency'].get()
    cmd.set('sphere_transparency', amount, glb.SELE)

# Set Sphere Size
def sphereSize():
    glb.populate()
    size = glb.GUI.view['sphereScale'].get()
    cmd.set('sphere_scale', size, glb.SELE)

#------------------------------------------#
#                Surface    Functions            #
#------------------------------------------#
# Set Surface Transparency
def surface_transparency():
    glb.populate()
    amount = glb.GUI.view['surfaceTransparency'].get()
    cmd.set('transparency', amount, glb.SELE)

#------------------------------------------#
#                Stick    Functions            #
#------------------------------------------#
# Set Stick Transparency
def stick_transparency():
    glb.populate()
    amount = glb.GUI.view['stickTransparency'].get()
    cmd.set('stick_transparency', amount, glb.SELE)
 
 # Set Stick Radius
def stickRad():
    glb.populate()
    size = glb.GUI.view['stickRadius'].get()
    cmd.set('stick_radius', size, glb.SELE)
    
def setray0():
    cmd.set("ray_trace_mode", "0")
    cmd.ray()

def setray1():
    cmd.set("ray_trace_mode", "1")
    cmd.bg_color('white')
    cmd.ray()

def setray2():
    cmd.set("ray_trace_mode", "2")
    cmd.bg_color('white')
    cmd.ray()

def setray3():
    cmd.set("ray_trace_mode", "3")
    cmd.ray()

def orient():
    cmd.orient('all')

def setfield(var):
    cmd.set("field_of_view", var)
    
def turnorthon():
    cmd.set("orthoscopic", "on")

def turnorthoff():
    cmd.set("orthoscopic", "off")

def seqviewon(event):
    cmd.set('seq_view', 1)
def seqviewoff(event):
    cmd.set('seq_view', 0)

def seqviewformat(tag):
    if tag == 'One letter':
        cmd.set('seq_view_format', '0')
    elif tag == 'Three letter':
        cmd.set('seq_view_format', '1')
    elif tag == 'AA atoms':
        cmd.set('seq_view_format', '2')
    elif tag == 'Chains':
        cmd.set('seq_view_format', '3')
        
def emesh(*args):
    delcrea()
    try:
        cmd.isomesh('map1','map', contour1.get())
    except:
        try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isomesh("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.isomesh('map1','map', contour1.get())
            cmd.refresh()
        except: 
            showinfo("Error", 'No PDB is present')
            interior.mainloop()
cmd.extend('emesh',emesh)
def edot(*args):
    delcrea()
    try:
        cmd.isodot('map1','map', contour1.get())
    except:
        try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isodot("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.refresh()
            cmd.isodot('map1','map', contour1.get())
        except:
            showinfo("Error", 'No PDB is present')
            interior.mainloop()
cmd.extend('edot',edot)
def esurf(*args):
    delcrea()
    try:
        cmd.isosurface('map1','map', contour1.get())
    except:
        try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isosurface("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.refresh()
            cmd.isosurface('map1','map', contour1.get())
        except:
            showinfo("Error", 'No PDB is present')
            interior.mainloop()
cmd.extend('esurf',esurf)
def roving_density():
    delcrea()
    try:
        cmd.set("suspend_updates",1,quiet=1)
        cmd.remove("hydro")
        cmd.disable()
        cmd.enable('all')
        cmd.map_new('map',"gaussian","0.75", 'all')
        cmd.set('roving_isomesh', rovingradius1.get())
        cmd.set("roving_detail",1)
        cmd.set("stick_radius",0.5)
        cmd.set("roving_sticks",0)
        cmd.set('roving_lines', rovingradius1.get())
        cmd.set("roving_polar_contacts",0)
        cmd.set("line_width","3")
        cmd.set("roving_map1_name",'map')
        cmd.isomesh("map1", "map", 9999.0, 'all')
        cmd.set("suspend_updates",0,quiet=1)
        cmd.refresh()
        cmd.delete('rov_s1')
        cmd.set('roving_isosurface',0)
    except:
        showinfo("Error", 'No PDB is present')
        interior.mainloop()
cmd.extend('roving_density',roving_density)
def roving_surface():
    delcrea()
    try:

        cmd.remove("hydro")
        cmd.disable()
        cmd.enable('all')
        cmd.map_new('map',"gaussian","0.75", 'all')
        cmd.set("roving_detail",1)
        cmd.set("roving_origin",1)
        cmd.set('roving_lines', 8)
        cmd.set("roving_polar_contacts",0)
        cmd.set("line_width","3")
        cmd.set("roving_map1_name",'map')
        cmd.set('roving_isosurface', rovingradius1.get())
        cmd.show('lines', 'all')
        cmd.set('roving_isomesh', '0')
        cmd.set('transparency', '0.15')
        cmd.delete('rov_1')
        cmd.delete('rov_m1')
    except:
        showinfo("Error", 'No PDB is present')
        interior.mainloop()
def emesh1(event):
    delcrea()
    try:
        cmd.isomesh('map1','map', contour1.get(), 'sele')
    except:
        try:

            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isomesh('map1','map', contour1.get(), 'sele')

        except:
            cmd.orient('all')


            showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')

            interior.mainloop()
def edot1(event):
    delcrea()
    try:
        cmd.isodot('map1','map', contour1.get(), 'sele')
    except:
        try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isodot("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.refresh()
            cmd.isodot('map1','map', contour1.get(), 'sele')
            cmd.get_names('all')
        except:
            cmd.orient('all')

            showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
            interior.mainloop()
def esurf1(event):
    delcrea()
    try:
        cmd.isosurface('map1','map', contour1.get(), 'sele')
    except:
        try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.isosurface("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.refresh()
            cmd.isosurface('map1','map', contour1.get(), 'sele')
        except:
            cmd.orient('all')
            showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
            interior.mainloop()
def doublemapres(event):
    try:
        cmd.map_double('map', '1')
    except:
        showinfo("Error", 'No map is present')
        interior.mainloop()
def tv(event):
  cmd.mouse('three_button_viewing')
def te(event):
  cmd.mouse('three_button_editing')
def dv(event):
  cmd.mouse('two_button_viewing')
def ds(event):
  cmd.mouse('two_button_selecting')
def de(event):
  cmd.mouse('two_button_editing')
def ov(event):
  cmd.mouse('one_button_viewing')