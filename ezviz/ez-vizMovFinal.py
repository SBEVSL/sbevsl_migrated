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
                           label = 'EZ-Viz Movie',
                           command = lambda s=self : PGUI(s))

#---------------------------------------------------------------#
#                                                               #
#               Catalytic Site Atlas Parser                     #
#                                                               #
#   Get the residues that are involved in the active site       #
#                                                               #
#---------------------------------------------------------------#
class Csa:

    def __init__(self):
        self.true = 1

    #Read in the CSA file
    def readFile(self, file):
        active = ""
        aSites = []
        inFile = open(file, 'r')
        #get the object names from PyMOL
        names = cmd.get_names('all')
        pdb = names[0]
        #IF PDB IS "" THEN DISPLAY A POP-UP WINDOW TO TELL THE USER TO LOAD A FILE!!!!####
        #Create the regular expression matcher
        p = re.compile("^"+pdb, re.IGNORECASE)

        count = 0
        sites = 0
        lineNum = 1

        while self.true:
            line = inFile.readline()
            if line == "":
                break
            #Find the line(s) for the specific loaded PDB file
            elif p.match(line):
                lineArray = line.split(',')
                siteNum = string.atoi(lineArray[1])
                num = sites + siteNum + 1
                if (num > sites):
                    sites = siteNum +1 
                count += 1
            lineNum += 1
        inFile.close()
        
        inFile = open(file, 'r')
        for i in range(sites):
            aSites.append("")

        while self.true:
            line = inFile.readline()
            if line == "":
                break
            elif p.match(line):
                #grab the characters we need to select the active site
                lineArray = line.split(',')
                siteNum = lineArray[1]
                residueName = lineArray[2]
                resiChain = lineArray[3]
                resiNum = lineArray[4]
                #create on ID string based on if the chain ID is given
                if resiChain == "":
                    id = "resi " + resiNum
                else:
                    id = resiChain + "/" + resiNum +"/"
                active = id + " + "
                i = string.atoi(siteNum)
                val = aSites[i]
                val += active
                aSites[i] = val
        #close the file
        inFile.close()
        return aSites

