README
ConSCRIPT
a Rasmol to Pymol converter
ConSCRIPT (C) Copyright 2007-2010

S. Mottarella, P. Craig, H. Bernstein
GPL, No Warranty

2.0 Release Candidate 3
by Mario Rosa
12 July 2010

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
 
ConSCRIPT is a product of the 

Structural Biology Extensible Visualization Language (SBEVSL)

project, supported in part by supported by Award Number R15GM078077 
from the National Institute Of General Medical Sciences. The content is 
solely the responsibility of the authors and does not necessarily represent 
the official views of the National Institute Of General Medical Sciences 
or the National Institutes of Health.”

The purpose of ConSCRIPT is to allow PyMOL to be used with RasMOL or
SBEVSL scripts and commands.

=========================================================================

ConSCRIPT Installation Instructions

ConSCRIPT is a plugin for PyMOL.  PyMOL is available as an open source
program from

http://sourceforge.net/projects/pymol/

and is incorpoated into many unix releases.  PyMOL is also available
in proprietary versions from

http://www.pymol.org.  See that website for information on PyMOL licensing.

PyMOL is a program that was written by the late Warren DeLano.  PyMOL
is a trademark of Schrodinger, LLC.  ConSCRIPT is a plugin for PyMOL,
not a derivative part of PyMOL, but depends on having a copy of PyMOL
in order to operate.

Therefore, in order to use ConSCRIPT, you first must have a copy of
PyMOL installed.

download PyMOL from http://pymol.sourceforge.net and install to 
default location

download ConSCRIPT.py from

http://downloads.sourceforge.net/sbevsl/ConSCRIPT-2.0rc3.tar.gz

and unpack ConSCRIPT.py from the kit.  On an MS Windows system,
if you do not have a suitable utility to read "tarballs", when
you double click ConSCRIPT-2.0rc3.tar.gz, they system should
suggest a program to download.  If it does not, you may wish to
consider using Stuffit Expander or WinZip.  On unix systems, or
using MINGW under windows you may unpack the tarball with

gunzip < ConSCRIPT-2.0rc3.tar.gz | tar xvf -

If you have not already done so, first install PyMOL.  Then,
the simplest way to install ConSCRIPT is by using the

Plugin->Manage Plugins->Install... menu

to install CONSCRIPT.py

To use that menu item, you need the same administrative rights as
were needed to install PyMOL, itself.  For example, under windows
you may need to be a system administrator, or under unix to have
root access (e.g. via sudo).

ALternatively, you may copy ConSCRIPT.py into the correct place
in the directory tree used by PyMOL for plugins.  For example,
for PyMOL 0.99 under MS windows:

  C:\Program Files\DeLano Scientific\pymol\modules\pmg_tk\startup\

On other systems you will need to find the portion of the pymol i
nstallation tree that contains 

   modules/pmg_tk/startup

and place ConSCRIPT.py in startup.  For example in a fink pymol
istallation for python 2.4, 2.5 or 2.6 under OSX under 

  /sw/lib/pymol-py24/modules/pmg_tk/startup
or
  /sw/lib/pymol-py25/modules/pmg_tk/startup
or
  /sw/lib/pymol-py26/modules/pmg_tk/startup

When all files are in place, the ConScript interface can be run by
choosing ConSCRIPT from the PyMOL plug-in menu.  

=========================================================================

Work done in part with support from NIH and Nation Institute of 
General Medical Sciences (NIGMS) under Grant number 1R15GM078077-01.

Work presented at ASBMB COnference in San Diego, April 2008:

Executing RasMol Scripts in PyMOL
Scott Mottarella1, Corey Wischmeyer1, Brett Hanson3, Charles 
Westin4, Herbert Bernstein< b>5< /b>2. 1Biological Sciences, 
2Chemistry,  Rochester  Institute  of  Technology,  Rochester,  NY, 
3Immunology and Microbiology, Wayne State University, Detroit, 
MI, 4University of Louisville School of Medicine, Louisville, KY, 
5Mathematics  and  Computer  Science, Dowling  College, Oakdale, 
NY 

