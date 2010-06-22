#
#                              pdb_index_search.py
#                             -------------------
#     begin                : Sat Oct 22 2005 
#     email                : j.pansanel@pansanel.net
#     last modification    : Tue Apr 11 2006
#     version              : 0.7
#
# Description:
# ============
# This program is an extension for the PyMOL software. This software add the
# ability to search keywords into the PDB Index File. The results are
# displayed into a spreadsheet and each PDB can be open into the visualisation
# window by double-clicking on the row.
# PyMOL software is an OPEN SOURCE program distribued under the "Python"
# license. Please visit the PyMOL website for more informations:
# http://www.pymol.org 
# To use this program, you need a database supported by Python DB-API.
# This database must contain a table with at least 2 fields, the
# structure (in mdl mol format) and the name.
#
# PDB Index Search Copyright Notice
# ====================================
# 
# The PDB Entry Search source code in this file is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
# 
# ----------------------------------------------------------------------
# Copyright notice:
#   Copyright (C) 2005 by Jerome Pansanel <j.pansanel@pansanel.net
#   Copyright (C) 2004 Charles Moad <cmoad@indiana.edu> 
#           FecthPDB class: http://
#   Copyright (C) 2004 Georgy Gruss <d001120t0330@hotmail.com>
#           MolSheet and MolSheetApp class: http://zxw.nm.ru/tk_ss.htm
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

from pymol import cmd
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import string
import os
from tkFileDialog import askopenfilename, asksaveasfilename
import re
import urllib2
import StringIO
import gzip
import time

def __init__(self):
  # Simply add the menu entry and callback
  self.menuBar.addmenuitem('Plugin', 'command',
                           'PDB Index Search',
                           label = 'PDB Index Search',
                           command = lambda s=self : PDBIndexSearch(s))
'''
def PDBIndexSearch
main function who lead the investigation
'''
def PDBIndexSearch(app):
    word_list = []
    string_list = []
    results = []

    # First, we are asking for the requested string
    query_string = tkSimpleDialog.askstring('Advance PDB search',
                                            'Query: ',
                                            parent=app.root)
    if query_string:
        string_list = query_string.split(' ')

    # Remove empty string
    for word in string_list:
        if word:
            word_list.append(word)
    if word_list:
        PDBEntries = PDBEntryFile()
        results,hits = PDBEntries.search(word_list)
        if results:
	    if hits == 500:
	        print "The maximum number of hits is 500 and you are over"
		print "Please refine your search"
            print "Search is successful (%i hits)"%hits
            spreadsheet = MolSheetApp(parent=app.root,values=results)
        else:
            print "Search is unsuccessful"

