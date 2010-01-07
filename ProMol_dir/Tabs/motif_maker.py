from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
Pmw.initialise()

def initialise():

    group = Pmw.Group(pglob.Tabs['motif_maker']['tab'], tag_text = 'Motif Database')
    group.grid(row=3, column=0, padx=0, pady=0)
    interior = group.interior()
    atlab = tk.Label(interior, text = "Atoms")
    atlab.grid(row=1, column =0, sticky = 'w')



    entcount = tk.Entry(interior)
    entz = tk.Entry(interior)


    motifdrop = Pmw.ScrolledListBox(interior,
                items=(),
                dblclickcommand = runcusmotif,
                listbox_height = 6,
                usehullsize = 1,
                hull_width = 300,
                hull_height = 150,)
    motifdrop.grid(row=2, column =0)



    nmlab = tk.Label(interior, text = 'Motif Name')
    nmlab.grid(row=1, column =0, sticky = 'n')
    runbtn1 = tk.Button(interior, text = 'Run all Motifs', command = runum)
    runbtn1.grid(row = 0, column =0, sticky = 'W')
    mobtn = tk.Button(interior, text = 'Motif Maker', command = loadmotifer)
    mobtn.grid(row = 0, column = 0, sticky = 'E')

    button333 = tk.Button(interior, text = 'Get Random PDB', width =25, command = randomized)
    button333.grid(row = 3, column = 0, padx = 10, sticky = 'N')