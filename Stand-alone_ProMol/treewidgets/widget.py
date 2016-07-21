#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/widget.py,v 1.3 2002/09/18 02:10:16 matt Exp $

"""

widget.py
---------

Provide the TreeWidget class, an abstract base class for different types
of TreeWidgets.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from Tkinter import *
import tkFont, os
from constants import *
from treewidgets.node import TWTreeNode, DOMTreeNode, FSTreeNode, CustomTreeNode
from util import warn

FONTS = {'all': {'family': ['helvetica','arial','geneva','swiss'], 'size': 11}}
#NORMAL_FG = 'black'
NORMAL_FG = '#000000'
#NORMAL_BG = 'white'
NORMAL_BG = '#ffffff'
#ACTIVE_FG = 'blue'
ACTIVE_FG = '#0000ff'
SELECTED_BG = '#000080'
#SELECTED_FG = 'white'
SELECTED_FG = '#ffffff'
SEL_ACT_FG = '#ffff00'



class TreeWidget:
    """
    Base class for GUI widgets that display tree structures.

    This class cannot be instantiated directly. Please use one of its
    subclasses, TextTree or CanvasTree.

    """
    
    def __init__(self,master,app=None,funcs={}):
        """
        Create a TreeWidget instance.

        Arguments:
        master      -- the widget that contains this one

        Keyword arguments:
        app         -- the application object (default: None)

        """

        self.master = master
        if app:
            self.app = app
        elif not app and hasattr(master,'app'):
            self.app = master.app
        else:
            self.app = master

        self.showContentFunc = funcs.get('showContent',lambda n: None)
        self.showAttsFunc = funcs.get('showAtts',lambda n: None)
        self.glimpseFunc = funcs.get('glimpse',lambda n: None)
        self.unGlimpseFunc = funcs.get('unGlimpse',lambda n: None)

        self.all_nodes = []
        self._last_autoid = -1

        self.log = None
        
        f = self._frame = Frame(master)
        #apply(klass.__init__,(self,f),tkconfig)
        

    ########################################################################
    ##    GUI Setup    #####################################################
    ########################################################################

    def _gui_setup(self,iconmap,fontmap,**tkconfig):
        f = self._frame
        vsb = self._vsb = Scrollbar(f,orient="vertical")
        hsb = self._hsb = Scrollbar(f,orient="horizontal")
        vsb.configure(command=self.yview)
        hsb.configure(command=self.xview)
        self.configure(yscrollcommand=vsb.set)
        self.configure(xscrollcommand=hsb.set)
        self._grid(row=0, column=0, sticky="NSEW")
        vsb.grid(row=0, column=1, sticky="NS")
        hsb.grid(row=1, column=0, sticky="EW")
        f.grid_rowconfigure(0,weight=1)
        f.grid_columnconfigure(0,weight=1)

        if fontmap:
            self.fonts = self._mkfonts(fontmap)
        else:
            self.fonts = self._mkfonts()
        if iconmap:
            self.icons = self._mkicons(iconmap)
        elif iconmap is None:
            self.icons = {}
        else:
            self.icons = self._mkicons()
        self.selected = None

        # TEMPORARY
        self.normal_fg = NORMAL_FG
        self.normal_bg = NORMAL_BG
        self.active_fg = ACTIVE_FG
        self.selected_fg = SELECTED_FG
        self.selected_bg = SELECTED_BG
        self.sel_act_fg = SEL_ACT_FG


    def _mkfonts(self, fontmap=None):
        fontmap = fontmap or FONTS
        fonts = {}
        families = tkFont.families()
        for key, desc in fontmap.items():
            fs = desc.get('family')
            
            for f in fs:
                if f in families:
                    desc['family'] = f
                    break
                break
            else:
                del desc['family']
            fonts[key] = apply(tkFont.Font,(),desc)
            
        return fonts

    def _mkicons(self, iconmap=None):
        iconmap = iconmap or {'type': 'bitmap',
                              'all': ('node','nodeplus',
                                      'nodeminus')}
        all_icons = {}
        path = iconmap.get('path')
        type = iconmap.get('type')
        try: del iconmap['path']
        except: pass
        try: del iconmap['type']
        except: pass
        if path is not None:
            for key, files in iconmap.items():
                icons = []
                for f in files:
                    f = os.path.join(path, f)
                    if not os.path.isfile(f):
                        warn("Icon file '%s' not found. Using built-in icons." % f)
                        all_icons = {}
                        break
                    if type == 'bitmap':
                        i = BitmapImage(file=f)
                    elif type == 'photo':
                        i = PhotoImage(file=f)
                    else:
                        raise ValueError, "Unknown icon type '%s'."
                    icons.append(i)
                all_icons[key] = icons
        if not all_icons:
            from treewidgets.icons import photo_data, bitmap_data
            for key, names in iconmap.items():
                icons = []
                for n in names:
                    if type == 'bitmap':
                        i = BitmapImage(data=bitmap_data[n])
                    elif type == 'photo':
                        i = PhotoImage(data=photo_data[n])
                    else:
                        raise ValueError, "Unknown icon type '%s'."
                    icons.append(i)
                all_icons[key] = icons
        return all_icons
    

    ########################################################################
    ##   Event handlers    #################################################
    ########################################################################

    def _onUp(self, event=None):
        current = self.getNodeByID(self.selected)
        self.goPrevious(current)

    def _onDown(self, event=None):
        current = self.getNodeByID(self.selected)
        self.goNext(current)

    def _onSpace(self, event=None):
        current = self.getNodeByID(self.selected)
        self.toggleNode(current)

    def _onReturn(self, event=None):
        current = self.getNodeByID(self.selected)
        self.showContentFunc(current)

    def _onEscape(self, event=None):
        self.deselectNode(self.selected)


    ########################################################################
    ##    Debugging    #####################################################
    ########################################################################

    def logNodeStates(self, tag):
        """
        Logs a representation of all nodes in the tree for debugging.

        Arguments:
        tag     -- an arbitrary string that can be used to associate the
                   log entry with a known event or state
        """
        if not self.log:
            self.log = open('ns.log','w')
        log = self.log
        width = 72
        taglen = len(tag)
        log.write("%s %s\n\n" % (tag, '-' * (width - (taglen + 1))))
        for n in self.all_nodes:
            log.write("%s\n" % n._dump())
        log.write("\n%s\n\n\n" % ('-' * width))
            

    ########################################################################
    ##    Tkinter geometry manager overrides    ############################
    ########################################################################

    def pack(self, *args, **kw):
        """Override the Tkinter pack() method."""
        apply(self._frame.pack, args, kw)
    def pack_forget(self):
        """Override the Tkinter pack_forget() method."""
        self._frame.pack_forget()

    def grid(self, *args, **kw):
        """Override the Tkinter grid() method."""
        apply(self._frame.grid, args, kw)
    def grid_forget(self):
        """Override the Tkinter grid_forget() method."""
        self._frame.grid_forget()

    def place(self, *args, **kw):
        """Override the Tkinter place() method."""
        apply(self._frame.place, args, kw)
    def place_forget(self):
        """Override the Tkinter place_forget() method."""
        self._frame.place_forget()


    ########################################################################
    ##    Data structure information    ####################################
    ########################################################################

    def generateNodeID(self, datanode):
        """
        Generate a unique string (within the current tree) for a node ID.

        Arguments:
        datanode      -- any node from the tree data structure

        This is the default means of generating node ID's. In an autobuilt
        tree, it will be invoked automatically when needed--generally, any
        case where the source data lacks "built-in" IDs, and you have not
        provided a function for obtaining IDs.

        Common cases of objects with built-in IDs are XML elements with ID
        attributes, and files in a file system. In the latter case, the full
        path is the file's ID.

        If you have defined an application object, and it has a
        generateNodeID() method, this method will delegate to it.

        """
        if hasattr(self.app,'generateNodeID'):
            id = self.app.generateNodeID(datanode)
        else:
            self._last_autoid = self._last_autoid + 1
            id = 'n%d' % self._last_autoid
        return id

    def getNodeByID(self, node_id):
        """Return the node having a given ID."""
        nodelist = filter(lambda n, id=node_id: n.id == id, self.all_nodes)
        if len(nodelist) > 1:
            raise RuntimeError, "Apparently two or more nodes have the \
                                 ID '%s'. That shouldn't happen." % node_id
        elif len(nodelist) == 1:
            result = nodelist[0]
        else:
            warn("TreeWidget.getNodeByID() failed to find a node with \
                  ID '%s'. This may indicate a programming error." % node_id)
            result = None
        return result

    def nodesPreceding(self, node):
        """Return the list of all nodes preceding a given node in display order."""
        idx = self.all_nodes.index(node)
        return self.all_nodes[:idx]

    def nodesFollowing(self, node):
        """Return the list of all nodes following a given node in display order."""
        idx = self.all_nodes.index(node)
        return self.all_nodes[idx+1:]
    

    ########################################################################
    ##    Tree manipulation    #############################################
    ########################################################################

    def showTree(self, data, datatype, expand_limit=None,
                 node_funcs={}, props=0, state=0):
        """
        Build and display a tree of TreeNode objects.

        Arguments:
        data          -- any hierarchical data structure
        datatype      -- an integer representing an appropriate data type for
                         the 'data' argument. Should be one of the constants
                         DT_TWSTRUCT, DT_XMLDOM, DT_FILESYSTEM, and DT_CUSTOM.

        Keyword arguments:
        expand_limit  -- the number of levels to expand the tree display.
                         A value of 0 will cause only the root node to be
                         displayed; -1 means no limit--be careful with this!
                         If you try to show a filesystem tree starting at the 
                         root directory with expand_limit=-1, the widget will 
                         try to display *every file in your filesystem*. That is
                         probably not what you want. (default: None -- if you
                         don't pass a value, the built-in defaults of the 
                         various node classes take precedence.)
        props         -- property flags for the root node* (default: None)
        state         -- state flags for the root node*    (default: None)
        node_funcs    -- a dictionary of functions used to determine node
                         names, types, children, and other characteristics
                         --needed only for CustomTreeNode instances (default: {})

        * For more infomation about state and property flags, see constants.py

        AUTOBUILT TREES:
        If you include NP_AUTOBUILD in the property flags ('props' argument), 
        the entire tree will be constructed and displayed with no further
        effort on your part. If the datatype is DT_CUSTOM, the 'node_funcs'
        argument comes into play. See CustomTreeNode.__init__ for more
        information on 'node_funcs'.

        """
        treeargs = (self,None,data,expand_limit,
                    props, state, node_funcs)
        if datatype == DT_XMLDOM:
            apply(DOMTreeNode,treeargs)
        elif datatype == DT_FILESYSTEM:
            apply(FSTreeNode,treeargs)
        elif datatype == DT_TWSTRUCT:
            apply(TWTreeNode,treeargs)
        elif datatype == DT_CUSTOM:
            apply(CustomTreeNode,treeargs)
        else:
            raise ValueError, "TreeWidget.showTree requires a datatype flag."
        self.redisplay()

    def redisplay(self):
        """Refresh the tree display after showing, hiding, or moving nodes."""
        self.hideNodes()
        self.hideNodes4Shift()
        self.showNodes()


    def addNode(self, node):
        self.all_nodes.append(node)

    def removeNode(self, node):
        self.all_nodes.remove(node)

    def insertBefore(self, refnode, newnode):
        idx = self.all_nodes.index(refnode)
        self.all_nodes.insert(idx,newnode)

    def insertAfter(self, refnode, newnode):
        idx = self.all_nodes.index(refnode)
        self.all_nodes.insert(idx+1,newnode)
        
    def scheduleShiftFollowing(self, node):
        nodes2shift = filter(lambda n: n.state & NS_VISIBLE,
                             self.nodesFollowing(node))
        for n in nodes2shift:
            n.state = n.state | NS_PENDING_SHIFT
        
    def hideNodes(self):
        nodes = filter(lambda n: (n.state & NS_VISIBLE and 
                                  n.state & NS_PENDING_HIDE),
                       self.all_nodes)
        for n in nodes:
            self.hideNode(n)

    def hideNodes4Shift(self):
        nodes = filter(lambda n: (n.state & NS_VISIBLE and
                                  n.state & NS_PENDING_SHIFT),
                       self.all_nodes)
        for n in nodes:
            self.hideNode(n)
            n.state = n.state | NS_PENDING_SHOW

    def showNodes(self):
        nodes = filter(lambda n: n.state & NS_PENDING_SHOW,
                       self.all_nodes)
        if nodes:
            start = len(filter(lambda n: n.state & NS_VISIBLE,
                               self.nodesPreceding(nodes[0])))
            for i in range(len(nodes)):
                self.showNode(nodes[i],start+i)
        
    def showNode(self, node, row):
        if self._show_node(node, row):
            node.state = ((node.state|NS_PENDING_SHOW) ^ NS_PENDING_SHOW) | NS_VISIBLE

    def hideNode(self, node):
        if self._hide_node(node):
            #node.state = (node.state ^ (NS_PENDING_HIDE|NS_PENDING_SHIFT|NS_VISIBLE))
            node.state = (node.state|NS_PENDING_HIDE|NS_PENDING_SHIFT|NS_VISIBLE) ^ (NS_PENDING_HIDE|NS_PENDING_SHIFT|NS_VISIBLE)

    def toggleNode(self, node):
        self.showContentFunc(node)#changed 4/21


    ########################################################################
    ##    Navigation    ####################################################
    ########################################################################

    def goNext(self, node):
        ##print "node: %s" % node.id
        try:
            vis = filter(lambda n: n.state & NS_VISIBLE, self.all_nodes)
            if node is vis[-1]:
                next = vis[0]
            else:
                next_idx = vis.index(node) + 1
                next = vis[next_idx]
        ##print "next: %s" % next.id
            self.selectNode(next.id)
        except IndexError:
            exit

    def goPrevious(self, node):
        ##print "node: %s" % node.id
        try:
            vis = filter(lambda n: n.state & NS_VISIBLE, self.all_nodes)
            if node is vis[0]:
                prev = vis[-1]
            else:
                prev_idx = vis.index(node) - 1 
                prev = vis[prev_idx]
            ##print "prev: %s" % prev.id
            self.selectNode(prev.id)
        except IndexError:
            exit

