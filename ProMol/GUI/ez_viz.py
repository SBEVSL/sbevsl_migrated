from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.visual import *
from pmg_tk.startup.ProMol.Methods.movie import *
from pmg_tk.startup.ProMol.Methods.setting import *

Pmw.initialise()
    
def initialise():
    
    #------------ Presets Group  ---------------
    group = tk.LabelFrame(glb.GUI.ez_viz['tab'], text='Preset Views')
    group.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    #menus for presets

    surface = Pmw.OptionMenu(group, label_text = 'Surfaces:', labelpos=tk.N,
                             items = ('', 'Surface', 'Surface on Cartoon', 'Surface on Sticks',
                                      'Surface on Spheres', 'Mesh on Sticks', 'Dots on Lines'),
                             command=pre_surface_view)
    surface.grid(row=0, column=0, sticky=tk.E+tk.W)

    cartoon = Pmw.OptionMenu(group, label_text = 'Cartoons:', labelpos=tk.N,
                items = ('', 'Cartoon', 'Putty', 'Lines on Cartoon', 'Color by Chain'),
                command=pre_cartoon_view)
    cartoon.grid(row=0, column=1, sticky=tk.E+tk.W)

    residue = Pmw.OptionMenu(group, label_text = 'By Residue:', labelpos=tk.N,
                             items = ('', 'Aromatics', 'Show Charged', 'Solubility'),
                             command=preres)
    residue.grid(row=0, column=2, sticky=tk.E+tk.W)

    #preset movies dropdown

    movies = Pmw.OptionMenu(group, label_text = 'Preset Movies:', labelpos=tk.N,
                items = ('', 'Build Protein', 'Highlight Chains', 'Rotate',
                    'Chain Pull', 'Ligand Pull', 'Surface to Stick',
                    'Surface to Cartoon', 'Play', 'Stop', 'Rewind'),
                command=premovie)
    movies.grid(row=1, column=0, sticky=tk.E+tk.W)

    misc = Pmw.OptionMenu(group, label_text = 'Miscellaneous:', labelpos=tk.N,
                          items = ('', 'Hetero Atoms', 'Chain Contacts', 'DNA & RNA', 'CPK', 'Ball & Stick'),
                          command=premisc)
    misc.grid(row=1, column=1, sticky=tk.E+tk.W)

    elecdensity = Pmw.OptionMenu(group, label_text = 'Electron Density:', labelpos=tk.N,
                                 items = ('', 'Mesh on Ribbon', 'Dots on Sticks', 'Surface on Lines'),
                                 command=preele)
    elecdensity.grid(row=1, column=2, sticky=tk.E+tk.W)

    roving = Pmw.OptionMenu(group, label_text = 'Roving:', labelpos=tk.N,
                            items = ('', 'Roving Sticks', 'Roving Ball&Sticks', 'Roving Spheres', 'Roving Lines'),
                            command=prerov)
    roving.grid(row=2, column=0, rowspan=2, sticky=tk.E+tk.W)

    #roving slider

    glb.GUI.ez_viz['roving'] = tk.Scale(group, width =8,showvalue="0",
        troughcolor="#ffffff",length="90",orient="horizontal",resolution="0.1",
        to="15.0")
    glb.GUI.ez_viz['roving'].grid(row=3, column=1, columnspan=2, sticky=tk.N+tk.E+tk.W)
    glb.GUI.ez_viz['roving'].set(8.0)
    labelradius = tk.Label(group, text = 'Roving Detail')
    labelradius.grid(row=2, column=1, columnspan=2, sticky=tk.S)


    group.rowconfigure(0, weight=2)
    group.rowconfigure(1, weight=2)
    group.rowconfigure(2, weight=1)
    group.rowconfigure(3, weight=1)
    group.columnconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.columnconfigure(2, weight=1)

    # Display Options
    group = tk.LabelFrame(glb.GUI.ez_viz['tab'], text='Display Options')
    group.grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    # menu for stereo options
    stereo = Pmw.OptionMenu(group, label_text = 'Stereo:', labelpos=tk.N,
                items = ("Off", "Quad", "Cross-Eye", "Wall-Eye"),
                command=stereo_switch)
    stereo.grid(row=0, column=0, sticky=tk.E+tk.W)


    # menu for background color changes
    stereo = Pmw.OptionMenu(group, label_text = 'Background Color:', labelpos=tk.N,
                items = ("Black", "White", "Grey", "Other"),
                command=bgcolor_switch)
    stereo.grid(row=0, column=1, sticky=tk.E+tk.W)

    # menu for background color changes
    stereo = Pmw.OptionMenu(group, label_text = 'Color Space:', labelpos=tk.N,
                items = ("PyMOL", "Publications", "Video/Web"),
                command=cspace_switch)
    stereo.grid(row=1, column=1, sticky=tk.E+tk.W)

    # menu for hide/show interface
    stereo = Pmw.OptionMenu(group, label_text = 'Internal GUI:', labelpos=tk.N,
                items = ("Show", "Hide"),
                command=hide_interface)
    stereo.grid(row=1, column=0, sticky=tk.E+tk.W)
    group.rowconfigure(0, weight=1)
    group.rowconfigure(1, weight=1)
    group.columnconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)

    # Automated Commands
    group = tk.LabelFrame(glb.GUI.ez_viz['tab'], text = 'Automated Commands')
    group.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
    
    tk.Label(group,text='Select:').grid(row=0, column=0, sticky=tk.S)
    glb.GUI.ez_viz['selection'] = tk.StringVar()
    glb.GUI.ez_viz['selection_menu'] = tk.OptionMenu(group, glb.GUI.ez_viz['selection'], 'All', 'Selected', 'Not Selected',command=glb.set_selection)
    glb.GUI.ez_viz['selection'].set('All')
    glb.GUI.ez_viz['selection_menu'].grid(row=1, column=0, sticky=tk.N+tk.E+tk.W)

    popbtn = tk.Button(group, text='Update Selection', command = glb.populate)
    popbtn.grid(row=1, column=1, columnspan=2, sticky=tk.N+tk.E+tk.W)

    viewOptions = Pmw.OptionMenu(group, labelpos=tk.N,
        label_text = 'Show:',
        items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Polar Contacts'),
        command=show_rep)

    viewOptions.grid(row=2, column=1, sticky=tk.E+tk.W)

    hideOptions = Pmw.OptionMenu(group, labelpos=tk.N,
        label_text = 'Hide:',
        items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Everything', 'Polar Contacts'),
        command=hide_rep)

    hideOptions.grid(row=2, column=2, sticky=tk.E+tk.W)

    # Coloring choices
    selection = Pmw.OptionMenu(group, labelpos=tk.N,
               label_text = 'Color:',
                items = ('Red', 'Green', 'Blue', 'Orange', 'Violet', 'Yellow', 'CPK', 'Other'),
                command = color_sel)
    selection.grid(row=2, column=0, sticky=tk.E+tk.W)

    group.rowconfigure(0, weight=1)
    group.rowconfigure(1, weight=1)
    group.rowconfigure(2, weight=2)
    group.columnconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.columnconfigure(2, weight=1)
    
    glb.GUI.ez_viz['tab'].rowconfigure(0, weight=3)
    glb.GUI.ez_viz['tab'].rowconfigure(1, weight=2)
    glb.GUI.ez_viz['tab'].rowconfigure(2, weight=2)
    glb.GUI.ez_viz['tab'].columnconfigure(0, weight=1)
