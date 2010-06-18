ConScript Installation Instructions

download PyMOL from http://pymol.sourceforge.net and install to default location

Unzip all all files and move ConSCRIPT.py to:

  C:\Program Files\DeLano Scientific\pymol\modules\pmg_tk\startup\

on windows with a standard 0.99 pymol installation, or locate
the portion of the pymol installation tree that contains 

   modules/pmg_tk/startup

and place ConSCRIPT.py in startup.  For example in a fink pymol
istallation for python 2.4 on a mac

  /sw/lib/pymol-py24/modules/pmg_tk/startup


When all files are in place, the ConScript interface can be run by choosing ConSCRIPT from the PyMOL plug-in menu.  

Work done in part with support from NIH and Nation Institute of General Medical Sciences (NIGMS) under Grant number 1R15GM078077-01.

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
advantages.  ; Howeve ions also has its own 
scripting language.   For scientists to  utilize  multiple  molecular 
visualization applications, they must learn  each  of those scripting 
languages.   To  unite  these applications, it is  necessary to  create 
tools to  interconvert these scripts according  to  the  conventions  of  each program.  We have created a plugin that can read scripts from 
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

A Rasmol to PyMOL Translator. Scott Mottarella, Brett Hanson, Charles Westin, Paul Craig, Herbert Bernstein,
Biological Sciences, Rochester Inst. of Technology, 85 Lomb Memorial Dr., Rochester, NY 14623 USA.
For many educators and scientists, PyMOL is the application of choice for preparing images and animations of their
structures because of the beauty and quality of the images. However, many are most familiar with the scripting
languages associated with RasMol, Chime and Jmol. The long-range goal of our Structural Biology Extensible
Visualization Scripting Language project is to make the multiple molecular visualization tools available to the
broadest possible audience, where each user can use many programs, with knowledge of the scripting language for
only one of those programs. The first step has been a comparison of the command sets for RasMol and PyMOL,
followed by creation of a plug-in for PyMOL that will accept RasMol script files, translate the commands into
PyMOL script and execute the commands. The process involves searching for recognized, valid, RasMol script
commands and performing its PyMOL equivalent, either as a single command or as a series of commands that
produce the same result. Future plans include expansion to additional molecular visualization programs and the
preparation of a web site to provide script translation among the various programs. The project is funded in part by
NIGMS grant #1R15GM078077.


ChangeLog:

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
       
