'''The GUI for ProMol'''
from pymol import cmd
import Tkinter as tk
from tkFileDialog import askopenfilename
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
from pmg_tk.startup.remote_pdb_load import FetchPDB as showFetchDialog
Pmw.initialise()

def __init__(pymol):
    '''
    This starts the promol GUI.
    '''
    def bottom_buttons(result):
        '''
        Resultants of clicking buttons at the bottom of gui.
        '''
        if result == 'Open PDB':
            pdb = askopenfilename(initialdir = glb.HOME)
            if pdb:
                cmd.load(pdb)
                glb.update()
        elif result == 'Random PDB':
            glb.randompdb()
        elif result == 'Fetch PDB':
            showFetchDialog(pymol)
            glb.update()
        elif result == 'Clear':
            cmd.reinitialize()
        else:
            ProMol.withdraw()
    
    ProMol = tk.Toplevel()
    ProMol.minsize(600, 600)
    ProMol.title('ProMOL %s'%(glb.VERSION))
    
    buttons = ('Open PDB', 'Fetch PDB', 'Random PDB', 'Clear')
    buttonsl = len(buttons)

    notebook = Pmw.NoteBook(ProMol)
    notebook.grid(row=0, column=0, padx=3, pady=3, sticky=tk.N+tk.E+tk.S+tk.W)

    from pmg_tk.startup.ProMol.GUI import welcome, ez_viz, motifs, \
        motif_maker, view, db_admin
        
    # Removed unused toolboxes, movie_maker and save modules
    # We think we made sure this won't have side effects or
    # dependency problems. -Kip

    # Don't be fooled: initialise() is being called on the imports
    # NOT on the fields of glb.GUI with the same names
    # glb.GUI.welcome != welcome
    glb.GUI.welcome = {'tab':notebook.add('Welcome')}
    welcome.initialise()

    glb.GUI.ez_viz = {'tab':notebook.add('EZ-Viz')}
    ez_viz.initialise()
    
    glb.GUI.motifs = {'tab':notebook.add('Motif Finder')}
    motifs.initialise()
    
    glb.GUI.motif_maker = {'tab':notebook.add('Motif Maker')}
    motif_maker.initialise()
    
    glb.GUI.view = {'tab':notebook.add('View Options')}
    view.initialise()
    
    glb.GUI.db_admin = {'tab':notebook.add('Database')}
    db_admin.initialise()
    
    buttonsref = []
    buttonframe = tk.Frame(ProMol)
    for i in range(buttonsl):
        buttonsref.append(tk.Button(buttonframe, text=buttons[i], 
            command=lambda b=buttons[i]:bottom_buttons(b)))
        buttonsref[i].grid(row=0, column=i, padx=1)
        buttonframe.columnconfigure(i, weight=1)
    buttonframe.grid(row=1, column=0, sticky=tk.S, pady=1)
    ProMol.columnconfigure(0, weight=1)
    ProMol.rowconfigure(0, weight=1)
    glb.update()