There are many freely available molecular visualization programs 
used by scientists  to  view macromolecules.  Each application  has 
advantages.  However, each of these applications also has its own 
scripting language.   For scientists to  utilize  multiple  molecular 
visualization applications, they must learn  each  of those scripting 
languages.   To  unite  these applications, it is  necessary to  create 
tools to  interconvert these scripts according  to  the  conventions  of 
each program.  We have created a plugin that can read scripts from 
RasMol  and  execute  the  equivalent  commands  in  PyMOL. 
Challenges  have included  different sets  of commands and  object-
oriented  vs.  simple  text  formats.  It  is  the  goal  of  the  Structural 
Biology  Extensible  Visualization  Scripting  Language  project  to 
create  an interface  that will enable use of  scripts from one 
molecular  visualization  application  in  a  variety  of  other 
applications. This will enable users to run multiple programs while 
only needing to develop expertise in the scripting language for one 
of those programs. The project is funded in part by NIGMS grant 
#1R15GM078077. 

And also at the ACA Conference in Knoxville, TN, June 2008:

A Rasmol to PyMOL Translator. Scott Mottarella, Brett Hanson, Charles Westin, 
Paul Craig, Herbert Bernstein, Biological Sciences, Rochester Inst. of Technology, 
85 Lomb Memorial Dr., Rochester, NY 14623 USA.

For many educators and scientists, PyMOL is the application of choice for preparing 
images and animations of their structures because of the beauty and quality of 
the images. However, many are most familiar with the scripting languages 
associated with RasMol, Chime and Jmol. The long-range goal of our Structural 
Biology Extensible Visualization Scripting Language project is to make the multiple 
molecular visualization tools available to the broadest possible audience, where 
each user can use many programs, with knowledge of the scripting language for
only one of those programs. The first step has been a comparison of the command 
sets for RasMol and PyMOL, followed by creation of a plug-in for PyMOL that will 
accept RasMol script files, translate the commands into PyMOL script and execute 
the commands. The process involves searching for recognized, valid, RasMol script
commands and performing its PyMOL equivalent, either as a single command or as a 
series of commands that produce the same result. Future plans include expansion to 
additional molecular visualization programs and the preparation of a web site to 
provide script translation among the various programs. The project is funded in 
part by NIGMS grant #1R15GM078077.

=========================================================================


ChangeLog:

Revision 101  - (view) (download) (as text) (annotate) - [select for diffs]
Modified Mon Jul 12 20:12:30 2010 UTC (45 minutes, 15 seconds ago) by vinnyrose
File length: 114558 byte(s)
Diff to previous 100

Version 2.0rc3. Fixed a few typos. Correct handling of floats. More token usage. 
Several same fixes. Select still needs work on more complicated expressions.

Revision 100 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Sat Jul 10 03:22:23 2010 UTC (2 days, 17 hours ago) by yaya-hjb
File length: 116236 byte(s)
Diff to previous 99

Update version to 2.0rc2
Update readme.txt
Add local copy of gpl.txt
-- HJB


Revision 99  - (view) (download) (as text) (annotate) - [select for diffs]
Modified Fri Jul 9 23:52:12 2010 UTC (3 hours, 20 minutes ago) by vinnyrose
File length: 116183 byte(s)
Diff to previous 97

Moved selection dictionary/tuples into the init. Many bug fixes. More token usage. 
Selection algebra still needs work. Version 2.0rc1.5.

Revision 97 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Jul 6 19:10:22 2010 UTC (3 days, 8 hours ago) by vinnyrose
File length: 113326 byte(s)
Diff to previous 96

Small fix. Same version. 2.0rc1.

Revision 96 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Jul 6 18:33:40 2010 UTC (3 days, 8 hours ago) by vinnyrose
File length: 113330 byte(s)
Diff to previous 95

Updated color functions to support all of "color <atom> <color>" commands 
except for 'user' color. Can also "color bond". Several small changes to 
conform to style standards. Version 2.0rc1.

Revision 95 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Jun 30 01:54:14 2010 UTC (10 days, 1 hour ago) by yaya-hjb
File length: 97631 byte(s)
Diff to previous 94

Add back copyright notice and add GPL notice
Fix missing parens on code for atomno =
Make rasmol script .scr the default type

Revision 94 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Jun 29 19:55:13 2010 UTC (10 days, 7 hours ago) by vinnyrose
File length: 96029 byte(s)
Diff to previous 91

