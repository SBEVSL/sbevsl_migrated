    # Add "Settings" tab to notebook
    page = notebook.add('EZ-Viz')
    
    #------Write Script Out-------------
    
    scriptwrite = Pmw.OptionMenu(page,label_text = 'Script Writing:',labelpos = 'n',
            items = ("Off", "On"),
            menubutton_width = 11, command=write_script)
    scriptwrite.grid(row=5,column=0,sticky=NW)
    
    group = Pmw.Group(page, tag_text='Run Script')
    group.grid(row=5, column=0, padx=8, pady=0, sticky = N)
    interior = group.interior()
    scriptbutton = Button(interior, width = 10, text = 'Run Script')
    scriptbutton.grid()
    
    
    loaderent = Entry(interior, width = 7)
    
    def loadlog(event):
      loaderent.delete(0, 1000)
      
      file = askopenfilename(defaultextension=".pml")
      loaderent.insert(0, file)
      cmd.do('@'+loaderent.get())
      page.mainloop()
    
    scriptbutton.bind('<Button-1>', loadlog)
    
    #------------ Presets Group  ---------------
    group = Pmw.Group(page, tag_text='Preset Views')
    group.grid(row=0, column=0, padx=0, pady=0)
    
    interior=group.interior()
    
    #menus for presets
    
    surface = Pmw.OptionMenu(interior,label_text = 'Surfaces:',labelpos = 'n',
                             items = ('','Surface','Surface on Cartoon','Surface on Sticks',
                                      'Surface on Spheres', 'Mesh on Sticks', 'Dots on Lines'),
                             menubutton_width = 10, command=self.presurf)
    surface.grid(row=0,column=0,sticky=NW)
    
    cartoon = Pmw.OptionMenu(interior,label_text = 'Cartoons:',labelpos = 'n',
                items = ('','Cartoon','Putty','Lines on Cartoon', 'Color by Chain'),
                menubutton_width = 10, command=self.pretoon)
    cartoon.grid(row=0,column=1,sticky=NW)
    
    residue = Pmw.OptionMenu(interior,label_text = 'By Residue:',labelpos = 'n',
                             items = ('','Aromatics','Show Charged','Solubility'),
                             menubutton_width = 10, command=self.preres)
    residue.grid(row=0,column=2,sticky=NW)
    
    roving = Pmw.OptionMenu(interior,label_text = 'Roving:',labelpos = 'n',
                            items = ('','Roving Sticks','Roving Ball&Sticks','Roving Spheres', 'Roving Lines'),
                            menubutton_width = 10, command=self.prerov)
    roving.grid(row=1,column=2,sticky=NW)
    
    elecdensity = Pmw.OptionMenu(interior,label_text = 'Electron Density:',labelpos = 'n',
                                 items = ('','Mesh on Ribbon','Dots on Sticks','Surface on Lines'),
                                 menubutton_width = 10, command=self.preele)
    elecdensity.grid(row=1,column=1,sticky=NW)
    
    misc = Pmw.OptionMenu(interior,label_text = 'Miscellaneous:',labelpos = 'n',
                          items = ('','Hetero Atoms','Chain Contacts','DNA & RNA','CPK','Ball & Stick'),
                          menubutton_width = 10, command=self.premisc)
    misc.grid(row=1,column=0,sticky=NW)
    
    #roving slider
    
    self.rovingradius2 = Scale(interior, width =8)
    self.rovingradius2.configure(showvalue="0")
    self.rovingradius2.configure(troughcolor="#ffffff")
    self.rovingradius2.configure(length="90")
    self.rovingradius2.configure(orient="horizontal")
    self.rovingradius2.configure(resolution="0.1")
    self.rovingradius2.configure(to="15.0")
    self.rovingradius2.grid(row=1, column=3, padx=0, pady=0, sticky=S)
    self.rovingradius2.set(8.0)
    labelradius = Label(interior, text = 'Roving Detail')
    labelradius.grid(row=1, column=3, padx=0, pady=0, sticky=N)

