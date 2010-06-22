from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as pglob
from pmg_tk.startup.ProMol.Methods.motif import *
Pmw.initialise()

def initialise():
    pglob.GUI['motif_maker']['maker'] = tk.LabelFrame(pglob.GUI['motif_maker']['tab'], text='Motif Maker')
    pglob.GUI['motif_maker']['maker'].grid(row=0, column=0, padx=0, pady=0)
    
    lpdb = tk.Label(pglob.GUI['motif_maker']['maker'], text='PDB:')
    lpdb.grid(row=0, column=0, sticky=tk.E)
    
    pglob.GUI['motif_maker']['pdb'] = tk.Entry(pglob.GUI['motif_maker']['maker'], width=4)
    pglob.GUI['motif_maker']['pdb'].grid(row=0, column=1, sticky=tk.W)
    
    lec = tk.Label(pglob.GUI['motif_maker']['maker'], text='EC #:')
    lec.grid(row=0, column=2, sticky=tk.E)
    
    pglob.GUI['motif_maker']['ec'] = tk.Entry(pglob.GUI['motif_maker']['maker'], width=10)
    pglob.GUI['motif_maker']['ec'].grid(row=0, column=3, columnspan=2, sticky=tk.W)
    
    labrange = tk.Label(pglob.GUI['motif_maker']['maker'], text='Precision Factor:')
    labrange.grid(row=0, column=5,columnspan=2, sticky=tk.E)
        
    framerange = tk.Frame(pglob.GUI['motif_maker']['maker'])
    framerange.grid(row=0, column=7,sticky=tk.W)
    ballrange = Pmw.Balloon(pglob.GUI['motif_maker']['maker'])
    ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault= 2')
    pglob.GUI['motif_maker']['pf'] = tk.Spinbox(framerange,width=4,increment="0.01",from_="0.01",
        to="4.00",bg="#ffffff")
    pglob.GUI['motif_maker']['pf'].grid(row=0, column=7, sticky=tk.W)
    pglob.GUI['motif_maker']['pf'].delete(0,tk.END)
    pglob.GUI['motif_maker']['pf'].insert(0,'2.00')
    
    
    pglob.GUI['motif_maker']['guinames'] = ('canvas','resn','resi','backbone',
        'chain','curorder','neworder')
    for name in pglob.GUI['motif_maker']['guinames']:
        pglob.GUI['motif_maker'][name] = {}
    
    for i in range(1,11):
        tk.Label(pglob.GUI['motif_maker']['maker'], text='%s Residue:'%(i)).grid(row=i, column=0, sticky=tk.E)
        
        pglob.GUI['motif_maker']['resn'][i] = tk.Entry(pglob.GUI['motif_maker']['maker'], width=8)
        pglob.GUI['motif_maker']['resn'][i].grid(row=i, column=1)
        
        tk.Label(pglob.GUI['motif_maker']['maker'], text='Chain:').grid(row=i, column=2)
        
        pglob.GUI['motif_maker']['chain'][i] = tk.Entry(pglob.GUI['motif_maker']['maker'], width=2)
        pglob.GUI['motif_maker']['chain'][i].grid(row=i, column=3)
    
        tk.Label(pglob.GUI['motif_maker']['maker'], text='Number:').grid(row=i, column=4)
        
        pglob.GUI['motif_maker']['resi'][i] = tk.Entry(pglob.GUI['motif_maker']['maker'], width=5)
        pglob.GUI['motif_maker']['resi'][i].grid(row=i, column=5, sticky=tk.W)
        
        tk.Label(pglob.GUI['motif_maker']['maker'], text='BackBone:').grid(row=i, column=6)
        
        pglob.GUI['motif_maker']['backbone'][i] = tk.Spinbox(pglob.GUI['motif_maker']['maker'],values=('Off','On'),width=3,
            wrap=True,state='readonly',readonlybackground='#ffffff')
        pglob.GUI['motif_maker']['backbone'][i].grid(row=i, column=7)
        
        pglob.GUI['motif_maker']['curorder'][i] = i
        pglob.GUI['motif_maker']['neworder'][i] = i
    
    pglob.GUI['motif_maker']['canvas'] = tk.Canvas(pglob.GUI['motif_maker']['maker'],bd=0)
    pglob.GUI['motif_maker']['canvas'].grid(row=1, column=0,
        rowspan=10, columnspan=8, sticky=tk.N+tk.E+tk.S+tk.W)
    pglob.GUI['motif_maker']['canvas'].create_line(0,0,450,0)
    for i in range(1,11):
        g = 22*i
        h = g-12
        pglob.GUI['motif_maker']['canvas'].create_line(0,g-22,450,g-22, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_line(0,g,450,g, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_polygon(7,g-22,2,g-12,13,g-12, tags=('up','row%s'%i))
        pglob.GUI['motif_maker']['canvas'].create_polygon(7,g,2,g-10,13,g-10, tags=('down','row%s'%i))
        pglob.GUI['motif_maker']['canvas'].create_text(20, h, text='Residue:', anchor=tk.W, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_text(70, h, text='', anchor=tk.W, tags=('resn%s'%i,'row%s'%i))
        pglob.GUI['motif_maker']['canvas'].create_text(140, h, text='Chain:', anchor=tk.W, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_text(178, h, text='', anchor=tk.W, tags=('chain%s'%i,'row%s'%i))
        pglob.GUI['motif_maker']['canvas'].create_text(200, h, text='Number:', anchor=tk.W, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_text(248, h, text='', anchor=tk.W, tags=('resi%s'%i,'row%s'%i))
        pglob.GUI['motif_maker']['canvas'].create_text(325, h, text='Backbone:', anchor=tk.W, tags='row%s'%i)
        pglob.GUI['motif_maker']['canvas'].create_text(385, h, text='', anchor=tk.W, tags=('back%s'%i,'row%s'%i))
    
    pglob.GUI['motif_maker']['canvas'].create_line(0,220,450,220)
    pglob.GUI['motif_maker']['canvas'].grid_remove()
    
    pglob.GUI['motif_maker']['test'] = tk.Button(pglob.GUI['motif_maker']['maker'], text='Test',command=lambda:makemotif(0))
    pglob.GUI['motif_maker']['test'].grid(row=11, column=4, columnspan=2)
    
    pglob.GUI['motif_maker']['save'] = tk.Button(pglob.GUI['motif_maker']['maker'], text= 'Save', command=lambda:makemotif(1))
    pglob.GUI['motif_maker']['save'].grid(row=11, column=5, columnspan=2)
    
    pglob.GUI['motif_maker']['export'] = tk.Button(pglob.GUI['motif_maker']['maker'], text= 'Export', command=lambda:makemotif(2))
    pglob.GUI['motif_maker']['export'].grid(row=11, column=6, columnspan=2, sticky=tk.E)
    
    pglob.GUI['motif_maker']['clear'] = tk.Button(pglob.GUI['motif_maker']['maker'],text='Clear',command=lambda:makemotif(3))
    pglob.GUI['motif_maker']['clear'].grid(row=11, column=1, sticky=tk.W)
    
    pglob.GUI['motif_maker']['order'] = tk.Button(pglob.GUI['motif_maker']['maker'],text='Order',command=lambda:makemotif(5))
    pglob.GUI['motif_maker']['order'].grid(row=11, column=0, sticky=tk.W)
    #pglob.GUI['motif_maker']['order']['state'] = tk.DISABLED
    
    pglob.GUI['motif_maker']['done'] = tk.Button(pglob.GUI['motif_maker']['maker'],text='Done',command=lambda:makemotif(5.1))
    pglob.GUI['motif_maker']['done'].grid(row=11, column=0, sticky=tk.W)
    pglob.GUI['motif_maker']['done'].grid_remove()
    
    pglob.GUI['motif_maker']['recommend'] = tk.Button(pglob.GUI['motif_maker']['maker'],text='Recommend Order',command=lambda:makemotif(5.2))
    pglob.GUI['motif_maker']['recommend'].grid(row=11, column=1, columnspan=4, sticky=tk.W)
    pglob.GUI['motif_maker']['recommend']['state'] = tk.DISABLED
    pglob.GUI['motif_maker']['recommend'].grid_remove()
    
    pglob.GUI['motif_maker']['cancel'] = tk.Button(pglob.GUI['motif_maker']['maker'],text='Cancel',command=lambda:makemotif(5.3))
    pglob.GUI['motif_maker']['cancel'].grid(row=11, column=4, columnspan=2)
    pglob.GUI['motif_maker']['cancel'].grid_remove()
    
    group = tk.LabelFrame(pglob.GUI['motif_maker']['tab'], text='Homolog and Random Testing')
    group.grid(row=1, column=0, padx=0, pady=0, sticky=tk.NW)
    pglob.GUI['motif_maker']['radio'] = tk.IntVar()
    
    pglob.GUI['motif_maker']['testpdb'] = tk.Entry(group, width=4)
    pglob.GUI['motif_maker']['testpdb'].grid(row=0, column=1)
    
    hlog = tk.Radiobutton(group, text="Homolog:",
        variable=pglob.GUI['motif_maker']['radio'], value=1,
        command=lambda:pglob.GUI['motif_maker']['testpdb'].config(state=tk.NORMAL))
    hlog.grid(row=0, column=0)
    
    rand = tk.Radiobutton(group, text="Random",
    variable=pglob.GUI['motif_maker']['radio'], value=2,
        command=lambda:pglob.GUI['motif_maker']['testpdb'].config(state=tk.DISABLED))
    rand.grid(row=0, column=2)
    
    hlog.select()
    
    pglob.GUI['motif_maker']['extest'] = tk.Button(group, text='Test',command=lambda:makemotif(4))
    pglob.GUI['motif_maker']['extest'].grid(row=0, column=3)
