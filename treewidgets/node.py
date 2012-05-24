#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/node.py,v 1.3 2002/09/18 02:11:20 matt Exp $

"""

node.py
-------

Provides TreeNode class, a base class for the nodes in tree widgets.
This is an abstract class. To create instances, use either TextTreeNode
or CanvasTreeNode, depending on which type of TreeWidget you use.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

from constants import *
from util import warn
from xml.dom import Node
import sys, string, os

# These constants will be replaced by a configuration module as
# the code matures.
DEFAULT_PROPS = NP_ALLOW_CHILDREN|NP_AUTOBUILD
DEFAULT_STATE = NS_PENDING_SHOW|NS_EXPANDED
DEFAULT_REFUSALS = {'default': ERR_WARN}
#DEBUG = DE_LOG_NODE_STATES
DEBUG = 0

class TreeNode:

    """
    This is the basic unit of the tree data structure.

    TreeNode is a base class for several more specific node types; since
    it lacks a few essential attributes, you should always use one of the
    subclasses in your application. In any case, you will normally not 
    need to directly create any nodes: if you invoke TreeWidget.showTree()
    with the appropriate arguments, an entire tree of nodes will be created
    automatically.

    """

    def __init__(self, treewidget, parent, data,
                 expand_limit,props=None,state=None,node_funcs={}):
        """
        Create a TreeNode instance.

        Arguments:
        treewidget   -- a TreeWidget instance
        parent       -- the parent node (use none when creating the root node)
        data         -- the underlying node in the data structure
        expand_limit -- number of levels to expand the node's subtree

        Keyword arguments:
        props        -- property flags for the node* (default: None)
        state        -- state flags for the node*    (default: None)
        node_funcs   -- a dictionary of functions used to determine the node's
                        name, type, children, and other characteristics
                        --used only in CustomTreeNode instances (default: {})

        * For more infomation about state and property flags, see constants.py

        """

        self.treewidget = treewidget
        self.app = self.treewidget.app
        self.parent = parent

        if props is None: props = DEFAULT_PROPS
        if state is None: state = DEFAULT_STATE
        if not parent:
            props = props | NP_ROOT
        if props & NP_ROOT and props ^ NP_ABSTRACT:
            state = state | NS_PENDING_SHOW
        if not expand_limit:
            state = (state | NS_EXPANDED) ^ NS_EXPANDED
        self.properties = props
        self.state = state
        self.data = data

        if node_funcs and not parent and hasattr(self,'_assimilate_node_funcs'):
            self._assimilate_node_funcs(node_funcs)

        self.type = ""
        self.name = ""
        self.content = ""
        self.attrs = {}
        self.icons = []

        self.children = []
        self._ancestors = []
        self._depth = 0
        self._moved = 1

        self._set_id(data)

        if props & NP_AUTOBUILD:
            self._autobuild(data,expand_limit)


    def configure(self,init=0,node_type=None,**kw):

        """
        Set important attributes of the node object.

        Keyword arguments:
        init        -- 1 for initial configuration, 0 for reconfiguration
                       (default: 0)
        node_type   -- an application-specific type name for the node
                       (default: None -- but *must* be specified on initial
                       configuration)
        name        -- a human-readable name for the node
        properties  -- property flags (see 'constants.py')
        state       -- state flag (see 'constants.py')
        content     -- textual content of the node (roughly equivalent to
                       PCDATA element content in XML)
        attributes  -- a dictionary of arbitrary, application-specific
                       attributes
                       
        This method is normally called automatically by the autobuild process.

        """
        if init:
            assert node_type is not None, "ERROR: node_type must be specified \
                                      on initial configuration."
        self.type = node_type or self.type
        self.name = kw.get('name') or self.name or node_type
        self.properties = kw.get('properties') or self.properties
        self.state = kw.get('state') or self.state
        self.content = kw.get('content') or self.content
        self.attrs = kw.get('attributes') or self.attrs

    def _set_bindings(self):    
        tw = self.treewidget
        id = self.id
        tw.tag_bind(id,'<ButtonRelease-1>',self._onClick1)
        tw.tag_bind(id,'<ButtonRelease-2>',self._onClick2)
        tw.tag_bind(id,'<ButtonRelease-3>',self._onClick3)
        tw.tag_bind(id,'<Double-Button>',self._onDoubleClick)
        tw.tag_bind(id,'<Enter>',self._onEnter)
        tw.tag_bind(id,'<Leave>',self._onLeave)


    ########################################################################
    ##     Event handlers      #############################################
    ########################################################################

    def _onClick1(self, event):
        self.treewidget.selectNode(self.id)

    def _onClick2(self, event):
        self.treewidget.selectNode(self.id)

    def _onClick3(self, event):
        self.treewidget.selectNode(self.id)

    def _onDoubleClick(self, event):
        if DEBUG & DE_LOG_NODE_STATES:
            self.treewidget.logNodeStates('%s: _onDoubleClick: BEFORE' % self.id)
        self.treewidget.toggleNode(self)
        self.showContent()
        if DEBUG & DE_LOG_NODE_STATES:
            self.treewidget.logNodeStates('%s: _onDoubleClick: AFTER' % self.id)

    def _onEnter(self, event):
        ## This is the *mouse* entering the node. For the 'Enter' key,
        ## see TreeWidget._onReturn().
        self.glimpse()
        self.treewidget.activateNode(self.id)

    def _onLeave(self, event):
        self.unglimpse()
        self.treewidget.deactivateNode(self.id)

    def _doNothing(self, event=None):
        print "Doing nothing."


    ########################################################################
    ##    Debugging methods    #############################################
    ########################################################################

    def _dump(self):
        return "%s: props = %s ; state = %s" % (self.id, self._show_props(),
                                                self._show_state())
    
    def _show_props(self):
        prop_names = ("NP_NONE", "NP_ROOT", "NP_ALLOW_CHILDREN",
                      "NP_AUTOBUILD", "NP_ABSTRACT")
        prop_names = filter(lambda name, p=self.properties: p & eval(name),
                            prop_names)
        return string.join(prop_names,'|')
        
    def _show_state(self):
        state_names = ("NS_NONE", "NS_VISIBLE", "NS_PENDING_SHOW",
                       "NS_PENDING_HIDE", "NS_PENDING_SHIFT", 
                       "NS_EXPANDED", "NS_HAS_CHILDREN", "NS_LOCKED")
        state_names = filter(lambda name, s=self.state: s & eval(name),
                             state_names)
        return string.join(state_names,'|')
        

    ########################################################################
    ##    Informational methods    #########################################
    ########################################################################

    def ancestors(self):
        """Return the list of all this node's ancestors."""
        if self._moved:
            if self.parent:
                self._ancestors = [self.parent] + self.parent.ancestors()
            else:
                self._ancestors = []
            self._moved = 0
        return self._ancestors

    def depth(self):
        """Return the depth of this node in the tree (minus abstract nodes)."""
        ## Careful with this--so far depth() is only used to set the 
        ## indent, but that could change.
        concrete_anc = filter(lambda n: ((n.properties ^ NP_ABSTRACT)
                                         & NP_ABSTRACT),
                              self.ancestors())
        return len(concrete_anc)

    def lastInSubtree(self):
        """Return the last descendant of this node."""
        if self.children:
            return self.children[-1].lastInSubtree()
        else:
            return self

    def showContent(self):
        """Display the node's content using an application-specific callback."""
        self.treewidget.showContentFunc(self)

    def showAtts(self):
        """Display the node's attributes using an application-specific callback."""
        self.treewidget.showAttsFunc(self)

    def glimpse(self):
        """Display a bit of the node's content using an application-specific callback."""
        self.treewidget.glimpseFunc(self)

    def unglimpse(self):
        """End whatever was started by glimpse()."""
        self.treewidget.unGlimpseFunc(self)

    def getName(self):
        return self.name

    ########################################################################
    ##    Tree manipulations    ############################################
    ########################################################################

    def expandAll(self,is_top=1):
        """
        Expand this node and all its descendants.

        Keyword arguments:
        is_top      -- 1 if this is the topmost node involved in the operation,
                       0 otherwise (default: 1)

        """
        if is_top:
            #self.treewidget.logNodeStates('BEFORE scheduleShift()')
            self.treewidget.scheduleShiftFollowing(self.lastInSubtree())
            #self.treewidget.logNodeStates('AFTER scheduleShift()')
        else:
            self.state = self.state | NS_PENDING_SHOW
        for ch in self.children:
            ch.expandAll(0)
        self.state = self.state | NS_EXPANDED
        if is_top:
            #self.treewidget.logNodeStates('BEFORE redisplay()')
            self.treewidget.redisplay()
            #self.treewidget.logNodeStates('AFTER redisplay()')

    def expandShallow(self, is_top=1):
        """
        Expand this node only -- that is, display its children, then stop.

        Keyword arguments:
        is_top      -- 1 if this is the topmost node involved in the operation,
                       0 otherwise (default: 1)

        """
        if is_top:
            last = None
            for ch in self.children:
                ch.expandShallow(0)
                last = ch
            if last:
                self.treewidget.scheduleShiftFollowing(last)
            self.state = self.state | NS_EXPANDED
            #self.treewidget.logNodeStates('Expand 1')
            self.treewidget.redisplay()
            #self.treewidget.logNodeStates('Expand 2')
        else:
            self.state = self.state | NS_PENDING_SHOW
            

    def collapseAll(self,is_top=1):
        """
        Collapse this node and all its descendants.

        Keyword arguments:
        is_top      -- 1 if this is the topmost node involved in the operation,
                       0 otherwise (default: 1)

        """
        if is_top:
            #self.treewidget.logNodeStates('BEFORE scheduleShift()')
            self.treewidget.scheduleShiftFollowing(self.lastInSubtree())
            #self.treewidget.logNodeStates('AFTER scheduleShift()')
        elif self.state & NS_VISIBLE:
            self.state = self.state | NS_PENDING_HIDE
        for ch in self.children:
            ch.collapseAll(0)
        self.state = (self.state|NS_EXPANDED) ^ NS_EXPANDED
        if is_top:
            #self.treewidget.logNodeStates('Collapse 1')
            self.treewidget.redisplay()
            #self.treewidget.logNodeStates('Collapse 2')


