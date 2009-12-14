    page = notebook.add(' Toolbox ')
    notebook.tab(' Toolbox ').focus_set()

#------------------External Resources------------------#
    group = Pmw.Group(page, tag_text='Resources')
    group.grid(row=2, column=1, columnspan=2, padx=2, pady=2, sticky=NE)
    interior = group.interior()
    pdber = Entry(interior, width = 4)
    pdber.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
    pdberlab = Label(interior, text = 'PDB code')
    pdberlab.grid(row=0, column=0, padx=1, pady=1, sticky=NW)
    seqget = Button(interior, width = 12, text = 'PDB sequence')
    seqget.grid(row=0, column=1, padx=1, pady=1, sticky=NW)
    def getsequence(event):
        import webbrowser
        webbrowser.open('http://www.rcsb.org/pdb/downloadFile.do?fileFormat=FASTA&compression=NO&structureId='+ pdber.get())
    seqget.bind('<Button-1>', getsequence)
    def gotofasta(event):
        import webbrowser
        webbrowser.open('http://fasta.bioch.virginia.edu/')
    fasta = Button(interior, width = 5, text = 'FASTA')
    fasta.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    fasta.bind('<Button-1>', gotofasta)
    def getabstract(event):
        import webbrowser
        webbrowser.open('http://www.rcsb.org/pdb/pubmed.do?structureId='+ pdber.get())
    abstracter = Button(interior, width = 12, text = 'PDB Abstract')
    abstracter.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
    abstracter.bind('<Button-1>', getabstract)
    def gotorcsb():
        import webbrowser
        webbrowser.open('http://www.rcsb.org/pdb/Welcome.do')
    rcsb = Button(interior, width = 5, text = 'RCSB')
    rcsb.grid(row=1, column=2, padx=1, pady=1, sticky=NW)
    rcsb.bind('<Button-1>', gotorcsb)
  
  #--------------Electrostatics-------------#
    
    group = Pmw.Group(page, tag_text='Electrostatics')
    group.grid(row=2, column=0, columnspan=3, padx=2, pady=2, sticky=NW)
    interior = group.interior()
    labelaa = Label(interior, text = 'Code:')
    frameelec = Frame(interior, width=16)
    frameelec.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    ballelec = Pmw.Balloon(interior)
    ballelec.bind(frameelec, "Enter PDB Code: of Loaded Protein.\nCase Sensitive.")
    elecbtn = Button(frameelec, text =  'Electrostatics', width=16)
    elecbtn.grid(row=0, column=2, padx=1, pady=1, sticky=NW)
    entelc = Entry(interior, width =6)
    entelc.grid(row=0, column=1, sticky=E)
    elelabel = Label(interior, text='PDB Code:')
    elelabel.grid(row=0, column=0, sticky=W)
    def seq(event):
        try:
            util.protein_vacuum_esp(entelc.get(),mode=2,quiet=0)
        except:
            
            showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
            interior.mainloop()
    elecbtn.bind('<Button-1>', seq)
    framecdel = Frame(interior)
    framecdel.grid(row=0, column=3, padx=1, pady=1, sticky=NW)
    ballcdel = Pmw.Balloon(interior)
    ballcdel.bind(framecdel, 'Removes the current PDB Electrostatics')
    elecdel = Button(framecdel, width = 8, text = 'Remove')
    elecdel.grid(row=0, column=3, padx=1, pady=1, sticky=NW)
    def delelectro(event):
        try:
            cmd.select('goodbye',entelc.get()+'_e_chg')
            cmd.delete(entelc.get()+'_e_pot')
            cmd.delete(entelc.get()+'_e_chg')
            cmd.delete(entelc.get()+'_e_map')
            cmd.delete('goodbye')
            cmd.enable('all')
        except:
            cmd.delete('goodbye')
            cmd.delete(entelc.get()+'_e_pot')
            cmd.delete(entelc.get()+'_e_map')
            
            
            showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
            interior.mainloop()
    
    
    elecdel.bind('<Button-1>', delelectro)
    
    
    #---------Orthoscopic view and View distance-----#
    group = Pmw.Group(page, tag_text='Perspective')
    group.grid(row=1, column=1, padx=0, pady=0, sticky=NW)
    interior = group.interior()
    frameorthoon = Frame(interior, width = 16)
    frameorthoon.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
    balloonorth = Pmw.Balloon(interior)
    balloonorth.bind(frameorthoon, "Gives correct proportions to view.")
    frameorthoff = Frame(interior,width = 16)
    frameorthoff.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
    balloonorthoff = Pmw.Balloon(interior)
    balloonorthoff.bind(frameorthoff, "Gives greater distance perspective.")
    orthoon = Button(frameorthoon, text = 'Orthoscopic On', width = 16)
    orthoon.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
    viewsetter = Label(interior, text = 'Set Field of View')
    viewsetter.grid(row=2, column=0, padx=0, pady=0, sticky=N)
    
    def turnorthon(event):
        cmd.set("orthoscopic", "on")
    orthoon.bind('<Button-1>', turnorthon)
    orthoff = Button(frameorthoff, text = 'Orthoscopic Off',width = 16)
    orthoff.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
    def turnorthoff(event):
        cmd.set("orthoscopic", "off")
    orthoff.bind('<Button-1>', turnorthoff)
    framefieldview = Frame(interior)
    framefieldview.grid(row=3, column=0, padx=2, pady=2, sticky='N')
    balloonview = Pmw.Balloon(interior)
    balloonview.bind(framefieldview, "Also gives differing degrees of distance\n perspective, default is 20.")
    setfieldofview  = Scale(framefieldview, width =8)
    setfieldofview.configure(troughcolor="#ffffff")
    setfieldofview.configure(length="65")
    setfieldofview.configure(orient="horizontal")
    setfieldofview.configure(resolution="5")
    setfieldofview.configure(to="100")
    setfieldofview.grid(row=3, column=0, padx=0, pady=0, sticky='N')
    setfieldofview.set(20)
    def setfield(event):
        cmd.set("field_of_view", setfieldofview.get())
    getfield = Button(interior, text = 'Update',width = 16)
    getfield.grid(row=4, column=0, padx=2, pady=2, sticky=N)
    getfield.bind('<Button-1>', setfield)
    #-----------------full screen----------------------
    framefullscreen = Frame(interior,width = 16)
    framefullscreen.grid(row=5, column=0, padx=2, pady=2, sticky='N')
    balloonfullscreen = Pmw.Balloon(interior)
    balloonfullscreen.bind(framefullscreen, "Once full screen mode is initiated\n it cannot be turned off.")
    fullonbtn = Button(framefullscreen, text = 'Fullscreen Mode',width = 16)
    fullonbtn.grid(row=5, column=0, padx=2, pady=2, sticky='N')
    def fullon(event):
      cmd.set("full_screen", '1')
      cmd.set('internal_gui','0')
    fullonbtn.bind('<Button-1>', fullon)
