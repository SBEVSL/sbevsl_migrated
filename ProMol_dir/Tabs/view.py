from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.setting import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
from pmg_tk.startup.ProMol_dir.Methods.visual import *
Pmw.initialise()

def initialise():
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)
    interior = group.interior()

    popbtn = tk.Button(pglob.Tabs['view']['tab'], text='Update Selection')
    popbtn.grid(row = 0, column = 0, sticky = tk.E)
    popbtn.bind('<Button-1>', pglob.populate)


    #-------------- Selection Dropdown -----------------
    pglob.Tabs['view'].update({'advanced_selection':Pmw.OptionMenu(pglob.Tabs['view']['tab'],label_text = 'Select:',labelpos = tk.W,
                items = (''), menubutton_width = 10, command = set_sel1)})

    pglob.Tabs['view']['advanced_selection'].grid(row=0, column=0,sticky = tk.NW)

    #--------------- Setting Defaults -----------------
    defaults = Pmw.OptionMenu(pglob.Tabs['view']['tab'],label_text = 'Reset:',labelpos = tk.W,
                items = ('Cartoon', 'Spheres', 'Sticks','Surface', 'Ambient'),
                menubutton_width = 10, command=pglob.defaults)
    defaults.grid(row=0,column=1,sticky = tk.NW)

    #--------------- Cartoon Group----------------
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text='Cartoon:')
    group.grid(row=1, column=0, padx=1, pady=0, sticky = tk.NW)
    interior = group.interior()



    #----------------Version 2------------#


    # Cartoon Width Slider
    label3 = tk.Label(interior, text = 'Width')
    label3.grid(row=0, column=0, padx=0, pady=0, sticky = tk.W)
    toonWidth = Scale(interior, width =8)
    toonWidth.configure(troughcolor="#ffffff")
    toonWidth.configure(length="65")
    toonWidth.configure(orient="horizontal")
    toonWidth.configure(resolution="0.05")
    toonWidth.configure(to="2.0")
    toonWidth.set(1.4)
    toonWidth.grid(row=0, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,cartoon_width,0,2, tk.SW)


    # Cartoon Thickness Slider
    label4 = tk.Label(interior, text = 'Thickness')
    label4.grid(row=1, column=0, padx=0, pady=0, sticky = tk.W)
    toonThickness = tk.Scale(interior, width =8)
    toonThickness.configure(troughcolor="#ffffff")
    toonThickness.configure(length="65")
    toonThickness.configure(orient="horizontal")
    toonThickness.configure(resolution="0.05")
    toonThickness.configure(to="2.0")
    toonThickness.set(0.3)
    toonThickness.grid(row=1, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,cartoon_thickness,1,2, tk.SW)

    # Cartoon Transparency Slider
    label5 = tk.Label(interior, text = 'Transparency')
    label5.grid(row=2, column=0, padx=0, pady=0, sticky = tk.W)
    cartoonTransparency = tk.Scale(interior, width =8)
    cartoonTransparency.configure(length="65")
    cartoonTransparency.configure(troughcolor="#ffffff")
    cartoonTransparency.configure(orient="horizontal")
    cartoonTransparency.configure(resolution="0.05")
    cartoonTransparency.configure(to="1.0")
    cartoonTransparency.grid(row=2, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,cartoon_transparency,2,2, tk.SW)

    # Cartoon Tube Radius Slider
    label6 = tk.Label(interior, text = 'Tube Radius')
    label6.grid(row=3, column=0, padx=0, pady=0, sticky = tk.W)
    toonTubeRadius = Scale(interior, width =8)
    toonTubeRadius.configure(troughcolor="#ffffff")
    toonTubeRadius.configure(length="65")
    toonTubeRadius.configure(orient="horizontal")
    toonTubeRadius.configure(resolution="0.05")
    toonTubeRadius.configure(to="1.0")
    toonTubeRadius.set(0.5)
    toonTubeRadius.grid(row=3, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,cartoon_tube_radius,3,2, tk.SW)

    #----------------Ribbon Type Slider------------------
    ribbonTypes = Pmw.OptionMenu (interior,
            items = ('Automatic', 'Skip', 'Loop', 'Rectangle', 'Oval', 'Tube', 'Arrow', 'Dumbbell','Putty', 'Fancy helix'),
            menubutton_width = 7, command = ribType)
    ribbonTypes.grid(row=4,column=0,sticky= tk.SW)

    #-------------- Sphere Group--------------------
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text='Spheres:')
    group.grid(row=1, column=1, padx=1, pady=0, sticky = tk.NW)
    interior = group.interior()

    # Sphere Size Slider
    label1 = tk.Label(interior, text = 'Size')
    label1.grid(row=0, column=0, padx=0, pady=0, sticky = tk.E)
    sphereScale = tk.Scale(interior, width =8)
    sphereScale.configure(troughcolor="#ffffff")
    sphereScale.configure(length="65")
    sphereScale.configure(orient="horizontal")
    sphereScale.configure(resolution="0.05")
    sphereScale.configure(to="2.0")
    sphereScale.set(0.7)
    sphereScale.grid(row=0, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,sphereSize,0,2, tk.SW)

    # Sphere Transparency Slider
    label2 = tk.Label(interior, text = 'Transparency')
    label2.grid(row=1, column=0, padx=0, pady=0, sticky = tk.E)
    sphereTransparency = tk.Scale(interior, width =8)
    sphereTransparency.configure(troughcolor="#ffffff")
    sphereTransparency.configure(length="65")
    sphereTransparency.configure(orient="horizontal")
    sphereTransparency.configure(resolution="0.05")
    sphereTransparency.configure(to="1.0")
    sphereTransparency.grid(row=1, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,sphere_transparency,1,2, tk.SW)

    #--------------- Stick Group --------------------
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text='Sticks:')
    group.grid(row=1, column=1, padx=1, pady=0, sticky = tk.SW)
    interior = group.interior()

    # Stick Radius Slider
    label7 = tk.Label(interior, text = 'Radius')
    label7.grid(row=0, column=0, padx=0, pady=0, sticky = tk.E)
    stickRadius = tk.Scale(interior, width =8)
    stickRadius.configure(troughcolor="#ffffff")
    stickRadius.configure(length="65")
    stickRadius.configure(orient="horizontal")
    stickRadius.configure(resolution="0.05")
    stickRadius.configure(to="3.0")
    stickRadius.set(0.2)
    stickRadius.grid(row=0, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,stickRad,0,2, tk.SW)


    # Stick Transparency Slider
    label8 = tk.Label(interior, text = 'Transparency')
    label8.grid(row=1, column=0, padx=0, pady=0, sticky = tk.E)
    stickTransparency = tk.Scale(interior, width =8)
    stickTransparency.configure(troughcolor="#ffffff")
    stickTransparency.configure(length="65")
    stickTransparency.configure(orient="horizontal")
    stickTransparency.configure(resolution="0.05")
    stickTransparency.configure(to="1.0")
    stickTransparency.grid(row=1, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,stick_transparency,1,2, tk.SW)


    #-------------- Surface Group -------------------
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text='Surface:')
    group.grid(row=2, column=1, padx=1, pady=0, sticky = tk.SW)
    interior = group.interior()

    # Surface Transparency Slider
    label9 = tk.Label(interior, text = 'Transparency')
    label9.grid(row=2, column=0, padx=0, pady=0, sticky = tk.E)
    surfaceTransparency = tk.Scale(interior, width =8)
    surfaceTransparency.configure(troughcolor="#ffffff")
    surfaceTransparency.configure(length="65")
    surfaceTransparency.configure(orient="horizontal")
    surfaceTransparency.configure(resolution="0.05")
    surfaceTransparency.configure(to="1.0")
    surfaceTransparency.grid(row=2, column=1, padx=0, pady=0, sticky = tk.W)
    buttonAdd(interior,'Update',10,surface_transparency,2,2, tk.SW)


    #----------Ambient Light Group----------------------
    group = Pmw.Group(pglob.Tabs['view']['tab'], tag_text='Ambient Light')
    group.grid(row=2, column=0, padx=0, pady=0, sticky = tk.SW)
    interior = group.interior()
     #-----------------Ambient Light------------------------#
    lamb = tk.Label(interior, text = 'Ambient Light')
    lamb.grid(row=0, column=0, padx=9, pady=0, sticky = tk.E)
    frameasca = tk.Frame(interior)
    frameasca.grid(row=0, column=1, padx=0, pady=0, sticky = tk.W)
    ballasca = Pmw.Balloon(interior)
    ballasca.bind(frameasca, "Default ambient is .25")
    asca = tk.Scale(frameasca, width =8)
    asca.configure(troughcolor="#ffffff")
    asca.configure(length="65")
    asca.configure(orient="horizontal")
    asca.configure(resolution="0.01")
    asca.configure(to="2.0")
    asca.grid(row=0, column=1, padx=0, pady=0, sticky = tk.W)
    asca.set(.25)
    ambientupdate = tk.Button(interior, text = 'Update')
    ambientupdate.grid(row=0, column=2, padx=0, pady=0, sticky = tk.SW)
    ambientupdate.configure(width = 10)
    ambientupdate.pack
    ambientupdate.bind('<Button-1>', ambient_update)