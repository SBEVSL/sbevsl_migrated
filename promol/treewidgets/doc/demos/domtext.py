#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/doc/demos/domtext.py,v 1.2 2002/09/18 02:13:45 matt Exp $

"""

domtree.py
----------

Test script for texttree.TextTree.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
from pmg_tk.startup.treewidgets.constants import *
from pmg_tk.startup.treewidgets.texttree import TextTree
from xml.dom.ext.reader import PyExpat
from xml.dom import Node
import os
import addresses
import dummyfuncs as dummy

def test(file=None):
    
    reader = PyExpat.Reader()

    if xml_file and os.path.exists(xml_file):
        s = open(file)
    else:
        s = addresses.xmlstream
    struct = reader.fromStream(s)
    s.close()

    # This icon map or something like it should probably be the default
    # for trees of DOMTreeNode's, but there's no mechanism for setting a
    # default yet.
    iconmap = {'type': 'photo',
               Node.DOCUMENT_TYPE_NODE: ('doctype', 'doctypeplus',
                                         'doctypeminus'),
               Node.COMMENT_NODE: ('comment','commentplus',
                                   'commentminus'),
               Node.ELEMENT_NODE: ('xmlelt','xmleltplus',
                                   'xmleltminus'),
               Node.ATTRIBUTE_NODE: ('xmlatt','xmlattplus',
                                     'xmlattminus'),
               Node.TEXT_NODE: ('xmltext','xmltextplus',
                                'xmltextminus'),
               'default': ('node','nodeplus','nodeminus')}

    win = Tk()
    win.title("DOM Tree")
    tt = TextTree(win,win,icons=iconmap,
                  funcs={'showContent': dummy.showContent,
                         'showAtts': dummy.showAtts,
                         'glimpse': dummy.glimpse,
                         'unGlimpse': dummy.unGlimpse})
    tt.pack(expand=YES,fill=BOTH)
    tt.showTree(struct,DT_XMLDOM,1,
                props=NP_AUTOBUILD|NP_ALLOW_CHILDREN|NP_ABSTRACT,
                state=NS_EXPANDED)

    return (win, tt)

if __name__ == '__main__':
    import sys, getopt

    opts, args = getopt.getopt(sys.argv[1:],'f:',['file='])
    
    xml_file = None
    for opt, val in opts:
        if opt in ('-f','--file'):
            xml_file = val
    if xml_file and xml_file[0] == '~' and os.name == 'posix':
        xml_file = os.path.join(os.environ.get('HOME'),xml_file[1:])
    
    win, tt = test(xml_file)
    win.mainloop()

