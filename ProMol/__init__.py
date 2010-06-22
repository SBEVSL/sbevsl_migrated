'''
Connects ProMol to PyMol
'''
from pmg_tk.startup.ProMol.promolglobals import VERSION
from pmg_tk.startup.ProMol.GUI.main import start
import pmg_tk.startup.ProMol.ChimeConverter

def __init__(self):
    '''
    This will attach `ProMol` with `Pymol` though the plugin menu.
    '''
    self.menuBar.addmenuitem('Plugin', 'command',
                             label = 'ProMol %s'%VERSION,
                             command = lambda s=self:start(s))
