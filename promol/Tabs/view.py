    page = notebook.add('View\nOptions')
    notebook.tab('View\nOptions').focus_set()
    
    group = Pmw.Group(page, tag_text = 'Automated Commands')
    group.grid(row=2, column=0, padx=0, pady=0)
    interior = group.interior()


    
    
    popbtn=Button(page, text='Update Selection')
    popbtn.grid(row = 0, column = 0, sticky='E')
    popbtn.bind('<Button-1>', populater)


#-------------- Selection Dropdown -----------------
    self.advancedSelection = Pmw.OptionMenu(page,label_text = 'Select:',labelpos = 'w',
                items = (''),
                menubutton_width = 10, command = self.set_sel1)
    
    self.advancedSelection.grid(row=0, column=0,sticky=NW)

#--------------- Setting Defaults -----------------
defaults = Pmw.OptionMenu(page,label_text = 'Reset:',labelpos = 'w',
                items = ('Cartoon', 'Spheres', 'Sticks','Surface', 'Ambient'),
                menubutton_width = 10, command=self.set_advanced_defaults)
    defaults.grid(row=0,column=1,sticky=NW)

#--------------- Cartoon Group----------------
group = Pmw.Group(page, tag_text='Cartoon:')
group.grid(row=1, column=0, padx=1, pady=0, sticky='NW')
interior = group.interior()



#----------------Version 2------------#


# Cartoon Width Slider
    label3 = Label(interior, text = 'Width')
    label3.grid(row=0, column=0, padx=0, pady=0, sticky = W)
    self.toonWidth = Scale(interior, width =8)
    self.toonWidth.configure(troughcolor="#ffffff")
    self.toonWidth.configure(length="65")
    self.toonWidth.configure(orient="horizontal")
    self.toonWidth.configure(resolution="0.05")
    self.toonWidth.configure(to="2.0")
    self.toonWidth.set(1.4)
    self.toonWidth.grid(row=0, column=1, padx=0, pady=0, sticky=W)
    self.buttonAdd(interior,'Update',10,self.cartoon_width,0,2,SW)


# Cartoon Thickness Slider
    label4 = Label(interior, text = 'Thickness')
    label4.grid(row=1, column=0, padx=0, pady=0, sticky = W)
    self.toonThickness = Scale(interior, width =8)
    self.toonThickness.configure(troughcolor="#ffffff")
    self.toonThickness.configure(length="65")
    self.toonThickness.configure(orient="horizontal")
    self.toonThickness.configure(resolution="0.05")
    self.toonThickness.configure(to="2.0")
    self.toonThickness.set(0.3)
    self.toonThickness.grid(row=1, column=1, padx=0, pady=0, sticky = W)
    self.buttonAdd(interior,'Update',10,self.cartoon_thickness,1,2,SW)