ConSCRIPT select function fixed. Many changes made to the structure of the 
code including making the class truly classified. Before all the functions 
were in the init of the class. The handle command now looks at token equality 
instead of command substrings. Parsing colors has been modified to a smaller 
code base.
Promol: some small bug fixes in the motif maker that occur when unwanted 
spaces occur in the input fields, a fixed motif was added. A better way 
of updating motif files is needed when this is all distributed. Version 
changed to 3.6.2. Version 4.0 candidate 3.2

Revision 91 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Fri Jun 18 16:40:23 2010 UTC (3 weeks ago) by yaya-hjb
File length: 102958 byte(s)
Diff to previous 89

Fix cartoon command -- HJB

Revision 89 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Thu Jun 17 23:42:54 2010 UTC (3 weeks, 1 day ago) by yaya-hjb
File length: 102738 byte(s)
Diff to previous 82

Add r, R, rasmol and RASMOL as alternates for VSL
Add surface and verbose -- HJB

Revision 82 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Mar 17 02:44:19 2010 UTC (3 months, 3 weeks ago) by vinnyrose
File length: 101197 byte(s)
Diff to previous 56

Changes to ConSCRIPT to make it compatible with Linux.

Many changes to ProMol.
Changed motif maker to have it's own tab, and am still working on making it 
compatible with motif finder.
Made changes to make it more compatible with linux and need to make more 
changes in that area.
Changed the GUI in many areas.
Deleted many motifs that don't seem to have a use right now. 

Revision 56 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Jun 30 15:52:20 2009 UTC (12 months, 1 week ago) by sxm3428
File length: 100866 byte(s)
Diff to previous 54

-added commands: "map color","map zap", "set", "label", "bond", "unbond"
-added internal parameters: "background", "ambient", "unitcell", "axes",
 "fontsize", "stereo", "hydrogen", "hetero", "solvent", "monitor",
 "specular", "shadow"
-determined that these parameters are incompatible: 'backfade','bondmode',
'bonds','cisangle','fontstroke','hourglass ','kinemage','menus','strands',
'transparent','vectps','write'
-added support for named maps, still can only be one at a time (ability to 
select multiple not available yet)
-edited 'load' to allow for parentheses to flank the file name
-edited 'save' to convert image types into .png if .bmp or .gif is specified
-edited 'backbone' to display more similar to RasMol's backbone
-edited 'cartoon' to display all cartoon as rectangles as RasMol does 
instead of ribbons 
-fixed a error that occurred with "zoom" when used before any center command
-Edited text on ConSCRIPT: correct spelling on P. Craig
-fixed an error that occurred when 'select' was not followed by any parameters
-added error messages for all commands not otherwise handled

Revision 54 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Apr 15 17:23:21 2009 UTC (14 months, 3 weeks ago) by hk0i
File length: 79992 byte(s)
Diff to previous 53

added the rasmol native representations to sbevsl conceal/reveal commands. Some
of the rasmol representations that are not in pymol still need to be added (to
pymol) - GM

Revision 53 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Apr 15 15:37:37 2009 UTC (14 months, 3 weeks ago) by hk0i
File length: 78135 byte(s)
Diff to previous 52

Added my name to credits in ConSCRIPT GUI, and word wrapped the text kwarg to
fit nicely and represent the \ns more clearly. - GM

Revision 52 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Apr 8 21:17:12 2009 UTC (15 months ago) by hk0i
File length: 78056 byte(s)
Diff to previous 51

removed a confusing debug output for the users.


Revision 51 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Apr 8 18:37:10 2009 UTC (15 months ago) by hk0i
File length: 78096 byte(s)
Diff to previous 50

Fixed a lot of errors caused by previous commit. Pulled unnecessary functions
out of converter class. Renamed converter class to csDialog (ConSCRIPT Dialog)
and renamed Boffo and Boffocmd functions to look more like event handling
functions. Added some docstrings as well.


Revision 50 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Apr 7 20:49:09 2009 UTC (15 months ago) by hk0i
File length: 82351 byte(s)
Diff to previous 49

Fixed a MAJOR indentation problem, lots of code was reworked. Script load
button now "clicks" properly. Also switched to using 'import Tkinter.' Fixed a
bug with the vsl reveal command that would print out a command error, even
though the command worked fine. - GM


Revision 49 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Tue Apr 7 15:03:20 2009 UTC (15 months ago) by hk0i
File length: 86280 byte(s)
Diff to previous 47

