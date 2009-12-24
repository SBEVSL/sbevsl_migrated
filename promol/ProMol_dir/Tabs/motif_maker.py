        page = notebook.add('Motif Database')
        notebook.tab('Motif Database').focus_set()
        
        group = Pmw.Group(page, tag_text = 'Binding Search')
        group.grid(row=2, column=0, padx=0, pady=0)
        interior = group.interior()

        
        
        Codeent = Label(interior, text = "Enter PDB Code:")
        Codeent.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'nw')
        entpdb = Entry(interior, width = 6)
        entpdb.grid(row = 0, column = 1, padx = 5, pady = 5, sticky ='nw')
        entl = Entry(interior)
        entl.insert(0,0)
        entl1 = Entry(interior)
        entl1.insert(0,2)
        entl2 = Entry(interior)
        entl2.insert(0,6)
        entl3 = Entry(interior)
        entl3.insert(0,7)
        ent2 = Entry(interior)
        databtn = Button(interior, text = 'Databaser')
        databtn.grid()


        
        
        def editor(event):
            root = Tk()
            deletebtn = Button(root, text = 'Delete Database')
            deletebtn.grid()
            pdblists = Pmw.OptionMenu(root,label_text = 'Databases:',labelpos = 'n',
                items = (' ',),
                menubutton_width = 8, command=binding)
            pdblists.grid()
            
            reader = open('./modules/pmg_tk/startup/PDB_List/Master.txt', 'r')
            for line in reader:
                items = eval(line)
                items.sort()
                pdblists.setitems(items)
        
        
        editbtn = Button(interior, text = 'Database Edit')
        editbtn.grid()
        editbtn.bind('<Button-1>', editor)
        
        
        def binding(tag):
            running = True #keep the loop running...

            
            
            f = open('./modules/pmg_tk/startup/PDB_List/'+tag+'.log', 'r')
            
            for line in f:
                print line
                listpdb = line
            
            
            #Read the file dummy
            
            while running: #loop
                try:
                    
                    ent2.delete(0,100000)
                    
                    a = int(entl.get()) + 1
                    
                    if a ==1:
                        b = 2
                        c = 7
                    
                    if a >1:
                       b = int(entl1.get()) + 9
                       c = int(entl3.get()) + 9
                    
                    ent2.insert(0,listpdb[b:c])
                    if len(ent2.get())<4:
                        thiswillkillit.dead#make it except
                    entl.delete(0,100000)
                    entl.insert(0,a)
                    
                    entl1.delete(0,100000)
                    entl1.insert(0,b)
                    entl3.delete(0,100000)
                    entl3.insert(0,c)
                    
                    cmd.do("load /Program Files/DeLano Scientific/PyMOL/modules/pmg_tk/startup/dump/%s.pdb"%(listpdb[b:c]))
                    
                    try:
                        cmd.do('set all_states, on')
                        cmd.intra_fit ('%s'%(entpdb.get()))
                        cmd.intra_fit('%s'%(listpdb[b:c]))
                    
                    except:
                        pass
                    
                    cmd.do('align %s////CA, %s////CA, object=alignment'%(entpdb.get(),listpdb[b:c]))
                    
                    cmd.delete("%s"%(listpdb[b:c]))
                
                except:
                    running = False #end the loop
                    entl.delete(0,100000)
                    entl.insert(0,0)


        
        
        #master list stuff
        pdblists = Pmw.OptionMenu(interior,label_text = 'Databases:',labelpos = 'n',
                items = (' ',),
                menubutton_width = 8, command=binding)
        pdblists.grid()
        
        reader = open('./modules/pmg_tk/startup/PDB_List/Master.txt', 'r')
        for line in reader:
            items = eval(line)
            items.sort()
            pdblists.setitems(items)
        
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
        
        def PDBIndexSearch(event):
            word_list = []
            string_list = []
            results = []
            
            # First, we are asking for the requested string
            query_string = askstring('Advance PDB search',
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
                    if hits == 1000: #lookin
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
                    if row >= 1000: #
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
                        showinfo('PDB EntryFile',
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
                            showinfo('PDB EntryFile','The download is finished')
                            return True
                    except urllib2.URLError:
                        print "Network Error: ",sys.exc_info()[1]
                        showerror('Download Error',
                                               'Can not retrieve PDB Entries file.\nPlease check your network connection.')
                        return False
                    except OSError:
                        print "File Error: ",sys.exc_info()[1]
                        showerror('File Error',
                                               sys.exc_info()[1])
                        return False
                    except:
                        print "Unexpected error:", sys.exc_info()[1]
                        showerror('File Error',
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
                showinfo( "MolSheet - ver.%s" % self.VERSION,
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
                selected_rgb = "#CCCCCC"
                
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
                
                self.entry = Entry(frame, width=5)
                self.entry.pack(side='left')
                self.entry.bind('<Return>', self.enter)
                #entry fields for database function...Charlie's Code
                self.lab1 = Label(frame, text='ligand:')
                self.lab1.pack(side='left')
                
                self.entry1 = Entry(frame, width=5)
                self.entry1.pack(side='left')
                
                self.lab2 = Label(frame, text='range:')
                self.lab2.pack(side='left')
                
                self.entry2 = Entry(frame, width=5)
                self.entry2.pack(side='left')
                Button(frame, text='Database',  command=self.database).pack(side='left')
                self.dumbent = Entry(frame)
                self.entl = Entry(frame)
                self.entl.insert(0,0)
                self.ent2 = Entry(frame)
                self.ent3 = Entry(frame)
                
                #end of Charlie's code
                
                Button(frame, text='home',  command=self.scroll_home ).pack(side='left',padx=4)
                Button(frame, text='<',     command=self.scroll_left ).pack(side='left')
                Button(frame, text='>',     command=self.scroll_right).pack(side='left')
                Button(frame, text='^',     command=self.scroll_up   ).pack(side='left')
                Button(frame, text='v',     command=self.scroll_down ).pack(side='left')
                Button(frame, text='help',  command=self.help_msg    ).pack(side='left',padx=8)
                Button(frame, text='quit',  command=self.execute     ).pack(side='left')
                
                
                start_widget = self.lbls[ (1,1) ]
                selct( start_widget )
                if values:
                    self.loadValues(values)
                self.entry.focus_set()
                
                self.root.mainloop()
            
            def populate(self):
                    objects = cmd.get_names('all')
                    cmd.select("Chain-A", "chain A")
                    cmd.select("Chain-B", "chain B")
                    cmd.select("Chain-C", "chain C")
                    cmd.select("Chain-D", "chain D")
                    cmd.select("Chain-E", "chain E")
                    cmd.select("Chain-F", "chain F")
                    cmd.select("Chain-G", "chain G")
                    cmd.select("Chain-H", "chain H")
                    cmd.select("Chain-I", "chain I")
                    cmd.select("Chain-J", "chain J")
                    cmd.select("Chain-K", "chain K")
                    cmd.select("Chain-L", "chain L")
                    cmd.select("Chain-M", "chain M")
                    cmd.select("Chain-N", "chain N")
                    cmd.select("Chain-O", "chain O")
                    cmd.select("Chain-P", "chain P")
                    cmd.select("Chain-Q", "chain Q")
                    cmd.select("Chain-R", "chain R")
                    cmd.select("Chain-S", "chain S")
                    cmd.select("Chain-T", "chain T")
                    cmd.select("Chain-U", "chain U")
                    cmd.select("Chain-V", "chain V")
                    cmd.select("Chain-W", "chain W")
                    cmd.select("Chain-X", "chain X")
                    cmd.select("Chain-Y", "chain Y")
                    cmd.select("Chain-Z", "chain Z")
                    objects = cmd.get_names('all')
                    if 'Chain-A' in objects:
                        x1 = cmd.index('Chain-A')
                        n1  = len(x1)
                        if(n1 < 1):
                            cmd.delete('Chain-A')
                    if 'Chain-B' in objects:
                        x2 = cmd.index('Chain-B')
                        n2 = len(x2)
                        if(n2 < 1):
                            cmd.delete('Chain-B')
                    if 'Chain-C' in objects:
                        x3 = cmd.index('Chain-C')
                        n3 = len(x3)
                        if(n3 < 1):
                            cmd.delete('Chain-C')
                    if 'Chain-D' in objects:
                        x4 = cmd.index('Chain-D')
                        n4  = len(x4)
                        if(n4 < 1):
                            cmd.delete('Chain-D')
                    if 'Chain-E' in objects:
                        x5 = cmd.index('Chain-E')
                        n5 = len(x5)
                        if(n5 < 1):
                            cmd.delete('Chain-E')
                    if 'Chain-F' in objects:
                        x6 = cmd.index('Chain-F')
                        n6 = len(x6)
                        if(n6 < 1):
                            cmd.delete('Chain-F')
                    if 'Chain-G' in objects:
                        x7 = cmd.index('Chain-G')
                        n7  = len(x7)
                        if(n7 < 1):
                            cmd.delete('Chain-G')
                    if 'Chain-H' in objects:
                        x8 = cmd.index('Chain-H')
                        n8 = len(x8)
                        if(n8 < 1):
                            cmd.delete('Chain-H')
                    if 'Chain-I' in objects:
                        x9 = cmd.index('Chain-I')
                        n9 = len(x9)
                        if(n9 < 1):
                            cmd.delete('Chain-I')
                    if 'Chain-J' in objects:
                        x10 = cmd.index('Chain-J')
                        n10  = len(x10)
                        if(n10 < 1):
                            cmd.delete('Chain-J')
                    if 'Chain-K' in objects:
                        x11 = cmd.index('Chain-K')
                        n11 = len(x11)
                        if(n11 < 1):
                            cmd.delete('Chain-K')
                    if 'Chain-L' in objects:
                        x12 = cmd.index('Chain-L')
                        n12 = len(x12)
                        if(n12 < 1):
                            cmd.delete('Chain-L')
                    if 'Chain-M' in objects:
                        x13 = cmd.index('Chain-M')
                        n13  = len(x13)
                        if(n13 < 1):
                            cmd.delete('Chain-M')
                    if 'Chain-N' in objects:
                        x14 = cmd.index('Chain-N')
                        n14 = len(x14)
                        if(n14 < 1):
                            cmd.delete('Chain-N')
                    if 'Chain-O' in objects:
                        x15 = cmd.index('Chain-O')
                        n15 = len(x15)
                        if(n15 < 1):
                            cmd.delete('Chain-O')
                    if 'Chain-P' in objects:
                        x16 = cmd.index('Chain-P')
                        n16  = len(x16)
                        if(n16 < 1):
                            cmd.delete('Chain-P')
                    if 'Chain-Q' in objects:
                        x17 = cmd.index('Chain-Q')
                        n17 = len(x17)
                        if(n17 < 1):
                            cmd.delete('Chain-Q')
                    if 'Chain-R' in objects:
                        x18 = cmd.index('Chain-R')
                        n18 = len(x18)
                        if(n18 < 1):
                            cmd.delete('Chain-R')
                    if 'Chain-S' in objects:
                        x19 = cmd.index('Chain-S')
                        n19  = len(x19)
                        if(n19 < 1):
                            cmd.delete('Chain-S')
                    if 'Chain-T' in objects:
                        x20 = cmd.index('Chain-T')
                        n20 = len(x20)
                        if(n20 < 1):
                            cmd.delete('Chain-T')
                    if 'Chain-U' in objects:
                        x21 = cmd.index('Chain-U')
                        n21 = len(x21)
                        if(n21 < 1):
                            cmd.delete('Chain-U')
                    if 'Chain-V' in objects:
                        x22 = cmd.index('Chain-V')
                        n22 = len(x22)
                        if(n22 < 1):
                            cmd.delete('Chain-V')
                    if 'Chain-W' in objects:
                        x23 = cmd.index('Chain-W')
                        n23 = len(x23)
                        if(n23 < 1):
                            cmd.delete('Chain-W')
                    if 'Chain-X' in objects:
                        x24 = cmd.index('Chain-X')
                        n24 = len(x24)
                        if(n24 < 1):
                            cmd.delete('Chain-X')
                    if 'Chain-Y' in objects:
                        x25 = cmd.index('Chain-Y')
                        n25 = len(x25)
                        if(n25 < 1):
                            cmd.delete('Chain-Y')
                    if 'Chain-Z' in objects:
                        x26 = cmd.index('Chain-Z')
                        n26 = len(x26)
                        if(n26 < 1):
                            cmd.delete('Chain-Z')
            
            def clean(self):
                running = True
                import os
                f = open('./modules/pmg_tk/startup/PDB_List/%s_%s.log'%(self.entry1.get(),self.entry2.get()), 'r')
                
                for line in f:
                    listpdb = eval(line)
                self.dumbent.delete(0,100000)
                pdblist2 = []
                listpdb.insert(0, "bar")
                while running:
                    try:
                        
                        self.ent2.delete(0,100000)
                        a = int(self.entl.get()) + 1
                        self.entl.delete(0,100000)
                        self.entl.insert(0,a)
                        self.ent2.insert(0,listpdb[a])
                        
                        cmd.do("load /Program Files/DeLano Scientific/PyMOL/modules/pmg_tk/startup/dump/%s.pdb"%(listpdb[a]))
                        
                        self.populate()
                        
                        objects = cmd.get_names('all')
                        
                        if 'Chain-A' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sA.pdb,(Chain-A)'%(listpdb[a]))
                            
                            pdblist2.append(self.ent2.get()+'A')
                        
                        if 'Chain-B' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sB.pdb,(Chain-B)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'B')
                        if 'Chain-C' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sC.pdb,(Chain-C)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'C')
                        if 'Chain-D' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sD.pdb,(Chain-D)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'D')
                        if 'Chain-E' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sE.pdb,(Chain-E)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'E')
                        if 'Chain-F' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sF.pdb,(Chain-F)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'F')
                        if 'Chain-G' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sG.pdb,(Chain-G)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'G')
                        if 'Chain-H' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sH.pdb,(Chain-H)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'H')
                        if 'Chain-I' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sI.pdb,(Chain-I)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'I')
                        if 'Chain-J' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sJ.pdb,(Chain-J)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'J')
                        if 'Chain-K' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sK.pdb,(Chain-K)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'K')
                        if 'Chain-L' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sL.pdb,(Chain-L)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'L')
                        if 'Chain-M' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sM.pdb,(Chain-M)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'M')
                        if 'Chain-N' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sN.pdb,(Chain-N)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'N')
                        if 'Chain-O' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sO.pdb,(Chain-O)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'O')
                        if 'Chain-P' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sP.pdb,(Chain-P)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'P')
                        if 'Chain-Q' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sQ.pdb,(Chain-Q)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'Q')
                        if 'Chain-R' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sR.pdb,(Chain-R)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'R')
                        if 'Chain-S' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sS.pdb,(Chain-S)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'S')
                        if 'Chain-T' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sT.pdb,(Chain-T)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'T')
                        if 'Chain-U' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sU.pdb,(Chain-U)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'U')
                        if 'Chain-V' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sV.pdb,(Chain-V)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'V')
                        if 'Chain-W' in objects:
                            
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sW.pdb,(Chain-W)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'W')
                        
                        if 'Chain-X' in objects:
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sX.pdb,(Chain-X)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'X')
                        
                        if 'Chain-Y' in objects:
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sY.pdb,(Chain-Y)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'Y')
                        
                        if 'Chain-Z' in objects:
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%sZ.pdb,(Chain-Z)'%(listpdb[a]))
                            pdblist2.append(self.ent2.get()+'Z')
                        cmd.delete('all')
                        
                        cmd.reinitialize()
                        
                        fil = './modules/pmg_tk/startup/dump/%s.pdb'%(listpdb[a])
                        os.remove(fil)

                    
                    
                    except:
                        
                        
                        running = False
                        self.dumbent.insert(0,pdblist2)
                        logfile1 = open(f.name, 'w')
                        logfile1.write(self.dumbent.get())
                        logfile1.close()
                        print file(f.name).read()
                        self.dumbent.delete(0,10000)
                        reader = open('./modules/pmg_tk/startup/PDB_List/Master.txt', 'r')
                        for line in reader:
                            items = eval(line)
                            items.sort()
                            pdblists.setitems(items)


            
            
            def database (self):
                running = True #keep the loop running...
                garbage = []
                pdblist = []
                masterlist = []
                while running: #loop
                    self.entry.delete(0,1)
                    if int(len(self.entry.get())) == 4: #make sure your not at the end of the list
                        pdbName = self.entry.get()
                        pdb = FetchPDB(self.root,pdbName)
                        cmd.remove('resn hoh')
                        cmd.select('resn %s around %s'%(self.entry1.get(),self.entry2.get()))#ligand name then range size
                        x = cmd.index('sele')
                        n  = len(x)
                        if(n < 1): #make sure that something was selected
                            cmd.do('reinitialize')
                            self.scroll_down()
                        else:
                            cmd.do('save C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup/dump/%s.pdb,(sele)'%(self.entry.get()))
                            pdblist.append(self.entry.get())
                            cmd.do('reinitialize')
                            self.scroll_down()
                    else: #your at the end
                        running = False #end the loop
                else:
                    self.dumbent.insert(0,pdblist)
                    logfile = open('./modules/pmg_tk/startup/PDB_List/%s_%s.log'%(self.entry1.get(),self.entry2.get()), 'w')
                    logfile.write(self.dumbent.get())
                    logfile.close()
                    print file('./modules/pmg_tk/startup/PDB_List/%s_%s.log'%(self.entry1.get(),self.entry2.get())).read()
                    
                    reader = open('./modules/pmg_tk/startup/PDB_List/Master.txt', 'r')
                    for line in reader:
                      masterlist = eval(line)
                    masterlist.append('%s_%s'%(self.entry1.get(),self.entry2.get()))
                    logfile2 = open('./modules/pmg_tk/startup/PDB_List/Master.txt', 'w')
                    self.ent3.insert(0,masterlist)
                    logfile2.write(self.ent3.get())
                    logfile2.close()
                    self.ent3.delete(0,100000)
                    
                    self.clean()
                    cmd.reinitialize()

                    
                    
                    self.execute()


               
               
               #End of Charlie's Code
            
            
            def add_label( self, r, c, txt, bg, w ):
                align = c==0 and E or CENTER
                lbl = Label( self.root, text=txt, bg=bg, borderwidth=1, width=w, anchor=align )
                lbl.grid( row=r, column=c, padx=1, pady=1 )
                rc = (r,c)
                self.lbls[rc] = lbl # widget
                self.lbls[lbl] = rc # use it in mapping click to r.c
            
            def ask_save( self ): # return False if Cancel
                if self.ss_dirty:
                    answer = _show("Save PySS", "The table is modified, save it?",
                                   icon=QUESTION, type=YESNOCANCEL )
                    if answer == CANCEL:
                        return False
                    if answer == YES:
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
                    if selected:
                        selected.configure( bg=self.normal_rgb )
                    selct( e.widget )
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
                        showinfo('PDB File','Dowloading PDB File %s'%pdbName)
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
                selected = widget
                selected.configure( bg=selected_rgb )
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
                r,c = self.lbls[ selected ]
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
                selct( selected )
            
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
                self.R0 = min( self.MAX_ROWS-self.NR, self.R0+1 )
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
                    showerror('Connection Error',
                                           'Can not retrieve PDB file.\nPlease check your network connection.')
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    showerror('Error',
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
                update()
            
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
                update()
            
            def cancel(self, event=None):
                self.event = 'cancel'
                if self.parent:
                    self.parent.focus_set()
                self.destroy()
        
        if __name__ == "__main__":
            root= Tk()
            root.update()
            t=PDBSearch(root)
        
        databtn.bind('<Button-1>', PDBIndexSearch)
        
        group = Pmw.Group(page, tag_text = 'Motif Database')
        group.grid(row=3, column=0, padx=0, pady=0)
        interior = group.interior()
        atlab = Label(interior, text = "Atoms")
        atlab.grid(row=1, column =0, sticky = 'w')
        
        def randomized(*args):
            cmd.delete('all')
            pdbCode = linecache.getline('./modules/pmg_tk/startup/pdb_entry_type.txt',random.randint(1, 41258))
            
            pdbCode = string.upper(pdbCode)
            try:
                filename = urllib.urlretrieve('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                                                        pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                                                        pdbCode + '&compression=gz')[0]
            except:
                showerror('Connection Error',
                                       'Can not access to the PDB database.\n'+
                                       'Please check your Internet access.',
                                       parent=app.root)
            else:
                if (os.path.getsize(filename) > 0): # If 0, then pdb code was invalid
                    # Uncompress the file while reading
                    fpin = gzip.open(filename)
                    
                    # Form the pdb output name
                    outputname = os.path.dirname(filename) + os.sep + pdbCode + '.pdb'
                    fpout = open(outputname, 'w')
                    fpout.write(fpin.read()) # Write pdb file
                    
                    fpin.close()
                    fpout.close()
                    
                    cmd.load(outputname,quiet=0) # Load the fresh pdb
                else:
                    showerror('Invalid Code',
                                                  'You entered an invalid pdb code:' + pdbCode,
                                                  parent=app.root)
                
                os.remove(filename) # Remove tmp file (leave the pdb)
        
        cmd.extend('randomized',randomized)
        
        entcount = Entry(interior)
        entz = Entry(interior)
        def runum():#run all the motifs and count the atoms n the Motifs folder
                
                a = ['']
                entz.delete(0,1000)
                entz.insert(0,0)
                for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
                    a.append(object)
                skipping =True
                list  = []
                while skipping:
                    
                    z = int(entz.get()) + 1
                    entz.delete(0,1000)
                    entz.insert(0,z)
                    try:
                        cmd.set("suspend_updates",1,quiet=1)
                        time.sleep(1)#rate limiter
                        cmd.delete('Motif')
                        cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[z])
                        cmd.set("suspend_updates",0,quiet=1)
                        time.sleep(1)#rate limiter
                        
                        r = cmd.count_atoms('Motif')
                        entcount.delete(0,100)
                        entcount.insert(0,r)
                        
                        
                        time.sleep(1)
                        if len(entcount.get())==1:
                               list.append(entcount.get()+'        '+a[z])
                        if len(entcount.get())==2:
                               list.append(entcount.get()+'       '+a[z])
                        if len(entcount.get())==3:
                               list.append(entcount.get()+'      '+a[z])
                    
                    
                    except:
                        cmd.set("suspend_updates",0,quiet=1)
                        skipping = False
                        self.motifdrop.setlist(list)
                        list.sort()
        
        self.motifdrop = Pmw.ScrolledListBox(interior,
                    items=(),
                    dblclickcommand = self.runcusmotif,
                    listbox_height = 6,
                    usehullsize = 1,
                    hull_width = 300,
                    hull_height = 150,)
        self.motifdrop.grid(row=2, column =0)
        
        def loadmotifer():
            try:
                ###mRN = motif resn number aka number of residues in motif
                premRN = askstring('Motif Maker','How many residues are in your motif?\n'
                                                  +'Please enter a number >= 2 and <=10.\n')
                if premRN == None:
                    raise Exception
                else:
                    mRN = int(premRN)
                if mRN < 2 or mRN > 10:
                    raise ValueError
                
                def populate_chain_list():
                    items=[]
                    items.append('')
                    for letter in AlphaSequence:
                        if cmd.count_atoms("chain "+letter) > 0:
                            items.append(letter)
                    items.sort()
                    for i in range(1,mRN+1):
                        chain[i].setitems(items)
                
                def makemotif():
                    try:
                        exception = False
                        excepLoop = 0
                        exceptions = ''
                        skip = {}
                        skip[0] = 0
                        for i in range(1,mRN+1):
                            skip[i] = False
                            if resn[i].getvalue() == '' and resi[i].get() != '':
                                exception = True
                                exceptions += 'Please enter a residue for residue %s\n'%(i)
                            elif resn[i].getvalue() != '' and resi[i].get() == '':
                                exception = True
                                exceptions += 'Please enter a number for residue %s\n'%(i)
                            elif resn[i].getvalue() == '' and resi[i].get() == '':
                                ### this gives us the ability to skip whole blocks
                                skip[i] = True
                                skip[0] += 1
                            else:
                                excepLoop +=1
                                if chain[i].getvalue() == '':
                                    exception = True
                                    exceptions += 'Please select a chain for residue %s\n.'%(i)
                                elif resn[i].getvalue() == "gly" and backbone[i].getvalue() == "Off":
                                    exception = True
                                    exceptions += 'Please turn on the backbone for glycine residue %s\n'%(i)
                                elif cmd.count_atoms(chain[i].getvalue()+'/'+resn[i].getvalue()+'`'+resi[i].get()+'/') == 0:
                                    exception = True
                                    exceptions += 'There is no '+resn[i].getvalue()+' at number '+resi[i].get()+' on chain '+chain[i].getvalue()+'.\n'
                        if excepLoop < 2:
                            exception = True
                            exceptions += 'Motifs require that 2 or more residues be entered.'
                        if exception == True:
                            
                            showinfo('Error', 'The following errors have occurred:\n'+exceptions)
                            interior.mainloop()
                        else:
                            cmd.remove('resn HOH')
                            
                            Q = asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                            if Q == None:
                                interior.mainloop()
                            f=open(Q, 'w')
                            f.write("######################################################################\n")
                            f.write("### This motif uses shortened selection algebra and property selectors\n")
                            f.write("### + = and\n")
                            f.write("### w. = within\n")
                            f.write("### br. = byres\n")
                            f.write("### r. = resn\n")
                            f.write("### n. = name\n")
                            f.write("### e. = elem\n")
                            f.write("######################################################################\n")
                            atomlist = {}
                            ### backbone off aka just side chains from beta carbon onwards
                            atomlist[0] = {'ala':('CB'),
                                           'arg':('CB','CG','CD','NE','CZ','NH1','NH2'),
                                           'asn':('CB','CG','OD1','ND2'),
                                           'asp':('CB','CG','OD1','OD2'),
                                           'cys':('CB','SG'),
                                           'gln':('CB','CG','CD','OE1','NE2'),
                                           'glu':('CB','CG','CD','OE1','OE2'),
                                           'gly':(),
                                           'his':('CB','CG','ND1','CD2','CE1','NE2'),
                                           'ile':('CB','CG1','CG2','CD'),
                                           'leu':('CB','CG','CD1','CD2'),
                                           'lys':('CB','CG','CD','CE','NZ'),
                                           'met':('CB','CG','SD','CE'),
                                           'phe':('CB','CG','CD1','CD2','CE1','CE2','CZ'),
                                           'pro':('CB','CG','CD'),
                                           'ser':('CB','OG'),
                                           'thr':('CB','OG1','CG2'),
                                           'trp':('CB','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'),
                                           'tyr':('CB','CG','CD1','CD2','CE1','CE2','CZ','OH'),
                                           'val':('CB','CG1','CG2')}
                            atomlist[1] = ('O','C','CA','N')### backbone on
                            resnlist = ['']### residue list
                            resnlistf = ['']### residue list with appended 'i', making them unique
                            resilist = ['']### residue id list. Based on sequence number.
                            chainlist = ['']### chain list
                            bonelist = ['']### backbone list
                            
                            numOfi = 0
                            for i in range(1,mRN+1):
                                if skip[i] == False:
                                    resnlist.append(resn[i].getvalue())
                                    resilist.append(resi[i].get())
                                    resnlistf.append(resn[i].getvalue()+('i'*(numOfi)))
                                    chainlist.append(chain[i].getvalue())
                                    bonelist.append(backbone[i].getvalue())
                                    numOfi += 1
                            
                            ### This loop will increment through the amino acids. The amino acid we are looking
                            ### at right now is specified by the e variable. The a variable will count the
                            ### number of times it is compared to the carbons in the other amino acids. And is
                            ### used later on to print the "byres" and select line, and delete line below.
                            ### NOTE:
                            ### Because we are able to skip a whole block, mRN is not used beyond this point,
                            ### instead resnlen is used as it gives a more accurate picture of the motif.
                            resnlen = (len(resnlist)-1)
                            e = 0
                            while e < resnlen:
                                try:
                                    try:
                                        a = 0
                                        e += 1
                                        ### select stuff explained later on
                                        selectlimit = 200
                                        selectstart = 1 ### where to start selection
                                        selectlimiter = 1 ### limit defined as a/200
                                        selectextra = '' ### add to selection at the end
                                        deleteextra = '' ### add to deletion at the end
                                        
                                        if bonelist[e] == 'Off':###just sidechains
                                            bList=atomlist[0][resnlist[e]]
                                        else:### sidechain with backbone
                                            bList=atomlist[0][resnlist[e]]+atomlist[1]
                                        
                                        ### This loop will increment through the amino acids that we want
                                        ### to compare to the amino acid we want to find. The amino acid
                                        ### being compared is specified by the d variable.
                                        d = 0
                                        while d < resnlen:
                                            try:
                                                d += 1
                                                ### The following line: compare amino acids
                                                ### If they are the same, then lets increment one.
                                                if resnlistf[e] == resnlistf[d]:
                                                    d += 1
                                                    if d > resnlen:
                                                        continue
                                                
                                                if bonelist[d] == 'Off':###just sidechains
                                                    cList=atomlist[0][resnlist[d]]
                                                else:### sidechain with backbone
                                                    cList=atomlist[0][resnlist[d]]+atomlist[1]
                                                
                                                ### This loop increments through all the carbons
                                                ### in the amino acid we want to find.
                                                blen = (len(bList)-1)
                                                clen = (len(cList)-1)
                                                b = -1
                                                while b < blen:
                                                    b += 1
                                                    ### This loop increments through all the carbons
                                                    ### in the other amino acids that we are want to
                                                    ### compare with.
                                                    c = -1
                                                    while c < clen:
                                                        try:
                                                            c += 1
                                                            
                                                            ### Okay lets get the distance between our atoms in our selected amino acids.
                                                            r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+bList[b],chainlist[d]+'/'+resilist[d]+'/'+cList[c])
                                                            ### The precision factor
                                                            ### The ranger is the slider that is moved.
                                                            ### r is set by the get_distance above.
                                                            g = '%.2f' %(float(r) + float(ranger1.get()))
                                                            
                                                            a += 1
                                                            
                                                            ### apparently pymol cannot handle over a number
                                                            ### between 248 and 264 selections at one time.
                                                            ### This fixes that by making sure we do not pass
                                                            ### "selectlimit" selections at one time.
                                                            if float(selectlimiter) < (float(a)/float(selectlimit)):
                                                                f.write("cmd.select('"+resnlistf[e]+str(selectlimiter*selectlimit)+"','")
                                                                for i in range(selectstart,a):
                                                                    if i==(a-1):
                                                                        f.write("br. "+resnlistf[e]+str(i)+"')\n")
                                                                    else:
                                                                        f.write("br. "+resnlistf[e]+str(i)+" and ")
                                                                f.write("cmd.delete('")
                                                                for i in range(selectstart,a):
                                                                    if i==(a-1):
                                                                        pass
                                                                    elif i==(a-2):
                                                                        f.write(resnlistf[e]+str(i)+"')\n")
                                                                    else:
                                                                        f.write(resnlistf[e]+str(i)+"+")
                                                                selectextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+' and '
                                                                deleteextra += ''+resnlistf[e]+str(selectlimiter*selectlimit)+'+'
                                                                selectlimiter += 1
                                                                selectstart += selectlimit
                                                            
                                                            ### e > d is all the combinations of residues
                                                            ### that would already have one of the residues
                                                            ### found in the motif, therefore the second
                                                            ### amino acid does not need an r. (resn)
                                                            ### property selection, as it is already a selection.
                                                            if e > d:
                                                                f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and '+resnlistf[d]+'"%('+g+'))\n')
                                                                continue
                                                            else:
                                                               f.write( 'cmd.select("'+resnlistf[e]+''+str(a)+'", "n. '+bList[b]+' and r. '+resnlist[e]+' w. %s of n. '+cList[c]+' and r. '+resnlist[d]+'"%('+g+'))\n')
                                                               continue
                                                        except:
                                                            pass
                                            except:
                                                pass
                                    except:
                                        pass
                                finally:
                                    f.write('cmd.select("'+resnlistf[e]+'","')
                                    if selectextra != '':
                                        f.write(selectextra)
                                    for i in range(selectstart,a+1):
                                        if i==a:
                                            f.write('br. '+resnlistf[e]+str(i)+'")\n')
                                        else:
                                            f.write('br. '+resnlistf[e]+str(i)+' and ')
                                    f.write('cmd.delete("')
                                    if deleteextra != '':
                                        f.write(deleteextra)
                                    for i in range(selectstart,a+1):
                                        if i==a:
                                            f.write(resnlistf[e]+str(i)+'")\n')
                                        else:
                                            f.write(resnlistf[e]+str(i)+'+')
                        
                        resnlistfstr = ""
                        for i in range(1,resnlen+1):
                            if i == resnlen:
                                resnlistfstr += resnlistf[i]
                            else:
                                resnlistfstr += resnlistf[i]+'+'
                        
                        f.write("cmd.select('Motif','"+resnlistfstr+"')\n")
                        f.write("cmd.delete('"+resnlistfstr+"')\n")
                        f.write('cmd.hide("everything","all")\n')
                        f.write('cmd.show("cartoon", "all")\n')
                        f.write('cmd.set("cartoon_transparency","0.5", "all")\n')
                        f.write('cmd.show("sticks","Motif")\n')
                        f.write('cmd.color("grey","all")\n')
                        f.write('cmd.color("oxygen","(e. O+Motif)")\n')
                        f.write('cmd.color("nitrogen","(e. N+Motif)")\n')
                        f.write('cmd.color("sulfur","(e. S+Motif)")\n')
                        f.write('cmd.color("hydrogen","(e. H+Motif)")\n')
                        f.write('cmd.color("white","(e. C+Motif)")\n')
                        f.write('cmd.deselect()\n')
                        f.write('cmd.orient("Motif")\n')
                        
                        print '\n\n\n\n\n\nMotif Maker\nBy: Brett Hanson and Charlie Westin\n2007\nImproved by: Mario Rosa\n2009\n%s Amino Acid Motif Written \n\n\n\n'%(len(resnlist)-1)
                        f.close()
                        interior.mainloop()
                    except:
                        pass
                
                root = Tk()
                group = Pmw.Group(root, tag_text='Motif Maker')#And a new group
                group.grid(row=0, column=0, padx=0, pady=0, sticky=NW)
                interior = group.interior()
                
                resn = {}
                for i in range(1,mRN+1):
                    resn[i] = Pmw.OptionMenu(interior,labelpos = 'w',
                                                label_text = 'Residue %s:'%(i),
                                                items = AminoMenuList,
                                                menubutton_width = 8)
                    resn[i].grid(row = (i-1), column =0)
                
                lent = {}
                for i in range(1,mRN+1):
                    lent[i] = Label(interior, text = 'Number:')
                    lent[i].grid(row = (i-1), column =1)
                
                resi = {}
                for i in range(1,mRN+1):
                    resi[i] = Entry(interior, width = 8)
                    resi[i].grid(row = (i-1), column =2)
                
                backbone = {}
                for i in range(1,mRN+1):
                    backbone[i] = Pmw.OptionMenu(interior,labelpos = 'w',
                                                 label_text = 'BackBone:',
                                                 items = ('Off', 'On'),
                                                 menubutton_width = 8)
                    backbone[i].grid(row = (i-1), column =3)
                
                chain = {}
                for i in range(1,mRN+1):
                    chain[i] = Pmw.OptionMenu(interior,labelpos = 'w',
                                                  label_text = 'Chain %s:'%(i),
                                                  items = (''),
                                                  menubutton_width = 8)
                    chain[i].grid(row=(i-1), column=4)
                
                but1 = Button(interior, text = 'Make Motif', width = 10, command = makemotif)
                but1.grid(row =mRN, column =3, sticky = 'se')
                
                popbtn = Button(interior, text = 'Chain Info', width = 10, command = populate_chain_list)
                popbtn.grid(row = mRN, column = 4, sticky = 'se')
                
                framerange = Frame(interior)
                framerange.grid(row=mRN, column=0,columnspan = 3, sticky = 'e')
                ballrange = Pmw.Balloon(interior)
                ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault = 2')
                ranger1 = Scale(framerange, width =8,
                                troughcolor="#ffffff",
                                length="160",
                                orient="horizontal",
                                resolution="0.1",
                                to="4.0")
                ranger1.grid(row=5, column=1,columnspan = 4, sticky = 'e')
                ranger1.set(2)
                
                labrange = Label(interior, text='Precision Factor:')
                labrange.grid(row=mRN, column=0, sticky='sw')
                
                group = Pmw.Group(root, tag_text = 'Run Motif')
                group.grid(row=1, column=0, padx=190, pady=0, sticky = 'NE')
                interior = group.interior()
                
                def getmotif():
                    
                    f = askopenfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                    if f == None:
                        interior.mainloop()
                    else:
                        cmd.do('run '+f+'')
                        interior.mainloop()
                openbtn = Button(interior, text= 'Open Motif', command = getmotif)
                openbtn.grid()
            
            #---------------------Show residues around active site---------------#
                def motifoption(tag):
                        if tag=='Surface Pocket':
                            objects = cmd.get_names('all')
                            cmd.set('transparency', '0.5', 'all')
                            if 'Motif' in objects:
                                cmd.show('surface', 'all')
                                cmd.hide('cartoon', 'all')
                                cmd.color('white', '!Motif ')
                        elif tag=='Polar Contacts':
                                try:
                                    objects = cmd.get_names('all')
                                    cmd.dist("Motif_polar_conts","Motif","Motif",quiet=1,mode=2,label=0,reset=1)
                                    cmd.enable(self.mot+"_polar_conts")
                                except:
                                    pass
                                
                                if 'Adjacent' in objects:
                                    cmd.dist('Adjacent_polar_conts','Adjacent','Adjacent',quiet=1,mode=2,label=0,reset=1)
                                if 'substrate' in objects:
                                    cmd.dist("Motif_around_polar_conts","Motif","(byobj (Motif)) and (not (Motif))",quiet=1,mode=2,label=0,reset=1)
                                    cmd.enable("Motif_around_polar_conts")
                        elif tag=='Hide Contacts':
                            objects = cmd.get_names('all')
                            try:
                                  try:
                                    cmd.delete("Motif_polar_conts")
                                  except:
                                    pass
                                  if 'Adjacent' in objects:
                                    cmd.delete('Adjacent_polar_conts')
                                  if 'substrate' in objects:
                                    cmd.delete("substrate_polar_conts")
                            except:
                                  
                                  showinfo('Alert', "No motif polar contacts to hide")
                        elif tag=='Show Substrate':
                            try:
                              cmd.select('substrate', 'byres het within 7 of  Motif')
                              objects = cmd.get_names('all')
                              xp = cmd.index('substrate')
                              np  = len(xp)
                              if(np < 1):
                                  cmd.delete('substrate')
                              if 'substrate' in objects:
                                  cmd.show('sticks', 'substrate')
                                  cmd.deselect()
                                  cmd.color("oxygen","(elem O and substrate)")
                                  cmd.color("nitrogen","(elem N and substrate)")
                                  cmd.color("sulfur","(elem S and substrate)")
                                  cmd.color("hydrogen","(elem H and substrate)")
                                  cmd.color("white","(elem C and substrate)")
                            except:
                                
                                showinfo('Alert', "No substrate found")
                        elif tag=='Show label':
                         objects = cmd.get_names('all')
                         try:
                                      cmd.label('''(name ca+C1*+C1' and (byres(Motif)))''','''"%s-%s"%(resn,resi)''')
                                      if 'Adjacent' in objects:
                                             cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''','''"%s-%s"%(resn,resi)''')
                         except:
                                    
                                    showinfo('Alert', "Select a motif first")
                        elif tag=='Hide Label':
                            objects = cmd.get_names('all')
                            try:
                                  cmd.label("Motif","''")
                                  if 'Adjacent' in objects:
                                      cmd.label('byres Adjacent',"''")
                            except:
                                    
                                    showinfo('Alert', "No motif labels to hide")
                        elif tag=='Hide Substrate':
                                          try:
                                            cmd.hide('sticks', 'substrate')
                                          except:
                                            
                                            showinfo('Alert', "No substrate selected")
                stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos = 'w',
                            items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                            menubutton_width = 8, command=motifoption)
                stereo.grid(row=0,column=3,sticky=NW)
                
                group = Pmw.Group(root, tag_text='Adjacent')
                group.grid(row=1, column=0, columnspan=1, padx=2, pady=2, sticky=W)
                
                interior = group.interior()
                framesela = Frame(interior)
                framesela.grid(row=0, column=0, columnspan = 2, padx=0, pady=0, sticky=N)
                ballsela = Pmw.Balloon(interior)
                ballsela.bind(framesela, 'Within # Angstroms')
                selA = Scale(framesela, width =8)
                selA.configure(troughcolor="#ffffff")
                selA.configure(length="130")
                selA.configure(orient="horizontal")
                selA.configure(resolution="0.2")
                selA.configure(to="10.0")
                selA.grid(row=0, column=0, columnspan= 2, padx=0, pady=0, sticky=N)
                selA.set(5.0)
                frameadj = Frame(interior)
                frameadj.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
                balladj = Pmw.Balloon(interior)
                balladj.bind(frameadj, 'Display residues adjacent to motif')
                
                def roundres():
                    try:
                        cmd.hide('sticks', '!Motif')
                        cmd.color('white', '!Motif')
                        cmd.select('Adjacent', 'byres Motif around %s'%(selA.get()))
                        cmd.show('sticks', 'Adjacent')
                        cmd.color('orange', 'Adjacent')
                        util.cnc('Adjacent')
                        cmd.remove('hydro')
                        cmd.deselect()
                    except:
                        
                        showinfo('Alert', 'You must load a motif first')
                        interior.mainloop()
                showround = Button(frameadj, width = 12, text = 'Adjacent', command = roundres)
                showround.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
                
                def resdel():
                    try:
                        objects = cmd.get_names('all')
                        cmd.hide('sticks', '!Motif')
                        cmd.color('white', '!Motif')
                        if 'Adjacent' in objects:
                            cmd.delete('Adjacent_polar_conts')
                        if 'Adjacent' in objects:
                            cmd.label('byres Adjacent',"''")
                        cmd.delete('Adjacent')
                    except:
                        
                        showinfo('Alert', 'You must load a motif first')
                        interior.mainloop()
                delres = Button(interior, width = 14, text = 'Delete Adjacent', command = resdel)
                delres.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
            
            except ValueError:
                
                showinfo('Error', 'Please enter a number greater than or equal to 2.\n'
                                                                +'Please enter a number less than or equal to 10.')
                loadmotifer()
            except:
                pass
        
        nmlab = Label(interior, text = 'Motif Name')
        nmlab.grid(row=1, column =0, sticky = 'n')
        runbtn1 = Button(interior, text = 'Run all Motifs', command = runum)
        runbtn1.grid(row = 0, column =0, sticky = 'W')
        mobtn = Button(interior, text = 'Motif maker', command = loadmotifer)
        mobtn.grid(row = 0, column = 0, sticky = 'E')
        
        button333 =Button(interior, text = 'Get Random PDB', width =25, command = randomized)
        button333.grid(row = 3, column = 0, padx = 10, sticky = 'N')