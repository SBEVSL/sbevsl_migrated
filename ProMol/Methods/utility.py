from pymol import cmd
import Tkinter as tk
import Pmw
from pmg_tk.startup.ProMol import promolglobals as glb
Pmw.initialise()

# ADD RADIO BUTTONS
# Create and add radio buttons to the GUI
def radioAdd(frame, pos, orient, cmd, label, btn_labels, gridrow,
         gridcol, cspan, rspan, gridstick):
    labels = btn_labels     #the list of labels passed in by the user

    # create the radio button
    newRadio = Pmw.RadioSelect(frame, labelpos = pos, labelmargin = 0,
                    buttontype = 'radiobutton',
                    orient = orient,
                    label_text = label,
                    command = cmd)
     # add it to the gui
    newRadio.grid(row = gridrow, column = gridcol, columnspan = cspan,
             rowspan = rspan, sticky = gridstick, padx = 5)

    # add text to the buttons
    for text in labels:
        newRadio.add(text)
        newRadio.setvalue(labels[0])

def showaminopic():
    dimension = glb.GUI.toolbox['picdimension'].get()
    text = glb.GUI.toolbox['aminoimage'].get().lower()
    try:
        amino = glb.AminoHashTable[text][3].upper()
        glb.GUI.toolbox['aminocanvas'].create_image(0, 0,
            image=glb.Photos['%s%s' % (amino, dimension)], anchor=tk.NW)
    except KeyError:
        pass

def dis(event):
    cmd.wizard('Distance')

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
        file = askopenfilename(defaultextension=".ccp4", initialdir=glb.HOME)
        if len(file)>0:
            cmd.load(file)
        interior.mainloop()
    loadbtn.bind('<Button-1>', loadccp4)
    #go to upsalla website for maps
    def getmap():
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
        webbrowser.open(glb.pathmaker('EDMHelp.htm'))
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
