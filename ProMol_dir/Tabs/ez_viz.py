from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.visual import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *

Pmw.initialise()
def initialise():

    scriptwrite = Pmw.OptionMenu(pglob.Tabs['ez_viz'], label_text = 'Script Writing:', labelpos = 'n',
            items = ("Off", "On"),
            menubutton_width = 11, command=write_script)
    scriptwrite.grid(row=5, column=0, sticky=NW)

    group = Pmw.Group(pglob.Tabs['ez_viz'], tag_text='Run Script')
    group.grid(row=5, column=0, padx=8, pady=0, sticky = N)
    interior = group.interior()
    scriptbutton = Button(interior, width = 10, text = 'Run Script')
    scriptbutton.grid()
    scriptbutton.bind('<Button-1>', loadlog)
    
    loaderent = Entry(interior, width = 7)

    #------------ Presets Group  ---------------
    group = Pmw.Group(pglob.Tabs['ez_viz'], tag_text='Preset Views')
    group.grid(row=0, column=0, padx=0, pady=0)

    interior=group.interior()

    #menus for presets

    surface = Pmw.OptionMenu(interior, label_text = 'Surfaces:', labelpos = 'n',
                             items = ('', 'Surface', 'Surface on Cartoon', 'Surface on Sticks',
                                      'Surface on Spheres', 'Mesh on Sticks', 'Dots on Lines'),
                             menubutton_width = 10, command=presurf)
    surface.grid(row=0, column=0, sticky=NW)

    cartoon = Pmw.OptionMenu(interior, label_text = 'Cartoons:', labelpos = 'n',
                items = ('', 'Cartoon', 'Putty', 'Lines on Cartoon', 'Color by Chain'),
                menubutton_width = 10, command=pretoon)
    cartoon.grid(row=0, column=1, sticky=NW)

    residue = Pmw.OptionMenu(interior, label_text = 'By Residue:', labelpos = 'n',
                             items = ('', 'Aromatics', 'Show Charged', 'Solubility'),
                             menubutton_width = 10, command=preres)
    residue.grid(row=0, column=2, sticky=NW)

    roving = Pmw.OptionMenu(interior, label_text = 'Roving:', labelpos = 'n',
                            items = ('', 'Roving Sticks', 'Roving Ball&Sticks', 'Roving Spheres', 'Roving Lines'),
                            menubutton_width = 10, command=prerov)
    roving.grid(row=1, column=2, sticky=NW)

    elecdensity = Pmw.OptionMenu(interior, label_text = 'Electron Density:', labelpos = 'n',
                                 items = ('', 'Mesh on Ribbon', 'Dots on Sticks', 'Surface on Lines'),
                                 menubutton_width = 10, command=preele)
    elecdensity.grid(row=1, column=1, sticky=NW)

    misc = Pmw.OptionMenu(interior, label_text = 'Miscellaneous:', labelpos = 'n',
                          items = ('', 'Hetero Atoms', 'Chain Contacts', 'DNA & RNA', 'CPK', 'Ball & Stick'),
                          menubutton_width = 10, command=premisc)
    misc.grid(row=1, column=0, sticky=NW)

    #roving slider

    rovingradius2 = Scale(interior, width =8)
    rovingradius2.configure(showvalue="0")
    rovingradius2.configure(troughcolor="#ffffff")
    rovingradius2.configure(length="90")
    rovingradius2.configure(orient="horizontal")
    rovingradius2.configure(resolution="0.1")
    rovingradius2.configure(to="15.0")
    rovingradius2.grid(row=1, column=3, padx=0, pady=0, sticky=S)
    rovingradius2.set(8.0)
    labelradius = Label(interior, text = 'Roving Detail')
    labelradius.grid(row=1, column=3, padx=0, pady=0, sticky=N)

    #preset movies dropdown

    movies = Pmw.OptionMenu(interior, label_text = 'Preset Movies:', labelpos = 'n',
                items = ('', 'Ligand Zoom', 'Build Protein', 'Highlight Chains', 'Rotate', 'Chain Pull', 'Ligand Pull', 'Surface to Stick', 'Surface to Cartoon', 'Play', 'Stop', 'Rewind'),
                menubutton_width = 10, command=premovie)
    movies.grid(row=0, column=3, sticky=NW)

    group = Pmw.Group(pglob.Tabs['ez_viz'], tag_text='Display Options')
    group.grid(row=4, column=0, columnspan=2, padx=0, pady=0)
    int=group.interior()


    # menu for stereo options
    stereo = Pmw.OptionMenu(int, label_text = 'Stereo:', labelpos = 'n',
                items = ("Off", "Quad", "Cross-Eye", "Wall-Eye"),
                menubutton_width = 11, command=stereo_switch)
    stereo.grid(row=0, column=0, sticky=NW)


    # menu for background color changes
    stereo = Pmw.OptionMenu(int, label_text = 'Background Color:', labelpos = 'n',
                items = ("Black", "White", "Grey", "Other"),
                menubutton_width = 11, command=bgcolor_switch)
    stereo.grid(row=0, column=1, sticky=NW)

    # menu for background color changes
    stereo = Pmw.OptionMenu(int, label_text = 'Color Space:', labelpos = 'n',
                items = ("PyMOL", "Publications", "Video/Web"),
                menubutton_width = 11, command=cspace_switch)
    stereo.grid(row=0, column=2, sticky=NW)

    # menu for hide/show interface
    stereo = Pmw.OptionMenu(int, label_text = 'Internal GUI:', labelpos = 'n',
                items = ("Show", "Hide"),
                menubutton_width = 11, command=hide_interface)
    stereo.grid(row=0, column=3, sticky=NW)

    group = Pmw.Group(pglob.Tabs['ez_viz'], tag_text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)
    interior = group.interior()
    popbtn=Button(interior, text='Update Selection', width=15)
    popbtn.place(x=50, y=32)
    popbtn.bind('<Button-1>', pglob.populate)

    selection = Pmw.OptionMenu(interior, labelpos = 'w',
               label_text = 'Select:',
                items = (''),
                menubutton_width = 10, command = set_sel)
    selection.grid(row=0, column=0, padx=8, pady=0)



    viewOptions = Pmw.OptionMenu(interior, labelpos='w',
    	label_text = 'Show:',
    	items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Everything', 'Polar Contacts'),
    	menubutton_width=10, command=show_rep)

    viewOptions.grid(row=0, column=1, padx=0, pady=0, sticky='N')

    hideOptions = Pmw.OptionMenu(interior, labelpos='w',
    	label_text = 'Hide:',
    	items = ('Lines', 'Sticks', 'Ribbons', 'Cartoon', 'Dots', 'Spheres', 'Mesh', 'Surface', 'Ball and Stick', 'Water', 'Everything', 'Polar Contacts'),
    	menubutton_width=10, command=hide_rep)

    hideOptions.grid(row=1, column=1, padx=0, pady=0, sticky='SE')

    # Coloring choices
    selection = Pmw.OptionMenu(interior, labelpos = 'w',
               label_text = 'Color:',
                items = ('Red', 'Green', 'Blue', 'Orange', 'Violet', 'Yellow', 'CPK', 'Other'),
                menubutton_width = 7, command = color_sel)

    selection.grid(row=0, column=2, padx=0, pady=0)
 
     # MANUAL COMMANDS SECTION
    group = Pmw.Group(pglob.Tabs['ez_viz'], tag_text='Manual Commands')
    group.grid(row=3, column=0, padx=0, pady=0)
    interior = group.interior()

    labels = ('PyMOL', 'Chime')
    commandChooser = radioAdd(interior, 'w', 'vertical', set_cmd_type, 'Command Type:', labels, 0,
                                        0, 1, 1, 'W')

    output = Pmw.ScrolledText(interior,
                                   usehullsize = 1,
                                   hull_width = 250,
                                   hull_height = 50,
                                   text_wrap= WORD)

    output.grid(row=0, column=1, padx=8, pady=2)
    output.setvalue('Command results will show in this box.\n\n')

    # PyMOL Command Prompt
    commandLine = Pmw.EntryField(interior, labelpos='w', label_text='Command Line:',
                                      value='Enter PyMOL Commands Here', entry_width=25, command=command_line)
    commandLine.grid(row=1, column=0, columnspan=2, pady=2)