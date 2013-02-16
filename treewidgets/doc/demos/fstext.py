#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/doc/demos/fstext.py,v 1.2 2002/09/18 02:13:45 matt Exp $

"""

fstext.py
---------

Demo of a TextTree widget displaying a tree of FSTreeNode objects.

Displays the current directory by default, but you can use the -d
option to specify another directory:

    fstext.py -d /var/foo/bar

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
from pmg_tk.startup.treewidgets.constants import *
from pmg_tk.startup.treewidgets.texttree import TextTree
import os.path

def test(top=None):

    if not top:
        top = os.path.abspath('.')

    win = Tk()
    win.title("File System Tree")
    tt = TextTree(win,win,icons={'type': 'photo',
                                 'directory': ('folder',
                                               'folderplus',
                                               'folderminus'),
                                 'file': ('page',
                                          'pageplus',
                                          'pageminus'),
                                 'symlink': ('symlink',
                                             'symlinkplus',
                                             'symlinkminus'),
                                 'default': ('node',
                                             'nodeplus',
                                             'nodeminus')},
                  funcs={'showContent': dummy.showContent,
                         'showAtts': dummy.showAtts,
                         'glimpse': dummy.glimpse,
                         'unGlimpse': dummy.unGlimpse})
                                             
    tt.pack(expand=YES,fill=BOTH)
    tt.showTree(top,DT_FILESYSTEM,1,
                props=NP_AUTOBUILD|NP_ALLOW_CHILDREN,
                state=NS_EXPANDED)

    return (win, tt)

if __name__ == '__main__':
    import sys, getopt

    opts, args = getopt.getopt(sys.argv[1:],'d:',['directory='])
    
    top = None
    for opt, val in opts:
        if opt in ('-d','--directory'):
            top = val
  
    win, tt = test(top)
    win.mainloop()
