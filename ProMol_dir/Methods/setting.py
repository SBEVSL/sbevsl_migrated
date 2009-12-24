from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
Pmw.initialise()

# Set Cartoon Thickness
def cartoon_thickness(self):
    self.populate()
    sel1 = ''
    value = self.toonThickness.get()
    cmd.set('cartoon_rect_width', value, 'all') # strands
    cmd.set('cartoon_oval_width', value, 'all') # helices


# Set Cartoon Width
def cartoon_width(self):
    self.populate()
    sel1 = ''
    value = self.toonWidth.get()
    cmd.set('cartoon_rect_length', value, 'all') # strands
    cmd.set('cartoon_oval_length', value, 'all') # helices

# Set Cartoon Transparency
def cartoon_transparency(self):
    self.populate()
    sel1 = ''
    amount = self.cartoonTransparency.get()
    cmd.set('cartoon_transparency', amount, 'all')

# Set Cartoon Tube Radius
def cartoon_tube_radius(self):
    self.populate()
    sel1 = ''
    value = self.toonTubeRadius.get()
    cmd.set('cartoon_tube_radius', value, 'all') # strands

#Set Ribbon Type
def ribType(self, tag):
    try:
        try:
            if tag == 'Skip':
                    cmd.cartoon('skip', sel1)
            elif tag == 'Automatic':
                    cmd.cartoon('automatic', sel1)
            elif tag == 'Oval':
                    cmd.cartoon('oval', sel1)
            elif tag == 'Tube':
                    cmd.cartoon('tube', sel1)
            elif tag == 'Rectangle':
                    cmd.cartoon('rectangle', sel1)
            elif tag == 'Loop':
                    cmd.cartoon('loop', sel1)
            elif tag == 'Arrow':
                    cmd.cartoon('arrow', sel1)
            elif tag == 'Dumbbell':
                    cmd.cartoon('dumbbell', sel1)
            elif tag == 'Putty':
                    cmd.cartoon('putty', sel1)
        except:
            self.populate()
            if tag == 'Skip':
                    cmd.cartoon('skip', sel1)
            elif tag == 'Automatic':
                    cmd.cartoon('automatic', sel1)
            elif tag == 'Oval':
                    cmd.cartoon('oval', sel1)
            elif tag == 'Tube':
                    cmd.cartoon('tube', sel1)
            elif tag == 'Rectangle':
                    cmd.cartoon('rectangle', sel1)
            elif tag == 'Loop':
                    cmd.cartoon('loop', sel1)
            elif tag == 'Arrow':
                    cmd.cartoon('arrow', sel1)
            elif tag == 'Dumbbell':
                    cmd.cartoon('dumbbell', sel1)
            elif tag == 'Putty':
                    cmd.cartoon('putty', sel1)
    except:
        showinfo('Error', 'Drop down menu is set to an invalid selection\n'+
            'You may need to update selections')

#------------------------------------------#
#                 Sphere Functions             #
#------------------------------------------#
# Set Sphere Transparency
def sphere_transparency(self):
    self.populate()
    sel1 = 'all'
    amount = self.sphereTransparency.get()
    cmd.set('sphere_transparency', amount, 'all')

# Set Sphere Size
def sphereSize(self):
    self.populate()
    sel1 = 'all'
    size = self.sphereScale.get()
    cmd.set('sphere_scale', size, 'all')

#------------------------------------------#
#                Surface    Functions            #
#------------------------------------------#
# Set Surface Transparency
def surface_transparency(self):
    self.populate()
    sel1 = 'all'
    amount = self.surfaceTransparency.get()
    cmd.set('transparency', amount, 'all')

#------------------------------------------#
#                Stick    Functions            #
#------------------------------------------#
# Set Stick Transparency
def stick_transparency(self):
    self.populate()
    sel1 = 'all'
    amount = self.stickTransparency.get()
    cmd.set('stick_transparency', amount, 'all')
 
 # Set Stick Radius
def stickRad(self):
    self.populate()
    sel1 = 'all'
    size = self.stickRadius.get()
    cmd.set('stick_radius', size, 'all')
    
def setray0(event):
    cmd.set("ray_trace_mode", "0")
    imgraysave()
def setray1(event):
    cmd.set("ray_trace_mode", "1")
    cmd.do('bg_color white')
    imgraysave()
def setray2(event):
    cmd.set("ray_trace_mode", "2")
    cmd.do('bg_color white')
    imgraysave()
def setray3(event):
    cmd.set("ray_trace_mode", "3")
    imgraysave()
def orient(event):
    cmd.orient('all')
def fullon(event):
    cmd.set("full_screen", '1')
    cmd.set('internal_gui','0')
def setfield(event):
    cmd.set("field_of_view", setfieldofview.get())
    
def turnorthon(event):
    cmd.set("orthoscopic", "on")
def turnorthoff(event):
    cmd.set("orthoscopic", "off")
    
def delelectro(event):
    try:
        cmd.select('goodbye',entelc.get()+'_e_chg')
        cmd.delete(entelc.get()+'_e_pot')
        cmd.delete(entelc.get()+'_e_chg')
        cmd.delete(entelc.get()+'_e_map')
        cmd.delete('goodbye')
        cmd.enable('all')
    except:
        cmd.delete('goodbye')
        cmd.delete(entelc.get()+'_e_pot')
        cmd.delete(entelc.get()+'_e_map')
        showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
        interior.mainloop()
def seq(event):
    try:
        util.protein_vacuum_esp(entelc.get(),mode=2,quiet=0)
    except:
        showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
        interior.mainloop()
        
#Defines Sculpting mode
def sculpt(*args):
    cmd.hide('everything')
    cmd.set('sphere_transparency',0.60)
    cmd.set('sphere_color','white')
    cmd.set('auto_sculpt',1)
    cmd.mouse('three_button_editing')
    cmd.show('sticks')
    cmd.show('spheres')
    cmd.zoom('all',4)
cmd.extend('sculpt',sculpt)

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
def roving_density(self):
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
def roving_surface(self):
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