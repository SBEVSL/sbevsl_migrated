from Tkinter import *
import Pmw
import pymol
from pymol import cmd
#from pymol import importing
import tkColorChooser
import re
import string

Pmw.initialise()

#---------------------------------------------------------------
# Link our GUI to PyMOL
#---------------------------------------------------------------
def __init__(self):
  self.menuBar.addmenuitem('Plugin', 'command',
                           'Easy GUI',
                           label = 'EZ-Viz',
                           command = lambda s=self : PGUI(s))
#---------------------------------------------------------------#
#								#
#                       PDBParser                               #
#								#
#								#
#								#
#       Parse PDB files and pull out the useful information     #
#								#
#---------------------------------------------------------------#
class PDBParser:
	
	global true
	#------Constructor----------
	def __init__(self):
		#self.filename=filename
		self.author = ''
		self.true=1
		self.title = ''
		self.ref = ''
		self.journal = ''
		self.name=''
		self.hetero=''
		self.hlist=[]
		self.chains={}
		self.classify=''
		self.idList=[]
		self.allHet=[]
		self.helices=[]
	
	
	# Read in the PDB file line by line
	# Call method depending on what line starts with
	def readFile(self, file):
  		in_file = open(file, 'r')
  		j=re.compile("^JRNL")
  		h=re.compile("^HEADER")
  		t=re.compile("^TITLE")
  		c=re.compile("^COMPND")
  		ht=re.compile("^HET ")
  		s=re.compile("^SEQRES")
  		hel=re.compile("^HELIX")

  		while self.true:
  			line=in_file.readline()
  			if line == "":
              			break
          		line = line[:-1]
          		#Molecular Classification
          		if h.match(line):
          			self.classify=string.strip(line[10:50])
          		#Molecule Name
          		elif t.match(line):
          			temp=string.strip(line[10:70])
          			self.name=self.name+' '+temp
          		elif c.match(line) and self.name=='':
          			temp=string.strip(line[10:70])
          			self.name=self.name+' '+temp
          		#Journal Entry
          		elif j.match(line):
          			self.getJrnl(line)
          		#Hetero Atoms
          		elif ht.match(line):
          			self.getHet(line)
          		elif s.match(line):
          			self.getSeq(line)
          		# find out if regular expression was found
        		elif hel.match(line):
            			#print 'HELIX FOUND: ' + line
            			self.get_helix_entry(line)
          	self.hetero=string.join(self.hlist, sep=', ')
          	self.journal=self.author+"\n"+self.title+"\n"+self.ref
      		in_file.close()
  	
  	# Get journal entry information
    	def getJrnl(self, line):
  		temp2=[]
  		a=re.compile("AUTH")
  		t=re.compile("TITL")
  		r=re.compile("REF")
  		if a.match(line[12:18]):
  			self.author = self.author+string.strip(line[19:70])
  		if t.match(line[12:18]):
  				self.title = self.title+" "+string.strip(line[19:70])
  		if r.match(line[12:18]):
  			st = string.strip(line[19:70])
  			temp=string.split(st)
  			temp2.append(temp)
  			for list in temp2:
  				for item in list:
  					self.ref = self.ref+' '+item
  					
  	#Get list of hetero atoms found in molecule
  	def getHet(self, line):
  		temp = string.strip(line[7:10])
  		id = string.strip(line[13:17])
  		if self.hlist.count(temp)==0:
  			self.hlist.append(temp)
  			#self.idList.append(id)
  		else:
  			pass
  		chain=string.strip(line[11:13])
  		if chain == "":
  			id = 'resi '+ id
  		else:
  			id = chain+"/"+id+"/"
  		self.idList.append(id)
  	#Get sequence/chain information
 	def getSeq(self, line):
 		chainID = line[11]
 		seq = string.strip(line[19:70])
 		if self.chains.has_key(chainID):
 			temp =self.chains[chainID]
 			seq =temp+' '+seq
 			self.chains[chainID]=seq
 		else:
 			self.chains[chainID]=seq
 	
 	# Get Helix start/stop locations
	# (adds a helix object to an array)
	def get_helix_entry(self, line):
	        start = string.strip(line[21:25])
	 	end = string.strip(line[33:37])
	 	chain = string.strip(line[19:20])
	 	tempHelix = Helix(start,end,chain)
	 	self.helices.append(tempHelix)
 		
 		
#---------------------------------------------------------------#
#								#
#                     Helix Class                               #
#								#
#								#
#								#
#              Helix Objects (used in movies)                   #
#								#
#---------------------------------------------------------------#
class Helix:
   
    def __init__(self, start, end, chain):
    	self.start = start
        self.end = end
        self.chain = chain

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end    
        		
    def getChain(self):
    	return self.chain

#---------------------------------------------------------------#
#								#
#                     Chime Converter                           #
#								#
#								#
#								#
#              Handle the entry of Chime commands               #
#								#
#---------------------------------------------------------------#

class ChimeConverter: 	
     
    #------Constructor----------
    def __init__(self):
        # initialize variables
	self.cmdLine = ' '
	self.command = ' '
	self.results = ' '
	self.args = []
	self.argsLength = 0
	self.rpsts = {'cartoon':'cartoon',
		      'cartoons':'cartoon',
		      'backbone':'ribbon', 
		      'spacefill':'spheres',
		      'dots':'dots',
		      'wireframe':'lines',
		      'ribbons':'cartoon',
		      'ribbon':'cartoon'}

	self.coloring={'colour':'color',
		       'color':'color',
		       'background':'bg_color'}
	
	self.individuals={'center':'zoom',
			  'centre':'zoom'}
		
	self.selections={'dna':'resn a+g+c+t+u',
		         'protein':'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+MSE',
			 'hydrophobic':'resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL',
			 'hydrophilic':'resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS',
			 'acidic':'resn ASP+GLU',
			 'basic':'resn ARG+HIS+LYS'}
    # parse the command
    def parseIt(self, input, commLine, resultBox):
        
        self.cmdLine = commLine
        self.results = resultBox
	
	# get rid of capitalizations and leading/ending
	# white space
        ui = input.lower()
        ui = ui.strip()
        
        # store the command
        self.args = ui.split()
        self.argsLength = len(self.args)
        
        self.command = self.args[0]

  	# representations
  	if self.command in self.rpsts.keys():
  		# repeat the command back to the user
		self.results.appendtext('Chime: ' + ui + '\n')
  		self.on_off_conversions()
  		
  	# coloring stuff
  	elif self.command in self.coloring.keys():
  		# repeat the command back to the user
	        self.results.appendtext('Chime: ' + ui + '\n')
  		self.coloring_conversions()

  	# commands without additional arguments
  	elif self.command in self.individuals.keys():
  		# repeat the command back to the user
	        self.results.appendtext('Chime: ' + ui + '\n')
  		self.convert_individual()
  	
  	# action commands ( such as spin )	
        elif self.command == 'spin':
        	self.results.appendtext('Chime: ' + ui + '\n')
        	self.convert_spin()
        	
  	# selections from the user
  	elif self.command == 'select':
  		self.results.appendtext('Chime: ' + ui + '\n')
  		self.convert_selections()
	# if the command is not recognized, let the user know  	 	
  	else:
  		self.results.appendtext('Error:  Chime command not recognized.\n\n')
	
	self.cmdLine.clear() 
	#self.cmdLine.focus_force()
    #-----------------------------------------#  	
    #        Chime Conversion Methods         #
    #-----------------------------------------#
    
    # handle on/off type commands
    def on_off_conversions(self):
	pymShow = 'PyMOL: show '+ self.rpsts[self.command] + ', all\n\n'
	pymHide = 'PyMOL: hide ' + self.rpsts[self.command]+ ', all\n\n'
	if self.args[0] == 'backbone': 
	    cmd.hide('everything')
	    cmd.show('ribbon','all')
	    pymShow = 'PyMOL: hide everything; show '+ self.rpsts[self.command] + ', all\n\n'
	
	if self.argsLength > 1:
            switch = self.args[1]
            if switch == 'on': 
                cmd.show(self.rpsts[self.command],'all')
                self.results.appendtext(pymShow)
            else:
                cmd.hide(self.rpsts[self.command],'all')
                self.results.appendtext(pymHide)
        else: 
            cmd.show(self.rpsts[self.command],'all')
            self.results.appendtext(pymShow)
       	
    # background command
    def coloring_conversions(self):
        selections = cmd.get_names('all')
        currentSel = selections[len(selections)-1]
        #print currentSel
    	if self.argsLength > 1:
       	    pymCmd = 'PyMOL: '+self.coloring[self.command]+' '+self.args[1]
       	    if self.command=='color' or self.command=='colour':
       	        cmd.color(self.args[1],currentSel)
		pymCmd = pymCmd + ', '+currentSel+'\n\n'
       	    elif self.command=='background':
       	    	cmd.bg_color(self.args[1])
       	    	pymCmd = pymCmd + '\n\n'
       	    	
       	    self.results.appendtext(pymCmd)
       	    
       	else:
       	    self.results.appendtext('Usage: '+self.command+' + [color]\n\n')
    
    def convert_spin(self):
        pymSpin = 'PyMOL: mset 1 x180; util.mroll(1,180,1); mplay\n\n'
        if self.argsLength > 1:
            if self.args[1] == 'off': 
                cmd.do('mstop; mset')
                pymSpin = 'PyMOL: mstop; mset\n\n'
            else:
                cmd.do('mset 1 x180; util.mroll(1,180,1);mplay')
        else:
            cmd.do('mset 1 x180; util.mroll(1,180,1);mplay')
        self.results.appendtext(pymSpin)
            
    # convert chime selections
    def convert_selections(self):
       	if self.argsLength > 1:
     	    pymSelect = 'PyMOL: select '+self.selections[self.args[1]]+'\n\n'
     	    self.results.appendtext(pymSelect)
     	    cmd.select(self.selections[self.args[1]])
    	else:
     	    self.results.appendtext('Usage: select [selection]')
   	    
    # 'individual command' conversions
    def convert_individual(self):
        pymShow = 'PyMOL: '+self.individuals[self.command]+'\n\n' 
        cmd.do(self.individuals[self.command])
        self.results.appendtext(pymShow)
    