Fixed Enable VSL button GUI lockup, and switched it to a checkbutton. Also began
implementing vsl CONCEAL and REVEAL commands. Also added vim modelines.


Revision 47 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Fri Mar 20 02:52:46 2009 UTC (15 months, 2 weeks ago) by yaya-hjb
File length: 84109 byte(s)
Diff to previous 46

Decorate buttons -- HJB

Revision 46 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Fri Mar 20 02:27:39 2009 UTC (15 months, 2 weeks ago) by yaya-hjb
File length: 83876 byte(s)
Diff to previous 45

Add unused kwargs to VSL for PyMol 1.1.x -- HJB

Revision 45 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Mon Mar 16 18:59:34 2009 UTC (15 months, 3 weeks ago) by yaya-hjb
File length: 83865 byte(s)
Diff to previous 44

Fix indentation error in map code -- HJB

Revision 44 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Sun Oct 5 23:31:54 2008 UTC (21 months ago) by yaya-hjb
File length: 83861 byte(s)
Diff to previous 42

Map command updates by SM 28 Jul 08

Revision 42 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Jul 23 02:27:23 2008 UTC (23 months, 2 weeks ago) by yaya-hjb
File length: 82757 byte(s)
Diff to previous 35

Interim update for map support by S. Mottarella.

Revision 35 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Jun 25 02:27:56 2008 UTC (2 years ago) by yaya-hjb
File length: 77268 byte(s)
Diff to previous 33

Update of ConSCRIPT.py for 
ConSCRIPT release 1.13 by Scott Mottarella.
The new commands are monitor and translate and the edited commands are
spacefill/cpk, wireframe, ribbons, trace, dots, cartoon, center, zoom,
load, echo and rotate.
Rev 1.14:  Fix some indentation problems in last CVS update
Add support for temporary selections -- HJB
Rev 1.15:  Correct scaling of wireframe
Default load to CPK colors
Add support for explicit CPK colors -- HJB
brought over from blondie CVS

Revision 33 - (view) (download) (as text) (annotate) - [select for diffs]
Modified Wed Apr 30 14:28:28 2008 UTC (2 years, 2 months ago) by yaya
File length: 63640 byte(s)
Diff to previous 32

30 April 2008 -- HJB
   Unable to resolve selection problem with RGB.  Temporarily
reverted to trying to use PyMOL color name when possible in order
to restore operation of current test cases.  Moved to holding
current selection in a global VSLselection to help in debugging.
Added a VSLVerbose flag to make it easier to turn on debugging
messages. -- HJB 

26 April 2008 -- HJB

Add RasMol FetchToken as VSLFetchToken and rewrite Load command to use it
   Change all uses of SelectionSBEVSL VSLSelection
Add more of the RasMol infrastructure, including the command error
messages, the color name table converted to 0-1. instead of 0-255.
and the logic to parse RGB colors.
Provide hooks for command line SBEVSL command processing on a second tab.
The command line commands need to be enabled from the tab and then
entered with a VSL prefix.
In addition the code on VSLFetchToken has been changed to do individual
characters as -ord(ch) to avoid a conflict with tokens when unicode
characters are used in an identifier.

Note:  The update for the RGB parse is not yet complete.  The major
remaining problem seems to be that the color is not being applied
just to the current selection, but to more of the molecule

25 April 2008 -- SM (integrated by HJB)

Integrated mods by SM against base level into CVS at the 23 April level:
   Add user-defined groups via the "define" command
   Process "echo", "hbonds", "ssbonds"
   Change SBEVSLselected of prior mod to SelectionSBEVSL
   Add handling of colors by RGB triplets to handling of colors by name
   Accept empty lines and comment lines
   Rotate any loaded image by 180 around x
   

23 April 2008 -- HJB

Fixes to correct lost mod for restrict and to change to use of PyMOL 
SBEVSLselection selection name instead of variable named selected
to remember RasMol sticky selection between commands.

19 April 2008 -- HJB

Start of a restructuring to allow for nested scripts and handling of more commands:
    Create global variables filestack and filelevel to track nested scripts
    Add full copyright notice
    Change from "Script Editor" to "SBEVSL Script Loader"
    Allow "colour" as well as "color"
    Change to a standard for p in f loop to read lines
    Break up event handler into smaller routines:
       handlecommand( p ) to process a single command line p
       processSBEVSLscript( Q ) to process a script file Q
       
