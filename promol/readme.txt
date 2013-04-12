README
ProMOL (C) Copyright 2004-2013
Charlie Westin, Brett Hanson & Paul Craig
GPL, No Warranty

4.2 by Cyprian Corwin and Greg Dodge
Monday, July 25, 2011

Based on Maddy's and Mario Rosa's versions

5.0 RC 2 by the SBEVSL team, see the User's Guide
Thursday, 11 April 2013 -- HJB

Special Thanks to the following for their contributions to ProMOL:
Laura Grell, Chris Parkin, T.J. Esposito, C. Wischmeyer
   
/*************************** GPL NOTICES ******************************
 *                                                                    *
 * This program is free software; you can redistribute it and/or      *
 * modify it under the terms of the GNU General Public License as     *
 * published by the Free Software Foundation; either version 2 of     *
 * the License, or (at your option) any later version.                *
 *                                                                    *
 * This program is distributed in the hope that it will be useful,    *
 * but WITHOUT ANY WARRANTY; without even the implied warranty of     *
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      *
 * GNU General Public License for more details.                       *
 *                                                                    *
 * You should have received a copy of the GNU General Public License  *
 * along with this program; if not, write to the Free Software        *
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA           *
 * 02111-1307  USA                                                    *
 *                                                                    *
 **********************************************************************/

ProMOL is a product of the Structural Biology Extensible Visualization
Language (SBEVSL) project, supported in part by Award Number
R15GM078077 from the National Institute Of General Medical Sciences. 
The content is solely the responsibility of the authors and does not
necessarily represent the official views of the National Institute Of 
General Medical Sciences or the National Institutes of Health.

The purpose of ProMOL is to assist in the visualization of protein structures
in PyMOL, as well as assist in the identification of small catalytic sites, and
the creation of catalytic site motifs.

=========================================================================

ProMOL Installation Instructions

ProMOL is a plugin for PyMOL.  PyMOL is available as an open source program
from

http://sourceforge.net/projects/pymol/

and is incorporated into many Unix releases.  PyMOL is also available in
proprietary versions from

http://www.pymol.org.  See that website for information on PyMOL licensing.

PyMOL is a program that was written by the late Warren DeLano.  PyMOL is a
trademark of Schrodinger, LLC.  ProMOL is a plugin for PyMOL, not a
derivative part of PyMOL, but depends on having a copy of PyMOL in order to
operate.

Therefore, in order to use ProMOL, you first must have a copy of PyMOL
installed.

Download PyMOL from http://pymol.sourceforge.net and install to default
location.

ProMOL can be downloaded in a compressed file format from

http://sourceforge.net/projects/sbevsl/files

You can choose to download either a .tar.gz compressed file
(ProMOL-5.0-r209.tar.gz) or a zip compressed file
(ProMOL-5.0-r209.zip). The way you expand the 
file depends on your operating system.

On Unix or Linux systems, or using MINGW under Windows you may unpack the
tarball with

gunzip < ProMOL-5.0-r209.tar.gz | tar xvf -

Windows and Macintosh systems may have a native application that will expand
your .tar.gz or .zip files; if not you may wish to consider using Stuffit
Expander or WinZip.

If you have not already done so, first install PyMOL. Under Mac OS X 
you may need to rename the MacPymol application to MacPymolX11Hybrid, in
order to get access to plugins.  You will also need to have the X window
system installed.  This is included on your Mac OS install disc, but may
not be installed by default.

To install ProMOL, copy ProMol.py and the folder ProMol into the correct
place in the directory tree used by PyMOL for plugins.  For example, for
PyMOL 1.4.1 under Microsoft Windows:

C:\Program Files\PyMol\modules\pmg_tk\startup\

On other systems you will need to find the portion of the PyMOL installation
tree that contains

modules/pmg_tk/startup

and place ProMol.py and the folder ProMol in the startup folder.
For example in a fink PyMOL installation for python 2.4, 2.5 or 2.6 under
Mac OS X, the ProMol.py file and ProMol folder belongs under

/sw/lib/pymol-py24/modules/pmg_tk/startup or
/sw/lib/pymol-py25/modules/pmg_tk/startup or
/sw/lib/pymol-py26/modules/pmg_tk/startup

