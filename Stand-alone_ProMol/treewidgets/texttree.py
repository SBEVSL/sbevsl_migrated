#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/texttree.py,v 1.3 2002/09/18 02:12:09 matt Exp $

"""

texttree.py
-----------

Provides the TextTree class, a TreeWidget subclass based on Tkinter.Text.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

import string
from Tkinter import *
from treewidgets.widget import TreeWidget
from treewidgets.node import TreeNode, TWTreeNode
from treewidgets.constants import *

LEFT_MARGIN = 2
INDENT_WIDTH = 16
SPACE_BEFORE = 2
SPACE_AFTER = 2
ICON_HSPACE = 6
TREE_WIDTH = 36
TREE_BG = 'white'

class TextTree(TreeWidget,Text):
    """
    A TreeWidget based on the Tkinter Text class.

    """

    _pack = Text.pack
    _pack_forget = Text.pack_forget
    _grid = Text.grid
    _grid_forget = Text.grid_forget
    _place = Text.place
    _place_forget = Text.place_forget

    def __init__(self,master,app=None,icons={},fonts={},funcs={},**tkconfig):
        """
        Create a TextTree instance.

        Arguments:
          master      -- the widget containing this one
          app         -- the application that uses this widget (default: None)
          icons       -- a dictionary of icon names or files (details below)
          fonts       -- a dictionary of font characteristics (details below)

        Standard Tkinter configuration options are also accepted (but not all
        implemented yet).

        Setting icons:

          By default, all nodes in the TreeWidget are displayed with the 'node'
          icon, which works but is rather boring. You may wish to use a
          different icon, or a set of icons varying according to the node type,
          or perhaps no icons at all. You can configure the icons according to
          your needs by creating the TreeWidget with an 'icons' argument. The
          value of this is either a dictionary, which we will call an icon map,
          or None to disable all icons.

          An icon map has the following predefined keys:

          'type'      -- the type of icon to use: either 'photo', for a 
                         Tkinter PhotoImage, or 'bitmap', for a BitmapImage.
          'path'      -- *if* the icons are to be created from image files,
                         this argument specifies the directory where those
                         files are to be found. If 'path' is omitted, 
                         built-in icons will be used.
          'all'       -- icon set for all nodes
          'default'   -- default icon set

          To associate a set of icons with a node type, add an item to the 
          icon map using the node type as a key:

              icon_map[<node_type>] = <icon_set>
        
          [What if there is a node type with the same name as one of the
           predefined keys? Obviously this concept needs a little work]

          An icon set is a tuple of three (3) icon names:
              
              (<plain_icon_name>,<collapsed_icon_name>,<expanded_icon_name>)

          Each icon name must be either a built-in icon name or a file name
          (with the extension but without the path). The plain icon will be
          used for nodes with no children, the collapse and expanded icons
          for nodes with children, alternating according to the node state.
          The built-in icons follow the common convention of displaying 
          collapsed nodes with plus signs and expanded nodes with minus signs.
          
        Setting fonts [not implemented in 8/28/2002 release]:
          
          When this feature is implemented, you will be able to configure
          fonts on a per-node-type basis by giving the widget a font map
          similar to the icon map described above.
          
        """
        #TreeWidget.__init__(self,Text,master,app,width=TREE_WIDTH,bg=TREE_BG)
        TreeWidget.__init__(self,master,app,funcs=funcs)
        tkconfig.update({'state': 'disabled', 'width': TREE_WIDTH,
        #tkconfig.update({'width': TREE_WIDTH,
                         'bg': TREE_BG,'cursor':'left_ptr'})
        # doesn't work because 'icons' is in tkconfig
        apply(Text.__init__,(self,self._frame),tkconfig)

        self._gui_setup(icons,fonts)
        
        global_font = self.fonts.get('all')
        if global_font:
            self.configure(font=global_font)

        self.bind('<Up>',self._onUp)
        self.bind('<Down>',self._onDown)
        self.bind('<space>',self._onSpace)
        self.bind('<Enter>',self._setFocus)
        self.bind('<Return>',self._onReturn)
        self.bind('<Escape>',self._onEscape)

    def _setFocus(self, event=None):
        self.focus_set()

    def _show_node(self, node, row):
        row = row + 1
        indent = INDENT_WIDTH * node.depth() + LEFT_MARGIN
        id = node.id
        start = '%s.0' % row
        end = '%s.end' % row
        si = self.icons
        icons = si.get('all', si.get(node.type, si.get('default')))
        if icons:
            if (node.state & NS_EXPANDED and node.state & NS_HAS_CHILDREN):
                icon = icons[2]
            elif node.state & NS_HAS_CHILDREN:
                icon = icons[1]
            else:
                icon = icons[0]
            self.image_create(start, name='%s-icon' % id,
                              image=icon, padx=ICON_HSPACE)
        sf = self.fonts
        font = sf.get('all',sf.get(node.type,sf.get('default')))
        label = node.name
        if label[-1] != '\n':       # NOT os.linesep--'\n' is cross-platform
            label = "%s\n" % label
        self.insert(end, label)
        self.tag_add('node',start,end)
        self.tag_add(node.type,start,end)
        self.tag_add(id,start,end)
        self.tag_add('node-label','%s.1' % row,end)
        self.tag_add('%s-label' % id,'%s.1' % row,end)
        self.tag_configure(id,lmargin1=indent,spacing1=SPACE_BEFORE,
                           spacing3=SPACE_AFTER)
        node._set_bindings()
        return 1

    def _hide_node(self, node):
       # r = self.tag_ranges(node.id)
       # assert len(r) <= 2
        #start = r[0]
        #endrow = int(string.split(start,'.')[0]) + 1
        #end = '%d.0' % endrow
       # self.delete(start,end)
        return 1

    def _move_node(self, node, distance):
        pass

    def selectNode(self, node_id):
        """
        Display a node using the 'selected' colors and set self.selected to this node's ID.

        Arguments:
        node_id         -- The id of the node you wish to select.
        
        """
        if self.selected:
            self.deselectNode(self.selected)
        self.selected = node_id
        self.tag_configure('%s-label' % node_id, background=self.selected_bg,
                           foreground=self.selected_fg)
        self.update_idletasks()

    def deselectNode(self, node_id):
        """
        Display a node using the normal colors.
        
        Arguments:
        node_id         -- The id of the node you wish to deselect.
        
        """
        self.tag_configure('%s-label' % node_id, background=self.normal_bg,
                           foreground=self.normal_fg)

    def activateNode(self, node_id):
        """
        Change a node's colors to the "active" scheme.

        Arguments:
        node_id         -- The id of the node to be activated.

        """
        #self.tag_configure('%s-label' % node_id, foreground=self.active_fg)
        if self.selected == node_id:
            self.tag_configure('%s-label' % node_id, foreground=self.sel_act_fg)
        else:
            self.tag_configure('%s-label' % node_id, foreground=self.active_fg)
        self.glimpseFunc(self.getNodeByID(node_id))

    def deactivateNode(self, node_id):
        """
        Change a node's colors to the normal scheme.

        Arguments:
        node_id         -- The id of the node to be deactivated.

        """
        #self.tag_configure('%s-label' % node_id, foreground=self.normal_fg)
        if self.selected == node_id:
            self.tag_configure('%s-label' % node_id, foreground=self.selected_fg)
        else:
            self.tag_configure('%s-label' % node_id, foreground=self.normal_fg)
        self.unGlimpseFunc(self.getNodeByID(node_id))

    def redisplay(self):
        """Refresh the tree display after showing, hiding, or moving nodes."""
        self.configure(state='normal')
        TreeWidget.redisplay(self)
        self.configure(state='disabled')

    def destroy(self):
        """Eliminate the GUI manifestation of this object."""
        Text.destroy(self)
        self._frame.destroy()



if __name__ == '__main__':
    testapp = Tk()
    tt = TextTree(testapp,testapp)
    tt.pack()
    testapp.mainloop()
    
