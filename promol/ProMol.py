'''
Starts the ProMol Plugin for Pymol.
'''
from pymol import cmd
import Tkinter as tk
from tkFileDialog import askopenfilename
import Pmw
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
                             command = lambda s = self : promol(s, 1))
    promol(self, 0)

def promol(pymol, user_click):
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
            getPdb()
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

    lab = tk.Label(interior, text = 'ProMol \nDeveloped By: '+
            'The SBEVSL Team Version 3.03, 2009', background = '#000066',
            foreground = 'white')
    lab.pack(expand = 0, fill = 'x', padx = 4, pady = 0)

    notebook = Pmw.NoteBook(interior)
    notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

    pglob.Tabs['welcome'] = notebook.add('Welcome')
    from pmg_tk.startup.ProMol_dir.Tabs import welcome
    welcome.initialise()

    pglob.Tabs['batch_motif'] = notebook.add('Batch Motif')
    from pmg_tk.startup.ProMol_dir.Tabs import batch_motif
    batch_motif.initialise()
    
    pglob.Tabs['ez_viz'] = notebook.add('EZ-Viz')
    from pmg_tk.startup.ProMol_dir.Tabs import ez_viz
    ez_viz.initialise()
    
    pglob.Tabs['motifs'] = notebook.add('Motifs')
    from pmg_tk.startup.ProMol_dir.Tabs import motifs
    motifs.initialise()
    
    pglob.Tabs['custom_motifs'] = notebook.add('Custom\nMotifs')
    from pmg_tk.startup.ProMol_dir.Tabs import custom_motifs
    custom_motifs.initialise()
    
    pglob.Tabs['motif_maker'] = notebook.add('Motif Database')
    from pmg_tk.startup.ProMol_dir.Tabs import motif_maker
    motif_maker.initialise()
    
    pglob.Tabs['view'] = notebook.add('View\nOptions')
    from pmg_tk.startup.ProMol_dir.Tabs import view
    view.initialise()
    
    pglob.Tabs['toolbox'] = notebook.add('Toolbox')
    from pmg_tk.startup.ProMol_dir.Tabs import toolbox
    toolbox.initialise()
    
    pglob.Tabs['advanced_toolbox'] = notebook.add('Advanced\n Toolbox')
    from pmg_tk.startup.ProMol_dir.Tabs import advanced_toolbox
    advanced_toolbox.initialise()
    
    pglob.Tabs['movie_maker'] = notebook.add('Movie\n Maker')
    from pmg_tk.startup.ProMol_dir.Tabs import movie_maker
    movie_maker.initialise()

    notebook.setnaturalsize()
