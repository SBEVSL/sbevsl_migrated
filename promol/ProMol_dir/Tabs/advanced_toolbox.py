from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.setting import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
Pmw.initialise()

def initialise():
    #--------------Mode---------------------
    group = Pmw.Group(pglob.Tabs['advanced_toolbox'], tag_text='Mode:')
    group.grid(row=0, column=1, padx=2, pady=2, sticky = tk.NW)
    interior = group.interior()
    framesculbtn = tk.Frame(interior, width=16)
    framesculbtn.grid(row=0, column=0, padx=1, pady=1, sticky = tk.NW)
    balloonsculpt = Pmw.Balloon(interior)
    balloonsculpt.bind(framesculbtn, "Ctrl + Right Click to drag an atom.\nCtrl + Left Click to rotate bonds.")
    sculbtn = tk.Button(framesculbtn, text = 'Sculpting', width=16)
    sculbtn.grid(row=0, column=0, padx=1, pady=1, sticky = tk.NW)
    sculbtn.bind('<Button-1>',sculpt)

    #-------------Measurment-------------------#
      #Measures distance between two atoms

    framedis = tk.Frame(interior, width=16)
    framedis.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
    balldis = Pmw.Balloon(interior)
    balldis.bind(framedis, "Use internal GUI on PyMol\n to turn this mode off.")
    disbtn = tk.Button(framedis, text = 'Measurement Tool', width=16)
    disbtn.grid(row=1, column=0, padx=1, pady=1, sticky = tk.NW)
    disbtn.bind('<Button-1>', dis)

    #Defines Sequence View Open and close
    #Defines Sequence View Open and close
    #opens Pymol sequence viewer, and can switch
    #between 4 diff modes, 1 letter aa, 3 letter aa, residue atoms, chains
    frameseq1 = tk.Frame(interior, width=16)
    frameseq1.grid(row=2, column=0, padx=1, pady=1, sticky = tk.NW)
    frameseq2 = tk.Frame(interior, width=16)
    frameseq2.grid(row=3, column=0, padx=1, pady=1, sticky = tk.NW)
    seqbtn1 = tk.Button(frameseq1, text = "Sequence Viewer On", width=16)
    seqbtn1.grid(row=2, column=0, padx=1, pady=1, sticky = tk.NW)
    seqbtn0 = tk.Button(frameseq2, text = "Sequence Viewer Off", width=16)
    seqbtn0.grid(row=3, column=0, padx=1, pady=1, sticky = tk.NW)
    seqbtn1.bind('<Button-1>', seqviewon)
    seqbtn0.bind('<Button-1>', seqviewoff)
    seqformat = tk.Entry(interior)

    labels = ("One letter", "Three letter", "AA atoms", "Chains")
    radioAdd(interior, 'w', 'vertical', seqviewformat,
              ' ', labels, 4, 0, 1, 1, 'NW')



    #------------Amino Acid Select------------------------------
    group = Pmw.Group(pglob.Tabs['advanced_toolbox'], tag_text='Amino Acid Selector:')
    group.grid(row=1, column=0, padx=2, pady=2, sticky = tk.SW)
    interior = group.interior()
    labelaa = tk.Label(interior, text = 'Code:')
    labelaa.grid(row=1, column=0, padx=2, pady=2)
    x = tk.Entry(interior, width =5)
    x.grid(row=1, column=1, padx=2, pady=2)
    selecta = tk.Button(interior, width = 15,text = 'Select Residues')
    selecta.grid(row=1, column=2, padx=2, pady=2)

    #-------------Residue Select------------------------
    labelr = tk.Label(interior, text = ' Number:')
    labelr.grid(row=0, column=0, padx=2, pady=2)
    xr = tk.Entry(interior, width =5)
    xr.grid(row=0, column=1, padx=2, pady=2)
    selectr = tk.Button(interior, width = 15,text = 'Select Residues')
    selectr.grid(row=0, column=2, padx=2, pady=2)

    selectr.bind('<Button-1>', selectresi)


    x.bind('<Return>', selres)
    selecta.bind('<Button-1>', selres)


    #----------Set up scales for controlling how much of protein is roved----------


    group = Pmw.Group(pglob.Tabs['advanced_toolbox'], tag_text='Electron Density Mapping')#And a new group
    group.grid(row=0, column=0, padx=2, pady=2, sticky = tk.NW)
    interior = group.interior()
    framemesh = tk.Frame(interior)
    framemesh.grid(row=0, column=0, padx=0, pady=2, sticky = tk.W)
    framesurf = tk.Frame(interior)
    framesurf.grid(row=2, column=0, padx=0, pady=2, sticky = tk.W)
    framedots = tk.Frame(interior)
    framedots.grid(row=1, column=0, padx=0, pady=2, sticky = tk.W)
    framerov = tk.Frame(interior)
    framerov.grid(row=3, column=0, padx=0, pady=2, sticky = tk.W)
    framemeshsel = tk.Frame(interior)
    framemeshsel.grid(row=0, column=1, padx=0, pady=2, sticky = tk.W)
    framedotsel = tk.Frame(interior)
    framedotsel.grid(row=1, column=1, padx=0, pady=2, sticky = tk.W)
    framesurfsel = tk.Frame(interior)
    framesurfsel.grid(row=2, column=1, padx=0, pady=2, sticky = tk.W)
    imesh = tk.Button(framemesh)#Mesh Button
    imesh.grid(row=0, column=0, padx=0, pady=2, sticky = tk.W)
    imesh.configure(text="Mesh")
    imesh.configure(width="10")
    framecontour1 = tk.Frame(interior)
    framecontour1.grid(row=5, column=1, padx=0, pady=0, sticky = tk.NW)
    contour1 = tk.Scale(framecontour1, width =8)
    contour1.configure(troughcolor="#ffffff")
    contour1.configure(length="100")
    contour1.configure(orient="horizontal")
    contour1.configure(resolution="0.05")
    contour1.configure(to="4.0")
    contour1.grid(row=4, column=1, padx=1, pady=0, sticky = tk.W)
    contour1.set(1.0)
    frameradii = tk.Frame(interior)
    frameradii.grid(row=6, column=1, padx=0, pady=0, sticky = tk.N)
    ballradii = Pmw.Balloon(interior)
    ballradii.bind(frameradii, 'After changing detail, re-click on roving option')
    rovingradius1 = tk.Scale(frameradii, width =8)
    rovingradius1.configure(troughcolor="#ffffff")
    rovingradius1.configure(length="100")
    rovingradius1.configure(orient="horizontal")
    rovingradius1.configure(resolution="0.1")
    rovingradius1.configure(to="15.0")
    rovingradius1.grid(row=6, column=1, padx=0, pady=0, sticky = tk.N)
    rovingradius1.set(8.0)
    labrovrad = tk.Label(interior, text = 'Roving Detail')
    labrovrad.grid(row=6, column=0, padx=5, pady=0, sticky = tk.SE)

    imesh.bind('<Button-1>', emesh)
    idot = tk.Button(framedots)
    idot.grid(row=1, column=0, padx=0, pady=2, sticky = tk.W)
    idot.configure(text="Dots")
    idot.configure(width="10")

    idot.bind('<Button-1>', edot)

    isurf = tk.Button(framesurf)
    isurf.grid(row=2, column=0, padx=0, pady=2, sticky = tk.W)
    isurf.configure(text="Surface")
    isurf.configure(width="10")
    #Isosurface function

    isurf.bind('<Button-1>', esurf)



    rden = tk.Button(framerov)
    rden.grid(row=3, column=0, padx=0, pady=2, sticky = tk.W)
    rden.configure(text="Roving Mesh")
    rden.configure(width="10")
    #roving isomesh function

    rden.bind ('<Button-1>', roving_density)

    framerovs = tk.Frame(interior)
    framerovs.grid(row=4, column=0, padx=0, pady=2, sticky = tk.W)
    surfacing = tk.Button(framerovs, width = 10)
    surfacing.grid(row=4, column=0, padx=0, pady=2, sticky = tk.W)
    surfacing.configure(text = 'Rove Surface')
    surfacing.bind('<Button-1>', roving_surface)
    #----------Electron Density Map on only Selection------------------------
    labelcon = tk.Label(interior, text = '  Contour')
    labelcon.grid(row=5, column=0, padx=5, pady=2, sticky = tk.S)
    imesh1 = tk.Button(framemeshsel)
    imesh1.grid(row=0, column=1, padx=0, pady=2, sticky = tk.W)
    imesh1.configure(text="Mesh Select")
    imesh1.configure(width="10")
    #isomesh on only selection

    imesh1.bind('<Button-1>', emesh1)
    idot1 = tk.Button(framedotsel)
    idot1.grid(row=1, column=1, padx=0, pady=2, sticky = tk.W)
    idot1.configure(text="Dots Select")
    idot1.configure(width="10")
    #isodot on only selection

    idot1.bind('<Button-1>', edot1)
    isurf1 = tk.Button(framesurfsel)
    isurf1.grid(row=2, column=1, padx=0, pady=2, sticky = tk.W)
    isurf1.configure(text="Surface Select")
    isurf1.configure(width="12")

    isurf1.bind('<Button-1>', esurf1)

    frame = tk.Frame(interior)
    frame.grid(row=3, column=1, padx=0, pady=0, sticky = tk.SW)
    doublemapbtn = tk.Button(frame, text = 'Double resolution')
    doublemapbtn.grid(row=3, column=1, padx=0, pady=0, sticky = tk.SW)

    balloon = Pmw.Balloon(interior)
    balloon.bind(frame, "Please be patient.\nButton can only be used once.\nPyMol will close if used twice.")

    doublemapbtn.bind('<Button-1>', doublemapres)#workspot


    balloon1 = Pmw.Balloon(interior)
    balloon1.bind(framemesh, '''Display entire map as a mesh.''')
    balloon2 = Pmw.Balloon(interior)
    balloon2.bind(framedots, '''Display entire map as dots.''')
    balloon3 = Pmw.Balloon(interior)
    balloon3.bind(framesurf, '''Display entire map as surface.''')
    balloon4 = Pmw.Balloon(interior)
    balloon4.bind(framerov, "View small portions of map at a time\n using middle mouse button to scan across.")
    balloon45 = Pmw.Balloon(interior)
    balloon45.bind(framerovs, "View small portions of map at a time\n using middle mouse button to scan across.")
    balloon5 = Pmw.Balloon(interior)
    balloon5.bind(framemeshsel, "Must have PDB loaded.\n Display mesh on only selected residues (sele).")
    balloon6 = Pmw.Balloon(interior)
    balloon6.bind(framedotsel, "Must have PDB loaded.\n Display dots on only selected residues (sele).")
    balloon7 = Pmw.Balloon(interior)
    balloon7.bind(framesurfsel, "Must have PDB loaded.\n Display surface on only selected residues (sele).")
    balloon11 = Pmw.Balloon(interior)
    balloon11.bind(framecontour1, "After altering countour click again\n on map view of choice for change to occur.")

    framemapdoer = Frame(interior)
    framemapdoer.grid(row=4, column=1, padx=0, pady=5, sticky = tk.NW)
    balloon972 = Pmw.Balloon(interior)
    balloon972.bind(framemapdoer, "For advanced users only\nRequires external map download")
    loadmapbtn = tk.Button(framemapdoer, text = 'External map')
    loadmapbtn.grid(row=4, column=1, padx=0, pady=5, sticky = tk.NW)
    loadmapbtn.bind('<Button-1>', loadmapps)

    #------------Fetch Ramachandran Plot --------------------
    group = Pmw.Group(pglob.Tabs['advanced_toolbox'], tag_text='Ramachandran Plot:')
    group.grid(row=1, column=1, padx=2, pady=2, sticky = tk.SW)
    interior = group.interior()
    framebtn1 = tk.Frame(interior)
    framebtn1.grid(row=1, column=0, padx=2, pady=2, sticky = tk.NE)
    balloon12 = Pmw.Balloon(interior)
    balloon12.bind(framebtn1, "Must have internet connection, goes to external website.")
    Labelpdb = tk.Label(interior, text = 'Enter PDB code:')
    Labelpdb.grid(row=0, column=0, columnspan = 2, padx=2, pady=2, sticky = tk.NW)
    enterpdb = tk.Entry(interior, width=6)
    enterpdb.grid(row=1, column=1, padx=2, pady=4, sticky = tk.NW)
    btn1 = tk.Button(framebtn1, text = 'Fetch Plot', width = 10)
    btn1.grid(row=1, column=0, padx=2, pady=2, sticky = tk.NW)
    btn1.bind('<Button-1>', fetchurl)