import Tkinter as tk
import Pmw
from ttk import *
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol.adminmanager import *
#from pmg_tk.startup.ProMol.accountCreator import *
import tkMessageBox
Pmw.initialise()

def loginEvent(event):
    tkMessageBox.showinfo("Entered","Check your email for information regarding your login information")

def initialise():
    group = tk.Frame(glb.GUI.db_admin['tab'])

    glb.GUI.db_admin['Login'] = tk.Label(glb.GUI.db_admin['tab'], text='\nLog in to Database\n')
    glb.GUI.db_admin['Login'].pack()

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

    #Additions below added by Cameron Baker 6/26/14

    glb.GUI.db_admin['Create account'] = tk.Label(glb.GUI.db_admin['tab'], text='\nCreate an account\n')
    glb.GUI.db_admin['Create account'].pack()

    glb.GUI.db_admin['New Username'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['New Username'].pack()
    glb.GUI.db_admin['New Username'].insert(0, "Username")

    glb.GUI.db_admin['New Password'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['New Password'].pack()
    glb.GUI.db_admin['New Password'].insert(0, "Password")

    glb.GUI.db_admin['Email'] = tk.Entry(glb.GUI.db_admin['tab'])
    glb.GUI.db_admin['Email'].pack()
    glb.GUI.db_admin['Email'].insert(0, "Email for verification")

    glb.GUI.db_admin['Enter Information'] = tk.Button(glb.db_admin['tab'],text='Enter Information', command=ENTER METHOD HERE)
    glb.GUI.db_admin['Enter Information'].bind("<Button-1>",loginEvent)
    glb.GUI.db_admin['Enter Information'].pack()

    



