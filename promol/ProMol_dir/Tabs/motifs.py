from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
Pmw.initialise()

def initialise():
    group = Pmw.Group(pglob.Tabs['motifs']['tab'], tag_text='Motif Search')
    group.grid(row=0, column=0, columnspan=1, padx=2, pady=2, sticky=tk.W)
    interior = group.interior()

    framemot = Frame(interior)
    framemot.grid(row = 0, column = 0)
    ballmot = Pmw.Balloon(interior)
    ballmot.bind(framemot, 'Searches through all motifs\n0 = Motif not found, 1 = exact match, 2 = within range'+
        '\nDouble click on returns to show')
    pglob.Tabs['motifs']['findmotif'] = Button(framemot, text ='Motif Finder', command=motifchecker)
    pglob.Tabs['motifs']['findmotif'].grid(row = 0, column = 0)

    pglob.Tabs['motifs']['motifbox'] = Pmw.ScrolledListBox(interior,
        items=(),
        listbox_height = 6,
        dblclickcommand=allmotif,
        usehullsize = 1,
        hull_width = 350,
        hull_height = 400)
    pglob.Tabs['motifs']['motifbox'].grid()
    
    group = Pmw.Group(pglob.Tabs['motifs']['tab'], tag_text='Tools')
    group.grid(row=0, column=1, columnspan=1, padx=2, pady=2, sticky=tk.W)
    interior = group.interior()
    
    labrange = Label(interior, text='Precision Factor:')
    labrange.grid(row=1, column=0, sticky=tk.SW)
        
    rerange = Button(interior, text='Reset',highlightthickness=0, 
                  width=8,command=resetrange,padx=2,pady=0)
    rerange.grid(row=2, column=2, sticky=tk.SW, padx=2, pady=2)

    framerange = Frame(interior)
    framerange.grid(row=2, column=0,columnspan = 2, padx=0, pady=0, sticky=tk.N)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Multiplier for default measured values\n'+
        'Re-click on desired motif to render change')
    pglob.Tabs['motifs'].update({'delta':Scale(framerange, width =8)})
    pglob.Tabs['motifs']['delta'].configure(troughcolor="#ffffff")
    pglob.Tabs['motifs']['delta'].configure(length="175")
    pglob.Tabs['motifs']['delta'].configure(orient="horizontal")
    pglob.Tabs['motifs']['delta'].configure(resolution="0.01")
    pglob.Tabs['motifs']['delta'].configure(to="2.0")
    pglob.Tabs['motifs']['delta'].grid(row=2, column=1,columnspan = 4, padx=0, pady=0, sticky=tk.N)
    pglob.Tabs['motifs']['delta'].set(1)
    
    labadjacent = Label(interior, text='Adjacent:')
    labadjacent.grid(row=3, column=0, sticky=tk.SW)

    #---------------------Show residues around active site---------------#
    
    framesela = Frame(interior)
    framesela.grid(row=4, column=0, columnspan = 2, padx=0, pady=0, sticky=tk.N)
    ballsela = Pmw.Balloon(interior)
    ballsela.bind(framesela, 'Within # Angstroms')
    selA = Scale(framesela, width =8)
    selA.configure(troughcolor="#ffffff")
    selA.configure(length="175")
    selA.configure(orient="horizontal")
    selA.configure(resolution="0.2")
    selA.configure(to="10.0")
    selA.grid(row=4, column=0, columnspan=2, padx=0, pady=0, sticky=tk.N)
    selA.set(5.0)

    showround = Button(interior, width = 12, text = 'Adjacent', command=roundres)
    showround.grid(row=5, column=0, columnspan=2, padx=1, pady=1, sticky=tk.NW)
    balladj = Pmw.Balloon(interior)
    balladj.bind(showround, 'Display residues adjacent to motif')

    delres = Button(interior, width = 14, text = 'Delete Adjacent', command=resdel)
    delres.grid(row=5, column=1, columnspan=2, padx=1, pady=1, sticky=tk.NW)
    
    stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos =tk.W,
                items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 
                'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                menubutton_width = 8, command=motifoption)
    stereo.grid(row=6,column=0,sticky=tk.N)
