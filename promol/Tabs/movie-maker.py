	page = notebook.add('movie\n maker')
notebook.tab('movie\n maker').focus_set()

#-----------Mouse Mode--------------
    group = Pmw.Group(page, tag_text='Mouse Mode:')
group.grid(row=1, column=0, padx=0, pady=0, sticky=NW)
    interior = group.interior()
    ddddd = Button(interior, width = 15, text = '3 Button Viewing')
    ddddd.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
    dddd = Button(interior, width = 15,text = '3 Button Editing')
    dddd.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
    fffff = Button(interior, width = 15,text = '2 Button Viewing')
    fffff.grid(row=2, column=0, padx=2, pady=2, sticky=NW)
    ffff = Button(interior, width = 15,text = '2 Button Selecting')
    ffff.grid(row=0, column=1, padx=2, pady=2, sticky=NW)
    fff = Button(interior, width = 15,text = '2 Button Editing')
    fff.grid(row=1, column=1, padx=2, pady=2, sticky=NW)
    ggggg = Button(interior, width = 15,text = '1 Button Viewing')
    ggggg.grid(row=2, column=1, padx=2, pady=2, sticky=NW)
    def tv(event):
      cmd.mouse('three_button_viewing')
    def te(event):
      cmd.mouse('three_button_editing')
    def dv(event):
      cmd.mouse('two_button_viewing')
    def ds(event):
      cmd.mouse('two_button_selecting')
    def de(event):
      cmd.mouse('two_button_editing')
    def ov(event):
      cmd.mouse('one_button_viewing')
    ddddd.bind('<Button-1>', tv)
    dddd.bind('<Button-1>', te)
    fffff.bind('<Button-1>', dv)
    ffff.bind('<Button-1>', ds)
    fff.bind('<Button-1>', de)
    ggggg.bind('<Button-1>', ov)

    
    
    #----------Load and Save Frame Group------------------#


group = Pmw.Group(page, tag_text='Load and Save:')
group.grid(row=0, column=0, padx=0, pady=0, sticky="NE")
    interior = group.interior()
    #------------File extension Selector---------------#
    
    filexlab = Label(interior, text = "File Extension:")
    filexlab.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
    entfilex = Entry(interior, width = 5)
    entfilex.grid(row=4, column=1, padx=5, pady=5, sticky=NW)
    entfilex.insert(0, ".pdb")
    
    #---------------Load Button and Function---------------------#