#---------------------------------------------------------------#
#								                                #
#                       PDBParser                               #
#								                                #
#								                                #
#								                                #
#       Parse PDB files and pull out the useful information     #
#								                                #
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
		self.heteroMov=''
		self.hlist=[]
		#the ligand list that will be displayed on the movie tab
		self.hlistMov=[]
		self.chains={}
		self.classify=''
		self.idList=[]
		self.allHet=[]
		self.helices=[]
		self.actionString=''
	
	
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
          	self.heteroMov=string.join(self.hlistMov, sep=', ')
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
  	    #get the name of the group - ex. HEM, P04
  		temp = string.strip(line[7:10])
  		#get the sequence ID number
  		id = string.strip(line[13:17])
  		#create a list with each name only appearing once for the Info tab
  		if self.hlist.count(temp)==0:
  			self.hlist.append(temp)
  			#self.idList.append(id)
  		else:
  			pass
  		#get the letter of the chain
  		chain=string.strip(line[11:13])
  		#if there is no chain identifer just use the sequence id
  		if chain == "":
  			id = 'resi '+ id
  		#otherwise use both chain and id 
  		else:
  			id = chain+"/"+id+"/"
  			
  		#append all the ids to the idlist for use in movies
  		self.idList.append(id)
  		#create a list with all names for the Movie Tab drop down
  		self.hlistMov.append(temp + ' ' + id)
  		
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
    global count
    
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
    splash = PhotoImage(file="modules\pmg_tk\startup\splash_movie.gif")
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
        self.comm = ("color carbgray, elem C" + str+"; color red, elem O" + str +"; color white, elem H" + str +"; "+
                "color nitblue, elem N"+str + "; color sulfyellow, elem S" + str +"; color phosorange, elem P+Fe+Ba"+str+"; "+
                "color green, elem Cl+B"+str+"; color brown, elem Br+Zn+Cu+Ni"+str +"; color blue, elem Na"+str+"; "+
                "color forest, elem Mg"+str+"; color darkgray, elem Ca+Mn+Al+Ti+Cr+Ag"+str+"; color goldenrod, elem Au+F+Si"+str+"; "+
                "color ipurple, elem I"+str+"; color firebrick, elem Li"+str+"; color helpink, elem He"+str+";")

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
            self.comm = "#show lines for "+sel+"\nshow lines, "+sel+"\n"
        elif tag == 'Sticks':
            cmd.show('sticks', sel)
            self.comm = "#show sticks for "+sel+"\nshow sticks, "+sel+"\n"
        elif tag == 'Ribbons':
            cmd.show('ribbon', sel)
            self.comm = "#show ribbons for "+sel+"\nshow ribbon, "+sel+"\n"
        elif tag == 'Cartoon':
            cmd.show('cartoon', sel)
            self.comm = "#show cartoon for "+sel+"\nshow cartoon, "+sel+"\n"
        elif tag == 'Dots':
            cmd.show('dots', sel)
            self.comm = "#show dots for "+sel+"\nshow dots, "+sel+"\n"
        elif tag == 'Spheres':
            cmd.show('spheres', sel)
            self.comm = "#show spheres for "+sel+"\nshow spheres, "+sel+"\n"
        elif tag == 'Mesh':
            cmd.show('mesh', sel)
            self.comm = "#show mesh for "+sel+"\nshow mesh, "+sel+"\n"
        elif tag == 'Surface':
            cmd.show('surface', sel)
            self.comm = "#show surface for "+sel+"\nshow surface, "+sel+"\n"
        elif tag == 'Water':
            cmd.show('(resn HOH)')
            cmd.show('spheres', '(resn HOH)')
            self.comm = "#show spheres for "+sel+"\nshow spheres, resn HOH\n"
        elif tag == 'Everything':
            cmd.show('everything', sel)
            self.comm = "#show everything for "+sel+"\nshow everything, "+sel+"\n"
        elif tag=='Ball and Stick':
            cmd.set('sphere_scale', '0.35', sel)
            cmd.show('spheres',sel)
            cmd.show('sticks',sel)
            self.comm = "#show ball and stick for "+sel+"\nshow spheres, "+sel+"\nshow sticks, "+sel+"\n"
        self.currentSelBox.setentry(self.comm)
      	    
    # Hide individual representations
    def hide_rep(self, tag):
    	sel = self.sel
        if tag == 'Lines':
            cmd.hide('lines',sel)
            self.comm = "#hide lines for "+sel+"\nhide lines , "+sel+"\n"
        elif tag == 'Sticks':
            cmd.hide('sticks', sel)
            self.comm = "#hide sticks for "+sel+"\nhide sticks, "+sel+"\n"
        elif tag == 'Ribbons':
            cmd.hide('ribbon', sel)
            self.comm = "#hide ribbon for "+sel+"\nhide ribbon, "+sel+"\n"
        elif tag == 'Cartoon':
            cmd.hide('cartoon', sel)
            self.comm = "#hide cartoon for "+sel+"\nhide cartoon, "+sel+"\n"
        elif tag == 'Dots':
            cmd.hide('dots', sel)
            self.comm = "#hide dots for "+sel+"\nhide dots, "+sel+"\n"
        elif tag == 'Spheres':
            cmd.hide('spheres', sel)
            self.comm = "#hide spheres for "+sel+"\nhide spheres, "+sel+"\n"
        elif tag == 'Mesh':
            cmd.hide('mesh', sel)
            self.comm = "#hide mesh for "+sel+"\nhide mesh, "+sel+"\n"
        elif tag == 'Surface':
            cmd.hide('surface', sel)
            self.comm = "#hide surface for "+sel+"\nhide surface, "+sel+"\n"
        elif tag == 'Water':
            cmd.hide('(resn HOH)')
            self.comm = "#hide water for "+sel+"\nhide resn HOH\n"
        elif tag == 'Everything':
            cmd.hide('everything', sel)
            self.comm = "#hide everything for "+sel+"\nhide everything, "+sel+"\n"
        elif tag=='Ball and Stick':
            cmd.hide('spheres',sel)
            cmd.hide('sticks',sel)
            self.comm = "#hide ball & stick for "+sel+"\nhide spheres, "+sel+"\n hide sticks, "+sel+"\n"
        self.currentSelBox.setentry(self.comm)
        
    # Set selection of atoms
    # initial selection is 'all'
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
            #changed 3/31/07 fixed chain deselection error
            id = tag[5]
            cmd.select(tag, 'chain '+id)
            cmd.deselect()
            self.sel='chain ' + id
        elif tag=='Not Selected':
            cmd.select('selection', '!'+self.sel)
            cmd.deselect()
            self.sel= 'selection'
        elif tag=='Hydrophobic':
            self.sel='hydrophobic'
        elif tag=='Hydrophilic':
            self.sel='hydrophilic'
        else:
            self.sel = tag
		
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
            self.comm = "#color "+sel+" red\ncolor red , "+sel+"\n"
        elif tag=='Green':
            cmd.color('green', sel)
            self.comm = "#color "+sel+" green\ncolor green, "+sel+"\n"
        elif tag=='Orange':
            cmd.color('orange', sel)
            self.comm = "#color "+sel+" orange\ncolor orange, "+sel+"\n"
        elif tag=='Yellow':
            cmd.color('yellow', sel)
            self.comm = "#color "+sel+" yellow\ncolor yellow, "+sel+"\n"
        elif tag=='Blue':
            cmd.color('blue', sel)
            self.comm = "#color "+sel+" blue\ncolor blue, "+sel+"\n"
        elif tag=='Violet':
            cmd.color('violet', sel)
            self.comm = "#color "+sel+" violet\ncolor violet, "+sel+"\n"
        elif tag=='CPK':
            self.color_cpk(' & '+sel)
        elif tag=='Other':
            color=tkColorChooser.askcolor(parent=self.int, title="Selection Color Chooser")
            colorArray =[]
            if color[0]!= None:
                list=color[0]
                #print list
                for each in list:
                    z = (each/255.0)
                    val=repr(z)
                    colorArray.append(val)
                cmd.set_color('newcolor', colorArray)
                cmd.color('newcolor', sel) 
                self.comm = ("#color "+sel+" newcolor\nset_color newcolor, ["+colorArray[0]+","+colorArray[1]+", "+colorArray[2]+"]"+
                "\ncolor newcolor, "+sel+"\n")
        self.currentSelBox.setentry(self.comm)
        
    
    #--------------------------------------#
    #					                   #
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
    	
    	file = tkFileDialog.asksaveasfilename(defaultextension=".pse", initialdir='C:/Program Files/Delano Scientific/PyMOL/')
        if len(file)>0:
    		cmd.save(file)      
        
    
    #--------------------------------------#
    #					                   #
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
    #					                   #
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
    		cmd.set('seq_view_format', '3')
    	elif tag == "Atoms":
    		cmd.set('seq_view_format', '2')
    	else:
    		cmd.set('seq_view_format', '4')
    	
    #Frame Speed Settings
    def frame_speed(self, tag):
    	if tag == '30':
    		cmd.set('movie_delay', '33')
    	elif tag == '15':
    		cmd.set('movie_delay', '66')
    	elif tag == '5':
    		cmd.set('movie_delay', '200')
    	elif tag == '1':
    		cmd.set('movie_delay', '1000')
    	elif tag == '0.3':
    		cmd.set('movie_delay', '3000')
    	else:
    		cmd.set('movie_delay', '0')
    		

    #--------------------------------------#
    #					                   #
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
    	self.info.component('text').config(state=NORMAL)
    	self.info.delete(1.0,END)
    	self.info.insert(END, info)
    	#self.info.config(state=DISABLED)
    	return type
    	
    #--------------------------------------#
    #					                   #
    #           MAKE MOVIE METHODS         #
    #                                      #
    #--------------------------------------#
    
    #update the output box
    def updateOutput(self, command):
        cmd = str(command)
        name = str(self.count)
        self.movOutput.mark_set(name, INSERT)
        self.movOutput.mark_gravity(name, LEFT)
        self.movOutput.appendtext(cmd)
        self.count += 1
    
    #write out the movie commands to file
    def writeFile(self):
        import tkFileDialog
        file = tkFileDialog.asksaveasfilename(defaultextension=".py", initialdir='C:/Program Files/Delano Scientific/PyMOL/')
        if len(file)>0:
            #set the loaded movie file label
            dir = string.split(file, "/")
            i = len(dir)-1
            self.fileMovie.set(dir[i])
            #append the number of frames to the end of the file
            self.movOutput.appendtext("#"+str(self.currentFrame))
            #export the movie to file
            self.movOutput.exportfile(file)
            #remove the added number of frames from the output window
            self.movOutput.component('text').config(state=NORMAL)
            self.movOutput.delete("%s -1lines" % END,END)
            self.movOutput.insert(END, "\n")
            self.movOutput.component('text').config(state=DISABLED)
            
    
    #read the CSA file and extract the active site for the molecule
    #update the drop down to contain the actve sites
    def enableAS(self):
        c = Csa()
        #call readFile from the CSA class
        self.activeSites = c.readFile("modules\pmg_tk\startup\CSA.dat")
        #delete the current active sites menu
        self.object_menu.delete(0)
        self.feature_menu.delete(0)
        #create a new active sites menu
        self.activemenu = Menu(self.ligandsmb, tearoff=0)
        self.frameactivemenu = Menu(self.sButton, tearoff=0)
        self.object_menu.insert_cascade(0, label="Active Sites", menu=self.activemenu)
        self.feature_menu.insert_cascade(0, label="Active Sites", menu=self.frameactivemenu)
        #fill the active sites menu
        if (len(self.activeSites) == 0):
            self.activemenu.add_command(label="No active sites listed")
            self.frameactivemenu.add_command(label="No active sites listed")
        else:
            for site in range(len(self.activeSites)):
                val = self.activeSites[site]
                self.activeSites[site] = val.rstrip(" +")
                self.activemenu.add_command(label=self.activeSites[site], command=lambda i=self.activeSites[site]: self.ligSet(i))  
                self.frameactivemenu.add_command(label=self.activeSites[site], command=lambda i=self.activeSites[site]: self.selSet(i))
    
    #parse the selected value so it returns the correct selection value
    #take in the currently selected menu value and parse it to determine the correct syntax
    def parseCommand(self, value):
        if (value.find("+") != -1):
            #set the action string accordingly
            actionString = value
        else:
            selection = string.split(value)
            if (selection[0] == "Click"):
                actionString = ""
            elif (len(selection) == 1):
                if (selection[0] == "Hydrophobic"):
                    actionString = "hydrophobic"
                elif (selection[0] == "Hydrophilic"):
                    actionString = "hydrophilic"
                elif (selection[0] == "All"):
                    actionString = "all"
                elif (selection[0] == "Protein"):
                    actionString = "protein"
                elif (selection[0] == "DNA"):
                    actionString = "dna"
                elif (selection[0] == "Ligands"):
                    actionString = "ligands"
                elif (len(selection[0])== 1):
                    actionString = "chain " + selection[0]
                else:
                    actionString = selection[0]
            elif (len(selection) == 2):
                actionString = "resn " + selection[0] + " and " + selection[1]
            elif (len(selection) == 3):
                actionString = "resn " + selection[0] + " and " + selection[1] + " " + selection[2]
            else:
                actionString = selection
        return actionString

    #Issues the mstore commands that change the frames for the movie
    def addFrames(self):
        self.framesAdded = 1
        import tkMessageBox
        answer = 1
        if self.movieMade == 1:
            answer = tkMessageBox.askyesno("Add More Frames", "Adding more frames to your movie will \"unmake\" your movie."+
                "\nTo incorporate the added frames into your movie please click the 'Make Movie' button.\nDo you wish to proceed?")
            #If the user wishes to continue
            if answer == 1:
                #delete the interpolation code from the output box
                self.movOutput.component('text').config(state=NORMAL)
                self.movOutput.delete("%s-3lines"% END, END)
                self.movOutput.insert(END, "\n")
                #delete the frames setting command from the output box
                self.movOutput.delete("1.end", "3.end")
                self.movOutput.component('text').config(state=DISABLED)
                #enable the make movie button and disable the edit and undo button
                self.make.config(state=NORMAL)
                self.edit.config(state=DISABLED)
                self.undo.config(state=NORMAL)
                #let the interface know the movie is not made
                self.movieMade = 0
        else:
            if self.currentFrame == 1:
                comm = "#store current frame as starting frame\n" + "%s%d%s" % ("cmd.mview(\'store\', ",self.currentFrame, ")\n")
            else:
                comm = ""
            #get the feature to be added 
            fet = self.feature.getvalue()
            #getting the ending frame for the sequence
            if (self.currentFrame == 1):
                self.currentFrame += (string.atoi(self.frames.getvalue()) - 1)
            else:
                self.currentFrame += string.atoi(self.frames.getvalue())
            #depending on feature selected, issue commands to make changes
            if fet == 'Zoom In':
                #get the seleced ligand/chain from the dropdown
                actionString = self.parseCommand(self.ligands.getvalue())
                cmd.orient(actionString)
                comm += "#Zoom in on bound ligand\ncmd.orient(\'"+ actionString+"\')\n"
            elif fet == 'Zoom Out':
                cmd.orient();
                comm += "#Zoom out from bound ligand\ncmd.orient()\n" 
            elif fet == 'Rotate Y 180':
                cmd.turn('y',180)
                comm += "#Rotate molecule on Y\ncmd.turn('y',180)\n"
            elif fet == 'Rotate X 180':
                cmd.turn('x', 180)
                comm += "#rotate molecule on X\ncmd.turn('x', 180)\n"
            elif fet == 'Rotate Z 180':
                cmd.turn('z', 180)
                comm += "#rotate molecule on Z\ncmd.turn('z', 180)\n"
            else:
                comm += "%s%d%s" % ("#hold on this view\ncmd.mview(\'store\', " ,self.currentFrame, ")\n")
            self.currentFrameBox.setvalue(self.currentFrame)
            comm += "#store as ending frame\n" + "%s%d%s" % ("cmd.mview(\'store\', ",self.currentFrame, ")\n")
            #add the commands for adding the frames to the output box
            self.updateOutput(comm)
            #let the interface know the movie is not made
            self.movieMade = 0

    def undoAction(self):
        self.framesRemoved = 1
        #get the command that is next in the list to be undone
        name = str((self.count-1))
        if name != "0":
            self.movOutput.component('text').config(state=NORMAL)
            self.movOutput.delete(name, INSERT)
            self.count -= 1
            #search for previously executed command on the molecule and revert molecule to that position
            previous = self.movOutput.getvalue()
            commands = string.split(previous, "\n")
            #delete the mview commands so the frames are not set when going back to last executed frame
            for i in range (len(commands)):
                line = commands[i]
                if line.startswith("cmd.mview"):
                    commands[i] = "" 
            #rest the molecule to its starting position
            cmd.do('reset')
            #make the molecule appear as it would prior to the "undone' command being issued
            cmd.do(commands)
        #only if there are commands left to delete, calculate the current frame
        #if a movie has been loaded, and all newly added commands are removed set the current frames
        #to the number of frames the movie was saved at
        if (self.count != 1 or (self.count==1 and self.loadedMovie==1)):
            #get the previously executed store command
            stayCommand = self.movOutput.get("%s -2lines"%INSERT, INSERT)
            #break it apart at the comma
            broken = string.split(stayCommand, ", ")
            #get the second part with the frame number - remove whitespace and the parenthese
            stay = broken[1].strip()
            stay = stay.rstrip(")")
            self.currentFrame = string.atoi(stay)
        #otherwise set the current frame to 1
        else:
            self.currentFrame = 1
        #set the current frame box on the main window to the number of frames remaining
        self.currentFrameBox.setvalue(self.currentFrame)
        self.movOutput.component('text').config(state=DISABLED)
               

    def enableButtons(self):
        #enable all buttons on the interface
        self.make.config(state=NORMAL)
        self.edit.config(state=DISABLED)
        self.write.config(state=NORMAL)
        self.addSeq.config(state=NORMAL)
        self.prev.config(state=NORMAL)
        self.undo.config(state=NORMAL)
        self.currentFrameBox.component('entry').config(state='readonly')
        self.currentFrameBox.component('label').config(state=NORMAL)
        self.feature.component('Zoom In').config(state=NORMAL)
        self.feature.component('Zoom Out').config(state=NORMAL)
        self.feature.component('Rotate Y 180').config(state=NORMAL)
        self.feature.component('Rotate X 180').config(state=NORMAL)
        self.feature.component('Rotate Z 180').config(state=NORMAL)
        self.feature.component('Hold on View').config(state=NORMAL)
        self.feature.component('label').config(state=NORMAL)
        self.ligands.component('menubutton').config(state=NORMAL)
        self.ligands.component('label').config(state=NORMAL)
        self.frames.component('menubutton').config(state=NORMAL)
        self.frames.component('label').config(state=NORMAL)
        self.ligands.setvalue("Click to choose")
        self.frames.setvalue("1")
        
    #Set Initial conditions of the GUI
    def initial(self):
        #set the current frame to 1 - this will be updated as we add to the movie
        self.currentFrame = 1;
        cmd.mclear()
        #disable all the buttons - except for 'New Movie' & 'Load Movie'
        self.write.config(state=DISABLED)
        self.make.config(state=DISABLED)
        self.addSeq.config(state=DISABLED)
        self.edit.config(state=DISABLED)
        self.prev.config(state=DISABLED)
        self.currentFrameBox.component('entry').config(state=DISABLED)
        self.currentFrameBox.component('label').config(state=DISABLED)
        self.feature.component('Zoom In').config(state=DISABLED)
        self.feature.component('Zoom Out').config(state=DISABLED)
        self.feature.component('Rotate Y 180').config(state=DISABLED)
        self.feature.component('Rotate X 180').config(state=DISABLED)
        self.feature.component('Rotate Z 180').config(state=DISABLED)
        self.feature.component('Hold on View').config(state=DISABLED)
        self.feature.component('label').config(state=DISABLED)
        self.ligands.component('menubutton').config(state=DISABLED)
        self.ligands.component('label').config(state=DISABLED)
        self.movOutput.component('text').config(state=DISABLED)
        self.frames.component('menubutton').config(state=DISABLED)
        self.frames.component('label').config(state=DISABLED)
        self.undo.config(state=DISABLED)

    #move to the specified frame of the movie according to the slider
    def moveFrame(self, num):
        frame = self.slider.get() 
        cmd.frame(frame)
        self.label.set("Frame "+str(frame))

    #update the slide bar to the correct number of total frames
    def slideUpdater(self, *args):
        self.slider.config(to=string.atoi(self.slideNum.get()))

    #set the around ligands value
    def setAround(self, tag):
        selection = self.selVar.get()
        #strip the angstrom character from the tag of the selection
        tag = (tag.split())[0]
        if ((selection.find("+") != -1) and (tag != "None")):
            self.sel = selection + " around "+tag
        elif (len(selection)>2):
            command = self.parseCommand(selection)
            if (tag != "None"):
                self.sel = command + " around " + tag
            else:
                self.sel = command
        self.currentSelBox.setentry(self.sel)

    #show the frame editor window
    def showEditor(self):
        self.sel ="all"
        #set the dropdowns and entry fields back to their default values
        self.colors.setvalue('Red')
        self.hideFrameRep.setvalue('Lines')
        self.viewFrameRep.setvalue('Lines')
        self.ligSelector.setvalue('All')
        self.presets.setvalue('Default')
        self.currentSelBox.clear()
        self.frameEdits.clear()
        self.comm = ""
        if (self.editor.active() == 0):
            self.editor.activate('nograb')
        else:
            self.editor.show()

    #accept the changes made to the molecule in the frame editor
    def accept(self):
        #get most recent change
        command = self.comm.split("\n")
        #clear the command string
        self.comm = ""
        for each in command:
            cmd.do(each)
            if (each != ""):
                self.frameEdits.appendtext(each+"\n")
        
    def undoEdit(self):
        self.frameEdits.delete("%s -1lines" % INSERT, INSERT)

    #once all changes have been accepted - set the frame
    def setFrame(self):
        frame = self.slider.get()
        #only if the window is NOT empty
        if (self.frameEdits.get("1.0") !="\n" ):
            #get the commands from the window
            commands = self.frameEdits.get()
            #remove all the new line characters from the commands
            commands = commands.rstrip("\n")
            commands = commands.replace("\n", " ")
            #send the command to the output window
            self.movOutput.component('text').config(state=NORMAL)
            #insert the mdo commands above all the frame adding commands
            #check to see if the frame has already been edited
            pos = self.movOutput.search("cmd.do('mdo "+str(frame)+":", "1.0", END)
            #if it hasn't been edited insert the command
            if not pos:
                self.movOutput.insert("EDITS", "cmd.do(\'mdo "+str(frame)+": "+commands+"\')\n")
            #if it has been executed, delete the previous command and input the new command
            else:
                self.movOutput.delete(pos, "%s +1lines" %pos)
                self.movOutput.insert("EDITS", "cmd.do(\'mdo "+str(frame)+": "+commands+"\')\n")
            self.movOutput.component('text').config(state=DISABLED) 
            #issue the commands so that the changes will occur in the previewed movie
            print "MOVIE"+commands+"COMMANDS"
            cmd.do("mdo "+str(frame)+": "+commands)
            #clear the edit box when the frame is completed
            self.frameEdits.clear()

    #set the selection on the frame editor window
    def selSet(self,name):
        self.selVar.set(name)
        selection = self.parseCommand(name)
        self.sel = selection
        self.currentSelBox.setvalue(self.sel)

    #update the ligand/chain drop-down to display the currently selected object     
    def ligSet(self, name):
        self.ligVar.set(name)

    #start a new movie
    def newMovie(self):
        import tkMessageBox
        import tkFileDialog
        self.movOutput.component('text').config(state=NORMAL)
        #checks if there is a movie created in the box
        if (self.movOutput.get('2.0') != "\n" and self.movOutput.get('2.0') != ""):
            answer = tkMessageBox.askyesno("Save Current Movie", "Do you want to save the current movie? If no, the current movie will be lost.")
            if (answer == 1):
                file = tkFileDialog.asksaveasfilename(defaultextension=".pml", initialdir='C:/Program Files/Delano Scientific/PyMOL/')
                if (len(file)>0):
                    self.movOutput.exportfile(file)
        self.movOutput.component('text').config(state=DISABLED)
        #need to check if a PDB file is loaded - movies can only be created with a PDB file loaded
        list = cmd.get_names()
        if (len(list)!=0):
            #clear the movie box
            self.movOutput.clear()
            self.movOutput.appendtext("#"+list[0]+"\n")
            cmd.mstop()
            cmd.mclear()
            cmd.mset()
            cmd.reset()
            #update the loaded movie label
            self.fileMovie.set("")
            #set the movie speed to 15
            self.speed.invoke('15')
            self.enableButtons()
        else:
            tkMessageBox.showinfo("Load PDB File", "You must load a PDB file before creating a movie")
        self.currentFrame = 1
        self.currentFrameBox.setvalue(self.currentFrame)

    #load a movie from file
    def loadMovie(self):
        import tkFileDialog
        import tkMessageBox
        if (len(cmd.get_names()) == 0):
            tkMessageBox.showinfo("Load PDB File", "Please load the corresponding PDB file for the movie that you want to "+
                    "load, prior to loading the movie")
        else:
            self.loadedMovie = 1
            file = tkFileDialog.askopenfilename(defaultextension=".py", initialdir='C:/Program Files/Delano Scientific/PyMOL/')
            if file != "":
                #stop the currently playing movie if there is one
                cmd.mstop()
                #clear movie output and put PDB file name at top of box
                self.movOutput.clear()
                list = cmd.get_names()
                self.movOutput.appendtext("#"+list[0]+"\n")
                #set the loaded movie file label
                dir = string.split(file, "/")
                i = len(dir)-1
                self.fileMovie.set(dir[i])
                #clear the movie cache
                cmd.mclear()
                cmd.mset()
                #set the movie speed to 15
                self.speed.invoke('15')
                #clear the movie output box to import the file into
                self.movOutput.component('text').config(state=NORMAL)
                self.movOutput.clear()
                self.movOutput.importfile(file)
                #get the PDB code to check if the right molecule is loaded for the movie
                name = self.movOutput.get('1.1', '1.end')
                #if the molecule name is correct
                if name == (cmd.get_names())[0]:
                    #run the file
                    cmd.do('run '+file)
                    #update the frames added varible to notify that frames have been added since last preview
                    self.framesAdded =1
                    #set the number of frames for the movie that is being loaded
                    #get the number of frames from the last line of the movie file
                    frames = self.movOutput.get("%s -1lines"%INSERT, INSERT)
                    #delete the number of frames so that it doesn't appear in the output window
                    self.movOutput.delete("%s -1lines"%INSERT, INSERT)
                    #strip the white space and the comment from the number of frames
                    frames = frames.lstrip('#')
                    frames = frames.rstrip()
                    self.currentFrame = string.atoi(frames)
                    #set the number of frames on the edit frame window slidebar
                    self.slideNum.set(self.currentFrame)
                    #set the number of frames in the current frames box on the main window
                    self.currentFrameBox.component('entry').config(state="readonly")
                    self.currentFrameBox.setvalue(self.currentFrame)
                    #Insert mark that lets it know not to delete beyond this point
                    self.movOutput.mark_set("LOADED", INSERT)
                    self.movOutput.mark_gravity("LOADED", LEFT)
                    
                    #determine if the movie is already made and set the movieMade value/button accordingly
                    #get the last line of the movie file
                    pos = self.movOutput.search("interpolate", "1.0", END)
                    #if the word interpolate is on the last line the movie is made
                    if pos:
                        self.movieMade = 1
                    #otherwise the movie is not made
                    else:
                        self.movieMade = 0
                    #update the buttons on the interface to go along with actions
                    self.enableButtons()
                    if self.movieMade == 1:
                        #disable the make and undo buttons
                        self.make.config(state=DISABLED)
                        self.undo.config(state=DISABLED)
                        #set the area where frame edits are to be added to the output window
                        self.movOutput.mark_set("EDITS", "4.0")
                        self.movOutput.mark_gravity("EDITS", LEFT)
                        #enable the edit frames button
                        self.edit.config(state=NORMAL)
                    self.movOutput.component('text').config(state=DISABLED) 
                #otherwise this is not the correct PDB file for this movie - show error  
                else:
                    tkMessageBox.showerror("Incorrect PDB", "This is not the correct PDB file for this movie. Please load the "+
                        "PDB file "+name)
                    self.initial()
                    self.movOutput.clear()

    #preview the movie
    def preview(self):
        #if frames are added or removed then execute the movie making commands
        if ((self.framesAdded == 1) or (self.framesRemoved == 1)):
            #set the total number of frames that the user had created - append frame setting command to top of output
            self.movOutput.component('text').config(state=NORMAL)
            self.movOutput.component('text').insert("2.0", "#set the number of frames\ncmd.mset('1', "+ "%d%s" % (self.currentFrame, ")\n"))
            #set the slider to the correct number of frames on the edit frames window
            self.slideNum.set(self.currentFrame)
            #add the interpolate and stop commands to the end of the output window
            self.movOutput.insert(END, "#make movie\ncmd.mview(\'interpolate\')\nmdo "+str(self.currentFrame)+": mstop;")
            allCommands = self.movOutput.getvalue()
            #clear the current movie contents
            cmd.mclear()
            cmd.mset()
            cmd.mdump()
            cmd.do('reset')
            #execute the new movie
            cmd.do(allCommands)
            #delete the interpolate and frame setting commands from the output window
            self.movOutput.delete("%s-3lines"% END, END)
            self.movOutput.insert(END, "\n")
            self.movOutput.delete("1.end", "3.end")
        #once the movie is made then rewind and play it
        #rewind the previewed movie and play it for the user
        cmd.rewind()
        cmd.mplay()
        #reset the variables for adding and removing frames
        self.framesAdded = 0
        self.framesRemoved = 0
        

    #interpolate all the frames created by mview
    def interpolate(self):
        self.movieMade = 1
        #set the total number of frames that the user had created - append frame setting command to top of output
        self.movOutput.component('text').config(state=NORMAL)
        self.movOutput.component('text').insert("2.0", "#set the number of frames\ncmd.mset('1', "+ "%d%s" % (self.currentFrame, ")\n"))
        #insert a mark here to tell edit frames where to insert new mdo commands
        self.movOutput.mark_set("EDITS", "4.0")
        self.movOutput.mark_gravity("EDITS", LEFT)
        self.slideNum.set(self.currentFrame)
        self.movOutput.insert(END, "#make movie\ncmd.mview(\'interpolate\')\n")
        #clear the movie cache
        cmd.mclear()
        cmd.mset()
        #reset the molecule to its original orientation
        cmd.reset()
        #get all the movie commands from the output box
        allCommands = self.movOutput.getvalue()
        #execute the commands
        cmd.do(allCommands)
        #rewind the movie to the start
        cmd.rewind()
        #set the buttons to the correct states
        self.movOutput.component('text').config(state=DISABLED) 
        self.make.config(state=DISABLED)
        self.edit.config(state=NORMAL)   
        self.undo.config(state=DISABLED)
        #self.write.config(state=NORMAL)

    def movPresets(self, tag):
        #self.std_view()
        objects = cmd.get_names()
        frame = self.slider.get()
        #self.set_defaults()
        if (tag == 'Default'):
            self.comm = ('hide everything, all; show cartoon, protein; color red, ss h; color yellow, ss s;' +
                'color cyan, ss l+;') 

            if 'dna' in objects:
   	            self.comm += ('show sticks, dna; color carbgray, elem C & dna; color red, elem O & dna; color white, elem H & dna; '+
                        'color nitblue, elem N & dna; color sulfyellow, elem S & dna; color phosorange, elem P+Fe+Ba & dna; ' +
                        'color green, elem Cl+B & dna; color brown, elem Br+Zn+Cu+Ni & dna; color blue, elem Na & dna; '+
                        'color forest, elem Mg & dna; color darkgray, elem Ca+Mn+Al+Ti+Cr+Ag & dna; color goldenrod, elem Au+F+Si & dna; '+
                        'color ipurple, elem I & dna ; color firebrick, elem Li & dna; color helpink, elem He & dna;')

            if 'rna' in objects:
                self.comm += ('show sticks, rna; show spheres, rna; color carbgray, elem C & rna; color red, elem O & rna; '+
                        'color white, elem H & rna; color nitblue, elem N & rna; color sulfyellow, elem S & rna; '+
                        'color phosorange, elem P+Fe+Ba & rna; color green, elem Cl+B & rna; color brown, elem Br+Zn+Cu+Ni & rna; '+
                        'color blue, elem Na & rna; color forest, elem Mg & rna; color darkgray, elem Ca+Mn+Al+Ti+Cr+Ag & rna; '+
                        'color goldenrod, elem Au+F+Si & rna; color ipurple, elem I & rna ; color firebrick, elem Li & rna; '+
                        'color helpink, elem He & rna;')

            if 'ligands' in objects:
                self.comm += ('show spheres,ligands; color cyan,ligands;')
            self.currentSelBox.setentry("set molecule to default view")

        elif (tag=='Ball & Stick'):
            self.comm += ('hide everything; set stick_radius,0.1,all; set sphere_scale,0.3,all;')
        
            if 'protein' in objects:
                self.comm+= ('show spheres, protein; show sticks, protein; color green, elem C; color red, elem O; ' +
	                    'color blue, elem N;')

            if 'dna' in objects:
                self.comm+=('show sticks, dna; set stick_radius, 0.2, dna; hide spheres, dna; ')
                self.colorCpkMov(' & dna') 

            if 'rna' in objects:
                self.comm+=('show spheres, rna; show sticks, rna; ')
                self.colorCpkMov(' & rna')

            if 'ligands' in objects:
                self.comm+=('color orange, ligands;')
            self.currentSelBox.setentry("set molecule to ball & stick view")

        elif(tag=='Color by Chain'):
            self.comm+=('hide everything;')
            if 'protein' in objects:
	            self.comm+=('show cartoon, protein;')

            if 'dna' in objects:
                self.comm+=('show sticks , dna;')
	
	        if 'rna' in objects:
	            self.comm+=('show sticks, rna; show spheres, rna; set sphere_scale, 0.4, rna;')
	        
        	self.comm+=('color blue, chain A; color orange, chain B; color silver, chain C; color green, chain D; color yellow, chain E;' +
        	    'color purple, chain F; color grey, chain G; color brown, chain H; color slate, chain I; color brightorange, chain J;'+
        	    'color lightblue, chain K; color lightorange, chain L; color purple, chain M; color pink, chain N; color forest, chain O;' +
                'color firebrick, chain P; color paleyellow, chain Q; color purpleblue, chain R; color deepteal, chain S;'+
                'color deepolive, chain T; color pink, chain U; color salmon, chain V; color ruby, chain W; color wheat, chain X;' +
        	    'color lightmagenta, chain Y; color aquamarine, chain Z;')
            self.currentSelBox.setentry("set molecule to color by chain view")
    
        elif (tag=='Hetero Atoms'):
            if 'ligands' in objects:
                self.comm+='hide everything; '
   	    
                if 'protein' in objects:
	                self.comm+=('show cartoon, protein; set cartoon_transparency, 0.7, protein;')
	    
                if 'dna' in objects:
	                self.comm+=('show sticks, dna; set stick_transparency, 0.7, dna;')
	    
                if 'rna' in objects:
	                self.comm+=('show sticks, rna; show spheres, rna; set stick_transparency, 0.7, rna; set sphere_transparency, 0.7, rna;')

                self.comm+=('show spheres, ligands; set sphere_transparency, 0.1, ligands; show sticks, ligands around 6; '+
                    'set stick_radius, 0.3, ligands around 6; color orange, ligands;')
                
                self.comm+=('select interaction, ligands around 6; ')
                self.colorCpkMov(' & interaction')
                self.comm+=('delete interaction;') 

                self.currentSelBox.setentry("set molecule to hetero atoms view")
            else: 
                self.currentSelBox.setentry("Error", "There are no hetero atoms in this molecule.")
        
        elif (tag=='Surface'):
            self.comm+='hide everything; '
            self.colorCpkMov(' & all')
            
            if 'protein' in objects:
                self.comm+=('show surface, protein;') 

       	    if 'dna' in objects:
   	            self.comm+=('show sticks, dna; show surface, dna; set transparency, 0.7, dna;') 

      	    if 'rna' in objects:
   	            self.comm+=('show sticks, rna; show spheres, rna; set sphere_scale, 0.4, rna; show surface, rna; set transparency, 0.7, rna; ')

            if 'ligands' in objects:
	            self.comm+=('show spheres, ligands; color orange, ligands;')
            self.currentSelBox.setentry("set molecule to surface view")
    
        elif (tag=='Polarity'):
            self.comm+=('hide everything; show surface, hydrophobic; color red, hydrophobic; color blue, hydrophilic; show surface, hydrophilic; ')
        
            if 'ligands' in objects:
                self.comm+=('show spheres, ligands; color green, ligands; ')
        
            if 'dna' in objects:
                self.comm+=('show sticks, dna;' )
                self.colorCpkMov(' & dna')
        
            if 'rna' in objects:
                self.comm+=('show sticks, rna; show spheres, rna; set sphere_scale, 0.4, rna; ')
                self.colorCpkMov(' & rna')
            self.currentSelBox.setentry("set molecule to polarity view")

        elif (tag=='Aromatics'):
            self.comm+=('hide everything; select aromatics, resn phe+tyr+trp+his; color red, aromatics; show sticks, aromatics and (!name c+n+o); '+
                'set stick_radius, 0.4, all; deselect; delete aromatics; ')
            if 'protein' in objects:
    	        self.comm+=('show cartoon, protein; color aquamarine, protein; set cartoon_transparency, 0.6, protein; ')

    	    if 'dna' in objects:
    	        self.comm+=('show cartoon, dna; color aquamarine, dna; set cartoon_transparency, 0.6, dna; ')
    	    
            if 'rna' in objects:
    	        self.comm+=('show cartoon, rna; color aquamarine, rna; set cartoon_transparency, 0.6, rna; ')
            self.currentSelBox.setentry("set molecule to aromatic view")

        elif (tag=='Putty'):
            self.comm+='hide everything; '
            if 'protein' in objects:
       	        self.comm+=('show cartoon, protein; color red, ss h; color yellow, ss s; color cyan, ss l+\'\'; cartoon putty, protein; ')
    	
    	    if 'dna' in objects:
    	        self.comm+='show sticks, dna; '
    	        self.colorCpkMov(' & dna')
    	    
    	    if 'rna' in objects:
    	        self.comm+=('show sticks, rna; show spheres, rna; set sphere_scale, 0.4, rna;')
    	        self.colorCpkMov(' & rna')
            self.currentSelBox.setentry("set molecule to putty view")

        elif(tag=='DNA & RNA'):
            if ('dna' in objects) or ('rna' in objects):
                self.comm+='hide everything; '

    	        if 'dna' in objects:
    	            self.comm+='show sticks, dna; '
    	            self.colorCpkMov(' & dna')
    	    
    	        if 'rna' in objects:
    	            self.comm+='show sticks, rna; '
    	            self.colorCpkMov(' & rna')

                if 'protein' in objects:
	                self.comm+=('show cartoon, protein; color red, protein; set cartoon_transparency, 0.7, protein; ')

                if 'ligands' in objects:
	    	        self.comm+=('show spheres, ligands; set sphere_transparency, 0.7, ligands; set sphere_scale, 0.4, ligands;')
                
                self.currentSelBox.setentry("set molecule to DNA/RNA view")
            else:
                self.currentSelBox.setentry("no DNA or RNA present")
                
	
	        
            
        self.comm += "\n"
        
    
    #color CPK method  for the  movies tab
    def colorCpkMov(self, str):
        self.comm += ("color carbgray, elem C" + str+"; color red, elem O" + str +"; color white, elem H" + str +"; "+
                "color nitblue, elem N"+str + "; color sulfyellow, elem S" + str +"; color phosorange, elem P+Fe+Ba"+str+"; "+
                "color green, elem Cl+B"+str+"; color brown, elem Br+Zn+Cu+Ni"+str +"; color blue, elem Na"+str+"; "+
                "color forest, elem Mg"+str+"; color darkgray, elem Ca+Mn+Al+Ti+Cr+Ag"+str+"; color goldenrod, elem Au+F+Si"+str+"; "+
                "color ipurple, elem I"+str+"; color firebrick, elem Li"+str+"; color helpink, elem He"+str+";")

    #Edit colors in movie frames
    def colorMovSel(self, tag):
    	sel=self.sel
        tag = tag.lower()
        if tag != 'other' and tag != 'cpk':
            self.comm = "color "+tag+", "+sel+";\n"
            edit = "color " +tag+", "+sel
        elif tag=='cpk':
            self.colorCpkMov((' & '+sel))
            edit = "color cpk," +sel
        elif tag=='other':
            color=tkColorChooser.askcolor(parent=self.int, title="Selection Color Chooser")
            colorArray =[]
            if color[0]!= None:
                list=color[0]
                #print list
                for each in list:
                    z = (each/255.0)
                    val=repr(z)
                    colorArray.append(val)
                self.comm = ("set_color newcolor, ["+colorArray[0]+","+colorArray[1]+", "+colorArray[2]+"];\ncolor newcolor, "+sel+";\n")
                edit = ("set_color newcolor, ["+colorArray[0]+","+colorArray[1]+", "+colorArray[2]+"]"+
                "; color newcolor, "+sel+";")
            else:
                edit = "color red, "+sel
        else:
            edit = "color red, "+sel
        self.currentSelBox.setentry(edit)
     
    # Show individual representations
    def showMovRep(self, tag):
        sel = self.sel
        tag = tag.lower()
        if tag != 'water' and tag != 'ball and stick':
            self.comm = "show "+tag+", "+sel+";\n"
            edit = "show "+tag+", "+sel
        elif tag == 'water':
            self.comm = "show spheres, resn HOH;\n"
            edit = "show spheres, resn HOH"
        elif tag=='ball and stick':
            self.comm = "show spheres, "+sel+";\nshow sticks, "+sel+";\n"
            edit = "show spheres, "+sel+"  show sticks, "+sel
        self.currentSelBox.setentry(edit)
      	    
    # Hide individual representations
    def hideMovRep(self, tag):
    	sel = self.sel
        tag = tag.lower()
        if tag != 'water' and tag != 'ball and stick':
            self.comm = "hide "+tag+", "+sel+";\n"
            edit = "hide "+tag+", "+sel
        elif tag == 'water':
            self.comm = "hide spheres, resn HOH;\n"
            edit = "hide spheres, resn HOH"
        elif tag=='ball and stick':
            self.comm = "hide spheres, "+sel+";\n hide sticks, "+sel+";\n"
            edit = "hide spheres, "+sel+" hide sticks, "+sel
        self.currentSelBox.setentry(edit)

    #click the back button on the frame editor to return to the make movies tab
    def backToMov(self):
        self.editor.deactivate()

    #--------------------------------------#
    #					                   #
    #           Pre-Made MOVIE METHODS     #
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
    
        colors = ['blue','orange','silver','green','yellow','purple','brightorange','lightblue','lightorange',
       	            'pink','forest','firebrick','paleyellow','salmon','ruby','wheat','lightmagenta','nitblue']
        
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
        cmd.color('red','all')
    
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
    
	#ligan zoom movie  	
    def ligandZoom(self):
    	import tkMessageBox
    	cmd.mclear()
    	cmd.mset()
        cmd.mstop()
    	q=360
    	ids = self.p.idList
    	if len(ids)==0:
            tkMessageBox.showinfo("Ligand Zoom", "Sorry this PDB file contains no ligands and cannot be made into a movie")
    	else:
    	    objects = cmd.get_names('all')
    	    self.set_defaults()
    	    ids.sort()
    	    #calculate the number of frames
    	    numFrames = 600+(335*(len(ids)))
    	    cmd.deselect()
    	    cmd.do('bg_color white')
    	    cmd.cartoon('tube', 'all')
    	    cmd.mset('1', numFrames)
    	    #set the appearance for the first frame
    	    cmd.do('mdo 1: show cartoon, all; hide cartoon, resn a+t+c+g; show sticks, resn a+t+c+g;')
    	    cmd.reset()
    	    #rotate 180 on the x axis
    	    cmd.do('turn x, 180')
    	    cmd.orient()
    	    cmd.mview('store', '1')
    	    #rotate 180 on the y axis
    	    cmd.do('turn y, 180')
    	    cmd.mview('store', '120')
    	    cmd.mview('store', '150')
    	    cmd.do('turn y, 180')
    	    cmd.mview('store', '240')
    	    cmd.mview('store', '270')
    	    #zoom in on each bound ligand, then zoom out and move to the next one
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
     					 'slow down the playback of your movie significantly. '+
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
    #								                             #
    #                  PDB Abstract Getter                       #
    #		            					                     #					 
    # 								                             #
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
    #								                                #
    #                   GUI CREATION METHOD                         #
    #			      (INIT)			 	                        #
    #								                                #
    #								                                #
    #	             create and organize the interface              #          
    #								                                #
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
        self.parent = parent
        self.dialog = Pmw.Dialog(parent,
                                 buttons = ('Open','Fetch PDB','Clear','Help','Quit'),
                                 title = 'EZ-Viz Movie',command = self.execute)
        
     	interior = self.dialog.interior()
 	
        lab = Label(interior, text='EZ-Viz\nCreated By: Laura Grell, Chris Parkin, Len Slatest & Paul Craig\nVersion 2.0, 2007', 
                    background='#660000', foreground='white')
        lab.pack(expand=0, fill='x', padx=4, pady=0)
 	
        # Create the notebook to hold the tabs
        notebook = Pmw.NoteBook(interior)
        notebook.pack(fill='both', expand=1, padx=10, pady=10)

        #--------------------------------------#
        #			                           #
        #         WELCOME  TAB                 #
        #                                      #
        #--------------------------------------#
        page = notebook.add('Welcome')
        notebook.tab('Welcome').focus_set()
        canvas=Canvas(page)
        canvas.pack(fill='both', expand=1)
        canvas.create_image(0,0,image=splash,anchor=NW)
        
        #--------------------------------------#
        #			                           #
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

        #separate the images
        self.addSpace(interior, 0, 1)

        #chain coloring image
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
        #			                           #
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
	              
        
        
        #--------------------------------------#
        #			                           #
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
        #		       Make MOVIE TAB		       #
        #					                       #
        #------------------------------------------#
        # Add Movie tab to notebook
        page = notebook.add('  Make Movies  ')
        notebook.tab('  Make Movies  ').focus_set()
               
        group = Pmw.Group(page, tag_text="Make Movies")
        group.grid(row=0,column=0, padx=2, pady=2)
        interior = group.interior()

        self.new = Button(interior, text='New Movie', width=10, command=self.newMovie)
        self.new.grid(row=1, column=0, pady=10) 

        #add a button to write all the movie commands to a file - movie.py
        self.write = Button(interior, text='Save Movie', width=10, command=self.writeFile)
        self.write.grid(row=1, column=1, columnspan=2, pady=10, sticky='n') 

        self.loadMov = Button(interior, text='Load Movie', width=10, command=self.loadMovie)
        self.loadMov.grid(row=1, column=3, pady=10)
        
        #Create Group for Frame manipulation buttons
        frameGroup = Pmw.Group(interior, tag_text="Add Frames")
        frameGroup.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
        finterior = frameGroup.interior()

         #Current Frame Display
        self.currentFrameBox = Pmw.EntryField(finterior, labelpos='w', label_text='Current Frame:',
                            entry_width=8, value = 1, validate='numeric')
        self.currentFrameBox.grid(row=2, column=1, padx=0, pady=15, sticky='s')

        #feature radio buttons - allow user to select something to add to the movie
        self.feature = Pmw.RadioSelect(finterior, labelpos='w', labelmargin=0,
    				    buttontype='radiobutton',
    				    orient='vertical',
    				    label_text='Add a \nfeature')
        #If labels are changed they must also be changed in the setNumFrames method!!!
    	self.feature.add('Zoom In')
    	self.feature.add('Zoom Out')
    	self.feature.add('Rotate Y 180')
    	self.feature.add('Rotate X 180')
        self.feature.add('Rotate Z 180')
    	self.feature.add('Hold on View')
        self.feature.invoke(5)
    	self.feature.grid(row=0,column=0, rowspan=3, padx=0, pady=0)
        	
    	#select the number of frames for a given action
        self.frames = Pmw.OptionMenu(finterior,labelpos = 'w', label_text = 'Frames:',
                        items = ('1','10','25','50','100','200'), menubutton_width = 2)
        self.frames.grid(row=0,column=2, padx=0,pady=0, sticky='n,e,s')

        #ligands selector drop down - allows user to select a ligand to zoom in on
        #create the option menu
        self.ligands = Pmw.OptionMenu(finterior, labelpos='w', label_text = "Zoom In\nOn:", items=(''), menubutton_width = 12,)
        #get the menubutton from the option menu
        self.ligandsmb = self.ligands.component('menubutton')
        #create the variable to be updated on the menubutton when an object in the menu is clicked
        self.ligVar = StringVar()
        self.ligVar.set("Click to choose")
        #configure the menu button to be raised and have its text changed when self.ligVar is changed
        self.ligandsmb.config(text="Ligands & Chains", textvariable=self.ligVar, relief=RAISED)
        #create a menu for the menu button and set it as the menu buttons menu
        self.object_menu = Menu(self.ligandsmb, tearoff=0)
        self.ligandsmb["menu"] = self.object_menu
        #create menus for chains and ligands
        self.chainmenu = Menu(self.ligandsmb, tearoff=0)
        self.ligandmenu = Menu(self.ligandsmb, tearoff=0)
        self.activemenu = Menu(self.ligandsmb, tearoff=0)
        #add the chain, active site, and ligand menus to the menubutton menu
        self.object_menu.insert_cascade(0, label="Active Sites", menu=self.activemenu)
        self.object_menu.insert_cascade(1, label="Ligands", menu=self.ligandmenu)
        self.object_menu.insert_cascade(2, label="Chains", menu=self.chainmenu)
        self.ligands.grid(row=0,column=1,pady=10, sticky='n')

        #add button to add sequence of frames
        self.addSeq = Button(finterior, text='Add Frames', width=15, command=self.addFrames)
        self.addSeq.grid(row=1, column=2, columnspan=2, pady=5, padx=10, sticky='N')

        self.undo = Button(finterior, text='Undo', width=15, command=self.undoAction)
        self.undo.grid(row=2, column=2, columnspan=2, sticky='N')

        #labels to display the loaded movie file name
        Label(interior, text="Loaded Movie:").grid(row=2, column=0, sticky='ns')
        self.fileMovie=StringVar()
        self.fileMovie.set("")
        Label(interior, textvariable=self.fileMovie, font=("arial",12, "bold")).grid(row=2, column=1, sticky='nsw')
    
        #button to open the edit frames tab
        self.edit = Button(interior, text='Edit Frames', width=15, command=self.showEditor)
        self.edit.grid(row=2, column=3, sticky='S')

        #commands that will be issued to generate the movie
        self.movOutput = Pmw.ScrolledText(interior, usehullsize = 1, hull_width = 250,
                hull_height = 100, text_wrap= WORD)
        self.movOutput.grid(row=4, column=0, rowspan=3, columnspan=3, padx=12, pady=15)     

        #add button to preview the movie
        self.prev = Button(interior, text='Preview Movie', width=15, height=2, command=self.preview, bg='yellow')
        self.prev.grid(row=5, column=3, pady=10, padx=10, sticky='W')

        #add button to interpolate the frames together
        self.make = Button(interior, text='Make Movie', width=15, height=2, command=self.interpolate, bg='green')              
        self.make.grid(row=6, column=3, pady=10, padx=10, sticky='W')

        #set the initial movie conditions- 100 frames, current frame is 1
        self.initial()
        self.count = 1
        self.movieMade = 0
        self.framesAdded = 0
        self.framesRemoved = 0
        self.loadedMovie = 0
    #--------------------------------------#
    #					                   #
    #           Pre MOVIE Tab              #
    #                                      #
    #--------------------------------------#
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
        
        #Radio Buttons for Frame Speed
        self.speed =Pmw.RadioSelect(interior, labelpos='w', labelmargin=0,
    				    buttontype='radiobutton',
    				    orient='horizontal',
    				    label_text='Frame Speed(FPS)',
                        command = self.frame_speed)
        #If labels are changed they must also be changed in the setNumFrames method!!!
    	self.speed.add('Max')
        self.speed.add('30')
        self.speed.add('15')
        self.speed.add('5')
        self.speed.add('1')
        self.speed.add('0.3')
        self.speed.grid(row=5, column=0, columnspan=4)
        self.speed.invoke('15')
        
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
        #			                           #
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
    	self.info =Pmw.ScrolledText(page, usehullsize=1, hull_height=100, hull_width=250 )
        self.info.grid(row=8, column=1, columnspan=2, sticky='nw',padx=5, pady=0)
        
        #checks to see if there is a file loaded in the viewer prior to the GUI being opened
        self.fileLoaded = ' '
        loadedPDB=cmd.get_names()
        if loadedPDB!=[]:
        	self.fileLoaded = loadedPDB[0]
        	self.getPdb()
        self.fileLoaded = ' '
	
        #--------------------------------------#
        #			                           #
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
        #			                           #
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
        #			                           #
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
        'In 2007, the Ez-Viz interface received a major upgrade with the addition of the Make Movies tab. '+
        'Laura Grell developed the new tab so that both old and new users can easily create their own movies in PyMOL. '+
        'This project was completed at R.I.T. and fulfilled the thesis requirement for the Master of Science degree '+
        'in Bioinformatics.\n\n'+
        'For questions and/or comments regarding this interface please contact Dr. Paul Craig at paul.craig@rit.edu.',
        wraplength=275, justify=LEFT)
        aboutText.grid(row=0, column=0, sticky=NW)
 	    
        notebook.setnaturalsize()
        #-------------------------------------#
        #                                     #
        #         Frame Editor Window         #
        #           keep it hidden            #
        #-------------------------------------#
      
        self.frameString = ""

        self.editor = Pmw.MegaToplevel(self.dialog.interior())
        self.editor.title("Frame Editor")

        #group for selection selection options
        self.editGroup = Pmw.Group(self.editor.interior(), tag_text='Edit Frames')
    	self.editGroup.grid(row=0, column=0, rowspan=8, columnspan=5, padx=1, pady=0, sticky='NW')

        #add a scrollbar to scroll through the frames
        self.slider = Scale(self.editGroup.interior(), orient='horizontal', from_=1, length=500, 
                                label='Move to Frame', command=self.moveFrame)
        self.slider.grid(row=8, column=0, columnspan=5, padx=5, sticky='w')

        self.back = Button(self.editGroup.interior(), text='Close Frame\nEditor', width=15, command=self.backToMov)
        self.back.grid(row=8, column=4, sticky='ns', pady=5)

        #ligand selector drop down - allows user to select a ligand/active site to alter
        #create the option menu
        self.ligSelector = Pmw.OptionMenu(self.editGroup.interior(), labelpos='w', label_text = "Select:", items=(''), menubutton_width = 12,)
        #get the menubutton from the option menu
        self.sButton = self.ligSelector.component('menubutton')
        #create the variable to be updated on the menubutton when an object in the menu is clicked
        self.selVar = StringVar()
        self.selVar.set("All")
        #configure the menu button to be raised and have its text changed when self.ligVar is changed
        self.sButton.config(text="Select:", textvariable=self.selVar, relief=RAISED)
        #create a menu for the menu button and set it as the menu button's menu
        self.feature_menu = Menu(self.sButton, tearoff=0)
        self.sButton["menu"] = self.feature_menu
        #create menus for chains and ligands
        self.frameligandmenu = Menu(self.sButton, tearoff=0)
        self.frameactivemenu = Menu(self.sButton, tearoff=0)
        self.framechainmenu = Menu(self.sButton, tearoff=0)
        self.frameothermenu = Menu(self.sButton, tearoff=0)
        #add the chain, active site, and ligand menus to the menubutton menu
        self.feature_menu.insert_cascade(0, label="Active Sites", menu=self.frameactivemenu)
        self.feature_menu.insert_cascade(1, label="Ligands", menu=self.frameligandmenu)
        self.feature_menu.insert_cascade(2, label="Chains", menu=self.framechainmenu)
        self.feature_menu.insert_cascade(3, label="Other", menu=self.frameothermenu)
        self.ligSelector.grid(row=0,column=0, rowspan=3, pady=10, padx=5, sticky='w,n,e,s')

        self.around =Pmw.RadioSelect(self.editGroup.interior(), labelmargin=0, buttontype='radiobutton',
    				    orient='vertical', labelpos='n', label_text="Around Ligands", pady=0, command=self.setAround)
        #If labels are changed they must also be changed in the setNumFrames method!!!
    	self.around.add('None')
        self.around.add('1 '+u'\u212B')
        self.around.add('3 '+u'\u212B')
        self.around.add('5 '+u'\u212B')
        self.around.grid(row=0, column=1, rowspan=3)

        #create string to hold around value 
        self.aroundString = ""
        
        #group for selection selection options
        opGroup = Pmw.Group(self.editGroup.interior(), tag_text='Options')
    	opGroup.grid(row=0, column=2, rowspan=3, columnspan=3, padx=1, pady=0, sticky='NW')
    	interior = opGroup.interior()

        #color menu
        self.colors = Pmw.OptionMenu(interior,labelpos = 'w', label_text = 'Color:',
                items = ('Red','Green','Blue','Orange','Violet','Yellow','CPK','Other'),
                menubutton_width = 7, command = self.colorMovSel)
        self.colors.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky='n,s,e,w')

        #show and hide menus
        self.viewFrameRep = Pmw.OptionMenu(interior, labelpos='w', label_text = 'Show:',
                items = ('Lines', 'Sticks', 'Ribbon','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water', 'Everything'),
                menubutton_width=10, command=self.showMovRep)
    	self.viewFrameRep.grid(row=0,column=1,padx=5,pady=5)
 	
        self.hideFrameRep = Pmw.OptionMenu(interior, labelpos='w', label_text = 'Hide:',
    		    items = ('Lines', 'Sticks', 'Ribbon','Cartoon','Dots','Spheres','Mesh','Surface','Ball and Stick','Water','Everything'),
    		    menubutton_width=10, command=self.hideMovRep)
    	self.hideFrameRep.grid(row=1,column=1,padx=5,pady=5, sticky='S')

        #string variable used to update the total frames on the slidebar
        self.slideNum = StringVar()
        self.slideNum.trace('w', self.slideUpdater)
        self.slideNum.set('100')

        #Dropdown with Presets
        self.presets = Pmw.OptionMenu(interior, labelpos='w', label_text='Presets:', menubutton_width=8, 
            items =('Default', ' '), 
                command=self.movPresets)
        self.presets.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        #Box to display current selection
        self.currentSelBox = Pmw.EntryField(self.editGroup.interior(), label_text="Current Edit:", labelpos='wsn')
        self.currentSelBox.component('entry').config(state="readonly", width=40)
        self.currentSelBox.grid(row=4, column=0, columnspan=2, sticky='nsw')

        #button to accept single change to frame
        Button(self.editGroup.interior(), text='Accept', width=15, command=self.accept).grid(row=5, column=0, columnspan=2, sticky='n')
        #button to click when frame is ready to be added to movie
        Button(self.editGroup.interior(), text='Undo', width=15, command=self.undoEdit).grid(row=7, column=3, sticky='n', pady=5)

        self.label = StringVar()
        label = "Frame 1"
        frameLabel = Label(self.editGroup.interior(), textvariable=self.label, font='arial, 12').grid(row=3, column=3, sticky='nw')

        #text box to display all changes to current frame
        self.frameEdits =Pmw.ScrolledText(self.editGroup.interior(), usehullsize=1, hull_height=100, hull_width=300)
        self.frameEdits.grid(row=4, column=3, columnspan=3, rowspan=3, sticky='nw')

        #button to accept single change to frame
        Button(self.editGroup.interior(), text='Frame Complete', width=15, command=self.setFrame).grid(row=7, column=4, sticky='nw', pady=5)

        #hide the window initially - until user clicks 'Add Frames' button   
        self.editor.withdraw()
        #do not destroy the window when 'X' is hit - just deactiavte it
        #if destroyed - will need to be created again and will have to restart Ez-Viz
        self.editor.protocol('WM_DELETE_WINDOW', self.editor.deactivate()) #deactivate on close
        
        #--------------------------------------#
        #      		                           #
        #   HANDLE BUTTONS AT BOTTOM OF GUI    #
        #    (open, fetch.., help, exit)       #
        #--------------------------------------#         
    def execute(self, result):
        import tkFileDialog
        import tkMessageBox
        names = cmd.get_names()
        answer = 1
        if result == 'Open':
            if (len(names)>0):
                answer = tkMessageBox.askyesno("Mulitple PDB Files", "Loading a new PDB file will clear the existing molecule. " +
                    "Do you wish to continue?")
            if (answer==1): 
                file=tkFileDialog.askopenfilename(initialdir='C:/Documents and Settings/Administrator/My Documents/')
                cmd.reinitialize()
                self.movOutput.clear()
                self.initial()
                print file
                if file:
                    cmd.load(file)
                    self.pdbCode = file
                    self.p=PDBParser()
                    self.p.readFile(file)
                    self.update(self.p)
                    self.std_view()
                    #clear the movie cache
                    cmd.mdump()
        elif result == 'Help':
            self.help()
        elif result == 'Fetch PDB':
            if (len(names)>0):
                answer = tkMessageBox.askyesno("Mulitple PDB Files", "Loading a new PDB file will clear the existing molecule. " +
                    "Do you wish to continue?")
            if answer==1:
                cmd.reinitialize()
                self.movOutput.clear()
                self.initial()
                self.getPdb()
                self.std_view()
                #clear the movie cache
                cmd.mdump()
        elif result == 'Clear':
            cmd.reinitialize()
            #clear the movie output window
            self.movOutput.clear()
            self.currentFrame = 1
            self.currentFrameBox.setvalue(self.currentFrame)
            self.movieMade = 0
            self.initial()
            self.fileMovie.set("")
        else:
            #was withdraw - changed to destroy 3/31/07
            self.dialog.destroy()
            #clear the movie cache
            cmd.mdump()

    # Update all Labels on Information Tab  
    def update(self, p):
    	#chainlist contains the pre-existing options for selections - All, ligands, not selected, hydrophobic, hydrophillic
    	chainList=['All','Not Selected','Hydrophobic','Hydrophilic']
        self.cmdType = 'PyMOL'
        #Update all the fields on the information tab
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
        heteroMovString =""
    	if (len(p.hetero)!=0):
            chainList.append("Ligands")
            hetero=string.split(p.hetero, sep=', ')
            hetero=string.join(hetero, sep='+')
            #create the ligands object
            cmd.create('ligands', '(resn '+string.strip(hetero)+')')
            
            #Create a separate string of hetero atoms to display on the movie tab
            heteroMovString = string.split(p.heteroMov, sep=', ')

        #delete the previous ligands menus
        self.object_menu.delete(1)
        self.feature_menu.delete(1)
        #create new ligands menus
        self.ligandmenu = Menu(self.ligandsmb, tearoff=0)
        self.frameligandmenu = Menu(self.sButton, tearoff=0)
        #insert the new menu into the dropdown
        self.object_menu.insert_cascade(1, label="Ligands", menu=self.ligandmenu)
        self.feature_menu.insert_cascade(1, label="Ligands", menu=self.frameligandmenu)
        #add all the ligands for this molecule to the menu 
        for lig in heteroMovString:
            self.ligandmenu.add_command(label=lig, command=lambda i=lig: self.ligSet(i))
            self.frameligandmenu.add_command(label=lig, command=lambda i=lig: self.selSet(i))

        #add the active sites to the drop down
        self.enableAS()
        
        #get the chain names and store the in items - then sort them	
        items=p.chains.keys()
        items.sort()
        #append chains to the heteroMovString and then update the list on the make movies tab
        self.object_menu.delete(2)
        self.feature_menu.delete(2)
        self.chainmenu = Menu(self.ligandsmb, tearoff=0)
        self.framechainmenu = Menu(self.sButton, tearoff=0)
        self.object_menu.insert_cascade(2, label="Chains", menu=self.chainmenu)
        self.feature_menu.insert_cascade(2, label="Chains", menu=self.framechainmenu)
        for i in items:
            if i != " ":
                #set the chain drop down on the make movies tab
                self.chainmenu.add_command(label=i, command=lambda i=i: self.ligSet(i))
                self.framechainmenu.add_command(label=i, command=lambda i=i: self.selSet(i))

	    #put the chain names in the drop down for chains on the information tab
    	self.chain.setitems(items)
    	items2=[]
    	prt=''
    	dna=''
    	rna=''
    	self.helixList = p.helices
    	self.init_color()
    	true=0
	    #determine what type the chains are: protein or nucleic acid
    	for id in items:
    		type =self.seqGetter(id)
    		if type=='Protein':
    			prt=prt+id
    			true=1
    		elif type=='DNA':
    			dna=dna+id
    		elif type=='RNA':
    			rna=rna+id 
		    #append the chain to the items2 list to be concatenated to the existing chainlist
            #fixed 3/31/07 - space removed from id to fix chain deselection error
    		id = "Chain"+id
    		items2.append(id)
    	prt =string.join(prt, sep='+')
    	dna =string.join(dna, sep='+')
    	rna =string.join(rna, sep='+')
	    #create a protein or nucleic acid object depending that includes all chains of that type
	    #append those found to chainlist to be added to the drop down on the commands tab
    	if prt !=' 'and prt !='':
    		cmd.create('protein', 'chain '+prt)
    		chainList.append("Protein")
    	if dna != '':
    		cmd.create('dna', 'chain '+dna)
    		chainList.append("DNA")
    	if rna != '':
    		cmd.create('rna', 'chain '+rna)
    		chainList.append("RNA")
   	#---------------ADDED 8/8/05------------------------#
    	if (prt==' ' or prt=='') and true==1:
    		cmd.create('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    		chainList.append("Protein")
    	#------------------------------------------------#
    	cmd.do('deselect')

        self.feature_menu.delete(3)
        self.frameothermenu = Menu(self.sButton, tearoff=0)
        self.feature_menu.insert_cascade(3, label="Other", menu=self.frameothermenu)

        #update the select drop down on the frame editor tab
        for item in chainList:
            self.frameothermenu.insert_command(0, label=item, command=lambda i=item: self.selSet(i))

	#update chain list to include everything it already has and all the chain names
    	chainList = chainList+items2

    #THIS FUNCTIONALITY HAS BEEN GIVEN TO THE MENU UPDATER METHOD 3/31/07
    #BY SETTING THE StringVar "dropDowns" BELOW - THE SELECTION LIST IS AUTOMATICALLY UPDATED
	#update the drop down menu on the commands tab
    	self.selection.setitems(chainList)
	#update the drop down menu on the advanced tab
    	self.advancedSelection.setitems(chainList)

    #Display the molecule name on the Info page
    	if p.name=='':
    		self.name.set("None Given")
    	else:
    		self.name.set(p.name)
    
	cmd.create('hydrophilic','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
	cmd.create('hydrophobic','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')


# //PyMOL_EZ.py     	
     
     	
  	
       
