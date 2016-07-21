'''Starts the ProMol Plugin for Pymol.
   ProMOL (C) Copyright 2004-2013
   Charlie Westin, Brett Hanson & Paul Craig
   GPL, No Warranty

   Release 5.0 RC 2, by HJB, 11 Apr 2013
   
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
 **********************************************************************/'''
import ProMol
def __init__(self):
    '''If everything is installed correctly this won't run'''
    import os
    print '\n'
    print ('''ERROR: The folder `ProMol` that was distributed alongside
`ProMol.py` must be installed in order for the ProMol plugin to work. 
 Please close PyMol and install the `ProMol` folder in "%s/" by copy and
 pasting.''' % os.path.dirname(__file__)).replace('\n','')
 
