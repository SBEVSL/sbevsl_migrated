import Tkinter as tk
from Tkinter import *
from ttk import *
import Pmw
from pmg_tk.startup.treewidgets import widget, node, texttree
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.motif import *
from pmg_tk.startup.ProMol.Methods.local import *
Pmw.initialise()


def initialise():
    group = tk.Frame(glb.GUI.motifs['tab'])
    group.grid(row=0, column=1, rowspan=4, sticky=tk.N+tk.E+tk.S+tk.W)

    glb.GUI.motifs['motifbox'] = tk.Listbox(group, height=20, width=40)
    glb.GUI.motifs['motifbox'].grid(row=1,column=0, sticky=tk.N+tk.E+tk.S+tk.W)

    #creates preliminary empty texttree with  glb.GUI.motifs['motifbox'] as its parent
    glb.GUI.motifs['tt'] = texttree.TextTree(glb.GUI.motifs['motifbox'],funcs={'showContent':showContent})
    glb.GUI.motifs['tt'].pack(expand = YES, fill=BOTH)
    
    group.rowconfigure(0, weight=0)
    group.columnconfigure(1, weight=1)   
    
    group = tk.Frame(glb.GUI.motifs['tab'])
    group.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W, padx=5)
    glb.GUI.motifs['single'] = tk.Label(group, text='Press Start to begin search')
    glb.GUI.motifs['single'].grid(row=0, column=0,columnspan=2)
    glb.GUI.motifs['singlestatus'] = glb.ScalableProgressBar(group)
    glb.GUI.motifs['singlestatus'].getWidget().grid(row=1, column=0, columnspan=2, sticky=tk.E+tk.W)
    glb.GUI.motifs['overall'] = tk.Label(group,text='Overall Progress')
    glb.GUI.motifs['overall'].grid(row=2,column=0,columnspan=2)
    glb.GUI.motifs['overallstatus'] = glb.ScalableProgressBar(group)
    glb.GUI.motifs['overallstatus'].getWidget().grid(row=3, column=0, columnspan=2, sticky=tk.E+tk.W)
    glb.GUI.motifs['findmotif'] = tk.Button(group, text ='Start', 
        command=setChoiceDialogBox)#start button now calls setChoiceDialogBox in motif.py
    glb.GUI.motifs['findmotif'].grid(row=4, column=0, padx=5)#7
    glb.GUI.motifs['cancelbutton'] = tk.Button(group, text='Cancel', command=motifcancel)
    glb.GUI.motifs['cancelbutton'].grid(row=4, column=1, padx=5)#7
    glb.GUI.motifs['cancelbutton']['state'] = tk.DISABLED
    group.columnconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.rowconfigure(0,weight=0)

    # Creates, then hides, the root for the dialog box that allows user to
    # choose a set of motifs to compare to  
    glb.GUI.motifs['root'] = Toplevel(group)
    glb.GUI.motifs['root'].title("Choose A Set")
    glb.GUI.motifs['root'].minsize(200, 200)
    glb.GUI.motifs['root'].withdraw()
    glb.GUI.motifs['var'] = 0
    glb.GUI.motifs['varrmsd'] = 0
    
    group = tk.Frame(glb.GUI.motifs['tab'])
    group.grid(row=1, column=0, sticky=tk.N+tk.E+tk.W+tk.S, padx=5)
    pdbentrylabel = tk.Label(group, text='PDB entries to search (comma separated):', justify=tk.LEFT)
    pdbentrylabel.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.E+tk.W+tk.S)
    ballentrylabel = Pmw.Balloon(group)
    ballentrylabel.bind(pdbentrylabel, \
                        "Type PDB entry codens into the text box or use one of these two buttons")
    # button to load a PDB file from system
    glb.GUI.motifs['browseButton'] = tk.Button(group, text='PDB file name ...', command=loadlocal)
    glb.GUI.motifs['browseButton'].grid(row=1, column=0, padx=1, sticky=tk.N+tk.W)
    ballbrowsebut = Pmw.Balloon(group)
    ballbrowsebut.bind(glb.GUI.motifs['browseButton'], \
                       "Browse for a PDB entry")
    # button to load a list of PDB files
    glb.GUI.motifs['uploadTxtButton'] = tk.Button(group, text='PDB entry list ...', command=askopenfilename)
    glb.GUI.motifs['uploadTxtButton'].grid(row=1, column=2, columnspan=2, padx=1, sticky=tk.N+tk.E)
    balluploadbut = Pmw.Balloon(group)
    balluploadbut.bind(glb.GUI.motifs['uploadTxtButton'], \
                       "Browse for a list of PDB entries\none per line, no commas")
    pdbscroll = tk.Scrollbar(group, orient=tk.VERTICAL)
    pdbscroll.grid(row=2, column=3, sticky=tk.N+tk.S)
    glb.GUI.motifs['multipdb'] = tk.Text(group, state=tk.NORMAL, wrap=tk.WORD, width=12, height=14, yscrollcommand=pdbscroll.set)
    glb.GUI.motifs['multipdb'].grid(row=2, column=0, columnspan=3,sticky=tk.N+tk.E+tk.W)
    pdbscroll['command'] = glb.GUI.motifs['multipdb'].yview
    # button to clear the input textbox
    glb.GUI.motifs['clearButton'] = tk.Button(group, text='Clear input', command=clearpdbinput)
    glb.GUI.motifs['clearButton'].grid(row=3, column=0, padx=1, sticky=tk.N+tk.W)
    # button to export results
    glb.GUI.motifs['exportButton'] = tk.Button(group, text='Export ...', command=exportAllResults, state=tk.DISABLED)
    glb.GUI.motifs['exportButton'].grid(row=3, column=2, columnspan=2, padx=1, sticky=tk.N+tk.E)
    group.columnconfigure(0, weight=1)
    group.columnconfigure(1, weight=1)
    group.columnconfigure(2, weight=1)
    group.columnconfigure(3, weight=0)
    group.rowconfigure(1, weight=0)

    #group = tk.LabelFrame(glb.GUI.motifs['tab'], text='Tools')
    toolgroup = tk.LabelFrame(group,text='Tools')
    #group.grid(row=2, column=0, sticky=tk.N, padx=5)
    toolgroup.grid(row=4, column=1, columnspan=3, sticky=tk.N+tk.E+tk.W, padx=5)
    
    #labrange = tk.Label(group, text='Precision Factor:')
    labrange = tk.Label(toolgroup, text='Precision Factor:')
    labrange.grid(row=0, column=0, sticky=tk.E+tk.N)

    ballrange = Pmw.Balloon(toolgroup)
    glb.GUI.motifs['delta'] = tk.Spinbox(toolgroup, width=4,
        bg="#ffffff", increment="0.01", from_="0.01", to="2.00")
    ballrange.bind(glb.GUI.motifs['delta'], 'Multiplier for default measured values')
    glb.GUI.motifs['delta'].grid(row=0, column=1, sticky=tk.W+tk.N)
    glb.GUI.motifs['delta'].delete(0,4)
    glb.GUI.motifs['delta'].insert(0,'1.00')
 
    glb.GUI.motifs['align'] = tk.IntVar()
    alignbox = tk.Checkbutton(toolgroup, text="Show alignment",
        variable=glb.GUI.motifs['align'], command=togglealign)
    alignbox.grid(row=1, column=0, columnspan=2,sticky=tk.N)

    glb.GUI.motifs['rmsd'] = tk.IntVar()
    rmsdbox = tk.Checkbutton(toolgroup, text="Calculate RMSD", variable=glb.GUI.motifs['rmsd'])
    rmsdbox.grid(row=2, column=0, columnspan=2, sticky=tk.N)
    
    
    glb.GUI.motifs['ec1'] = StringVar()
    glb.GUI.motifs['ec2'] = StringVar()
    glb.GUI.motifs['ec3'] = StringVar()
    glb.GUI.motifs['ec4'] = StringVar()
    
    glb.GUI.motifs['motifColorLabel'] = tk.Label(toolgroup, text="Motif Color")
    glb.GUI.motifs['motifColorLabel'].grid(row=3, column=0, sticky=tk.E)
    glb.GUI.motifs['motifcolor'] = tk.Label(toolgroup, bg='#ffffff', bd=3, relief=tk.SUNKEN)
    glb.GUI.motifs['motifcolor'].grid(row=3,column=1, sticky=tk.N+tk.E+tk.W, padx=2, pady=2)
    
    glb.GUI.motifs['queryColorLabel'] = tk.Label(toolgroup, text="Match Color")
    glb.GUI.motifs['queryColorLabel'].grid(row=4, column=1, sticky=tk.E)
    glb.GUI.motifs['querycolor'] = tk.Label(toolgroup, bg='#ff0000', bd=3, relief=tk.SUNKEN)
    glb.GUI.motifs['querycolor'].grid(row=4,column=1, sticky=tk.N+tk.E+tk.W, padx=2, pady=2)
    
    glb.GUI.motifs['motifColorLabel'].grid_remove()
    glb.GUI.motifs['motifcolor'].grid_remove()
    
    glb.GUI.motifs['querycolor'].bind("<ButtonRelease-1>", changecolor)
    glb.GUI.motifs['motifcolor'].bind("<ButtonRelease-1>", changecolor)

    group.rowconfigure(2,weight=0)

    
    # Configure motif finder GUI layout
    glb.GUI.motifs['tab'].columnconfigure(0, weight=3)
    glb.GUI.motifs['tab'].columnconfigure(1, weight=1)
    glb.GUI.motifs['tab'].rowconfigure(1, weight=1)
