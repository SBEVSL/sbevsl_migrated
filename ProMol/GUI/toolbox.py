from pymol import cmd
import Tkinter as tk
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.motif import *
from pmg_tk.startup.ProMol.Methods.setting import *
from pmg_tk.startup.ProMol.Methods.utility import *

def initialise():

    #---------Orthoscopic view and View distance-----#
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Perspective')
    group.grid(row=1, column=1, padx=0, pady=0, sticky=tk.NW)
    orthoon = tk.Button(group, text = 'Orthoscopic On', width = 16, command=turnorthon)
    orthoon.grid(row=0, column=0, padx=2, pady=2, sticky=tk.NW)
    orthoff = tk.Button(group, text = 'Orthoscopic Off',width = 16, command=turnorthoff)
    orthoff.grid(row=1, column=0, padx=2, pady=2, sticky=tk.NW)
    viewsetter = tk.Label(group, text = 'Set Field of View')
    viewsetter.grid(row=2, column=0, padx=0, pady=0, sticky=tk.N)
    
    glb.GUI.toolbox['setfieldofview'] = IntVar()
    setfieldofview = tk.Scale(group, width=8, troughcolor="#ffffff",
        length="65", orient="horizontal", resolution="5", to="100",
        variable=glb.GUI.toolbox['setfieldofview'], command=setfield)
    setfieldofview.grid(row=3, column=0, padx=0, pady=0, sticky=tk.N)
    glb.GUI.toolbox['setfieldofview'].set(20)
    getfield = tk.Button(group, text = 'Update',width = 16)
    getfield.grid(row=4, column=0, padx=2, pady=2, sticky=tk.N)
    #----------------Orient the screen--------------#
    orientbutt = tk.Button(group, text = 'Orient Screen', width = 16,
        command=orient)
    orientbutt.grid(row=6, column=0, padx=2, pady=2, sticky=tk.N)

    #-------------------Alternate Ray Tracing----------------------
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Ray Trace Options')
    group.grid(row=0, column=0,columnspan=2, padx=0, pady=5, sticky=tk.NW)
    rayzero = tk.Button(group, text = 'Default Ray', command=setray0)
    rayzero.grid(row=0, column=0, padx=2, pady=2, sticky=tk.E)
    rayone = tk.Button(group, text = 'Black Outline Ray', command=setray1)
    rayone.grid(row=0, column=1, padx=2, pady=2, sticky=tk.E)
    raytwo = tk.Button(group, text = 'Black and White Ray', command=setray2)
    raytwo.grid(row=0, column=2, padx=2, pady=2, sticky=tk.E)
    raythree = tk.Button(group, text = 'Cartoon Ray', command=setray3)
    raythree.grid(row=0, column=3, padx=2, pady=2, sticky=tk.E)

    #------------------Amino Acid Reference Group-----------------
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Amino Acid Reference:')
    group.grid(row=1, column=0,  padx=0, pady=0, sticky=tk.NW)
    
    msg = tk.Label(group, text="Amino Acid:")
    msg.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NE)
    glb.GUI.toolbox['aminoimage'] = tk.Entry(group, width=7,)
    glb.GUI.toolbox['aminoimage'].grid(row=0, column=1, padx=4, pady=3,
        sticky=tk.NW)
    but37 = tk.Button(group, text="Submit", width="7", command=showaminopic)
    but37.grid(row=0, column=2, padx=4, pady=3, sticky=tk.NW)
    
    glb.GUI.toolbox['aminocanvas'] = tk.Canvas(group, width=200, height=150)
    glb.GUI.toolbox['aminocanvas'].grid(row=1, column=0,columnspan=2, rowspan=6,
        padx=0, pady=0, sticky=tk.NE)

    labels = ('2D', '3D')
    glb.GUI.toolbox['picdimension'] = StringVar()
    glb.GUI.toolbox['picdimension'].set('2D')
    labelrow = 1
    for label in labels:
        dimensionsel = tk.Radiobutton(group, text=label, value=label,
            variable=glb.GUI.toolbox['picdimension'])
        dimensionsel.grid(column=2,row=labelrow)
        labelrow += 1
