#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/canvastree.py,v 1.1.1.1 2002/08/21 05:18:56 matt Exp $

"""

canvastree.py
-------------

A TreeWidget based on the Tkinter Canvas class.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
from treewidgets.widget import TreeWidget

class CanvasTree(TreeWidget, Canvas):

    _pack = Canvas.pack
    _pack_forget = Canvas.pack_forget
    _grid = Canvas.grid
    _grid_forget = Canvas.grid_forget
    _place = Canvas.place
    _place_forget = Canvas.place_forget

    def __init__(self,master,app=None):
        TreeWidget.__init__(self,Canvas,master,app)


if __name__ == '__main__':
    testapp = Tk()
    ct = CanvasTree(testapp,testapp)
    ct.pack()
    testapp.mainloop()
