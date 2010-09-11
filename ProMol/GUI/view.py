'''The view tab'''
import Tkinter as tk
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.setting import *
from pmg_tk.startup.ProMol.Methods.visual import *

def initialise():
    '''Start the view tab'''

    #-------------- Selection Dropdown -----------------
    tk.Label(glb.GUI.view['tab'], text='Select:').grid(row=0, column=0,
        sticky=tk.NE)
    glb.GUI.view['advanced_selection'] = tk.StringVar()
    glb.GUI.view['advanced_selection'].set('All')
    glb.GUI.view['advanced_selection_menu'] = tk.OptionMenu(glb.GUI.view['tab'],
        glb.GUI.view['advanced_selection'], 'All', 'Selected',
        'Not Selected', command=glb.set_selection)
    glb.GUI.view['advanced_selection_menu'].grid(row=0, column=1, sticky=tk.NW)
    
    tk.Button(glb.GUI.view['tab'], text='Update Selection',
        command=glb.populate).grid(row=0, column=2, sticky=tk.E)

    #--------------- Setting Defaults -----------------
    tk.Label(glb.GUI.view['tab'], text='Reset:').grid(row=0, column=4,
        sticky=tk.NE)
    defaults = tk.StringVar()
    defaults.set('Cartoon')
    defaults_menu = tk.OptionMenu(glb.GUI.view['tab'], defaults,
        'Cartoon', 'Spheres', 'Sticks', 'Surface', 'Ambient',
        command=glb.defaults)
    defaults_menu.grid(row=0, column=5, sticky=tk.NW)

    #--------------- Cartoon Group----------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Cartoon:')
    group.grid(row=1, column=0, padx=1, columnspan=3, pady=0, sticky=tk.NW)

    # Cartoon Width Slider
    tk.Label(group, text='Width').grid(row=0, column=0, padx=0, pady=0,
        sticky=tk.W)
    glb.GUI.view['toonWidth'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['toonWidth'].set(1.4)
    glb.GUI.view['toonWidth'].grid(row=0, column=1, padx=0, pady=0,
        sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=cartoon_width).grid(row=0, column=2, sticky=tk.SW, padx=2,
        pady=2)

    # Cartoon Thickness Slider
    tk.Label(group, text='Thickness').grid(row=1, column=0, padx=0, pady=0,
        sticky=tk.W)
    glb.GUI.view['toonThickness'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['toonThickness'].set(0.3)
    glb.GUI.view['toonThickness'].grid(row=1, column=1, padx=0, pady=0,
        sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=cartoon_thickness).grid(row=1, column=2, sticky=tk.SW, padx=2,
        pady=2)

    # Cartoon Transparency Slider
    tk.Label(group, text='Transparency').grid(row=2, column=0, padx=0, pady=0,
        sticky=tk.W)
    glb.GUI.view['cartoonTransparency'] = tk.Scale(group, width=8,
        length="65", troughcolor="#ffffff", orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['cartoonTransparency'].grid(row=2, column=1, padx=0,
        pady=0, sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10, 
        command=cartoon_transparency).grid(row=2, column=2, sticky=tk.SW, 
        padx=2, pady=2)

    # Cartoon Tube Radius Slider
    tk.Label(group, text='Tube Radius').grid(row=3, column=0, padx=0, pady=0,
        sticky=tk.W)
    glb.GUI.view['toonTubeRadius'] = Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['toonTubeRadius'].set(0.5)
    glb.GUI.view['toonTubeRadius'].grid(row=3, column=1, padx=0, pady=0,
        sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=cartoon_tube_radius).grid(row=3, column=2, sticky=tk.SW, padx=2,
        pady=2)
    
    ribbonTypes = StringVar()
    ribbonTypes.set('Automatic')
    ribbonTypes_menu = tk.OptionMenu (group, ribbonTypes, 'Automatic', 'Skip',
        'Loop', 'Rectangle', 'Oval', 'Tube', 'Arrow', 'Dumbbell', 'Putty',
        'Fancy helix', command=ribType)
    ribbonTypes_menu.grid(row=4, column=2, sticky=tk.SW)
    
    #-------------- Sphere Group--------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Spheres:')
    group.grid(row=1, column=3, columnspan=3, padx=1, pady=0, sticky=tk.NW)

    # Sphere Size Slider
    tk.Label(group, text='Size').grid(row=0, column=0, padx=0, pady=0,
        sticky=tk.E)
    glb.GUI.view['sphereScale'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['sphereScale'].set(0.7)
    glb.GUI.view['sphereScale'].grid(row=0, column=1, padx=0, pady=0,
        sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=sphereSize).grid(row=0, column=2, sticky=tk.SW, padx=2, pady=2)

    # Sphere Transparency Slider
    tk.Label(group, text='Transparency').grid(row=1, column=0, padx=0, pady=0,
        sticky=tk.E)
    glb.GUI.view['sphereTransparency'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['sphereTransparency'].grid(row=1, column=1, padx=0,
        pady=0, sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=sphere_transparency).grid(row=1, column=2, sticky=tk.SW, padx=2,
        pady=2)

    #--------------- Stick Group --------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Sticks:')
    group.grid(row=1, column=3, columnspan=3, padx=1, pady=0, sticky=tk.SW)

    # Stick Radius Slider
    tk.Label(group, text='Radius').grid(row=0, column=0, padx=0, pady=0,
        sticky=tk.E)
    glb.GUI.view['stickRadius'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="3.0")
    glb.GUI.view['stickRadius'].set(0.2)
    glb.GUI.view['stickRadius'].grid(row=0, column=1, padx=0, pady=0,
        sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10, 
        command=stickRad).grid(row=0, column=2, sticky=tk.SW, padx=2, pady=2)

    # Stick Transparency Slider
    tk.Label(group, text='Transparency').grid(row=1, column=0, padx=0, pady=0,
        sticky=tk.E)
    glb.GUI.view['stickTransparency'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['stickTransparency'].grid(row=1, column=1, padx=0,
        pady=0, sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=stick_transparency).grid(row=1, column=2, sticky=tk.SW, padx=2,
        pady=2)

    #-------------- Surface Group -------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Surface:')
    group.grid(row=2, column=3, columnspan=3, padx=1, pady=0, sticky=tk.SW)

    # Surface Transparency Slider
    tk.Label(group, text='Transparency').grid(row=2, column=0, padx=0, pady=0,
        sticky=tk.E)
    glb.GUI.view['surfaceTransparency'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['surfaceTransparency'].grid(row=2, column=1, padx=0,
        pady=0, sticky=tk.W)
    tk.Button(group, text='Update', highlightthickness=0, width=10,
        command=surface_transparency).grid(row=2, column=2, sticky=tk.SW,
        padx=2, pady=2)

    #----------Ambient Light Group----------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Ambient Light')
    group.grid(row=2, column=0, columnspan=3, padx=0, pady=0, sticky=tk.SW)
     #-----------------Ambient Light------------------------#
    tk.Label(group, text='Ambient Light').grid(row=0, column=0, padx=9, pady=0,
        sticky=tk.E)
    glb.GUI.view['asca'] = tk.Scale(group, width=8,
        troughcolor="#ffffff", length="65", orient="horizontal",
        resolution="0.01", to="2.0")
    glb.GUI.view['asca'].grid(row=0, column=1, padx=0, pady=0,
        sticky=tk.W)
    glb.GUI.view['asca'].set(.25)
    tk.Button(group, text='Update', command=ambient_update,
        width=10).grid(row=0, column=2, padx=0, pady=0, sticky=tk.SW)