'''
class PDBEntryFile
This class deals with the PDB index file, who contains all the information requested.
'''
class PDBEntryFile:
    '''
    def __init__(self)
    This function initialize the PDBEntryFile class. It set : 
    req_url : the url, where the entries file can be download
    PDBDir : the directory where is stored the entries file. This directory is called pdb, as it can contain other pdb related files.
    EntryFile : the file itself
    '''
    def __init__(self):
        self.req_url = 'ftp://ftp.rcsb.org/pub/pdb/derived_data/index/entries.idx'
        self.line_ar = [] #results is in PSS format
        try:
            self.PDBDir = os.environ['HOME'] + os.sep + ".pymol" + os.sep + "pdb"
            self.EntryFile = self.PDBDir + os.sep + "entries.idx"
        except:
            # Microsoft Windows issue with python version < 2.4
            self.PDBDir = os.environ['APPDATA'] + os.sep + ".pymol" + os.sep + "pdb"
            self.EntryFile = self.PDBDir + os.sep + "entries.idx"

    def search(self,word_list):
        self.keywords = []
        for word in word_list:
	    self.keywords.append(re.compile(word,re.IGNORECASE))
        if not self.checkEntryFile():
            return None,0
        InfoFile = open(self.EntryFile,'r')
        row = 0
        for line in InfoFile:
            if row >= 500:
                break
            state = True
            for regexp in self.keywords:
                if not regexp.search(line):
                    state = False
                    break
            if state: 
                row = row+1
                temp = line.split("\t")
                col = 0
                for part in temp:
                    if col > 26:
                        break
                    col = col+1
                    self.line_ar.append( chr(col+64) + "%i"%row + " '" + string.strip(part) ) #Strip to put away the \n character
        InfoFile.close()
        return self.line_ar,row

    def checkEntryFile(self):
        if os.path.isfile(self.EntryFile):
            return True
        else:
            try:
                tkMessageBox.showinfo('PDB EntryFile',
                                      'The PDB EntryFile does not exist. PyMOL will download it (ca. 7 Mo)')
                if not os.path.isdir(self.PDBDir):
                    os.makedirs(self.PDBDir)
                PDBEntriesDownload = TkDownloader(self.req_url, filename="PDB EntryFile")
                PDBEntries = PDBEntriesDownload.fetch()
                if not PDBEntries:
		    if PDBEntriesDownload.state == "cancel":
		        print "Download cancelled"
			return False
	            else:
                        raise urllib2.URLError("The entry file could not be accessed")
		else:
                    InfoFile = open(self.EntryFile,'w')
                    for line in PDBEntries:
                        InfoFile.write(line)
                    InfoFile.close()
                    tkMessageBox.showinfo('PDB EntryFile','The download is finished')
                    return True
            except urllib2.URLError:
                print "Network Error: ",sys.exc_info()[1]
                tkMessageBox.showerror('Download Error',
                                       'Can not retrieve PDB Entries file.\nPlease check your network connection.')
                return False
            except OSError:
                print "File Error: ",sys.exc_info()[1]
                tkMessageBox.showerror('File Error',
                                       sys.exc_info()[1])
                return False
            except:
                print "Unexpected error:", sys.exc_info()[1]
                tkMessageBox.showerror('File Error',
                                       'Unhandled error\nPlease report bug to j dot pansanel at pansanel dot net.')
                return False

'''
class MolSheet
The main part of this class has been written by Georgy Pruss
'''
class MolSheet:
    def __init__(self):
        self.cells      = {} # as entered, e.g.  'A1':3.14159265
        self.dependants = {} # dependant cells   'B2':['D4','E4']
        self.values     = {} # calculated values 'C3':True

    def _add_dependant( self, cell, target ):
        if self.dependants.has_key( cell ):
            deps = self.dependants[ cell ]
        if target not in deps:
            deps.append( target )
        else:
            self.dependants[ cell ] = [target]

    def _calculate( self, index, formula ):
        self.values[ index ] = None # to catch errors
        try:
            self.values[ index ] = eval( formula, globals(), self.values )
        except:
            self.values[ index ] = "*ERROR*"

    def _propagate( self, index, changed, started_from ):
      if self.dependants.has_key( index ):
          for cell in self.dependants[ index ]:
              if cell==started_from:
                  self.values[ index ] = "*CYCLE*"
                  return
              changed.append( cell )
              self._calculate( cell, self.cells[ cell ][0] )
              self._propagate( cell, changed, started_from )

    def __setitem__( self, index, value ):
        if value is None:
            if self.cells.has_key( index ):
                del self.cells[ index ]
            if self.values.has_key( index ):
                del self.values[ index ]
        elif isinstance( value, (int,float,str) ):
            self.cells[ index ] = value
            self.values[ index ] = value
        elif isinstance( value, tuple ): # (formula,varnames)
            self.cells[ index ] = value
            for cell in value[1]:
                self._add_dependant( cell, index ) # 'cell' influences 'index'
            # calculate this cell value
            self._calculate( index, value[0] )
        # change dependants
        self.changed = [] # which cells changed
        self._propagate( index, self.changed, index )

    def __getitem__( self, index ):
        return self.cells.get( index, None ) # return None if absent

    def value( self, index ):
        return self.values.get( index, None ) # return None if absent

