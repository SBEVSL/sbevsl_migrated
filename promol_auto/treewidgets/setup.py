#!/usr/bin/env python

# $Header: /home/cvs/treewidgets/setup.py,v 1.3 2002/08/28 22:31:52 matt Exp $

"""

setup.py
--------

Distutils installation script for Treewidgets.

Copyright (c) 2002  Matthew C. Gushee <mgushee@havenrock.com>

This is free software, released under the terms of the BSD License.
See the file LICENSE for details.

"""

from distutils.core import setup

setup(name="treewidgets",
      version="1.0a1",
      description="A Tkinter tree widget library",
      author="Matt Gushee",
      author_email="mgushee@havenrock.com",
      url="http://www.havenrock.com/software/treewidgets/",
      packages=["treewidgets"],
      package_dir={"treewidgets":"."},
      data_files=[('doc/treewidgets-1.0a1',
                   ['BUGS','ChangeLog','INSTALL','LICENSE',
                    'README','TODO','doc/twstruct.txt']),
                  ('doc/treewidgets-1.0a1/apidocs',
                   ['doc/apidocs/treewidgets.__init__.html',
                    'doc/apidocs/treewidgets.canvastree.html',
                    'doc/apidocs/treewidgets.constants.html',
                    'doc/apidocs/treewidgets.html',
                    'doc/apidocs/treewidgets.icons.html',
                    'doc/apidocs/treewidgets.node.html',
                    'doc/apidocs/treewidgets.texttree.html',
                    'doc/apidocs/treewidgets.tttest.html',
                    'doc/apidocs/treewidgets.util.html',
                    'doc/apidocs/treewidgets.widget.html']),
                  ('doc/treewidgets-1.0a1/demos',
                   ['doc/demos/addresses.py',
                    'doc/demos/customtext.py',
                    'doc/demos/domtext.py',
                    'doc/demos/fstext.py',
                    'doc/demos/twtext.py'])])
