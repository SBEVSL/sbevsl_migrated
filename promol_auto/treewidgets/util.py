#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/util.py,v 1.2 2002/08/28 21:14:53 matt Exp $

"""

util.py
-------

Miscellaneous utility functions for TreeWidgets.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License. See
the file LICENSE for details.

"""

import sys

def warn(message):
    sys.stderr.write("WARNING: %s" % message)
    