#---------------------------------------------------------------#
#								#
#                           GUI Class                           #
#								#
#								#
#								#
#	           The look of the interface		        #
#								#
#---------------------------------------------------------------#
class PGUI:
    global defaultImage
    global chains
    global heteroImg
    global ballStickImg
    global ligand
    global name
    global surfaceImg
    global cmdType  
    global polarityImg
    global aromaticsImg
    global puttyImg
    global dnaImg
    global build
    global chainsMovieImg
    global playButton
    global stopButton
    global rewindButton
    global rotateImg
    global splash
    
    # Images used in Presets tab
    defaultImage = PhotoImage( file="modules\pmg_tk\startup\default.gif")
    chains = PhotoImage(file="modules\pmg_tk\startup\chains.GIF")
    heteroImg = PhotoImage(file="modules\pmg_tk\startup\heteroAtom.GIF")
    ballStickImg = PhotoImage(file="C:\Program Files\DeLano Scientific\PyMOL\modules\pmg_tk\startup\showBallStick.GIF")
    surfaceImg = PhotoImage(file="modules\pmg_tk\startup\surface.GIF")
    polarityImg = PhotoImage(file="modules\pmg_tk\startup\polarity.GIF")
    puttyImg = PhotoImage(file="modules\pmg_tk\startup\putty.GIF")
    aromaticsImg = PhotoImage(file="modules\pmg_tk\startup\showAromatics.GIF")
    dnaImg = PhotoImage(file="modules\pmg_tk\startup\dna.GIF")
    
    # Movie tab images
    ligand = PhotoImage(file="modules\pmg_tk\startup\zoom.GIF")
    build = PhotoImage(file="modules\pmg_tk\startup\prot.GIF")
    chainsMovieImg = PhotoImage(file="modules\pmg_tk\startup\chainsMovie.GIF")
    rotateImg = PhotoImage(file="modules\pmg_tk\startup\Rotate.GIF")
    playButton = PhotoImage(file="modules\pmg_tk\startup\play.GIF")
    stopButton = PhotoImage(file="modules\pmg_tk\startup\stop.GIF")
    rewindButton = PhotoImage(file="modules\pmg_tk\startup\Rewind.GIF")
    
    # Welcome tab image
    splash = PhotoImage(file="modules\pmg_tk\startup\splash.GIF")
    #--------------------------------------#
    #					   #
    #         PRESETS METHODS              #
    #                                      #
    #--------------------------------------#
    def set_defaults(self):
        transparencies = ['transparency','cartoon_transparency','stick_transparency','sphere_transparency']
	for i in transparencies:
	    cmd.set(i,'0.0','all')
	    
	list = cmd.get_names()    
        for i in list:
            cmd.hide('everything',i)
            cmd.set('transparency','0.0',i)
            cmd.set('cartoon_transparency','0.0',i)
            cmd.set('transparency','0',i)
            cmd.set('sphere_transparency','0.0',i)
            cmd.set('stick_transparency','0.0',i)
            cmd.set('sphere_scale','0.7',i)
            cmd.cartoon('automatic',i)
            cmd.set('stick_radius','0.2',i)

        cmd.hide('everything','all')
            
    # emphasize DNA
    def show_dna_rna(self):
    	import tkMessageBox
    	points = 0
    	objects = cmd.get_names('all')
    	if 'dna' in objects or 'rna' in objects:
	    self.set_defaults()
    	    if 'dna' in objects:
    	        cmd.show('sticks', 'dna')
    	        self.color_cpk(' & dna')
    	        points = points + 1
    	    
    	    if 'rna' in objects:
    	        cmd.show('sticks', 'rna')
    	        self.color_cpk(' & rna')
	        if 'dna' in objects:
	            cmd.show('spheres','rna')
    	            cmd.set('sphere_scale','0.4','rna')
	        points = points + 2
	
	    if 'protein' in objects:
	        cmd.show('cartoon','protein')
	        cmd.color('red','protein')
	        cmd.set('cartoon_transparency','0.7','protein')
	    if 'ligands' in objects:
	    	cmd.show('spheres','ligands')
	    	cmd.set('sphere_transparency','0.7','ligands')
	    	cmd.set('sphere_scale','0.4','ligands')

	    if points == 3:
	        tkMessageBox.showinfo('Distinguishing RNA and DNA','RNA = Ball and Stick\n'
	        		       + 'DNA = Sticks only')
	    elif points == 1: 
	        tkMessageBox.showinfo('Notice:','There is no RNA present in this molecule.')
	    elif points == 2: 
	        tkMessageBox.showinfo('Notice:','There is no DNA present in this molecule.')	        	    
    	else:
   	    tkMessageBox.showinfo("Error", "There is no DNA or RNA in this molecule.")
	    

    	    
    # default view
    def std_view(self):
	self.set_defaults()
	objects = cmd.get_names('all')
	if 'protein' in objects:	
	    cmd.show('cartoon','protein')
	    cmd.color("red", "ss h")
	    cmd.color("yellow", "ss s")
	    cmd.color("cyan", "ss l+\'\'")
	
	if 'dna' in objects:
   	    cmd.show('sticks', 'dna')
	    self.color_cpk(' & dna')
	
	if 'rna' in objects:
	    cmd.show('sticks', 'rna')
	    cmd.show('spheres','rna')
	    self.color_cpk(' & rna')

	if 'ligands' in objects:
	    cmd.show('spheres','ligands')
	    cmd.color('cyan','ligands')
	    
    # show hetero atoms    
    def show_hetero(self):
        import tkMessageBox
	objects = cmd.get_names('all')
	if 'ligands' in objects:
   	    self.set_defaults()
   	    
	    if 'protein' in objects:
	        cmd.show('cartoon', 'protein')
	        cmd.set('cartoon_transparency','0.7','protein')
	    
	    if 'dna' in objects:
	        cmd.show('sticks','dna')
	        cmd.set('stick_transparency','0.7','dna')
	    
	    if 'rna' in objects:
	        cmd.show('sticks', 'rna')
	        cmd.show('spheres','rna')
	        cmd.set('stick_transparency','0.7','rna')
	        cmd.set('sphere_transparency','0.7','rna')
	    
	    cmd.show('spheres','ligands')
	    cmd.set('sphere_transparency','0.1','ligands')
	    cmd.show("sticks", "ligands around 6'")
	    cmd.set('stick_radius','0.3','ligands around 6')
	    cmd.color('orange','ligands')
	    cmd.select("interaction","ligands around 6'")
	    self.color_cpk("& interaction")
	    cmd.delete('interaction')
	else: 
	    tkMessageBox.showinfo("Error", "There are no hetero atoms in this molecule.")
		    
    # ball and stick view	
    def ball_and_stick(self):
        objects = cmd.get_names('all')
        self.set_defaults()
        cmd.set("stick_radius","0.1","all")
        cmd.set("sphere_scale","0.3","all")
        
        if 'protein' in objects:
            cmd.show('spheres','protein')
	    cmd.show('sticks','protein')
	    self.color_default()
	
	if 'dna' in objects:
	    cmd.show('sticks','dna')
	    cmd.set('stick_radius','0.2','dna')	
  	    cmd.hide('spheres','dna')
  	    self.color_cpk(" & dna")
  	
  	if 'rna' in objects:
	    cmd.show('spheres','rna')
	    cmd.show('sticks','rna')
  	    self.color_cpk(" & rna")

	if 'ligands' in objects:
	    cmd.color('orange','ligands')
  	    
    # show the surface of the molecule
    def surface_view(self):
        objects = cmd.get_names('all')
        self.set_defaults()
        if 'protein' in objects:
            cmd.show('surface','protein')
            self.color_cpk('& protein')

       	if 'dna' in objects:
   	    cmd.show('sticks', 'dna')
	    cmd.show('surface','dna')
	    cmd.set('transparency','0.7','dna')
	    self.color_cpk( " & dna" )

      	if 'rna' in objects:
   	    cmd.show('sticks', 'rna')
   	    cmd.show('spheres','rna')
   	    cmd.set('sphere_scale','0.4','rna')
	    cmd.show('surface','rna')
	    cmd.set('transparency','0.7','rna')
	    self.color_cpk( " & rna")
	    
	if 'ligands' in objects:
	    cmd.show('spheres','ligands')
	    cmd.color('orange','ligands')
	    
    # show the polarities of the molecule
    def view_polarity(self):
        import tkMessageBox
        objects = cmd.get_names('all')
        self.set_defaults()
        
        cmd.show('surface','hydrophobic')
        cmd.color('red','hydrophobic')
        cmd.color('blue','hydrophilic')
        cmd.show('surface','hydrophilic')
        
        if 'ligands' in objects:
            cmd.show('spheres','ligands')
            cmd.color('green','ligands')
        
        if 'dna' in objects:
            cmd.show('sticks','dna')
            self.color_cpk(' & dna')
        
        if 'rna' in objects:
            cmd.show('sticks','rna')
            cmd.show('spheres','rna')
            cmd.set('sphere_scale','0.4','rna')
            self.color_cpk(' & rna')
        
        tkMessageBox.showinfo("Coloring", "Color Scheme: Red = Hydrophobic, Blue = Hydrophilic")
    
    # putty representation
    def show_putty(self):
	self.set_defaults()
    	objects = cmd.get_names('all')

    	if 'protein' in objects:
       	    cmd.show('cartoon','protein')
	    cmd.color("red", "ss h")
	    cmd.color("yellow", "ss s")
	    cmd.color("cyan", "ss l+\'\'")
    	    cmd.cartoon('putty','protein')
    	
    	if 'dna' in objects:
    	    cmd.show('sticks','dna')
    	    self.color_cpk(' & dna')
    	    
    	if 'rna' in objects:
    	    cmd.show('sticks','rna')
    	    cmd.show('spheres','rna')
    	    cmd.set('sphere_scale','0.4','rna')
    	    self.color_cpk(' & rna')
                 	    
    # aromatics view
    def color_aromatics(self):
	objects = cmd.get_names('all')
        self.set_defaults()
	if 'protein' in objects:
    	    cmd.show('cartoon','protein')
    	    cmd.color('aquamarine','protein')
    	    cmd.set('cartoon_transparency','0.6','protein')
    	if 'dna' in objects:
    	    cmd.show('cartoon','dna')
    	    cmd.color('aquamarine','dna')
    	    cmd.set('cartoon_transparency','0.6','dna')
    	if 'rna' in objects:
    	    cmd.show('cartoon','rna')
    	    cmd.color('aquamarine','rna')
    	    cmd.set('cartoon_transparency','0.6','rna')
	    	
	cmd.select('aromatics','resn phe+tyr+trp+his')
	cmd.color('red', 'aromatics')
	cmd.show('sticks','aromatics and (!name c+n+o)')
	cmd.set('stick_radius','0.4','all')
        cmd.deselect()
	cmd.delete('aromatics')        
	
    # color the molecule by chain
    def color_by_chain(self):
	self.set_defaults()
	objects = cmd.get_names('all')
	
	if 'protein' in objects:
	    cmd.show('cartoon','protein')

	if 'dna' in objects:
	    cmd.show('sticks','dna')
	
	if 'rna' in objects:
	    cmd.show('sticks','rna')
	    cmd.show('spheres','rna')
	    cmd.set('sphere_scale','0.4','rna')
	        
	cmd.color("blue","chain A")
	cmd.color("orange","chain B" )
	cmd.color("silver","chain C")
	cmd.color("green","chain D")
	cmd.color("yellow","chain E")
	cmd.color("purple","chain F")
	cmd.color("grey","chain G")
	cmd.color("brown","chain H")
	cmd.color("slate","chain I")
	cmd.color("brightorange","chain J")
	cmd.color("lightblue","chain K" )
	cmd.color("lightorange","chain L" )
	cmd.color("purple","chain M" )
	cmd.color("pink","chain N" )
	cmd.color("forest","chain O" )
	cmd.color("firebrick","chain P" )
	cmd.color("paleyellow","chain Q" )
	cmd.color("purpleblue","chain R" )
	cmd.color("deepteal","chain S" )
	cmd.color("deepolive","chain T" )
	cmd.color("pink","chain U" )
	cmd.color("salmon","chain V" )
	cmd.color("ruby","chain W" )
	cmd.color("wheat","chain X" )
	cmd.color("lightmagenta","chain Y")
	cmd.color("aquamarine","chain Z")
    
    #--------------------------------------#
    #					   #
    #        "ADVANED" TAB METHODS         #
    #                                      #
    #--------------------------------------#
    #------------------------------------------#
    #              Cartoon Functions           #
    #------------------------------------------#       
    # Set Cartoon Thickness 
    def cartoon_thickness(self):
        value = self.toonThickness.getvalue()
        cmd.set('cartoon_rect_width', value, self.sel) # strands
        cmd.set('cartoon_oval_width', value, self.sel) # helices 

    # Set Cartoon Width 
    def cartoon_width(self):
        value = self.toonWidth.getvalue()
        cmd.set('cartoon_rect_length', value, self.sel) # strands
        cmd.set('cartoon_oval_length', value, self.sel) # helices
            
    # Set Cartoon Transparency
    def cartoon_transparency(self):
        amount=self.cartoonTransparency.getvalue()
        cmd.set('cartoon_transparency', amount, self.sel)
        
    # Set Cartoon Tube Radius 
    def cartoon_tube_radius(self):
        value = self.toonTubeRadius.getvalue()
        cmd.set('cartoon_tube_radius', value, self.sel) # strands
    
    #Set Ribbon Type
    def ribType(self,tag):
    	if tag == 'Skip':
    		cmd.cartoon('skip', self.sel)
    	elif tag == 'Automatic':
    		cmd.cartoon('automatic', self.sel)
	elif tag == 'Oval':
    		cmd.cartoon('oval', self.sel)
    	elif tag == 'Tube':
    		cmd.cartoon('tube', self.sel)
    	elif tag == 'Rectangle':
    		cmd.cartoon('rectangle', self.sel)
    	elif tag == 'Loop':
    		cmd.cartoon('loop', self.sel)
    	elif tag == 'Arrow':
    		cmd.cartoon('arrow', self.sel)
    	elif tag == 'Dumbbell':
    		cmd.cartoon('dumbbell', self.sel) 
    	elif tag == 'Putty':
    		cmd.cartoon('putty', self.sel)   
    
    #------------------------------------------#
    #               Sphere Functions           #
    #------------------------------------------#
    # Set Sphere Transparency
    def sphere_transparency(self):
        amount=self.sphereTransparency.getvalue()
        cmd.set('sphere_transparency', amount, self.sel)
           		
    # Set Sphere Size
    def sphereSize(self):
    	size=self.sphereScale.getvalue()
    	cmd.set('sphere_scale', size, self.sel)

    #------------------------------------------#
    #              Surface  Functions          #
    #------------------------------------------#       
    # Set Surface Transparency
    def surface_transparency(self):
        amount=self.surfaceTransparency.getvalue()
        cmd.set('transparency', amount, self.sel)
    
    #------------------------------------------#
    #              Stick  Functions            #
    #------------------------------------------#       
    # Set Stick Transparency
    def stick_transparency(self):
        amount=self.stickTransparency.getvalue()
        cmd.set('stick_transparency', amount, self.sel)     
           
     # Set Stick Radius
    def stickRad(self):
    	size=self.stickRadius.getvalue()
    	cmd.set('stick_radius',size, self.sel)

    #------------------------------------------#
    #             Set Default Values           #
    #------------------------------------------#       
    def set_advanced_defaults(self, tag):
        if tag == 'Cartoon':
	    
	    # apply the changes
	    cmd.set('cartoon_rect_length', '1.4', self.sel) # strands
            cmd.set('cartoon_oval_length', '1.4', self.sel) # helices
            cmd.set('cartoon_rect_width', '0.3', self.sel) # strands
            cmd.set('cartoon_oval_width', '0.3', self.sel) # helices 
            cmd.set('cartoon_tube_radius','0.5',self.sel)
            cmd.set('cartoon_transparency','0.0',self.sel)
            cmd.cartoon('automatic',self.sel)
            
            # change the slider values
            self.toonWidth.setvalue('1.4')
            self.toonThickness.setvalue('0.3')
            self.cartoonTransparency.setvalue('0.0')
            self.toonTubeRadius.setvalue('0.5')
            self.ribbonTypes.invoke(0)
            
        elif tag == 'Spheres':
            # apply changes
            cmd.set('sphere_scale','0.7',self.sel)
            cmd.set('sphere_transparency','0.0',self.sel)
            
            # change slider values
            self.sphereScale.setvalue('0.7')
            self.sphereTransparency.setvalue('0.0')
            
        elif tag == 'Sticks':
            # apply the changes
            cmd.set('stick_radius','0.2',self.sel)
            cmd.set('stick_transparency','0.0',self.sel)
	    
	    # change slider values
	    self.stickRadius.setvalue('0.2')
	    self.stickTransparency.setvalue('0.0')
	    
        elif tag == 'Surface':	
            # apply the changes
            cmd.set('transparency','0.0',self.sel)
            
            # change slider value
            self.surfaceTransparency.setvalue('0.0')
            
    #--------------------------------------#
    #					   #
    #      "COMMANDS" TAB METHODS          #
    #                                      #
    #--------------------------------------#	
    # Color the molecule
    def color_cpk(self, str ):
	cmd.color("carbgray", "(elem C)" + str )
	cmd.color("red", "elem O" + str )
	cmd.color("white", "elem H" + str )
	cmd.color("nitblue", "elem N" + str )
	cmd.color("sulfyellow", "elem S" + str )
	cmd.color("phosorange", "elem P+Fe+Ba" + str )
	cmd.color("green", "elem Cl+B" + str )
	cmd.color("brown", "elem Br+Zn+Cu+Ni" + str )
	cmd.color("blue", "elem Na" + str )
	cmd.color("forest", "elem Mg" + str )
	cmd.color("darkgray", "elem Ca+Mn+Al+Ti+Cr+Ag" + str )
	cmd.color("goldenrod", "elem Au+F+Si" + str)
	cmd.color("ipurple", "elem I" + str)
	cmd.color("firebrick", "elem Li" + str)
	cmd.color("helpink", "elem He" + str)

    # Attempt to simulate the default PyMOL colorings
    def color_default(self):
	cmd.color("green", "elem C")
	cmd.color("red", "elem O")
	cmd.color("blue", "elem N")
    
    # Show ligands as spheres
    def space_fill_ligand(self):
	cmd.select("Bad", "resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c+t+u+HOH+MSE")
	cmd.select("ligand","!Bad")
	cmd.hide("everything", "ligand")
	cmd.show("spheres", "ligand")
	cmd.delete("Bad")
	self.color_cpk(" & ligand")
	cmd.deselect()
    
    # create additional colors
    # (adopted from some code written by 
    #  Kevin Galens and Jamie Duke at RIT)
    def init_color(self):
	cmd.set_color("sulfyellow", "[ 1.00, 0.78, 0.20 ]")
	cmd.set_color("carbgray", "[ 0.78, 0.78, 0.78 ]")
	cmd.set_color("nitblue", "[ 0.56, 0.56, 1.00 ]")
	cmd.set_color("phosorange", "[ 1.00, 0.65, 0.00 ]")
	cmd.set_color("znbrown", "[ 0.65, 0.16, 0.16 ]")
	cmd.set_color("goldenrod", "[ 0.85, 0.65, 0.125 ]")
	cmd.set_color("ipurple", "[ 0.63, 0.125, 0.94 ]")
	cmd.set_color("helpink", "[ 1.00, 0.75, 0.80 ]")
	cmd.set_color("darkgray", "[ 0.5, 0.5, 0.56 ]")
 
    # Show/Hide ALL representations
    def show_all(self, tag):
    	list = self.rep1.getvalue()
    	list2 = self.rep2.getvalue()
    	if tag == 'Show all':
    		self.rep1.invoke('Lines')
    		self.rep1.invoke('Sticks')
    		self.rep1.invoke('Ribbons')
    		self.rep1.invoke('Cartoon')
    		self.rep2.invoke('Dots')
    		self.rep2.invoke('Spheres')
    		self.rep2.invoke('Mesh')
    		self.rep2.invoke('Surface')
    		for item in list:
    			self.rep1.invoke(item)
    		for item in list2:
    			self.rep2.invoke(item)
		cmd.do('show everything')
    	else:
    		cmd.do('hide everything')
    		for item in list:
    			self.rep1.invoke(item)
    		for item in list2:
    			self.rep2.invoke(item)

    # Show individual representations
    def show_rep(self, tag):
    	sel = self.sel
	if tag == 'Lines':
  		cmd.show('lines',sel)
	elif tag == 'Sticks':
		cmd.show('sticks', sel)
	elif tag == 'Ribbons':
    		cmd.show('ribbon', sel)
	elif tag == 'Cartoon':
    		cmd.show('cartoon', sel)
	elif tag == 'Dots':
    		cmd.show('dots', sel)
	elif tag == 'Spheres':
    		cmd.show('spheres', sel)
      	elif tag == 'Mesh':
    		cmd.show('mesh', sel)
	elif tag == 'Surface':
    		cmd.show('surface', sel)
	elif tag == 'Water':
		cmd.show('(resn HOH)')
		cmd.show('spheres', '(resn HOH)')
	elif tag=='Ball and Stick':
		cmd.set('sphere_scale', '0.35', sel)
		cmd.show('spheres',sel)
		cmd.show('sticks',sel)
      	    
    # Hide individual representations
    def hide_rep(self, tag):
    	sel = self.sel
	if tag == 'Lines':
		cmd.hide('lines',sel)
       	elif tag == 'Sticks':
   	    	cmd.hide('sticks', sel)
        elif tag == 'Ribbons':
        	cmd.hide('ribbon', sel)
        elif tag == 'Cartoon':
        	cmd.hide('cartoon', sel)
       	elif tag == 'Dots':
        	cmd.hide('dots', sel)
        elif tag == 'Spheres':
       	    	cmd.hide('spheres', sel)
        elif tag == 'Mesh':
        	cmd.hide('mesh', sel)
        elif tag == 'Surface':
        	cmd.hide('surface', sel)
        elif tag == 'Water':
        	cmd.hide('(resn HOH)')
        elif tag == 'Everything':
        	cmd.hide('everything', sel)
        elif tag=='Ball and Stick':
		cmd.hide('spheres',sel)
		cmd.hide('sticks',sel)

      
    # Set selection of atoms
    #   - initial selection is 'all'
    def set_sel(self, tag):
    	cmd.deselect()
    	c=re.compile("^Chain")
	if tag=='All':
        	self.sel = 'all'
	elif tag=='Protein':
		self.sel = 'protein'
	elif tag=='DNA':
        	self.sel = 'dna'
        elif tag=='RNA':
        	self.sel = 'rna'
	elif tag=='Ligands':
		h=' '
		for each in self.p.hlist:
			h = h + "+" + each
		if h==' ':
			pass
		else:
        		self.sel = 'ligands'
        elif c.match(tag):
        	id = tag[6]
        	cmd.select(tag, 'chain '+id)
        	cmd.deselect()
        	self.sel=tag
        elif tag=='Not Selected':
        	cmd.select('selection', '!'+self.sel)
        	cmd.deselect()
        	self.sel= 'selection'
        elif tag=='Hydrophobic':
               	self.sel='hydrophobic'
	elif tag=='Hydrophilic':
		self.sel='hydrophilic'
		
	#self.advSel.set('Current Selection: ' + self.sel)
	self.selection.setvalue(tag)
	self.advancedSelection.setvalue(tag)
	
    # Tell our command line what type of commands to read
    def set_cmd_type(self, tag):
        if tag == 'PyMOL':
            self.commandLine.setvalue('Enter PyMOL Commands Here')
            self.cmdType = 'PyMOL'
        else:
            self.commandLine.setvalue('Enter Chime Commands Here')
            self.cmdType = 'Chime'
            
    # Read commands from command line    
    def command_line(self):
	command = self.commandLine.getvalue()
        if self.cmdType == 'PyMOL':
            cmd.do(command)
            self.commandLine.clear()
        else:
            self.converter.parseIt(command, self.commandLine, self.output)
       
    # Coloring on Selection
    def color_sel(self, tag):
    	sel=self.sel
	if tag=='Red':
		cmd.color('red', sel)
	elif tag=='Green':
		cmd.color('green', sel)
	elif tag=='Orange':
		cmd.color('orange', sel)
	elif tag=='Yellow':
		cmd.color('yellow', sel)
	elif tag=='Blue':
		cmd.color('blue', sel)
	elif tag=='Violet':
		cmd.color('violet', sel)
	elif tag=='CPK':
		self.color_cpk(' & '+sel)
	elif tag=='Other':
		color=tkColorChooser.askcolor(parent=self.int, title="Selection Color Chooser")
		colorArray =[]
		if color[0]!= None:
			list=color[0]
			print list
			for each in list:
				z = (each/255.0)
				val=repr(z)
				colorArray.append(val)
			cmd.set_color('newcolor', colorArray)
			cmd.color('newcolor', sel) 
    
    #--------------------------------------#
    #					   #
    #           SAVE   METHODS             #
    #                                      #
    #--------------------------------------#	 
    def imgSave(self):
    	import tkFileDialog
    	import tkMessageBox
	if tkMessageBox.askyesno('Ray Trace Image', "Do you want to ray trace you image before saving it? Depending on your image "+
					"this make take a few minutes if you select yes."):
		cmd.ray()    	
    	file = tkFileDialog.asksaveasfilename(defaultextension=".png", initialdir="C:/Program Files/DeLano Scientific/PyMOL/")
    	if len(file)>0:
    		cmd.save(file)
    	
    	
    
    def sessionSave(self):
    	import tkFileDialog
    	import tkMessageBox 
    	
    	file = tkFileDialog.asksaveasfilename(defaultextension=".pse", initialdir='C:/Program Files/Delano Scientific/PyMOL/')
    	print file
        if len(file)>0:
    		cmd.save(file)      
        
    
    #--------------------------------------#
    #					   #
    #         UTILITY  METHODS             #
    #                                      #
    #--------------------------------------#	 
    # ADD BUTTONS
    # Create and add buttons to the GUI
    def buttonAdd(self,frame,text,size,cmd,gridrow,gridcol,gridstick):
        # create the button
        newBtn = Button(frame, text=text,highlightthickness=0, 
                      width=size,command=cmd,padx=0,pady=0)

	# add it to the gui
        newBtn.grid(row=gridrow, column=gridcol, sticky=gridstick, padx=2, pady=2)
        
    # ADD RADIO BUTTONS
    # Create and add radio buttons to the GUI
    def radioAdd(self,frame,pos,orient,cmd,label,btn_labels, gridrow, 
    		 gridcol, cspan, rspan, gridstick):
    	labels = btn_labels   #the list of labels passed in by the user
    	
    	# create the radio button
    	newRadio = Pmw.RadioSelect(frame, labelpos=pos, labelmargin=0,
    				    buttontype='radiobutton',
    				    orient=orient,
    				    label_text=label,
    				    command=cmd)
 	# add it to the gui
 	newRadio.grid(row=gridrow, column=gridcol, columnspan=cspan, 
 		      rowspan=rspan, sticky=gridstick, padx=5)
 	
 	# add text to the buttons
 	for text in labels:
   	    newRadio.add(text)
	    newRadio.setvalue(labels[0])
	   
    # ADD FORMATTING SPACERS
    # Add white space to the GUI (used in formatting)
    def addSpace(self,frame,gridrow, gridcol):
        # create the button
        space = Label(frame, text='            ')
        space.grid(row=gridrow, column=gridcol)

    #--------------------------------------#
    #					   #
    #         SETTINGS TAB METHODS         #
    #                                      #
    #--------------------------------------#
    # handle stereo commands
    def stereo_switch(self, tag):
	if tag == 'Off':
	    cmd.stereo('off')
	elif tag == 'Quad Buffered':
	    cmd.stereo('off')
            cmd.stereo('cross')
            cmd.stereo('quadbuffer')
            cmd.stereo('on')
        elif tag == 'Cross-Eye':
            cmd.stereo('off')
            cmd.stereo('cross')
            cmd.stereo('on')
        else:
            cmd.stereo('off')
            cmd.stereo('walleye')
            cmd.stereo('on')
        
    # change background colors
    def bgcolor_switch(self, tag):
        if tag == 'Black':
            cmd.do('bg_color black')
        elif tag == 'White':
            cmd.do('bg_color white')
        elif tag == 'Grey':
            cmd.do('bg_color grey')
        elif tag == 'Other':
        	color=tkColorChooser.askcolor(parent=self.int, title="Background Color Chooser")
        	colorArray =[]
        	if color[0]!= None:
        		list=color[0]
        		print list
        		for each in list:
        			z = (each/255.0)
        			val=repr(z)
        			colorArray.append(val)
        		cmd.set_color('newcolor', colorArray)
        		cmd.do('bg_color newcolor') 	
        else: 
       	    self.do_nothing()
        
    # change the color space
    def cspace_switch(self, tag):
	if tag == 'PyMOL':
	    cmd.space('pymol')
	elif tag == 'Publications':
	    cmd.space('rgb')
	else: 
	    cmd.space('cmyk')
	    
    # hide/show interface
    def hide_interface(self, tag):
	if tag == 'Show':
	    cmd.set('internal_gui','1')
	else:
	    cmd.set('internal_gui','0')
    # Show/Hide Water
    def show_hide_water(self, tag):
        if tag == 'Show':
        	cmd.show('(resn HOH)')
        	cmd.show('spheres', '(resn HOH)')
        else:
        	cmd.hide('(resn HOH)')
    
    # Toggle Sequence on/off
    def sequence(self, tag):
    	if tag == 'On':
    		cmd.set('seq_view', '1')
    	else:
    		cmd.set('seq_view', '0')
    		
    #Change sequence view formats
    def sequence_view(self, tag):
    	if tag == "Residue Codes":
    		cmd.set('seq_view_format', '0')
    	elif tag == "Residues":
    		cmd.set('seq_view_format', '1')
    	elif tag == "Chains":
    		cmd.set('seq_view_format', '2')
    	elif tag == "Atoms":
    		cmd.set('seq_view_format', '3')
    	else:
    		cmd.set('seq_view_format', '4')
    	
    #Frame Speed Settings
    def frame_speed(self, tag):
    	if tag == '30':
    		cmd.set('movie_delay', '66')
    	elif tag == '15':
    		cmd.set('movie_delay', '33')
    	elif tag == '5':
    		cmd.set('movie_delay', '200')
    	elif tag == '1':
    		cmd.set('movie_delay', '1000')
    	elif tag == '0.3':
    		cmd.set('movie_delay', '3000')
    	else:
    		cmd.set('movie_delay', '0')
    		

    #--------------------------------------#
    #					   #
    #         PARSING  METHODS             #
    #                                      #
    #--------------------------------------#        	
    # Sequence Getter
    def seqGetter(self, id):
    	seq = self.p.chains[id]
    	seq=string.upper(seq)
    	seqArray=string.split(seq, ' ')
    	if len(seqArray[0])==1:
    		if seq[0]=='U':
    			type ='RNA'
    		if string.find(seq,'U')!=-1:
    			type ='RNA'
    		else:
    			type = 'DNA'
    		seq=string.replace(seq," ", "")
    	else:
    		type='Protein'
    	info = "Chain "+id+"\nSequence Type: "+type+"\nSequence: "+seq
    	self.info.config(state=NORMAL)
    	self.info.delete(1.0,END)
    	self.info.insert(END, info)
    	self.info.config(state=DISABLED)
    	return type
    	
    #--------------------------------------#
    #					   #
    #           MOVIE METHODS              #
    #                                      #
    #--------------------------------------#
    def rotate_y(self):
	cmd.mset()
	cmd.mset('1','180')
        cmd.util.mroll('1','180','1')
        cmd.mplay()

    # Movie to show locations of each of the chains in the molecule	
    def highlight_chains(self):
	cmd.mstop()
	cmd.mclear()
	cmd.mset()
	self.set_defaults()
	
	colors = ['blue','orange','silver','green','yellow',
       	        'purple','brightorange','lightblue','lightorange',
       	        'pink','forest','firebrick','paleyellow','salmon',
       	        'ruby','wheat','lightmagenta','nitblue']
       	        
        numChains = len(self.p.chains)
        numFrames = (numChains*200)+70
        cmd.mset('1',numFrames)
        cmd.do('mdo 1: color red, all; hide cartoon, all')
        cmd.orient()
        cmd.mview('store','1')
       
        colorCount = 0
        frameCount = 1
        for i in self.p.chains.keys():
            cmd.orient('chain ' + i)
            cmd.mview('store', frameCount+59)
            cmd.mview('store', frameCount+115)
            self.flash_chain(i, frameCount+59, 'red', colors[colorCount])
            cmd.orient()
            cmd.turn('x','270')
            cmd.turn('y','180')
            cmd.mview('store',frameCount+150)
	    cmd.mview('store',frameCount+170)
	    colorCount += 1
            frameCount += 200
            if(frameCount > numFrames-100):
                cmd.orient()
            cmd.do('mdo '+str(numFrames)+': mstop')
        cmd.mview('store',(numChains*200)+70)
        cmd.mview('interpolate')
        cmd.show('ribbon')
        #cmd.show('surface')
        cmd.color('red','all')
        #cmd.set('transparency','0.75','all')
        #cmd.set('cartoon_transparency','0.0','all')
    
    # flash the chains on and off, eventually changing the color
    # (utilized by the highlight_chains method)       
    def flash_chain(self, chainID, frame, initialColor, afterColor):
       cmd.do('mdo ' + str(frame)+': show cartoon, chain ' + str(chainID))
       cmd.do('mdo '+str(frame+7)+': color '+afterColor+', chain '+str(chainID))
       cmd.do('mdo '+str(frame+14)+': color '+initialColor+', chain '+str(chainID))                  
       cmd.do('mdo '+str(frame+21)+': color '+afterColor+', chain '+str(chainID))
       cmd.do('mdo '+str(frame+28)+': color '+initialColor+', chain '+str(chainID))                  	              
       cmd.do('mdo '+str(frame+35)+': color '+afterColor+', chain '+str(chainID))
       cmd.do('mdo '+str(frame+42)+': color '+initialColor+', chain '+str(chainID))         
       cmd.do('mdo '+str(frame+49)+': color '+afterColor+', chain '+str(chainID))
    
	    	
    def ligandZoom(self):
    	import tkMessageBox
    	cmd.mstop()
	cmd.mclear()
	cmd.mset()
    	q=360
    	ids = self.p.idList
    	if len(ids)==0:
            tkMessageBox.showinfo("Ligand Zoom", "Sorry this PDB file contains no ligands and cannot be made into a movie")
    	else:
	    objects = cmd.get_names('all')
	    self.set_defaults()
	    ids.sort()
	    numFrames = 600+(335*(len(ids)))
	    cmd.deselect()
	    cmd.do('bg_color white')
	    cmd.cartoon('tube', 'all')
	    cmd.mset('1', numFrames)
	    cmd.do('mdo 1: show cartoon, all; hide cartoon, resn a+t+c+g; show sticks, resn a+t+c+g;')
	    cmd.reset()
	    cmd.do('turn x, 180')
	    cmd.orient()
	    cmd.mview('store', '1')
	    cmd.do('turn y, 180')
	    cmd.mview('store', '120')
	    cmd.mview('store', '150')
	    cmd.do('turn y, 180')
	    cmd.mview('store', '240')
	    cmd.mview('store', '270')
	    for i in range(len(ids)):
	    	self.color_cpk(' and (byres (ligands and '+ids[i]+')around 5)')
	    	self.color_cpk(' and ligands')
	    	cmd.orient('(ligands and '+ids[i]+')around 7')
	    	cmd.mview('store', str(q))
	    	cmd.do('mdo '+str((q+1))+':set sphere_transparency, 0.1, ligands; set cartoon_transparency, 0.9, all;  show spheres, (ligands and '+ids[i]+'); show sticks, (ligands and '+ids[i]+');')
	    	cmd.mview('store', str(q+10))
	    	cmd.do('mdo '+str((q+11))+':set sphere_transparency, 0.2, ligands;')
	    	cmd.mview('store', str(q+20))
	    	cmd.do('mdo '+str((q+21))+':set sphere_transparency, 0.3, ligands;')
	        cmd.mview('store', str(q+30))
	    	cmd.do('mdo '+str((q+31))+':set sphere_transparency, 0.4, ligands;')
	    	cmd.mview('store', str(q+40))
	    	cmd.do('mdo '+str((q+41))+':set sphere_transparency, 0.5, ligands;')
	    	cmd.mview('store', str(q+50))
	    	cmd.do('mdo '+str((q+51))+':show sticks, (byres (ligands and '+ids[i]+')around 1);')
	    	cmd.mview('store', str(q+60))
	    	cmd.do('mdo '+str((q+61))+':show sticks, (byres (ligands and '+ids[i]+')around 2);')
	    	cmd.mview('store', str(q+70))
	    	cmd.do('mdo '+str((q+71))+':show sticks, (byres (ligands and '+ids[i]+')around 3);')
	    	cmd.mview('store', str(q+80))
	    	cmd.do('mdo '+str((q+81))+':show sticks, (byres (ligands and '+ids[i]+')around 4);')
	    	cmd.mview('store', str(q+81))
	    	cmd.do('turn y, 180')
	    	cmd.mview('store', str(q+125))
	    	cmd.mview('store', str(q+150))
	    	cmd.do('mdo '+str((q+151))+': set cartoon_transparency, 0, all;')
	    	cmd.reset()
	    	cmd.orient()
	    	cmd.mview('store', str(q+215))
	    	cmd.mview('store', str(q+255))
	    	if i==(len(ids)-1):
	    	    cmd.reset()
	    	    cmd.orient()
	    	    cmd.do('turn x, 180')
	    	    cmd.mview('store', str(numFrames))
	        else:
	    	    cmd.mview('store', str(q+335))
	    	    q=q+335		
	    		
	    cmd.do('mdo '+str(numFrames)+': hide spheres, ligands; hide sticks, ligands around 4; label ligands, \' \'')
	    cmd.do('mdo '+str(numFrames)+': mstop')
	    cmd.mview('interpolate')
	    cmd.rewind()
	    	
	    
    def growProtein(self):
   	cmd.mstop()
	cmd.mclear()
	cmd.mset()
    	objects = cmd.get_names()

    	if 'protein' in objects:
            self.set_defaults()
    	    cmd.bg_color('black')
    	    
    	    # create the objects to be used in this movie
    	    cmd.create('helix', 'ss h and protein')
    	    cmd.create('sheets', 'ss s and protein')
    	    cmd.create('surface', objects[0]) 
    	    
    	    cmd.mset('1', '1400')
    	    
    	    # dna and rna will be represented as sticks
    	    # to make them stand out from the protein
    	    if 'dna' in objects:
   	        cmd.show('sticks','dna')
    	        self.color_cpk(' & dna')
   	    
    	    if 'rna' in objects:
 	        cmd.show('sticks','rna')
 	        cmd.show('spheres','rna')
    	        cmd.set('sphere_scale','0.4','rna')
    	        self.color_cpk(' & rna')
    	     	        
    	    # coloring the protein and secondary structures
    	    cmd.color('white', 'protein')
       	    cmd.color('ipurple', 'helix')
    	    cmd.color('teal', 'sheets')
    	    
    	    cmd.cartoon('loop', 'protein')
    	    cmd.cartoon('automatic', 'helix')
    	    cmd.cartoon('automatic', 'sheets')
    	    cmd.show('cartoon', 'protein')
    	    
    	    
    	
    	    #cmd.do('mdo 1: hide cartoon, helix; hide cartoon, sheets;')
    	    cmd.util.mrock('2','200','90','1','1')
    	    cmd.do('mdo 201: show cartoon, helix;')
    	    cmd.util.mrock('202','400','90','1','1') 
    	    cmd.do('mdo 401: show cartoon, sheets;')
    	    cmd.util.mrock('402','600','90','1','1')
    	    if 'ligands' in objects:
    	        cmd.color('hotpink','ligands')
    	        cmd.do('mdo 600: show spheres, ligands; show sticks, ligands; set sphere_transparency=0.5, ligands;')
    	    
    	    cmd.util.mroll('601','800','1',axis="x")
    	    cmd.color('nitblue', 'surface')
    	    cmd.mview('store', '800')
    	    cmd.do('turn z, 180')
    	    cmd.mview('store' ,'1000')
    	    cmd.do('turn z, 180')
    	    cmd.do('mdo 800: show surface, surface; set transparency=0.8, surface;')
    	    cmd.do('mdo 850: set transparency=0.7, surface;')
    	    cmd.do('mdo 900: set transparency=0.6, surface;')
    	    cmd.do('mdo 950: set transparency=0.5, surface;')
    	    cmd.do('mdo 1000: set transparency=0.4, surface;')
    	    cmd.do('mdo 1050: set transparency=0.3, surface;')
    	    cmd.do('mdo 1100: set transparency=0.2, surface;')
    	    cmd.do('mdo 1150: set transparency=0.1, surface;')
    	    cmd.do('mdo 1200: set transparency=0.0, surface;')
    	    cmd.mview('store', '1200')
    	    cmd.util.mrock('1201','1399','180','1','1')
    	    cmd.hide('everything', 'surface')
    	    cmd.hide('everything', 'helix')
    	    cmd.hide('everything', 'sheets')
    	    cmd.reset()
    	    cmd.orient()
    	    cmd.do('mdo 1400: hide everything, all; show cartoon, protein;')
    	    cmd.do('mdo 1400: mstop')
    	    cmd.mview('interpolate')
    	    cmd.rewind()
   
    def play(self):
    	cmd.mplay()
    
    def stop(self):
    	cmd.mstop()
    
    def rewind(self):
	cmd.mstop()
        cmd.rewind()
        
    def ray(self,r,state):
	import tkMessageBox
     	if state:
     		if tkMessageBox.askyesno('Ray Trace Frames', 'Enabling this feature may '+
     					 'slow own the playback of your movie significantly. '+
     					 'Are you sure that you want to proceed?'):
     			cmd.set('ray_trace_frames','1')
     		else:
     			self.ray.invoke('Ray Tracing On')
     	else:
     		cmd.set('ray_trace_frames','0')
     
    #------------------------------------------------
    # Connecting to the PDB Loader
    # Copyright Notice
	# ================
	# 
	# The PyMOL Plugin source code in this file is copyrighted, but you can
	# freely use and copy it as long as you don't change or remove any of
	# the copyright notices.
	# 
	# This PyMOL Plugin is Copyright (C) 2004 by Charles Moad <cmoad@indiana.edu>
    #----------------------------------------------------------------------------------
    def getPdb(self):
      import tkSimpleDialog
      import tkMessageBox
      import urllib
      import gzip
      import os
      import string
      
      if self.fileLoaded ==' ':	
      	pdbCode = tkSimpleDialog.askstring('PDB Loader Service',
                                         'Please enter a 4-digit pdb code:')
      else:
      	pdbCode=self.fileLoaded
      	#print pdbCode
      
      if pdbCode: # None is returned for user cancel
         pdbCode = string.upper(pdbCode)
         filename = urllib.urlretrieve('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                    pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                    pdbCode + '&compression=gz')[0]        
         # If 0, then pdb code was invalid           
         if (os.path.getsize(filename) > 0): 
	    
            # Decompress the file while reading
            fpin = gzip.open(filename)

            # Form the pdb output name
            outputname = os.path.dirname(filename) + os.sep + pdbCode + '.pdb'
            fpout = open(outputname, 'w')
            fpout.write(fpin.read()) # Write pdb file
            
            fpin.close()
            fpout.close()
            
            cmd.load(outputname) # Load the fresh pdb
            if self.fileLoaded ==' ':
            	self.std_view()
            #---------------THIS WAS JUST ADDED---------------------------
            self.p=PDBParser()
            self.p.readFile(outputname)
            self.update(self.p)
            cmd.deselect()

         else:
            tkMessageBox.showerror('Invalid Code',
                                   'You entered an invalid pdb code:' + pdbCode)

         os.remove(filename) # Remove tmp file (leave the pdb)
        		
    #------------------------------------------------------------#
    #								 #
    #                  PDB Abstract Getter                       #
    #		            					 #					 
    # 								 #
    #------------------------------------------------------------#
    
    def getPubMed(self):
    	import webbrowser
    	import urllib
    	import tkMessageBox
    	
    	objs = cmd.get_names('all')
    	id = objs[0]
    	ref = urllib.urlopen('http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?'+
    		'cmd=search&db=pubmed&term='+id)
    	source = ref.read()
    	ref.close()
    	p = re.compile("PMID: [0-9]+")
    	found = p.search(source)
    	if found == None:
    		title = self.p.title
    		list = title.split(" ")
    		list2=[]
    		for items in list:
    			t= string.strip(items)
    			list2.append(t)
    		title = string.join(list2,"+")
    		ref = urllib.urlopen('http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?'+
    			'cmd=search&db=pubmed&term='+title)
    		source = ref.read()
    		ref.close()
    		found = p.search(source)
    		if found==None:
    			tkMessageBox.showinfo("Unable to Find PubMed Article", "Sorry we couldn't find the article for this molecule. "+
    				"Please visit the PubMed website to continue looking. http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=PubMed")	  		
    	if found != None:
    		start = found.start()
    		end = found.end()
    		id = source[start+6:end]
    		webbrowser.open('http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?'+
    			'cmd=retrieve&db=pubmed&list_uids='+id+'&dopt=abstract')
    #------Open Help File---------#
    def help(self):
    	import webbrowser
    	webbrowser.open('modules\pmg_tk\startup\Help\EZ-VizWebMain.html')
    			
    #---------------------------------------------------------------#
    #								    #
    #                   GUI CREATION METHOD                         #
    #			      (INIT)			 	    #
    #								    #
    #								    #
    #	             create and organize the interface              #          
    #								    #
    #---------------------------------------------------------------#
    def __init__(self, app):
        
        self.pdbCode = ' '  	
        self.p=PDBParser()
        self.converter = ChimeConverter()
        
        # initialize the additional colors
        self.init_color() 
        self.sel='all'
   
        # create the dialog box which contains the GUI
        parent = app.root
        self.dialog = Pmw.Dialog(parent,buttons = ('Open','Fetch PDB','Clear','Help','Quit'),
                      title = 'EZ-Viz',command = self.execute)
        
        # set the size of the 
        #self.dialog.geometry('550x550')
     	interior = self.dialog.interior()
 	
 	# Let everyone know who the cool kids are who made this for them
 	lab = Label(interior, 
 		    text='EZ-Viz\nCreated By: Laura Grell, Chris Parkin, Len Slatest & Paul Craig\nVersion 1.0, 2005', 
 		    background='#000066', foreground='white')
 		    
 	lab.pack(expand=0, fill='x', padx=4, pady=0)
 	
        # Create the notebook to hold the tabs
        notebook = Pmw.NoteBook(interior)
        notebook.pack(fill='both', expand=1, padx=10, pady=10)
        #--------------------------------------#
        #			               #
        #         WELCOME  TAB                 #
        #                                      #
        #--------------------------------------#
        page = notebook.add('Welcome')
        notebook.tab('Welcome').focus_set()
        canvas=Canvas(page)
 	canvas.pack(fill='both', expand=1)
 	canvas.create_image(0,0,image=splash,anchor=NW)
        
        #--------------------------------------#
        #			               #
        #          PRESETS TAB                 #
        #                                      #
        #--------------------------------------#
        # Add Presets tab to notebook
        page = notebook.add('Presets')
        notebook.tab('Presets').focus_set()
        
        #------------ Presets Group  ---------------
        group = Pmw.Group(page, tag_text='Pre-defined Views')
        group.pack(fill='both', side=LEFT, expand='1', padx=2, pady=2)
        interior=group.interior()
      
        #------- Row 1 Images -------
        canvas1=Canvas(interior, width=57, height=48)
        canvas1.grid(row=0, column=0, padx=0, pady=0)
        canvas1.create_image(0,0,image=defaultImage,anchor=NW)

	# separate the images
 	self.addSpace(interior, 0, 1) 
 	
 	# chain coloring image
 	canvas2=Canvas(interior, width=57, height=48)
 	canvas2.grid(row=0, column=2)
 	canvas2.create_image(0,0,image=chains,anchor=NW)
 	
 	# separate the images
 	self.addSpace(interior,0,3)
 	
 	# hetero atoms image
	canvas3=Canvas(interior, width=57, height=48)
 	canvas3.grid(row=0, column=4)
 	canvas3.create_image(0,0,image=heteroImg,anchor=NW)
 	
        # Row 1 Buttons
        self.buttonAdd(interior, 'Default', 15, self.std_view, 1, 0, 'N,S,E,W')
        self.buttonAdd(interior, 'Color by Chain', 15, self.color_by_chain, 1, 2, 'N,S,E,W')
        self.buttonAdd(interior, 'Hetero Atoms', 15, self.show_hetero, 1, 4, 'N,S,E,W')
        
        # add a spacer
        self.addSpace(interior, 2, 0)
        
        #------- Row 2 Images --------
        # ball and stick image
        canvas5=Canvas(interior, width=57, height=48)
        canvas5.grid(row=3, column=0, padx=0, pady=0)
        canvas5.create_image(0,0,image=ballStickImg,anchor=NW)

	# separate the images
 	self.addSpace(interior, 3, 1) # separate the images
 	
 	# surface image
 	canvas6=Canvas(interior, width=57, height=48)
 	canvas6.grid(row=3, column=2)
 	canvas6.create_image(0,0,image=surfaceImg,anchor=NW)
 	
 	# separate the images
 	self.addSpace(interior,3,3)
 	
 	# polarity image
	canvas7=Canvas(interior, width=57, height=48)
 	canvas7.grid(row=3, column=4)
 	canvas7.create_image(0,0,image=polarityImg,anchor=NW)
 	
 	#------- Row 2 Buttons --------
        self.buttonAdd(interior, 'Ball & Stick', 15, self.ball_and_stick, 4, 0, 'N,S,E,W')
        self.buttonAdd(interior, 'Surface', 15, self.surface_view, 4, 2, 'N,S,E,W')
        self.buttonAdd(interior, 'Polarity', 15, self.view_polarity, 4, 4, 'N,S,E,W')
        
        # add a spacer
        self.addSpace(interior, 5, 0)
        
        #------- Row 3 Images --------
        # ball and stick image
        canvas8=Canvas(interior, width=57, height=48)
        canvas8.grid(row=6, column=0, padx=0, pady=0)
        canvas8.create_image(0,0,image=aromaticsImg,anchor=NW)

	# separate the images
 	self.addSpace(interior, 6, 1) # separate the images
 	
 	# putty image
 	canvas9=Canvas(interior, width=57, height=48)
 	canvas9.grid(row=6, column=2)
 	canvas9.create_image(0,0,image=puttyImg,anchor=NW)
 	
 	# separate the images
 	self.addSpace(interior,3,3)
 	
 	# dna image
	canvas10=Canvas(interior, width=57, height=48)
 	canvas10.grid(row=6, column=4)
 	canvas10.create_image(0,0,image=dnaImg,anchor=NW)
 	
 	#------- Row 3 Buttons --------
        self.buttonAdd(interior, 'Aromatics', 15, self.color_aromatics, 7, 0, 'N,S,E,W')
        self.buttonAdd(interior, 'Putty', 15, self.show_putty, 7, 2, 'N,S,E,W')
        self.buttonAdd(interior, 'DNA & RNA', 15, self.show_dna_rna, 7, 4, 'N,S,E,W')

        #--------------------------------------#
        #			               #
        #            SETTINGS TAB              #
        #                                      #
        #--------------------------------------#
        # Add "Settings" tab to notebook
        page = notebook.add('Settings')
      
        #------------ Display Group ----------------
        group = Pmw.Group(page, tag_text='Display')
        group.pack(fill='both', side=LEFT, expand='1', padx=2, pady=2)
        self.int=group.interior()
        
        # Add labels for corresponding radio button 	
 	lab = Label(self.int, text='Stereo Viewing:')
 	lab.grid(row=0, column=0, sticky='E')
 	
 	lab = Label(self.int, text='Background Color:')
 	lab.grid(row=1, column=0, sticky='E')
 	
 	lab = Label(self.int, text='Color Space:')
 	lab.grid(row=2, column=0, sticky='E')
 	
 	lab = Label(self.int, text='PyMOL Interface:')
 	lab.grid(row=3, column=0, sticky='E')
 	
 	lab = Label(self.int, text='Sequence Mode:')
 	lab.grid(row=4, column=0, sticky='E')
 	
 	lab = Label(self.int, text='Sequence Format:')
 	lab.grid(row=5,column=0, sticky='E')
 	
 	lab = Label(self.int, text='Frame Speed (FPS):')
 	lab.grid(row=6, column=0, sticky='E')
 	
        # Radio buttons for stereo options
        labels = ("Off", "Quad Buffered", "Cross-Eye", "Wall-Eye")        
        self.radioAdd(self.int, 'w', 'horizontal', self.stereo_switch,
                      ' ', labels, 0, 1, 1, 1, 'W')
        
       	# Radio buttons for background color changes
	labels = ("Black", "White", "Grey", "Other")
	self.radioAdd(self.int, 'w', 'horizontal', self.bgcolor_switch, 
	              ' ', labels, 1, 1, 1, 1, 'W')

       	# Radio Buttons for color space
	labels = ("PyMOL", "Publications", "Video/Web")
	self.radioAdd(self.int, 'w', 'horizontal', self.cspace_switch,
	              ' ', labels, 2, 1, 1, 1, 'W')
	              
	# Radio Buttons for hide/show interface
	labels = ("Show", "Hide")
	self.radioAdd(self.int, 'w', 'horizontal', self.hide_interface,
		      ' ', labels, 3, 1, 1, 1, 'W')
		      
	#Radio Buttons for sequence view
	labels = ("On", "Off")
	self.radioAdd(self.int, 'w', 'horizontal', self.sequence,
		      ' ', labels, 4, 1, 1, 1, 'W')	
	
	#Radio Buttons for sequence view format
	labels = ("Residue Codes", "Residues", "Chains", "Atoms", "States")
	self.radioAdd(self.int, 'w', 'horizontal', self.sequence_view,
	              ' ' , labels, 5, 1, 1, 1, 'W')
	              
	#Radio Buttons for Frame Speed
	labels = ("Max", "30", "15", "5", "1", "0.3")
	self.radioAdd(self.int, 'w', 'horizontal', self.frame_speed,
	              ' ', labels, 6, 1, 1, 1, 'W')
        
        #--------------------------------------#
        #			               #
        #            COMMANDS TAB              #
        #                                      #
        #--------------------------------------#       
        # ADD COMMANDS TAB TO NOTEBOOK
        page = notebook.add('Commands')
        notebook.tab('Commands').focus_set()

        # AUTOMATED COMMANDS TAB
        group = Pmw.Group(page, tag_text = 'Automated Commands')
        group.grid(row=0, column=0, padx=0, pady=0)
        interior = group.interior()
        
	self.selection = Pmw.OptionMenu(interior,labelpos = 'w',
                   label_text = 'Select:',
                    items = ('All', 'Not Selected', 'Hydrophobic','Hydrophilic'),
                    menubutton_width = 10, command = self.set_sel)
                       
        self.selection.grid(row=0, column=0, padx=8, pady=0)
        
        self.viewOptions = Pmw.OptionMenu(interior, labelpos='w',
    		label_text = 'Show:',
    		items = ('Lines', 'Sticks', 'Ribbons','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water', 'Everything'),
    		menubutton_width=10, command=self.show_rep)
    		
 	self.viewOptions.grid(row=0,column=1,padx=8,pady=0,sticky='N')
 	
 	self.hideOptions = Pmw.OptionMenu(interior, labelpos='w',
    		label_text = 'Hide:',
    		items = ('Lines', 'Sticks', 'Ribbons','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water','Everything'),
    		menubutton_width=10, command=self.hide_rep)
    		
 	self.hideOptions.grid(row=1,column=1,padx=8,pady=0, sticky='S')
 	
 	# Coloring choices
	selection = Pmw.OptionMenu(interior,labelpos = 'w',
                   label_text = 'Color:',
                    items = ('Red','Green','Blue','Orange','Violet','Yellow','CPK','Other'),
                    menubutton_width = 7, command = self.color_sel)
                       
        selection.grid(row=0, column=2, padx=0, pady=0)
                  
        # MANUAL COMMANDS SECTION
        group = Pmw.Group(page, tag_text='Manual Commands')
        group.grid(row=1,column=0, padx=0,pady=0)
        interior = group.interior()
        
        labels = ('PyMOL','Chime')
        self.commandChooser = self.radioAdd(interior,'w','vertical',self.set_cmd_type,'Command Type:',labels, 0, 
    		      0, 1, 1, 'W')
        
        self.output = Pmw.ScrolledText(interior,
                usehullsize = 1,
                hull_width = 250,
                hull_height = 100,
                text_wrap= WORD)
        
        self.output.grid(row=0,column=1,padx=8,pady=2)
        self.output.setvalue('Command results will show in this box.\n\n')
        
        # PyMOL Command Prompt
        self.commandLine = Pmw.EntryField(interior, labelpos='w', label_text='Command Line:',
                           value='Enter PyMOL Commands Here', entry_width=45, command=self.command_line)
        self.commandLine.grid(row=1, column=0, columnspan=2, pady=2)
        
        #------------------------------------------#
        #                                          #
        #		MOVIE TAB		   #
        #					   #
        #------------------------------------------#
        # Add Movie tab to notebook
        page = notebook.add('  Movies  ')
        notebook.tab('  Movies  ').focus_set()
               
        group = Pmw.Group(page, tag_text="Movies")
        group.pack(fill='both', side=LEFT, expand='1', padx=2, pady=2)
        interior = group.interior()
	 
        # Ligand Zoom Movie Icon
        canvas1=Canvas(interior, width=57, height=48)
        canvas1.grid(row=0, column=0, padx=0, pady=0)
        canvas1.create_image(0,0,image=ligand,anchor=NW)
        
        self.addSpace(interior, 0, 1)
        
        # Grow Protein Movie Icon
        canvas2=Canvas(interior, width=57, height=48)
        canvas2.grid(row=0, column=2, padx=0, pady=0)
        canvas2.create_image(0,0,image=build, anchor=NW)
   
        # Color Chains Movie Icon
        canvas3=Canvas(interior, width=57, height=48)
        canvas3.grid(row=2, column=0, padx=0, pady=0)
        canvas3.create_image(0,0,image=chainsMovieImg, anchor=NW)
        
        self.addSpace(interior, 2, 1)
        
        # Rotate Movie Icon
        canvas4=Canvas(interior, width=57, height=48)
        canvas4.grid(row=2, column=2, padx=0, pady=3)
        canvas4.create_image(0,0,image=rotateImg, anchor=NW)
        
        # ligand zoom button
        self.buttonAdd(interior, 'Ligand Zoom',15,self.ligandZoom,1,0,N)
        
        # grow protein button
        self.buttonAdd(interior, 'Build Protein',15,self.growProtein,1,2,N)
        
      	# highlight chains button
	self.buttonAdd(interior, 'Highlight Chains', 15, self.highlight_chains,3,0,N)
	
        # rotate button
	self.buttonAdd(interior, 'Rotate', 15, self.rotate_y, 3, 2, N)
	
	# group containing movie controls
        controls = Pmw.Group(interior, tag_text="Movie Controls")
        controls.grid(row=4, column=0, columnspan=3, padx=2, pady=2)
        interior = controls.interior()
	
    	# play button image
    	canvas5=Canvas(interior, width=38, height=38)
    	canvas5.grid(row=0, column=0, padx=0, pady=3)
    	canvas5.create_image(2,2,image=playButton, anchor=NW)
    	self.addSpace(interior, 0, 1)
    	
    	# stop button image
    	canvas6=Canvas(interior, width=38, height=38)
    	canvas6.grid(row=0, column=2, padx=0, pady=3)
    	canvas6.create_image(2,2,image=stopButton, anchor=NW)
 	self.addSpace(interior, 0, 3)
    	
    	# rewind button image
    	canvas7=Canvas(interior, width=38, height=38)
    	canvas7.grid(row=0, column=4, padx=0, pady=3)
    	canvas7.create_image(2,2,image=rewindButton,anchor=NW)
    	
    	self.buttonAdd(interior, 'Play',10, self.play,1,0,'NSEW')
    	self.buttonAdd(interior, 'Stop', 10, self.stop,1,2,'NSEW')
        self.buttonAdd(interior, 'Rewind', 10, self.rewind,1,4,'NSEW')
 
        labels = ("Ray Tracing On")
    	self.ray = Pmw.RadioSelect(interior, labelpos='w', labelmargin=0, 
    		                   buttontype='checkbutton',orient='vertical',
    		                   command=self.ray)
    	self.ray.add("Ray Tracing On")
    	self.ray.grid(row=2, column=0, columnspan=5, padx=0)
  	 	
	#--------------------------------------#
        #			               #
        #            INFORMATION TAB           #
        #                                      #
        #--------------------------------------#
	page = notebook.add('Information')
	notebook.tab('Information').focus_set()
	
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
	
	filler = Label(page, text="     ")
	filler.grid(row=3, column=0)
	
	#Journal Entry Field
	label=Label(page, text="Primary Citation")
	label.grid(row=4, column=0, sticky='sw', padx=5, pady=0)
	self.jrnlEnt = Text(page, state=NORMAL, width=75,height=7)
	self.jrnlEnt.insert(END,"The primary citation will appear here")
	self.jrnlEnt.grid(row=5, column=0,columnspan=2,sticky='w',padx=5, pady=0)
	
	#Get PubMed Article Button
	self.buttonAdd(page,'Get PubMed Article',20,self.getPubMed,6,0,'W')
	
	#Hetero Atoms
	label=Label(page, text="Hetero Atoms")
	label.grid(row=1, column=1, sticky='sw', padx=5, pady=0)
	self.het = Text(page, state=NORMAL, height=1.4, width=25)
	self.het.insert(END,"List of hetero atoms")
	self.het.grid(row=2,column=1, sticky='w',padx=5,pady=0)
	
	#Chain List
	self.chain = Pmw.OptionMenu(page, labelpos='w',label_text = 'Chains:',items = ' ',menubutton_width=7, command=self.seqGetter)
    	self.chain.grid(row=7, column=0, sticky='w',padx=5,pady=5)
    	
    	#Chain Sequence Information
    	label=Label(page, text='Sequence')
    	label.grid(row=7, column=1, sticky='sw', padx=5, pady=0)
    	self.info =Text(page, state=NORMAL, height=4, width=40 )
        self.info.grid(row=8, column=1, columnspan=2, sticky='nw',padx=5, pady=0)
        
        #checks to see if there is a file loaded in the viewer prior to the GUI being opened
        self.fileLoaded = ' '
        loadedPDB=cmd.get_names()
        if loadedPDB!=[]:
        	self.fileLoaded = loadedPDB[0]
        	self.getPdb()
        self.fileLoaded = ' '
	
        #--------------------------------------#
        #			               #
        #           ADVANCED TAB               #
        #                                      #
        #--------------------------------------#
	page = notebook.add('Advanced')
	notebook.tab('Advanced').focus_set()
	
  	#-------------- Selection Dropdown -----------------
 	self.advancedSelection = Pmw.OptionMenu(page,label_text = 'Select:',labelpos = 'w',
                    items = ('All', 'Not Selected', 'Hydrophobic','Hydrophilic'),
                    menubutton_width = 10, command = self.set_sel)
                       
        self.advancedSelection.grid(row=0, column=0,sticky='W')
 	
 	#--------------- Setting Defaults -----------------
 	defaults = Pmw.OptionMenu(page,label_text = 'Reset:',labelpos = 'w',
                    items = ('Cartoon', 'Spheres', 'Sticks','Surface'),
                    menubutton_width = 10, command=self.set_advanced_defaults)
        defaults.grid(row=0,column=0,sticky='E')
	
	#--------------- Cartoon Group----------------
 	group = Pmw.Group(page, tag_text='Cartoon:')
 	group.grid(row=1, column=0, padx=1, pady=0, sticky='NW')
 	interior = group.interior()
 	 	
 	# Cartoon Width Slider
        self.toonWidth = Pmw.Counter(interior,labelpos='w',label_text='Width:',
                         entryfield_value='1.4', increment=.05,
                         datatype={'counter':'real','separator':'.'},
                         entryfield_validate={'validator':'real',
                         'min':'0.0','max':'2.0','separator':'.'})
        self.toonWidth.grid(row=0,column=0, padx=0, pady=0, sticky=E)
	self.buttonAdd(interior,'Update',10,self.cartoon_width,0,1,'SW')
	
	# Cartoon Thickness Slider
	self.toonThickness = Pmw.Counter(interior,labelpos='w',label_text='Thickness:',
                         entryfield_value='0.3', increment=.05,
                         datatype={'counter':'real','separator':'.'},
                         entryfield_validate={'validator':'real',
                         'min':'0.0','max':'2.0','separator':'.'})
	self.toonThickness.grid(row=1,column=0, padx=0, pady=0, sticky=E)
	self.buttonAdd(interior,'Update',10,self.cartoon_thickness,1,1,'SW')
	
	# Cartoon Transparency Slider
	self.cartoonTransparency = Pmw.Counter(interior, labelpos='w', label_text='Transparency:',
        		      entryfield_value='0.0', increment=.05,
        		      datatype={'counter':'real','separator':'.'},
        		      entryfield_validate={'validator':'real',
        		      'min':'0.0','max':'1.0','separator':'.'})
    	self.cartoonTransparency.grid(row=2, column=0, padx=0, pady=0, sticky='W')
    	self.buttonAdd(interior,'Update',10,self.cartoon_transparency,2,1,'SW')
    	
    	# Cartoon Tube Radius Slider
	self.toonTubeRadius = Pmw.Counter(interior, labelpos='w',label_text='Tube Radius:',
			      entryfield_value='0.5', increment=.1,
			      datatype={'counter':'real','separator':'.'},
                              entryfield_validate={'validator':'real',
                              'min':'0.0','max':'1.0','separator':'.'})
        self.toonTubeRadius.grid(row=3,column=0,padx=0,pady=0,sticky=E)
        self.buttonAdd(interior,'Update',10,self.cartoon_tube_radius,3,1,'SW')
        
        # Ribbon Type Slider
	self.ribbonTypes = Pmw.OptionMenu (interior,labelpos = 'w', label_text='Type:',
                items = ('Automatic', 'Skip', 'Loop', 'Rectangle', 'Oval', 'Tube', 'Arrow', 'Dumbbell','Putty'),
                menubutton_width = 7, command = self.ribType)
        self.ribbonTypes.grid(row=4, column=0, padx=75, columnspan=2, pady=0, sticky='W')
                
	#-------------- Sphere Group--------------------
	group = Pmw.Group(page, tag_text='Spheres:')
 	group.grid(row=2, column=0, padx=1, pady=0, sticky='NW')
 	interior = group.interior()     
        
        # Sphere Size Slider
        self.sphereScale = Pmw.Counter(interior, labelpos='w', label_text='Size:',
                           entryfield_value='0.7', increment=.05,
                           datatype={'counter':'real','separator':'.'},
                           entryfield_validate={'validator':'real',
                           'min':'0.0','max':'4.0','separator':'.'})
        self.sphereScale.grid(row=0, column=0, padx=0, pady=0, sticky=E)
        self.buttonAdd(interior,'Update',10,self.sphereSize,0,1,'SW')
        
        # Sphere Transparency Slider
	self.sphereTransparency = Pmw.Counter(interior, labelpos='w', label_text='Transparency:',
        		      entryfield_value='0.0', increment=.05,
        		      datatype={'counter':'real','separator':'.'},
        		      entryfield_validate={'validator':'real',
        		      'min':'0.0','max':'1.0','separator':'.'})
    	self.sphereTransparency.grid(row=1, column=0, padx=0, pady=0, sticky='W')
    	self.buttonAdd(interior,'Update',10,self.sphere_transparency,1,1,'SW')
    	
    	#--------------- Stick Group --------------------
    	group = Pmw.Group(page, tag_text='Sticks:')
    	group.grid(row=3, column=0, padx=1, pady=0, sticky='NW')
    	interior = group.interior()
    	
    	# Stick Radius Slider
        self.stickRadius = Pmw.Counter(interior, labelpos='w', label_text='Radius:',
                           entryfield_value='0.2', increment=.05,
                           datatype={'counter':'real','separator':'.'},
                           entryfield_validate={'validator':'real',
                           'min':'0.0','max':'3.0','separator':'.'})
        self.stickRadius.grid(row=0, column=0, padx=1, pady=0, sticky=E)
        self.buttonAdd(interior,'Update',10,self.stickRad,0,1,'SW')
               
        # Stick Transparency Slider
        self.stickTransparency = Pmw.Counter(interior,labelpos='w',label_text='Transparency:',
                            entryfield_value='0.0', increment=.05,
                            datatype={'counter':'real','separator':'.'},
                            entryfield_validate={'validator':'real',
                            'min':'0.0','max':'1.0','separator':'.'})
        self.stickTransparency.grid(row=1, column=0, padx=1, pady=0, sticky=E)
        self.buttonAdd(interior,'Update',10,self.stick_transparency,1,1,'SW')
        
        #-------------- Surface Group -------------------
        group = Pmw.Group(page, tag_text='Surface:')
	group.grid(row=4, column=0, padx=1, pady=0, sticky='NW')
	interior = group.interior()
	
	# Surface Transparency Slider
	self.surfaceTransparency = Pmw.Counter(interior,labelpos='w',label_text='Transparency:',
                            entryfield_value='0.0', increment=.05,
                            datatype={'counter':'real','separator':'.'},
                            entryfield_validate={'validator':'real',
                            'min':'0.0','max':'1.0','separator':'.'})
	self.surfaceTransparency.grid(row = 3, column=0, sticky='E')
	self.buttonAdd(interior, 'Update',10,self.surface_transparency,3,1,'SW')


        #--------------------------------------#
        #			               #
        #         SAVING YOUR WORK TAB         #
        #                                      #
        #--------------------------------------#
	page = notebook.add('   Save   ')
	notebook.tab('   Save   ').focus_set()
	
	#--------------- Cartoon Group----------------
 	group = Pmw.Group(page, tag_text='Save Options:')
 	group.pack(fill='both', side=LEFT, expand='1', padx=2, pady=2)
 	interior = group.interior()
 	
  	# save session button and explanation
	self.buttonAdd(interior, 'Save Session', 15, self.sessionSave, 0, 0, NW)
	saveSessionLabel = Label(interior, text='Choose this option to save '+
			   'a PyMOL file containing all of your work up '+
			   'to this point.', wraplength=275, justify=LEFT)
 	saveSessionLabel.grid(row=0, column=1, sticky=NW)
	
	self.addSpace(interior,1,0)
	self.addSpace(interior,2,0)
	# save image button & explanation
    	self.buttonAdd(interior, 'Save Image',15, self.imgSave,3,0,NW)
    	saveImgLabel = Label(interior, text='Choose this option when '+
    		      'you would like to save an image of the current '+
    		      'representation shown in the PyMOL Viewer', wraplength=275, justify=LEFT)
    	saveImgLabel.grid(row=3, column=1, sticky=NW)
    	
    	#--------------------------------------#
        #			               #
        #              ABOUT TAB               #
        #                                      #
        #--------------------------------------#
	page = notebook.add('About')
	notebook.tab('About').focus_set()
	
	aboutText = Label(page, text='EZ-Viz was created as part of a project funded by the NSF '+
	'in the summer of 2005.  Working at Brookhaven National Laboratory, Laura Grell and Chris '+
	'Parkin, both Bioinformatics majors at the Rochester Institute of Technology, developed this '+
	'interface hoping to simplify the molecular visualization process in PyMOL while also acting as '+
	'an educational tool to students and professors alike.\n\n'+
	'For questions and/or comments regarding this interface please contact Dr. Paul Craig at paul.craig@rit.edu.',
	wraplength=275, justify=LEFT)
 	aboutText.grid(row=0, column=0, sticky=NW)
 	
 	notebook.setnaturalsize()
	
    #--------------------------------------#
    #      		                   #
    #   HANDLE BUTTONS AT BOTTOM OF GUI    #
    #    (open, fetch.., help, exit)       #
    #--------------------------------------#         
    def execute(self, result):
        import tkFileDialog
    
        if result == 'Open':
            file=tkFileDialog.askopenfilename(initialdir='C:/Documents and Settings/Administrator/My Documents/')
            if file:
            	cmd.load(file)
            	self.pdbCode = file
            	#cmd.select('selection','all')
           	#cmd.deselect()
           	#----Connect to parser to read file------
		self.p=PDBParser()
            	self.p.readFile(file)
            	self.update(self.p)
            	self.std_view()
        elif result == 'Help':
            self.help()
        elif result == 'Fetch PDB':
            self.getPdb()
            self.std_view()
        elif result == 'Clear':
            cmd.reinitialize()
        else:
            self.dialog.withdraw()

    # Update all Labels on Information Tab  
    def update(self, p):
    	chainList=['All','Ligands','Not Selected','Hydrophobic','Hydrophilic']
        self.cmdType = 'PyMOL'
    	self.jrnlEnt.config(state=NORMAL)
    	self.jrnlEnt.delete(1.0,END)
    	self.jrnlEnt.insert(END, p.journal)
    	self.jrnlEnt.config(state=DISABLED)
    	self.classify.config(state=NORMAL)
    	self.classify.delete(1.0, END)
    	self.classify.insert(END, p.classify)
    	self.classify.config(state=DISABLED)
    	self.het.config(state=NORMAL)
    	self.het.delete(1.0, END)
    	self.het.insert(END, p.hetero)
    	self.het.config(state=DISABLED)
    	if len(p.hetero)!=0:
    		hetero=string.split(p.hetero, sep=', ')
    		hetero=string.join(hetero, sep='+')
    		cmd.create('ligands', '(resn '+string.strip(hetero)+')')
   	items=p.chains.keys()
    	items.sort()
    	self.chain.setitems(items)
    	items2=[]
    	prt=''
    	dna=''
    	rna=''
    	self.helixList = p.helices
    	self.init_color()
    	true=0
    	for id in items:
    		type =self.seqGetter(id)
    		if type=='Protein':
    			prt=prt+id
    			true=1
    		elif type=='DNA':
    			dna=dna+id
    		elif type=='RNA':
    			rna=rna+id   		
    		id = "Chain "+id
    		items2.append(id)
    	prt =string.join(prt, sep='+')
    	dna =string.join(dna, sep='+')
    	rna =string.join(rna, sep='+')
    	if prt !=' 'and prt !='':
    		cmd.create('protein', 'chain '+prt)
    		chainList.append("Protein")
    	if dna != '':
    		cmd.create('dna', 'chain '+dna)
    		chainList.append("DNA")
    	if rna != '':
    		cmd.create('rna', 'chain '+rna)
    		chainList.append("RNA")
   	#---------------ADDED 8/8------------------------#
    	if (prt==' ' or prt=='') and true==1:
    		cmd.create('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    		chainList.append("Protein")
    	#------------------------------------------------#
    	cmd.do('deselect')
    	chainList = chainList+items2
    	self.selection.setitems(chainList)
    	self.advancedSelection.setitems(chainList)
    	if p.name=='':
    		self.name.set("None Given")
    	else:
    		self.name.set(p.name)
	cmd.create('hydrophilic','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
	cmd.create('hydrophobic','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')

# //PyMOL_EZ.py     	
     
     	
  	
       
