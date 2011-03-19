import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.motif import *
from pmg_tk.startup.ProMol.Methods.ftp import *
Pmw.initialise()

def initialise():
    group = tk.LabelFrame(glb.GUI.motifs['tab'], text='Motif Finder')
    group.grid(row=0, column=1, rowspan=4)
    
    xscroll = tk.Scrollbar(group, orient=tk.HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=tk.E+tk.W)
    yscroll = tk.Scrollbar(group, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
    glb.GUI.motifs['motifbox'] = tk.Listbox(group, height=20, width=40,
        xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    glb.GUI.motifs['hidmotif'] = tk.Listbox(group)
    glb.GUI.motifs['motifbox'].grid(row=0,column=0,sticky=tk.E)
    xscroll["command"] = glb.GUI.motifs['motifbox'].xview
    yscroll["command"] = glb.GUI.motifs['motifbox'].yview
    glb.GUI.motifs['motifbox'].bind('<Double-Button-1>',dbckmotif)
    
    group = tk.LabelFrame(glb.GUI.motifs['tab'])
    group.grid(row=0, column=0)
    glb.GUI.motifs['single'] = tk.Label(group, text='Press Start to begin search')
    glb.GUI.motifs['single'].grid(row=0, column=0,columnspan=2)
    glb.GUI.motifs['singlestatus'] = glb.ProgressBar(group,10,200,1,0,2)
    glb.GUI.motifs['overall'] = tk.Label(group,text='Press Start to begin search')
    glb.GUI.motifs['overall'].grid(row=2,column=0,columnspan=2)
    glb.GUI.motifs['overallstatus'] = glb.ProgressBar(group,10,200,3,0,2)
    glb.GUI.motifs['findmotif'] = tk.Button(group, text ='Start', 
        command=motifchecker)
    glb.GUI.motifs['findmotif'].grid(row=4, column=0)
    glb.GUI.motifs['cancelbutton'] = tk.Button(group, width=12, text='Cancel', command=motifcancel)
    glb.GUI.motifs['cancelbutton'].grid(row=4, column=1)
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
    
    group = tk.LabelFrame(glb.GUI.motifs['tab'], text='PDB(s) to search\n(comma separated)')
    group.grid(row=1, column=0)
    glb.GUI.motifs['multipdb'] = tk.Text(group, state=tk.NORMAL, 
        width=28, height=4)
    glb.GUI.motifs['multipdb'].grid(row=1, column=0)
    glb.GUI.motifs['openfile'] = tk.Button(group, text ='Open File', command=openfile)
    glb.GUI.motifs['openfile'].grid(row=1, column=1)   
    
    #FTP GUI Code
    glb.GUI.motifs['ftptxt'] = tk.Entry(group, state=tk.NORMAL, width=28)
    glb.GUI.motifs['ftptxt'].bind('<Return>', openftp)
    glb.GUI.motifs['ftptxt'].grid(row=2, column=0)
    glb.GUI.motifs['openftp'] = tk.Button(group, text ='Open FTP', command=openftp)
    glb.GUI.motifs['openftp'].grid(row=2, column=1)
    glb.GUI.motifs['ftppath'] = tk.Entry(group, state=tk.NORMAL, width=25)
    glb.GUI.motifs['ftppath'].grid(row=3, column=0)
    glb.GUI.motifs['up'] = tk.Button(group, text ='<--', command=ftpup)
    glb.GUI.motifs['up'].grid(row=3, column=1)
    fscroll = tk.Scrollbar(group, orient=tk.VERTICAL)
    fscroll.grid(row=4, column=1, sticky=tk.N+tk.S)
    glb.GUI.motifs['ftplist'] = tk.Listbox(group, width=25, height=8, yscrollcommand=fscroll.set)
    glb.GUI.motifs['ftplist'].grid(row=4, column=0, sticky=tk.E)
    glb.GUI.motifs['ftplist'].bind('<Double-Button-1>',ftpcd)
    fscroll["command"] = glb.GUI.motifs['ftplist'].yview
    glb.GUI.motifs['opendir'] = tk.Button(group, text ='Open', command=openftpdir)
    glb.GUI.motifs['opendir'].grid(row=4, column=2)
    #End FTP Code
    
    group = tk.LabelFrame(glb.GUI.motifs['tab'], text='Export')
    group.grid(row=2, column=0)
    glb.GUI.motifs['csv'] = tk.Button(group, text ='CSV', 
        command=export2csv, state=tk.DISABLED)
    glb.GUI.motifs['csv'].grid(row = 0, column = 1, padx=5, pady=5)
    
    #glb.GUI.motifs['ods'] = tk.Button(group, text ='ODS', 
    #    command=export2ods, state=tk.DISABLED)
    #glb.GUI.motifs['ods'].grid(row = 0, column = 2, padx=5, pady=5)   
    
    group = tk.LabelFrame(glb.GUI.motifs['tab'], text='Tools')
    group.grid(row=3, column=0)
    
    labrange = tk.Label(group, text='Precision Factor:')
    labrange.grid(row=1, column=0, sticky=tk.W)

    framerange = tk.Frame(group)
    framerange.grid(row=1, column=1, sticky=tk.N)
    ballrange = Pmw.Balloon(group)
    ballrange.bind(framerange, 'Multiplier for default measured values')
    glb.GUI.motifs['delta'] = tk.Spinbox(framerange, width=4,
        bg="#ffffff", increment="0.01", from_="0.01", to="2.00")
    glb.GUI.motifs['delta'].grid(row=1, column=1, sticky=tk.N)
    glb.GUI.motifs['delta'].delete(0,4)
    glb.GUI.motifs['delta'].insert(0,'1.00')
    
    glb.GUI.motifs['align'] = tk.IntVar()
    alignbox = tk.Checkbutton(group, text="Show alignment?",
        variable=glb.GUI.motifs['align'])
    alignbox.grid(row=2, column=0)
    alignbox.bind("<ButtonRelease-1>", togglealign)
    
    tempcollab = tk.Label(group, text="Template Color")
    tempcollab.grid(row=3, column=0, sticky=tk.E)
    glb.GUI.motifs['templatecolor'] = tk.Canvas(group, bg='#ffffff', width=50,
        height=25, bd=3, relief=tk.SUNKEN)
    glb.GUI.motifs['templatecolor'].grid(row=3,column=1)
    
    motcollab = tk.Label(group, text="Motif Color")
    motcollab.grid(row=4, column=0, sticky=tk.E)
    glb.GUI.motifs['motifcolor'] = tk.Canvas(group, bg='#ff0000', width=50,
        height=25, bd=3, relief=tk.SUNKEN)
    glb.GUI.motifs['motifcolor'].grid(row=4,column=1)    
    
