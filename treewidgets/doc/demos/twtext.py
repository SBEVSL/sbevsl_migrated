#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/doc/demos/twtext.py,v 1.2 2002/09/18 02:13:45 matt Exp $

"""

tttest.py
---------

Test script for texttree.TextTree.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
from pmg_tk.startup.treewidgets.constants import *
from pmg_tk.startup.treewidgets.texttree import TextTree
import dummyfuncs as dummy

def test():
    struct = {'type': 'Document',
              'name': "My Document",
              'properties': NP_ROOT|NP_ALLOW_CHILDREN|NP_AUTOBUILD,
              'children': [{'type': 'Section',
                            'name': "Section 1",
                            'children': [{'type': 'SubSection',
                                          'name': 'Subsection 1'},
                                         {'type': 'SubSection',
                                          'name': 'Subsection 2'}]},
                           {'type': 'Section',
                            'name': "Section 2",
                            'children': [{'type': 'SubSection',
                                          'name': 'Subsection 1'},
                                         {'type': 'SubSection',
                                          'name': 'Subsection 2'}]},
                           {'type': 'Section',
                            'name': "Section 3",
                            'children': [{'type': 'SubSection',
                                          'name': 'Subsection 1'},
                                         {'type': 'SubSection',
                                          'name': 'Subsection 2'}]}]}

    win = Tk()
    win.title("TWStruct Tree")
    tt = TextTree(win,win,funcs={'showContent': dummy.showContent,
                                 'showAtts': dummy.showAtts,
                                 'glimpse': dummy.glimpse,
                                 'unGlimpse': dummy.unGlimpse})
    tt.pack(expand=YES,fill=BOTH)
    tt.showTree(struct,DT_TWSTRUCT,-1,
                props=NP_AUTOBUILD|NP_ALLOW_CHILDREN,
                state=NS_EXPANDED)

    return (win, tt)

if __name__ == '__main__':
    win, tt = test()
    win.mainloop()
