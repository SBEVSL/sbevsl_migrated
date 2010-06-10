from pymol import cmd
import Tkinter as tk
import Pmw
from tkColorChooser import askcolor
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.visual import *
from pmg_tk.startup.ProMol_dir.Methods.movie import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *

Pmw.initialise()

def pre_surface_view(tag):
    if tag == 'Surface':
        surface_view()
    elif tag == 'Surface on Cartoon':
        surface_view('toon')
    elif tag == 'Surface on Sticks':
        surface_view('stick')
    elif tag == 'Surface on Spheres':
        surface_view('sphere')
    elif tag == 'Mesh on Sticks':
        surface_view('mesh')
    elif tag == 'Dots on Lines':
        surface_view('dot')

def pre_cartoon_view(tag):
    if tag == 'Cartoon':
        cartoon_view()
    elif tag == 'Putty':
        cartoon_view('putty')
    elif tag == 'Lines on Cartoon':
        stick_toon()
    elif tag == 'Color by Chain':
        util.cbc()

def preres(tag):
    if tag == 'Aromatics':
        color_aromatics()
    elif tag == 'Show Charged':
        show_charged()
    elif tag == 'Solubility':
        view_polarity()

def prerov(tag):
    if tag == 'Roving Sticks':
        rovingstickers()
    elif tag == 'Roving Ball&Sticks':
        rovingballstick()
    elif tag == 'Roving Spheres':
        rovingspheres()
    elif tag == 'Roving Lines':
        rovinglines()

def preele(tag):
    if tag == 'Mesh on Ribbon':
        mesh_ribbon()
    elif tag == 'Dots on Sticks':
        dot_sticks()
    elif tag == 'Surface on Lines':
        surfinglines()

def premisc(tag):
    if tag == 'Hetero Atoms':
        show_hetero()
    elif tag == 'Chain Contacts':
        chain_contact()
    elif tag == 'DNA & RNA':
        show_dna_rna()
    elif tag == 'CPK':
        pglob.procolor()
    elif tag == 'Ball & Stick':
        ball_and_stick()

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

def set_cmd_type(tag):
    '''
    Tell our command line what type of commands to read
    '''
    if tag == 'PyMOL':
        commandLine.setvalue('Enter PyMOL Commands Here')
        cmdType = 'PyMOL'
    else:
        commandLine.setvalue('Enter Chime Commands Here')
        cmdType = 'Chime'

def command_line(self):
    '''
    Read commands from command line
    '''
    try:
        command = commandLine.getvalue()
        if cmdType == 'PyMOL':
            cmd.do(command)
            commandLine.clear()
        else:
            converter.parseIt(command, commandLine, output)
    except:
        showinfo('Error',
            'Invalid command or you must load the PDB through Pro-MOL')

# Coloring on Selection
def color_sel(tag):
    try:
        sel = sel
        if tag == 'Red':
            cmd.color('red', sel)
        elif tag == 'Green':
            cmd.color('green', sel)
        elif tag == 'Orange':
            cmd.color('orange', sel)
        elif tag == 'Yellow':
            cmd.color('yellow', sel)
        elif tag == 'Blue':
            cmd.color('blue', sel)
        elif tag == 'Violet':
            cmd.color('violet', sel)
        elif tag == 'CPK':
            cmd.color("oxygen", "(elem O and "+sel+")")
            cmd.color("nitrogen", "(elem N and "+sel+")")
            cmd.color("sulfur", "(elem S and "+sel+")")
            cmd.color("hydrogen", "(elem H and "+sel+")")
            cmd.color("gray", "(elem C and "+sel+")")
        elif tag == 'Other':
            color = askcolor(title = "Selection Color Chooser")
            colorArray = []
            if color[0] != None:
                list = color[0]
                for each in list:
                    z = (each/255.0)
                    val = repr(z)
                    colorArray.append(val)
                cmd.set_color('newcolor', colorArray)
                cmd.color('newcolor', sel)
    except:
        showinfo('Error', 'Update Selection!')
        
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

# change background colors
def bgcolor_switch(tag):
    if tag == 'Black':
        cmd.do('bg_color black')
    elif tag == 'White':
        cmd.do('bg_color white')
    elif tag == 'Grey':
        cmd.do('bg_color grey')
    elif tag == 'Other':
        color = askcolor(title = "Background Color Chooser")
        colorArray = []
        if color[0] != None:
            list = color[0]
            for each in list:
                z = (each/255.0)
                val = repr(z)
                colorArray.append(val)
            cmd.set_color('newcolor', colorArray)
            cmd.do('bg_color newcolor')
    else:
        pass

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
# Show/Hide Water
def show_hide_water(tag):
    if tag == 'Show':
        cmd.show('(resn HOH)')
        cmd.show('spheres', '(resn HOH)')
    else:
        cmd.hide('(resn HOH)')
    
