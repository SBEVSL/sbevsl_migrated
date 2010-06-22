import Tkinter as tk
import tkFont as tkF
from pmg_tk.startup.ProMol import promolglobals as pglob

def initialise():
    canvas = tk.Canvas(pglob.GUI['welcome']['tab'],width=500)
    canvas.grid(row=0, column=0, sticky=tk.NW)
    canvas.create_text(10, 10, text = 'ProMol', font='-*-new century schoolbook-bold-r-normal-*-34-*-*-*-*-*-*-*', anchor=tk.NW)
    canvas.create_text(50, 50, text = 'Developed by the SBEVSL Project', font='-*-new century schoolbook-bold-r-normal-*-25-*-*-*-*-*-*-*', anchor=tk.NW)
    canvas.create_text(50, 70, text = 'Licensed under GPL', font='-*-new century schoolbook-bold-r-normal-*-25-*-*-*-*-*-*-*', anchor=tk.NW)
    if len(pglob.MOTIFS['errors']) != 0:
        errorbox = tk.LabelFrame(pglob.GUI['welcome']['tab'], text='Motif Loading Errors')
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
        for error in pglob.MOTIFS['errors']:
            errors.insert(tk.END,error)
    else:
        canvas2 = tk.Canvas(pglob.GUI['welcome']['tab'], height=200)
        canvas2.grid(row=1, column=0)