'''
class MolSheetApp
The main part of this class has been written by Georgy Pruss
Major class who handle the graphic interface of the spreadsheet program
'''
class MolSheetApp:

    def help_msg(self):
        tkMessageBox.showinfo( "MolSheet - ver.%s" % self.VERSION,
                  "This version is limited to 995 rows and 25 columns.\n"
                  "Each cell can contain Integer and float numbers,\n"
	          "strings which start with ' and formulas starting with =\n."
                  "Formulas may contain practically any Python\n"
                  "expression and references to cells e.g. A1, I99.\n"
                  "Case matters. Please, be aware that no checks are done !\n"
                  "Red 'F' shows formulas in the table.\n"
	          "Some hotkeys are working: Home, PgUp, PgDn,\n"
                  "F1, Ctrl+O (open PSS file), Ctrl+S (save).\n\n"
                  "To do: scrollbars, navigation with keys\n"
                  "formatting, menu and much much more, integration of\n"
	          "2D molecular picture,...\n\n"
                  "Email: j dot pansanel at pansanel dot net\n"
                  "Copyright %s" % self.COPYRGT )

    '''
    __init__: initialize th e MolSheetApp class. Take up to 3 arg.
    parent: parent application window
    NR: number of row
    NC: number of column
    '''
    def __init__(self, parent, NR=10, NC=8, values=[]):
        self.MAX_ROWS = 995 # well, 3 digits is quite enough :)
        self.MAX_COLS =  25 # to fit in single letter i.e. A to Y, and I scroll by 5
        self.VERSION = "0.5"
        self.COPYRGT = "(C) 2004 Georgy Pruss\nModification by (C) 2005 Jerome Pansanel"
        self.ss = MolSheet() # that's the 'brain' of the program
        self.ss_dirty = False

        self.NR = NR
        self.NC = NC

        self.root = Toplevel(master=parent)
        self.root.title("MolSheet - Molecular SpreadSheet %s " % (self.VERSION))

        self.name = '' # file name (when loaded/saved) - could be shown in title too

        self.normal_rgb   = "#FFFFFF"
        self.selected_rgb = "#CCCCCC"

        self.lbls = {} # all NR*NC labels shown

        self.add_label( 0,0, "# ", "#9999FF", 3 )
        for col in range(1,NC+1):
	    if 1 == col:
                self.add_label( 0,col, 'c', "#9999FF", 5 )
	    elif 4 == col:
                self.add_label( 0,col, 'c', "#9999FF", 40 )
	    elif 7 == col:
                self.add_label( 0,col, 'c', "#9999FF", 5 )
	    else:
                self.add_label( 0,col, 'c', "#9999FF", 10 )
        for row in range(1,NR+1):
            self.add_label( row,0, 'r', "#9999FF", 3 )
            for col in range(1,NC+1):
	        if 1 == col:
                    self.add_label( row,col, '', self.normal_rgb, 5 )
  	        elif 4 == col:
                    self.add_label( row,col, '', self.normal_rgb, 40 )
	        elif 7 == col:
                    self.add_label( row,col, '', self.normal_rgb, 5 )
 	        else:
                    self.add_label( row,col, '', self.normal_rgb, 10 )

        self.R0 = 0 # offset of the upper left cell
        self.C0 = 0

        self.refresh_rows()
        self.refresh_cols()

        self.root.bind('<Double-Button-1>', self.doubleclick)
        self.root.bind('<Button-1>',self.click)  # left mouse button
        self.root.bind('<KeyPress>', self.keyhit)

        frame = Frame(self.root) # controls at the bottom
        frame.grid( row=NR+1, column=0, columnspan=NC+1, padx=1, pady=1 )

        Button(frame, text='open', command=self.loadFile ).pack(side='left')
        Button(frame, text='save', command=self.saveFile ).pack(side='left',padx=8)

        self.addr = Label(frame, text='', bg="#000040", fg="#FFFFFF", width=5,
                          borderwidth=0, anchor=E )
        self.addr.pack(side='left',padx=4)

        self.entry = Entry(frame, width=30)
        self.entry.pack(side='left')
        self.entry.bind('<Return>', self.enter)

        Button(frame, text='enter', command=self.enter ).pack(side='left')

        self.sh_f = Label( frame, text='F', bg="red", fg="white", borderwidth=0 )
        self.sh_f.pack(side='left',padx=4)
        self.sh_f.bind('<Enter>', self.show_formulas)
        self.sh_f.bind('<Leave>', self.refresh)

        Button(frame, text='home',  command=self.scroll_home ).pack(side='left',padx=4)
        Button(frame, text='<',     command=self.scroll_left ).pack(side='left')
        Button(frame, text='>',     command=self.scroll_right).pack(side='left')
        Button(frame, text='^',     command=self.scroll_up   ).pack(side='left')
        Button(frame, text='v',     command=self.scroll_down ).pack(side='left')
        Button(frame, text='help',  command=self.help_msg    ).pack(side='left',padx=8)
        Button(frame, text='quit',  command=self.execute     ).pack(side='left')

        start_widget = self.lbls[ (1,1) ]
        self.selct( start_widget )
        if values:
            self.loadValues(values)
        self.entry.focus_set()
        self.root.mainloop()

    def add_label( self, r, c, txt, bg, w ):
        align = c==0 and E or CENTER
        lbl = Label( self.root, text=txt, bg=bg, borderwidth=1, width=w, anchor=align )
        lbl.grid( row=r, column=c, padx=1, pady=1 )
        rc = (r,c)
        self.lbls[rc] = lbl # widget
        self.lbls[lbl] = rc # use it in mapping click to r.c

    def ask_save( self ): # return False if Cancel
        if self.ss_dirty:
            answer = tkMessageBox._show("Save PySS", "The table is modified, save it?",
                           icon=tkMessageBox.QUESTION, type=tkMessageBox.YESNOCANCEL )
            if answer == tkMessageBox.CANCEL:
                return False
            if answer == tkMessageBox.YES:
                self.saveFile()
        return True

    def keyhit( self, e ):
        # I wish Python had switch...
        if e.keysym == 'Prior': self.scroll_up()   # PgUp -- 5 lines up
        if e.keysym == 'Next' : self.scroll_down() # PgDn -- 5 lines down
        if e.keysym == 'Home' : self.scroll_home() # Home -- to A1 cell
        if e.keysym == 'F1'   : self.help_msg()    # F1   -- help :)
        if len(e.char)==1:
            c = ord(e.char)
            if c==15: self.loadFile()                    # Ctrl+O -- load PSS
            if c==19: self.saveFile()                    # Ctrl+S -- save PSS

    def click(self,e):
        if not self.lbls.has_key( e.widget ):
            return
        r,c = self.lbls[ e.widget ]
        if r and c: # ignore heads
            if self.selected:
                self.selected.configure( bg=self.normal_rgb )
            self.selct( e.widget )
            # focus and select
            self.entry.focus_set()
            self.entry.selection_range(0, END)

    def doubleclick(self,e):
        if not self.lbls.has_key( e.widget ):
            return
        r,c = self.lbls[ e.widget ]
        if r: #ignoring head row
            cn = self.cell_name(r,1)
            pdbName = self.ss.value(cn)
            if pdbName:
                tkMessageBox.showinfo('PDB File','Dowloading PDB File %s'%pdbName)
                pdb = FetchPDB(self.root,pdbName)
        return

    def cell_name(self, row, col):
        return chr(ord('A')+col-1+self.C0) + str(row+self.R0)

    def cell_coords( self, cellname ):
        c = ord(cellname[0])-ord('A')+1-self.C0
        r = int(cellname[1:])-self.R0
        return r,c

    def parse_enter( self, value ): # static
        if len(value)==0:
            return None
        if value[0]=="'": # string
            if value[-1:]=="'":
                value = value[1:-1] # quote at the end
            else:
                value = value[1:]
        elif value[0]=="=": # formula
            value = value[1:]
            cells = re.findall(r"\b[A-Z]\d+",value) # very dumb and simple parsing
                                                 # it doesn't undestand "strings"
            value = (value,tuple(cells))
        else: # number, could be re too
            try:
                if '.' in value or 'e' in value:
                    value = float(value)
                else:
                    value = int(value)
            except:
                return None
        return value

    def selct(self,widget):
        self.selected = widget
        self.selected.configure( bg=self.selected_rgb )
        r,c = self.lbls[ widget ]
        cn = self.cell_name(r,c)
        self.addr.configure( text=cn )
        value = self.ss[ cn ]
        if value is None:
            value = ''
        elif isinstance(value,int):
            value = str(value)
        elif isinstance(value,float): 
            value = "%.16g" % value
        elif isinstance(value,str):
            value = "'" + value
        elif isinstance(value,tuple):
            value = "=" + value[0]
        else:
            value = "?" + str(value) # just in case
        self.entry.delete(0,END)
        self.entry.insert(0,value)

    def enter(self,e=None):
        r,c = self.lbls[ self.selected ]
        cn = self.cell_name(r,c)
        self.enter_cell_value( cn, self.entry.get() )

    def show_cell( self, rc, value, align=None ):
        if align is None:
            value,align = self.format_for_cell( value )
        if 1<=rc[0]<=self.NR and 1<=rc[1]<=self.NC:
            widget = self.lbls[ rc ]
            widget.configure( text=value,anchor=align )

    def enter_cell_value(self,cn,text):
        value = self.parse_enter( text )
        self.ss[ cn ] = value
        self.ss_dirty = True
        value = self.ss.value( cn ) # recalculated
        self.show_cell( self.cell_coords( cn ), value )
        for cell in self.ss.changed:
            value = self.ss.value( cell ) # recalculated
            rc = self.cell_coords( cell )
            self.show_cell( rc, value )

    def format_for_cell(self,value): # ret value, default-align
        if value is None:
            return '',W
        if isinstance(value,bool):
            return str(value),CENTER
        if isinstance(value,int):
            return ("%d" % value),E
        if isinstance(value,float):
            return ("%.6g" % value),E
        return str(value),W

    def show_formulas(self,e=None):
        for row in range(1,self.NR+1):
            for col in range(1,self.NC+1):
                cn = self.cell_name( row, col )
                value = self.ss[ cn ]
                if isinstance(value,tuple):
                    self.show_cell( (row,col), value[0],W )

    def refresh(self,e=None): # e is passed when called from binding
        for row in range(1,self.NR+1):
            for col in range(1,self.NC+1):
                cn = self.cell_name( row, col )
                value = self.ss.value( cn ) # recalculated
                self.show_cell( (row,col), value )

    def refresh_rows( self ):
        offset = self.R0
        for row in range(1,self.NR+1):
            lbl = self.lbls[ (row,0) ]
            lbl.configure( text=str(row+offset) )

    def refresh_cols( self ):
        offset = self.C0
        for col in range(1,self.NC+1):
            lbl = self.lbls[ (0,col) ]
            lbl.configure( text=chr(ord('A')+col-1+offset) )

    def finish_scroll(self):
        self.refresh_rows()
        self.refresh_cols()
        self.refresh()
        self.selct( self.selected )

    def scroll_home(self):
        self.R0 = 0
        self.C0 = 0
        self.finish_scroll()

    def scroll_left(self):
        self.C0 = max( 0, self.C0-5 )
        self.finish_scroll()

    def scroll_right(self):
        self.C0 = min( self.MAX_COLS-self.NC, self.C0+5 )
        self.finish_scroll()

    def scroll_up(self):
        self.R0 = max( 0, self.R0-5 )
        self.finish_scroll()

    def scroll_down(self):
        self.R0 = min( self.MAX_ROWS-self.NR, self.R0+5 )
        self.finish_scroll()

    def quit(self):
        if self.ask_save():
            self.root.quit()

    def loadFile(self, name=False):
        if not self.ask_save():
            return
        if not name:
            name = askopenfilename(master=self.root, title='Select PySS file to open',
                                   filetypes=[('PySS files','*.pss'),('All Files','*.*')])
        if name:
            self.ss = MolSheet()
            self.ss_dirty = False
            f = file( name, "rt" )
            for line in f:
                if len(line)<3 or line.startswith('#'):
                    continue
                head,tail = line.split(' ',1)
                self.enter_cell_value(head,tail[:-1])
            f.close()
            self.scroll_home()
            self.name = name

    def loadValues(self, var):
        for line in var:
            if len(line)<3 or line.startswith('#'):
                continue
            head,tail = line.split(' ',1)
            self.enter_cell_value(head,tail)
        self.scroll_home()
        self.name = "PDBSearch"

    '''
    def save(self)
    This is the save function. It's open an file dialog, and write the file at the right place.
    Default file format is pss. It could be interesting to add support for csv file.
    '''
    def saveFile( self ):
        name = asksaveasfilename(master=self.root,
                                 title='Select/enter PySS file to save',
                                 defaultextension="*.pss|*.*||",
                                 filetypes=[('PySS files','*.pss'),('All Files','*.*')],
                                 initialfile=self.name)
        if name:
            f = file( name, "wt" )
            print >>f, "# PySS", self.VERSION
            for k,v in self.ss.cells.items():
                if   isinstance(v,int):
                    print >>f, k,v
                elif isinstance(v,float):
                    print >>f, k,"%.16g"%v
                elif isinstance(v,str):
                    print >>f, k,"'"+v
                elif isinstance(v,tuple):
                    print >>f, k,"="+v[0]
                else:
                    print >>f, "# ???",str(v)
            print >>f, "# EOF"
            f.close()
            self.ss_dirty = False
            self.name = name

    def execute(self):
        self.root.destroy()