#----------------Orient the screen--------------#
    frameorient = Frame(interior)
    frameorient.grid(row=6, column=0, padx=2, pady=2, sticky='N')
    ballorient = Pmw.Balloon(interior)
    ballorient.bind(frameorient, 'This will center the screen on the protein')
    orientbutt = Button(interior, text = 'Orient Screen', width = 16)
    orientbutt.grid(row=6, column=0, padx=2, pady=2, sticky='N')
    def orient(event):
        cmd.orient('all')
    orientbutt.bind('<Button-1>', orient)
    
    
    #-------------------Alternate Ray Tracing----------------------
    group = Pmw.Group(page, tag_text='Ray Trace Options')
group.grid(row=0, column=0,columnspan=2, padx=0, pady=5, sticky=NW)
interior = group.interior()
    def setray0(event):
        cmd.set("ray_trace_mode", "0")
        self.imgraysave()
    def setray1(event):
        cmd.set("ray_trace_mode", "1")
        cmd.do('bg_color white')
        self.imgraysave()
    def setray2(event):
        cmd.set("ray_trace_mode", "2")
        cmd.do('bg_color white')
        self.imgraysave()
    def setray3(event):
        cmd.set("ray_trace_mode", "3")
        self.imgraysave()
    rayzero = Button(interior, text = 'Default Ray')
    rayzero.grid(row=0, column=0, padx=2, pady=2, sticky=E)
    rayzero.bind('<Button-1>', setray0)
    rayone = Button(interior, text = 'Black Outline Ray')
    rayone.grid(row=0, column=1, padx=2, pady=2, sticky=E)
    rayone.bind('<Button-1>', setray1)
    raytwo = Button(interior, text = 'Black and White Ray')
    raytwo.grid(row=0, column=2, padx=2, pady=2, sticky=E)
    raytwo.bind('<Button-1>', setray2)
    raythree = Button(interior, text = 'Cartoon Ray')
    raythree.grid(row=0, column=3, padx=2, pady=2, sticky=E)
    raythree.bind('<Button-1>', setray3)

