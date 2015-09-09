#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/doc/demos/customtext.py,v 1.2 2002/09/18 02:13:45 matt Exp $

"""

customtext.py
-------------

Demonstrates a TextTree displaying autobuilt CustomTextNodes.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
from pmg_tk.startup.treewidgets.constants import *
from pmg_tk.startup.treewidgets.texttree import TextTree
import string
import dummyfuncs as dummy

## Just a utility function
def pageTitle2ID(title):
    """Converts a series of capitalized words to a lower-case page ID.
    """
    # This just converts everything to lowercase and truncates to
    # 12 characters. Needs some work.
    id = string.lower(string.join(string.split(title),''))[:12]
    id = string.replace(id,'/','%2F')
    return id

## The following 'node functions' allow the tree to be autobuilt
## See the CustomTreeNode.__init__ documentation for more info.
def nfGetType(node):
    tag = node[0]
    return {'P': 'page','F': 'folder', 'S': 'section'}.get(tag,'unknown')

def nfGetID(node):
    title = node[1]
    return pageTitle2ID(title)

def nfGetName(node):
    return node[1]

def nfSetName(node, newname):
    node[1] = newname

def nfGetChildren(node):
    return node[2]

def nfAddChild(node, newchild):
    node[2].append(newchild)

def nfDelChild(node, badchild):
    if badchild in node[2]:
        node[2].remove(badchild)

def test():
    struct = ['F',"LiteSite Docs",
              [['P', 'Overview', []],
               ['F', 'Tutorial',
                [['P', 'Concepts', []],
                 ['P', 'Installation', []],
                 ['P', 'Site Maps', []],
                 ['P', 'Templates', []],
                 ['P', 'Creating Pages', []]]]]]

    win = Tk()
    win.title("Custom Tree")
    iconmap = {'type': 'photo',
               'folder': ('folder','folderplus','folderminus'),
               'page': ('page','pageplus','pageminus'),
               'section': ('sect','sectplus','sectminus'),
               'default': ('node','nodeplus','nodeminus')}
    tt = TextTree(win,win,icons=iconmap,
                  funcs={'showContent': dummy.showContent,
                         'showAtts': dummy.showAtts,
                         'glimpse': dummy.glimpse,
                         'unGlimpse': dummy.unGlimpse})
    tt.pack(expand=YES,fill=BOTH)
    tt.showTree(struct,DT_CUSTOM,-1,
                node_funcs={'type': nfGetType,
                            'id': nfGetID,
                            'get_name': nfGetName,
                            'set_name': nfSetName,
                            'get_children': nfGetChildren,
                            'add_child': nfAddChild,
                            'del_child': nfDelChild},
                props=NP_AUTOBUILD|NP_ALLOW_CHILDREN,
                state=NS_EXPANDED)

    return (win, tt)

if __name__ == '__main__':
    win, tt = test()
    win.mainloop()
