from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods.motif import *
from pmg_tk.startup.ProMol.Methods.setting import *
from pmg_tk.startup.ProMol.Methods.utility import *
Pmw.initialise()

def initialise():
    #------------------External Resources------------------#
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Resources')
    group.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=NE)
    pdber = Entry(group, width = 4)
    pdber.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
    pdberlab = Label(group, text = 'PDB code')
    pdberlab.grid(row=0, column=0, padx=1, pady=1, sticky=NW)
    seqget = Button(group, width = 12, text = 'PDB sequence')
    seqget.grid(row=0, column=1, padx=1, pady=1, sticky=NW)
    seqget.bind('<Button-1>', getsequence)

    fasta = Button(group, width = 5, text = 'FASTA')
    fasta.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    fasta.bind('<Button-1>', gotofasta)
    abstracter = Button(group, width = 12, text = 'PDB Abstract')
    abstracter.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
    abstracter.bind('<Button-1>', getabstract)
    rcsb = Button(group, width = 5, text = 'RCSB')
    rcsb.grid(row=1, column=2, padx=1, pady=1, sticky=NW)
    rcsb.bind('<Button-1>', gotorcsb)

    #--------------Electrostatics-------------#

    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Electrostatics')
    group.grid(row=2, column=0, columnspan=3, padx=2, pady=2, sticky=NW)
    labelaa = Label(group, text = 'Code:')
    frameelec = Frame(group, width=16)
    frameelec.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    ballelec = Pmw.Balloon(group)
    ballelec.bind(frameelec, "Enter PDB Code: of Loaded Protein.\nCase Sensitive.")
    elecbtn = Button(frameelec, text =  'Electrostatics', width=16)
    elecbtn.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    entelc = Entry(group, width =6)
    entelc.grid(row=0, column=1, sticky=E)
    elelabel = Label(group, text='PDB Code:')
    elelabel.grid(row=0, column=0, sticky=W)
    elecbtn.bind('<Button-1>', seq)
    framecdel = Frame(group)
    framecdel.grid(row=0, column=3, padx=1, pady=1, sticky=NW)
    ballcdel = Pmw.Balloon(group)
    ballcdel.bind(framecdel, 'Removes the current PDB Electrostatics')
    elecdel = Button(framecdel, width = 8, text = 'Remove')
    elecdel.grid(row=0, column=3, padx=1, pady=1, sticky=NW)
    elecdel.bind('<Button-1>', delelectro)


    #---------Orthoscopic view and View distance-----#
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Perspective')
    group.grid(row=1, column=1, padx=0, pady=0, sticky=NW)
    frameorthoon = Frame(group, width = 16)
    frameorthoon.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
    balloonorth = Pmw.Balloon(group)
    balloonorth.bind(frameorthoon, "Gives correct proportions to view.")
    frameorthoff = Frame(group,width = 16)
    frameorthoff.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
    balloonorthoff = Pmw.Balloon(group)
    balloonorthoff.bind(frameorthoff, "Gives greater distance perspective.")
    orthoon = Button(frameorthoon, text = 'Orthoscopic On', width = 16)
    orthoon.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
    viewsetter = Label(group, text = 'Set Field of View')
    viewsetter.grid(row=2, column=0, padx=0, pady=0, sticky=N)


    orthoon.bind('<Button-1>', turnorthon)
    orthoff = Button(frameorthoff, text = 'Orthoscopic Off',width = 16)
    orthoff.grid(row=1, column=0, padx=2, pady=2, sticky=NW)

    orthoff.bind('<Button-1>', turnorthoff)
    framefieldview = Frame(group)
    framefieldview.grid(row=3, column=0, padx=2, pady=2, sticky='N')
    balloonview = Pmw.Balloon(group)
    balloonview.bind(framefieldview, "Also gives differing degrees of distance\n perspective, default is 20.")
    setfieldofview  = Scale(framefieldview, width =8)
    setfieldofview.configure(troughcolor="#ffffff")
    setfieldofview.configure(length="65")
    setfieldofview.configure(orient="horizontal")
    setfieldofview.configure(resolution="5")
    setfieldofview.configure(to="100")
    setfieldofview.grid(row=3, column=0, padx=0, pady=0, sticky='N')
    setfieldofview.set(20)
    getfield = Button(group, text = 'Update',width = 16)
    getfield.grid(row=4, column=0, padx=2, pady=2, sticky=N)
    getfield.bind('<Button-1>', setfield)
    #-----------------full screen----------------------
    framefullscreen = Frame(group,width = 16)
    framefullscreen.grid(row=5, column=0, padx=2, pady=2, sticky='N')
    balloonfullscreen = Pmw.Balloon(group)
    balloonfullscreen.bind(framefullscreen, "Once full screen mode is initiated\n it cannot be turned off.")
    fullonbtn = Button(framefullscreen, text = 'Fullscreen Mode',width = 16)
    fullonbtn.grid(row=5, column=0, padx=2, pady=2, sticky='N')
    fullonbtn.bind('<Button-1>', fullon)
    #----------------Orient the screen--------------#
    frameorient = Frame(group)
    frameorient.grid(row=6, column=0, padx=2, pady=2, sticky='N')
    ballorient = Pmw.Balloon(group)
    ballorient.bind(frameorient, 'This will center the screen on the protein')
    orientbutt = Button(group, text = 'Orient Screen', width = 16)
    orientbutt.grid(row=6, column=0, padx=2, pady=2, sticky='N')
    orientbutt.bind('<Button-1>', orient)


    #-------------------Alternate Ray Tracing----------------------
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Ray Trace Options')
    group.grid(row=0, column=0,columnspan=2, padx=0, pady=5, sticky=NW)
    rayzero = Button(group, text = 'Default Ray')
    rayzero.grid(row=0, column=0, padx=2, pady=2, sticky=E)
    rayzero.bind('<Button-1>', setray0)
    rayone = Button(group, text = 'Black Outline Ray')
    rayone.grid(row=0, column=1, padx=2, pady=2, sticky=E)
    rayone.bind('<Button-1>', setray1)
    raytwo = Button(group, text = 'Black and White Ray')
    raytwo.grid(row=0, column=2, padx=2, pady=2, sticky=E)
    raytwo.bind('<Button-1>', setray2)
    raythree = Button(group, text = 'Cartoon Ray')
    raythree.grid(row=0, column=3, padx=2, pady=2, sticky=E)
    raythree.bind('<Button-1>', setray3)

    #------------------Amino Acid Reference Group-----------------
    group = tk.LabelFrame(glb.GUI.toolbox['tab'], text='Amino Acid Reference:')
    group.grid(row=1, column=0,  padx=0, pady=0, sticky=NW)
    canvas79=Canvas(group, width=200, height=150)
    canvas79.grid(row=2, column=0,columnspan = 2, padx=0, pady=0, sticky=NE)
    msg = Message(group, width = 200, text="Amino Acid Code:")
    msg.grid(row=0, column=0, padx=0, pady=0, sticky=NE)
    name5 = Entry (group, width = 7)
    name5.grid(row=0, column=1, padx=4, pady=3, sticky=NW)
    but37 = Button (group)
    but37.grid(row=0, column=2, padx=4, pady=3, sticky=NW)
    but37.configure(text="Submit")
    but37.configure(width="7")
    name6 = Entry (group, width = 10)
    name6.grid(row=1, column=1, padx=4, pady=3, sticky=NW)
    but49 = Button (group)
    but49.grid(row=1, column=2, padx=4, pady=3, sticky=NW)
    but49.configure(text="Submit")
    but49.configure(width="7")
    msg = Message(group, width = 200, text="Amino Acid name:")
    msg.grid(row=1, column=0, padx=0, pady=0, sticky=NE)
    diment = Entry(group)


    labels = ('2D', '3D')
    radioAdd(group, 'w', 'vertical', dim_dim,
          ' ', labels, 2, 2, 1, 1, 'NW')

    name5.bind('<Return>', aaget)
    but37.bind('<Button-1>', aaget)
    but49.bind('<Button-1>', aagive)