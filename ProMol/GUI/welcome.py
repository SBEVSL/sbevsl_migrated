import Tkinter as tk
import tkFont as tkF
import os
from pmg_tk.startup.ProMol import promolglobals as glb

def initialise():
    canvas = tk.Canvas(glb.GUI.welcome['tab'],height=110, width=500)
    canvas.grid(row=0, column=0, sticky=tk.NW)
    canvas.create_text(10, 10, text = 'ProMOL', font='-*-new century schoolbook-bold-r-normal-*-34-*-*-*-*-*-*-*', anchor=tk.NW)
    canvas.create_text(50, 50, text = 'Developed by the SBEVSL Project', font='-*-new century schoolbook-bold-r-normal-*-25-*-*-*-*-*-*-*', anchor=tk.NW)
    canvas.create_text(50, 70, text = 'Licensed under GPL, No Warranty', font='-*-new century schoolbook-bold-r-normal-*-25-*-*-*-*-*-*-*', anchor=tk.NW)
    if len(glb.MOTIFS['errors']) != 0:
        errorbox = tk.LabelFrame(glb.GUI.welcome['tab'], text='Motif Loading Errors')
        errorbox.grid(row=1, column=0)
        xscroll = tk.Scrollbar(errorbox, orient=tk.HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=tk.E+tk.W)
        yscroll = tk.Scrollbar(errorbox, orient=tk.VERTICAL)
        yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
        errors = tk.Listbox(errorbox, height=10, width=70,
            xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        errors.grid(row=0,column=0)
        xscroll["command"] = errors.xview
        yscroll["command"] = errors.yview
        for error in glb.MOTIFS['errors']:
            errors.insert(tk.END,error)
    else:
        canvas2 = tk.Canvas(glb.GUI.welcome['tab'], height=200, width=450)
        canvas2.grid(row=1, column=0)
        canvas2.create_text(10,10, text = 'Partial Funding Provided By',font='-*-new century schoolbook-bold-r-normal-*-15-*-*-*-*-*-*-*', anchor=tk.NW)
        canvas2.create_text(20,25, text = 'NSF DUE 0402408',font='-*-new century schoolbook-bold-r-normal-*-10-*-*-*-*-*-*-*', anchor=tk.NW)
        canvas2.create_text(20,40, text = 'NIGMS 1R15GM078077',font='-*-new century schoolbook-bold-r-normal-*-10-*-*-*-*-*-*-*', anchor=tk.NW)
        canvas2.create_text(20,55, text = 'RIT and Dowling College',font='-*-new century schoolbook-bold-r-normal-*-10-*-*-*-*-*-*-*', anchor=tk.NW)
        motd=open(os.path.join(glb.PROMOL_DIR_PATH,'motd'),"r")
        motdall = motd.read()          
        canvas2.create_text(10,70, text = motdall, font='-*-new century schoolbook-bold-r-normal-*-10-*-*-*-*-*-*-*', anchor=tk.NW)
        motd.close()