'''
class FetchPDB
This class is inspired from the remote_load_pdb.py file, written by Charles Moad.
Function:
__init__(self,app,pdbCode): initialization of the class

'''
class FetchPDB:
    def __init__(self,app,pdbCode):
        self.parent = app
        self.pdbCode = pdbCode.upper()
        pdbFile = None
        try:
            pdbDownload = TkDownloader('http://www.rcsb.org/pdb/files/' + self.pdbCode + '.pdb.gz',
                                       filename = pdbCode + ".pdb")
            pdbFile = pdbDownload.fetch()
            if not pdbFile:
	        if pdbDownload.state == "cancel":
		    print "Download cancelled"
		else:
                    raise  urllib2.URLError
	    else:
                pdbStream = StringIO.StringIO( pdbFile )
                pdbData = gzip.GzipFile(fileobj=pdbStream)
                cmd.read_pdbstr(pdbData.read(), self.pdbCode)

        except urllib2.URLError:
            tkMessageBox.showerror('Connection Error',
                                   'Can not retrieve PDB file.\nPlease check your network connection.')
        except:
            print "Unexpected error:", sys.exc_info()[0]
            tkMessageBox.showerror('Error',
                                   'Unhandled error\nPlease report bug to j dot pansanel at pansanel dot net.')

