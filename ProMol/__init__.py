'''
Connects ProMol to PyMol
'''
#sets up promol
from pmg_tk.startup.ProMol.promolglobals import VERSION

#command line interpreters
import pmg_tk.startup.ProMol.ChimeConverter

#GUI
from pmg_tk.startup.ProMol import GUI

def __init__(pymol):
    '''
    This will attach `ProMol` with `Pymol` though the plugin menu.
    '''
    pymol.menuBar.addmenuitem('Plugin', 'command', label = 'ProMol %s'%VERSION,
        command = lambda p=pymol:GUI.__init__(p))
