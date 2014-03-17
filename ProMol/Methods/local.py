from pymol import cmd
from pymol import stored
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
from pmg_tk.startup.treewidgets import widget, node, texttree
from pmg_tk.startup.treewidgets.constants import *
import Tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
import pmg_tk.startup.ProMol.load_csa_lit as lib
import pmg_tk.startup.ProMol.Methods.proutils as proutils
import pmg_tk.startup.ProMol.Methods.motifset as motifset
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
pdbsl = 0
Pmw.initialise()

#loads a PDB file from hard drive
#the custom file is added to multipdb textbox, saved to the PDBDownloads file, and read from there
#only for LINUX: filenames are case sensitive, only works when the filenames are all lower case
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
            #if len(glb.GUI.motifs['multipdb'].get()) > 0:
            #    name = ', ' + name
            #name += ','
            glb.GUI.motifs['multipdb'].insert(END, name) 
            print "Loaded local file " + pdb
        except: 
            showerror("Open Source File", "Failed to read file \n'%s'"%pdb)
            return

#this method simply clears out everything from the pdb textbox			
def clearpdbinput():
    glb.GUI.motifs['multipdb'].delete(1.0, END)