from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
Pmw.initialise()

def initialise():
    #Molecular Classification Field
    label = Label(pglob.Tabs['motifs'], text='Protein Classification')
    label.grid(row=1,column=0,sticky='sw',padx=5,pady=0)
    classify = Text(pglob.Tabs['motifs'], state=NORMAL, height=1.4, width=30)
    classify.insert(END,"Protein Classification")
    classify.grid(row=2, column=0, sticky='sw',padx=5, pady=0)

    #Molecule Name Field
    name = StringVar()
    molName = Label(pglob.Tabs['motifs'], textvariable=name, font='arial, 14', wraplength='450')
    name.set("")
    molName.grid(row=0, column=0, columnspan=2,sticky='w',padx=5, pady=5)


    #Hetero Atoms
    label=Label(pglob.Tabs['motifs'], text="Hetero Atoms")
    label.grid(row=1, column=1, sticky='sw', padx=5, pady=0)
    het = Text(pglob.Tabs['motifs'], state=NORMAL, height=1.4, width=25)
    het.insert(END,"List of hetero atoms")
    het.grid(row=2,column=1, sticky='w',padx=5,pady=0)
    
    #mechanisim group
    group = Pmw.Group(pglob.Tabs['motifs'], tag_text = 'Motifs')
    group.grid(row=3, column=0,columnspan =2, padx=0, pady=0)
    interior = group.interior()

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Oxidoreductases:',labelpos = 'n',
                items = ('','Superoxide Dismutase','Peroxidase','Alcohol Dehydrogenase',
                         'Aldose Reductase','NAD Reductase', 'NAD Reductase2','Betaine aldehyde dehydrogenase'),
                menubutton_width = 8, command=oxidoreductase)
    stereo.grid(row=0,column=0,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Transferases:',labelpos = 'n',
                            items = ('','Amino Transferase', 'Glutamine Amidotransferase',
                                     'Thymidine Kinase', 'ACTase', 'Adenylate Kinase','SRC Family Kinase',
                                     'Hhal Methyltransferase','Serotonin Acetyltransferase', 'Cyclin Dependent Kinase'),
                            menubutton_width = 8, command=transferase)
    stereo.grid(row=0,column=1,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Hydrolases:',labelpos = 'n',
                items = ('','Serine Protease', 'Papain Like', 'Metalloprotease', 'Tyrosine Phosphatase', 'Beta Lactamase', 'O-Glycosyl', 'Cephalosporin deacetylase'),
                menubutton_width = 8, command=hydrolase)
    stereo.grid(row=0,column=2,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Lyases:',labelpos = 'n',
                items = ('','Carbonic Anhydrase', 'Carbon Carbon','Chondroitinase', 'Hyaluronate-Lyase', 'Exonuclease 3', 'Citrate Synthase'),
                menubutton_width = 8, command=lyase)
    stereo.grid(row=0,column=3,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Isomerases:',labelpos = 'n',
                items = ('','Fucose Isomerase','Triose Phosphate Isomerase', 'FK506 Cis-Trans'),
                menubutton_width = 8, command=isomerase)
    stereo.grid(row=1,column=0,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Ligase:',labelpos = 'n',
                items = (' ', 'DNA Ligase'),
                menubutton_width = 8, command=ligase)
    stereo.grid(row=1,column=1,sticky=NW)

    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Other:',labelpos = 'n',
                items = ('','Zinc Finger'),
                menubutton_width = 8, command=other)
    stereo.grid(row=1,column=2,sticky=NW)

    stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos = 'n',
                items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                menubutton_width = 8, command=motifoption)
    stereo.grid(row=1,column=3,sticky=NW)
    framerange = Frame(interior)
    framerange.grid(row=2, column=1,columnspan = 4, padx=0, pady=0, sticky=NW)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Multiplier for default measured values\nRe-click on desired motif to render change')
    range = Scale(framerange, width =8)
    range.configure(troughcolor="#ffffff")
    range.configure(length="200")
    range.configure(orient="horizontal")
    range.configure(resolution="0.01")
    range.configure(to="2.0")
    range.grid(row=2, column=1,columnspan = 4, padx=0, pady=0, sticky=NW)
    range.set(1)

    labrange = Label(interior, text='Precision Factor:')
    labrange.grid(row=2, column=0, sticky=SE)

    buttonAdd(interior, 'Reset', 10, resetrange, 3, 3, 'SE')



    #---------------------Show residues around active site---------------#
    group = Pmw.Group(pglob.Tabs['motifs'], tag_text='Tools')
    group.grid(row=4, column=0, columnspan=1, padx=2, pady=2, sticky=W)
    interior = group.interior()
    framesela = Frame(interior)
    framesela.grid(row=0, column=0, columnspan = 2, padx=0, pady=0, sticky=N)
    ballsela = Pmw.Balloon(interior)
    ballsela.bind(framesela, 'Within # Angstroms')
    selA = Scale(framesela, width =8)
    selA.configure(troughcolor="#ffffff")
    selA.configure(length="130")
    selA.configure(orient="horizontal")
    selA.configure(resolution="0.2")
    selA.configure(to="10.0")
    selA.grid(row=0, column=0, columnspan= 2, padx=0, pady=0, sticky=N)
    selA.set(5.0)
    frameadj = Frame(interior)
    frameadj.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
    balladj = Pmw.Balloon(interior)
    balladj.bind(frameadj, 'Display residues adjacent to motif')


    showround = Button(frameadj, width = 12, text = 'Adjacent')
    showround.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
    showround.bind('<Button-1>', roundres)

    delres = Button(interior, width = 14, text = 'Delete Adjacent')
    delres.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
    delres.bind('<Button-1>', resdel)

    group = Pmw.Group(pglob.Tabs['motifs'], tag_text='Motif Search')
    group.grid(row=4, column=1, columnspan=1, padx=2, pady=2, sticky=W)
    interior = group.interior()

    framemot = Frame(interior)
    framemot.grid(row = 0, column = 0)
    ballmot = Pmw.Balloon(interior)
    ballmot.bind(framemot, 'Searches through all motifs\n1 = better, 2 = worse\nDouble click on returns to show')
    find_motif = Button(framemot, text ='Motif Finder')
    find_motif.grid(row = 0, column = 0)

    find_motif.bind('<Button-1>', motifchecker)


    motifbox = Pmw.ScrolledListBox(interior,
    items=(),
    listbox_height = 6,
    dblclickcommand=allmotif,
    usehullsize = 1,
    hull_width = 180,
    hull_height = 100,)
    #Changed hull_height to 100 to see more - Corey
    motifbox.grid()