#------------------Amino Acid Reference Group-----------------
    group = Pmw.Group(page, tag_text='Amino Acid Reference:')
    group.grid(row=1, column=0,  padx=0, pady=0, sticky=NW)
    interior = group.interior()
    canvas79=Canvas(interior, width=200, height=150)
    canvas79.grid(row=2, column=0,columnspan = 2, padx=0, pady=0, sticky=NE)
    msg = Message(interior, width = 200, text="Amino Acid Code:")
    msg.grid(row=0, column=0, padx=0, pady=0, sticky=NE)
    name5 = Entry (interior, width = 7)
    name5.grid(row=0, column=1, padx=4, pady=3, sticky=NW)
    but37 = Button (interior)
    but37.grid(row=0, column=2, padx=4, pady=3, sticky=NW)
    but37.configure(text="Submit")
    but37.configure(width="7")
    name6 = Entry (interior, width = 10)
    name6.grid(row=1, column=1, padx=4, pady=3, sticky=NW)
    but49 = Button (interior)
    but49.grid(row=1, column=2, padx=4, pady=3, sticky=NW)
    but49.configure(text="Submit")
    but49.configure(width="7")
    
    msg = Message(interior, width = 200, text="Amino Acid name:")
    msg.grid(row=1, column=0, padx=0, pady=0, sticky=NE)
    
    diment = Entry(interior)
    
    # 2D/3D interface, shows amino acid as specified
    def dim_dim(tag):
        if tag == '2D':
          diment.delete(0,2)
          diment.insert(0,'1')
        else:
          diment.delete(0,2)
          diment.insert(0,'2')
    
    labels = ('2D', '3D')
self.radioAdd(interior, 'w', 'vertical', dim_dim,
	      ' ', labels, 2, 2, 1, 1, 'NW')
    
    
    #Defines Which amino acid is to be displayed