class TWTreeNode(TreeNode):
    """
    This TreeNode subclass encapsulates a TWStruct data structure.

    See TreeNode documentation for more details.
    
    """
    def _set_id(self,data=None):
        id = data.get('id',
                      self.treewidget.generateNodeID(data))
        self.id = id
        
    def _autobuild(self, data, expand_limit):
        node_type = data['type']
        self.configure(1,node_type,name=data.get('name',node_type))
        if (self.properties ^ NP_ABSTRACT) & NP_ABSTRACT:
            self.treewidget.addNode(self)
        children = data.get('children',[])
        if self.properties & NP_ABSTRACT:
            childprops = (self.properties ^ NP_ABSTRACT) | NP_ROOT
        else:
            childprops = (self.properties|NP_ROOT) ^ NP_ROOT
        if self.state & NS_EXPANDED:
            childstate = self.state
        else:
            childstate = ((self.state | NS_PENDING_SHOW | NS_VISIBLE)
                          ^ (NS_PENDING_SHOW | NS_VISIBLE))
        for ch in children:
            if type(ch) is type(()):
                child_type, child_data = ch 
                if child_type == DT_XMLDOM:
                    treenode = DOMTreeNode(self.treewidget,
                                           self,child_data,
                                           expand_limit-1,
                                           props=childprops,
                                           state=childstate)
                elif child_type == DT_FILESYSTEM: 
                    treenode = FSTreeNode(self.treewidget,
                                          self, child_data,
                                          expand_limit-1,
                                          props=childprops,
                                          state=childstate)
                else:
                    treenode = CustomTreeNode(self.treewidget,
                                              self, child_data,
                                              expand_limit-1,
                                              props=childprops,
                                              state=childstate)
            else:
                treenode = TWTreeNode(self.treewidget,self,
                                    ch, expand_limit-1,
                                    props=childprops,
                                    state=childstate)
            self.children.append(treenode)
        if children:
            self.state = self.state | NS_HAS_CHILDREN


