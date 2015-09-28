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
    group.grid(row=0, column=0, padx=0, pady=0)

    #menus for presets

    surface = Pmw.OptionMenu(group, label_text = 'Surfaces:', labelpos=tk.N,
                             items = ('', 'Surface', 'Surface on Cartoon', 'Surface on Sticks',
                                      'Surface on Spheres', 'Mesh on Sticks', 'Dots on Lines'),
                             menubutton_width = 10, command=pre_surface_view)
    surface.grid(row=0, column=0, sticky=tk.NW)

    cartoon = Pmw.OptionMenu(group, label_text = 'Cartoons:', labelpos=tk.N,
                items = ('', 'Cartoon', 'Putty', 'Lines on Cartoon', 'Color by Chain'),
                menubutton_width = 10, command=pre_cartoon_view)
    cartoon.grid(row=0, column=1, sticky=tk.NW)

    residue = Pmw.OptionMenu(group, label_text = 'By Residue:', labelpos=tk.N,
                             items = ('', 'Aromatics', 'Show Charged', 'Solubility'),
                             menubutton_width = 10, command=preres)
    residue.grid(row=0, column=2, sticky=tk.NW)

    roving = Pmw.OptionMenu(group, label_text = 'Roving:', labelpos=tk.N,
                            items = ('', 'Roving Sticks', 'Roving Ball&Sticks', 'Roving Spheres', 'Roving Lines'),
                            menubutton_width = 10, command=prerov)
    roving.grid(row=1, column=2, sticky=tk.NW)

    elecdensity = Pmw.OptionMenu(group, label_text = 'Electron Density:', labelpos=tk.N,
                                 items = ('', 'Mesh on Ribbon', 'Dots on Sticks', 'Surface on Lines'),
                                 menubutton_width = 10, command=preele)
    elecdensity.grid(row=1, column=1, sticky=tk.NW)

    misc = Pmw.OptionMenu(group, label_text = 'Miscellaneous:', labelpos=tk.N,
                          items = ('', 'Hetero Atoms', 'Chain Contacts', 'DNA & RNA', 'CPK', 'Ball & Stick'),
                          menubutton_width = 10, command=premisc)
    misc.grid(row=1, column=0, sticky=tk.NW)

    #roving slider

    glb.GUI.ez_viz['roving'] = tk.Scale(group, width =8,showvalue="0",
        troughcolor="#ffffff",length="90",orient="horizontal",resolution="0.1",
        to="15.0")
    glb.GUI.ez_viz['roving'].grid(row=1, column=3, padx=0, pady=0, sticky=tk.S)
    glb.GUI.ez_viz['roving'].set(8.0)
    labelradius = tk.Label(group, text = 'Roving Detail')
    labelradius.grid(row=1, column=3, padx=0, pady=0, sticky=tk.N)

    #preset movies dropdown

    movies = Pmw.OptionMenu(group, label_text = 'Preset Movies:', labelpos=tk.N,
                items = ('', 'Build Protein', 'Highlight Chains', 'Rotate',
                    'Chain Pull', 'Ligand Pull', 'Surface to Stick',
                    'Surface to Cartoon', 'Play', 'Stop', 'Rewind'),
                menubutton_width = 10, command=premovie)
    movies.grid(row=0, column=3, sticky=tk.NW)

    group = tk.LabelFrame(glb.GUI.ez_viz['tab'], text='Display Options')
    group.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

    # menu for stereo options
    stereo = Pmw.OptionMenu(group, label_text = 'Stereo:', labelpos=tk.N,
                items = ("Off", "Quad", "Cross-Eye", "Wall-Eye"),
                menubutton_width = 11, command=stereo_switch)
    stereo.grid(row=0, column=0, sticky=tk.NW)


    # menu for background color changes
    stereo = Pmw.OptionMenu(group, label_text = 'Background Color:', labelpos=tk.N,
                items = ("Black", "White", "Grey", "Other"),
                menubutton_width = 11, command=bgcolor_switch)
    stereo.grid(row=0, column=1, sticky=tk.NW)

    # menu for background color changes
    stereo = Pmw.OptionMenu(group, label_text = 'Color Space:', labelpos=tk.N,
                items = ("PyMOL", "Publications", "Video/Web"),
                menubutton_width = 11, command=cspace_switch)
    stereo.grid(row=0, column=2, sticky=tk.NW)

    # menu for hide/show interface
    stereo = Pmw.OptionMenu(group, label_text = 'Internal GUI:', labelpos=tk.N,
                items = ("Show", "Hide"),
                menubutton_width = 11, command=hide_interface)
    stereo.grid(row=0, column=3, sticky=tk.NW)

    group = tk.LabelFrame(glb.GUI.ez_viz['tab'], text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)

    popbtn = tk.Button(group, text='Update Selection', width=15,command = glb.populate)
    popbtn.grid(row=1,column=0, columnspan=2)
    
    tk.Label(group,text='Select').grid(row=0,column=0)
    glb.GUI.ez_viz['selection'] = tk.StringVar()
    glb.GUI.ez_viz['selection_menu'] = tk.OptionMenu(group, glb.GUI.ez_viz['selection'], 'All', 'Selected', 'Not Selected',command=glb.set_selection)
    glb.GUI.ez_viz['selection'].set('All')
    glb.GUI.ez_viz['selection_menu'].grid(row=0,column=1,sticky=tk.NW)

    viewOptions = Pmw.OptionMenu(group, labelpos='w',
    	label_text = 'Show:',
    	items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Polar Contacts'),
    	menubutton_width=10, command=show_rep)

    viewOptions.grid(row=0, column=2, padx=0, pady=0, sticky=tk.N)

    hideOptions = Pmw.OptionMenu(group, labelpos='w',
    	label_text = 'Hide:',
    	items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Everything', 'Polar Contacts'),
    	menubutton_width=10, command=hide_rep)

    hideOptions.grid(row=1, column=2, padx=0, pady=0, sticky=tk.SE)

    # Coloring choices
    selection = Pmw.OptionMenu(group, labelpos=tk.W,
               label_text = 'Color:',
                items = ('Red', 'Green', 'Blue', 'Orange', 'Violet', 'Yellow', 'CPK', 'Other'),
                menubutton_width = 7, command = color_sel)
    selection.grid(row=0, column=3, padx=0, pady=0)