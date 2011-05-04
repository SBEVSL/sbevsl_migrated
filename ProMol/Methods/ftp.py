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
from ftplib import all_errors
import Tkinter as tk
import tkMessageBox
import re

#Create the ftp instance
ftp = FTP()

#Listing of supported file types, to add a file type
#just add it to this listing
filetypes = ['pdb', 'ent', 'cif']


def ftplistadd(dirline):
    glb.GUI.motifs['ftplist'].insert(tk.END, dirline)
    	
def openftp(event = None):
    
    ftpaddress = glb.GUI.motifs['ftptxt'].get()
    global ftp 
    try:
    	ftp = FTP(ftpaddress)
    	ftp.login()
    except all_errors: 
    	tkMessageBox.showwarning("Error", "Could not connect to server.")
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

def searchdirectory(directory, timeout = 200):   
    
    filetree = ftp.nlst(directory)
    timeout = timeout
    for loc in filetree:
    	splits = loc.split(".")
    	for split in splits:
    		if split in filetypes:
    			glb.GUI.motifs['multipdb'].insert(0.0, ", " + loc[3:7])
    			break
    	else:
    		thisdir = directory + '/' + loc
    		searchdirectory(thisdir, timeout)
    	if timeout <= 0:
    	 	break
    	timeout = timeout - 1
    	    

def openftpdir():
       
    index = glb.GUI.motifs['ftplist'].curselection()[0] 
    directory = glb.GUI.motifs['ftplist'].get(index)
    print("Opened FTP directory: '" + ftp.pwd() + '/' + directory + "'")
    ftp.cwd(ftp.pwd() + '/' + directory)
    glb.GUI.motifs['ftppath'].delete(0, tk.END)
    glb.GUI.motifs['ftppath'].insert(tk.END, ftp.pwd() + '/')
    glb.GUI.motifs['multipdb'].delete(0.0, tk.END)
    searchdirectory(ftp.pwd(),  int(glb.GUI.motifs['toval'].get()) )
    glb.GUI.motifs['multipdb'].delete(0.0, 1.2)
    ftpup()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