def initialise():
    
    #------------ Presets Group  ---------------
    group = Pmw.Group(pglob.Tabs['ez_viz']['tab'], tag_text='Preset Views')
    group.grid(row=0, column=0, padx=0, pady=0)

    interior=group.interior()

    #menus for presets

    surface = Pmw.OptionMenu(interior, label_text = 'Surfaces:', labelpos = 'n',
                             items = ('', 'Surface', 'Surface on Cartoon', 'Surface on Sticks',
                                      'Surface on Spheres', 'Mesh on Sticks', 'Dots on Lines'),
                             menubutton_width = 10, command=pre_surface_view)
    surface.grid(row=0, column=0, sticky=tk.NW)

    cartoon = Pmw.OptionMenu(interior, label_text = 'Cartoons:', labelpos = 'n',
                items = ('', 'Cartoon', 'Putty', 'Lines on Cartoon', 'Color by Chain'),
                menubutton_width = 10, command=pre_cartoon_view)
    cartoon.grid(row=0, column=1, sticky=tk.NW)

    residue = Pmw.OptionMenu(interior, label_text = 'By Residue:', labelpos = 'n',
                             items = ('', 'Aromatics', 'Show Charged', 'Solubility'),
                             menubutton_width = 10, command=preres)
    residue.grid(row=0, column=2, sticky=tk.NW)

    roving = Pmw.OptionMenu(interior, label_text = 'Roving:', labelpos = 'n',
                            items = ('', 'Roving Sticks', 'Roving Ball&Sticks', 'Roving Spheres', 'Roving Lines'),
                            menubutton_width = 10, command=prerov)
    roving.grid(row=1, column=2, sticky=tk.NW)

    elecdensity = Pmw.OptionMenu(interior, label_text = 'Electron Density:', labelpos = 'n',
                                 items = ('', 'Mesh on Ribbon', 'Dots on Sticks', 'Surface on Lines'),
                                 menubutton_width = 10, command=preele)
    elecdensity.grid(row=1, column=1, sticky=tk.NW)

    misc = Pmw.OptionMenu(interior, label_text = 'Miscellaneous:', labelpos = 'n',
                          items = ('', 'Hetero Atoms', 'Chain Contacts', 'DNA & RNA', 'CPK', 'Ball & Stick'),
                          menubutton_width = 10, command=premisc)
    misc.grid(row=1, column=0, sticky=tk.NW)

    #roving slider

    pglob.Tabs['ez_viz']['roving'] = Scale(interior, width =8,showvalue="0",
        troughcolor="#ffffff",length="90",orient="horizontal",resolution="0.1",
        to="15.0")
    pglob.Tabs['ez_viz']['roving'].grid(row=1, column=3, padx=0, pady=0, sticky=S)
    pglob.Tabs['ez_viz']['roving'].set(8.0)
    labelradius = Label(interior, text = 'Roving Detail')
    labelradius.grid(row=1, column=3, padx=0, pady=0, sticky=tk.N)

    #preset movies dropdown

    movies = Pmw.OptionMenu(interior, label_text = 'Preset Movies:', labelpos = 'n',
                items = ('', 'Build Protein', 'Highlight Chains', 'Rotate', 'Chain Pull', 'Ligand Pull', 'Surface to Stick', 'Surface to Cartoon', 'Play', 'Stop', 'Rewind'),
                menubutton_width = 10, command=premovie)
    movies.grid(row=0, column=3, sticky=tk.NW)

    group = Pmw.Group(pglob.Tabs['ez_viz']['tab'], tag_text='Display Options')
    group.grid(row=4, column=0, columnspan=2, padx=0, pady=0)
    interior=group.interior()


    # menu for stereo options
    stereo = Pmw.OptionMenu(interior, label_text = 'Stereo:', labelpos = 'n',
                items = ("Off", "Quad", "Cross-Eye", "Wall-Eye"),
                menubutton_width = 11, command=stereo_switch)
    stereo.grid(row=0, column=0, sticky=tk.NW)


    # menu for background color changes
    stereo = Pmw.OptionMenu(interior, label_text = 'Background Color:', labelpos = 'n',
                items = ("Black", "White", "Grey", "Other"),
                menubutton_width = 11, command=bgcolor_switch)
    stereo.grid(row=0, column=1, sticky=tk.NW)

    # menu for background color changes
    stereo = Pmw.OptionMenu(interior, label_text = 'Color Space:', labelpos = 'n',
                items = ("PyMOL", "Publications", "Video/Web"),
                menubutton_width = 11, command=cspace_switch)
    stereo.grid(row=0, column=2, sticky=tk.NW)

    # menu for hide/show interface
    stereo = Pmw.OptionMenu(interior, label_text = 'Internal GUI:', labelpos = 'n',
                items = ("Show", "Hide"),
                menubutton_width = 11, command=hide_interface)
    stereo.grid(row=0, column=3, sticky=tk.NW)

    group = Pmw.Group(pglob.Tabs['ez_viz']['tab'], tag_text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)
    interior = group.interior()
    popbtn=Button(interior, text='Update Selection', width=15,command = pglob.populate)
    popbtn.place(x=50, y=32)

    pglob.Tabs['ez_viz']['selection'] = Pmw.OptionMenu(interior, labelpos = 'w',
               label_text = 'Select:',
                items = (''),
                menubutton_width = 10, command = pglob.set_selection)
    pglob.Tabs['ez_viz']['selection'].grid(row=0, column=0, padx=8, pady=0)

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
    group = Pmw.Group(pglob.Tabs['ez_viz']['tab'], tag_text='Manual Commands')
    group.grid(row=3, column=0, padx=0, pady=0)
    interior = group.interior()

    labels = ('PyMOL', 'Chime')
    commandChooser = radioAdd(interior, 'w', 'vertical', set_cmd_type, 'Command Type:', labels, 0,
                                        0, 1, 1, 'W')

    output = Pmw.ScrolledText(interior,
                                   usehullsize = 1,
                                   hull_width = 250,
                                   hull_height = 50,
                                   text_wrap= tk.WORD)

    output.grid(row=0, column=1, padx=8, pady=2)
    output.setvalue('Command results will show in this box.\n\n')

    # PyMOL Command Prompt
    commandLine = Pmw.EntryField(interior, labelpos='w', label_text='Command Line:',
                                      value='Enter PyMOL Commands Here', entry_width=25, command=command_line)
    commandLine.grid(row=1, column=0, columnspan=2, pady=2)