SHOW_EMPTY_TEXT_NODES = 0

class DOMTreeNode(TreeNode):
    """
    This TreeNode subclass encapsulates an XML DOM object.

    See TreeNode documentation for more details.
    
    """
    
    ATTR = Node.ATTRIBUTE_NODE
    CDATA = Node.CDATA_SECTION_NODE
    COMMENT = Node.COMMENT_NODE
    FRAGMENT = Node.DOCUMENT_FRAGMENT_NODE
    DOCUMENT = Node.DOCUMENT_NODE
    DOCTYPE = Node.DOCUMENT_TYPE_NODE
    ELEMENT = Node.ELEMENT_NODE
    ENTITY = Node.ENTITY_NODE
    ENTITY_REF = Node.ENTITY_REFERENCE_NODE
    NOTATION = Node.NOTATION_NODE
    PI = Node.PROCESSING_INSTRUCTION_NODE
    TEXT = Node.TEXT_NODE

    named_types = (ELEMENT, ATTR, ENTITY, ENTITY_REF, PI,
                   DOCTYPE,NOTATION)
    name_lookup = {CDATA: 'CData Section', COMMENT: 'Comment',
                   FRAGMENT: 'Document Fragment',
                   DOCUMENT: 'Document', TEXT: 'Text'}
    content_types = (TEXT, ATTR, CDATA, COMMENT, PI)
    default_visible_types = (ELEMENT, TEXT, CDATA,
                             DOCTYPE, COMMENT)

    def __init__(self, treewidget, parent, *args, **kw):
        """
        Create a DOMTreeNode instance.

        Keyword argument:
        id_qname     -- the QName of the ID-type attribute in this DOM
                        (default: 'id').

        All other arguments are identical to those of the base class
        constructor. See class TreeNode for more info.

        Most of the initialization is done by TreeNode.__init__.
        In addition to accepting the above variable, this constructor sets 
        the instance variable 'root', which is peculiar to DOMTreeNode.
        """
        if parent:
            self.root = parent.root
        else:
            self.root = self
        self.id_qname = kw.get('id_qname','id')
        apply(TreeNode.__init__,(self,treewidget,parent) + args, kw)

    def _set_id(self,data=None):
        qname = self.root.id_qname 
        qnparts = string.split(qname,':')
        if len(qnparts) == 2:
            ns, attname = qname
        elif len(qnparts) ==1:
            ns = None
            attname = qname
        else:
            raise ValueError("Invalid QName: '%s' has more than one colon." % qname)
        id = None
        if data.nodeType == self.ELEMENT:
            id = data.getAttributeNS(ns, attname)
        if not id:
            id = self.treewidget.generateNodeID(data)
        self.id = id

    def _autobuild(self, data, expand_limit):
        node_type = data.nodeType
        name = data.nodeName
        if not name:
            name = self.name_lookup(node_type)
        self.configure(1,node_type,name=name)
        if (self.properties ^ NP_ABSTRACT) & NP_ABSTRACT:
            self.treewidget.addNode(self)
        if self.properties & NP_ABSTRACT:
            childprops = (self.properties ^ NP_ABSTRACT) | NP_ROOT
        else:
            childprops = (self.properties|NP_ROOT) ^ NP_ROOT
        if self.state & NS_EXPANDED:
            childstate = self.state
        else:
            childstate = ((self.state | NS_PENDING_SHOW | NS_VISIBLE)
                          ^ (NS_PENDING_SHOW | NS_VISIBLE))
        children = data.childNodes
        if not SHOW_EMPTY_TEXT_NODES:
            children = filter(lambda n,ne=self._notEmpty,tn=self.TEXT: ne(n), 
                              children)
        for ch in children:
            treenode = DOMTreeNode(self.treewidget,self,ch,
                                   expand_limit-1,
                                   props=childprops,
                                   state=childstate)
            self.children.append(treenode)
        if children:
            self.state = self.state | NS_HAS_CHILDREN

    def _notEmpty(self, n):
        return ((n.nodeType == self.TEXT and n.nodeValue and
                 string.strip(n.nodeValue)) or
                 n.nodeType != self.TEXT)

