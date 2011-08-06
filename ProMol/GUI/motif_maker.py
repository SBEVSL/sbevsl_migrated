from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.motif import *
Pmw.initialise()

def initialise():
    glb.GUI.motif_maker['maker'] = tk.LabelFrame(glb.GUI.motif_maker['tab'], text='Motif Maker')
    glb.GUI.motif_maker['maker'].grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
    
    lpdb = tk.Label(glb.GUI.motif_maker['maker'], text='PDB:')
    lpdb.grid(row=0, column=0, sticky=tk.E)
    
    glb.GUI.motif_maker['pdb'] = tk.Entry(glb.GUI.motif_maker['maker'], width=4)
    glb.GUI.motif_maker['pdb'].grid(row=0, column=1, sticky=tk.E+tk.W)
    
    lec = tk.Label(glb.GUI.motif_maker['maker'], text='EC #:')
    lec.grid(row=0, column=2, sticky=tk.E)
    
    glb.GUI.motif_maker['ec'] = tk.Entry(glb.GUI.motif_maker['maker'], width=10)
    glb.GUI.motif_maker['ec'].grid(row=0, column=3, columnspan=2, sticky=tk.E+tk.W)
    
    labrange = tk.Label(glb.GUI.motif_maker['maker'], text='Tolerance:')
    labrange.grid(row=0, column=5,columnspan=2, sticky=tk.E)

    glb.GUI.motif_maker['pf'] = tk.Spinbox(glb.GUI.motif_maker['maker'],width=4,increment="0.01",from_="0.01",
        to="4.00",bg="#ffffff")
    ballrange = Pmw.Balloon(glb.GUI.motif_maker['maker'])
    ballrange.bind(glb.GUI.motif_maker['pf'], 'Changes precision of motif definition\nby expanding the search radii.\n(Default is 2)')
    glb.GUI.motif_maker['pf'].grid(row=0, column=7, sticky=tk.W)
    glb.GUI.motif_maker['pf'].delete(0,tk.END)
    glb.GUI.motif_maker['pf'].insert(0,'2.00')
    
    
    glb.GUI.motif_maker['guinames'] = ('resn','resi','backbone',
        'chain')
    for name in glb.GUI.motif_maker['guinames']:
        glb.GUI.motif_maker[name] = {}
    
    glb.GUI.motif_maker['maker'].rowconfigure(0, weight=1)
    
    for i in range(1,11):
        glb.GUI.motif_maker['maker'].rowconfigure(i, weight=1)
        tk.Label(glb.GUI.motif_maker['maker'], text='%s Residue:'%(i)).grid(row=i, column=0, sticky=tk.E)
        
        glb.GUI.motif_maker['resn'][i] = tk.Entry(glb.GUI.motif_maker['maker'], width=8)
        glb.GUI.motif_maker['resn'][i].grid(row=i, column=1, sticky=tk.E+tk.W)
        
        tk.Label(glb.GUI.motif_maker['maker'], text='Chain:').grid(row=i, column=2, sticky=tk.E)
        
        glb.GUI.motif_maker['chain'][i] = tk.Entry(glb.GUI.motif_maker['maker'], width=2)
        glb.GUI.motif_maker['chain'][i].grid(row=i, column=3, sticky=tk.E+tk.W)
    
        tk.Label(glb.GUI.motif_maker['maker'], text='Number:').grid(row=i, column=4, sticky=tk.E)
        
        glb.GUI.motif_maker['resi'][i] = tk.Entry(glb.GUI.motif_maker['maker'], width=5)
        glb.GUI.motif_maker['resi'][i].grid(row=i, column=5, sticky=tk.E+tk.W)
        
        tk.Label(glb.GUI.motif_maker['maker'], text='Backbone:').grid(row=i, column=6, sticky=tk.E)
        
        glb.GUI.motif_maker['backbone'][i] = tk.Spinbox(glb.GUI.motif_maker['maker'],values=('Off','On'),width=3,
            wrap=True,state='readonly',readonlybackground='#ffffff')
        glb.GUI.motif_maker['backbone'][i].grid(row=i, column=7, sticky=tk.W)
        
        # Deleted canvas
    
    glb.GUI.motif_maker['maker'].columnconfigure(1, weight=1)
    glb.GUI.motif_maker['maker'].columnconfigure(3, weight=1)
    glb.GUI.motif_maker['maker'].columnconfigure(5, weight=1)
    
    # I know this should really use a singleton Motif Maker, but the MM refactor was kind of quick and dirty
    # It's better, but not perfect, so it still acts procedural
    # It's safer to use instances once and throw them away in case I missed an initializer or something
    # That way, any errors that don't show up the first time won't show up later
    
    buttonFrame = tk.Frame(glb.GUI.motif_maker['maker'])
    buttonFrame.grid(row=11, column=0, columnspan=8, sticky=tk.S+tk.E+tk.W)
    
    glb.GUI.motif_maker['clear'] = tk.Button(buttonFrame,text='Clear',command=lambda:MotifMaker().clear())
    glb.GUI.motif_maker['clear'].pack(side=tk.LEFT)

    glb.GUI.motif_maker['save'] = tk.Button(buttonFrame, text= 'Save', command=lambda:MotifMaker().saveMotif())
    glb.GUI.motif_maker['save'].pack(side=tk.RIGHT)
    
    glb.GUI.motif_maker['export'] = tk.Button(buttonFrame, text= 'Export', command=lambda:MotifMaker().exportMotif())
    glb.GUI.motif_maker['export'].pack(side=tk.RIGHT)
    
    group = tk.LabelFrame(glb.GUI.motif_maker['tab'], text='Testing')
    group.grid(row=1, column=0, sticky=tk.E+tk.S+tk.W)
    glb.GUI.motif_maker['radio'] = tk.IntVar()

    matchColorLabel = tk.Label(group, text="Match color:")
    matchColorLabel.grid(row=1, column=0, sticky=tk.W)
    glb.GUI.motif_maker['matchcolor'] = tk.Label(group, bg='#ff0000', bd=3, relief=tk.RIDGE)
    glb.GUI.motif_maker['matchcolor'].grid(row=1,column=1, sticky=tk.N+tk.E+tk.S+tk.W, padx=2, pady=2)
    glb.GUI.motif_maker['matchcolor'].bind("<ButtonRelease-1>", changecolor)
    
    tk.Label(group, text='Test against:').grid(row=0, column=0, sticky=tk.W)
    
    selfTest = tk.Radiobutton(group, text='Self',
        variable=glb.GUI.motif_maker['radio'], value=0,
        command=lambda:glb.GUI.motif_maker['testpdb'].config(state=tk.DISABLED))
    selfTest.grid(row=0, column=1)
        
    hlog = tk.Radiobutton(group, text="Homolog:",
        variable=glb.GUI.motif_maker['radio'], value=1,
        command=lambda:glb.GUI.motif_maker['testpdb'].config(state=tk.NORMAL))
    hlog.grid(row=0, column=2, sticky=tk.E)
    
    glb.GUI.motif_maker['testpdb'] = tk.Entry(group, width=4, state=tk.DISABLED)
    glb.GUI.motif_maker['testpdb'].grid(row=0, column=3, sticky=tk.E+tk.W)

    rand = tk.Radiobutton(group, text="Random",
        variable=glb.GUI.motif_maker['radio'], value=2,
        command=lambda:glb.GUI.motif_maker['testpdb'].config(state=tk.DISABLED))
    rand.grid(row=0, column=4)
    
    selfTest.select()
        
    glb.GUI.motif_maker['extest'] = tk.Button(group, text='Test',command=lambda:MotifMaker().testMotif())
    glb.GUI.motif_maker['extest'].grid(row=1, column=4, sticky=tk.E)

    group.columnconfigure(1, weight=1)
    group.columnconfigure(2, weight=1)
    group.columnconfigure(3, weight=4)
    group.columnconfigure(4, weight=1)
    group.rowconfigure(0, weight=0)
    group.rowconfigure(1, weight=1)
    
    glb.GUI.motif_maker['tab'].rowconfigure(0, weight=1)
    glb.GUI.motif_maker['tab'].columnconfigure(0, weight=1)