# Cartoon Transparency Slider
    label5 = Label(interior, text = 'Transparency')
    label5.grid(row=2, column=0, padx=0, pady=0, sticky = W)
    self.cartoonTransparency = Scale(interior, width =8)
    self.cartoonTransparency.configure(length="65")
    self.cartoonTransparency.configure(troughcolor="#ffffff")
    self.cartoonTransparency.configure(orient="horizontal")
    self.cartoonTransparency.configure(resolution="0.05")
    self.cartoonTransparency.configure(to="1.0")
    self.cartoonTransparency.grid(row=2, column=1, padx=0, pady=0, sticky = W)
    self.buttonAdd(interior,'Update',10,self.cartoon_transparency,2,2,SW)
	
	# Cartoon Tube Radius Slider
    label6 = Label(interior, text = 'Tube Radius')
    label6.grid(row=3, column=0, padx=0, pady=0, sticky=W)
    self.toonTubeRadius = Scale(interior, width =8)
    self.toonTubeRadius.configure(troughcolor="#ffffff")
    self.toonTubeRadius.configure(length="65")
    self.toonTubeRadius.configure(orient="horizontal")
    self.toonTubeRadius.configure(resolution="0.05")
    self.toonTubeRadius.configure(to="1.0")
    self.toonTubeRadius.set(0.5)
    self.toonTubeRadius.grid(row=3, column=1, padx=0, pady=0, sticky = W)
    self.buttonAdd(interior,'Update',10,self.cartoon_tube_radius,3,2,SW)
	
	#----------------Ribbon Type Slider------------------
    self.ribbonTypes = Pmw.OptionMenu (interior,
            items = ('Automatic', 'Skip', 'Loop', 'Rectangle', 'Oval', 'Tube', 'Arrow', 'Dumbbell','Putty', 'Fancy helix'),
            menubutton_width = 7, command = self.ribType)
    self.ribbonTypes.grid(row=4,column=0,sticky=SW)
    
    #-------------- Sphere Group--------------------
    group = Pmw.Group(page, tag_text='Spheres:')
    group.grid(row=1, column=1, padx=1, pady=0, sticky=NW)
    interior = group.interior()
    
    # Sphere Size Slider
    label1 = Label(interior, text = 'Size')
    label1.grid(row=0, column=0, padx=0, pady=0, sticky=E)
    self.sphereScale =  Scale(interior, width =8)
    self.sphereScale.configure(troughcolor="#ffffff")
    self.sphereScale.configure(length="65")
    self.sphereScale.configure(orient="horizontal")
    self.sphereScale.configure(resolution="0.05")
    self.sphereScale.configure(to="2.0")
    self.sphereScale.set(0.7)
    self.sphereScale.grid(row=0, column=1, padx=0, pady=0, sticky='W')
    self.buttonAdd(interior,'Update',10,self.sphereSize,0,2,'SW')
    
    # Sphere Transparency Slider
    label2 = Label(interior, text = 'Transparency')
    label2.grid(row=1, column=0, padx=0, pady=0, sticky=E)
    self.sphereTransparency = Scale(interior, width =8)
    self.sphereTransparency.configure(troughcolor="#ffffff")
    self.sphereTransparency.configure(length="65")
    self.sphereTransparency.configure(orient="horizontal")
    self.sphereTransparency.configure(resolution="0.05")
    self.sphereTransparency.configure(to="1.0")
    self.sphereTransparency.grid(row=1, column=1, padx=0, pady=0, sticky='W')
    self.buttonAdd(interior,'Update',10,self.sphere_transparency,1,2,'SW')
    
    #--------------- Stick Group --------------------
    group = Pmw.Group(page, tag_text='Sticks:')
    group.grid(row=1, column=1, padx=1, pady=0, sticky=SW)
    interior = group.interior()
	
	# Stick Radius Slider
    label7 = Label(interior, text = 'Radius')
    label7.grid(row=0, column=0, padx=0, pady=0, sticky=E)
    self.stickRadius = Scale(interior, width =8)
    self.stickRadius.configure(troughcolor="#ffffff")
    self.stickRadius.configure(length="65")
    self.stickRadius.configure(orient="horizontal")
    self.stickRadius.configure(resolution="0.05")
    self.stickRadius.configure(to="3.0")
    self.stickRadius.set(0.2)
    self.stickRadius.grid(row=0, column=1, padx=0, pady=0, sticky='W')
    self.buttonAdd(interior,'Update',10,self.stickRad,0,2,'SW')
    
    
    # Stick Transparency Slider
    label8 = Label(interior, text = 'Transparency')
    label8.grid(row=1, column=0, padx=0, pady=0, sticky=E)
    self.stickTransparency = Scale(interior, width =8)
    self.stickTransparency.configure(troughcolor="#ffffff")
    self.stickTransparency.configure(length="65")
    self.stickTransparency.configure(orient="horizontal")
    self.stickTransparency.configure(resolution="0.05")
    self.stickTransparency.configure(to="1.0")
    self.stickTransparency.grid(row=1, column=1, padx=0, pady=0, sticky='W')
    self.buttonAdd(interior,'Update',10,self.stick_transparency,1,2,'SW')
    
    
    #-------------- Surface Group -------------------
    group = Pmw.Group(page, tag_text='Surface:')
    group.grid(row=2, column=1, padx=1, pady=0, sticky=SW)
    interior = group.interior()
    
    # Surface Transparency Slider
    label9 = Label(interior, text = 'Transparency')
    label9.grid(row=2, column=0, padx=0, pady=0, sticky=E)
    self.surfaceTransparency  = Scale(interior, width =8)
    self.surfaceTransparency.configure(troughcolor="#ffffff")
    self.surfaceTransparency.configure(length="65")
    self.surfaceTransparency.configure(orient="horizontal")
    self.surfaceTransparency.configure(resolution="0.05")
    self.surfaceTransparency.configure(to="1.0")
    self.surfaceTransparency.grid(row=2, column=1, padx=0, pady=0, sticky='W')
    self.buttonAdd(interior,'Update',10,self.surface_transparency,2,2,'SW')
    
    
    #----------Ambient Light Group----------------------
    group = Pmw.Group(page, tag_text='Ambient Light')
    group.grid(row=2, column=0, padx=0, pady=0, sticky=SW)
    interior = group.interior()
     #-----------------Ambient Light------------------------#
    lamb = Label(interior, text = 'Ambient Light')
    lamb.grid(row=0, column=0, padx=9, pady=0, sticky=E)
    frameasca = Frame(interior)
    frameasca.grid(row=0, column=1, padx=0, pady=0, sticky=W)
    ballasca = Pmw.Balloon(interior)
    ballasca.bind(frameasca, "Default ambient is .25")
    self.asca = Scale(frameasca, width =8)
    self.asca.configure(troughcolor="#ffffff")
    self.asca.configure(length="65")
    self.asca.configure(orient="horizontal")
    self.asca.configure(resolution="0.01")
    self.asca.configure(to="2.0")
    self.asca.grid(row=0, column=1, padx=0, pady=0, sticky=W)
    self.asca.set(.25)
    stupid = Button(interior, text = 'Update')
    stupid.grid(row=0, column=2, padx=0, pady=0, sticky='SW')
    stupid.configure(width = 10)
    stupid.pack
    def finickystuff(event):#----Go to here
        cmd.set("ambient", self.asca.get())
    stupid.bind('<Button-1>', finickystuff)