class FSTreeNode(TreeNode):
    """
    This TreeNode subclass encapsulates a file system (AKA directory tree).

    See TreeNode documentation for more details.
    
    """

    def _set_id(self,data=None):
        self.id = data
        
    def _autobuild(self, data, expand_limit):
        children = []
        if os.path.islink(data):
            node_type = 'symlink'
        elif os.path.isdir(data):
            node_type = 'directory'
            try:
                children = os.listdir(data)
                children = map(lambda f,d=data: os.path.join(d,f),
                               children)
            except OSError:
                warn("Unable to list directory '%s'" % data)
                children = []
        else:
            node_type = 'file'
        self.configure(1,node_type,name = os.path.basename(data))
        if (self.properties ^ NP_ABSTRACT) & NP_ABSTRACT:
            self.treewidget.addNode(self)
        if self.properties & NP_ABSTRACT:
            childprops = (self.properties ^ NP_ABSTRACT) | NP_ROOT
        else:
            childprops = (self.properties|NP_ROOT) ^ NP_ROOT
        if self.state & NS_EXPANDED:
            childstate = self.state
        else:
            childstate = ((self.state | NS_PENDING_SHOW | NS_VISIBLE)
                          ^ (NS_PENDING_SHOW | NS_VISIBLE))
        for ch in children:
            treenode = FSTreeNode(self.treewidget,self,ch,
                                  expand_limit-1,
                                  props=childprops,
                                  state=childstate)
            self.children.append(treenode)
        if children:
            self.state = self.state | NS_HAS_CHILDREN
    

