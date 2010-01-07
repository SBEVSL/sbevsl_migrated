from pymol import cmd
from Tkinter import *
import Pmw
from pmg_tk.startup.ProMol_dir import promolglobals as pglob
from pmg_tk.startup.ProMol_dir.Methods.motif import *
from pmg_tk.startup.ProMol_dir.Methods.utility import *
Pmw.initialise()

def initialise():
    #custom group
    group = Pmw.Group(pglob.Tabs['custom_motifs']['tab'], tag_text = 'Custom Motifs')
    group.grid(row=0, column=0,columnspan =4, padx=0, pady=0)
    interior = group.interior()
    #menu bars
    selectionAA = Pmw.OptionMenu(interior,label_text = 'Selection A:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifA)
    selectionAA.grid(row=0,column=0,sticky=NW)

    selectionAB = Pmw.OptionMenu(interior,label_text = 'Selection B:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifB)
    selectionAB.grid(row=0,column=1,sticky=NW)

    selectionAC = Pmw.OptionMenu(interior,label_text = 'Selection C:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifC)
    selectionAC.grid(row=0,column=2,sticky=NW)

    selectionAD = Pmw.OptionMenu(interior,label_text = 'Selection D:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifD)
    selectionAD.grid(row=0,column=3,sticky=NW)


    #sliders
    selA = Scale(interior, width =8)
    selA.configure(troughcolor="#ffffff")
    selA.configure(length="80")
    selA.configure(orient="horizontal")
    selA.configure(resolution="0.25")
    selA.configure(to="8.0")
    selA.grid(row=1, column=0, padx=0, pady=0, sticky=NW)
    selA.set(4.0)

    selB = Scale(interior, width =8)
    selB.configure(troughcolor="#ffffff")
    selB.configure(length="80")
    selB.configure(orient="horizontal")
    selB.configure(resolution="0.25")
    selB.configure(to="8.0")
    selB.grid(row=1, column=1, padx=0, pady=0, sticky=NW)
    selB.set(4.0)

    selC = Scale(interior, width =8)
    selC.configure(troughcolor="#ffffff")
    selC.configure(length="80")
    selC.configure(orient="horizontal")
    selC.configure(resolution="0.25")
    selC.configure(to="8.0")
    selC.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
    selC.set(4.0)

    #labels

    lab1 = Label(interior, text='Range A to B')
    lab1.grid(row = 2, column = 0)
    lab2 = Label(interior, text='Range B to C')
    lab2.grid(row = 2, column = 1)
    lab3 = Label(interior, text='Range C to D')
    lab3.grid(row = 2, column = 2)

    #custom buttons

    buttonAdd(interior, 'AB Selection', 15, bimotif, 3, 0, 'N,S,E,W')
    buttonAdd(interior, 'ABC Selection', 15, trimotif, 3, 1, 'N,S,E,W')
    buttonAdd(interior, 'ABCD Selection', 15, quadmotif, 3, 2, 'N,S,E,W')
    buttonAdd(interior, 'Reset', 12, resetmotif, 1, 3, 'SW')

    #--------------------------------------#
    #			               #
    #     Addvanced Custom Motifs Tab      #
    #                                      #
    #--------------------------------------#

    #custom group
    group = Pmw.Group(pglob.Tabs['custom_motifs']['tab'], tag_text = 'Advanced Custom Motifs')
    group.grid(row=1, column=0,columnspan =4, padx=0, pady=0)
    interior = group.interior()
    #menu bars
    selectionA = Pmw.OptionMenu(interior,label_text = 'Selection A:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifAA)
    selectionA.grid(row=0,column=0,sticky=NW)

    selectionB = Pmw.OptionMenu(interior,label_text = 'Selection B:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifAB)
    selectionB.grid(row=0,column=1,sticky=NW)

    selectionC = Pmw.OptionMenu(interior,label_text = 'Selection C:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifAC)
    selectionC.grid(row=0,column=2,sticky=NW)

    selectionD = Pmw.OptionMenu(interior,label_text = 'Selection D:',labelpos = 'n',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motifAD)
    selectionD.grid(row=0,column=3,sticky=NW)


    #sliders
    selAB = Scale(interior, width =8)
    selAB.configure(troughcolor="#ffffff")
    selAB.configure(length="100")
    selAB.configure(orient="horizontal")
    selAB.configure(resolution="0.25")
    selAB.configure(to="15")
    selAB.grid(row=1, column=0, padx=0, pady=0, sticky=NW)
    selAB.set(4.0)

    selAC = Scale(interior, width =8)
    selAC.configure(troughcolor="#ffffff")
    selAC.configure(length="100")
    selAC.configure(orient="horizontal")
    selAC.configure(resolution="0.25")
    selAC.configure(to="15")
    selAC.grid(row=1, column=1,columnspan=2, padx=2, pady=0, sticky=NW)
    selAC.set(4.0)

    selAD = Scale(interior, width =8)
    selAD.configure(troughcolor="#ffffff")
    selAD.configure(length="100")
    selAD.configure(orient="horizontal")
    selAD.configure(resolution="0.25")
    selAD.configure(to="15")
    selAD.grid(row=1, column=2,columnspan=2, padx=2, pady=0, sticky=NW)
    selAD.set(4.0)

    selBC = Scale(interior, width =8)
    selBC.configure(troughcolor="#ffffff")
    selBC.configure(length="100")
    selBC.configure(orient="horizontal")
    selBC.configure(resolution="0.25")
    selBC.configure(to="15")
    selBC.grid(row=3, column=0,columnspan=2, padx=2, pady=0, sticky=NW)
    selBC.set(4.0)

    selBD = Scale(interior, width =8)
    selBD.configure(troughcolor="#ffffff")
    selBD.configure(length="100")
    selBD.configure(orient="horizontal")
    selBD.configure(resolution="0.25")
    selBD.configure(to="15")
    selBD.grid(row=3, column=1,columnspan=2, padx=2, pady=0, sticky=NW)
    selBD.set(4.0)

    selCD = Scale(interior, width =8)
    selCD.configure(troughcolor="#ffffff")
    selCD.configure(length="100")
    selCD.configure(orient="horizontal")
    selCD.configure(resolution="0.25")
    selCD.configure(to="15")
    selCD.grid(row=3, column=2,columnspan=2, padx=2, pady=0, sticky=NW)
    selCD.set(4.0)

    #labels

    lab1 = Label(interior, text='Range A to B')
    lab1.grid(row = 2, column = 0)
    lab2 = Label(interior, text='Range A to C')
    lab2.grid(row = 2, column = 1)
    lab3 = Label(interior, text='Range A to D')
    lab3.grid(row = 2, column = 2)

    lab1 = Label(interior, text='Range B to C')
    lab1.grid(row = 4, column = 0)
    lab2 = Label(interior, text='Range B to D')
    lab2.grid(row = 4, column = 1)
    lab3 = Label(interior, text='Range C to D')
    lab3.grid(row = 4, column = 2)

    #custom buttons

    buttonAdd(interior, 'AB Selection', 15, Abimotif, 5, 0, 'N,S,E,W')
    buttonAdd(interior, 'ABC Selection', 15, Atrimotif, 5, 1, 'N,S,E,W')
    buttonAdd(interior, 'ABCD Selection', 15, Aquadmotif, 5, 2, 'N,S,E,W')
    buttonAdd(interior, 'Reset', 12, resetmotif, 1, 3, 'SE')