class TkDownloader:
    '''
    This provides a simple downloader with progress bar.
    '''
    def __init__(self,url,parent=None,filename=None):
        '''Initialize the download environment

        Arguments:
            parent -- a parent window (the application window)
            url -- the url to fetch
            filename -- the name of the file to retrieve
        '''
        self.PERC_STEP  = 1
        self.CHUNK_SIZE = 10*1024
        self.url = url
        self.parent = parent
        self.filename = filename
        # Initialize result data
        self.content = ''
	self.state = "ok"

    def fetch(self):
        '''
        Initialize the download
        Create progress bar
        Get content and update progress bar
        Close progress bar and return result
        '''
        f_in = None
        bar = None
        # Open the URL for reading, try getting the content length.
        try:
            f_in = urllib2.urlopen(self.url)
            f_in_info = f_in.headers.getheader("Content-Length", "-1")
            f_in_size = int(f_in_info.split(";",1)[0])
            '''
            In some case, we can not get the size of the file
            we call a special progressbar
            '''
            if f_in_size == -1:
                bar = ProgressBar(self.parent,self.filename,0)
            else:
                bar = ProgressBar(self.parent,self.filename,1)
                
            # Initialize variables tracking download progress
            perc_step, perc, next_perc = self.PERC_STEP, 0, 0
            perc_chunk = f_in_size / (100/self.PERC_STEP) 
            content_size = 0
            while True:
                # Read in a chunk of data, breaking from loop if 
                # no data returned
                data = f_in.read(self.CHUNK_SIZE)
                if len(data) == 0: break
            
                # Write a chunk of data, incrementing output file size
                self.content = self.content + data
                content_size += len(data)
                if bar.event == 'cancel':
                    break
                # If the current output size has exceeded the next
                if f_in_size == -1:
                    bar.updateProgress()
		elif f_in_size > 0 and content_size >= next_perc:
                    bar.updateProgress(perc)
                    perc += perc_step
                    next_perc += perc_chunk
            
            # Close output and return container with data
            if "cancel" == bar.event:
	        self.state = "cancel"
	        self.content = None
  	    bar.destroy()
            f_in.close()
            return self.content	
            
        except:
            print sys.exc_info()[1]
  	    if f_in is not None:
	        f_in.close()
  	    if bar is not None:
	        bar.destroy()
            return None

