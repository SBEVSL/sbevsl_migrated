from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.save import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *

Pmw.initialise()

def initialise():
    group = Pmw.Group(pglob.Tabs['batch_motif']['tab'], tag_text='Enter Location of List')
    group.grid(row=0, column=0, padx=0, pady=0)
    interior = group.interior()
    
    myFormats = [('Text File', '*.txt')]

    w = tk.Text(interior, height = 3)
    w.insert(END, "\n")
    w.insert(END, "Make a comma separated list of sensitivities")
    w.insert(END, "\n")
    w.insert(END, "Find your text file of molecules.")
    w.config(state = DISABLED)

    sensEntry = tk.Entry(interior)
    entry123 = tk.Entry(interior)
    button123 = tk.Button(interior, text = 'Run')
    browse = tk.Button(interior, text = 'Browse')
    browse.bind('<Button-1>', openfilename);

    w.grid(row = 0, column = 0, columnspan = 2)
    tk.Label(interior, text = 'Sensitivities:').grid(row = 1, column = 0, sticky =  E)
    tk.Label(interior, text = 'File:').grid(row = 2, column = 0, sticky = E)
    sensEntry.grid(row = 1, column = 1, sticky = W)
    entry123.grid(row = 2, column = 1, sticky = W)
    button123.grid(row = 3, column = 0, sticky = E)
    interior.pack()
    browse.grid(row = 3, column = 1, sticky = W)
    
    button123.bind('<Button-1>', batchLoop)