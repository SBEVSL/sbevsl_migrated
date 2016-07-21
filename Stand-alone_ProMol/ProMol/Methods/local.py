import Tkinter as tk
import Pmw
import os
import re
import time
import math
import tkFileDialog
from shutil import copy
from tkFileDialog import asksaveasfile, askdirectory, askopenfile, askopenfilename
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
from treewidgets import widget, node, texttree
from treewidgets.constants import *
import Tkinter as tk
import ProMol.promolglobals as glb
import ProMol.Methods.proutils as proutils
import ProMol.Methods.motifset as motifset
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
pdbsl = 0
Pmw.initialise()

#loads a PDB file from hard drive
#the custom file is added to multipdb textbox, saved to the PDBDownloads file, and read from there
def loadlocal(): 
    last_used_dir = glb.LAST_USED_DIR
    pdb = askopenfilename(filetypes = (("PDB files", "*.pdb"),("PDB files", "*.pdb")), initialdir = last_used_dir, multiple=False)
    if pdb is not None:
        glb.LAST_USED_DIR = os.path.dirname(pdb)
    if pdb: 
        try: 	
            copy(pdb, glb.FETCH_PATH)
            data = pdb.split("/")
            name = data[len(data) - 1].split(".")[0]
            #name += ', '
            glb.GUI.motifs['multipdb'].insert(END, name) 
            print "Loaded local file " + pdb
        except: 
            showerror("Open Source File", "Failed to read file \n'%s'"%pdb)
            return

#clears all input from the multipdb texbox
def clearpdbinput():
    glb.GUI.motifs['multipdb'].delete(1.0, END)