However, we believe that this version of ProMOL may use features of the Python
language that were introduced in 2.6, so it may not run with earlier versions.
Furthermore, has only been tested on Python 2.7.x, and will not work with Python 3.

For PyMOL installed from the Ubuntu Software Center (it may be the same
from source), ProMol.py and the ProMol folder can be placed under:

/usr/lib/pymodules/python2.7/pmg_tk/startup

When all files are in place, the ProMOL interface can be run by choosing
ProMOL from the PyMOL plug-in menu.

=========================================================================

WARNING: While running a search with the Motif Finder, PLEASE DO NOT
double-click in the results list of a previous search, or load, modify,
manipulate, or clear any structures or named selections present in PyMOL.
Doing so will likely lead to erroneous results!

Other important notes and tips:

- Motifs generated using the Motif Maker tab are stored the subfolder
UserMotifs in the ProMOL application data directory.  This folder is usually
located in the following places:

Windows: %AppData%/SBEVSL/ProMol/
(On Windows 7, %AppData% may be located at C:\Users\[User Name]\AppData\Roaming)
Mac OS X/Darwin: ~/Library/Application Support/SBEVSL/ProMol
Other platforms, including Ubuntu: ~/.sbevsl/ProMol

- Do not install motifs obtained from any source except SBEVSL or your Motif Maker
tab inside either ProMOL's Motifs folder or your UserMotifs folder.  You have been
warned!

- Motif finder searches tend to run significantly faster if, once the search is
started, the user selects the PyMOL Viewer window and presses Escape to switch
into text mode.  To switch back, simply press Escape again.

- Exporting CSV files via the user interface button for a search with no results
will cause ProMOL to hang.  As a workaround, check the CSV file generated for each
search located in your application data directory (see above).

=========================================================================

Work done in part with support from NIH and Nation Institute of General Medical
Sciences (NIGMS) under Grant number 1R15GM078077-01.

ASBMB Annual Meeting
April 28 -- May 3, 2007
Washington, DC

Using PyMOL's Selection Algebra for Enzyme Catalytic Site Prediction
B. R. Hanson, C. Westin, P. A Craig

<>

American Crystallographic Association Meeting
21 -- 26 July 2007
Salt Lake City, Utah

ProMOL, Simplification and Increased Functionality of PyMOL
B. Hanson, C. Westin, L. Slatest, P. Craig

<>

American Crystallographic Association Meeting
31 May -- 5 June 2008
Knoxville, TN

