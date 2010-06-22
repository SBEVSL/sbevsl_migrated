import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as pglob
from pmg_tk.startup.ProMol.Methods.motif import *
from pmg_tk.startup.ProMol.Methods.utility import *
Pmw.initialise()

def initialise():
    group = tk.LabelFrame(pglob.GUI['motifs']['tab'], text='Motif Finder')
    group.grid(row=0, column=1, rowspan=4)
    
    xscroll = tk.Scrollbar(group, orient=tk.HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=tk.E+tk.W)
    yscroll = tk.Scrollbar(group, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
    pglob.GUI['motifs']['motifbox'] = tk.Listbox(group, height=20, width=40,
        xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    pglob.GUI['motifs']['hidmotif'] = tk.Listbox(group)
    pglob.GUI['motifs']['motifbox'].grid(row=0,column=0,sticky=tk.E)
    xscroll["command"] = pglob.GUI['motifs']['motifbox'].xview
    yscroll["command"] = pglob.GUI['motifs']['motifbox'].yview
    pglob.GUI['motifs']['motifbox'].bind('<Double-Button-1>',dbckmotif)
    
    group = tk.LabelFrame(pglob.GUI['motifs']['tab'])
    group.grid(row=0, column=0)
    pglob.GUI['motifs']['single'] = tk.Label(group, text='Press Start to begin search')
    pglob.GUI['motifs']['single'].grid(row=0, column=0,columnspan=2)
    pglob.GUI['motifs']['singlestatus'] = pglob.ProgressBar(group,10,200,1,0,2)
    pglob.GUI['motifs']['overall'] = tk.Label(group,text='Press Start to begin search')
    pglob.GUI['motifs']['overall'].grid(row=2,column=0,columnspan=2)
    pglob.GUI['motifs']['overallstatus'] = pglob.ProgressBar(group,10,200,3,0,2)
    pglob.GUI['motifs']['findmotif'] = tk.Button(group, text ='Start', 
        command=motifchecker)
    pglob.GUI['motifs']['findmotif'].grid(row=4, column=0)
    pglob.GUI['motifs']['cancelbutton'] = tk.Button(group, width=12, text='Cancel', command=motifcancel)
    pglob.GUI['motifs']['cancelbutton'].grid(row=4, column=1)
    pglob.GUI['motifs']['cancelbutton']['state'] = tk.DISABLED
    
    group = tk.LabelFrame(pglob.GUI['motifs']['tab'], text='PDB(s) to search\n(comma separated)')
    group.grid(row=1, column=0)
    pglob.GUI['motifs']['multipdb'] = tk.Text(group, state=tk.NORMAL, 
        width=28, height=4)
    pglob.GUI['motifs']['multipdb'].grid(row=1, column=0)
    
    group = tk.LabelFrame(pglob.GUI['motifs']['tab'], text='Export')
    group.grid(row=2, column=0)
    pglob.GUI['motifs']['csv'] = tk.Button(group, text ='CSV', 
        command=export2csv, state=tk.DISABLED)
    pglob.GUI['motifs']['csv'].grid(row = 0, column = 1, padx=5, pady=5)
    
    #pglob.GUI['motifs']['ods'] = tk.Button(group, text ='ODS', 
    #    command=export2ods, state=tk.DISABLED)
    #pglob.GUI['motifs']['ods'].grid(row = 0, column = 2, padx=5, pady=5)   
    
    group = tk.LabelFrame(pglob.GUI['motifs']['tab'], text='Tools')
    group.grid(row=3, column=0)
    
    labrange = tk.Label(group, text='Precision Factor:')
    labrange.grid(row=1, column=0, sticky=tk.W)

    framerange = tk.Frame(group)
    framerange.grid(row=1, column=1, sticky=tk.N)
    ballrange = Pmw.Balloon(group)
    ballrange.bind(framerange, 'Multiplier for default measured values')
    pglob.GUI['motifs']['delta'] = tk.Spinbox(framerange, width=4,
        bg="#ffffff", increment="0.01", from_="0.01", to="2.00")
    pglob.GUI['motifs']['delta'].grid(row=1, column=1, sticky=tk.N)
    pglob.GUI['motifs']['delta'].delete(0,4)
    pglob.GUI['motifs']['delta'].insert(0,'1.00')
    
    labrandom = tk.Label(group, text='Random PDB:')
    labrandom.grid(row=2, column=0, sticky=tk.SW)
    
    random = tk.Button(group, text='Get Random PDB', width=25, command=randompdb)
    random.grid(row=3, column=0, columnspan=3, sticky=tk.N)
