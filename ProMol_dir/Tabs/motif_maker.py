from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
Pmw.initialise()

def initialise():
    pglob.Tabs['motif_maker']['maker'] = Pmw.Group(pglob.Tabs['motif_maker']['tab'], tag_text='Motif Maker')
    pglob.Tabs['motif_maker']['maker'].grid(row=0, column=0, padx=0, pady=0)
    interior = pglob.Tabs['motif_maker']['maker'].interior()
    
    lpdb = tk.Label(interior, text='PDB:')
    lpdb.grid(row=0, column=0, sticky=tk.E)
    
    pglob.Tabs['motif_maker']['pdb'] = tk.Entry(interior, width=4)
    pglob.Tabs['motif_maker']['pdb'].grid(row=0, column=1, sticky=tk.W)
    
    lec = tk.Label(interior, text='EC #:')
    lec.grid(row=0, column=2, sticky=tk.E)
    
    pglob.Tabs['motif_maker']['ec'] = tk.Entry(interior, width=10)
    pglob.Tabs['motif_maker']['ec'].grid(row=0, column=3, columnspan=2, sticky=tk.W)
    
    labrange = tk.Label(interior, text='Precision Factor:')
    labrange.grid(row=0, column=5,columnspan=2, sticky=tk.E)
        
    framerange = tk.Frame(interior)
    framerange.grid(row=0, column=7,sticky=tk.W)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault= 2')
    pglob.Tabs['motif_maker']['pf'] = tk.Spinbox(framerange,width=4,increment="0.01",from_="0.01",
        to="4.00",bg="#ffffff")
    pglob.Tabs['motif_maker']['pf'].grid(row=0, column=7, sticky=tk.W)
    pglob.Tabs['motif_maker']['pf'].delete(0,tk.END)
    pglob.Tabs['motif_maker']['pf'].insert(0,'2.00')
    
    
    pglob.Tabs['motif_maker']['guinames'] = ('canvas','lresn','resn','lresi',
        'resi','lbackbone','backbone','lchain','chain','curorder','canvasl1',
        'canvasl2','canvas1','canvas2','canvas3','canvasrl','canvasr','canvascl',
        'canvasc','canvasnl','canvasn','canvasbl','canvasb','neworder')
    for name in pglob.Tabs['motif_maker']['guinames']:
        pglob.Tabs['motif_maker'][name] = {}
    
    for i in range(1,11):
        pglob.Tabs['motif_maker']['lresn'][i] = tk.Label(interior, text='%s Residue:'%(i))
        pglob.Tabs['motif_maker']['lresn'][i].grid(row=i, column=0, sticky=tk.E)
        
        pglob.Tabs['motif_maker']['resn'][i] = tk.Entry(interior, width=8)
        pglob.Tabs['motif_maker']['resn'][i].grid(row=i, column=1)
        
        pglob.Tabs['motif_maker']['lchain'][i] = tk.Label(interior, text='Chain:')
        pglob.Tabs['motif_maker']['lchain'][i].grid(row=i, column=2)
        
        pglob.Tabs['motif_maker']['chain'][i] = tk.Entry(interior, width=2)
        pglob.Tabs['motif_maker']['chain'][i].grid(row=i, column=3)
    
        pglob.Tabs['motif_maker']['lresi'][i] = tk.Label(interior, text='Number:')
        pglob.Tabs['motif_maker']['lresi'][i].grid(row=i, column=4)
        
        pglob.Tabs['motif_maker']['resi'][i] = tk.Entry(interior, width=5)
        pglob.Tabs['motif_maker']['resi'][i].grid(row=i, column=5, sticky=tk.W)
        
        pglob.Tabs['motif_maker']['lbackbone'][i] = tk.Label(interior, text='BackBone:')
        pglob.Tabs['motif_maker']['lbackbone'][i].grid(row=i, column=6)
        
        pglob.Tabs['motif_maker']['backbone'][i] = tk.Spinbox(interior,values=('Off','On'),width=3,
            wrap=True,state='readonly',readonlybackground='#ffffff')
        pglob.Tabs['motif_maker']['backbone'][i].grid(row=i, column=7)
        
        pglob.Tabs['motif_maker']['curorder'][i] = i
    
    pglob.Tabs['motif_maker']['canvas'] = tk.Canvas(interior,bd=0)
    pglob.Tabs['motif_maker']['canvas'].grid(row=1, column=0,
        rowspan=10, columnspan=8, sticky=tk.N+tk.E+tk.S+tk.W)
    pglob.Tabs['motif_maker']['canvas'].create_line(0,0,450,0)
    for i in range(1,11):
        g = 22*i
        h = g-12
        pglob.Tabs['motif_maker']['canvasl1'][i] = pglob.Tabs['motif_maker']['canvas'].create_line(0,g-22,450,g-22, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasl2'][i] = pglob.Tabs['motif_maker']['canvas'].create_line(0,g,450,g, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvas1'][i] = pglob.Tabs['motif_maker']['canvas'].create_rectangle(1,g-17,15,g-16, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvas2'][i] = pglob.Tabs['motif_maker']['canvas'].create_rectangle(1,g-13,15,h, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvas3'][i] = pglob.Tabs['motif_maker']['canvas'].create_rectangle(1,g-9,15,g-8, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasrl'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(20, h, text='Residue:', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasr'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(70,
            h, text='', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvascl'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(140, h, text='Chain:', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasc'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(178,
            h, text='', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasnl'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(200, h, text='Number:', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasn'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(248,
            h, text='', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasbl'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(325, h, text='Backbone:', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['canvasb'][i] = pglob.Tabs['motif_maker']['canvas'].create_text(385,
            h, text='', anchor=tk.W, tags='row%s'%i)
        pglob.Tabs['motif_maker']['neworder'][i] = i
    pglob.Tabs['motif_maker']['canvas'].create_line(0,220,450,220)
    pglob.Tabs['motif_maker']['canvas'].grid_remove()
    
    pglob.Tabs['motif_maker']['test'] = tk.Button(interior, text='Test',command=lambda:makemotif(0))
    pglob.Tabs['motif_maker']['test'].grid(row=11, column=4, columnspan=2)
    
    pglob.Tabs['motif_maker']['save'] = tk.Button(interior, text= 'Save', command=lambda:makemotif(1))
    pglob.Tabs['motif_maker']['save'].grid(row=11, column=5, columnspan=2)
    
    pglob.Tabs['motif_maker']['export'] = tk.Button(interior, text= 'Export', command=lambda:makemotif(2))
    pglob.Tabs['motif_maker']['export'].grid(row=11, column=6, columnspan=2, sticky=tk.E)
    
    pglob.Tabs['motif_maker']['clear'] = tk.Button(interior,text='Clear',command=lambda:makemotif(3))
    pglob.Tabs['motif_maker']['clear'].grid(row=11, column=1, sticky=tk.W)
    
    pglob.Tabs['motif_maker']['order'] = tk.Button(interior,text='Order',command=lambda:makemotif(5))
    pglob.Tabs['motif_maker']['order'].grid(row=11, column=0, sticky=tk.W)
    pglob.Tabs['motif_maker']['order']['state'] = tk.DISABLED
    
    pglob.Tabs['motif_maker']['done'] = tk.Button(interior,text='Done',command=lambda:makemotif(5.1))
    pglob.Tabs['motif_maker']['done'].grid(row=11, column=0, sticky=tk.W)
    pglob.Tabs['motif_maker']['done'].grid_remove()
    
    pglob.Tabs['motif_maker']['recommend'] = tk.Button(interior,text='Recommend Order',command=lambda:makemotif(5.2))
    pglob.Tabs['motif_maker']['recommend'].grid(row=11, column=1, columnspan=4, sticky=tk.W)
    pglob.Tabs['motif_maker']['recommend'].grid_remove()
    
    pglob.Tabs['motif_maker']['cancel'] = tk.Button(interior,text='Cancel',command=lambda:makemotif(5.3))
    pglob.Tabs['motif_maker']['cancel'].grid(row=11, column=4, columnspan=2)
    pglob.Tabs['motif_maker']['cancel'].grid_remove()
    
    group = Pmw.Group(pglob.Tabs['motif_maker']['tab'], tag_text='Homolog and Random Testing')
    group.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NW)
    interior = group.interior()
    pglob.Tabs['motif_maker']['radio'] = tk.IntVar()
    
    pglob.Tabs['motif_maker']['testpdb'] = tk.Entry(interior, width=4)
    pglob.Tabs['motif_maker']['testpdb'].grid(row=0, column=1)
    
    hlog = tk.Radiobutton(interior, text="Homolog:",
        variable=pglob.Tabs['motif_maker']['radio'], value=1,
        command=lambda:pglob.Tabs['motif_maker']['testpdb'].config(state=tk.NORMAL))
    hlog.grid(row=0, column=0)
    
    rand = tk.Radiobutton(interior, text="Random",
    variable=pglob.Tabs['motif_maker']['radio'], value=2,
        command=lambda:pglob.Tabs['motif_maker']['testpdb'].config(state=tk.DISABLED))
    rand.grid(row=0, column=2)
    
    hlog.select()
    
    pglob.Tabs['motif_maker']['extest'] = tk.Button(interior, text='Test',command=lambda:makemotif(4))
    pglob.Tabs['motif_maker']['extest'].grid(row=0, column=3)
