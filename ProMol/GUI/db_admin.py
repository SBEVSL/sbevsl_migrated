import Tkinter as tk
from ttk import *
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.adminmanager import *
Pmw.initialise()

def initialise():
    group = tk.Frame(glb.GUI.db_admin['tab'])

    glb.GUI.db_admin['Server'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['Server'].pack()
    glb.GUI.db_admin['Server'].insert(0, "Host Server")

    glb.GUI.db_admin['Database'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['Database'].pack()
    glb.GUI.db_admin['Database'].insert(0, "Database")

    glb.GUI.db_admin['Username'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['Username'].pack()
    glb.GUI.db_admin['Username'].insert(0, "Username")

    glb.GUI.db_admin['Password'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['Password'].pack()
    glb.GUI.db_admin['Password'].insert(0, "Password")

    glb.GUI.db_admin['Use Database'] = tk.Button(glb.GUI.db_admin['tab'], text='Use Database', command=toggleDB)
    glb.GUI.db_admin['Use Database'].pack()    
