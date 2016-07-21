import Tkinter as tk
import os
from ProMol import promolglobals as glb

def initialise():
    tab = glb.GUI.welcome['tab']
    titleLabel = tk.Label(tab, text='ProMOL', font=('Times', 28))
    titleLabel.grid(row=0, column=0)
    #versionLabel = tk.Label(tab, text='Version {0}'.format(glb.VERSION), font=('Times', 18))
    versionLabel = tk.Label(tab, text='Version %s'%(glb.VERSION), font=('Times', 18))
    versionLabel.grid(row=1, column=0)
    messagebox = tk.Frame(tab)
    yscroll = tk.Scrollbar(messagebox, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
    messagetext = tk.Text(messagebox, yscrollcommand=yscroll.set, wrap=tk.WORD, width=10, height=10)
    messagetext.insert(tk.END, 'Welcome to ProMOL.\n')
    if len(glb.motifErrors) == 0:
        messagetext.insert(tk.END, 'All motifs loaded successfully.\n')
    else:
        #messagetext.insert(tk.END, 'Encountered {0} errors while loading motifs.\nSee below for details.\n'.format(len(glb.motifErrors)))
        messagetext.insert(tk.END, 'Encountered %s errors while loading motifs.\nSee below for details.\n'%(len(glb.motifErrors)))
    messagestring = '''
Developed by the SBEVSL Project

Partial funding provided by:
NSF DUE 0402408
NIGMS 1R15GM078077
NIGMS 1R15GM078077-01
NIGMS 3R15GM078077-01S
NIGMS 2R15GM078077-02 
NIGMS 3R15GM078077-02S1
RIT
Dowling College

This program is free software; you can redistribute it and/or \
modify it under the terms of the GNU General Public License as \
published by the Free Software Foundation; either version 2 of \
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied warranty of \
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the \
GNU General Public License for more details.

You should have received a copy of the GNU General Public License \
along with this program; if not, write to the Free Software \
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA \
02111-1307 USA'''
    messagetext.insert(tk.END, messagestring)
    if len(glb.motifErrors) > 0:
        messagetext.insert(tk.END, '\n\nMotif loading errors:')
    # It's OK that this is not indented.  It doesn't matter.
    for error in glb.motifErrors:
        messagetext.insert(tk.END, '\n\n')
        messagetext.insert(tk.END, error)
    messagetext.config(state=tk.DISABLED)
    messagetext.grid(row=0,column=0, sticky=tk.N+tk.E+tk.S+tk.W)
    yscroll['command'] = messagetext.yview
    messagebox.columnconfigure(0, weight=1)
    messagebox.rowconfigure(0, weight=1)
    messagebox.grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
    tab.rowconfigure(2, weight=1)
    tab.columnconfigure(0, weight=1)
