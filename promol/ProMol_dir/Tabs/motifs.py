page = notebook.add('Motifs')

#Molecular Classification Field
    label = Label(page, text='Protein Classification')
    label.grid(row=1,column=0,sticky='sw',padx=5,pady=0)
    self.classify = Text(page, state=NORMAL, height=1.4, width=30)
self.classify.insert(END,"Protein Classification")
self.classify.grid(row=2, column=0, sticky='sw',padx=5, pady=0)

#Molecule Name Field
self.name = StringVar()
self.molName = Label(page, textvariable=self.name, font='arial, 14', wraplength='450')
self.name.set("")
self.molName.grid(row=0, column=0, columnspan=2,sticky='w',padx=5, pady=5)


#Hetero Atoms
label=Label(page, text="Hetero Atoms")
label.grid(row=1, column=1, sticky='sw', padx=5, pady=0)
self.het = Text(page, state=NORMAL, height=1.4, width=25)
self.het.insert(END,"List of hetero atoms")
self.het.grid(row=2,column=1, sticky='w',padx=5,pady=0)
    
    #mechanisim group
    group = Pmw.Group(page, tag_text = 'Motifs')
    group.grid(row=3, column=0,columnspan =2, padx=0, pady=0)
    interior = group.interior()
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Oxidoreductases:',labelpos = 'n',
                items = ('','Superoxide Dismutase','Peroxidase','Alcohol Dehydrogenase',
                         'Aldose Reductase','NAD Reductase', 'NAD Reductase2','Betaine aldehyde dehydrogenase'),
                menubutton_width = 8, command=self.oxidoreductase)
    stereo.grid(row=0,column=0,sticky=NW)
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Transferases:',labelpos = 'n',
                            items = ('','Amino Transferase', 'Glutamine Amidotransferase',
                                     'Thymidine Kinase', 'ACTase', 'Adenylate Kinase','SRC Family Kinase',
                                     'Hhal Methyltransferase','Serotonin Acetyltransferase', 'Cyclin Dependent Kinase'),
                            menubutton_width = 8, command=self.transferase)
    stereo.grid(row=0,column=1,sticky=NW)
   
   # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Hydrolases:',labelpos = 'n',
                items = ('','Serine Protease', 'Papain Like', 'Metalloprotease', 'Tyrosine Phosphatase', 'Beta Lactamase', 'O-Glycosyl', 'Cephalosporin deacetylase'),
                menubutton_width = 8, command=self.hydrolase)
    stereo.grid(row=0,column=2,sticky=NW)
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Lyases:',labelpos = 'n',
                items = ('','Carbonic Anhydrase', 'Carbon Carbon','Chondroitinase', 'Hyaluronate-Lyase', 'Exonuclease 3', 'Citrate Synthase'),
                menubutton_width = 8, command=self.lyase)
    stereo.grid(row=0,column=3,sticky=NW)
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Isomerases:',labelpos = 'n',
                items = ('','Fucose Isomerase','Triose Phosphate Isomerase', 'FK506 Cis-Trans'),
                menubutton_width = 8, command=self.isomerase)
    stereo.grid(row=1,column=0,sticky=NW)
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Ligase:',labelpos = 'n',
                items = (' ', 'DNA Ligase'),
                menubutton_width = 8, command=self.ligase)
    stereo.grid(row=1,column=1,sticky=NW)
    
    # Menu for motifs
    stereo = Pmw.OptionMenu(interior,label_text = 'Other:',labelpos = 'n',
                items = ('','Zinc Finger'),
                menubutton_width = 8, command=self.other)
    stereo.grid(row=1,column=2,sticky=NW)
    
    stereo = Pmw.OptionMenu(interior,label_text = 'Options:',labelpos = 'n',
                items = ('','Surface Pocket','Polar Contacts', 'Hide Contacts', 'Show Substrate', 'Hide Substrate', 'Show label', 'Hide Label'),
                menubutton_width = 8, command=self.motifoption)
    stereo.grid(row=1,column=3,sticky=NW)
    framerange = Frame(interior)
    framerange.grid(row=2, column=1,columnspan = 4, padx=0, pady=0, sticky=NW)
    ballrange = Pmw.Balloon(interior)
    ballrange.bind(framerange, 'Multiplier for default measured values\nRe-click on desired motif to render change')
    self.range = Scale(framerange, width =8)
    self.range.configure(troughcolor="#ffffff")
    self.range.configure(length="200")
    self.range.configure(orient="horizontal")
    self.range.configure(resolution="0.01")
    self.range.configure(to="2.0")
    self.range.grid(row=2, column=1,columnspan = 4, padx=0, pady=0, sticky=NW)
    self.range.set(1)
    
    labrange = Label(interior, text='Precision Factor:')
    labrange.grid(row=2, column=0, sticky=SE)
    
    self.buttonAdd(interior, 'Reset', 10, self.resetrange, 3, 3, 'SE')



