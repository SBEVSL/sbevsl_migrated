from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
Pmw.initialise()

def initialise():
    group = Pmw.Group(pglob.Tabs['motif_maker']['tab'], tag_text='Motif Maker')
    group.grid(row=0, column=0, columnspan=2, padx=0, pady=0, sticky=tk.NW)
    interior = group.interior()
    
    lpdb = tk.Label(interior, text='PDB:')
    lpdb.grid(row=0, column=0, sticky=tk.E)
    
    pglob.Tabs['motif_maker']['pdb'] = tk.Entry(interior, width=4)
    pglob.Tabs['motif_maker']['pdb'].grid(row=0, column=1, sticky=tk.W)
    
    lec = tk.Label(interior, text='EC #:')
    lec.grid(row=0, column=2, sticky=tk.E)
    
    pglob.Tabs['motif_maker']['ec'] = tk.Entry(interior, width=10)
    pglob.Tabs['motif_maker']['ec'].grid(row=0, column=3, columnspan=2, sticky=tk.W)
    
    pglob.Tabs['motif_maker']['lresn'] = {}
    pglob.Tabs['motif_maker']['resn'] = {}
    pglob.Tabs['motif_maker']['lresi'] = {}
    pglob.Tabs['motif_maker']['resi'] = {}
    pglob.Tabs['motif_maker']['lbackbone'] = {}
    pglob.Tabs['motif_maker']['backbone'] = {}
    pglob.Tabs['motif_maker']['lchain'] = {}
    pglob.Tabs['motif_maker']['chain'] = {}
    for i in range(1,11):
        pglob.Tabs['motif_maker']['lresn'][i] = tk.Label(interior, text='%s Residue:'%(i))
        pglob.Tabs['motif_maker']['lresn'][i].grid(row=i, column=0)
        
        pglob.Tabs['motif_maker']['resn'][i] = tk.Entry(interior, width=8)
        pglob.Tabs['motif_maker']['resn'][i].grid(row=i, column=1)
    
        pglob.Tabs['motif_maker']['lresi'][i] = tk.Label(interior, text='Number:')
        pglob.Tabs['motif_maker']['lresi'][i].grid(row=i, column=2)
        
        pglob.Tabs['motif_maker']['resi'][i] = tk.Entry(interior, width=5)
        pglob.Tabs['motif_maker']['resi'][i].grid(row=i, column=3, sticky=tk.W)
        
        pglob.Tabs['motif_maker']['lchain'][i] = tk.Label(interior, text='Chain:')
        pglob.Tabs['motif_maker']['lchain'][i].grid(row=i, column=4)
        
        pglob.Tabs['motif_maker']['chain'][i] = tk.Entry(interior, width=2)
        pglob.Tabs['motif_maker']['chain'][i].grid(row=i, column=5)
        
        pglob.Tabs['motif_maker']['lbackbone'][i] = tk.Label(interior, text='BackBone:')
        pglob.Tabs['motif_maker']['lbackbone'][i].grid(row=i, column=6)
        
        pglob.Tabs['motif_maker']['backbone'][i] = tk.Spinbox(interior,values=('Off','On'),width=3,
            wrap=True,state='readonly',readonlybackground='#ffffff')
        pglob.Tabs['motif_maker']['backbone'][i].grid(row=i, column=7)
    
    labrange = tk.Label(interior, text='Precision Factor:')
    labrange.grid(row=11, column=0,columnspan=2, sticky=tk.SE)
        
    framerange = tk.Frame(interior)
    framerange.grid(row=11, column=2,sticky=tk.W)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault= 2')
    pglob.Tabs['motif_maker']['pf'] = tk.Spinbox(framerange,width=4,increment="0.01",from_="0.01",
        to="4.00",bg="#ffffff")
    pglob.Tabs['motif_maker']['pf'].grid(row=11, column=2, sticky=tk.W)
    pglob.Tabs['motif_maker']['pf'].delete(0,4)
    pglob.Tabs['motif_maker']['pf'].insert(0,'2.00')
    
    but1 = tk.Button(interior, text='Test',command=makemotif)
    but1.grid(row=11, column=3, sticky=tk.SE)
    
    save = tk.Button(interior, text= 'Save', command=makemotif)
    save.grid(row=11, column=4, columnspan=2, sticky=tk.SE)
    
    saveas = tk.Button(interior, text= 'Export', command=makemotif)
    saveas.grid(row=11, column=6, sticky=tk.SE)