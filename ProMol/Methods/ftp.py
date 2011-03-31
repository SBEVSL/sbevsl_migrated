#  ftp.py
#  ==============
#
#  This file contains all the code for the built in ftp client.
#  This client is used to search a directory on a ftp server 
#  for pdb files, and then run them all in the motif finder.
#
#  RJ Bacon
#
#  February 14th, 2011
#  
#  =================

from pmg_tk.startup.ProMol import promolglobals as glb
from ftplib import FTP
import Tkinter as tk
import re

#Create the ftp instance
ftp = FTP()


def ftplistadd(dirline):
    	glb.GUI.motifs['ftplist'].insert(tk.END, dirline)
    	
def openftp(event = None):
    
    ftpaddress = glb.GUI.motifs['ftptxt'].get()
    global ftp 
    ftp = FTP(ftpaddress)
    ftp.login()
    glb.GUI.motifs['ftppath'].insert(tk.END, ftp.pwd())
    glb.GUI.motifs['ftplist'].delete(0, tk.END)
    ftp.retrlines('NLST', ftplistadd)

def ftpcd(event):

    index = glb.GUI.motifs['ftplist'].curselection()[0]
    ftp.cwd(glb.GUI.motifs['ftppath'].get() + glb.GUI.motifs['ftplist'].get(index) + '/')
    glb.GUI.motifs['ftppath'].delete(0, tk.END)
    glb.GUI.motifs['ftppath'].insert(tk.END, ftp.pwd() + '/')
    glb.GUI.motifs['ftplist'].delete(0, tk.END)
    ftp.retrlines('NLST', ftplistadd)


def ftpup():
    
    ftp.cwd('..')
    glb.GUI.motifs['ftppath'].delete(0, tk.END)
    glb.GUI.motifs['ftppath'].insert(tk.END, ftp.pwd() + '/')
    glb.GUI.motifs['ftplist'].delete(0, tk.END)
    ftp.retrlines('NLST', ftplistadd)

def searchdirectory(filetree, timeout = 200):   
    
    thisdir = ftp.pwd() + '/'	
    timeout = timeout
    for loc in filetree:
    	if loc.endswith(".pdb"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".pdb")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	elif loc.endswith(".ent"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".ent")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	elif loc.endswith(".ent.gz"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".ent.gz")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	elif loc.endswith(".cif"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".cif")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	elif loc.endswith(".pdb.gz"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".pdb.gz")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	elif loc.endswith(".cif.gz"):
    	       pdbfile = loc.lstrip("pdb")
    	       pdbfile = pdbfile.rstrip(".cif.gz")
    	       glb.GUI.motifs['multipdb'].insert(0.0, ", " + pdbfile)
    	else:
    	 	    newtree = []
    	 	    thisdir = thisdir + loc
    		    newtree = ftp.nlst(thisdir)
    		    searchdirectory(newtree, timeout)
    	if timeout <= 0:
    	 	break
    	timeout = timeout - 1
    	    

def openftpdir():
       
    index = glb.GUI.motifs['ftplist'].curselection()[0] 
    directory = glb.GUI.motifs['ftplist'].get(index)
    print("Opened FTP directory: '" + ftp.pwd() + '/' + directory + "'")
    filetree = ftp.nlst(ftp.pwd() + '/' + directory)
    ftp.cwd(ftp.pwd() + '/' + directory)
    glb.GUI.motifs['ftppath'].delete(0, tk.END)
    glb.GUI.motifs['ftppath'].insert(tk.END, ftp.pwd() + '/')
    glb.GUI.motifs['multipdb'].delete(0.0, tk.END)
    searchdirectory(filetree,  int(glb.GUI.motifs['toval'].get()) )
    glb.GUI.motifs['multipdb'].delete(0.0, 1.2)
    ftpup()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