#---------------------Show residues around active site---------------#
    group = Pmw.Group(page, tag_text='Tools')
group.grid(row=4, column=0, columnspan=1, padx=2, pady=2, sticky=W)
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
    
    
    showround = Button(frameadj, width = 12, text = 'Adjacent')
    showround.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
    
    def roundres(event):
        try:
            cmd.hide('sticks', '!'+self.mot)
            cmd.color('white', '!'+self.mot)
            cmd.select('Adjacent', 'byres '+self.mot+' around %s'%(selA.get()))
            cmd.show('sticks', 'Adjacent')
            cmd.color('orange', 'Adjacent')
            util.cnc('Adjacent')
            cmd.remove('hydro')
            cmd.deselect()
        except:
            
            showinfo('Alert', 'You must load a motif first')
            interior.mainloop()
    showround.bind('<Button-1>', roundres)
    delres = Button(interior, width = 14, text = 'Delete Adjacent')
    delres.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
    def resdel(event):
        try:
            objects = cmd.get_names('all')
            cmd.hide('sticks', '!'+self.mot)
            cmd.color('white', '!'+self.mot)
            if 'Adjacent' in objects:
                cmd.delete('Adjacent_polar_conts')
            if 'Adjacent' in objects:
                cmd.label('byres Adjacent',"''")
            cmd.delete('Adjacent')
        except:
            
            showinfo('Alert', 'You must load a motif first')
            interior.mainloop()
    
    delres.bind('<Button-1>', resdel)
    
    
    #Mofit Finder---------------------------------
    #------Goes through all motif functions and counts atoms for viable returns
    
    group = Pmw.Group(page, tag_text='Motif Search')
	group.grid(row=4, column=1, columnspan=1, padx=2, pady=2, sticky=W)
