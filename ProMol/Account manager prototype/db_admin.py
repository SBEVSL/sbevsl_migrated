import Tkinter as tk
from ttk import *
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.adminmanager import *
#from pmg_tk.startup.ProMol import accountmanager as am
Pmw.initialise()

def initialise():
    group = tk.Frame(glb.GUI.db_admin['tab'])

    glb.GUI.db_admin['LoginLabel'] = tk.Label(glb.GUI.db_admin['tab'],text="Login")
    glb.GUI.db_admin['LoginLabel'].pack()	

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

    glb.GUI.db_admin['Use Database'] = tk.Button(glb.GUI.db_admin['tab'], text='Use Database', command=glb.ADMIN.toggleDB)
    glb.GUI.db_admin['Use Database'].pack()

    glb.GUI.db_admin['Upload CSVs'] = tk.Button(glb.GUI.db_admin['tab'], text='Upload CSVs', command=glb.ADMIN.submitCSVs)
    glb.GUI.db_admin['Upload CSVs'].pack()  

    glb.GUI.db_admin['AccountCreatorLabel'] =tk.Label(glb.GUI.db_admin['tab'],text="\nCreate an account")
    glb.GUI.db_admin['AccountCreatorLabel'].pack()

    glb.GUI.db_admin['newUsername'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['newUsername'].pack()
    glb.GUI.db_admin['newUsername'].insert(0, "Username")

    glb.GUI.db_admin['newPassword'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['newPassword'].pack()
    glb.GUI.db_admin['newPassword'].insert(0, "Password")

 #   glb.GUI.db_admin['Create Account'] = tk.Button(glb.GUI.db_admin['tab'], text='Create Account', command=am.createAccount)
 #   glb.GUI.db_admin['Create Account'].pack()

