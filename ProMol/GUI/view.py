'''The view tab'''
import Tkinter as tk
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.setting import *
from pmg_tk.startup.ProMol.Methods.visual import *

def initialise():
    '''Start the view tab'''

    #-------------- Selection Dropdown -----------------
    tk.Label(glb.GUI.view['tab'], text='Select:').grid(row=0, column=0,
        sticky=tk.E, pady=0)
    glb.GUI.view['advanced_selection'] = tk.StringVar()
    glb.GUI.view['advanced_selection'].set('All')
    glb.GUI.view['advanced_selection_menu'] = tk.OptionMenu(glb.GUI.view['tab'],
        glb.GUI.view['advanced_selection'], 'All', 'Selected',
        'Not Selected', command=glb.set_selection)
    glb.GUI.view['advanced_selection_menu'].grid(row=0, column=1, sticky=tk.W, pady=0)
    
    tk.Button(glb.GUI.view['tab'], text='Update Selection',
        command=glb.populate).grid(row=0, column=2, pady=0)

    #--------------- Setting Defaults -----------------
    tk.Label(glb.GUI.view['tab'], text='Reset:').grid(row=0, column=3,
        sticky=tk.E, pady=0)
    defaults = tk.StringVar()
    defaults.set('Cartoon')
    defaults_menu = tk.OptionMenu(glb.GUI.view['tab'], defaults,
        'Cartoon', 'Spheres', 'Sticks', 'Surface', 'Ambient',
        command=glb.defaults)
    defaults_menu.grid(row=0, column=4, sticky=tk.W, pady=0)

    #--------------- Cartoon Group----------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Cartoon')
    group.grid(row=1, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W, pady=0)

    # Cartoon Width Slider
    tk.Label(group, text='Width').grid(row=0, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['toonWidth'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['toonWidth'].set(1.4)
    glb.GUI.view['toonWidth'].grid(row=0, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=cartoon_width).grid(row=0, column=2, sticky=tk.S, pady=0)

    # Cartoon Thickness Slider
    tk.Label(group, text='Thickness').grid(row=0, column=3, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['toonThickness'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['toonThickness'].set(0.3)
    glb.GUI.view['toonThickness'].grid(row=0, column=4, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=cartoon_thickness).grid(row=0, column=5, sticky=tk.S, pady=0)

    # Cartoon Transparency Slider
    tk.Label(group, text='Transparency').grid(row=1, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['cartoonTransparency'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['cartoonTransparency'].grid(row=1, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=cartoon_transparency).grid(row=1, column=2, sticky=tk.S, pady=0)

    # Cartoon Tube Radius Slider
    tk.Label(group, text='Tube Radius').grid(row=1, column=3, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['toonTubeRadius'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['toonTubeRadius'].set(0.5)
    glb.GUI.view['toonTubeRadius'].grid(row=1, column=4, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=cartoon_tube_radius).grid(row=1, column=5, sticky=tk.S, pady=0)
    
    tk.Label(group, text='Ribbon Type').grid(row=2, column=0, sticky=tk.E+tk.S, pady=0)
    ribbonTypes = StringVar()
    ribbonTypes.set('Automatic')
    ribbonTypes_menu = tk.OptionMenu (group, ribbonTypes, 'Automatic', 'Skip',
        'Loop', 'Rectangle', 'Oval', 'Tube', 'Arrow', 'Dumbbell', 'Putty',
        'Fancy helix', command=ribType)
    ribbonTypes_menu.grid(row=2, column=1, columnspan=2, sticky=tk.E+tk.W+tk.S, pady=0)
    
    group.columnconfigure(1, weight=1)
    group.columnconfigure(4, weight=1)
    group.rowconfigure(0, weight=1)
    group.rowconfigure(1, weight=1)
    group.rowconfigure(2, weight=1)
    
    #-------------- Sphere Group--------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Spheres')
    group.grid(row=2, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W, pady=0)

    # Sphere Size Slider
    tk.Label(group, text='Size').grid(row=0, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['sphereScale'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="2.0")
    glb.GUI.view['sphereScale'].set(0.7)
    glb.GUI.view['sphereScale'].grid(row=0, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=sphereSize).grid(row=0, column=2, sticky=tk.S, pady=0)

    # Sphere Transparency Slider
    tk.Label(group, text='Transparency').grid(row=0, column=3, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['sphereTransparency'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['sphereTransparency'].grid(row=0, column=4, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=sphere_transparency).grid(row=0, column=5, sticky=tk.S, pady=0)

    group.rowconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.columnconfigure(4, weight=1)
    
    #--------------- Stick Group --------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Sticks')
    group.grid(row=3, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W, pady=0)

    # Stick Radius Slider
    tk.Label(group, text='Radius').grid(row=0, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['stickRadius'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="3.0")
    glb.GUI.view['stickRadius'].set(0.2)
    glb.GUI.view['stickRadius'].grid(row=0, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=stickRad).grid(row=0, column=2, sticky=tk.S, pady=0)

    # Stick Transparency Slider
    tk.Label(group, text='Transparency').grid(row=0, column=3, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['stickTransparency'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['stickTransparency'].grid(row=0, column=4, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=stick_transparency).grid(row=0, column=5, sticky=tk.S, pady=0)

    group.rowconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.columnconfigure(4, weight=1)
    
    #-------------- Surface Group -------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Surface')
    group.grid(row=4, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W, pady=0)

    # Surface Transparency Slider
    tk.Label(group, text='Transparency').grid(row=0, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['surfaceTransparency'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.05", to="1.0")
    glb.GUI.view['surfaceTransparency'].grid(row=0, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    tk.Button(group, text='OK', command=surface_transparency).grid(row=0, column=2, sticky=tk.S, pady=0)

    group.rowconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    #----------Ambient Light Group----------------------
    group = tk.LabelFrame(glb.GUI.view['tab'], text='Global')
    group.grid(row=5, column=0, columnspan=5, sticky=tk.N+tk.E+tk.S+tk.W, pady=0)
     #-----------------Ambient Light------------------------#
    tk.Label(group, text='Ambient Light').grid(row=0, column=0, sticky=tk.E+tk.S, pady=0)
    glb.GUI.view['ambientLight'] = tk.Scale(group, width=8, orient="horizontal",
        resolution="0.01", to="2.0")
    glb.GUI.view['ambientLight'].grid(row=0, column=1, sticky=tk.E+tk.W+tk.S, pady=0)
    glb.GUI.view['ambientLight'].set(.25)
    tk.Button(group, text='OK', command=ambient_update).grid(row=0, column=2, sticky=tk.S, pady=0)
    
    group.rowconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    
    glb.GUI.view['tab'].rowconfigure(0, weight=1)
    glb.GUI.view['tab'].rowconfigure(1, weight=2)
    glb.GUI.view['tab'].rowconfigure(2, weight=1)
    glb.GUI.view['tab'].rowconfigure(3, weight=1)
    glb.GUI.view['tab'].rowconfigure(4, weight=1)
    glb.GUI.view['tab'].rowconfigure(5, weight=1)
    glb.GUI.view['tab'].columnconfigure(0, weight=1)
    glb.GUI.view['tab'].columnconfigure(1, weight=1)
    glb.GUI.view['tab'].columnconfigure(2, weight=1)
    glb.GUI.view['tab'].columnconfigure(3, weight=1)
    glb.GUI.view['tab'].columnconfigure(4, weight=1)
