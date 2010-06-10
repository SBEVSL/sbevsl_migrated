import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
Pmw.initialise()

def initialise():
    group = Pmw.Group(pglob.Tabs['motifs']['tab'], tag_text='Motif Finder')
    group.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W, rowspan=2)
    interior = group.interior()

    framemot = tk.Frame(interior)
    framemot.grid(row = 0, column = 0)
    ballmot = Pmw.Balloon(interior)
    ballmot.bind(framemot, 'Searches through all coded motifs.\n'+
        '1 = exact match, 2 = within range'+
        '\nDouble click on returns to run motif.')
    pglob.Tabs['motifs']['mode'] = IntVar()
    pglob.Tabs['motifs']['findmotif'] = tk.Button(framemot, text ='Motif Finder', 
        command=motifchecker)
    pglob.Tabs['motifs']['findmotif'].grid(row = 0, column = 0)
    pglob.Tabs['motifs']['csv'] = tk.Button(framemot, text ='Export CSV', 
        command=export2csv, state=tk.DISABLED)
    pglob.Tabs['motifs']['csv'].grid(row = 0, column = 1)

    pglob.Tabs['motifs']['motifbox'] = Pmw.ScrolledListBox(interior,
        items=(),
        listbox_height = 6,
        dblclickcommand=allmotif,
        usehullsize = 1,
        hull_width = 350,
        hull_height = 300)
    pglob.Tabs['motifs']['motifbox'].grid()
    
    # group = Pmw.Group(pglob.Tabs['motifs']['tab'], tag_text='Batch Search')
    # group.grid(row=0, column=1, padx=2, pady=2, sticky=tk.W)
    # interior = group.interior()
    # pglob.Tabs['motifs']['multimotif'] = tk.Checkbutton(interior, 
    #     text="Run multiple PDB's?", variable=pglob.Tabs['motifs']['mode'],
    #     padx=2, pady=0, command=toggleMultiState)
    # pglob.Tabs['motifs']['multimotif'].grid(row=0, column=0, stick=tk.W)
    # pglob.Tabs['motifs']['multipdb'] = tk.Text(interior, state=tk.NORMAL, 
    #     width=35, height=2)
    # pglob.Tabs['motifs']['multipdb'].grid(row=1, column=0)
    # pglob.Tabs['motifs']['multipdbtxt'] = 'Enter a comma seperated list of PDB'
    # pglob.Tabs['motifs']['multipdb'].insert(tk.END,
    #     pglob.Tabs['motifs']['multipdbtxt'])
    
    group = Pmw.Group(pglob.Tabs['motifs']['tab'], tag_text='Tools')
    group.grid(row=1, column=1, sticky=tk.W)
    interior = group.interior()
    
    labrange = tk.Label(interior, text='Precision Factor:')
    labrange.grid(row=1, column=0, sticky=tk.W)

    framerange = tk.Frame(interior)
    framerange.grid(row=1, column=1, padx=0, pady=0, sticky=tk.N)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Multiplier for default measured values')
    pglob.Tabs['motifs']['delta'] = tk.Spinbox(framerange, width=4,
        bg="#ffffff", increment="0.01", from_="0.01", to="2.00")
    pglob.Tabs['motifs']['delta'].grid(row=1, column=1, sticky=tk.N)
    pglob.Tabs['motifs']['delta'].delete(0,4)
    pglob.Tabs['motifs']['delta'].insert(0,'1.00')
    
    labrandom = tk.Label(interior, text='Random PDB:')
    labrandom.grid(row=2, column=0, sticky=tk.SW)
    
    random = tk.Button(interior, text='Get Random PDB', width=25, command=randompdb)
    random.grid(row=3, column=0, columnspan=3, sticky=tk.N)
