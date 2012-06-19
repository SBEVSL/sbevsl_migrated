import MySQLdb
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.ProMol import databasemanager as dbm
import tkMessageBox

def toggleDB():
    glb.USEDB = not glb.USEDB
    if glb.USEDB:
        glb.HOST = glb.GUI.db_admin['Server'].get()
        glb.UN = glb.GUI.db_admin['Username'].get()
        glb.PW = glb.GUI.db_admin['Password'].get()
        glb.DB = glb.GUI.db_admin['Database'].get()
        try:
            dm = dbm.databaseManager() #Creates a databasemanager
        except Exception as e:
            glb.USEDB = False
            print "Failed to connect to the database:", e
            tkMessageBox.showerror("Database Connection Failed",
                                   "Failed to connect to the database." +
                                   "  See the PyMOL console for details.")
        else:
            glb.GUI.db_admin['Use Database'].config(text='Disconnect')
            dm.update() #Updates the database
            dm.close() #Closes the dbm's connection to the db
    else:
        glb.GUI.db_admin['Use Database'].config(text='Connect')
