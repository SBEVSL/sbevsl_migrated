'''The GUI for ProMol'''
from pymol import cmd
import Tkinter as tk
from tkFileDialog import askopenfilename
import Pmw
from pmg_tk.startup.ProMol import promolglobals as pglob
from pmg_tk.startup.ProMol.remote_pdb_load import PDBDialog
Pmw.initialise()

def start(pymol):
    '''
    This starts the promol GUI.
    '''
    def bottom_buttons(result):
        '''
        Resultants of clicking buttons at the bottom of gui.
        '''
        if result == 'Open PDB':
            pdb = askopenfilename(initialdir = pglob.HOME)
            if pdb:
                cmd.load(pdb)
                pglob.update()
        elif result == 'Help':
            import webbrowser
            try:
                webbrowser.open(pglob.pathmaker('Help','EZ-Viz.chm'))
            except:
                webbrowser.open(pglob.pathmaker('Help','EZ-VizWebMain.html'))
        elif result == 'Fetch PDB':
            PDBDialog(pymol)
            pglob.update()
        elif result == 'Clear':
            cmd.reinitialize()
        elif result == 'Thanks':
            import webbrowser
            webbrowser.open(pglob.pathmaker('Thanks.html'))
        else:
            ProMol.withdraw()
    
    ProMol = tk.Toplevel()
    ProMol.title('ProMol Version %s'%(pglob.VERSION))
    
    buttons = ('Open PDB', 'Fetch PDB', 'Clear', 'Help', 'Thanks' , 'Quit')
    buttonsl = len(buttons)

    notebook = Pmw.NoteBook(ProMol)
    notebook.grid(row=0,column=0, columnspan=buttonsl, padx=10, pady=10)
    from pmg_tk.startup.ProMol.GUI import welcome, ez_viz, motifs, \
        custom_motifs, motif_maker, view, toolbox, advanced_toolbox, movie_maker

    pglob.GUI['welcome'] = {'tab':notebook.add('Welcome')}
    welcome.initialise()

    pglob.GUI['ez_viz'] = {'tab':notebook.add('EZ-Viz')}
    ez_viz.initialise()
    
    pglob.GUI['motifs'] = {'tab':notebook.add('Motif Finder')}
    motifs.initialise()
    
    #pglob.GUI['custom_motifs'] = {'tab':notebook.add('Custom\nMotifs')}
    #custom_motifs.initialise()
    
    pglob.GUI['motif_maker'] = {'tab':notebook.add('Motif Maker')}
    motif_maker.initialise()
    
    pglob.GUI['view'] = {'tab':notebook.add('View\nOptions')}
    view.initialise()
    
    #pglob.GUI['toolbox'] = {'tab':notebook.add('Toolbox')}
    #toolbox.initialise()
    
    #pglob.GUI['advanced_toolbox'] = {'tab':notebook.add('Advanced\n Toolbox')}
    #advanced_toolbox.initialise()
    
    #pglob.GUI['movie_maker'] = {'tab':notebook.add('Movie\n Maker')}
    #movie_maker.initialise()

    notebook.setnaturalsize()
    
    tk.Canvas(ProMol, height=1, bg='#696969', borderwidth=1, relief=tk.SUNKEN).grid(row=1, column=0,
        columnspan=buttonsl, sticky=tk.E+tk.W)
    
    max = 0
    buttonsref = []
    for i in range(buttonsl):
        buttonsref.append(tk.Button(ProMol, text=buttons[i], 
            command=lambda b=buttons[i]:bottom_buttons(b)))
        buttonsref[i].grid(row=2, column=i, pady=10)
        width = ProMol.grid_bbox(i, 1)[2]
        max = width>max and width or max
    for i in range(buttonsl):
        ProMol.grid_columnconfigure(i,minsize=max)
        buttonsref[i]['width'] = max/buttonsl
    
    #pymol_geo = pymol.winfo_geometry()
    #promol_geo = ProMol.geometry()
    
    #ProMol.geometry('%s+%s+%s'%(promol_geo.split('+')[0],pymol_geo.split('x')[0],pymol_geo.split('+')[2]))
        
    pglob.update()
