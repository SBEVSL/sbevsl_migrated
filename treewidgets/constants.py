# DT: Data types
DT_NONE = 0
DT_TWSTRUCT = 1    #A native data structure. See twstruct.txt for details.
DT_XMLDOM = 2      #A normal XML DOM instance.
DT_FILESYSTEM = 4  #A file system (AKA directory tree).
DT_CUSTOM = 8      #Any other data structure.
DT_ALL = (DT_TWSTRUCT|DT_XMLDOM|DT_FILESYSTEM|DT_CUSTOM)

# NP: Node properties
NP_NONE = 1           #For explicitly disabling all properties.
NP_ROOT = 2           #Indicates a root node.
NP_ALLOW_CHILDREN = 4 #Indicates that a node can have children.
NP_AUTOBUILD = 8  #This node and all descendants will be automatically constructed.
NP_ABSTRACT = 16  #This node is an invisible container, and will not be displayed.
NP_ALL = (NP_NONE|NP_ROOT|NP_ALLOW_CHILDREN|NP_AUTOBUILD|NP_ABSTRACT)

# NS: Node state
NS_NONE = 1             #For explicitly disabling all state flags.
NS_VISIBLE = 2          #The node is currently visible.
NS_PENDING_SHOW = 4     #The node is to be shown in an upcoming redisplay() call.
NS_PENDING_HIDE = 8     #The node is to be hidden in an upcoming redisplay() call.
NS_PENDING_SHIFT = 16   #The node is to be moved in an upcoming redisplay() call.
NS_EXPANDED = 32        #The node is currently expanded.
NS_HAS_CHILDREN = 64    #The node has children.
NS_LOCKED = 128         #The node is locked: no changes are permitted.
NS_ALL = (NS_NONE|NS_VISIBLE|NS_PENDING_SHOW|NS_PENDING_HIDE|NS_PENDING_SHIFT|NS_EXPANDED|NS_HAS_CHILDREN|NS_LOCKED)

# DE: Debugging
DE_LOG_NODE_STATES = 1

# ERR: Error handling
# These flags should be considered requests; actual behavior depends on the
# library and application code.
ERR_IGNORE = 1
ERR_WARN = 2
ERR_FAIL = 4

# Miscellaneous
UP = 1
DOWN = 2
TRUE = 1
FALSE = 2   # Non-zero value allows you to say 'if FALSE: ...'
