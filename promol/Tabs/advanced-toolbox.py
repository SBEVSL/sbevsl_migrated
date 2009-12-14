        page = notebook.add('Advanced\n Toolbox')#Making a new tab
        notebook.tab('Advanced\n Toolbox').focus_set()
        
        #--------------Mode---------------------
        group = Pmw.Group(page, tag_text='Mode:')
        group.grid(row=0, column=1, padx=2, pady=2, sticky=NW)
        interior = group.interior()
        framesculbtn = Frame(interior, width=16)
        framesculbtn.grid(row=0, column=0, padx=1, pady=1, sticky=NW)
        balloonsculpt = Pmw.Balloon(interior)
        balloonsculpt.bind(framesculbtn, "Ctrl + Right Click to drag an atom.\nCtrl + Left Click to rotate bonds.")
        sculbtn = Button(framesculbtn, text = 'Sculpting', width=16)
        sculbtn.grid(row=0, column=0, padx=1, pady=1, sticky=NW)
        #Defines Sculpting mode
        def sculpt(*args):
            cmd.hide('everything')
            cmd.set('sphere_transparency',0.60)
            cmd.set('sphere_color','white')
            cmd.set('auto_sculpt',1)
            cmd.mouse('three_button_editing')
            cmd.show('sticks')
            cmd.show('spheres')
            cmd.zoom('all',4)
        cmd.extend('sculpt',sculpt)
        sculbtn.bind('<Button-1>',sculpt)
      
      #-------------Measurment-------------------#
          #Measures distance between two atoms
        def dis(event):
          cmd.wizard('Distance')
        framedis = Frame(interior, width=16)
        framedis.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
        balldis = Pmw.Balloon(interior)
        balldis.bind(framedis, "Use internal GUI on PyMol\n to turn this mode off.")
        disbtn = Button(framedis, text = 'Measurement Tool', width=16)
        disbtn.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
        disbtn.bind('<Button-1>', dis)
        
        #Defines Sequence View Open and close
        #Defines Sequence View Open and close
        #opens Pymol sequence viewer, and can switch
        #between 4 diff modes, 1 letter aa, 3 letter aa, residue atoms, chains
        frameseq1 = Frame(interior, width=16)
        frameseq1.grid(row=2, column=0, padx=1, pady=1, sticky=NW)
        frameseq2 = Frame(interior, width=16)
        frameseq2.grid(row=3, column=0, padx=1, pady=1, sticky=NW)
        seqbtn1 = Button(frameseq1, text = "Sequence Viewer On", width=16)
        seqbtn1.grid(row=2, column=0, padx=1, pady=1, sticky=NW)
        seqbtn0 = Button(frameseq2, text = "Sequence Viewer Off", width=16)
        seqbtn0.grid(row=3, column=0, padx=1, pady=1, sticky=NW)
        def seqviewon(event):
          cmd.set('seq_view', 1)
        def seqviewoff(event):
          cmd.set('seq_view', 0)
        seqbtn1.bind('<Button-1>', seqviewon)
        seqbtn0.bind('<Button-1>', seqviewoff)
        seqformat = Entry(interior)
        
        labels = ("One letter", "Three letter", "AA atoms", "Chains")
        def seqviewformat(tag):
            if tag == 'One letter':
                cmd.set('seq_view_format', '0')
            elif tag == 'Three letter':
                cmd.set('seq_view_format', '1')
            elif tag == 'AA atoms':
                cmd.set('seq_view_format', '2')
            elif tag == 'Chains':
                cmd.set('seq_view_format', '3')
	self.radioAdd(interior, 'w', 'vertical', seqviewformat,
	              ' ', labels, 4, 0, 1, 1, 'NW')

        
        
        #------------Amino Acid Select------------------------------
        group = Pmw.Group(page, tag_text='Amino Acid Selector:')
 	group.grid(row=1, column=0, padx=2, pady=2, sticky=SW)
        interior = group.interior()
        labelaa = Label(interior, text = 'Code:')
        labelaa.grid(row=1, column=0, padx=2, pady=2)
        x = Entry(interior, width =5)
        x.grid(row=1, column=1, padx=2, pady=2)
        selecta = Button(interior, width = 15,text = 'Select Residues')
        selecta.grid(row=1, column=2, padx=2, pady=2)
        
        #-------------Residue Select------------------------
        labelr = Label(interior, text = ' Number:')
        labelr.grid(row=0, column=0, padx=2, pady=2)
        xr = Entry(interior, width =5)
        xr.grid(row=0, column=1, padx=2, pady=2)
        selectr = Button(interior, width = 15,text = 'Select Residues')
        selectr.grid(row=0, column=2, padx=2, pady=2)
        def selectresi(event):
            try:
                cmd.select('resi %s' % (xr.get()))
            except:
                print 'Invalid selection'
        selectr.bind('<Button-1>', selectresi)
        
        #----------Selection function for individual amino acids----------
        #-----Experienced people just use Sequence viewer, which is recommended----
        def selres(*args):
          if x.get() == 'ala' :
              cmd.select('alanine', 'resn ala')
          if x.get() == 'asn' :
              cmd.select('asparagine', 'resn asn')
          if x.get() == 'val' :
              cmd.select('valine', 'resn val')
          if x.get() == 'leu' :
              cmd.select('leucine', 'resn leu')
          if x.get() == 'ile' :
              cmd.select('isoleucine', 'resn ile')
          if x.get() == 'met' :
              cmd.select('methionine', 'resn met')
          if x.get() == 'pro' :
              cmd.select('proline', 'resn pro')
          if x.get() == 'phe' :
              cmd.select('phenylalanine', 'resn phe')
          if x.get() == 'tyr' :
              cmd.select('tyrosine', 'resn tyr')
          if x.get() == 'trp' :
              cmd.select('tryptophan', 'resn trp')
          if x.get() == 'ser' :
              cmd.select('serine', 'resn ser')
          if x.get() == 'thr' :
              cmd.select('threonine', 'resn thr')
          if x.get() == 'cys' :
              cmd.select('cysteine', 'resn cys')
          if x.get() == 'lys' :
              cmd.select('lysine', 'resn lys')
          if x.get() == 'arg' :
              cmd.select('arginine', 'resn arg')
          if x.get() == 'his' :
              cmd.select('histidine', 'resn his')
          if x.get() == 'asp' :
              cmd.select('aspartate', 'resn asp')
          if x.get() == 'glu' :
              cmd.select('glutamate', 'resn glu')
          if x.get() == 'gln' :
              cmd.select('glutamine', 'resn gln')
          if x.get() == 'a' :
              cmd.select('alanine', 'resn ala')
          if x.get() == 'n' :
              cmd.select('asparagine', 'resn asn')
          if x.get() == 'v' :
              cmd.select('valine', 'resn val')
          if x.get() == 'l' :
              cmd.select('leucine', 'resn leu')
          if x.get() == 'i' :
              cmd.select('isoleucine', 'resn ile')
          if x.get() == 'm' :
              cmd.select('methionine', 'resn met')
          if x.get() == 'p' :
              cmd.select('proline', 'resn pro')
          if x.get() == 'f' :
              cmd.select('phenylalanine', 'resn phe')
          if x.get() == 'y':
              cmd.select('tyrosine', 'resn tyr')
          if x.get() == 'w':
              cmd.select('tryptophan', 'resn trp')
          if x.get() == 's' :
              cmd.select('serine', 'resn ser')
          if x.get() == 't' :
              cmd.select('threonine', 'resn thr')
          if x.get() == 'c' :
              cmd.select('cysteine', 'resn cys')
          if x.get() == 'k' :
              cmd.select('lysine', 'resn lys')
          if x.get() == 'r' :
              cmd.select('arginine', 'resn arg')
          if x.get() == 'h' :
              cmd.select('histidine', 'resn his')
          if x.get() == 'd' :
              cmd.select('aspartate', 'resn asp')
          if x.get() == 'e' :
              cmd.select('glutamate', 'resn glu')
          if x.get() == 'q' :
              cmd.select('glutamine', 'resn gln')
        
        x.bind('<Return>', selres)
        selecta.bind('<Button-1>', selres)
        cmd.extend('selres',selres)
        
        
        #----------Set up scales for controlling how much of protein is roved----------
        
        
        group = Pmw.Group(page, tag_text='Electron Density Mapping')#And a new group
        group.grid(row=0, column=0, padx=2, pady=2, sticky=NW)
        interior = group.interior()
        framemesh = Frame(interior)
        framemesh.grid(row=0, column=0, padx=0, pady=2, sticky=W)
        framesurf = Frame(interior)
        framesurf.grid(row=2, column=0, padx=0, pady=2, sticky=W)
        framedots = Frame(interior)
        framedots.grid(row=1, column=0, padx=0, pady=2, sticky=W)
        framerov = Frame(interior)
        framerov.grid(row=3, column=0, padx=0, pady=2, sticky=W)
        framemeshsel = Frame(interior)
        framemeshsel.grid(row=0, column=1, padx=0, pady=2, sticky=W)
        framedotsel = Frame(interior)
        framedotsel.grid(row=1, column=1, padx=0, pady=2, sticky=W)
        framesurfsel = Frame(interior)
        framesurfsel.grid(row=2, column=1, padx=0, pady=2, sticky=W)
        imesh = Button (framemesh)#Mesh Button
        imesh.grid(row=0, column=0, padx=0, pady=2, sticky=W)
        imesh.configure(text="Mesh")
        imesh.configure(width="10")
        framecontour1 = Frame(interior)
        framecontour1.grid(row=5, column=1, padx=0, pady=0, sticky=NW)
        contour1  = Scale(framecontour1, width =8)
        contour1.configure(troughcolor="#ffffff")
        contour1.configure(length="100")
        contour1.configure(orient="horizontal")
        contour1.configure(resolution="0.05")
        contour1.configure(to="4.0")
        contour1.grid(row=4, column=1, padx=1, pady=0, sticky=W)
        contour1.set(1.0)
        frameradii = Frame(interior)
        frameradii.grid(row=6, column=1, padx=0, pady=0, sticky=N)
        ballradii = Pmw.Balloon(interior)
        ballradii.bind(frameradii, 'After changing detail, re-click on roving option')
        rovingradius1 = Scale(frameradii, width =8)
        rovingradius1.configure(troughcolor="#ffffff")
        rovingradius1.configure(length="100")
        rovingradius1.configure(orient="horizontal")
        rovingradius1.configure(resolution="0.1")
        rovingradius1.configure(to="15.0")
        rovingradius1.grid(row=6, column=1, padx=0, pady=0, sticky=N)
        rovingradius1.set(8.0)
        labrovrad = Label(interior, text = 'Roving Detail')
        labrovrad.grid(row=6, column=0, padx=5, pady=0, sticky=SE)
         
         
         #---isomesh function
        def emesh(*args):
            delcrea()
            try:
                cmd.isomesh('map1','map', contour1.get())
            except:
                try:
                    cmd.set("suspend_updates",1,quiet=1)
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isomesh("map1", "map", 9999.0, 'all')
                    cmd.set("suspend_updates",0,quiet=1)
                    cmd.isomesh('map1','map', contour1.get())
                    cmd.refresh()
                except: 
                    showinfo("Error", 'No PDB is present')
                    interior.mainloop()
        
        cmd.extend('emesh',emesh)
        imesh.bind('<Button-1>', emesh)
        idot = Button (framedots)
        idot.grid(row=1, column=0, padx=0, pady=2, sticky=W)
        idot.configure(text="Dots")
        idot.configure(width="10")
        #Isodot function
        def edot(*args):
            delcrea()
            try:
                cmd.isodot('map1','map', contour1.get())
            except:
               try:
                    cmd.set("suspend_updates",1,quiet=1)
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isodot("map1", "map", 9999.0, 'all')
                    cmd.set("suspend_updates",0,quiet=1)
                    cmd.refresh()
                    cmd.isodot('map1','map', contour1.get())
               except:
                    showinfo("Error", 'No PDB is present')
                    interior.mainloop()
        
        cmd.extend('edot',edot)
        idot.bind('<Button-1>', edot)
        
        isurf = Button(framesurf)
        isurf.grid(row=2, column=0, padx=0, pady=2, sticky=W)
        isurf.configure(text="Surface")
        isurf.configure(width="10")
        #Isosurface function
        def esurf(*args):
            delcrea()
            try:
                cmd.isosurface('map1','map', contour1.get())
            except:
                try:
                    cmd.set("suspend_updates",1,quiet=1)
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isosurface("map1", "map", 9999.0, 'all')
                    cmd.set("suspend_updates",0,quiet=1)
                    cmd.refresh()
                    cmd.isosurface('map1','map', contour1.get())
                except:
                    showinfo("Error", 'No PDB is present')
                    interior.mainloop()
        cmd.extend('esurf',esurf)
        isurf.bind('<Button-1>', esurf)

        
        
        rden = Button (framerov)
        rden.grid(row=3, column=0, padx=0, pady=2, sticky=W)
        rden.configure(text="Roving Mesh")
        rden.configure(width="10")
        #roving isomesh function
        #From DeLano's code, need to cite
        def roving_density(self):
          delcrea()
          try:
            cmd.set("suspend_updates",1,quiet=1)
            cmd.remove("hydro")
            cmd.disable()
            cmd.enable('all')
            cmd.map_new('map',"gaussian","0.75", 'all')
            cmd.set('roving_isomesh', rovingradius1.get())
            cmd.set("roving_detail",1)
            cmd.set("stick_radius",0.5)
            cmd.set("roving_sticks",0)
            cmd.set('roving_lines', rovingradius1.get())
            cmd.set("roving_polar_contacts",0)
            cmd.set("line_width","3")
            cmd.set("roving_map1_name",'map')
            cmd.isomesh("map1", "map", 9999.0, 'all')
            cmd.set("suspend_updates",0,quiet=1)
            cmd.refresh()
            cmd.delete('rov_s1')
            cmd.set('roving_isosurface',0)
          
          except:
            
            
            showinfo("Error", 'No PDB is present')
            interior.mainloop()
        cmd.extend('roving_density',roving_density)
        rden.bind ('<Button-1>', roving_density)
        
        def roving_surface(self):
            delcrea()
            try:
                
                cmd.remove("hydro")
                cmd.disable()
                cmd.enable('all')
                cmd.map_new('map',"gaussian","0.75", 'all')
                cmd.set("roving_detail",1)
                cmd.set("roving_origin",1)
                cmd.set('roving_lines', 8)
                cmd.set("roving_polar_contacts",0)
                cmd.set("line_width","3")
                cmd.set("roving_map1_name",'map')
                cmd.set('roving_isosurface', rovingradius1.get())
                cmd.show('lines', 'all')
                cmd.set('roving_isomesh', '0')
                cmd.set('transparency', '0.15')
                cmd.delete('rov_1')
                cmd.delete('rov_m1')
            
            except:
                
                
                showinfo("Error", 'No PDB is present')
                interior.mainloop()
        framerovs = Frame(interior)
        framerovs.grid(row=4, column=0, padx=0, pady=2, sticky=W)
        surfacing = Button(framerovs, width = 10)
        surfacing.grid(row=4, column=0, padx=0, pady=2, sticky=W)
        surfacing.configure(text = 'Rove Surface')
        surfacing.bind('<Button-1>', roving_surface)
    #----------Electron Density Map on only Selection------------------------
        labelcon = Label(interior, text = '  Contour')
        labelcon.grid(row=5, column=0, padx=5, pady=2, sticky=S)
        imesh1 = Button (framemeshsel)
        imesh1.grid(row=0, column=1, padx=0, pady=2, sticky=W)
        imesh1.configure(text="Mesh Select")
        imesh1.configure(width="10")
        #isomesh on only selection
        
        def emesh1(event):
            delcrea()
            try:
                cmd.isomesh('map1','map', contour1.get(), 'sele')
            except:
                try:
                    
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isomesh('map1','map', contour1.get(), 'sele')
                
                except:
                    cmd.orient('all')
                    
                    
                    showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
                    
                    interior.mainloop()
        
        imesh1.bind('<Button-1>', emesh1)
        idot1 = Button (framedotsel)
        idot1.grid(row=1, column=1, padx=0, pady=2, sticky=W)
        idot1.configure(text="Dots Select")
        idot1.configure(width="10")
        #isodot on only selection
        def edot1(event):
            delcrea()
            try:
                cmd.isodot('map1','map', contour1.get(), 'sele')
            except:
                try:
                    cmd.set("suspend_updates",1,quiet=1)
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isodot("map1", "map", 9999.0, 'all')
                    cmd.set("suspend_updates",0,quiet=1)
                    cmd.refresh()
                    cmd.isodot('map1','map', contour1.get(), 'sele')
                    cmd.get_names('all')
                except:
                    cmd.orient('all')
                    
                    showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
                    interior.mainloop()
        
        idot1.bind('<Button-1>', edot1)
        isurf1 = Button(framesurfsel)
        isurf1.grid(row=2, column=1, padx=0, pady=2, sticky=W)
        isurf1.configure(text="Surface Select")
        isurf1.configure(width="12")
        #isosurface on only selection
        def esurf1(event):
            delcrea()
            try:
                cmd.isosurface('map1','map', contour1.get(), 'sele')
            except:
                try:
                    cmd.set("suspend_updates",1,quiet=1)
                    cmd.remove("hydro")
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isosurface("map1", "map", 9999.0, 'all')
                    cmd.set("suspend_updates",0,quiet=1)
                    cmd.refresh()
                    cmd.isosurface('map1','map', contour1.get(), 'sele')
                except:
                    cmd.orient('all')
                    showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
                    interior.mainloop()
        
        isurf1.bind('<Button-1>', esurf1)
        
        
        frame = Frame(interior)
        frame.grid(row=3, column=1, padx=0, pady=0, sticky=SW)
        doublemapbtn = Button(frame, text = 'Double resolution')
        doublemapbtn.grid(row=3, column=1, padx=0, pady=0, sticky=SW)
        
        balloon = Pmw.Balloon(interior)
        balloon.bind(frame, "Please be patient.\nButton can only be used once.\nPyMol will close if used twice.")
        
        #doubles map resolution (permanent because Pymol has errors associated
        #with halving the map resolution)
        def doublemapres(event):
            try:
                cmd.map_double('map', '1')
            except:
                showinfo("Error", 'No map is present')
                interior.mainloop()
        doublemapbtn.bind('<Button-1>', doublemapres)#workspot
        
        # 99 red balloons, floating in a summer sky
        
        balloon1 = Pmw.Balloon(interior)
        balloon1.bind(framemesh, '''Display entire map as a mesh.''')
        balloon2 = Pmw.Balloon(interior)
        balloon2.bind(framedots, '''Display entire map as dots.''')
        balloon3 = Pmw.Balloon(interior)
        balloon3.bind(framesurf, '''Display entire map as surface.''')
        balloon4 = Pmw.Balloon(interior)
        balloon4.bind(framerov, "View small portions of map at a time\n using middle mouse button to scan across.")
        balloon45 = Pmw.Balloon(interior)
        balloon45.bind(framerovs, "View small portions of map at a time\n using middle mouse button to scan across.")
        balloon5 = Pmw.Balloon(interior)
        balloon5.bind(framemeshsel, "Must have PDB loaded.\n Display mesh on only selected residues (sele).")
        balloon6 = Pmw.Balloon(interior)
        balloon6.bind(framedotsel, "Must have PDB loaded.\n Display dots on only selected residues (sele).")
        balloon7 = Pmw.Balloon(interior)
        balloon7.bind(framesurfsel, "Must have PDB loaded.\n Display surface on only selected residues (sele).")
        balloon11 = Pmw.Balloon(interior)
        balloon11.bind(framecontour1, "After altering countour click again\n on map view of choice for change to occur.")
        def loadmapps(event):
            root = Tk()
            group = Pmw.Group(root, tag_text='Electron Density Mapping')#And a new group
            group.grid(row=0, column=0, padx=0, pady=0, sticky=NW)
            interior = group.interior()
            framemesh = Frame(interior)
            framemesh.grid(row=2, column=0, padx=0, pady=2, sticky=W)
            framesurf = Frame(interior)
            framesurf.grid(row=4, column=0, padx=0, pady=2, sticky=W)
            framedots = Frame(interior)
            framedots.grid(row=3, column=0, padx=0, pady=2, sticky=W)
            framemeshsel = Frame(interior)
            framemeshsel.grid(row=2, column=1, padx=0, pady=2, sticky=W)
            framedotsel = Frame(interior)
            framedotsel.grid(row=3, column=1, padx=0, pady=2, sticky=W)
            framesurfsel = Frame(interior)
            framesurfsel.grid(row=4, column=1, padx=0, pady=2, sticky=W)
            framenameit = Frame(interior)
            framenameit.grid(row=0, column=1, padx=0, pady=2, sticky=SW)
            framepdbname = Frame(interior)
            framepdbname.grid(row=1, column=1, padx=0, pady=2, sticky=SW)
            framemapper = Frame(interior)
            framemapper.grid(row=4, column=2, padx=0, pady=2, sticky=W)
            imesh = Button (framemesh)#Mesh Button
            imesh.grid(row=2, column=0, padx=0, pady=2, sticky=W)
            imesh.configure(text="Mesh")
            imesh.configure(width="10")
            nameit = Entry (framenameit, width = 8)#Name Object Entry
            nameit.grid(row=0, column=1, padx=0, pady=0, sticky=SW)
            pdbname = Entry (framepdbname, width = 8)#Map Filename Entry
            pdbname.grid(row=1, column=1, padx=0, pady=0, sticky=SW)
            labelno = Label(interior, text = 'Name Object:')#Label for Object
            labelno.grid(row=0, column=0, padx=0, pady=0, sticky=SW)
            labelid = Label(interior, text = 'Map Filename:')#Label for Filename
            labelid.grid(row=1, column=0, padx=0, pady=0, sticky=SW)
            ehelp = Button (interior)
            ehelp.grid(row=5, column=0, padx=0, pady=2, sticky=W)
            ehelp.configure(text="Help")
            ehelp.configure(width="10")
            getmapper = Entry(interior, width = 4)
            getmapper.grid(row=3, column=2, padx=2, pady=2, sticky=SW)
            loadbtn = Button(interior, text = "Load Map")
            loadbtn.grid(row=5, column=2, padx=4, pady=2, sticky=W)
            def loadccp4(event):
              
              file = askopenfilename(defaultextension=".ccp4", initialdir="./PyMOL/")
              if len(file)>0:
                cmd.load(file)
              interior.mainloop()
            loadbtn.bind('<Button-1>', loadccp4)
            #go to upsalla website for maps
            def getmap(self):
                import webbrowser
                webbrowser.open('http://eds.bmc.uu.se/cgi-bin/eds/gen_maps_zip.pl?pdbCode='+ getmapper.get())
            mapper = Button (framemapper)
            mapper.grid(row=4, column=2, padx=0, pady=5, sticky=W)
            mapper.configure(text="Get Map")
            mapper.configure(width="10")
            
            labelcon = Label(interior, text = 'Input PDB code')
            labelcon.grid(row=2, column=2, padx=0, pady=2, sticky=SW)
            framecontour1 = Frame(interior)
            framecontour1.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
            contour1  = Scale(framecontour1, width =8)
            contour1.configure(troughcolor="#ffffff")
            contour1.configure(length="65")
            contour1.configure(orient="horizontal")
            contour1.configure(resolution="0.05")
            contour1.configure(to="4.0")
            contour1.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
            contour1.set(1.0)
            
            mapper.bind('<Button-1>', getmap)
            
            
            def elhelp(event):
                import webbrowser
                webbrowser.open('./modules/pmg_tk/startup/EDMHelp.htm')
            ehelp.bind('<Button-1>', elhelp)
             #---isomesh function
            def emesh(event):
                delcrea()
                try:
                    if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    
                    else:
                        cmd.isomesh(nameit.get(),pdbname.get(), contour1.get())
                except:
                    
                    
                    showinfo("Error", 'No map is present')
                    interior.mainloop()

            
            
            imesh.bind('<Button-1>', emesh)
            idot = Button (framedots)
            idot.grid(row=3, column=0, padx=0, pady=5, sticky=W)
            idot.configure(text="Dots")
            idot.configure(width="10")
            #Isodot function
            def edot(event):
                delcrea()
                try:
                     if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                     elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                     else:
                        cmd.isodot(nameit.get(), pdbname.get(), contour1.get())
                except:
                     
                     
                     showinfo("Error", 'No map is present')
                     interior.mainloop()
            
            idot.bind('<Button-1>', edot)
            isurf = Button(framesurf)
            isurf.grid(row=2, column=1, padx=0, pady=5, sticky=W)
            isurf.configure(text="Surface")
            isurf.configure(width="10")
            #Isosurface function
            def esurf(event):
                delcrea()
                try:
                    if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    else:
                        cmd.isosurface(nameit.get(), pdbname.get(), contour1.get())
                except:
                    
                    
                    showinfo("Error", 'No map is present')
                    interior.mainloop()
            
            isurf.bind('<Button-1>', esurf)

    
    
    #----------Electron Density Map on only Selection------------------------
            labelcon = Label(interior, text = '  Contour')
            labelcon.grid(row=0, column=2, padx=0, pady=2, sticky=SW)
            imesh1 = Button (framemeshsel)
            imesh1.grid(row=4, column=0, padx=0, pady=5, sticky=W)
            imesh1.configure(text="Mesh Select")
            imesh1.configure(width="10")
            #isomesh on only selection
            
            def emesh1(*args):
                delcrea()
                try:
                    if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    
                    else:
                        cmd.isomesh(nameit.get(),pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    
                    
                    showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
                    interior.mainloop()
            cmd.extend('emesh1',emesh1)
            imesh1.bind('<Button-1>', emesh1)
            idot1 = Button (framedotsel)
            idot1.grid(row=5, column=0, padx=0, pady=2, sticky=W)
            idot1.configure(text="Dots Select")
            idot1.configure(width="10")
            #isodot on only selection
            def edot1(event):
                delcrea()
                try:
                     if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                     elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                     else:
                        cmd.isodot(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    
                    
                    showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
                    interior.mainloop()
            
            
            idot1.bind('<Button-1>', edot1)
            isurf1 = Button(framesurfsel)
            isurf1.grid(row=4, column=1, padx=0, pady=2, sticky=W)
            isurf1.configure(text="Surface Select")
            isurf1.configure(width="12")
            #isosurface on only selection
            def esurf1(event):
                delcrea()
                try:
                    if len(nameit.get()) < 1:
                        
                        
                        showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        
                        
                        showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    
                    else:
                        cmd.isosurface(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    
                    
                    showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
                    interior.mainloop()
            
            isurf1.bind('<Button-1>', esurf1)
            
            
            frame = Frame(interior)
            frame.grid(row=5, column=1, padx=0, pady=0, sticky=SW)
            doublemapbtn = Button(frame, text = 'Double resolution')
            doublemapbtn.grid(row=5, column=1, padx=0, pady=3, sticky=SW)
            
            balloon = Pmw.Balloon(interior)
            balloon.bind(frame, "Please be patient.\nButton should only be used once.\nPyMol will close if used twice.")
            
            #doubles map resolution (permanent because Pymol has errors associated
            #with halving the map resolution)
            def doublemapres(*args):
                try:
                    cmd.map_double(pdbname.get(), '1')
                
                except:
                    
                    
                    showinfo("Error", 'No map is present')
                    interior.mainloop()
            doublemapbtn.bind('<Button-1>', doublemapres)
            cmd.extend('doublemapres',doublemapres)
            # 99 red balloons, floating in a summer sky
            balloon1 = Pmw.Balloon(interior)
            balloon1.bind(framemesh, "Display entire map as a mesh.")
            balloon2 = Pmw.Balloon(interior)
            balloon2.bind(framedots, "Display entire map as dots.")
            balloon3 = Pmw.Balloon(interior)
            balloon3.bind(framesurf, "Display entire map as surface.")
            balloon5 = Pmw.Balloon(interior)
            balloon5.bind(framemeshsel, "Must have PDB loaded.\n Display mesh on only selected residues (sele).")
            balloon6 = Pmw.Balloon(interior)
            balloon6.bind(framedotsel, "Must have PDB loaded.\n Display dots on only selected residues (sele).")
            balloon7 = Pmw.Balloon(interior)
            balloon7.bind(framesurfsel, "Must have PDB loaded.\n Display surface on only selected residues (sele).")
            balloon8 = Pmw.Balloon(interior)
            balloon8.bind(framenameit, "After loading map, must name the object\n to allow for more than one map instance.")
            balloon9 = Pmw.Balloon(interior)
            balloon9.bind(framepdbname, "After loading map, must enter filename\n of map to be viewed for PyMol to use it.")
            balloon10 = Pmw.Balloon(interior)
            balloon10.bind(framemapper, "View Help button for information on getting maps.")
            balloon11 = Pmw.Balloon(interior)
            balloon11.bind(framecontour1, "After altering countour click again\n on map view of choice for change to occur.")
        
        framemapdoer = Frame(interior)
        framemapdoer.grid(row=4, column=1, padx=0, pady=5, sticky=NW)
        balloon972 = Pmw.Balloon(interior)
        balloon972.bind(framemapdoer, "For advanced users only\nRequires external map download")
        loadmapbtn =  Button(framemapdoer, text = 'External map')
        loadmapbtn.grid(row=4, column=1, padx=0, pady=5, sticky=NW)
        loadmapbtn.bind('<Button-1>', loadmapps)
        
        #------------Fetch Ramachandran Plot --------------------
        group = Pmw.Group(page, tag_text='Ramachandran Plot:')
 	group.grid(row=1, column=1, padx=2, pady=2, sticky=SW)
        interior = group.interior()
        framebtn1 = Frame(interior)
        framebtn1.grid(row=1, column=0, padx=2, pady=2, sticky=NE)
        balloon12 = Pmw.Balloon(interior)
        balloon12.bind(framebtn1, "Must have internet connection, goes to external website.")
        Labelpdb = Label(interior, text = 'Enter PDB code:')
        Labelpdb.grid(row=0, column=0, columnspan = 2, padx=2, pady=2, sticky=NW)
        enterpdb = Entry(interior, width=6)
        enterpdb.grid(row=1, column=1, padx=2, pady=4, sticky=NW)
        btn1 = Button(framebtn1, text = 'Fetch Plot', width = 10)
        btn1.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
        def fetchurl(self):
            import webbrowser
            webbrowser.open('http://eds.bmc.uu.se/cgi-bin/eds/rama?pdbCode='+enterpdb.get())
        
        
        btn1.bind('<Button-1>', fetchurl)