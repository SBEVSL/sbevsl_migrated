'''
Connects ProMol to PyMol
'''
#sets up promol
from ProMol.promolglobals import VERSION

#command line interpreters
#not necessary when not using pymol
#import ProMol.ChimeConverter

#GUI
from ProMol import GUI

def __init__():
    '''
    This will attach `ProMol` with `Pymol` though the plugin menu.
    '''
##    pymol.menuBar.addmenuitem('Plugin', 'command', label = 'ProMol %s'%VERSION,
##        command = lambda p=pymol:GUI.__init__(p))
    GUI.__init__()
__init__()
