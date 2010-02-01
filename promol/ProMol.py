'''
Starts the ProMol Plugin for Pymol.
'''
from pymol import cmd
import Tkinter as tk
from tkFileDialog import askopenfilename
import Pmw
from pmg_tk.startup.ProMol_dir.remote_pdb_load import PDBDialog
from pmg_tk.startup.ProMol_dir import promolglobals as pglob

Pmw.initialise()

def __init__(self):
    '''
    This will attach `ProMol` with `Pymol` though the plugin menu.
    
    Will open ProMol when pymol opens. But will close immediately.
    Will open and stay open only when user clicks the on menu button.
    This allows ProMol to do setup stuff before being 'opened'
    '''
    self.menuBar.addmenuitem('Plugin', 'command',
                             'Easy GUI',
                             label = 'ProMol 3.03',
                             command = lambda s = self : promol(s))
    promol(self, 0)

def promol(pymol, user_click = 1):
    '''
    This starts promol. As well as setup the GUI.
    '''
    def acknowledge():
        '''
            Acknowledgements.
        '''
        import webbrowser
        webbrowser.open('./modules/pmg_tk/startup/Thanks.html')

    def promol_help():
        '''
            Help Files.
        '''
        import webbrowser
        try:
            webbrowser.open('./modules/pmg_tk/startup/Help/EZ-Viz.chm')
        except:
            webbrowser.open('./modules/pmg_tk/startup/Help/EZ-VizWebMain.html')

    def bottom_buttons(result):
        '''
            Resultants of clicking buttons at the bottom of gui.
        '''
        if result == 'Open':
            pdb = askopenfilename(initialdir = './PyMol')
            if pdb:
                cmd.load(pdb)
        elif result == 'Help':
            promol_help()
        elif result == 'Fetch PDB':
            PDBDialog(pymol)
            pglob.update()
        elif result == 'Clear':
            cmd.reinitialize()
        elif result == 'Thanks':
            acknowledge()
        else:
            dialog.withdraw()
    dialog = Pmw.Dialog(pymol.root, buttons = ('Open', 'Fetch PDB',
        'Clear', 'Help', 'Thanks' , 'Quit'),
        title = 'ProMol', command = bottom_buttons)
    interior = dialog.interior()
    if not user_click:
        bottom_buttons('Quit')

    lab = tk.Label(interior, text = 'ProMol Version 3.03\nDeveloped By: '+
            'The SBEVSL Team', background = '#000066',
            foreground = 'white')
    lab.pack(expand = 0, fill = 'x', padx = 4, pady = 0)

    notebook = Pmw.NoteBook(interior)
    notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)
    from pmg_tk.startup.ProMol_dir.Tabs import welcome, batch_motif, ez_viz,\
        motifs, custom_motifs, motif_maker, view, toolbox, advanced_toolbox,\
        movie_maker
    
    pglob.Tabs['welcome'] = {'tab':notebook.add('Welcome')}
    welcome.initialise()

    pglob.Tabs['batch_motif'] = {'tab':notebook.add('Batch Motif')}
    batch_motif.initialise()
    
    pglob.Tabs['ez_viz'] = {'tab':notebook.add('EZ-Viz')}
    ez_viz.initialise()
    
    pglob.Tabs['motifs'] = {'tab':notebook.add('Motifs')}
    motifs.initialise()
    
    pglob.Tabs['custom_motifs'] = {'tab':notebook.add('Custom\nMotifs')}
    custom_motifs.initialise()
    
    pglob.Tabs['motif_maker'] = {'tab':notebook.add('Motif Database')}
    motif_maker.initialise()
    
    pglob.Tabs['view'] = {'tab':notebook.add('View\nOptions')}
    view.initialise()
    
    pglob.Tabs['toolbox'] = {'tab':notebook.add('Toolbox')}
    toolbox.initialise()
    
    pglob.Tabs['advanced_toolbox'] = {'tab':notebook.add('Advanced\n Toolbox')}
    advanced_toolbox.initialise()
    
    pglob.Tabs['movie_maker'] = {'tab':notebook.add('Movie\n Maker')}
    movie_maker.initialise()

    notebook.setnaturalsize()
    
    pglob.update()