import Tkinter as tk
from pmg_tk.startup.ProMol_dir import promolglobals as pglob

def initialise():
    canvas = tk.Canvas(pglob.Tabs['welcome'])
    canvas.pack(fill = 'both', expand = 1)
    canvas.create_image(0, 0, image = pglob.splash, anchor = tk.NW)