import Tkinter as tk
from ttk import *
import Pmw
from ProMol import promolglobals as glb
from ProMol.Methods import client as c
Pmw.initialise()

def initialise():
	group = tk.Frame(glb.GUI.db_admin['tab'])

	ulabel = tk.Label(glb.GUI.db_admin['tab'], text='Username').grid(row=0,column=0)
	glb.GUI.db_admin['Username'] = tk.Entry(glb.GUI.db_admin['tab'])
	glb.GUI.db_admin['Username'].grid(row=0,column=1)

	plabel = tk.Label(glb.GUI.db_admin['tab'], text='Password').grid(row=1,column=0)
	glb.GUI.db_admin['Password'] = tk.Entry(glb.GUI.db_admin['tab'],show="*")
	glb.GUI.db_admin['Password'].grid(row=1,column=1)

	iphost = tk.Label(glb.GUI.db_admin['tab'], text='Host').grid(row=2,column=0)
	glb.GUI.db_admin['ip'] = tk.Entry(glb.GUI.db_admin['tab'])
	glb.GUI.db_admin['ip'].grid(row=2,column=1)

        fr = tk.Label(glb.GUI.db_admin['tab'], text='Full Run \n Uploads the results to the database \n Ignores option of filtering by EC/Pfam \n Recommended for custom motifs').grid(row=3,column=0)
	glb.GUI.db_admin['fr'] = tk.Checkbutton(glb.GUI.db_admin['tab'], variable = glb.full_run, onvalue = 1, offvalue = 0)
	glb.GUI.db_admin['fr'].grid(row=3,column=1)
	
	glb.GUI.db_admin['Use Database'] = tk.Button(glb.GUI.db_admin['tab'], text='Use Database', command=lambda: c.main('l',0))
	glb.GUI.db_admin['Use Database'].grid(row=4,column=0,columnspan=2)