#for amino acid reference
    def aaget(event):
        try:
            if name5.get() == 'g':
                if diment.get() == '2':
                    name6.delete(0,30)
                    name6.insert(0, 'glycine')
                    canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
                else:
                    name6.delete(0,30)
                    name6.insert(0, 'glycine')
                    canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
            if name5.get() == 'gly':
                if diment.get() == '2':
                    name6.delete(0,30)
                    name6.insert(0, 'glycine')
                    canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
                else:
                    name6.delete(0,30)
                    name6.insert(0, 'glycine')
                    canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
            if name5.get() == 'a':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'alanine')
                  canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'alanine')
                  canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
            if name5.get() == 'ala':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'alanine')
                  canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'alanine')
                  canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
            if name5.get() == 'v':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'valine')
                  canvas79.create_image(0,0,image=VALTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'valine')
                  canvas79.create_image(0,0,image=VALGUM,anchor=NW)
            if name5.get() == 'val':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'valine')
                  canvas79.create_image(0,0,image=VALTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'valine')
                  canvas79.create_image(0,0,image=VALGUM,anchor=NW)
            if name5.get() == 'l':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'leucine')
                  canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'leucine')
                  canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
            if name5.get() == 'leu':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'leucine')
                  canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'leucine')
                  canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
            if name5.get() == 'i':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'isoleucine')
                  canvas79.create_image(0,0,image=ILETACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'isoleucine')
                  canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
            if name5.get() == 'ile':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'isoleucine')
                  canvas79.create_image(0,0,image=ILETACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'isoleucine')
                  canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
            if name5.get() == 'm':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'methionine')
                  canvas79.create_image(0,0,image=METTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'methionine')
                  canvas79.create_image(0,0,image=METGUM,anchor=NW)
            if name5.get() == 'met':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'methionine')
                  canvas79.create_image(0,0,image=METTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'methionine')
                  canvas79.create_image(0,0,image=METGUM,anchor=NW)
            if name5.get() == 'r':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'arginine')
                  canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'arginine')
                  canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
            if name5.get() == 'arg':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'arginine')
                  canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'arginine')
                  canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
            if name5.get() == 'd':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'aspartate')
                  canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'aspartate')
                  canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
            if name5.get() == 'asp':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'aspartate')
                  canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'aspartate')
                  canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
            if name5.get() == 'c':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'cysteine')
                  canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'cysteine')
                  canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
            if name5.get() == 'c':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'cysteine')
                  canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'cysteine')
                  canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
            if name5.get() == 'e':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'glutamate')
                  canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'glutamate')
                  canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
            if name5.get() == 'glu':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'glutamate')
                  canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'glutamate')
                  canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
            if name5.get() == 'q':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'glutamine')
                  canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'glutamine')
                  canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
            if name5.get() == 'gln':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'glutamine')
                  canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'glutamine')
                  canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
            if name5.get() == 'h':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'histidine')
                  canvas79.create_image(0,0,image=HISTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'histidine')
                  canvas79.create_image(0,0,image=HISGUM,anchor=NW)
            if name5.get() == 'his':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'histidine')
                  canvas79.create_image(0,0,image=HISTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'histidine')
                  canvas79.create_image(0,0,image=HISGUM,anchor=NW)
            if name5.get() == 'k':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'lysine')
                  canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'lysine')
                  canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
            if name5.get() == 'lys':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'lysine')
                  canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'lysine')
                  canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
            if name5.get() == 'f':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'phenylalanine')
                  canvas79.create_image(0,0,image=PHETACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'phenylalanine')
                  canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
            if name5.get() == 'phe':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'phenylalanine')
                  canvas79.create_image(0,0,image=PHETACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'phenylalanine')
                  canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
            if name5.get() == 'p' :
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'proline')
                  canvas79.create_image(0,0,image=PROTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'proline')
                  canvas79.create_image(0,0,image=PROGUM,anchor=NW)
            if name5.get() == 'pro' :
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'proline')
                  canvas79.create_image(0,0,image=PROTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'proline')
                  canvas79.create_image(0,0,image=PROGUM,anchor=NW)
            if name5.get() == 's':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'serine')
                  canvas79.create_image(0,0,image=SERTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'serine')
                  canvas79.create_image(0,0,image=SERGUM,anchor=NW)
            if name5.get() == 'ser':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'serine')
                  canvas79.create_image(0,0,image=SERTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'serine')
                  canvas79.create_image(0,0,image=SERGUM,anchor=NW)
            if name5.get() == 't':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'threonine')
                  canvas79.create_image(0,0,image=THRTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'threonine')
                  canvas79.create_image(0,0,image=THRGUM,anchor=NW)
            if name5.get() == 'thr':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'threonine')
                  canvas79.create_image(0,0,image=THRTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'threonine')
                  canvas79.create_image(0,0,image=THRGUM,anchor=NW)
            if name5.get() == 'w':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'tryptophan')
                  canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'tryptophan')
                  canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
            if name5.get() == 'trp':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0,'tryptophan')
                  canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'tryptophan')
                  canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
            if name5.get() == 'y':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'tyrosine')
                  canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'tyrosine')
                  canvas79.create_image(0,0,image=TRYGUM,anchor=NW)
            if name5.get() == 'tyr':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'tyrosine')
                  canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'tyrosine')
                  canvas79.create_image(0,0,image=TRYGUM,anchor=NW)
            if name5.get() == 'n':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'asparagine')
                  canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'asparagine')
                  canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
            if name5.get() == 'asn':
                if diment.get() == '2':
                  name6.delete(0,30)
                  name6.insert(0, 'asparagine')
                  canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
                else:
                  name6.delete(0,30)
                  name6.insert(0, 'asparagine')
                  canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
        
        
        except:
            name6.delete(0,30)
            name6.insert(0, '')
    name5.bind('<Return>', aaget)
    but37.bind('<Button-1>', aaget)
    def aagive(event):
        try:
            if name6.get() == 'glycine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'gly, g')
                canvas79.create_image(0,0,image=GLYTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'gly, g')
                canvas79.create_image(0,0,image=GLYGUM,anchor=NW)
            if name6.get() == 'alanine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'ala, a')
                canvas79.create_image(0,0,image=TACOBUENO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'ala, a')
                canvas79.create_image(0,0,image=ALAGUM,anchor=NW)
            if name6.get() == 'valine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'val, v')
                canvas79.create_image(0,0,image=VALTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'val, v')
                canvas79.create_image(0,0,image=VALGUM,anchor=NW)
            if name6.get() == 'leucine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'leu, l')
                canvas79.create_image(0,0,image=LEUTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'leu, l')
                canvas79.create_image(0,0,image=LEUGUM,anchor=NW)
            if name6.get() == 'isoleucine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'ile, i')
                canvas79.create_image(0,0,image=ILETACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'ile, i')
                canvas79.create_image(0,0,image=ILEGUM,anchor=NW)
            if name6.get() == 'methionine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'met, m')
                canvas79.create_image(0,0,image=METTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'met, m')
                canvas79.create_image(0,0,image=METGUM,anchor=NW)
            if name6.get() == 'arginine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'arg, r')
                canvas79.create_image(0,0,image=ARGTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'arg, r')
                canvas79.create_image(0,0,image=ARGGUM,anchor=NW)
            if name6.get() == 'aspartate':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'asp, d')
                canvas79.create_image(0,0,image=ASPTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'asp, d')
                canvas79.create_image(0,0,image=ASPGUM,anchor=NW)
            if name6.get() == 'cysteine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'cys, c')
                canvas79.create_image(0,0,image=CYSTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'cys, c')
                canvas79.create_image(0,0,image=CYSGUM,anchor=NW)
            if name6.get() == 'glutamate':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'glu, e')
                canvas79.create_image(0,0,image=GLUTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'glu, e')
                canvas79.create_image(0,0,image=GLUGUM,anchor=NW)
            if name6.get() == 'glutamine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'gln, q')
                canvas79.create_image(0,0,image=GLNTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'gln, q')
                canvas79.create_image(0,0,image=GLNGUM,anchor=NW)
            if name6.get() == 'histidine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'his, h')
                canvas79.create_image(0,0,image=HISTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'his, h')
                canvas79.create_image(0,0,image=HISGUM,anchor=NW)
            if name6.get() == 'lysine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0,'lys, k')
                canvas79.create_image(0,0,image=LYSTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'lys, k')
                canvas79.create_image(0,0,image=LYSGUM,anchor=NW)
            if name6.get() == 'phenylalanine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'phe, f')
                canvas79.create_image(0,0,image=PHETACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'phe, f')
                canvas79.create_image(0,0,image=PHEGUM,anchor=NW)
            if name6.get() == 'proline':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'pro, p')
                canvas79.create_image(0,0,image=PROTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'pro, p')
                canvas79.create_image(0,0,image=PROGUM,anchor=NW)
            if name6.get() == 'serine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'ser, s')
                canvas79.create_image(0,0,image=SERTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'ser, s')
                canvas79.create_image(0,0,image=SERGUM,anchor=NW)
            if name6.get() == 'threonine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'thr, t')
                canvas79.create_image(0,0,image=THRTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'thr, t')
                canvas79.create_image(0,0,image=THRGUM,anchor=NW)
            if name6.get() == 'tryptophan':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'trp, w')
                canvas79.create_image(0,0,image=TRPTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'trp, w')
                canvas79.create_image(0,0,image=TRPGUM,anchor=NW)
            if name6.get() == 'tyrosine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'tyr, y')
                canvas79.create_image(0,0,image=TYRTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'tyr, y')
                canvas79.create_image(0,0,image=TYRGUM,anchor=NW)
            if name6.get() == 'asparagine':
              if diment.get() == '2':
                name5.delete(0,30)
                name5.insert(0, 'asn, n')
                canvas79.create_image(0,0,image=ASNTACO,anchor=NW)
              else:
                name5.delete(0,30)
                name5.insert(0, 'asn, n')
                canvas79.create_image(0,0,image=ASNGUM,anchor=NW)
        except:
            name5.delete(0,30)
            name5.insert(0, '')
    but49.bind('<Button-1>', aagive)