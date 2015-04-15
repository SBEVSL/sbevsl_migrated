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
from tkFileDialog import *
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from Tkinter import *
from pmg_tk.startup.treewidgets import widget, node, texttree
from pmg_tk.startup.treewidgets.constants import *
import Tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
import pmg_tk.startup.ProMol.Methods.proutils as proutils
import pmg_tk.startup.ProMol.Methods.motifset as motifset
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
    
# cdb 3/31/15
# takes a file consisting of 1 list of pdbids at one pdbid on each line and uploads 
# it into the entry box  
def askopenfilename():

    fileoptions = {}
    fileoptions['defaultextension'] = '.txt'
    fileoptions['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    fileoptions['initialdir'] = 'C:\\'
    fileoptions['initialfile'] = ''
    fileoptions['title'] = 'Select a file of proteins'

    filename = tkFileDialog.askopenfilename(**fileoptions)
 
    if len(filename) != 0:
	    fo = open(filename, 'r')
    else:
	    fo = False
	
    if fo is True:
	    query = ""
	    linecount = 0
	    for line in fo:
		    linecount += 1;
		    line = line.strip().replace('\n','')
		    if len(line) is not 0:
			    query+= line + ", "

	#account for empty files
	    if linecount > 1:
		    query = query[:-2]
	
	    fo.close()
	    glb.GUI.motifs['multipdb'].insert(END,query)
	