loadbtn1 = Button(interior, text = 'Load frame')
    loadbtn1.grid(row=2, column=0, padx=5, pady=5, sticky=NE)
    framelab = Label(interior, text = 'Frame:')
    framelab.grid(row=1, column=0, padx=5, pady=5, sticky=NE)
    enti = Entry(interior, width = 5)
    enti.insert(0,0)
    enti.grid(row=1, column=1, padx=5, pady=5, sticky=NW)
    entl = Entry(interior)
    entl.insert(0,0)
    def loadframe(event):
      a = int(entl.get()) + 1
      entl.delete(0,100000)
      entl.insert(0,a)
      
      
      if int(entl.get())<2:
        if askyesno('Load Frames', 'Click yes to load in discrete mode'):
            
            file = askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
            if len(file)>0:
              cmd.load(file, "mov", entl.get(), discrete=1)
 	    else:
            
            file = askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
            if len(file)>0:
              cmd.load(file, "mov", entl.get())
      else:
        
        file = askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
        if len(file)>0:
          cmd.load(file, "mov", entl.get())
      page.mainloop()
    
    loadbtn1.bind('<Button-1>', loadframe)
    #---------------Save Button------------------#
    
    savebtn = Button(interior, text = 'Save Frame')
    savebtn.grid(row=2, column=1, padx=5, pady=5, sticky=NW)
    
    labname = Label(interior, text = "Movie Title:")
    labname.grid(row=0, column=0, padx=5, pady=5, sticky=NE)
    name_mov = Entry(interior, width = 10)
    name_mov.grid(row=0, column=1, padx=5, pady=5, sticky=NW)
    #--------------------goto frame button and Function-----------#
    gotobtn = Button(interior, text = 'Go to Frame:')
    gotobtn.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    gotoent = Entry(interior, width = 10)
    gotoent.grid(row=3, column=1, padx=5, pady=5, sticky=NW)
    def gotoframe(event):
        try:
            cmd.frame(gotoent.get())
        except:
            
            showinfo('Alert!', 'You need to enter the frame number')
            interior.mainloop()
    gotobtn.bind('<Button-1>', gotoframe)
    
    #---------Save Function--------------------------#
    
    def molSave(self):
      try:
        try:
          import os
          os.mkdir('./modules/pmg_tk/startup/Movies/ ' + name_mov.get())
          a = int(enti.get()) + 1
          enti.delete(0,100000)
          enti.insert(0,a)
          
          file = asksaveasfilename(defaultextension=entfilex.get(), initialdir="./modules/pmg_tk/startup/Movies/ " + name_mov.get(), initialfile= "frame" + enti.get())
          if len(file)>0:
              cmd.save(file)
          page.mainloop()
        except:
          a = int(enti.get()) + 1
          enti.delete(0,100000)
          enti.insert(0,a)
          
          file = asksaveasfilename(defaultextension=entfilex.get(), initialdir="./modules/pmg_tk/startup/Movies/ " + name_mov.get(), initialfile= "frame" + enti.get())
          if len(file)>0:
              cmd.save(file)
        page.mainloop()
      except:
        
        
        showinfo("Error", 'Please enter a movie title')
    savebtn.bind('<Button-1>', molSave)
    
    #-----------Ray Trace Frames-----------
    #Self explanatory, and can save ray traced frames# as png images
    labels = ("Ray Trace Frames")
	self.ray = Pmw.RadioSelect(interior, labelpos='w', labelmargin=0,
		                   buttontype='checkbutton',orient='vertical',
		                   command=self.ray)
	self.ray.add("Ray Trace Frames")
	self.ray.grid(row=6, column=0, padx=5, pady=0, sticky=NE)
    
    mpngbtn = Button(interior, text = "Create PNGs")
    mpngbtn.grid(row=6, column=1, padx=5, pady=0, sticky=NW)
    def mping(event):
            cmd.mpng(name_mov.get(), first=0, last=0 )
    mpngbtn.bind('<Button>', mping)

    
    
    #----------Clearing Ram Button and Function----
    
    clearbtn = Button(interior, text = "Clear Ram")
    clearbtn.grid(row=7, column=1, padx=5, pady=3, sticky=NW)
    def clearram(event):
      cmd.mclear()
    clearbtn.bind('<Button-1>', clearram)
    
    #-----Cache off button and Function-----------
    
    labels = ("Frame Cache Off")
	self.cache = Pmw.RadioSelect(interior, labelpos='w', labelmargin=0,
		                   buttontype='checkbutton',orient='vertical',
		                   command=self.cacheframe)
	self.cache.add("Frame Cache Off")
	self.cache.grid(row=7, column=0, padx=5, pady=0, sticky=NE)
    
    #------------Scripted Animation GUI ----------#
	#Used for easier creation of movies, utilizing buttons
	#instead of the necessity to input Pymol commands constantly
    
    group = Pmw.Group(page, tag_text='Scripted Animation:')
