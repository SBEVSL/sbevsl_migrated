import Tkinter as tk
import Pmw
from ProMol import promolglobals as glb
from ProMol.Methods.movie import *
from ProMol.Methods.save import *
from ProMol.Methods.setting import *
Pmw.initialise()

def initialise():
    #-----------Mouse Mode--------------
    group = tk.LabelFrame(glb.GUI.movie_maker['tab'], text='Mouse Mode:')
    group.grid(row=1, column=0, padx=0, pady=0, sticky = tk.NW)
    ddddd = tk.Button(group, width = 15, text = '3 Button Viewing')
    ddddd.grid(row=0, column=0, padx=2, pady=2, sticky = tk.NW)
    dddd = tk.Button(group, width = 15,text = '3 Button Editing')
    dddd.grid(row=1, column=0, padx=2, pady=2, sticky = tk.NW)
    fffff = tk.Button(group, width = 15,text = '2 Button Viewing')
    fffff.grid(row=2, column=0, padx=2, pady=2, sticky = tk.NW)
    ffff = tk.Button(group, width = 15,text = '2 Button Selecting')
    ffff.grid(row=0, column=1, padx=2, pady=2, sticky = tk.NW)
    fff = tk.Button(group, width = 15,text = '2 Button Editing')
    fff.grid(row=1, column=1, padx=2, pady=2, sticky = tk.NW)
    ggggg = tk.Button(group, width = 15,text = '1 Button Viewing')
    ggggg.grid(row=2, column=1, padx=2, pady=2, sticky = tk.NW)

    ddddd.bind('<Button-1>', tv)
    dddd.bind('<Button-1>', te)
    fffff.bind('<Button-1>', dv)
    ffff.bind('<Button-1>', ds)
    fff.bind('<Button-1>', de)
    ggggg.bind('<Button-1>', ov)



    #----------Load and Save Frame Group------------------#


    group = tk.LabelFrame(glb.GUI.movie_maker['tab'], text='Load and Save:')
    group.grid(row=0, column=0, padx=0, pady=0, sticky = tk.NE)
    #------------File extension Selector---------------#

    filexlab = tk.Label(group, text = "File Extension:")
    filexlab.grid(row=4, column=0, padx=5, pady=5, sticky = tk.NE)
    entfilex = tk.Entry(group, width = 5)
    entfilex.grid(row=4, column=1, padx=5, pady=5, sticky = tk.NW)
    entfilex.insert(0, ".pdb")

    #---------------Load Button and Function---------------------#


    loadbtn1 = tk.Button(group, text = 'Load frame')
    loadbtn1.grid(row=2, column=0, padx=5, pady=5, sticky = tk.NE)
    framelab = tk.Label(group, text = 'Frame:')
    framelab.grid(row=1, column=0, padx=5, pady=5, sticky = tk.NE)
    enti = tk.Entry(group, width = 5)
    enti.insert(0,0)
    enti.grid(row=1, column=1, padx=5, pady=5, sticky = tk.NW)
    entl = tk.Entry(group)
    entl.insert(0,0)


    loadbtn1.bind('<Button-1>', loadframe)
    #---------------Save Button------------------#

    savebtn = tk.Button(group, text = 'Save Frame')
    savebtn.grid(row=2, column=1, padx=5, pady=5, sticky = tk.NW)

    labname = tk.Label(group, text = "Movie Title:")
    labname.grid(row=0, column=0, padx=5, pady=5, sticky = tk.NE)
    name_mov = tk.Entry(group, width = 10)
    name_mov.grid(row=0, column=1, padx=5, pady=5, sticky = tk.NW)
    #--------------------goto frame button and Function-----------#
    gotobtn = tk.Button(group, text = 'Go to Frame:')
    gotobtn.grid(row=3, column=0, padx=5, pady=5, sticky = tk.NE)
    gotoent = tk.Entry(group, width = 10)
    gotoent.grid(row=3, column=1, padx=5, pady=5, sticky = tk.NW)

    gotobtn.bind('<Button-1>', gotoframe)

    #---------Save Function--------------------------#


    savebtn.bind('<Button-1>', molSave)

    #-----------Ray Trace Frames-----------
    #Self explanatory, and can save ray traced frames# as png images
    labels = ("Ray Trace Frames")
    ray = Pmw.RadioSelect(group, labelpos='w', labelmargin=0,
    	                   buttontype='checkbutton',orient='vertical',
    	                   command=do_ray)
    ray.add("Ray Trace Frames")
    ray.grid(row=6, column=0, padx=5, pady=0, sticky = tk.NE)

    mpngbtn = tk.Button(group, text = "Create PNGs")
    mpngbtn.grid(row=6, column=1, padx=5, pady=0, sticky = tk.NW)

    mpngbtn.bind('<Button>', mping)



    #----------Clearing Ram Button and Function----

    clearbtn = tk.Button(group, text = "Clear Ram")
    clearbtn.grid(row=7, column=1, padx=5, pady=3, sticky = tk.NW)

    clearbtn.bind('<Button-1>', clearram)

    #-----Cache off button and Function-----------

    labels = ("Frame Cache Off")
    cache = Pmw.RadioSelect(group, labelpos='w', labelmargin=0,
    	                   buttontype='checkbutton',orient='vertical',
    	                   command=cacheframe)
    cache.add("Frame Cache Off")
    cache.grid(row=7, column=0, padx=5, pady=0, sticky = tk.NE)

    #------------Scripted Animation GUI ----------#
    #Used for easier creation of movies, utilizing buttons
    #instead of the necessity to input Pymol commands constantly

    group = tk.LabelFrame(glb.GUI.movie_maker['tab'], text='Scripted Animation:')
    group.grid(row=0, column=1, padx=0, pady=0, sticky = tk.NW)
    labscrp = tk.Label(group, text = "Frames in Movie:")
    labscrp.grid(row = 0, column=0, padx=5, pady=5, sticky = NE)
    fent = tk.Entry(group, width = 8)
    fent.grid(row = 0, column=1, padx=5, pady=5, sticky = NW)
    makmovframe = tk.Frame(group)
    makmovframe.grid(row = 0, column=2, padx=5, pady=3, sticky = NW)
    makball = Pmw.Balloon(group)
    makball.bind(makmovframe, 'Set the number of movie frames FIRST')
    makmov = tk.Button(makmovframe, text = "set movie")
    makmov.grid(row = 0, column=2, padx=5, pady=3, sticky = NW)

    makmov.bind('<Button-1>', makmovie)
    labscrp = tk.Label(group, text = "Frame:")
    labscrp.grid(row = 1, column=0, padx=5, pady=5, sticky = NE)
    scriptent = tk.Entry(group, width = 8)
    scriptent.grid(row = 1, column=1, padx=5, pady=5, sticky = NW)
    scriptent.insert(0,0)
    labmx = tk.Button(group, text = "Move X:")
    labmx.grid(row = 2, column=0, padx=5, pady=5, sticky = NE)
    entmx = tk.Entry(group, width = 6)
    entmx.grid(row = 3, column=0, padx=5, pady=5, sticky = NE)
    labmy = tk.Button(group, text = "Move Y:")
    labmy.grid(row = 2, column=1, padx=5, pady=5, sticky = NW)
    entmy = tk.Entry(group, width = 6)
    entmy.grid(row = 3, column=1, padx=5, pady=5, sticky = NW)
    labmz = tk.Button(group, text = "Move Z:")
    labmz.grid(row = 2, column=2, padx=5, pady=5, sticky = NW)
    entmz = tk.Entry(group, width = 6)
    entmz.grid(row = 3, column=2, padx=5, pady=5, sticky = NW)
    labtx = tk.Button(group, text = "Turn X:")
    labtx.grid(row = 4, column=0, padx=5, pady=5, sticky = NE)
    enttx = tk.Entry(group, width = 6)
    enttx.grid(row = 5, column=0, padx=5, pady=5, sticky = NE)
    labty = tk.Button(group, text = "Turn Y:")
    labty.grid(row = 4, column=1, padx=5, pady=5, sticky = NW)
    entty = tk.Entry(group, width = 6)
    entty.grid(row = 5, column=1, padx=5, pady=5, sticky = NW)
    labtz = tk.Button(group, text = "Turn Z:")
    labtz.grid(row = 4, column=2, padx=5, pady=5, sticky = NW)
    enttz = tk.Entry(group, width = 6)
    enttz.grid(row = 5, column=2, padx=5, pady=5, sticky = NW)
     #-----Movie translation functions, providing specification
    #of xyz coordinate translation of proteins and/or molecules

    labmx.bind('<Button-1>', movsetx)
    labmy.bind('<Button-1>', movsety)
    labmz.bind('<Button-1>', movsetz)
    labtx.bind('<Button-1>', tursetx)
    labty.bind('<Button-1>', tursety)
    labtz.bind('<Button-1>', tursetz)

    labmxyz = tk.Button(group, text = "Move All:")
    labmxyz.grid(row = 6, column=0, padx=5, pady=5, sticky = NE)
    labmxyz.bind('<Button-1>', movsetxyz)
    labtxyz = tk.Button(group, text = "Turn All:")
    labtxyz.grid(row = 6, column=1, padx=5, pady=5, sticky = NW)
    labtxyz.bind('<Button-1>', tursetxyz)

    labtxyz = tk.Button(group, text = "Do All:")
    labtxyz.grid(row = 6, column=2, padx=5, pady=5, sticky = NW)
    labtxyz.bind('<Button-1>', tursetxyzmovsetxyz)

    #--------------Selection Controls--------------------
    #---This creates frames, and thusly the ability to add
    #---Balloon pop up help for mask/protect buttons-----
    group = tk.LabelFrame(glb.GUI.movie_maker['tab'], text='Selection Controls')
    group.grid(row=1, column=1, padx=0, pady=0, sticky = tk.SW)
    framemaskbtn = tk.Frame(group)
    framemaskbtn.grid(row=1, column=0, padx=2, pady=1, sticky = tk.NW)
    ballmaskbtn = Pmw.Balloon(group)
    ballmaskbtn.bind(framemaskbtn, "This will mask a named selection\nand prevent it from being\nmodified or moved at all.")
    framemaskaebtn = tk.Frame(group)
    framemaskaebtn.grid(row=2, column=0, padx=2, pady=1, sticky = tk.NW)
    ballmaskaebtn = Pmw.Balloon(group)
    ballmaskaebtn.bind(framemaskaebtn, "This will mask all objects except the named selection\nand prevent them from being\nmodified or moved at all.")
    frameunmaskbtn = tk.Frame(group)
    frameunmaskbtn.grid(row=3, column=0, padx=2, pady=1, sticky = tk.NW)
    ballunmaskbtn = Pmw.Balloon(group)
    ballunmaskbtn.bind(frameunmaskbtn, "This will unmask a masked selection\nallowing modifications.")
    frameprotectbtn = tk.Frame(group)
    frameprotectbtn.grid(row=1, column=1, padx=2, pady=1, sticky = tk.NW)
    ballprotectbtn = Pmw.Balloon(group)
    ballprotectbtn.bind(frameprotectbtn, "This will protect a named selection\nand prevent it from being moved.\nBut it can still be modified.\nRecommended for only advanced users.")
    framedeprotectbtn = tk.Frame(group)
    framedeprotectbtn.grid(row=3, column=1, padx=2, pady=1, sticky = tk.NW)
    balldeprotect = Pmw.Balloon(group)
    balldeprotect.bind(framedeprotectbtn, "This will deprotect a protected selection\nallowing it to be moved.")
    frameprobtn = tk.Frame(group)
    frameprobtn.grid(row=2, column=1, padx=2, pady=1, sticky = tk.NW)
    ballprotbtn = Pmw.Balloon(group)
    ballprotbtn.bind(frameprobtn, "This will protect all objects excecpt the named selection\nand prevent it from being moved.\nBut it can still be modified.\nRecommended for only advanced users.")
    maskbtn = tk.Button(framemaskbtn, text = 'Mask Selection',width = 15)
    maskbtn.grid(row=1, column=0, padx=2, pady=1, sticky = tk.NW)
    unmaskbtn = tk.Button(frameunmaskbtn, text = 'Unmask Selection',width = 15)
    unmaskbtn.grid(row=3, column=0, padx=2, pady=1, sticky = tk.NW)
    maskaebtn = tk.Button(framemaskaebtn, text = 'Mask All Except',width = 15)
    maskaebtn.grid(row=2, column=0, padx=2, pady=1, sticky = tk.NW)
    probtn = tk.Button(frameprobtn, text = 'Protect All Except',width = 15)
    probtn.grid(row = 2, column =1, padx=2, pady=1, sticky = tk.NW)
    protectbtn= tk.Button(frameprotectbtn, text = 'Protect Selection',width = 15)
    protectbtn.grid(row=1, column=1, padx=2, pady=1, sticky = tk.NW)
    deprotectbtn = tk.Button(framedeprotectbtn, text = 'Deprotect Selection',width = 15)
    deprotectbtn.grid(row=3, column=1, padx=2, pady=1, sticky = tk.NW)
    maskent = tk.Entry(group, width = 10)
    maskent.grid(row=0, column=1, padx=2, pady=1, sticky = tk.NW)
    labby21 = tk.Label(group, text = 'Name:')
    labby21.grid(row=0, column=0, padx=2, pady=1, sticky = tk.NE)


    maskbtn.bind('<Button-1>', maskedman)
    unmaskbtn.bind('<Button-1>', unmaskedman)
    maskaebtn.bind('<Button-1>', maskallexcept)
    protectbtn.bind('<Button-1>', protectme)
    deprotectbtn.bind('<Button-1>', deprotectme)
