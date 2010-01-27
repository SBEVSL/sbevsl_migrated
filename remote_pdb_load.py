# Copyright Notice
# ================
# 
# The PyMOL Plugin source code in this file is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
# 
# ----------------------------------------------------------------------
# This PyMOL Plugin is Copyright (C) 2004 by Charles Moad <cmoad@indiana.edu>
# 
#                        All Rights Reserved
# 
# Permission to use, copy, modify, distribute, and distribute modified
# versions of this software and its documentation for any purpose and
# without fee is hereby granted, provided that the above copyright
# notice appear in all copies and that both the copyright notice and
# this permission notice appear in supporting documentation, and that
# the name(s) of the author(s) not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
# 
# THE AUTHOR(S) DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.  IN
# NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------
 
import tkSimpleDialog
import tkMessageBox
from pymol import cmd
import sys, urllib2, zlib
 
def __init__(self):
   self.menuBar.addmenuitem('Plugin', 'command',
                            'PDB Loader Service',
                            label = 'PDB Loader Service',
                            command = lambda s=self : fetchPDBDialog(s))
 
def remote(pdbCode):
   pdbCode = pdbCode.upper()
   try:
      pdbFile = urllib2.urlopen('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                                pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                                pdbCode + '&compression=gz')
      cmd.read_pdbstr(zlib.decompress(pdbFile.read()[22:], -zlib.MAX_WBITS), pdbCode)
   except:
      print "Unexpected error:", sys.exc_info()[0]
      tkMessageBox.showerror('Invalid Code',
                             'You entered an invalid pdb code:' + pdbCode)
 
def fetchPDBDialog(app):
   pdbCode = tkSimpleDialog.askstring('PDB Loader Service',
                                      'Please enter a 4-digit pdb code:',
                                      parent=app.root)
   if pdbCode:
      remote(pdbCode)
 
cmd.extend('remote', remote)