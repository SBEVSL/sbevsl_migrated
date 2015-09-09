This is the automotif version of ProMol by MO.
*** This version is set up for windows.  For Linux and Mac some of the
paths need to be changed.  Those changes will be made automatic in the
release version in the main branch ***

In order to use the automatic motif generation logic, you need to prepare
at least one of the following two files, and in some cases, both.
The default location for both files is in the ProMol folder.  Samples
are included

1.  pdb_list.txt

This is a comma separated list of pdb IDs.  You may split them over
multiple lines, but don't forget the comma at the end of each line
except for the last one, e.g.

1jms,1dji,1uw9,1pam,1nb8,1q6x,1otx,1v0h,1c7j,1auj,
1h6n,1glh,1d0c,3ev0,1ce8,3jqc,1sg8,1twr,1sev,2e8w

2.  lit_lib_23.txt

This is a file, usually drawn from the CSA, giving the PDB id's, EC numbers
and active site residues.  The sample provided in this kit is fairly
extensive, but if a pdb id is rejected in the auto motif build you
may have to add a section in with the necessary information.  Here is
a sample of the section for 2jjj

> 2jjj.A        3.4.23.22
SER     38      S
ASP     35      S
THR     222     S
ASP     219     S
THR     220     S
THR     36      S

The section begins with the character ">", a tab and then the PDB id 
followed immediately by a period and then the chain id, and then by
a horizontal tab character.  The EC code completes the first line.  This
line is followed by one line per residue with the tab-separated values:
residue name, residue number and "X", "S", "O", "N", ,"SO" or "SN" with
used as flags for turning the backbone on as follows:

                N : backbone amide
                SN : sidechain and backbone amide
                O : backbone carbonyl
                SO : sidechain and backbone carbonyl
                SNO : sidechain, backbone amide, and backbone carbonyl


  -- HJB, 9 Sep 15