Homology Exploration with ProMOL
C. Wischmeyer, P. Craig, H. Bernstein
The ProMOL plugin for PyMOL is an intuitive user interface that gives users
access to many of the complex tools that exist within PyMOL, without requiring
that the user learn to program in Python. Among its many tools, ProMOL features
a motif­matching interface that can compare enzyme active sites based on the
relative positions of the catalytic residues. Tools found in ProMOL can be used
to compare any structure with more than 30 known calalytic active site motifs,
which were drawn from the Catalytic Site Atlas
(http://www.ebi.ac.uk/thornton­srv/databases/CSA/). The motif analysis tool can
be fine tuned to narrow or expand the three dimensional search space for active
site alignment. Alignment results for enzyme classes across different taxonomic
categories will be presented and compared, along with suggestions for
implementing more effective alignment strategies with the motif tool in ProMOL.

=========================================================================
[Update by current developers: there are 440 motifs as of July 20, 2011.]
=========================================================================

The previous developers of ProMOL had incorporated a modified version of the
PDB Loader Service plugin into promolglobals.py.  We have removed that code
from ProMOL in favor of launching the existing copy on the user's machine
that is distributed with PyMol, and using PyMOL's built-in functionality.
The following notice was included with older versions of ProMOL, and may no
longer be required, but we have included it for the sake of completeness.
We believe it no longer applies to anything in ProMOL.

# Copyright Notice
# ================
# 
# The PyMOL Plugin source code [below this point] is copyrighted, but you can
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

=========================================================================

Change log:
Revision 149
Modified Monday, July 25, 2011 by Cyprian Corwin and Greg Dodge
Version 4.2.  Many bug fixes, a few enhancements, and code cleanup
based on Maddy's Revision 142.  Major changes from 142 include a new,
larger set of 440 motifs, removal of PERSISTENT database code,
changes to the way PDB structures are fetched and the way
the PDB Loader Service dialog is launched from within ProMOL, simplification of
the way in which aligned matches are rendered and named (when double-clicking
a result in Motif Finder), a fix for the issue preventing the creation of
motifs for active sites containing alanine, and a fix for the hang that
would formerly happen when a motif search returned zero results, among others.
For the full list, please see the file promol-changes.txt.

Revision 119
Modified Tue Dec 7 by vinnyrose
Version 4.1rc2. Minor backwards compatibility fix. Updated readme.

Revision 115
Modified Thu Aug 5 by vinnyrose 
Version 4.1rc1. Added and alignment option in the motif finder. [Turn alignment
on and double click on a motif in the result box to see the alignment of the
template pdb to the test pdb. The color of each may be specified by clicking on
the color boxes adjacent to "template color" and "motif color". These boxes are
only clickable if alignment is clicked on. The alignment box does not have to be
clicked on prior to starting a test, but it does need to be clicked on prior to
double clicking a result if you want the alignment to appear. You cannot align a
PDB with itself.] Many sorts have been changed to be faster and to have
backwards and forwards compatibility. All motifs have been changed to include a
LOCI attribute which includes information on where the residues were located in
the original template pdb. The motif maker has been updated to include the LOCI
attribute. The color functions have been changed to make the custom colors more
optimized and to avoid conflicting colors. global.show_as function added to
compensate for cmd.as being changed to cmd.show_as due to reservation of 'as' in
python 2.6. More reliable and faster finding of chains in global.update
function.

Revision 110
Modified Tue Jul 20 by vinnyrose 
Fetch falls back to non-compressed on zlib error. Thanks button removed.

Revision 109 
Modified Wed Jul 14 by yaya-hjb 

Add actual authors on copyright line.
Add gpl.txt
Needs a readme. -- HJB

Revision 107 
Modified Tue Jul 13 by vinnyrose 

System dependent bug fix.

Revision 105 
Modified Tue Jul 13 by vinnyrose 

ProMol
Changed persistent storage. Changed gui dictionary to a class object. Several 
small bug fixes. Promol will now advise the user to install the 'ProMol' folder
if it was not installed in the startup folder. Bug in random pdb fixed, now it 
actually is random. Version 4.0rc4.
ConSCRIPT
Some small fixes. 2.0rc4.1

Revision 98 
Modified Tue Jul 6 by yaya-hjb 

Raise rc number to 3.2 -- HJB

Revision 94 
Modified Tue Jun 29 by vinnyrose 

ConSCRIPT select function fixed. Many changes made to the structure of the code 
including making the class truly classified. Before all the functions were in 
the init of the class. The handle command now looks at token equality instead 
of command substrings. Parsing colors has been modified to a smaller code base.
Promol: some small bug fixes in the motif maker that occur when unwanted spaces
occur in the input fields, a fixed motif was added. A better way of updating
motif files is needed when this is all distributed. Version changed to 3.6.2.
Version 4.0 candidate 3.2

Revision 93 
Modified Fri Jun 25 by vinnyrose 

Some small bug fixes. Version changed to 3.6.1. Version 4.0 candidate 3.1.

Revision 92 
Modified Tue Jun 22 by vinnyrose 

Some small bug fixes. Updated the motif finder to support batch processing.
Motif maker has the capablity to change the order of the motifs being made.
Several organizational changes such as folder names and locations.
ChimeConverter is now active, and accessible with the 'c' command prefix.
Pmw has been replace by tkinter functions in many places.
Version changed to 3.06. Version 4.0 candidate 3.

Revision 88 
Modified Fri Jun 11 by vinnyrose 

Added all the motifs made so far. Created error reporting on motif loading.
Changed welcome screen. All pdb's entered into motif maker will be lowercased.
4.0 release candidate 2. (3.05)

Revision 87 
Modified Thu Jun 10 by vinnyrose 

Several changes. The motif maker has some bug fixes, as well as the ability to
check against homologs and random pdb's. The motif finder uses a levenshtein
distance calculation and reports the minimum and maximum (min/max) edit
distance found, if the min and max are the same it reports one distance.
It searches into each chain individually and the whole structure. In addition
it searches through every permutation of residues in cases where that is
applicable. Version changed to 3.04. Version 4.0 candidate.

Revision 86 
Modified Mon Mar 22 by vinnyrose 

Residues are capital insensitive in motif maker, multiple ec numbers can be
entered separated by a comma. The motifs are going through the last steps to
transfer them to individual files.

Revision 85 
Modified Sun Mar 21 by vinnyrose 

Some small changes, and preparing the motifs to be separated into individual 
files

Revision 83 
Modified Wed Mar 17 by vinnyrose 

More changes to the motif maker.

Revision 82 
Modified Wed Mar 17 by vinnyrose 

Changes to ConSCRIPT to make it compatible with Linux.

Many changes to ProMol.
Changed motif maker to have it's own tab, and am still working on making it
compatible with motif finder.
Made changes to make it more compatible with linux and need to make more
changes in that area.
Changed the GUI in many areas.
Deleted many motifs that don't seem to have a use right now. 

Revision 81 
Modified Tue Feb 16 by vinnyrose 

Remove reference to batch motif.

Revision 74 
Modified Wed Feb 3 by vinnyrose 

Temporarily commented out some tabs.

Revision 73 
Modified Mon Feb 1 by vinnyrose 

Moved remote_pdb_load into the Promol_dir as well as make a few changes in the
code. Made the motif finder faster.

Revision 65 
Modified Tue Jan 26 by vinnyrose 

Jess templates are done. Motif finder reworked. Random PDB finder is working
again.

Revision 63 
Modified Thu Jan 7 by vinnyrose 

Hooking stuff onto the new organization. Most Motif related functions have been
hooked on.

Revision 62 
Modified Thu Dec 24 by vinnyrose 

Made lots of organizational changes. Stable but with many bugs.

Revision 60 
Modified Tue Dec 15 by vinnyrose 

Made changes to the built-in motifs. No functionality changes, just making
things prettier. Still unstable, latest stable in 57.

Revision 59 
Modified Mon Dec 14 by vinnyrose 

This revision is absolutely positively unstable, DO NOT USE IT!

Removed unnecessary files and folders.

Removed ProMOL_302. If you want the latest stable go to revision 57.

Changed amino acid pictures names so that they are not confusing.

Changes to ProMol.py include:
	separating the code into multiple files
	Optimizing the code
	standardizing the formatting
This is the first commit in several to come that will dramatically change the
code. The functionality in most cases will not be changed.

Much of the indentation is not correct due an attempt to standardize.
Indentations will be fixed in a future revision.

Revision 58 
Modified Mon Dec 14 by vinnyrose 

~/Desktop/commit.rtf

Revision 57 
Modified Thu Jul 9 by vinnyrose 

the make motif function can now handle between 2 and 10 residue motifs and is
much faster. The make motif window can now handle empty rows. Amino acid list
are in alphabetical order. Trimmed white space at the end of lines. Made global
list of amino acids three letter codes. And made global list of alphabetical
letters.

Revision 55 
Modified Fri Jun 12 by vinnyrose 

Revisions made to makemotif fuction:
This revision is able to build a motif for active sites that have repeating
amino acids. The code has been commented so that it can be followed more easily
and the motifs that are built now have a smaller file size. The while loops
were improved and variable names were changed. -MROSA

Revision 40 
Modified Tue Jul 22 by yaya-hjb 

Correct spacing garbled on last upload -- HJB

Revision 39 
Modified Wed Jul 16 by yaya-hjb 

This update allows users to use commands that were once only available
in ProMOL in the command line as well as scripts (as long as
ProMOL itself is open).  See ProMOL_README.txt.
Mod by C. Wischmeyer. -- HJB

Revision 36 
Modified Wed Jun 25 by yaya-hjb 

Mods by Corey Wischmeyer introducing commands for ProMol ops
See the sbevsl wiki on sourceforge for details.

Revision 34 
Added Wed Jun 11 by yaya-hjb 
Copied from: trunk/promol/ProMOL_302.py revision 33
Remove version from name of ProMol.py, update to 303 with
batch motifier.  Mods by Corey Wischmeyer. -- HJB