class CustomTreeNode(TreeNode):
    """
    This TreeNode subclass encapsulates any hierarchical data structure.

    See TreeNode documentation for more details.
    
    """

    def __init__(self, treewidget, parent, data, expand_limit,
                 props=NP_AUTOBUILD,state=0,node_funcs={}):
        """
        Create a CustomTreeNode instance.

        All arguments are identical to those of the base class constructor;
        however, unlike the other TreeNode classes, CustomTreeNode uses the
        value of 'node_funcs', which is a dictionary of functions conforming
        to the following specification ([R] = required):

        Key               Arguments           Return type       Notes
        ---               ---------           -----------       -----
        'type' [R]        node                string            [1]
        'id'              node                string            
        'get_name'        node                string
        'set_name'        node, name          None
        'get_children'    node                list of nodes
        'add_child'       node, child         None              [2]
        'del_child'       node, child_id      None              [3]
        'get_props'       node                integer           [4]
        'get_state'       node                integer           [4]
        'set_state'       node, state         None              [4]
        'get_content'     node                any
        'set_content'     node, content       None
        'get_attrs'       node                dictionary
        'set_attrs'       node, attrs         None
        'get_attr'        node, attname       any
        'set_attr'        node, name, value   None
        'get_icon'        node                Image
        'set_icon'        node, icon          None

        [1] The value returned by the 'type' function should be an application-
            specific node type identifier (e.g. for an XML document, the node
            type would typically be the element name).
        [2] The value of the 'child' argument should be a node.
        [3] The value of the 'child_id' argument should be a string.
        [4] Property and state values should always be integers. For best
            results, use the constants defined in 'constants.py'.

        If there are node functions you do not wish to enable, simply omit them
        from the 'node_funcs' dictionary, and the CustomTreeNode instance will
        disable them in an appropriate way. If you attempt to override the 
        built-in behavior by, e.g. passing a value of None for some function,
        errors will probably occur.

        """
        if parent:
            self.node_funcs = parent.node_funcs
        else:
            self.node_funcs = {}
        TreeNode.__init__(self,treewidget,parent,data,
                          expand_limit,props,state,node_funcs)
        #else:
        #    self._assimilate_node_funcs(node_funcs)

    def _set_id(self,data=None):
        if data:
            id = self.node_funcs['get_id'](data)
        if not id:
            id = self.treewidget.generateNodeID(data)
        self.id = id
        
    def _autobuild(self, data, expand_limit):
        self._set_id(data)
        funcs = self.node_funcs
        node_type = funcs['get_type'](data)
        self.configure(1,node_type,name=funcs['get_name'](data))
        if (self.properties ^ NP_ABSTRACT) & NP_ABSTRACT:
            self.treewidget.addNode(self)
        if self.properties & NP_ABSTRACT:
            childprops = (self.properties ^ NP_ABSTRACT) | NP_ROOT
        else:
            childprops = (self.properties|NP_ROOT) ^ NP_ROOT
        if self.state & NS_EXPANDED:
            childstate = self.state
        else:
            childstate = ((self.state | NS_PENDING_SHOW | NS_VISIBLE)
                          ^ (NS_PENDING_SHOW | NS_VISIBLE))
        children = funcs['get_children'](data)
        if children:
            for ch in children:
                treenode = CustomTreeNode(self.treewidget,self,
                                          ch,expand_limit-1,
                                          props=childprops,
                                          state=childstate,
                                          node_funcs={})
                self.children.append(treenode)
            self.state = self.state | NS_HAS_CHILDREN

    def _assimilate_node_funcs(self, node_funcs):
        self.node_funcs['get_type'] = node_funcs['type']
        idfunc = node_funcs.get('id',
                                lambda: self_refuse('get_id'))
        self.node_funcs['get_id'] = idfunc
        self.node_funcs['get_name'] = node_funcs.get('get_name',idfunc)
        snf = node_funcs.get('set_name',
                             lambda name, r=self._refuse: r('set_name'))
        self.node_funcs['set_name'] = snf
        gkf = node_funcs.get('get_children',
                             lambda r=self._refuse: r('get_children'))
        self.node_funcs['get_children'] = gkf
        akf = node_funcs.get('add_child',
                             lambda child,r=self._refuse: r('add_child'))
        self.node_funcs['add_child'] = akf
        dkf = node_funcs.get('del_child',
                             lambda child_id,r=self._refuse: r('del_child'))
        self.node_funcs['del_child'] = dkf
        gpf = node_funcs.get('get_props',
                             lambda r=self._refuse: r('get_props'))
        self.node_funcs['get_props'] = gpf
        gsf = node_funcs.get('get_state',
                             lambda r=self._refuse: r('get_state'))
        self.node_funcs['get_state'] = gsf
        ssf = node_funcs.get('set_state',
                             lambda state, r=self._refuse: r('set_state'))
        self.node_funcs['set_state'] = ssf
        gcf = node_funcs.get('get_content',
                             lambda r=self._refuse: r('get_content'))
        self.node_funcs['get_content'] = gcf
        scf = node_funcs.get('set_content',
                             lambda content, r=self._refuse: r('set_content'))
        self.node_funcs['set_content'] = scf
        gasf = node_funcs.get('get_attrs',
                              lambda r=self._refuse: r('get_attrs'))
        self.node_funcs['get_attrs'] = gasf 
        sasf = node_funcs.get('set_attrs',
                              lambda attrs,r=self._refuse: r('set_attrs'))
        self.node_funcs['set_attrs'] = sasf 
        gaf = node_funcs.get('get_attr',
                              lambda attr,r=self._refuse: r('get_attr'))
        self.node_funcs['get_attr'] = gaf 
        saf = node_funcs.get('set_attr',
                              lambda name,value,r=self._refuse: r('set_attr'))
        self.node_funcs['set_attr'] = saf 
        gicf = node_funcs.get('get_icon',
                              lambda r=self._refuse: r('get_icon'))
        self.node_funcs['get_icon'] = gicf
        sif = node_funcs.get('set_icon',
                             lambda icon,r=self._refuse: r('set_icon'))
        self.node_funcs['set_icon'] = sif

    def _refuse(self, action):
        if hasattr(self.app,'refusals'):
            refusals = self.app.refusals
        else:
            refusals = DEFAULT_REFUSALS
        ref = refusals.get('all',refusals.get(action,refusals.get('default')))
        assert ref is not None, "Internal error: no 'refusals' dictionary available for TreeNode._refuse()!"
        if ref & ERR_FAIL:
            raise ValueError, "This application does not support the action '%s'." % action
        elif ref & ERR_WARN:
            warn("No handler for requested action: '%s'" % action)
            return None
        elif ref & ERR_IGNORE:
            return None
            