interior = group.interior()
    
    def motifchecker(event):
                
                cmd.hide('everything', 'all')
                cmd.remove("(all) and hydro")
                list=[]
                
                self.exonucleaseiii2()
                x = cmd.count_atoms('Exonuclease3')
                if x == 42:
                   list.append('1-Exonuclease 3')
                if x < 42 and x > 32:
                   list.append('2-Exonuclease 3')
                
                cmd.delete('Exonuclease3')
                
                
                self.cyclinkinase2()
                x = cmd.count_atoms('Cyclin_Kinase')
                if x == 26:
                  list.append('1-Cyclin Dependent Kinase')
                if x < 35 and x > 26:
                  list.append('2-Cyclin Dependent Kinase')
                if x < 26 and x > 23:
                  list.append('2-Cyclin Dependent Kinase')
                
                
                self.citratesynth2()
                x = cmd.count_atoms('Citrate_Synth')
                if x == 34:
                   list.append('1-Citrate Synthase')
                if x < 34 and x > 28:
                    list.append('2-Citrate Synthase')
                
                cmd.delete('Citrate_Synth')
                
                self.trioseisomerase2()
                x = cmd.count_atoms('TrioseIsomerase')
                if x == 40:
                   list.append('1-Triose Phosphate Isomerase')
                if x < 45 and x > 40:
                    list.append('2-Triose Phosphate Isomerase')
                if x < 40 and x > 32:
                    list.append('2-Triose Phosphate Isomerase')
                if x == 80:
                   list.append('1-Triose Phosphate Isomerase')
                if x < 90 and x > 80:
                    list.append('2-Triose Phosphate Isomerase')
                if x < 80 and x > 64:
                    list.append('2-Triose Phosphate Isomerase')
                
                self.serineprotease2()
                x = cmd.count_atoms('serineprotease')
                if x == 24:
                   list.append('1-Serine Protease')
                if x < 33 and x > 24:
                    list.append('2-Serine Protease')
                if x < 24 and x > 18:
                    list.append('2-Serine Protease')
                if x == 48:
                   list.append('1-Serine Protease')
                if x < 66 and x > 48:
                    list.append('2-Serine Protease')
                if x < 48 and x > 36:
                    list.append('2-Serine Protease')
                cmd.delete('serineprotease')
                
                self.Blactamase2()
                x = cmd.count_atoms('lactamase')
                if x == 45:
                   list.append('1-Beta Lactamase')
                if x < 55 and x > 45:
                    list.append('2-Beta Lactamase')
                if x < 45 and x > 35:
                    list.append('2-Beta Lactamase')
                if x == 90:
                   list.append('1-Beta Lactamase')
                if x < 110 and x > 90:
                    list.append('2-Beta Lactamase')
                if x < 90 and x > 70:
                    list.append('2-Beta Lactamase')
                cmd.delete('lactamase')
                
                cmd.select('zn', 'elem zn(elem cu)')
                x = cmd.count_atoms('zn')
                if x > 2:
                    self.superoxide2()
                    x = cmd.count_atoms('superoxide')
                    if x == 70:
                       list.append('1-Superoxide Dismutase')
                    if x < 90 and x > 70:
                        list.append('2-Superoxide Dismutase')
                    if x < 70 and x > 60:
                        list.append('2-Superoxide Dismutase')
                    if x == 140:
                       list.append('1-Superoxide Dismutase')
                    if x < 150 and x > 140:
                        list.append('2-Superoxide Dismutase')
                    if x < 140 and x > 115:
                        list.append('2-Superoxide Dismutase')
                    cmd.delete('superoxide')
                    cmd.delete('zn')
                else:
                    cmd.delete('zn')

                
                
                cmd.select('zn', 'elem zn')
                x = cmd.count_atoms('zn')
                if x > 1:
                    self.zincfinger2()
                    x = cmd.count_atoms('Zinc_finger')
                    if x == 32:
                       list.append('1-Zinc Finger')
                    if x < 50 and x > 32:
                        list.append('2-Zinc Finger')
                    if x < 32 and x > 20:
                        list.append('2-Zinc Finger')
                    if x == 64:
                       list.append('1-Zinc Finger')
                    if x < 100 and x > 64:
                        list.append('2-Zinc Finger')
                    if x < 64 and x > 40:
                        list.append('2-Zinc Finger')
                    cmd.delete('zn')
                    cmd.delete('Zince_finger')
                
                
                self.aminotransferase2()
                x = cmd.count_atoms('Aminotransferase')
                if x == 27 :
                   list.append('1-Amino Transferase')
                if x < 40 and x > 27:
                    list.append('2-Amino Transferase')
                if x < 27 and x > 20:
                    list.append('2-Amino Transferase')
                if x == 54:
                   list.append('1-Amino Transferase')
                if x < 80 and x > 54:
                    list.append('2-Amino Transferase')
                if x < 54 and x > 40:
                    list.append('2-Amino Transferase')
                cmd.delete('Aminotransferase')
                
                self.chondrolyase2()
                x = cmd.count_atoms('chondroitinase')
                if x == 41 :
                   list.append('1-Chondroitinase')
                if x < 51 and x > 41:
                    list.append('2-Chondroitinase')
                if x < 41 and x > 31:
                    list.append('2-Chondroitinase')
                if x == 82:
                   list.append('1-Chondroitinase')
                if x < 102 and x > 82:
                    list.append('2-Chondroitinase')
                if x < 82 and x > 62:
                    list.append('2-Chondroitinase')
                cmd.delete('chonroitinase')
                
                self.hyaluronlyase2()
                x = cmd.count_atoms('Hyaluronate_Lyase')
                if x == 41 :
                   list.append('1-Hyaluronate-Lyase')
                if x < 51 and x > 41:
                    list.append('2-Hyaluronate-Lyase')
                if x < 41 and x > 31:
                    list.append('2-Hyaluronate-Lyase')
                if x == 82:
                   list.append('1-Hyaluronate-Lyase')
                if x < 102 and x > 82:
                    list.append('2-Hyaluronate-Lyase')
                if x < 82 and x > 62:
                    list.append('2-Hyaluronate-Lyase')
                cmd.delete('Hyaluronate_Lyase')
                
                self.peroxidase2()
                x = cmd.count_atoms('Peroxidase')
                if x == 29 :
                   list.append('1-Peroxidase')
                if x < 39 and x > 29:
                    list.append('2-Peroxidase')
                if x < 29 and x > 19:
                    list.append('2-Peroxidase')
                if x == 29*2 :
                   list.append('1-Peroxidase')
                if x < 39*2 and x > 29*2:
                    list.append('2-Peroxidase')
                if x < 29*2 and x > 19*2:
                    list.append('2-Peroxidase')
                if x == 29*3 :
                   list.append('1-Peroxidase')
                if x < 39*3 and x > 29*3:
                    list.append('2-Peroxidase')
                if x < 29*3 and x > 19*3:
                    list.append('2-Peroxidase')
                if x == 29*4 :
                   list.append('1-Peroxidase')
                if x < 39*4 and x > 29*4:
                    list.append('2-Peroxidase')
                if x < 29*4 and x > 19*4:
                    list.append('2-Peroxidase')
                cmd.delete('Peroxidase')
                
                self.nadhbinder22()
                x = cmd.count_atoms('NAD-reductase')
                if x == 20 :
                   list.append('1-NAD Reductase')
                if x < 27 and x > 20:
                    list.append('2-NAD Reductase')
                if x < 20 and x > 16:
                    list.append('2-NAD Reductase')
                if x == 20*2 :
                   list.append('1-NAD Reductase')
                if x < 27*2 and x > 20*2:
                    list.append('2-NAD Reductase')
                if x < 20*2 and x > 16*2:
                    list.append('2-NAD Reductase')
                if x == 20*3 :
                   list.append('1-NAD Reductase')
                if x < 27*3 and x > 20*3:
                    list.append('2-NAD Reductase')
                if x < 20*3 and x > 16*3:
                    list.append('2-NAD Reductase')
                if x == 20*4 :
                   list.append('1-NAD Reductase')
                if x < 27*4 and x > 20*4:
                    list.append('2-NAD Reductase')
                if x < 20*4 and x > 16*4:
                    list.append('2-NAD Reductase')
                cmd.delete('NAD-reductase')
                
                self.nadhbinder222()
                x = cmd.count_atoms('NAD-reductase2')
                if x == 21 :
                   list.append('1-NAD Reductase2')
                if x < 28 and x > 21:
                    list.append('2-NAD Reductase2')
                if x < 21 and x > 17:
                    list.append('2-NAD Reductase2')
                if x == 21*2 :
                   list.append('1-NAD Reductase2')
                if x < 28*2 and x > 21*2:
                    list.append('2-NAD Reductase2')
                if x < 21*2 and x > 17*2:
                    list.append('2-NAD Reductase2')
                if x == 21*3 :
                   list.append('1-NAD Reductase2')
                if x < 28*3 and x > 21*3:
                    list.append('2-NAD Reductase2')
                if x < 21*3 and x > 17*3:
                    list.append('2-NAD Reductase2')
                if x == 21*4 :
                   list.append('1-NAD Reductase2')
                if x < 28*4 and x > 21*4:
                    list.append('2-NAD Reductase2')
                if x < 21*4 and x > 17*4:
                    list.append('2-NAD Reductase2')
                cmd.delete('NAD-reductase2')
                
                self.tyrosinekinase2()
                x = cmd.count_atoms('SRC-Kinase')
                if x == 24:
                   list.append('1-SRC Family Kinase')
                if x < 30 and x > 24:
                    list.append('2-SRC Family Kinase')
                if x < 24 and x > 16:
                    list.append('2-SRC Family Kinase')
                if x == 24*2:
                   list.append('1-SRC Family Kinase')
                if x < 30*2 and x > 24*2:
                    list.append('2-SRC Family Kinase')
                if x < 24*2 and x > 16*2:
                    list.append('2-SRC Family Kinase')
                cmd.delete('SRC-Kinase')
                
                
                self.cistransisomerase2()
                x = cmd.count_atoms('Cis-trans')
                if x == 36:
                   list.append('1-FK506 Cis-Trans')
                if x < 46 and x > 36:
                    list.append('2-FK506 Cis-Trans')
                if x < 36 and x > 26:
                    list.append('2-FK506 Cis-Trans')
                if x == 36*2:
                   list.append('1-FK506 Cis-Trans')
                if x < 46*2 and x > 36*2:
                    list.append('2-FK506 Cis-Trans')
                if x < 36*2 and x > 26*2:
                    list.append('2-FK506 Cis-Trans')
                cmd.delete('Cis-trans')
                
                
                self.cephdeacetylase2()
                x = cmd.count_atoms('deacetylase')
                if x == 32:
                   list.append('1-Cephalosporin deacetylase')
                if x < 42 and x > 32:
                    list.append('2-Cephalosporin deacetylase')
                if x < 32 and x > 26:
                    list.append('2-Cephalosporin deacetylase')
                if x == 32*2:
                   list.append('1-Cephalosporin deacetylase')
                if x < 42*2 and x > 32*2:
                    list.append('2-Cephalosporin deacetylase')
                if x < 32*2 and x > 26*2:
                    list.append('2-Cephalosporin deacetylase')
                cmd.delete('deacetylase')


                
                
                self.paplike2()
                x = cmd.count_atoms('paplike')
                if x == 25:
                  list.append('1-Papain Like')
                if x < 33 and x > 25:
                  list.append('2-Papain Like')
                if x < 25 and x > 17:
                  list.append('2-Papain Like')
                if x == 25*2:
                  list.append('1-Papain Like')
                if x < 33*2 and x > 25*2:
                  list.append('2-Papain Like')
                if x < 25*2 and x > 17*2:
                  list.append('2-Papain Like')
                if x == 25*3:
                  list.append('1-Papain Like')
                if x < 33*3 and x > 25*3:
                  list.append('2-Papain Like')
                if x < 25*3 and x > 17*3:
                  list.append('2-Papain Like')
                if x == 25*4:
                  list.append('1-Papain Like')
                if x < 33*4 and x > 25*4:
                  list.append('2-Papain Like')
                if x < 25*4 and x > 17*4:
                  list.append('2-Papain Like')
                cmd.delete('paplike')
                
                self.hhal2()
                x = cmd.count_atoms('hhal')
                if x == 37:
                  list.append('1-Hhal Methyltransferase')
                if x < 47 and x > 37:
                  list.append('2-Hhal Methyltransferase')
                if x < 37 and x > 27:
                  list.append('2-Hhal Methyltransferase')
                if x == 37*2:
                  list.append('1-Hhal Methyltransferase')
                if x < 47*2 and x > 37*2:
                  list.append('2-Hhal Methyltransferase')
                if x < 37*2 and x > 27*2:
                  list.append('2-Hhal Methyltransferase')
                if x == 37*3:
                  list.append('1-Hhal Methyltransferase')
                if x < 47*3 and x > 37*3:
                  list.append('2-Hhal Methyltransferase')
                if x < 37*3 and x > 27*3:
                  list.append('2-Hhal Methyltransferase')
                if x == 37*4:
                  list.append('1-Hhal Methyltransferase')
                if x < 47*4 and x > 37*4:
                  list.append('2-Hhal Methyltransferase')
                if x < 37*4 and x > 27*4:
                  list.append('2-Hhal Methyltransferase')
                cmd.delete('hhal')
                
                self.ACTase2()
                x = cmd.count_atoms('actase')
                if x == 140:
                  list.append('1-ACTase')
                if x < 150 and x > 140:
                  list.append('2-ACTase')
                if x < 140 and x > 130:
                  list.append('2-ACTase')
                if x == 140*2:
                  list.append('1-ACTase')
                if x < 150*2 and x > 140*2:
                  list.append('2-ACTase')
                if x < 140*2 and x > 130*2:
                  list.append('2-ACTase')
                if x == 140*3:
                  list.append('1-ACTase')
                if x < 150*3 and x > 140*3:
                  list.append('2-ACTase')
                if x < 140*3 and x > 130*3:
                  list.append('2-ACTase')
                if x == 140*4:
                  list.append('1-ACTase')
                if x < 150*4 and x > 140*4:
                  list.append('2-ACTase')
                if x < 140*4 and x > 130*4:
                  list.append('2-ACTase')
                cmd.delete('actase')
                
                self.alcoholdehyd2()
                x = cmd.count_atoms('alcoholdehyd')
                if x == 35:
                  list.append('1-Alcohol Dehydrogenase')
                if x < 45 and x > 35:
                  list.append('2-Alcohol Dehydrogenase')
                if x < 35 and x > 25:
                  list.append('2-Alcohol Dehydrogenase')
                if x == 35*2:
                  list.append('1-Alcohol Dehydrogenase')
                if x < 45*2 and x > 35*2:
                  list.append('2-Alcohol Dehydrogenase')
                if x < 35*2 and x > 25*2:
                  list.append('2-Alcohol Dehydrogenase')
                if x == 35*3:
                  list.append('1-Alcohol Dehydrogenase')
                if x < 45*3 and x > 35*3:
                  list.append('2-Alcohol Dehydrogenase')
                if x < 35*3 and x > 25*3:
                  list.append('2-Alcohol Dehydrogenase')
                if x == 35*4:
                  list.append('1-Alcohol Dehydrogenase')
                if x < 45*4 and x > 35*4:
                  list.append('2-Alcohol Dehydrogenase')
                if x < 35*4 and x > 25*4:
                  list.append('2-Alcohol Dehydrogenase')
                cmd.delete('alcoholdehyd')
                
                self.adenylatekinase2()
                x = cmd.count_atoms('adenylatekinase')
                if x == 66:
                  list.append('1-Adenylate Kinase')
                if x < 76 and x > 66:
                  list.append('2-Adenylate Kinase')
                if x < 66 and x > 56:
                  list.append('2-Adenylate Kinase')
                if x == 66*2:
                  list.append('1-Adenylate Kinase')
                if x < 76*2 and x > 66*2:
                  list.append('2-Adenylate Kinase')
                if x < 66*2 and x > 56*2:
                  list.append('2-Adenylate Kinase')
                if x == 66*3:
                  list.append('1-Adenylate Kinase')
                if x < 76*3 and x > 66*3:
                  list.append('2-Adenylate Kinase')
                if x < 66*3 and x > 56*3:
                  list.append('2-Adenylate Kinase')
                if x == 66*4:
                  list.append('1-Adenylate Kinase')
                if x < 76*4 and x > 66*4:
                  list.append('2-Adenylate Kinase')
                if x < 66*4 and x > 56*4:
                  list.append('2-Adenylate Kinase')
                cmd.delete('adenylatekinase')
                
                self.aldoreductase2()
                x = cmd.count_atoms('aldoreductase')
                if x == 39:
                  list.append('1-Aldose Reductase')
                if x < 49 and x > 39:
                  list.append('2-Aldose Reductase')
                if x < 39 and x > 29:
                  list.append('2-Aldose Reductase')
                if x == 39*2:
                  list.append('1-Aldose Reductase')
                if x < 49*2 and x > 39*2:
                  list.append('2-Aldose Reductase')
                if x < 39*2 and x > 29*2:
                  list.append('2-Aldose Reductase')
                if x == 39*3:
                  list.append('1-Aldose Reductase')
                if x < 49*3 and x > 39*3:
                  list.append('2-Aldose Reductase')
                if x < 39*3 and x > 29*3:
                  list.append('2-Aldose Reductase')
                if x == 39*4:
                  list.append('1Aldose Reductase')
                if x < 49*4 and x > 39*4:
                  list.append('2-Aldose Reductase')
                if x < 39*4 and x > 29*4:
                  list.append('2-Aldose Reductase')
                cmd.delete('aldoreductase')
                
                self.glutamine_amidotransferase2()
                x = cmd.count_atoms('glu_amidotransferase')
                if x == 25:
                  list.append('1-Glutamine Amidotransferase')
                if x < 33 and x > 25:
                  list.append('2-Glutamine Amidotransferase')
                if x < 25 and x > 17:
                  list.append('2-Glutamine Amidotransferase')
                if x == 25*2:
                  list.append('1-Glutamine Amidotransferase')
                if x < 33*2 and x > 25*2:
                  list.append('2-Glutamine Amidotransferase')
                if x < 25*2 and x > 17*2:
                  list.append('2-Glutamine Amidotransferase')
                if x == 25*3:
                  list.append('1-Glutamine Amidotransferase')
                if x < 33*3 and x > 25*3:
                  list.append('2-Glutamine Amidotransferase')
                if x < 25*3 and x > 17*3:
                  list.append('2-Glutamine Amidotransferase')
                if x == 39*4:
                  list.append('1-Glutamine Amidotransferase')
                if x < 33*4 and x > 25*4:
                  list.append('2-Glutamine Amidotransferase')
                if x < 25*4 and x > 17*4:
                  list.append('2-Glutamine Amidotransferase')
                cmd.delete('glu_amidotransferase')
                
                self.carboncarbon2()
                x = cmd.count_atoms('carboncarbon')
                if x == 25:
                  list.append('1-Carbon Carbon')
                if x < 33 and x > 25:
                  list.append('2-Carbon Carbon')
                if x < 25 and x > 17:
                  list.append('2-Carbon Carbon')
                if x == 25*2:
                  list.append('1-Carbon Carbon')
                if x < 33*2 and x > 25*2:
                  list.append('2-Carbon Carbon')
                if x < 25*2 and x > 17*2:
                  list.append('2-Carbon Carbon')
                if x == 25*3:
                  list.append('1-Carbon Carbon')
                if x < 33*3 and x > 25*3:
                  list.append('2-Carbon Carbon')
                if x < 25*3 and x > 17*3:
                  list.append('2-Carbon Carbon')
                if x == 39*4:
                  list.append('1-Carbon Carbon')
                if x < 33*4 and x > 25*4:
                  list.append('2-Carbon Carbon')
                if x < 25*4 and x > 17*4:
                  list.append('2-Carbon Carbon')
                cmd.delete('carboncarbon')
                
                self.carbanhyd2()
                x = cmd.count_atoms('carbonicanhydrase')
                if x == 32:
                  list.append('1-Carbonic Anhydrase')
                if x < 42 and x > 32:
                  list.append('2-Carbonic Anhydrase')
                if x < 32 and x > 22:
                  list.append('2-Carbonic Anhydrase')
                if x == 32*2:
                  list.append('1-Carbonic Anhydrase')
                if x < 42*2 and x > 32*2:
                  list.append('2-Carbonic Anhydrase')
                if x < 32*2 and x > 22*2:
                  list.append('2-Carbonic Anhydrase')
                if x == 32*3:
                  list.append('1-Carbonic Anhydrase')
                if x < 42*3 and x > 32*3:
                  list.append('2-Carbonic Anhydrase')
                if x < 32*3 and x > 22*3:
                  list.append('2-Carbonic Anhydrase')
                if x == 32*4:
                  list.append('1-Carbonic Anhydrase')
                if x < 42*4 and x > 32*4:
                  list.append('2-Carbonic Anhydrase')
                if x < 32*4 and x > 22*4:
                  list.append('2-Carbonic Anhydrase')
                cmd.delete('carbonicanhydrase')
                
                
                self.fisomerase2()
                x = cmd.count_atoms('fucoseisomerase')
                if x == 19:
                  list.append('1-Fucose Isomerase')
                if x < 24 and x > 19:
                  list.append('2-Fucose Isomerase')
                if x < 19 and x > 14:
                  list.append('2-Fucose Isomerase')
                if x == 19*2:
                  list.append('1-Fucose Isomerase')
                if x < 24*2 and x > 19*2:
                  list.append('2-Fucose Isomerase')
                if x < 19*2 and x > 14*2:
                  list.append('2-Fucose Isomerase')
                if x == 19*3:
                  list.append('1-Fucose Isomerase')
                if x < 24*3 and x > 19*3:
                  list.append('2-Fucose Isomerase')
                if x < 19*3 and x > 14*3:
                  list.append('2-Fucose Isomerase')
                if x == 19*4:
                  list.append('1-Fucose Isomerase')
                if x < 24*4 and x > 19*4:
                  list.append('2-Fucose Isomerase')
                if x < 19*4 and x > 14*4:
                  list.append('2-Fucose Isomerase')
                if x == 19*5:
                  list.append('1-Fucose Isomerase')
                if x < 24*5 and x > 19*5:
                  list.append('2-Fucose Isomerase')
                if x < 19*5 and x > 14*5:
                  list.append('2-Fucose Isomerase')
                
                cmd.delete('fucoseisomerase')
                
                self.tyrophos2()
                x = cmd.count_atoms('tyrophos')
                if x == 31:
                  list.append('1-Tyrosine Phosphatase')
                if x < 41 and x > 31:
                  list.append('2-Tyrosine Phosphatase')
                if x < 31 and x > 21:
                  list.append('2-Tyrosine Phosphatase')
                if x == 31*2:
                  list.append('1-Tyrosine Phosphatase')
                if x < 41*2 and x > 31*2:
                  list.append('2-Tyrosine Phosphatase')
                if x < 31*2 and x > 21*2:
                  list.append('2-Tyrosine Phosphatase')
                if x == 31*3:
                  list.append('1-Tyrosine Phosphatase')
                if x < 41*3 and x > 31*3:
                  list.append('2-Tyrosine Phosphatase')
                if x < 31*3 and x > 21*3:
                  list.append('2-Tyrosine Phosphatase')
                if x == 31*4:
                  list.append('1-Tyrosine Phosphatase')
                if x < 41*4 and x > 31*4:
                  list.append('2-Tyrosine Phosphatase')
                if x < 31*4 and x > 21*4:
                  list.append('2-Tyrosine Phosphatase')
                if x == 31*5:
                  list.append('1-Tyrosine Phosphatase')
                if x < 41*5 and x > 31*5:
                  list.append('2-Tyrosine Phosphatase')
                if x < 31*5 and x > 21*5:
                  list.append('2-Tyrosine Phosphatase')
                
                self.betainedehydrogenase2()
                x = cmd.count_atoms('betaine_dehydrogenase')
                if x == 23:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26 and x > 23:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23 and x > 20:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*2:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*2 and x > 23*2:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*2 and x > 20*2:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*3:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*3 and x > 23*3:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*3 and x > 20*3:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*4:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*4 and x > 23*4:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*4 and x > 20*4:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*5:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*5 and x > 20*5:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*5 and x > 20*5:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*6:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*6 and x > 23*6:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*6 and x > 20*6:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*7:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*7 and x > 23*7:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*7 and x > 20*7:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*8:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*8 and x > 23*8:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*8 and x > 20*8:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x == 23*9:
                  list.append('1-Betaine aldehyde dehydrogenase')
                if x < 26*9 and x > 23*9:
                  list.append('2-Betaine aldehyde dehydrogenase')
                if x < 23*9 and x > 20*9:
                  list.append('2-Betaine aldehyde dehydrogenase')
                
                self.serotoninacetyl2()
                x = cmd.count_atoms('Serotonin_transferase')
                if x == 44:
                   list.append('1-Serotonin Acetyltransferase')
                if x < 44 and x > 32:
                   list.append('2-Serotonin Acetyltransferase')
                if x == 24:
                   list.append('1-Serotonin Acetyltransferase')
                if x == 44*2:
                   list.append('1-Serotonin Acetyltransferase')
                if x < 44*2 and x > 32*2:
                   list.append('2-Serotonin Acetyltransferase')
                if x == 24*2:
                   list.append('1-Serotonin Acetyltransferase')
                if x == 44*3:
                   list.append('1-Serotonin Acetyltransferase')
                if x < 44*3 and x > 32*3:
                   list.append('2-Serotonin Acetyltransferase')
                if x == 24*3:
                   list.append('1-Serotonin Acetyltransferase')
                if x == 44*4:
                   list.append('1-Serotonin Acetyltransferase')
                if x < 44*4 and x > 32*4:
                   list.append('2-Serotonin Acetyltransferase')
                if x == 24*4:
                   list.append('1-Serotonin Acetyltransferase')
                
                cmd.delete('tyrophos')
                deletemotif()
                cmd.orient('all')
                list.sort()
                self.motifbox.setlist(list)
                cmd.show('cartoon', 'all')
                cmd.color('grey', 'all')
                return list
    
    framemot = Frame(interior)
    framemot.grid(row = 0, column = 0)
    ballmot = Pmw.Balloon(interior)
    ballmot.bind(framemot, 'Searches through all motifs\n1 = better, 2 = worse\nDouble click on returns to show')
    find_motif = Button(framemot, text ='Motif Finder')
    find_motif.grid(row = 0, column = 0)
    
    find_motif.bind('<Button-1>', motifchecker)
    
    
    self.motifbox = Pmw.ScrolledListBox(interior,
    items=(),
    listbox_height = 6,
    dblclickcommand=self.allmotif,
    usehullsize = 1,
    hull_width = 180,
    hull_height = 100,)
#Changed hull_height to 100 to see more - Corey
    self.motifbox.grid()