#preset movies dropdown
    
    movies = Pmw.OptionMenu(interior,label_text = 'Preset Movies:',labelpos = 'n',
                items = ('','Ligand Zoom','Build Protein','Highlight Chains','Rotate','Chain Pull', 'Ligand Pull', 'Surface to Stick', 'Surface to Cartoon', 'Play', 'Stop', 'Rewind'),
                menubutton_width = 10, command=self.premovie)
    movies.grid(row=0,column=3,sticky=NW)
    
    
    #---------------Version 1-----------------#

    
    
    #------------ Display Group ----------------#
    #                                                                           #
    #                                                                           #
    #-------------------------------------------#
    
    
    group = Pmw.Group(page, tag_text='Display Options')
    group.grid(row=4, column=0, columnspan=2, padx=0, pady=0)
    self.int=group.interior()
    
    
    # menu for stereo options
    stereo = Pmw.OptionMenu(self.int,label_text = 'Stereo:',labelpos = 'n',
                items = ("Off", "Quad", "Cross-Eye", "Wall-Eye"),
                menubutton_width = 11, command=self.stereo_switch)
    stereo.grid(row=0,column=0,sticky=NW)
    
    
    # menu for background color changes
    stereo = Pmw.OptionMenu(self.int,label_text = 'Background Color:',labelpos = 'n',
                items = ("Black", "White", "Grey", "Other"),
                menubutton_width = 11, command=self.bgcolor_switch)
    stereo.grid(row=0,column=1,sticky=NW)
    
    # menu for background color changes
    stereo = Pmw.OptionMenu(self.int,label_text = 'Color Space:',labelpos = 'n',
                items = ("PyMOL", "Publications", "Video/Web"),
                menubutton_width = 11, command=self.cspace_switch)
    stereo.grid(row=0,column=2,sticky=NW)
    
    # menu for hide/show interface
    stereo = Pmw.OptionMenu(self.int,label_text = 'Internal GUI:',labelpos = 'n',
                items = ("Show", "Hide"),
                menubutton_width = 11, command=self.hide_interface)
    stereo.grid(row=0,column=3,sticky=NW)




#----------------Version 2------------#
    
    
    # AUTOMATED COMMANDS TAB
    group = Pmw.Group(page, tag_text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)
    interior = group.interior()
    popbtn=Button(interior, text='Update Selection',width=15)
    popbtn.place(x=50, y=32)
    popbtn.bind('<Button-1>', populater)
    
    #-------------Version 1---------------#
    selection = Pmw.OptionMenu(interior,labelpos = 'w',
               label_text = 'Select:',
                items = (''),
                menubutton_width = 10, command = self.set_sel)
    selection.grid(row=0, column=0, padx=8, pady=0)

    
    
    self.viewOptions = Pmw.OptionMenu(interior, labelpos='w',
		label_text = 'Show:',
		items = ('Lines', 'Sticks', 'Ribbons','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water', 'Everything', 'Polar Contacts'),
		menubutton_width=10, command=self.show_rep)

self.viewOptions.grid(row=0,column=1,padx=0,pady=0,sticky='N')

self.hideOptions = Pmw.OptionMenu(interior, labelpos='w',
		label_text = 'Hide:',
		items = ('Lines', 'Sticks', 'Ribbons','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water','Everything', 'Polar Contacts'),
		menubutton_width=10, command=self.hide_rep)

self.hideOptions.grid(row=1,column=1,padx=0,pady=0, sticky='SE')

# Coloring choices
selection = Pmw.OptionMenu(interior,labelpos = 'w',
               label_text = 'Color:',
                items = ('Red','Green','Blue','Orange','Violet','Yellow','CPK','Other'),
                menubutton_width = 7, command = self.color_sel)
    
    selection.grid(row=0, column=2, padx=0, pady=0)
     
     # MANUAL COMMANDS SECTION
    group = Pmw.Group(page, tag_text='Manual Commands')
    group.grid(row=3,column=0, padx=0,pady=0)
    interior = group.interior()
    
    labels = ('PyMOL','Chime')
    self.commandChooser = self.radioAdd(interior,'w','vertical',self.set_cmd_type,'Command Type:',labels, 0,
                                        0, 1, 1, 'W')
    
    self.output = Pmw.ScrolledText(interior,
                                   usehullsize = 1,
                                   hull_width = 250,
                                   hull_height = 50,
                                   text_wrap= WORD)
    
    self.output.grid(row=0,column=1,padx=8,pady=2)
    self.output.setvalue('Command results will show in this box.\n\n')
    
    # PyMOL Command Prompt
    self.commandLine = Pmw.EntryField(interior, labelpos='w', label_text='Command Line:',
                                      value='Enter PyMOL Commands Here', entry_width=25, command=self.command_line)
    self.commandLine.grid(row=1, column=0, columnspan=2, pady=2)