group.grid(row=0, column=1, padx=0, pady=0, sticky="NW")
    interior = group.interior()
    labscrp = Label(interior, text = "Frames in Movie:")
    labscrp.grid(row = 0, column=0, padx=5, pady=5, sticky = NE)
    fent = Entry(interior, width = 8)
    fent.grid(row = 0, column=1, padx=5, pady=5, sticky = NW)
    makmovframe = Frame(interior)
    makmovframe.grid(row = 0, column=2, padx=5, pady=3, sticky = NW)
    makball = Pmw.Balloon(interior)
    makball.bind(makmovframe, 'Set the number of movie frames FIRST')
    makmov = Button(makmovframe, text = "set movie")
    makmov.grid(row = 0, column=2, padx=5, pady=3, sticky = NW)
    def makmovie(event):
        try:
            cmd.mset("1 -"+ fent.get())
            scriptent.delete(0,100000000)
            scriptent.insert(0,0)
        except:
            
            showinfo('Alert!', 'Enter the amount of frames to be in the movie')
            interior.mainloop()
    makmov.bind('<Button-1>', makmovie)
    interior = group.interior()
    labscrp = Label(interior, text = "Frame:")
    labscrp.grid(row = 1, column=0, padx=5, pady=5, sticky = NE)
    scriptent = Entry(interior, width = 8)
    scriptent.grid(row = 1, column=1, padx=5, pady=5, sticky = NW)
    scriptent.insert(0,0)
    labmx = Button(interior, text = "Move X:")
    labmx.grid(row = 2, column=0, padx=5, pady=5, sticky = NE)
    entmx = Entry(interior, width = 6)
    entmx.grid(row = 3, column=0, padx=5, pady=5, sticky = NE)
    labmy = Button(interior, text = "Move Y:")
    labmy.grid(row = 2, column=1, padx=5, pady=5, sticky = NW)
    entmy = Entry(interior, width = 6)
    entmy.grid(row = 3, column=1, padx=5, pady=5, sticky = NW)
    labmz = Button(interior, text = "Move Z:")
    labmz.grid(row = 2, column=2, padx=5, pady=5, sticky = NW)
    entmz = Entry(interior, width = 6)
    entmz.grid(row = 3, column=2, padx=5, pady=5, sticky = NW)
    labtx = Button(interior, text = "Turn X:")
    labtx.grid(row = 4, column=0, padx=5, pady=5, sticky = NE)
    enttx = Entry(interior, width = 6)
    enttx.grid(row = 5, column=0, padx=5, pady=5, sticky = NE)
    labty = Button(interior, text = "Turn Y:")
    labty.grid(row = 4, column=1, padx=5, pady=5, sticky = NW)
    entty = Entry(interior, width = 6)
    entty.grid(row = 5, column=1, padx=5, pady=5, sticky = NW)
    labtz = Button(interior, text = "Turn Z:")
    labtz.grid(row = 4, column=2, padx=5, pady=5, sticky = NW)
    enttz = Entry(interior, width = 6)
    enttz.grid(row = 5, column=2, padx=5, pady=5, sticky = NW)
     #-----Movie translation functions, providing specification
    #of xyz coordinate translation of proteins and/or molecules
    def movsetx(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "move x," + entmx.get())
    labmx.bind('<Button-1>', movsetx)
    def movsety(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "move y," + entmy.get())
    labmy.bind('<Button-1>', movsety)
    def movsetz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "move z," + entmz.get())
    labmz.bind('<Button-1>', movsetz)
    def tursetx(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "turn x," + enttx.get())
    labtx.bind('<Button-1>', tursetx)
    def tursety(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "turn y," + entty.get())
    labty.bind('<Button-1>', tursety)
    def tursetz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "turn z," + enttz.get())
    labtz.bind('<Button-1>', tursetz)
    def tursetz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(),  "turn z," + enttz.get())
    labtz.bind('<Button-1>', tursetz)
    def movsetxyz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(), "move x, %s; move y, %s; move z, %s" % (entmx.get(),entmy.get(),entmz.get()))
    labmxyz = Button(interior, text = "Move All:")
    labmxyz.grid(row = 6, column=0, padx=5, pady=5, sticky = NE)
    labmxyz.bind('<Button-1>', movsetxyz)
    def tursetxyz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(), "turn x, %s; turn y, %s; turn z, %s" % (enttx.get(),entty.get(),enttz.get()))
    labtxyz = Button(interior, text = "Turn All:")
    labtxyz.grid(row = 6, column=1, padx=5, pady=5, sticky = NW)
    labtxyz.bind('<Button-1>', tursetxyz)
    def tursetxyzmovsetxyz(event):
        a = int(scriptent.get()) +1
        scriptent.delete(0,100000)
        scriptent.insert(0,a)
        cmd.mdo( scriptent.get(), "turn x, %s; turn y, %s; turn z, %s; move x, %s; move y, %s; move z, %s" % (enttx.get(),entty.get(),enttz.get(),entmx.get(),entmy.get(),entmz.get()))
    labtxyz = Button(interior, text = "Do All:")
    labtxyz.grid(row = 6, column=2, padx=5, pady=5, sticky = NW)
    labtxyz.bind('<Button-1>', tursetxyzmovsetxyz)
    
    #--------------Selection Controls--------------------
    #---This creates frames, and thusly the ability to add
    #---Balloon pop up help for mask/protect buttons-----
    group = Pmw.Group(page, tag_text='Selection Controls')
    group.grid(row=1, column=1, padx=0, pady=0, sticky=SW)
    interior = group.interior()
    framemaskbtn = Frame(interior)
    framemaskbtn.grid(row=1, column=0, padx=2, pady=1, sticky=NW)
    ballmaskbtn = Pmw.Balloon(interior)
    ballmaskbtn.bind(framemaskbtn, "This will mask a named selection\nand prevent it from being\nmodified or moved at all.")
    framemaskaebtn = Frame(interior)
    framemaskaebtn.grid(row=2, column=0, padx=2, pady=1, sticky=NW)
    ballmaskaebtn = Pmw.Balloon(interior)
    ballmaskaebtn.bind(framemaskaebtn, "This will mask all objects except the named selection\nand prevent them from being\nmodified or moved at all.")
    frameunmaskbtn = Frame(interior)
    frameunmaskbtn.grid(row=3, column=0, padx=2, pady=1, sticky=NW)
    ballunmaskbtn = Pmw.Balloon(interior)
    ballunmaskbtn.bind(frameunmaskbtn, "This will unmask a masked selection\nallowing modifications.")
    frameprotectbtn = Frame(interior)
    frameprotectbtn.grid(row=1, column=1, padx=2, pady=1, sticky=NW)
    ballprotectbtn = Pmw.Balloon(interior)
    ballprotectbtn.bind(frameprotectbtn, "This will protect a named selection\nand prevent it from being moved.\nBut it can still be modified.\nRecommended for only advanced users.")
    framedeprotectbtn = Frame(interior)
    framedeprotectbtn.grid(row=3, column=1, padx=2, pady=1, sticky=NW)
    balldeprotect = Pmw.Balloon(interior)
    balldeprotect.bind(framedeprotectbtn, "This will deprotect a protected selection\nallowing it to be moved.")
    frameprobtn = Frame(interior)
    frameprobtn.grid(row=2, column=1, padx=2, pady=1, sticky=NW)
    ballprotbtn = Pmw.Balloon(interior)
    ballprotbtn.bind(frameprobtn, "This will protect all objects excecpt the named selection\nand prevent it from being moved.\nBut it can still be modified.\nRecommended for only advanced users.")
    maskbtn = Button(framemaskbtn, text = 'Mask Selection',width = 15)
    maskbtn.grid(row=1, column=0, padx=2, pady=1, sticky=NW)
    unmaskbtn = Button(frameunmaskbtn, text = 'Unmask Selection',width = 15)
    unmaskbtn.grid(row=3, column=0, padx=2, pady=1, sticky=NW)
    maskaebtn = Button(framemaskaebtn, text = 'Mask All Except',width = 15)
    maskaebtn.grid(row=2, column=0, padx=2, pady=1, sticky=NW)
    probtn = Button(frameprobtn, text = 'Protect All Except',width = 15)
    probtn.grid(row = 2, column =1, padx=2, pady=1, sticky=NW)
    protectbtn= Button(frameprotectbtn, text = 'Protect Selection',width = 15)
    protectbtn.grid(row=1, column=1, padx=2, pady=1, sticky=NW)
    deprotectbtn = Button(framedeprotectbtn, text = 'Deprotect Selection',width = 15)
    deprotectbtn.grid(row=3, column=1, padx=2, pady=1, sticky=NW)
    maskent = Entry(interior, width = 10)
    maskent.grid(row=0, column=1, padx=2, pady=1, sticky=NW)
    labby21 = Label(interior, text = 'Name:')
    labby21.grid(row=0, column=0, padx=2, pady=1, sticky=NE)
     #------Masking and protecting functions, prevents manipulation-----
    #------of specified selections, although protect function not------
    #------well documented, and for advanced users only------------
    def maskedman(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.mask(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    
    def unmaskedman(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.unmask(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    def maskallexcept(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.mask('All')
            cmd.unmask(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    cmd.extend('maskallexcept',maskallexcept)
    def protectallexcept(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.protect('All')
            cmd.deprotect(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    def protectme(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.protect(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    def deprotectme(event):
        try:
          if len(maskent.get()) < 1:
            
            
            showinfo("Error", 'Please enter the name of an object.')
            interior.mainloop()
          else:
            cmd.deprotect(maskent.get())
        except:
            
            
            showinfo("Error", 'That object is not present')
        interior.mainloop()
    maskbtn.bind('<Button-1>', maskedman)
    unmaskbtn.bind('<Button-1>', unmaskedman)
    maskaebtn.bind('<Button-1>', maskallexcept)
    protectbtn.bind('<Button-1>', protectme)
    deprotectbtn.bind('<Button-1>', deprotectme)