class ProgressBar(Toplevel):
    '''
    This provides a progress bar. 
    '''
    def __init__(self,parent,filename=None,bartype=0):
        Toplevel.__init__(self,parent)
        self.transient(parent)
        self.title('Download')
        self.protocol('WM_DELETE_WINDOW',self.destroy)
        self.parent = parent
	if filename:
	    self.headText = "Downloading " + filename
	else:
	    self.headText = "Downloading..."
	if bartype not in [0,1]:
            raise TypeError, "Bartype is not valid:" + str(bartype)
	else:
	    self.bartype = bartype
        self.event = "download"
        if self.parent is not None:
            self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                      parent.winfo_rooty()+50))
        self.main = Frame(self,relief='ridge',borderwidth=2)
        self.main.pack()
        # header
        self.header = Label(self.main, text=self.headText)
        self.header.pack(expand=1,fill="both")
	if bartype not in [0,1]:
            raise TypeError, "Bad value for bartype: " + str(bartype)
        if self.bartype == 0:
            #text body
            self.v = StringVar()
            self.v.set("---")
            self.bar = Label(self.main,textvariable = self.v)
            self.bar.pack()
        else:
            # create frame to hold status bar
            self.body = Frame(self.main,relief='sunken',borderwidth=3)
            self.body.pack()
            self.bar = Canvas(self.body,width=200,height=10)
            self.bar.pack()
            self.bar.create_rectangle(0,0,1,10,fill='green',
                                      tags='scale')
        # cancel button
        self.cancelButton = Button(self.main, text="Cancel",
                                   width=10, command=self.cancel)
        self.cancelButton.pack()
        self.main.bind("<Escape>", self.cancel)
        self.main.focus_set()
        # create interface
        self.event = ''
        self.update()

    def updateProgress(self,value=None):
        if value is None:
	    if self.bartype == 0:
                # Add function to update v.char
                if "---" == self.v.get():
                    self.v.set(" \\ ")
                elif " \\ " == self.v.get():
                    self.v.set(" | ")
                elif " | " == self.v.get():
                    self.v.set(" / ")
                else:
                    self.v.set("---")
	    else:
                raise OutOfRangeError,value
        elif value not in range(0,101):
            raise OutOfRangeError,value
        elif value == 100:
                self.event = 'finish'
                if self.parent:
                    self.parent.focus_set()
                self.destroy()
        else:
            self.bar.coords('scale',0,0,2*value,10)
        time.sleep(0.1)
        self.update()

    def cancel(self, event=None):
        self.event = 'cancel'
        if self.parent:
            self.parent.focus_set()
        self.destroy()

if __name__ == "__main__":
    root= Tk()
    root.update()
    t=PDBSearch(root) 
