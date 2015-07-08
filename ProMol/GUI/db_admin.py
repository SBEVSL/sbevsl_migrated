import Tkinter as tk
from ttk import *
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.Methods import client as c
Pmw.initialise()

def initialise():
	group = tk.Frame(glb.GUI.db_admin['tab'])

	glb.GUI.db_admin['ulabel'] = tk.Label(group, text='Username')
	glb.GUI.db_admin['ulabel'].grid(row=0, column=0,columnspan=2)
	glb.GUI.db_admin['Username'] = tk.Entry(glb.GUI.db_admin['tab'])
	glb.GUI.db_admin['Username'].pack()

	glb.GUI.db_admin['plabel'] = tk.Label(group, text='Password')
	glb.GUI.db_admin['plabel'].grid(row=0, column=0,columnspan=2)
	glb.GUI.db_admin['Password'] = tk.Entry(glb.GUI.db_admin['tab'])
	glb.GUI.db_admin['Password'].pack()

	glb.GUI.db_admin['Use Database'] = tk.Button(glb.GUI.db_admin['tab'], text='Use Database', command=lambda: c.main('l',0))
	glb.GUI.db_admin['Use Database'].pack()

