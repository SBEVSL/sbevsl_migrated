from Tkinter import *
import Pmw
import pymol
from pymol import cmd
import tkColorChooser
import re
import string
from pymol import cmd
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import string
import os
from tkFileDialog import askopenfilename, asksaveasfilename
import re
import urllib2
import StringIO
import gzip
import time
import types
import os
from pymol import util
import pickle
import random
import linecache
import Pmw
import urllib
from pymol import selector
from pymol import cmd
from pymol import _cmd
from cmd import*
try:
  PYMOL_PATH=os.environ['PYMOL_PATH']
except KeyError:
  PYMOL_PATH='./'

Pmw.initialise()


#---------------------------------------------------------------
# Link our GUI to PyMOL
#---------------------------------------------------------------
def __init__(self):
  self.menuBar.addmenuitem('Plugin', 'command',
                           'Easy GUI',
                           label = 'ProMOL 3.03',
                           command = lambda s=self : PGUI(s))

#-----------------------Version 1-------------------------------#

#--------------------------------------------------------------------#
#						                     #
#                       PDBParser                                    #
#					                             #
#					                             #
#					                             #
#       Parse PDB files and pull out the useful information          #
#					                             #
#--------------------------------------------------------------------#
universalPDB = ''
class PDBParser:
	#Most of this not called anymore, not enough time to sift through
        #and delete though
    
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
 		
 		
#------------------------------------------------------------------#
#						#
#                     Helix Class                                                                   #
#						#
#						#
#						#
#              Helix Objects (used in movies)                                      #
#						#
#------------------------------------------------------------------#
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
#					              #
#                     Chime Converter                                                   #
#					              #
#					              #
#					              #
#              Handle the entry of Chime commands                   #
#					              #
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
    #        Chime Conversion Methods       #
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
      try:
       	if self.argsLength > 1:
     	    pymSelect = 'PyMOL: select '+self.selections[self.args[1]]+'\n\n'
     	    self.results.appendtext(pymSelect)
     	    cmd.select(self.selections[self.args[1]])
    	else:
     	    self.results.appendtext('Usage: select [selection]')
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Error', 'That is not a supported command')
   	    
    # 'individual command' conversions
    def convert_individual(self):
        pymShow = 'PyMOL: '+self.individuals[self.command]+'\n\n' 
        cmd.do(self.individuals[self.command])
        self.results.appendtext(pymShow)
    
#---------------------------------------------------------------#
#					                        #
#                           GUI Class                           #
#					                        #
#						                #
#					                        #
#	           The look of the interface	                #
#					                        #
#---------------------------------------------------------------#
class PGUI:
    
    global splash
    global TACOBUENO
    global GLYTACO
    global ASPTACO
    global PROTACO
    global METTACO
    global PHETACO
    global ASNTACO
    global ARGTACO
    global SERTACO
    global CYSTACO
    global THRTACO
    global GLUTACO
    global TRPTACO
    global GLNTACO
    global VALTACO
    global HISTACO
    global ILETACO
    global LEUTACO
    global LYSTACO
    global TYRTACO
    global ALAGUM
    global ARGGUM
    global ASNGUM
    global ASPGUM
    global CYSGUM
    global GLUGUM
    global GLNGUM
    global GLYGUM
    global HISGUM
    global ILEGUM
    global LEUGUM
    global LYSGUM
    global METGUM
    global PHEGUM
    global PROGUM
    global SERGUM
    global THRGUM
    global TRPGUM
    global TYRGUM
    global VALGUM
    global script
    

    
    #-----Brett's and Charlie's amino acid images--------- 
    #3D Reference Image
    TACOBUENO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/TACOBUENO.GIF")
    GLYTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLYTACO.GIF")
    ASPTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ASPTACO.GIF")
    PROTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/PROTACO.GIF")
    METTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/METTACO.GIF")
    PHETACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/PHETACO.GIF")
    ASNTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ASNTACO.GIF")
    ARGTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ARGTACO.GIF")
    SERTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/SERTACO.GIF")
    CYSTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/CYSTACO.GIF")
    THRTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/THRTACO.GIF")
    GLUTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLUTACO.GIF")
    TRPTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/TRPTACO.GIF")
    GLNTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLNTACO.GIF")
    VALTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/VALTACO.GIF")
    HISTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/HISTACO.GIF")
    ILETACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ILETACO.GIF")
    LEUTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/LEUTACO.GIF")
    LYSTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/LYSTACO.GIF")
    TYRTACO = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/TYRTACO.GIF")

    #2D Reference Image
    ALAGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ALAGUM.GIF")
    GLYGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLYGUM.GIF")
    ASPGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ASPGUM.GIF")
    PROGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/PROGUM.GIF")
    METGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/METGUM.GIF")
    PHEGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/PHEGUM.GIF")
    ASNGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ASNGUM.GIF")
    ARGGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ARGGUM.GIF")
    SERGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/SERGUM.GIF")
    CYSGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/CYSGUM.GIF")
    THRGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/THRGUM.GIF")
    GLUGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLUGUM.GIF")
    TRPGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/TRPGUM.GIF")
    GLNGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/GLNGUM.GIF")
    VALGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/VALGUM.GIF")
    HISGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/HISGUM.GIF")
    ILEGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/ILEGUM.GIF")
    LEUGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/LEUGUM.GIF")
    LYSGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/LYSGUM.GIF")
    TYRGUM = PhotoImage(file="./modules/pmg_tk/startup/AminoPics/TYRGUM.GIF")
        
    # Welcome tab image
    splash = PhotoImage(file="./modules/pmg_tk/startup/splashmol.GIF")

    
    #--------------------------------------#
    #			                   #
    #         PRESETS METHODS              #
    #                                      #
    #--------------------------------------#
    
    #All initially Larua's and Chris's code, but modified by Brett and Charlie
    #none of the preset views worked when a PDB file was loaded
    #through Pymol, all had to be loaded through EZViz for parsing
    #reasons, so all presets were modified, and some completely redone
    #to allow for a user to load it from wherever they want, whenever they
    #want, and still have the view work.  Only functionality loss was distinguishin between DNA and RNA

    #---------------------Version 2-------------------------#
    
    script = 0
#     def write_script(self, tag):
#         if tag == 'Off':
#             script ='0'
           
#         if tag=='On': #write a script
#             try:
#                 script = '1'
#                 import tkFileDialog
#                 self.Q = tkFileDialog.asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Scripts")
#                 cmd.do('log_open %s,a' %(self.Q))            
#                 self.f=open(self.Q, 'w')
              
#             except:
#                pass

#     def set_defaults(self):
#         cmd.hide('everything','all')
#         cmd.set('transparency','0.0','all')
#         cmd.set('cartoon_transparency','0.0','all')
#         cmd.set('transparency','0','all')
#         cmd.set('sphere_transparency','0.0','all')
#         cmd.set('stick_transparency','0.0','all')
#         cmd.set('sphere_scale','0.7','all')
#         cmd.cartoon('automatic', 'all')
#         cmd.set('stick_radius','0.2','all')
#         if script == '1':
#                 f.write('''cmd.hide("everything","all") 
# cmd.set("transparency","0.0","all")
# cmd.set("cartoon_transparency","0.0","all")
# cmd.set("transparency","0","all")
# cmd.set("sphere_transparency","0.0","all")
# cmd.set("stick_transparency","0.0","all")
# cmd.set("sphere_scale","0.7","all")
# cmd.cartoon("automatic", "all")
# cmd.set("stick_radius","0.2","all")\n''')
#         delcrea()
#     cmd.extend('set_defaults',set_defaults)
    
   # emphasize DNA
    def show_dna_rna(*args):
        import tkMessageBox
        points = 0
        delcrea()
        self.update(self.p)
        objects = cmd.get_names('all')
        checkitforthese()
        try:
          cmd.set('cartoon_ring_mode' ,'1')
          if script == '1':
              f.write('''cmd.set('cartoon_ring_mode' ,'1')\n''')
          if 'nucleic_acid' in objects:
              set_defaults()
              if 'protein' in objects:
                  cmd.show('cartoon','protein')
                  cmd.color('gray60','protein')
                  if script == '1':
                      f.write('''cmd.show('cartoon','protein')
cmd.color('gray60','protein')\n''')
              if 'ligands' in objects:
                  cmd.show('spheres','ligands')
                  cmd.set('sphere_transparency','0.4','ligands')
                  cmd.set('sphere_scale','0.4','ligands')
                  cmd.color('orange', 'ligands')
                  if script == '1':
                      f.write('''cmd.show('spheres','ligands')
cmd.set('sphere_transparency','0.4','ligands')
cmd.set('sphere_scale','0.4','ligands')
cmd.color('orange', 'ligands')\n''')
              if 'nucleic_acid' in objects:
                  cmd.show('cartoon', 'nucleic_acid')
                  cmd.color('lightblue','resn a')
                  cmd.color('orange','resn c')
                  cmd.color('salmon','resn g')
                  cmd.color('palegreen','resn t')
                  cmd.color('paleyellow', 'resn u')
                  if script == '1':
                      f.write('''cmd.show('cartoon', 'nucleic_acid')
cmd.color('lightblue','resn a')
cmd.color('orange','resn c')
cmd.color('salmon','resn g')
cmd.color('palegreen','resn t')
cmd.color('paleyellow', 'resn u')\n''')
                  points = points + 3
          if points == 3:
	        tkMessageBox.showinfo('Nucleic Acid Key','Adenine = light blue\nCytosine = orange\nGuanine = salmon red\nThymine = light green\nUracil = light yellow')

          else:
                tkMessageBox.showinfo("Error", "There is no DNA or RNA in this molecule.")
        except:              
          if 'nucleic_acid' in objects:
              set_defaults()
              if 'protein' in objects:
                  cmd.show('cartoon','protein')
                  cmd.color('gray60','protein')
                  if script == '1':
                      f.write('''cmd.show('cartoon','protein')
cmd.color('gray60','protein')\n''')
              if 'ligands' in objects:
                  cmd.show('spheres','ligands')
                  cmd.set('sphere_transparency','0.4','ligands')
                  cmd.set('sphere_scale','0.4','ligands')
                  cmd.color('orange', 'ligands')
                  if script == '1':
                      f.write('''cmd.show('spheres','ligands')
cmd.set('sphere_transparency','0.4','ligands')
cmd.set('sphere_scale','0.4','ligands')
cmd.color('orange', 'ligands')\n''')
              if 'nucleic_acid' in objects:
                  cmd.show('cartoon', 'nucleic_acid')
                  cmd.color('lightblue','resn a')
                  cmd.color('orange','resn c')
                  cmd.color('salmon','resn g')
                  cmd.color('palegreen','resn t')
                  cmd.color('paleyellow', 'resn u')
                  if script == '1':
                      f.write('''cmd.show('cartoon', 'nucleic_acid')
cmd.color('lightblue','resn a')
cmd.color('orange','resn c')
cmd.color('salmon','resn g')
cmd.color('palegreen','resn t')
cmd.color('paleyellow', 'resn u')\n''')
                  points = points + 3
          if points == 3:
	        tkMessageBox.showinfo('Nucleic Acid Key','Adenine = light blue\nCytosine = orange\nGuanine = salmon red\nThymine = light green\nUracil = light yellow')

          else:
                tkMessageBox.showinfo("Error", "There is no DNA or RNA in this molecule.")
    cmd.extend('show_dna_rna',show_dna_rna)
    
  
    # default view
    def std_view(self):
      try:
        self.update(self.p)
        checkitforthese()
        set_defaults()
        delcrea()
        self.populate()
        cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.color("red", "ss h")
        cmd.color("yellow", "ss s")
        cmd.color("cyan", "ss l+\'\'")
        cmd.set('cartoon_ring_mode' ,'1')	
        cmd.show('spheres','het')
        if script == '1':
            f.write('''cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.color("red", "ss h")
cmd.color("yellow", "ss s")
cmd.color("cyan", "ss l+\'\'")
cmd.set('cartoon_ring_mode' ,'1')	
cmd.show('spheres','het')\n''')
        cpkligands()
        cmd.show('cartoon', 'resn a+t+g+c+u')
        cmd.color('limegreen','resn a+t+g+c+u')
        if script == '1':
            f.write('''cmd.show('cartoon', 'resn a+t+g+c+u')
cmd.color('limegreen','resn a+t+g+c+u')\n''')
      except:
        self.update(self.p)
        checkitforthese()
        set_defaults()
        delcrea()
        self.populate()
        cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.color("red", "ss h")
        cmd.color("yellow", "ss s")
        cmd.color("cyan", "ss l+\'\'")	
        cmd.show('spheres','het')
        if script=='1':
            f.write('''cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.color("red", "ss h")
cmd.color("yellow", "ss s")
cmd.color("cyan", "ss l+\'\'")	
cmd.show('spheres','het')''')
        cpkligands()
        cmd.show('cartoon', 'resn a+t+g+c+u')
        cmd.color('limegreen','resn a+t+g+c+u')
        if script =='1':
            f.write('''cmd.show('cartoon', 'resn a+t+g+c+u')
cmd.color('limegreen','resn a+t+g+c+u')\n''')

    # show hetero atoms    
    def show_hetero(self):
        try:
            import tkMessageBox
            delcrea()
            cmd.remove('resn HOH')
            if script=='1':
                f.write('''cmd.remove('resn HOH')\n''')
                self.update(self.p)
                objects = cmd.get_names('all')
                if script=='1':
                    f.write('''objects = cmd.get_names('all')\n''')
                checkitforthese()
            if 'ligands' in objects:
                set_defaults()
            if 'protein' in objects:
                cmd.show('cartoon', 'protein')
                cmd.set('cartoon_transparency','0.7','protein')
                if script=='1':
                    f.write('''cmd.show('cartoon', 'protein')
cmd.set('cartoon_transparency','0.7','protein')\n''')
            if 'nucleic_acid' in objects:
                cmd.set('cartoon_ring_mode', '1')
                cmd.show('cartoon','nucleic_acid')
                cmd.set('cartoon_transparency','0.7','nucleic_acid')
                cmd.color('cyan', 'nucleic_acid')
                if script=='1':
                    f.write('''cmd.set('cartoon_ring_mode', '1')
cmd.show('cartoon','nucleic_acid')
cmd.set('cartoon_transparency','0.7','nucleic_acid')
cmd.color('cyan', 'nucleic_acid')\n''')
                cmd.show('spheres','ligands')
                cmd.set('sphere_transparency','0.1','ligands')
                cmd.show("sticks", "ligands around 6'")
                cmd.set('stick_radius','0.3','ligands around 6')
                cmd.color('orange','ligands')
                cmd.select("interaction","ligands around 6'")
                if script=='1':
                    f.write('''cmd.show('spheres','ligands')
cmd.set('sphere_transparency','0.1','ligands')
cmd.show("sticks", "ligands around 6'")
cmd.set('stick_radius','0.3','ligands around 6')
cmd.color('orange','ligands')
cmd.select("interaction","ligands around 6'")\n''')
                cpkinteraction()
                cmd.set('stick_transparency', '0.1', 'interaction')
                cmd.disable('interaction')
                if script=='1':
                    f.write('''cmd.set('stick_transparency', '0.1', 'interaction')
cmd.disable('interaction')\n''')
            else:
                tkMessageBox.showinfo("Error", "There are no hetero atoms in this molecule.")
        except:
            import tkMessageBox
            delcrea()
            cmd.remove('resn HOH')
            if script =='1':
                f.write('''cmd.remove('resn HOH')\n''')
            self.update(self.p)
            objects = cmd.get_names('all')
            if script=='1':
                f.write('''objects = cmd.get_names('all')\n''')
            checkitforthese()
	if 'ligands' in objects:
   	    set_defaults()
	    if 'protein' in objects:
	        cmd.show('cartoon', 'protein')
	        cmd.set('cartoon_transparency','0.7','protein')
	        if script=='1':
                                f.write('''cmd.show('cartoon', 'protein')
cmd.set('cartoon_transparency','0.7','protein')\n''')
	    if 'nucleic_acid' in objects:
	        cmd.show('cartoon','nucleic_acid')
	        cmd.set('cartoon_transparency','0.7','nucleic_acid')
	        cmd.color('cyan', 'nucleic_acid')
	        if script=='1':
                                f.write('''cmd.show('cartoon','nucleic_acid')
cmd.set('cartoon_transparency','0.7','nucleic_acid')
cmd.color('cyan', 'nucleic_acid')\n''')
	    cmd.show('spheres','ligands')
	    cmd.set('sphere_transparency','0.1','ligands')
	    cmd.show("sticks", "ligands around 6'")
	    cmd.set('stick_radius','0.3','ligands around 6')
	    cmd.color('orange','ligands')
	    cmd.select("interaction","ligands around 6'")
	    if script=='1':
                            f.write('''cmd.show('spheres','ligands')
cmd.set('sphere_transparency','0.1','ligands')
cmd.show("sticks", "ligands around 6'")
cmd.set('stick_radius','0.3','ligands around 6')
cmd.color('orange','ligands')
cmd.select("interaction","ligands around 6'")\n''')
	    cpkinteraction()
	    cmd.set('stick_transparency', '0.1', 'interaction')
	    cmd.disable('interaction')
	    if script=='1':
                            f.write('''cmd.set('stick_transparency', '0.1', 'interaction')
cmd.disable('interaction')\n''')
	else:
	    tkMessageBox.showinfo("Error", "There are no hetero atoms in this molecule.")

    # ball and stick view	
    def ball_and_stick(self):
        self.update(self.p)
        objects = cmd.get_names('all')
        if script=='1':
            f.write('''objects = cmd.get_names('all')\n''')
        checkitforthese()
        set_defaults()
        delcrea()
        cmd.set("stick_radius","0.1","all")
        cmd.set("sphere_scale","0.3","all")
        if script=='1':
            f.write('''cmd.set("stick_radius","0.1","all")
cmd.set("sphere_scale","0.3","all")\n''')
        if 'protein' in objects:
            cmd.show('spheres','protein')
            cmd.show('sticks','protein')
            if script=='1':
                f.write('''cmd.show('spheres','protein')
cmd.show('sticks','protein')\n''')
            cpkprotein()
        if 'nucleic_acid' in objects:
            try:
                cmd.set('cartoon_ring_mode', '1')
                cmd.show('cartoon','resn a+g+c+t+u')
                cmd.show('spheres','resn a+g+c+t+u')
                cmd.show('sticks','resn a+g+c+t+u')
                if script=='1':
                    f.write('''cmd.set('cartoon_ring_mode', '1')
cmd.show('cartoon','resn a+g+c+t+u')
cmd.show('spheres','resn a+g+c+t+u')
cmd.show('sticks','resn a+g+c+t+u')\n''')
                cpknucleic()
            except:
                cmd.show('cartoon','resn a+g+c+t+u')
                if script=='1':
                    f.write('''cmd.show('cartoon','resn a+g+c+t+u')\n''')
                cpknucleic()
        if 'ligands' in objects:
            cmd.show('spheres','ligands')
            cmd.color('orange', 'ligands')
            if script=='1':
                f.write('''cmd.show('spheres','ligands')
cmd.color('orange', 'ligands')\n''')
	    
    # show the surface of the molecule
    def surface_view(self):
        delcrea()
        self.update(self.p)
        objects = cmd.get_names('all')
        if script=='1':
                f.write('''objects = cmd.get_names('all')\n''')
        checkitforthese()
        set_defaults()
        cmd.show('surface','all')
        if script=='1':
                f.write(''' cmd.show('surface','all')\n''')
        cpkprotein()
       
       	
    # show the polarities of the molecule
    def view_polarity(self):
        delcrea()
        self.update(self.p)
        checkitforthese()
        set_defaults()
        objects = cmd.get_names('all')
        if script=='1':
                f.write('''objects = cmd.get_names('all')\n''')
        if 'protein' in objects:
            cmd.show('surface', 'protein')
            if script=='1':
                f.write('''cmd.show('surface', 'protein')\n''')
        cmd.color('red','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
        cmd.color('blue','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
        cmd.show('spheres','het')
        cmd.color('green','het')
        if script=='1':
                f.write('''cmd.color('red','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
cmd.color('blue','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
cmd.show('spheres','het')
cmd.color('green','het')\n''')
        try:
          cmd.set('cartoon_ring_mode' ,'1')
          if script=='1':
              f.write(''' cmd.set('cartoon_ring_mode' ,'1')\n''')
        except:
          cmd.color('green','het')
          if script=='1':
              f.write('''cmd.color('green','het')\n''')
        cmd.show('cartoon','resn a+g+c+t+u')
        if script=='1':
            f.write('''cmd.show('cartoon','resn a+g+c+t+u')\n''')
        cpknucleic()
        import tkMessageBox
        tkMessageBox.showinfo('Info', 'Red = Hydrophobic\nBlue = Hydrophilic')
        
    # putty representation
    def show_putty(self):
      try:
        self.update(self.p)
        checkitforthese()
        set_defaults()
        delcrea()
        cmd.hide('all')
        cmd.show('spheres', 'het')
        cmd.color('orange', 'het')
        cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.color("red", "ss h")
        cmd.color("yellow", "ss s")
        cmd.color("cyan", "ss l+\'\'")
        cmd.cartoon('putty','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.show('sticks','resn t+g+c+a+u')
        if script=='1':
            f.write('''cmd.hide('all')
cmd.show('spheres', 'het')
cmd.color('orange', 'het')
cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.color("red", "ss h")
cmd.color("yellow", "ss s")
cmd.color("cyan", "ss l+\'\'")
cmd.cartoon('putty','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.show('sticks','resn t+g+c+a+u')\n''')
        cpknucleic()
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Error', 'Putty is not supported by this version of PyMol\nTry downloading the newest version to troubleshoot this problem')
                  	    
    # aromatics view
    def color_aromatics(self):
        self.update(self.p)
        set_defaults()
        checkitforthese()
        delcrea()
        cmd.hide('all')
        cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.color('aquamarine','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.set('cartoon_transparency','0.6','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.show('cartoon','resn t+u+g+c+a')
        cmd.color('aquamarine','resn u+g+c+a+t')
        cmd.set('cartoon_transparency','0.6','resn a+u+c+t+g')
        cmd.select('aromatics','resn phe+tyr+trp+his')
        cmd.color('red', 'aromatics')
        cmd.show('sticks','aromatics and (!name c+n+o)')
        cmd.set('stick_radius','0.4','all')
        cmd.delete('aromatics')
        if script=='1':
            f.write('''cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.color('aquamarine','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.set('cartoon_transparency','0.6','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.show('cartoon','resn t+u+g+c+a')
cmd.color('aquamarine','resn u+g+c+a+t')
cmd.set('cartoon_transparency','0.6','resn a+u+c+t+g')
cmd.select('aromatics','resn phe+tyr+trp+his')
cmd.color('red', 'aromatics')
cmd.show('sticks','aromatics and (!name c+n+o)')
cmd.set('stick_radius','0.4','all')
cmd.delete('aromatics')\n''')
        cmd.deselect()
	
    # color the molecule by chain
    def color_by_chain(self):
      color_by_chain()


        #------------Brett's and Charlie's Code------------
        #-------Show Charged-------------------
    def show_charged(*args):
      delcrea()
      set_defaults()
      try:
        self = args[0]
        self.update(self.p)
      except:
        pass
      checkitforthese()
      objects = cmd.get_names('all')
      cmd.hide('everything')
      cmd.show('cartoon','all')
      cmd.color('gray','all')
      cmd.select('pos','resn arg+lys+his')
      cmd.show('sticks', 'pos and !name c+n+o')
      cmd.color('marine','pos')
      cmd.delete('pos')
      cmd.select('neg', 'resn glu+asp')
      cmd.show('sticks', 'neg and !name c+n+o')
      cmd.color('red','neg')
      cmd.delete('neg')
      cmd.set('cartoon_smooth_loops','0')
      if script=='1':
          f.write('''objects = cmd.get_names('all')
cmd.hide('everything')
cmd.show('cartoon','all')
cmd.color('gray','all')
cmd.select('pos','resn arg+lys+his')
cmd.show('sticks', 'pos and !name c+n+o')
cmd.color('marine','pos')
cmd.delete('pos')
cmd.select('neg', 'resn glu+asp')
cmd.show('sticks', 'neg and !name c+n+o')
cmd.color('red','neg')
cmd.delete('neg')
cmd.set('cartoon_smooth_loops','0')\n''')
      if 'protein' in objects:
          import tkMessageBox
          tkMessageBox.showinfo('Charge Info', 'Blue = Positively charged Amino Acids\nRed = Negatively charged Amino Acids')
    cmd.extend('show_charged', show_charged)
      
   
    def surf_toon(*args):
      delcrea()
      color_by_chain()
      cmd.hide('everything')
      cmd.show('cartoon','all')
      cmd.select('surface', 'all')
      cmd.do('show surface, all')
      cmd.do('set transparency, 0.5, surface')
      cmd.set('cartoon_smooth_loops','0')       
      cmd.delete('surface')
      if script=='1':
          f.write('''cmd.hide('everything')
cmd.show('cartoon','all')
cmd.select('surface', 'all')
cmd.do('show surface, all')
cmd.do('set transparency, 0.5, surface')
cmd.set('cartoon_smooth_loops','0')       
cmd.delete('surface')\n''')
    cmd.extend('surf_over_toon',surf_toon)
     
      
  
    def surf_stick(*args):
      delcrea()
      try:
        self = args[0]
        self.update(self.p)
      except:
        pass
      checkitforthese()
      cmd.hide('everything')
      cmd.show('stick','all')
      cmd.select('surface', 'all')
      cmd.do('show surface, all')
      cmd.do('set transparency, 0.5, surface')              
      cmd.delete('surface')
      if script=='1':
          f.write('''  cmd.hide('everything')
cmd.show('stick','all')
cmd.select('surface', 'all')
cmd.do('show surface, all')
cmd.do('set transparency, 0.5, surface')              
cmd.delete('surface')\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('surf_over_stick',surf_stick)

      
          
    def mesh_stick(*args):
        delcrea()
        cmd.hide('everything')
        cmd.do("show stick, all")
        cmd.do("color white, all")
        cmd.do("create mesh1, all")
        cmd.set('mesh_quality', '3')
        cmd.do("show mesh, mesh1")
        cmd.color('tv_blue', 'mesh1')
        cmd.hide("stick", "mesh1")
        if script=='1':
            f.write('''cmd.hide('everything')
cmd.do("show stick, all")
cmd.do("color white, all")
cmd.do("create mesh1, all")
cmd.set('mesh_quality', '3')
cmd.do("show mesh, mesh1")
cmd.color('tv_blue', 'mesh1')
cmd.hide("stick", "mesh1")\n''')
    cmd.extend('mesh_over_stick',mesh_stick)

    def stick_toon(*args):
        delcrea()
        cmd.hide('everything')
        cmd.show('lines')
        cmd.create('cartoon', 'all')
        cmd.show('cartoon', 'cartoon')
        cmd.color('salmon', 'cartoon')
        cmd.color('cyan', 'resn a+t+u+g+c')
        if script=='1':
            f.write('''cmd.hide('everything')
cmd.show('lines')
cmd.create('cartoon', 'all')
cmd.show('cartoon', 'cartoon')
cmd.color('salmon', 'cartoon')
cmd.color('cyan', 'resn a+t+u+g+c')\n''')
    cmd.extend('stick_and_cartoon',stick_toon)

        
    def dot_line(*args):
        delcrea()
        cmd.set('dot_density', '3')
        cmd.hide('everything')
        cmd.remove('resn HOH')
        cmd.hide('everything')
        cmd.show('lines')
        cmd.show('dots', 'all')
        if script=='1':
            f.write('''cmd.set('dot_density', '3')
cmd.hide('everything')
cmd.remove('resn HOH')
cmd.hide('everything')
cmd.show('lines')
cmd.show('dots', 'all')\n''')
    cmd.extend('dot_line',dot_line)
        
    def rovingstickers(*args):
      cmdRovStick = ' '

      try:
        self = args[0]
        self.update(self.p)
      except:
        try:
          float(args[0])
        except (ValueError, IndexError):
          print "Usage: roving stick # (# is a value between 0 and 20)"
        else:
          cmdRovStick = args[0]

      checkitforthese()
      delcrea()
      cmd.hide('everything')
      cmd.remove("hydro")
      cmd.set("roving_detail",1)
      cmd.set("roving_origin",1)
      cmd.set("stick_radius",0.3)

      try:
        cmd.set("roving_sticks",self.rovingradius2.get())
      except:
        cmd.set("roving_sticks",cmdRovStick)

      cmd.set("roving_polar_contacts",8)
      if script=='1':
        f.write('''cmd.hide('everything')
cmd.remove("hydro")
cmd.set("roving_detail",1)
cmd.set("roving_origin",1)
cmd.set("stick_radius",0.3)
cmd.set("roving_sticks",self.rovingradius2.get())
cmd.set("roving_polar_contacts",8)\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('roving_stick',rovingstickers)
    
    def rovinglines(*args):
      cmdRovLine = ''

      #This next construction looks strange, I know, but this way it executes
      #the default settings if the user does not specifiy range!
      #Don't Worry. I plan on fixing this.

      try:
        self = args[0]
        self.update(self.p)
      except:
        try:
          cmdRovLine = float(args[0])
        except:
          print 'Usage: roving lines # (# is value between 0 and 20)'
        
      checkitforthese()
      delcrea()
      cmd.hide('everything')
      cmd.remove("hydro")
      cmd.set("roving_detail",1)
      cmd.set("roving_origin",1)
      cmd.set("roving_sticks",0)
      try:
        cmd.set('roving_lines', self.rovingradius2.get())
      except:
        cmd.set('roving_lines', cmdRovLine)
      cmd.set("roving_polar_contacts",8)
      if script=='1':
        f.write('''cmd.hide('everything')
cmd.remove("hydro")
cmd.set("roving_detail",1)
cmd.set("roving_origin",1)
cmd.set("roving_sticks",0)
cmd.set('roving_lines', self.rovingradius2.get())
cmd.set("roving_polar_contacts",8)\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('roving_line', rovinglines)
        
    def rovingballstick(*args):
      cmdRovBall = ''

      try:
        self = args[0]
        self.update(self.p)
      except:
        try:
          cmdRovBall = float(args[0])
        except:
          print 'Usage: roving ballstick # (# is value between 0 and 20)'
          
      checkitforthese()
      delcrea()
      cmd.hide('everything')
      cmd.remove("hydro")
      cmd.set("roving_detail",1)
      cmd.set("roving_origin",1)
      try:
        cmd.set('roving_sticks', self.rovingradius2.get())
      except:
        cmd.set('roving_sticks', cmdRovBall)
      cmd.set("roving_polar_contacts",8)
      try:
        cmd.set('roving_spheres', self.rovingradius2.get())
      except:
        cmd.set('roving_spheres', cmdRovBall)
      cmd.set('sphere_transparency', '0.2')
      cmd.set("stick_radius","0.1","all")
      cmd.set("sphere_scale","0.3","all")
      if script=='1':
        f.write('''cmd.hide('everything')
cmd.remove("hydro")
cmd.set("roving_detail",1)
cmd.set("roving_origin",1)
cmd.set('roving_sticks', self.rovingradius2.get())
cmd.set("roving_polar_contacts",8)
cmd.set('roving_spheres', self.rovingradius2.get())
cmd.set('sphere_transparency', '0.2')
cmd.set("stick_radius","0.1","all")
cmd.set("sphere_scale","0.3","all")\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('roving_ballstick',rovingballstick)
    

    def rovingspheres(*args):
      cmdRovSphere = ''
      
      try:
        self = args[0]
        self.update(self.p)
      except:
        try:
          cmdRovSphere = float(args[0])
        except:
          print 'Usage: rovingspheres # (# is value between 0 and 20)'

      checkitforthese()
      cmd.hide('everything')
      cmd.remove("hydro")
      cmd.set("roving_detail",1)
      cmd.set("roving_origin",1)
      try:
        cmd.set('roving_spheres', self.rovingradius2.get())
      except:
        cmd.set('roving_spheres', cmdRovSphere)
      cmd.set("roving_polar_contacts",8)
      cmd.set('sphere_transparency', '0.2')
      cmd.set('sphere_scale', '0.8', 'all')
      if script=='1':
          f.write('''cmd.hide('everything')
cmd.remove("hydro")
cmd.set("roving_detail",1)
cmd.set("roving_origin",1)
cmd.set('roving_spheres', self.rovingradius2.get())
cmd.set("roving_polar_contacts",8)
cmd.set('sphere_transparency', '0.2')
cmd.set('sphere_scale', '0.8', 'all')\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('roving_sphere',rovingspheres)

    def chain_contact(*args):
      try:
        self = args[0]
      except:
        pass
      delcrea()
      cmd.hide('everything')
      cmd.show('mesh', 'all')
      cmd.color('gray40', 'all')
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
      checkforchain()
      cmd.orient()
      objects = cmd.get_names('all')
      chainpulllist = []

      if 'Chain-A' in objects:
        chainpulllist.append('Chain-A')
      if 'Chain-B' in objects:
        chainpulllist.append('Chain-B')
      if 'Chain-C' in objects:
        chainpulllist.append('Chain-C')
      if 'Chain-D' in objects:
        chainpulllist.append('Chain-D')
      if 'Chain-E' in objects:
        chainpulllist.append('Chain-E')           
      if 'Chain-F' in objects:
        chainpulllist.append('Chain-F')
      if 'Chain-G' in objects:
        chainpulllist.append('Chain-G')
      if 'Chain-H' in objects:
        chainpulllist.append('Chain-H')
      if 'Chain-I' in objects:
        chainpulllist.append('Chain-I')
      if 'Chain-J' in objects:
        chainpulllist.append('Chain-J')
      if 'Chain-K' in objects:
        chainpulllist.append('Chain-K')
      if 'Chain-L' in objects:
        chainpulllist.append('Chain-L')
      if 'Chain-M' in objects:
        chainpulllist.append('Chain-M')
      if 'Chain-N' in objects:
        chainpulllist.append('Chain-N')
      if 'Chain-O' in objects:
        chainpulllist.append('Chain-O')
      if 'Chain-P' in objects:
        chainpulllist.append('Chain-P')
      if 'Chain-Q' in objects:
        chainpulllist.append('Chain-Q')
      if 'Chain-R' in objects:
        chainpulllist.append('Chain-R')
      if 'Chain-S' in objects:
        chainpulllist.append('Chain-S')
      if 'Chain-T' in objects:
        chainpulllist.append('Chain-T')
      if 'Chain-U' in objects:
        chainpulllist.append('Chain-U')
      if 'Chain-V' in objects:
        chainpulllist.append('Chain-V')
      if 'Chain-W' in objects:
        chainpulllist.append('Chain-W')
      if 'Chain-X' in objects:
        chainpulllist.append('Chain-X')
      if 'Chain-Y' in objects:
        chainpulllist.append('Chain-Y')
      if 'Chain-Z' in objects:
        chainpulllist.append('Chain-Z')         

      if len(chainpulllist) >1:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[1])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >2:
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >3:
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[3])
          cmd.delete('duh')
        if len(chainpulllist) >4:
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >5:
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >6:
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[1])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >2:
        
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[2])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >3:
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >4:
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >5:
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >6:
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[2])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >3:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[3])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >4:
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >5:
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >6:
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[3])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >4:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[4])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >5:
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >6:
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[4])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >5:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[5])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >6:
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[5])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >6:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[6])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >7:
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[6])
          cpkduh()
          cmd.delete('duh')    
          cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

          
      if len(chainpulllist) >7:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[7])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >8:
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[7])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')
        
      if len(chainpulllist) >8:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[8])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >9:
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[8])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')
        
      if len(chainpulllist) >9:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[9])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        if len(chainpulllist) >10:
          cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[9])
          cpkduh()
          cmd.delete('duh')
          cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[10])
          cpkduh()
          cmd.delete('duh')

      if len(chainpulllist) >10:
        cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[10])
        cpkduh()
        cmd.delete('duh')    
        cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[0])
        cpkduh()
        cmd.delete('duh')
        
    cmd.extend('chain_contact',chain_contact)
   

    def show_cpk(*args):
      try:
        self = args[0]
        self.update(self.p)
      except:
        pass
      objects = cmd.get_names('all')
      if script=='1':
            f.write('''objects = cmd.get_names('all')\n''')
      checkitforthese()
      set_defaults()
      delcrea()
      cmd.set("sphere_scale","0.7","all")
      cmd.show('spheres','all')
      if script=='1':
            f.write('''cmd.set("sphere_scale","0.7","all")
cmd.show('spheres','all')\n''')
      cpkprotein()#stopped here
      cpkligands()
      cpknucleic()
    cmd.extend('show_cpk',show_cpk)

    def spheresurf(*args):
      try:
        self = args[0]
        self.update(self.p)
      except:
        pass

      checkitforthese()
      set_defaults()
      delcrea()
      cmd.show('spheres', 'all')
      cmd.create('surface', 'all')
      cmd.show('surface', 'surface')
      cmd.color('white', 'surface')
      cmd.set('sphere_scale', '0.5', 'all')
      cmd.set('transparency', '0.4')
      if script=='1':
        f.write('''cmd.show('spheres', 'all')
cmd.create('surface', 'all')
cmd.show('surface', 'surface')
cmd.color('white', 'surface')
cmd.set('sphere_scale', '0.5', 'all')
cmd.set('transparency', '0.4')\n''')
      cpkprotein()
      cpknucleic()
      cpkligands()
    cmd.extend('spheresurf',spheresurf)
      #-----------Electron Density Presets----------------#
      
    def mesh_ribbon(self):
        try:
           
              
            delcrea()
           
            try:
                    cmd.hide('everything')
                    cmd.isomesh('map1','map', contour1.get())
                    if script=='1':
                        f.write('''cmd.hide('everything')
cmd.isomesh('map1','map', contour1.get())\n''')
                    
            except:
                    try:
                        cmd.set("suspend_updates",1,quiet=1)
                        cmd.remove("hydro")      
                        cmd.map_new('map',"gaussian","0.75", 'all')
                        cmd.set("suspend_updates",0,quiet=1)
                        cmd.refresh()
                        cmd.isomesh('map1','map', '1')
                        if script=='1':
                            f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isomesh('map1','map', '1')\n''')
                       
                    except:
                            import tkMessageBox
                            tkMessageBox.showinfo("Error", 'No PDB is present')
                            
                    cmd.show('ribbon', 'all')
            cmd.show('lines', 'all')
            cmd.color('red', 'all')
            cmd.color('purpleblue', 'map1')
            if script=='1':
                            f.write('''cmd.show('ribbon', 'all')
cmd.show('lines', 'all')
cmd.color('red', 'all')
cmd.color('purpleblue', 'map1')\n''')
            
        except:
            cmd.show('lines', 'all')
            if script=='1':
                f.write('''cmd.show('lines', 'all')''')
            import tkMessageBox
            tkMessageBox.showinfo('Alert', 'Protein must be present')
            

    def dot_sticks(self):
         try:  
             delcrea()
             cmd.hide('everything')
             if script=='1':
                f.write('''cmd.hide('everything')\n''')
             try:
                cmd.set("suspend_updates",1,quiet=1)
                cmd.remove("hydro")      
                cmd.enable('all')
                cmd.map_new('map',"gaussian","0.75", 'all')
                cmd.isodot("map1", "map", 9999.0, 'all')
                cmd.set("suspend_updates",0,quiet=1)
                cmd.refresh()
                cmd.isodot('map1','map', '1')
                if script=='1':
                    f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isodot("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isodot('map1','map', '1')\n''')
             except:
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'No PDB is present')
                
             cmd.show('sticks', 'all')
             cmd.color('blue', 'all')
             cmd.color('red', 'map1')
             if script=='1':
                    f.write('''cmd.show('sticks', 'all')
cmd.color('blue', 'all')
cmd.color('red', 'map1')\n''')
         except:
            cmd.show('lines', 'all')
            if script=='1':
                    f.write('''cmd.show('lines', 'all')\n''')
            import tkMessageBox
            tkMessageBox.showinfo('Alert', 'Protein must be present')

    def surfinglines(*args):

        try:
            cmd.hide('everything')
            if script=='1':
                    f.write('''cmd.hide('everything')\n''')

            self.update(self.p)
            checkitforthese()
            delcrea()
            
            try:
                cmd.remove("hydro")      
                cmd.map_new('map',"gaussian","0.75", 'all')
                cmd.isosurface('map1','map','1')
                cmd.show('lines', 'all')
                cpkprotein()
                cpkligands()
                cpknucleic()
                cmd.color('white', 'elem c')
                cmd.color('orange', "map1")
                cmd.set('transparency', '0.4')
                cmd.set('ambient', '0.45')
                if script=='1':
                    f.write('''cmd.remove("hydro")      
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isosurface('map1','map','1')
cmd.show('lines', 'all')
cpkprotein()
cpkligands()
cpknucleic()
cmd.color('white', 'elem c')
cmd.color('orange', "map1")
cmd.set('transparency', '0.4')
cmd.set('ambient', '0.45')\n''')
            except:
                cmd.show('lines', 'all')
                if script=='1':
                    f.write('''cmd.show('lines', 'all')\n''')
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'No PDB is present')
        except:
            cmd.show('lines', 'all')
            if script=='1':
                    f.write('''cmd.show('lines', 'all')\n''')
            import tkMessageBox
            tkMessageBox.showinfo('Alert', 'Protein must be present')
    cmd.extend('surfinglines',surfinglines)

#------------------Motif stuff---------------------
    def deletemotif(self):
      deletemotif()

        
#----------Motif definitions consisting of measuring atom to atom between different
        #  amino acid residues and allowing them to be altered by a slider

    def serineprotease(self):
      self.update(self.p)#updates list of molecular groups
      objects = cmd.get_names('all')#gets names of objects
      checkitforthese()#sees if objects are in objects
      set_defaults()#sets defaults
      delcrea()#deletes created objects
      deletemotif()#deletes previous motif
      cmd.select('asp1', 'resn asp within %s of resn his' %(self.range.get()*3)) #selects aspartate within 3 of histidine
      cmd.select('asp2', 'resn asp within %s of resn ser'%(self.range.get()*7))
      cmd.select('asp', 'byres asp1 and byres asp2') 
      cmd.select('his1', 'resn his within %s of asp' %(self.range.get()*4))
      cmd.select('his2', 'resn his within %s of resn ser' %(self.range.get()*4))
      cmd.select('his', 'byres his1 and byres his2') 
      cmd.select('ser1', 'name og within %s of name ne2' %(self.range.get()*3.5))
      cmd.select('ser2', 'resn ser within %s of asp' %(self.range.get()*7))
      cmd.select('ser', 'byres ser1 and byres ser2') 
      cmd.select('serineprotease', 'ser(his(asp))') 
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.set('cartoon_transparency', '0.5', 'all')
      cmd.show('sticks', 'serineprotease')
      cmd.set('stick_radius','0.5')
      cpkserineprotease()#colors in cpk
      cmd.orient('serineprotease')
      cmd.deselect()#deselects
      cmd.delete('asp')#deletes selections
      cmd.delete('his')
      cmd.delete('ser')
      cmd.delete('asp1')
      cmd.delete('his1')
      cmd.delete('ser1')
      cmd.delete('asp2')
      cmd.delete('his2')
      cmd.delete('ser2')
      

    def Blactamase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('lys1', 'name nz and resn lys within %s of (name oh and resn tyr)' %(self.range.get()*5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name cz and resn tyr)' %(self.range.get()*5.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name ce1 and resn tyr)' %(self.range.get()*6.5))
      cmd.select('lys4', 'name nz and resn lys within %s of (name ce2 and resn tyr)' %(self.range.get()*6.5))
      cmd.select('lys5', 'name ce and resn lys within %s of (name oh and resn tyr)' %(self.range.get()*5))
      cmd.select('lys6', 'name ce and resn lys within %s of (name cz and resn tyr)' %(self.range.get()*6))
      cmd.select('lys7', 'name nz and resn lys within %s of (name og and resn ser)' %(self.range.get()*6))
      cmd.select('lys8', 'name nz and resn lys within %s of (name cb and resn ser)' %(self.range.get()*5.2))
      cmd.select('lys9', 'name cb and resn lys within %s of (name cb and resn ser)' %(self.range.get()*9.2))
      cmd.select('lys10', 'name ce and resn lys within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('lys11', 'name nz and resn lys within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('lys12', 'name nz and resn lys within %s of (name oe2 and resn glu)' %(self.range.get()*12.5))
      cmd.select('lys13', 'name ce and resn lys within %s of (name cd and resn glu)' %(self.range.get()*11))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*5))
      cmd.select('tyr2', 'name cz and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*5.5))
      cmd.select('tyr3', 'name ce1 and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*6.5))
      cmd.select('tyr4', 'name ce2 and resn tyr within %s of (name nz and lys)' %(self.range.get()*6.5))
      cmd.select('tyr5', 'name oh and resn tyr within %s of (name ce and resn lys)' %(self.range.get()*5))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name ce and resn lys)' %(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name og and resn ser)' %(self.range.get()*6))
      cmd.select('tyr8', 'name cz and resn tyr within %s of (name og and resn ser)' %(self.range.get()*6.5))
      cmd.select('tyr9', 'name oh and resn tyr within %s of (name cb and resn ser)' %(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s of (name oe1 and resn glu)' %(self.range.get()*10))
      cmd.select('tyr11', 'name oh and resn tyr within %s of (name oe2 and resn glu)' %(self.range.get()*10))
      cmd.select('tyr12', 'name oh and resn tyr within %s of (name cd and resn glu)' %(self.range.get()*10))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12')
      cmd.select('ser1', 'name cb and resn ser within %s of (name nz and resn lys)' %(self.range.get()*6))
      cmd.select('ser2', 'name og and resn ser within %s of (name nz and resn lys)' %(self.range.get()*6))
      cmd.select('ser3', 'name cb and resn ser within %s of (name cb and lys)' %(self.range.get()*8.2))
      cmd.select('ser4', 'name og and resn ser within %s of (name cz and resn tyr)' %(self.range.get()*6.5))
      cmd.select('ser5', 'name cb and resn ser within %s of (name oh and resn tyr)' %(self.range.get()*6.5))
      cmd.select('ser6', 'name og and resn ser within %s of (name oh and tyr)' %(self.range.get()*6))
      cmd.select('ser7', 'name og and resn ser within %s of (name oe1 and resn glu)' %(self.range.get()*12))
      cmd.select('ser8', 'name og and resn ser within %s of (name oe2 and resn glu)' %(self.range.get()*12))
      cmd.select('ser9', 'name cb and resn ser within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('ser10', 'name cb and resn ser within %s of (name oe2 and resn glu)' %(self.range.get()*12.5))
      cmd.select('ser11', 'name og and resn ser within %s of (name cd and resn glu)' %(self.range.get()*12.5))
      cmd.select('ser12', 'name cb and resn ser within %s of (name cd and resn glu)' %(self.range.get()*11.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10 and byres ser11 and byres ser12')
      cmd.select('glu1', 'name oe1 and resn glu within %s of (name ce and resn lys)' %(self.range.get()*8.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)' %(self.range.get()*9.5))
      cmd.select('glu3', 'name oe2 and resn glu within %s of (name nz and lys)' %(self.range.get()*11.2))
      cmd.select('glu4', 'name cd and resn glu within %s of (name ce and resn lys)' %(self.range.get()*10.6))
      cmd.select('glu5', 'name oe1 and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*8.7))
      cmd.select('glu6', 'name oe2 and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*9.7))
      cmd.select('glu7', 'name cd and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*9.6))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and resn ser)' %(self.range.get()*10.5))
      cmd.select('glu9', 'name oe2 and resn glu within %s of (name og and resn ser)' %(self.range.get()*10.5))
      cmd.select('glu10', 'name oe1 and resn glu within %s of (name cb and resn ser)' %(self.range.get()*10))
      cmd.select('glu11', 'name oe2 and resn glu within %s of (name cb and resn ser)' %(self.range.get()*11.8))
      cmd.select('glu12', 'name cd and resn glu within %s of (name og and resn ser)' %(self.range.get()*11.8))
      cmd.select('glu13', 'name cd and resn glu within %s of (name cb and ser)' %(self.range.get()*11))
      cmd.select('glu14', 'name oe1 and resn glu within %s of (name cg and tyr)' %(self.range.get()*7.4))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14')     
      cmd.select('lactamase', 'ser(tyr(glu(lys)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.set('cartoon_transparency', '0.8', 'all')
      cmd.show('sticks', 'lactamase')
      cmd.set('stick_radius','0.5')
      cpkBlactamase()
      cmd.orient('lactamase')
      cmd.deselect
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr2')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser11')
      cmd.delete('ser12')
      cmd.delete('ser')
      cmd.delete('glu')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu12')
      cmd.delete('glu13')
      cmd.delete('glu14')
      cmd.deselect()

    def superoxide(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'byres resn his within %s of elem cu'%(self.range.get()*4))
      cmd.select('arg1', 'byres resn arg within %s of elem cu'%(self.range.get()*6))
      cmd.select('stuff', 'his1 and (byres elem zn around %s)'%(self.range.get()*4))
      cmd.select('stuff1', 'arg1 and (byres elem zn around %s)'%(self.range.get()*6))
      cmd.select('stuff2', 'byres elem cu around %s and his1'%(self.range.get()*4))
      cmd.select('stuff3', 'byres elem cu around %s and arg1'%(self.range.get()*6))
      cmd.select('stuff4', 'stuff and stuff1 and stuff2 and stuff3')
      cmd.select('superoxide', 'byres his1(arg1(stuff4))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.show('sticks', 'superoxide')
      cmd.color('copper', 'elem cu')
      cmd.color('grey40', 'elem zn')
      cmd.show('spheres', 'elem cu')
      cmd.show('spheres', 'elem zn')
      cmd.set('cartoon_transparency', '0.7', 'all')
      cpkreductase()
      cmd.deselect()
      cmd.orient('superoxide')
      cmd.delete('his1')
      cmd.delete('arg1')
      cmd.delete('stuff')
      cmd.delete('stuff1')
      cmd.delete('stuff2')
      cmd.delete('stuff3')
      cmd.delete('stuff4')

    def metalloprotease(self):
      self.update(self.p)
      objects = cmd.get_names('all')
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.hide('everything')
      cmd.select('zn', 'elem zn')
      cmd.show('sphere', 'zn')
      cmd.select('metalloprotease', 'zn(byres zn around %s)'%(self.range.get()*5))
      cmd.show('cartoon', 'all')
      cmd.set('cartoon_transparency', '0.5', 'all')
      cmd.show('sticks', 'metalloprotease')
      cpkmetalloprotease()
      cmd.delete('zn')
      cmd.orient('metalloprotease')
      cmd.deselect()

    def tyrophos(self):
      self.update(self.p)
      objects = cmd.get_names('all')
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.hide('everything')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(self.range.get()*6.5))
      cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
      cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name og and resn ser)'%(self.range.get()*10))
      cmd.select('arg8', 'name nh1 and resn arg within %s of (name cb and resn ser)'%(self.range.get()*11.2))
      cmd.select('arg9', 'name ne and resn arg within %s of (name ca and resn ser)'%(self.range.get()*9))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and arg)'%(self.range.get()*7))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('asp3', 'name cb and resn asp within %s of (name ne and arg)'%(self.range.get()*6.5))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name c and resn ser)'%(self.range.get()*11))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ca and resn ser)'%(self.range.get()*12))
      cmd.select('asp6', 'name cb and resn asp within %s of (name cb and resn ser)'%(self.range.get()*9.2))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(self.range.get()*12))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*11))
      cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(self.range.get()*10))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('cys1', 'name ca and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys3', 'name sg and resn cys within %s of (name ca and resn ser)'%(self.range.get()*6))
      cmd.select('cys4', 'name c and resn cys within %s of (name od1 and asp)'%(self.range.get()*12))
      cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and asp)'%(self.range.get()*11))
      cmd.select('cys6', 'name sg and resn cys within %s of (name cb and asp)'%(self.range.get()*10))
      cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and arg)'%(self.range.get()*7))
      cmd.select('cys9', 'name sg and resn cys within %s of (name ne and arg)'%(self.range.get()*6.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name nh2 and arg)'%(self.range.get()*10))
      cmd.select('ser2', 'name cb and resn ser within %s of (name nh1 and arg)'%(self.range.get()*11.2))
      cmd.select('ser3', 'name ca and resn ser within %s of (name ne and arg)'%(self.range.get()*9))
      cmd.select('ser4', 'name c and resn ser within %s of (name od2 and asp)'%(self.range.get()*11))
      cmd.select('ser5', 'name ca and resn ser within %s of (name od1 and asp)'%(self.range.get()*12))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cb and asp)'%(self.range.get()*9.2))
      cmd.select('ser7', 'name og and resn ser within %s of (name ca and cys)'%(self.range.get()*6.5))
      cmd.select('ser8', 'name cb and resn ser within %s of (name cb and cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name ca and resn ser within %s of (name sg and cys)'%(self.range.get()*6))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')      
      cmd.select('tyrophos', 'ser(asp(arg(cys)))')
      tycount = cmd.index('tyrophos')
      atcount  = len(tycount)
      if(atcount < 1):
        cmd.hide('everything')
        cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*7))
        cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*7))
        cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(self.range.get()*6.5))
        cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*7))
        cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
        cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6.5))
        cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6')
        cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(self.range.get()*7))
        cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*7))
        cmd.select('asp3', 'name cb and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6.5))
        cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(self.range.get()*12))
        cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*11))
        cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(self.range.get()*10))
        cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp7 and byres asp8 and byres asp9')
        cmd.select('cys4', 'name c and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*12))
        cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*11))
        cmd.select('cys6', 'name sg and resn cys within %s of (name cb and resn asp)'%(self.range.get()*10))
        cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(self.range.get()*7))
        cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and resn arg)'%(self.range.get()*7))
        cmd.select('cys9', 'name sg and resn cys within %s of (name ne and resn arg)'%(self.range.get()*6.5))
        cmd.select('cys', 'byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
        cmd.select('tyrophos', '(asp(arg(cys)))')
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'tyrophos')
        cmd.hide('cartoon', 'tyrophos')
        cpktyrophos()
        cmd.delete('arg')
        cmd.delete('arg1')
        cmd.delete('arg2')
        cmd.delete('arg3')
        cmd.delete('arg4')
        cmd.delete('arg5')
        cmd.delete('arg6')
        cmd.delete('arg7')
        cmd.delete('arg8')
        cmd.delete('arg9')    
        cmd.delete('ser')
        cmd.delete('ser1')
        cmd.delete('ser2')
        cmd.delete('ser3')
        cmd.delete('ser4')
        cmd.delete('ser5')
        cmd.delete('ser6')
        cmd.delete('ser7')
        cmd.delete('ser8')
        cmd.delete('ser9')
        cmd.delete('asp')
        cmd.delete('asp1')
        cmd.delete('asp2')
        cmd.delete('asp3')
        cmd.delete('asp4')
        cmd.delete('asp5')
        cmd.delete('asp6')
        cmd.delete('asp7')
        cmd.delete('asp8')
        cmd.delete('asp9') 
        cmd.delete('cys')
        cmd.delete('cys1')
        cmd.delete('cys2')
        cmd.delete('cys3')
        cmd.delete('cys4')
        cmd.delete('cys5')
        cmd.delete('cys6')
        cmd.delete('cys7')
        cmd.delete('cys8')
        cmd.delete('cys9')
        cmd.orient('tyrophos')
        cmd.deselect()
      else:
        cmd.show('cartoon', 'all')
        cmd.set('cartoon_transparency', '0.5', 'all')
        cmd.show('sticks', 'tyrophos')
        cmd.hide('cartoon', 'tyrophos')
        cpktyrophos()
        cmd.delete('arg')
        cmd.delete('arg1')
        cmd.delete('arg2')
        cmd.delete('arg3')
        cmd.delete('arg4')
        cmd.delete('arg5')
        cmd.delete('arg6')
        cmd.delete('arg7')
        cmd.delete('arg8')
        cmd.delete('arg9')    
        cmd.delete('ser')
        cmd.delete('ser1')
        cmd.delete('ser2')
        cmd.delete('ser3')
        cmd.delete('ser4')
        cmd.delete('ser5')
        cmd.delete('ser6')
        cmd.delete('ser7')
        cmd.delete('ser8')
        cmd.delete('ser9')
        cmd.delete('asp')
        cmd.delete('asp1')
        cmd.delete('asp2')
        cmd.delete('asp3')
        cmd.delete('asp4')
        cmd.delete('asp5')
        cmd.delete('asp6')
        cmd.delete('asp7')
        cmd.delete('asp8')
        cmd.delete('asp9') 
        cmd.delete('cys')
        cmd.delete('cys1')
        cmd.delete('cys2')
        cmd.delete('cys3')
        cmd.delete('cys4')
        cmd.delete('cys5')
        cmd.delete('cys6')
        cmd.delete('cys7')
        cmd.delete('cys8')
        cmd.delete('cys9')
        cmd.orient('tyrophos')
        cmd.deselect()

    def carbanhyd(self):
      self.update(self.p)
      objects = cmd.get_names('all')
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.hide('everything')
      cmd.select('zn', 'elem zn')
      cmd.select('his', 'resn his within %s of zn'%(self.range.get()*5))
      cmd.select('carbonicanhydrase', 'byres his or zn')
      cmd.show('cartoon', 'all')
      cmd.set('cartoon_transparency', '0.5', 'all')
      cmd.show('sticks', 'carbonicanhydrase')
      cmd.show('spheres', 'zn')
      cpkcarbanhyd()
      cmd.delete('zn')
      cmd.delete('his')
      cmd.orient('carbonicanhydrase')
      cmd.deselect()

    def paplike(self):
      self.update(self.p)
      objects = cmd.get_names('all')
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.hide('everything')
      cmd.select('gln1', 'name ne2 and resn gln within %s of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('gln2', 'name cd and resn gln within %s of (name ce1 and resn his)'%(self.range.get()*6.7))
      cmd.select('gln3', 'name oe1 and resn gln within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('gln4', 'name ne2 and resn gln within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('gln5', 'name oe1 and resn gln within %s of (name sg and resn cys)'%(self.range.get()*6.7))
      cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3 and byres gln4 and byres gln5')
      cmd.select('his1', 'name ne2 and resn his within %s of (name ne2 and gln)'%(self.range.get()*7))
      cmd.select('his2', 'name ce1 and resn his within %s of (name cd and gln)'%(self.range.get()*6.7))
      cmd.select('his3', 'name nd1 and resn his within %s of (name oe1 and gln)'%(self.range.get()*7))
      cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn cys)'%(self.range.get()*5.7))
      cmd.select('his5', 'name nd1 and resn his within %s of (name sg and resn cys)'%(self.range.get()*6))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5')
      cmd.select('cys1', 'name cb and resn cys within %s of (name ce1 and his)'%(self.range.get()*5.7))
      cmd.select('cys2', 'name sg and resn cys within %s of (name nd1 and his)'%(self.range.get()*6))
      cmd.select('cys3', 'name cb and resn cys within %s of (name ne2 and gln)'%(self.range.get()*5.5))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and gln)'%(self.range.get()*6.7))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4')
      cmd.select('paplike', 'gln(his(cys))')
      cmd.show('cartoon', 'all')
      cmd.set('cartoon_transparency', '0.5', 'all')
      cmd.show('sticks', 'paplike')
      cpkpaplike()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('gln')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln4')
      cmd.delete('gln5')                        
      cmd.orient('paplike')
      cmd.deselect()

    def zincfinger(self):
          self.update(self.p)
          checkitforthese()
          set_defaults()
          delcrea()
          deletemotif()
          cmd.select('zn1', 'elem zn')        
          xm = cmd.index('zn1')
          nm  = len(xm)
          if(nm < 1):
              cmd.delete('zn1')
          objects = cmd.get_names('all')
          if 'zn1' in objects:
              cmd.select('zn1', 'elem zn')
              cmd.select('his', 'resn his')
              cmd.select('cys', 'resn cys')
              cmd.select('cys1', 'resn cys around %s'%(self.range.get()*4))
              cmd.select('Zinc_finger', '(resn cys or resn his(and byres cys1))')
              cmd.show('cartoon', 'all')
              cmd.set('cartoon_transparency', '0.6', 'all')
              cmd.color('white', 'all')
              cmd.show('sticks', 'Zinc_finger')
              cmd.show('spheres', 'elem zn')
              cmd.color('grey40', 'elem zn')
              cpkzincfinger()
              cmd.delete('zn1')
              cmd.delete('his')
              cmd.delete('cys')
              cmd.delete('cys1')
              cmd.orient('Zinc_finger')
              cmd.deselect()
          else:
               cmd.show('cartoon', 'all')
               cmd.color('white', 'all')
               cmd.set('cartoon_transparency', '0.6', 'all')
          
    def aminotransferase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('asp1', 'name od1 and resn asp within %s of (name cb and resn his)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name cg and resn his)'%(self.range.get()*6))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('asp4', 'name cg and resn asp within %s of (name cb and resn his)'%(self.range.get()*6.5))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name nz and resn lys)'%(self.range.get()*9))
      cmd.select('asp8', 'name cg and resn asp within %s of (name nz and resn lys)'%(self.range.get()*9))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp8')
      cmd.select('his1', 'name cb and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('his2', 'name cg and resn his within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('his3', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('his4', 'name cb and resn his within %s of (name cg and asp)'%(self.range.get()*6.5))
      cmd.select('his5', 'name ne2 and resn his within %s of (name od1 and asp)'%(self.range.get()*8))
      cmd.select('his6', 'name cd2 and resn his within %s of (name od1 and asp)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*8))
      cmd.select('his9', 'name ce1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('lys1', 'name nz and resn lys within %s of (name od2 and asp)'%(self.range.get()*9))
      cmd.select('lys2', 'name nz and resn lys within %s of (name cg and asp)'%(self.range.get()*9))
      cmd.select('lys3', 'name nz and resn lys within %s of (name nd1 and his)'%(self.range.get()*7.5))
      cmd.select('lys4', 'name nz and resn lys within %s of (name ne2 and his)'%(self.range.get()*8))
      cmd.select('lys5', 'name nz and resn lys within %s of (name ce1 and his)'%(self.range.get()*7))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5')
      cmd.select('Aminotransferase', 'asp(his(lys))')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.show('sticks', 'Aminotransferase')
      cpkaminotransferase()
      cmd.orient('Aminotransferase')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.deselect()
      cmd.delete('his')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('lys')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('asp')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')



    def fisomerase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his', 'elem mn around %s(elem mn)'%(self.range.get()*5))
      cmd.select('fucoseisomerase', 'byres resn asp and his(byres resn glu and his(elem mn))')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.show('sticks', 'fucoseisomerase')
      cmd.show('spheres', 'elem mn')
      cmd.orient('fucoseisomerase')
      cpkfucoisomerase()
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.deselect()
      cmd.delete('his')

    def glutamine_amidotransferase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'name ND1 within %s of name OE2'%(self.range.get()*3))
      cmd.select('his2', 'name NE2 within %s of name SG'%(self.range.get()*3.5))
      cmd.select('his', 'byres his1 and byres his2')
      cmd.select('glu1', 'resn glu within %s of his'%(self.range.get()*3.2))
      cmd.select('glu2', 'resn glu within %s of resn cys'%(self.range.get()*7))
      cmd.select('glu', 'byres glu1 and byres glu2')
      cmd.select('cys1', 'resn cys within %s of his'%(self.range.get()*3.5))
      cmd.select('cys2', 'resn cys within %s of glu'%(self.range.get()*7))
      cmd.select('cys', 'byres cys1 and byres cys2')
      cmd.select('glu_amidotransferase', 'cys(his(glu))')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.show('sticks', 'glu_amidotransferase')
      cmd.orient('glu_amidotransferase')
      cpkglu_amidotransferase()
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.deselect()
      cmd.delete('his')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('glu')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')

    def dnaligase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('amp1', 'resn amp')
      cmd.select('atp1', 'resn atp')
########
      xp = cmd.index('amp1')
      np  = len(xp)
      if(np < 1):#-------------------looks to see if amp in objects and
          cmd.delete('amp1')
########
      xtp = cmd.index('atp1')
      ntp  = len(xtp)
      if(ntp < 1):
          cmd.delete('atp1')
      objects = cmd.get_names('all')
      if 'amp1' in objects:
          cmd.select('ramp1', 'byres resn amp around %s'%(self.range.get()*7.4))
          cmd.select('lys1', 'byres resn lys and ramp1')
          cmd.select('ramp2', 'byres resn amp around %s'%(self.range.get()*7))
          
          cmd.select('ramp3', 'byres resn amp around %s'%(self.range.get()*5.3))
          cmd.select('asp1', 'ramp3 and(byres resn asp within %s of lys1)'%(self.range.get()*3))
          cmd.select('arg1', 'ramp2 and(byres resn arg within %s of asp1)'%(self.range.get()*5))
          cmd.select('Ligase', 'byres lys1(amp1(byres arg1(byres asp1)))')
          cmd.hide('everything')
          cmd.show('cartoon', 'all')
          cmd.color('white', 'all')
          cmd.set('cartoon_transparency', '0.6', 'all')
          cmd.show('sticks', 'Ligase')
          cpkdnaligase()
          cmd.deselect()
      elif 'atp1' in objects:
          cmd.select('ratp1', 'byres resn atp around %s'%(self.range.get()*7.4))
          cmd.select('lys1', 'byres resn lys and ratp1')
          cmd.select('ratp2', 'byres resn atp around %s'%(self.range.get()*7))
          
          cmd.select('ratp3', 'byres resn atp around %s'%(self.range.get()*5.3))
          cmd.select('asp1', 'ratp3 and(byres resn asp within %s of lys1)'%(self.range.get()*3))
          cmd.select('arg1', 'ratp2 and(byres resn arg within %s of asp1)'%(self.range.get()*5))
          cmd.select('Ligase', 'byres lys1(atp1(byres arg1(byres asp1)))')
          cmd.hide('everything')
          cmd.show('cartoon', 'all')
          cmd.color('white', 'all')
          cmd.set('cartoon_transparency', '0.6', 'all')
          cmd.show('sticks', 'Ligase')
          cpkdnaligase()
          cmd.deselect()
    
      elif 'amp1' or 'atp1' not in objects:
          
          cmd.select('asp1', 'name OD2 within %s of name NE'%(self.range.get()*5.5))
          cmd.select('arg1', 'name NE within %s of name OD2'%(self.range.get()*5.5))
          cmd.select('lys1', 'name NZ within %s of name OD2'%(self.range.get()*9))
          cmd.select('lys4', 'name NZ within %s of name NH2'%(self.range.get()*10))
          cmd.select('arg', 'byres resn arg and arg1')
          cmd.select('asp', 'byres resn asp and asp1')
          cmd.select('lys3', 'byres resn lys and lys1 and lys4')
          cmd.select('Ligase', 'byres arg(asp(lys3))')
          cmd.hide('everything')
          cmd.show('cartoon', 'all')
          cmd.color('white', 'all')
          cmd.set('cartoon_transparency', '0.6', 'all')
          cmd.show('sticks', 'Ligase')
          cpkdnaligase()
          cmd.deselect()
      cmd.orient('Ligase')
      cmd.delete('asp1')
      cmd.delete('arg1')
      cmd.delete('lys1')
      cmd.delete('arg')
      cmd.delete('asp')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys')
      cmd.delete('ratp1')
      cmd.delete('ratp2')
      cmd.delete('ratp3')
      cmd.delete('atp1')
      cmd.delete('ramp1')
      cmd.delete('ramp2')
      cmd.delete('ramp3')
      cmd.delete('lys')
      cmd.delete('amp1')

    def thymidinekinase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()

     
      cmd.select('glu1', 'name OE1 and resn glu within %s of name NH2 and resn arg'%(self.range.get()*5))
      cmd.select('glu2', 'resn glu and name OE2 within %s of name NE and resn arg'%(self.range.get()*5))
      cmd.select('glu3', 'resn glu and name OE1 within %s of name NH1 and resn arg'%(self.range.get()*6))
      cmd.select('glu4', 'resn glu and name OE1 within %s of name NE and resn arg'%(self.range.get()*6))
      cmd.select('glu5', 'resn glu and name OE2 within %s of name NH2 and resn arg'%(self.range.get()*5.5))
      cmd.select('glu6', 'resn glu and name oe1 within %s of name CZ and resn arg'%(self.range.get()*5))
      cmd.select('glu7', 'resn glu and name oe2 within %s of name CZ and resn arg'%(self.range.get()*5))
      cmd.select('glu8', 'resn glu and name oe1 within %s of name CD and resn arg'%(self.range.get()*5.8))
      cmd.select('glu9', 'resn glu and name oe2 within %s of name CD and resn arg'%(self.range.get()*5.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres resn glu')
      cmd.select('arg1', 'resn arg and name NH1 within %s of name OE2 and glu'%(self.range.get()*6))
      cmd.select('arg2', 'resn arg and name NE within %s of name OE2 and glu'%(self.range.get()*5.2))
      cmd.select('arg3', 'resn arg and name NH1 within %s of name oe1 and glu'%(self.range.get()*6))
      cmd.select('arg4', 'resn arg and name ne within %s of name oe1 and resn glu'%(self.range.get()*6.5))
      cmd.select('arg5', 'resn arg and name nh2 within %s of name oe2 and resn glu'%(self.range.get()*5.8))
      cmd.select('arg', 'byres resn arg and byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5')
      cmd.select('gly1', 'byres resn gly within %s of arg'%(self.range.get()*6.2))
      cmd.select('gly2', 'byres resn gly within %s of glu'%(self.range.get()*9))
      cmd.select('gly', 'byres resn gly and byres gly1 and byres gly2')
      cmd.select('glu10', 'byres glu within 10 of gly')
      cmd.select('arg10', 'byres arg within 9 of gly')
      cmd.select('Tkinase', 'glu10(arg10(gly))')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Tkinase')
      cpkkinase()
      cmd.deselect()
      cmd.orient('Tkinase')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg10')
      cmd.delete('arg')
      cmd.delete('gly1')
      cmd.delete('gly2')
      cmd.delete('gly')
      cmd.delete('thm1')
      cmd.delete('tmp1')
      cmd.delete('tdp1')
      cmd.delete('ttp1')

    def oglycosyl(self):
      self.update(self.p)
      checkitforthese()
      self.aset_defaults()
      delcrea()
      deletemotif()
      cmd.select('asp1', 'name od1 and resn asp within %s of (name oe1 and resn glu)'%(self.range.get()*9.5))
      cmd.select('notasp', 'resn asp within %s of resn glu'%(4.5/self.range.get()))
      cmd.select('asp', 'asp1 and (byres not notasp)')
      cmd.select('glu1', 'name oe1 and resn glu within %s of (name od1 and resn asp)'%(self.range.get()*9.5))
      cmd.select('glu0', 'resn glu within %s of resn asp'%(4.5/self.range.get()))
      cmd.select('glu', 'byres glu1 and (not glu0)')
      cmd.select('o-glycosyl', 'byres asp | byres glu')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'o-glycosyl')
      cmd.delete('tyr')
      cmd.delete('glu')
      cmd.delete('notasp')
      cmd.delete('glu1')
      cmd.delete('glu0')
      cmd.delete('asp1')
      cmd.delete('asp')
      cmd.orient('o-glycosyl')
      cpkoglycosyl()
      cmd.deselect()

    def carboncarbon(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('asp1', 'name od1 within %s of name nz'%(self.range.get()*3.5))
      cmd.select('asp2', 'resn asp within %s of name ne2'%(self.range.get()*6))
      cmd.select('asp', 'byres asp1 and byres asp2')
      cmd.select('lys1', 'name nz within %s of asp'%(self.range.get()*6))
      cmd.select('lys2', 'resn lys within %s of resn his'%(self.range.get()*8))
      cmd.select('lys', 'byres lys1 and byres lys2')
      cmd.select('his1', 'name ne2 within %s of name nz'%(self.range.get()*6))
      cmd.select('his2', 'resn his within %s of lys'%(self.range.get()*6))
      cmd.select('his3', 'resn his within %s of asp'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3')
      cmd.select('carboncarbon', 'asp(lys(his))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'carboncarbon')
      cmd.delete('his1')
      cmd.delete('lys1')
      cmd.delete('glu1')
      cmd.orient('carboncarbon')
      cpkcarboncarbon()
      cmd.deselect()
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his')
      
      
    def peroxidase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('asn1', 'name od1 within %s of name nd1'%(self.range.get()*8))
      cmd.select('asn2', 'name od1 within %s of name ne2'%(self.range.get()*6))
      cmd.select('asn3', 'name nd2 within %s of name nd1'%(self.range.get()*10))
      cmd.select('asn4', 'name nd2 within %s of name ne2'%(self.range.get()*8))
      cmd.select('asn5', 'name od1 within %s of name nh2'%(self.range.get()*7))
      cmd.select('asn6', 'name od1 within %s of name nh1'%(self.range.get()*8.6))#measure more
      cmd.select('asn7', 'name od1 within %s of name ne'%(self.range.get()*8))
      cmd.select('asn8', 'name nd2 within %s of name nh2'%(self.range.get()*9))
      cmd.select('asn9', 'name nd2 within %s of name nh1'%(self.range.get()*11))#
      cmd.select('asn10', 'name nd2 within %s of name ne'%(self.range.get()*9.8))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10')
      cmd.select('his1', 'name nd1 within %s of name od1'%(self.range.get()*5))
      cmd.select('his2','name ne2 within %s of name od1'%(self.range.get()*5))
      cmd.select('his3', 'name nd1 within %s of name nd2'%(self.range.get()*8))#
      cmd.select('his4', 'name ne2 within %s of name nd2'%(self.range.get()*8.5))#
      cmd.select('his5', 'name ne2 within %s of name ne'%(self.range.get()*5.8))
      cmd.select('his6', 'name ne2 within %s of name nh2'%(self.range.get()*6))#
      cmd.select('his7', 'name ne2 within %s of name nh1'%(self.range.get()*8.2))#
      cmd.select('his8', 'name nd1 within %s of name nh1'%(self.range.get()*7.2))#
      cmd.select('his9', 'name nd1 within %s of name nh2'%(self.range.get()*5.8))
      cmd.select('his10', 'name nd1 within %s of name ne'%(self.range.get()*7))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('arg1', 'name nh2 within %s of name od1'%(self.range.get()*7.5))
      cmd.select('arg2', 'name nh2 within %s of name nd2'%(self.range.get()*9.5))
      cmd.select('arg3', 'name nh2 within %s of name ne2'%(self.range.get()*6))#
      cmd.select('arg4', 'name nh2 within %s of name nd1'%(self.range.get()*6))
      cmd.select('arg5', 'name nh1 within %s of name od1'%(self.range.get()*8))#
      cmd.select('arg6', 'name nh1 within %s of name nd2'%(self.range.get()*10))
      cmd.select('arg7', 'name nh1 within %s of name ne2'%(self.range.get()*8))#
      cmd.select('arg8', 'name nh1 within %s of name nd1'%(self.range.get()*7.4))#
      cmd.select('arg9', 'name ne within %s of name od1'%(self.range.get()*7.2))
      cmd.select('arg10', 'name ne within %s of name nd2'%(self.range.get()*8.9))
      cmd.select('arg11', 'name ne within %s of name ne2'%(self.range.get()*5.9))
      cmd.select('arg12', 'name ne within %s of name nd1'%(self.range.get()*6))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byres arg11 and byres arg12')
      cmd.select('Peroxidase', 'asn(his(arg))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Peroxidase')
      cpkperoxidase()
      cmd.orient('Peroxidase')
      cmd.deselect()
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg12')
      cmd.delete('arg')
      
    def trioseisomerase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys4', 'name ce and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys5', 'name ce and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys6', 'name ce and resn lys within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys7', 'name cd and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*6.2))
      cmd.select('lys8', 'name cd and resn lys within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys9', 'name cd and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys10', 'name nz and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('lys11', 'name nz and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7.5))
      cmd.select('lys12', 'name nz and resn lys within %s of (name ce1 and resn his)'%(self.range.get()*6.7))
      cmd.select('lys13', 'name nz and resn lys within %s of (name cd2 and resn his)'%(self.range.get()*7.5))
      cmd.select('lys14', 'name nz and resn lys within %s of (name cg and resn his)'%(self.range.get()*8))
      cmd.select('lys15', 'name ce and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*6.2))
      cmd.select('lys16', 'name ce and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7.6))
      cmd.select('lys17', 'name ce and resn lys within %s of (name ce1 and resn his)'%(self.range.get()*6.6))
      cmd.select('lys18', 'name ce and resn lys within %s of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('lys19', 'name ce and resn lys within %s of (name cg and resn his)'%(self.range.get()*7.5))
      cmd.select('lys20', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*8.5))
      cmd.select('lys21', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*10))
      cmd.select('lys22', 'name nz and resn lys within %s of (name cd and resn glu)'%(self.range.get()*9.5))
      cmd.select('lys23', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*9))
      cmd.select('lys24', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*10.2))
      cmd.select('lys25', 'name ce and resn lys within %s of (name cd and resn glu)'%(self.range.get()*10))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14 and byres lys15 and byres lys16 and byres lys17 and byres lys18 and byres lys19 and byres lys20 and byres lys21 and byres lys22 and byres lys23 and byres lys24 and byres lys25')
      cmd.select('asn1', 'name od1 and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn2', 'name nd2 and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn3', 'name cg and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn4', 'name od1 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn6', 'name cg and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn7', 'name od1 and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.2))
      cmd.select('asn8', 'name cg and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn10', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*6.3))
      cmd.select('asn11', 'name nd2 and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*6.2))
      cmd.select('asn12', 'name nd2 and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*7.3))
      cmd.select('asn13', 'name nd2 and resn asn within %s of (name nd1 and resn his)'%(self.range.get()*8))
      cmd.select('asn14', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn15', 'name od1 and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*9.2))
      cmd.select('asn16', 'name od1 and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*8.3))
      cmd.select('asn17', 'name cg and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*7.5))
      cmd.select('asn18', 'name cg and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*8.5))
      cmd.select('asn19', 'name cg and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*7.5))
      cmd.select('asn20', 'name nd2 and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*9))
      cmd.select('asn21', 'name nd2 and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*10.5))
      cmd.select('asn22', 'name nd2 and resn asn within %s of (name cd and resn glu)'%(self.range.get()*10.2))
      cmd.select('asn23', 'name cg and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*10))
      cmd.select('asn24', 'name cg and resn asn within %s of (name cd and resn glu)'%(self.range.get()*11))
      cmd.select('asn25', 'name cg and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*11.3))
      cmd.select('asn26', 'name od1 and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*11))
      cmd.select('asn27', 'name od1 and resn asn within %s of (name cd and resn glu)'%(self.range.get()*11))
      cmd.select('asn28', 'name od1 and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*12))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11 and byres asn12 and byres asn13 and byres asn14 and byres asn15 and byres asn16 and byres asn17 and byres asn18 and byres asn19 and byres asn20 and byres asn21 and byres asn22 and byres asn23 and byres asn24 and byres asn25 and byres asn26 and byres asn27 and byres asn28')
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*8.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*10))
      cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(self.range.get()*9.5))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*9))
      cmd.select('glu5', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*10.2))
      cmd.select('glu6', 'name cd and resn glu within %s of (name ce and resn lys)'%(self.range.get()*10))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*9))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*10.5))
      cmd.select('glu9', 'name cd and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*10.2))
      cmd.select('glu10', 'name oe2 and resn glu within %s of (name cg and resn asn)'%(self.range.get()*10))
      cmd.select('glu11', 'name cd and resn glu within %s of (name cg and resn asn)'%(self.range.get()*11))
      cmd.select('glu12', 'name oe1 and resn glu within %s of (name cg and resn asn)'%(self.range.get()*11.3))
      cmd.select('glu13', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('glu14', 'name cd and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('glu15', 'name oe1 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*12))
      cmd.select('glu16', 'name oe2 and resn glu within %s of (name ne2 and resn his)'%(self.range.get()*5.6))
      cmd.select('glu17', 'name oe2 and resn glu within %s of (name cd2 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu18', 'name oe2 and resn glu within %s of (name ce1 and resn his)'%(self.range.get()*5.8))
      cmd.select('glu19', 'name oe2 and resn glu within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu20', 'name oe2 and resn glu within %s of (name cg and resn his)'%(self.range.get()*6.6))
      cmd.select('glu21', 'name oe1 and resn glu within %s of (name ne2 and resn his)'%(self.range.get()*6.6))
      cmd.select('glu22', 'name oe1 and resn glu within %s of (name cd2 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu23', 'name oe1 and resn glu within %s of (name ce1 and resn his)'%(self.range.get()*5.8))
      cmd.select('glu24', 'name oe1 and resn glu within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu25', 'name oe1 and resn glu within %s of (name cg and resn his)'%(self.range.get()*6.6))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14 and byres glu15 and byres glu16 and byres glu17 and byres glu18 and byres glu19 and byres glu20 and byres glu21 and byres glu22 and byres glu23 and byres glu24 and byres glu25')
      cmd.select('his1', 'name ne2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*6.5))
      cmd.select('his2', 'name nd1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his3', 'name ce1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*6.7))
      cmd.select('his4', 'name cd2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his5', 'name cg and resn his within %s of (name nz and resn lys)'%(self.range.get()*8))
      cmd.select('his6', 'name ne2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*6.2))
      cmd.select('his7', 'name nd1 and resn his within %s of (name ce and resn lys)'%(self.range.get()*7.6))
      cmd.select('his8', 'name ce1 and resn his within %s of (name ce and resn lys)'%(self.range.get()*6.6))
      cmd.select('his9', 'name cd2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*7))
      cmd.select('his10', 'name cg and resn his within %s of (name ce and resn lys)'%(self.range.get()*7.5))
      cmd.select('his11', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*6.3))
      cmd.select('his12', 'name cd2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*6.2))
      cmd.select('his13', 'name ce1 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*7.3))
      cmd.select('his14', 'name nd1 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his15', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*8))
      cmd.select('his16', 'name ce1 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*9.2))
      cmd.select('his17', 'name cd2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*8.3))
      cmd.select('his18', 'name ne2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('his19', 'name ce1 and resn his within %s of (name cg and resn asn)'%(self.range.get()*8.5))
      cmd.select('his20', 'name cd2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('his21', 'name ne2 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*5.6))
      cmd.select('his22', 'name cd2 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his23', 'name ce1 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*5.8))
      cmd.select('his24', 'name nd1 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his25', 'name cg and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his26', 'name ne2 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his27', 'name cd2 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his28', 'name ce1 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*5.8))
      cmd.select('his29', 'name nd1 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his30', 'name cg and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13 and byres his14 and byres his15 and byres his16 and byres his17 and byres his18 and byres his19 and byres his20 and byres his21 and byres his22 and byres his23 and byres his24 and byres his25 and byres his26 and byres his27 and byres his28 and byres his29 and byres his30')
      cmd.select('TrioseIsomerase', 'glu(his(asn(lys)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'TrioseIsomerase')
      cpktriose()
      cmd.orient('TrioseIsomerase')
      cmd.deselect()
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn12')
      cmd.delete('asn13')
      cmd.delete('asn14')
      cmd.delete('asn15')
      cmd.delete('asn16')
      cmd.delete('asn17')
      cmd.delete('asn18')
      cmd.delete('asn19')
      cmd.delete('asn20')
      cmd.delete('asn21')
      cmd.delete('asn22')
      cmd.delete('asn23')
      cmd.delete('asn24')
      cmd.delete('asn25')
      cmd.delete('asn26')
      cmd.delete('asn27')
      cmd.delete('asn28')
      cmd.delete('asn')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his14')
      cmd.delete('his15')
      cmd.delete('his16')
      cmd.delete('his17')
      cmd.delete('his18')
      cmd.delete('his19')
      cmd.delete('his20')
      cmd.delete('his21')
      cmd.delete('his22')
      cmd.delete('his23')
      cmd.delete('his24')
      cmd.delete('his25')
      cmd.delete('his26')
      cmd.delete('his27')
      cmd.delete('his28')
      cmd.delete('his29')
      cmd.delete('his30')
      cmd.delete('his')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu12')
      cmd.delete('glu13')
      cmd.delete('glu14')
      cmd.delete('glu15')
      cmd.delete('glu16')
      cmd.delete('glu17')
      cmd.delete('glu18')
      cmd.delete('glu19')
      cmd.delete('glu20')
      cmd.delete('glu21')
      cmd.delete('glu22')
      cmd.delete('glu23')
      cmd.delete('glu24')
      cmd.delete('glu25')
      cmd.delete('glu')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys14')
      cmd.delete('lys15')
      cmd.delete('lys16')
      cmd.delete('lys17')
      cmd.delete('lys18')
      cmd.delete('lys19')
      cmd.delete('lys20')
      cmd.delete('lys21')
      cmd.delete('lys22')
      cmd.delete('lys23')
      cmd.delete('lys24')
      cmd.delete('lys25')
      cmd.delete('lys')
      
      
              
    def alcoholdehyd(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('tyr1', 'name cd1 and resn tyr within %s of (name nd2 and resn asn)'%(self.range.get()*5))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asn)'%(self.range.get()*8))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name nz and resn lys)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('tyr5', 'name ce2 and resn tyr within %s of (name cg and resn lys)'%(self.range.get()*6))
      cmd.select('tyr6', 'name cg and resn tyr within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name cd1 and tyr)'%(self.range.get()*5))
      cmd.select('asn2', 'name nd2 and resn asn within %s of (name oh and tyr)'%(self.range.get()*7))
      cmd.select('asn3', 'name od1 and resn asn within %s of (name oh and tyr)'%(self.range.get()*7))
      cmd.select('asn4', 'name od1 and resn asn within %s of (name ce1 and tyr)'%(self.range.get()*6))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*5.5))
      cmd.select('asn6', 'name od1 and resn asn within %s5 of (name nz and resn lys)'%(self.range.get()*5.5))
      cmd.select('asn7', 'name nd2 and resn asn within %s of (name og and resn ser)'%(self.range.get()*10))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7')
      cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and asn)'%(self.range.get()*6))
      cmd.select('lys2', 'name ce and resn lys within %s of (name nd2 and asn)'%(self.range.get()*6.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('lys4', 'name ce and resn lys within %s of (name cz and tyr)'%(self.range.get()*6))
      cmd.select('lys4', 'name nz and resn lys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('lys5', 'name ce and resn lys within %s of (name og and resn ser)'%(self.range.get()*7))
      cmd.select('lys6', 'name cg and resn lys within %s of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys7', 'name cd and resn lys within %s of (name cb and resn ser)'%(self.range.get()*6))
      cmd.select('lys8', 'name cd and resn lys within %s of (name cb and resn asn)'%(self.range.get()*7))
      cmd.select('lys9', 'name ce and resn lys within %s of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('ser2', 'name og and resn ser within %s of (name ce2 and tyr)'%(self.range.get()*6))
      cmd.select('ser3', 'name og and resn ser within %s of (name nz and lys)'%(self.range.get()*8))
      cmd.select('ser4', 'name cb and resn ser within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('ser5', 'name cb and resn ser within %s of (name cd and lys)'%(self.range.get()*6))
      cmd.select('ser6', 'name cb and resn ser within %s of (name od1 and asn)'%(self.range.get()*10))
      cmd.select('ser7', 'name ca and resn ser within %s of (name nd2 and asn)'%(self.range.get()*10))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7')
      cmd.select('alcoholdehyd','ser(tyr(lys(asn)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'alcoholdehyd')
      cpkalcoholdehyd()
      cmd.orient('alcoholdehyd')
      cmd.deselect()
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('asn')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('lys')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys1')
      cmd.delete('ser')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')

    def aldoreductase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('lys1', 'name cd and resn lys within %s of (name cg and resn his)'%(self.range.get()*6))
      cmd.select('lys2', 'name ce and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('lys3', 'name cd and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('lys4', 'name nz and resn lys within %s of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('lys5', 'name nz and resn lys within %s of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys6', 'name cg and resn lys within %s of (name cz and resn tyr)'%(self.range.get()*8))
      cmd.select('lys7', 'name nz and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('lys8', 'name ce and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*5.5))
      cmd.select('lys9', 'name cg and resn lys within %s of (name ca and resn asp)'%(self.range.get()*9))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
      cmd.select('his1', 'name cg and resn his within %s of (name cd and resn lys)'%(self.range.get()*6))
      cmd.select('his2', 'name ne2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*8))
      cmd.select('his3', 'name nd1 and resn his within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his5', 'name ce1 and resn his within %s of (name cz and resn tyr)'%(self.range.get()*6))
      cmd.select('his6', 'name nd1 and resn his within %s of (name ce1 and resn tyr)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*10.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name cg and resn asp)'%(self.range.get()*10))
      cmd.select('his9', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys )'%(self.range.get()*5))
      cmd.select('tyr2', 'name ce2 and resn tyr within %s of (name nz and resn lys )'%(self.range.get()*6))
      cmd.select('tyr3', 'name cz and resn tyr within %s of (name cg and resn lys)'%(self.range.get()*8))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr5', 'name cz and resn tyr within %s of (name ce1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr6', 'name ce1 and resn tyr within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('tyr8', 'name cz and resn tyr within %s of (name cb and resn asp)'%(self.range.get()*9))
      cmd.select('tyr9', 'name ce2 and resn tyr within %s of (name ca and resn asp)'%(self.range.get()*8))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nz and resn lys)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name ce and resn lys)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name ca and resn asp within %s of (name cg and resn lys)'%(self.range.get()*9))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*10.5))
      cmd.select('asp5', 'name cg and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*10))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*9))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('asp8', 'name cb and resn asp within %s of (name cz and resn tyr)'%(self.range.get()*9))
      cmd.select('asp9', 'name ca and resn asp within %s of (name ce2 and resn tyr)'%(self.range.get()*8))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('aldoreductase', 'asp(his(lys(tyr)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'aldoreductase')
      cmd.orient('aldoreductase')
      cpkaldoreductase()
      cmd.deselect()
      cmd.delete('lys')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys1')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')

    def cistransisomerase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*9))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asp)'%(self.range.get()*11))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and resn asp)'%(self.range.get()*9.8))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name cb and resn asp)'%(self.range.get()*9.8))
      cmd.select('tyr5', 'name cz and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*10.2))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name od1 and resn asp)'%(self.range.get()*11.5))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr8', 'name oh and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr9', 'name oh and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr10', 'name cz and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr11', 'name cz and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.8))
      cmd.select('tyr12', 'name cz and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.3))
      cmd.select('tyr14', 'name ce1 and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr15', 'name ce1 and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr', 'byres tyr1 and byre tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13 and byres tyr14 and byres tyr15')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name oh and tyr)'%(self.range.get()*8.7))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name oh and tyr)'%(self.range.get()*10.5))
      cmd.select('asp3', 'name cg and resn asp within %s of (name oh and tyr)'%(self.range.get()*9.3))
      cmd.select('asp4', 'name cb and resn asp within %s of (name oh and tyr)'%(self.range.get()*9.3))
      cmd.select('asp5', 'name od2 and resn asp within %s of (name cz and tyr)'%(self.range.get()*10))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name cz and resn tyr)'%(self.range.get()*11.1))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name cg2 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cd1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp9', 'name od2 and resn asp within %s of (name cg1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp10', 'name cb and resn asp within %s of (name cd1 and resn ile)'%(self.range.get()*10.8))
      cmd.select('asp11', 'name cb and resn asp within %s of (name cg2 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp12', 'name cb and resn asp within %s of (name cg1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11 and byres asp12')
      cmd.select('ile1', 'name cd1 and resn ile within %s of (name oh and tyr)'%(self.range.get()*6.5))
      cmd.select('ile2', 'name cg1 and resn ile within %s of (name oh and tyr)'%(self.range.get()*6.5))
      cmd.select('ile3', 'name cg2 and resn ile within %s of (name oh and tyr)'%(self.range.get()*5.5))
      cmd.select('ile4', 'name cd1 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*6.5))
      cmd.select('ile5', 'name cg1 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*6.8))
      cmd.select('ile6', 'name cg2 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*5.5))
      cmd.select('ile7', 'name cd1 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*6.3))
      cmd.select('ile8', 'name cg1 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('ile9', 'name cg2 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*5.5))
      cmd.select('ile10', 'name cg2 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile11', 'name cd1 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile12', 'name cg1 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile13', 'name cd1 and resn ile within %s of (name cb and asp)'%(self.range.get()*11))
      cmd.select('ile14', 'name cg2 and resn ile within %s of (name cb and resn asp)'%(self.range.get()*11.5))
      cmd.select('ile15', 'name cg1 and resn ile within %s of (name cb and resn asp)'%(self.range.get()*11.5))
      cmd.select('ile', 'byres ile1 and byres ile2 and byres ile3 and byres ile4 and byres ile5 and byres ile6 and byres ile7 and byres ile8 and byres ile9 and byres ile10 and byres ile11 and byres ile12 and byres ile13 and byres ile14 and byres ile15')
      cmd.select('Cis-trans', 'ile(asp(tyr))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Cis-trans')
      cpkcistrans()
      cmd.deselect()
      cmd.orient('Cis-trans')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr2')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('tyr14')
      cmd.delete('tyr15')
      cmd.delete('tyr')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp11')
      cmd.delete('asp12')
      cmd.delete('asp')
      cmd.delete('ile1')
      cmd.delete('ile2')
      cmd.delete('ile3')
      cmd.delete('ile4')
      cmd.delete('ile5')
      cmd.delete('ile6')
      cmd.delete('ile7')
      cmd.delete('ile8')
      cmd.delete('ile9')
      cmd.delete('ile10')
      cmd.delete('ile11')
      cmd.delete('ile12')
      cmd.delete('ile13')
      cmd.delete('ile14')
      cmd.delete('ile15')
      cmd.delete('ile')
      
    def nadhbinder(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('asp1', 'name od2 and resn asp within %s of (name sg and resn cys)'%(self.range.get()*5))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name sg and resn cys)'%(self.range.get()*6.4))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*7.2))
      cmd.select('asp5', 'name cg and resn asp within %s of (name sg and resn cys)'%(self.range.get()*5.5))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('asp8', 'name od1 and resn asp within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('asp9', 'name od1 and resn asp within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('asp10', 'name cg and resn asp within %s of (name og and resn ser)'%(self.range.get()*5.3))
      cmd.select('asp11', 'name cg and resn asp within %s of (name cb and resn ser)'%(self.range.get()*6.4))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11')
      cmd.select('cys1', 'name sg and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('cys3', 'name sg and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*6.4))
      cmd.select('cys4', 'name cb and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*7.2))
      cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.4))
      cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(self.range.get()*8))
      cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*8.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('ser4', 'name cb and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn asp)'%(self.range.get()*5.3))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn asp)'%(self.range.get()*6.4))
      cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(self.range.get()*6.4))
      cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8))
      cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
      cmd.select('NAD-reductase', 'ser(asp(cys))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'NAD-reductase')
      cpknadreductase()
      cmd.deselect()
      cmd.orient('NAD-reductase')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp11')
      cmd.delete('asp')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6')
      cmd.delete('cys7')
      cmd.delete('cys8')
      cmd.delete('cys9')
      cmd.delete('cys')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser')
   

    def nadhbinder2(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('glu2', 'name oe2 and resn glu within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('glu4', 'name oe1 and resn glu within %s of (name cb and resn cys)'%(self.range.get()*7.2))
      cmd.select('glu5', 'name cg and resn glu within %s of (name sg and resn cys)'%(self.range.get()*5.5))
      cmd.select('glu6', 'name oe2 and resn glu within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('glu9', 'name oe1 and resn glu within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('glu10', 'name cg and resn glu within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('glu11', 'name cg and resn glu within %s of (name cb and resn ser)'%(self.range.get()*6.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11')
      cmd.select('cys1', 'name sg and resn cys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys3', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys4', 'name cb and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*7.5))
      cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn glu)'%(self.range.get()*5.5))
      cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.5))
      cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(self.range.get()*8))
      cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*8.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name oe2 and resn glu)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name oe2 and resn glu)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name oe1 and resn glu)'%(self.range.get()*6))
      cmd.select('ser4', 'name cb and resn ser within %s of (name oe1 and resn glu)'%(self.range.get()*7))
      cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn glu)'%(self.range.get()*5.5))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn glu)'%(self.range.get()*6.5))
      cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8))
      cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
      cmd.select('NAD-reductase2', 'ser(glu(cys))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'NAD-reductase2')
      cpknadreductase2()
      cmd.deselect()
      cmd.orient('NAD-reductase2')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6') 
      cmd.delete('cys7') 
      cmd.delete('cys8')
      cmd.delete('cys9')
      cmd.delete('cys') 
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3') 
      cmd.delete('ser4')
      cmd.delete('ser5') 
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser')

    def cephdeacetylase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*4.5))
      cmd.select('his2', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('his3', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('his4', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his5', 'name ce1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('his6', 'name ne2 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('his7', 'name ne2 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*6.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('his9', 'name ce1 and resn his within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('his10', 'name nd1 and resn his within %s of (name cb and resn ala)'%(self.range.get()*6.5))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8.5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9.5))
      cmd.select('asp3', 'name cg and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9.5))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*4.5))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5))
      cmd.select('asp6', 'name cg and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp8', 'name od1 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*6))
      cmd.select('asp9', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asp10', 'name od2 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10')
      cmd.select('ala1', 'name cb and resn ala within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('ala2', 'name cb and resn ala within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('ala3', 'name cb and resn ala within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('ala4', 'name cb and resn ala within %s of (name od2 and resn asp)'%(self.range.get()*8.5))
      cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and resn asp)'%(self.range.get()*9.5))
      cmd.select('ala6', 'name cb and resn ala within %s of (name cg and resn asp)'%(self.range.get()*9.5))
      cmd.select('ala7', 'name c and resn ala within %s of (name n and resn gln)'%(self.range.get()*2.5))
      cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
      cmd.select('gln1', 'byres resn gln within %s of his'%(self.range.get()*9.5))
      cmd.select('gln2', 'byres resn gln within %s of asp'%(self.range.get()*13.5))
      cmd.select('gln3', 'byres resn gln within %s of ala'%(self.range.get()*3))
      cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3')
      cmd.select('deacetylase', 'his(asp(ala(gln)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'deacetylase')
      cpkdeacetylase()
      cmd.deselect()
      cmd.orient('deacetylase')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp')
      cmd.delete('ala1')
      cmd.delete('ala2')
      cmd.delete('ala3')
      cmd.delete('ala4')
      cmd.delete('ala5')
      cmd.delete('ala6')
      cmd.delete('ala7')
      cmd.delete('ala')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln')
    #hyaluronate/chondroitin lyase

    def chondrolyase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s  of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('tyr3', 'name oh and resn tyr within %s  of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s  of (name ne and resn arg)'%(self.range.get()*7))
      cmd.select('tyr5', 'name oh and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*5))
      cmd.select('tyr6', 'name oh and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s  of (name ce1 and resn his)'%(self.range.get()*5))
      cmd.select('tyr8', 'name ce2 and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr9', 'name ce1 and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr11', 'name oh and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr12', 'name ce1 and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
      cmd.select('his1', 'name ne2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his2', 'name ne2 and resn his within %s  of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his3', 'name cd2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s  of (name cg and resn asn)'%(self.range.get()*8))
      cmd.select('his5', 'name ne2 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his6', 'name nd1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his7', 'name ce1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s  of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('his9', 'name ne2 and resn his within %s  of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('his10', 'name ne2 and resn his within %s  of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('his11', 'name ce1 and resn his within %s  of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('his12', 'name nd1 and resn his within %s  of (name nh1 and resn arg)'%(self.range.get()*6.5))
      cmd.select('his13', 'name nd1 and resn his within %s  of (name cd and resn arg)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
      cmd.select('arg1', 'name nh2 and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg2', 'name nh1 and resn arg within %s  of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('arg3', 'name cz and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg4', 'name ne and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh2 and resn arg within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('arg6', 'name cz and resn arg within %s  of (name ce1 and resn his)'%(self.range.get()*7))
      cmd.select('arg7', 'name nh1 and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('arg8', 'name cd and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*9))
      cmd.select('arg9', 'name nh1 and resn arg within %s  of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('arg10', 'name cz and resn arg within %s  of (name cg and resn asn)'%(self.range.get()*12))
      cmd.select('arg11', 'name nh2 and resn arg within %s  of (name nd2 and resn asn)'%(self.range.get()*11.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
      cmd.select('asn1', 'name od1 and resn asn within %s  of (name nh1 and resn arg)'%(self.range.get()*11))
      cmd.select('asn2', 'name cg and resn asn within %s  of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('asn3', 'name nd2 and resn asn within %s  of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('asn4', 'name od1 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asn5', 'name nd2 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn6', 'name od1 and resn asn within %s  of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asn7', 'name cg and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn8', 'name od1 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn10', 'name od1 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn11', 'name nd2 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')
      cmd.select('chondroitinase', 'asn(his(arg(tyr)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'chondroitinase')
      cmd.deselect()
      cpkchondro()
      cmd.orient('chondroitinase')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg')


   
    def hyaluronlyase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s  of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('tyr3', 'name oh and resn tyr within %s  of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s  of (name ne and resn arg)'%(self.range.get()*7))
      cmd.select('tyr5', 'name oh and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*5))
      cmd.select('tyr6', 'name oh and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s  of (name ce1 and resn his)'%(self.range.get()*5))
      cmd.select('tyr8', 'name ce2 and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr9', 'name ce1 and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr11', 'name oh and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr12', 'name ce1 and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
      cmd.select('his1', 'name ne2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his2', 'name ne2 and resn his within %s  of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his3', 'name cd2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s  of (name cg and resn asn)'%(self.range.get()*8))
      cmd.select('his5', 'name ne2 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his6', 'name nd1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his7', 'name ce1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s  of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('his9', 'name ne2 and resn his within %s  of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('his10', 'name ne2 and resn his within %s  of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('his11', 'name ce1 and resn his within %s  of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('his12', 'name nd1 and resn his within %s  of (name nh1 and resn arg)'%(self.range.get()*6.5))
      cmd.select('his13', 'name nd1 and resn his within %s  of (name cd and resn arg)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
      cmd.select('arg1', 'name nh2 and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg2', 'name nh1 and resn arg within %s  of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('arg3', 'name cz and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg4', 'name ne and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh2 and resn arg within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('arg6', 'name cz and resn arg within %s  of (name ce1 and resn his)'%(self.range.get()*7))
      cmd.select('arg7', 'name nh1 and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('arg8', 'name cd and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*9))
      cmd.select('arg9', 'name nh1 and resn arg within %s  of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('arg10', 'name cz and resn arg within %s  of (name cg and resn asn)'%(self.range.get()*12))
      cmd.select('arg11', 'name nh2 and resn arg within %s  of (name nd2 and resn asn)'%(self.range.get()*11.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
      cmd.select('asn1', 'name od1 and resn asn within %s  of (name nh1 and resn arg)'%(self.range.get()*11))
      cmd.select('asn2', 'name cg and resn asn within %s  of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('asn3', 'name nd2 and resn asn within %s  of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('asn4', 'name od1 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asn5', 'name nd2 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn6', 'name od1 and resn asn within %s  of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asn7', 'name cg and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn8', 'name od1 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn10', 'name od1 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn11', 'name nd2 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')

      cmd.select('Hyaluronate_Lyase', 'asn(his(arg(tyr)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Hyaluronate_Lyase')
      cmd.deselect()
      cpkhyaluron()
      cmd.orient('Hyaluronate_Lyase')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg')

    def ACTase(self):
      import tkMessageBox
      tkMessageBox.showinfo('Info', 'This motif is based on sequence not position')
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('gln', 'resi 231 and resn gln')
      cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
      cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
      cmd.select('his', 'resi 134 and resn his')
      cmd.select('lys', 'resi 84 and resn lys')
      cmd.select('ser', 'resi 80 and resn ser')
      cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'actase')
      cpkactase()
      cmd.deselect()
      cmd.orient('actase')
      cmd.delete('arg')
      cmd.delete('lys')
      cmd.delete('thr')
      cmd.delete('ser')
      cmd.delete('gln')
      cmd.delete('his')

    def ACTase2(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('gln', 'resi 231 and resn gln')
      cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
      cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
      cmd.select('his', 'resi 134 and resn his')
      cmd.select('lys', 'resi 84 and resn lys')
      cmd.select('ser', 'resi 80 and resn ser')
      cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'actase')
      cpkactase()
      cmd.deselect()
      cmd.orient('actase')
      cmd.delete('arg')
      cmd.delete('lys')
      cmd.delete('thr')
      cmd.delete('ser')
      cmd.delete('gln')
      cmd.delete('his')
      
    def exonucleaseiii(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*5.5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('his3', 'name ne2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*5.5))
      cmd.select('his4', 'name cd2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*5.5))
      cmd.select('his5', 'name nd1 and resn his within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('his6', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his9', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp4', 'name cg and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp5', 'name od2 and resn asp within %s of (name nd2 and resn asn)'%(self.range.get()*5.7))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name od1 and resn asn)'%(self.range.get()*6))
      cmd.select('asp8', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7')
      cmd.select('asp9', 'byres resn asp within %s of asp8'%(self.range.get()*5.5))
      cmd.select('asp10', 'byres resn asp within %s of his'%(self.range.get()*5.5))
      cmd.select('asp', 'byres asp8 or (byres asp9 and byres asp10)')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn2', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('asn3', 'name cg and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn4', 'name cg and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn5', 'name cg and resn asn within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('asn6', 'name nd2 and resn asn within %s of (name od2 and resn asp)'%(self.range.get()*5.7))
      cmd.select('asn7', 'name nd2 and resn asn within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('asn8', 'name od1 and resn asn within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('asn9', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8')
      cmd.select('asn10', 'byres resn asn within %s of asn9'%(self.range.get()*8))
      cmd.select('asn11', 'byres resn asn within %s of his'%(self.range.get()*8))
      cmd.select('asn12', 'byres resn asn within %s of asp8'%(self.range.get()*6))
      cmd.select('asn', 'byres asn9 or (byres asn10 and byres asn11 and byres asn12)')
      cmd.select('Exonuclease3', 'his(asp(asn))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Exonuclease3')
      cpknuclease()
      cmd.orient('Exonuclease3')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn12')
      cmd.delete('asn')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp')

    def cyclinkinase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*6.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('glu4', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu5', 'name cd and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu6', 'name oe1 and resn glu within %s of (name cd and resn lys)'%(self.range.get()*5.5))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name cg and resn lys)'%(self.range.get()*5.5))
      cmd.select('glu9', 'name oe1 and resn glu within %s of (name od1 and resn asp)'%(self.range.get()*10))
      cmd.select('glu10', 'name oe2 and resn glu within %s of (name od1 and resn asp)'%(self.range.get()*10))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10')
      cmd.select('lys1', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*7))
      cmd.select('lys3', 'name nz and resn lys within %s of (name cd and glu)'%(self.range.get()*7))
      cmd.select('lys4', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*6))
      cmd.select('lys5', 'name ce and resn lys within %s of (name cd and resn glu)'%(self.range.get()*6))
      cmd.select('lys6', 'name cd and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*5.5))
      cmd.select('lys7', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*6))
      cmd.select('lys8', 'name cg and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*5.5))
      cmd.select('lys9', 'name nz and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys10', 'name nz and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*6))
      cmd.select('lys11', 'name ce and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys12', 'name ce and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*6.5))
      cmd.select('lys13', 'name cd and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys14', 'name cd and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name oe1 and glu)'%(self.range.get()*10))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name oe2 and glu)'%(self.range.get()*10))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nz and lys)'%(self.range.get()*6))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nz and lys)'%(self.range.get()*6))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ce and lys)'%(self.range.get()*6))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name cd and resn lys)'%(self.range.get()*6))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('asp9', 'name cg and resn asp within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('Cyclin_Kinase', 'lys(asp(glu))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Cyclin_Kinase')
      cpkcyclinkinase()
      cmd.orient('Cyclin_Kinase')
      cmd.deselect()
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys14')
      cmd.delete('lys')

    def adenylatekinase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      #p-loop first
      cmd.select('lys1', 'name nz and resn lys within %s of (name n and resn gly)'%(self.range.get()*7.5))
      cmd.select('lys2', 'name cg and resn lys within %s of (name c and resn gly)'%(self.range.get()*6))
      cmd.select('lys3', 'name n and resn lys within %s of (name n and resn gly)'%(self.range.get()*5))
      cmd.select('lys4', 'name n and resn lys within %s of (resn gly)'%(self.range.get()*2))
      cmd.select('lys5', 'name c and resn lys within %s of (resn gly)'%(self.range.get()*2))  
      cmd.select('lys6', 'name nz and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*13))
      cmd.select('lys7', 'name nz and resn lys within %s of (name ne and resn arg)'%(self.range.get()*11))
      cmd.select('lys8', 'name nz and resn lys within %s of (name nh2 and resn arg)'%(self.range.get()*9.5))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8')
      cmd.select('glya1', 'name n and resn gly within %s of (name nz and lys)'%(self.range.get()*7.5))
      cmd.select('glya2', 'name ca and resn gly within %s of (name cg and lys)'%(self.range.get()*7))
      cmd.select('glya3', 'name c and resn gly within %s of (name n and lys)'%(self.range.get()*2))
      cmd.select('glya4', 'name n and resn gly within %s of (name nh1 and resn arg)'%(self.range.get()*10))
      cmd.select('glya', 'byres glya1 and byres glya2 and byres glya3 and byres glya4')
      cmd.select('glyb', 'name n and resn gly within %s of (name c and lys)'%(self.range.get()*2))
      cmd.select('p-loop', 'lys(glya(byres glyb))')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('asp4', 'name od2 and resn asp within %s of p-loop'%(self.range.get()*15))
      cmd.select('aspa', 'byres asp1 and byres asp2 and byres asp3 and byres asp4')
      cmd.select('aspb1', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('aspb2', 'name cg and resn asp within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('aspb3', 'name od1 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('aspb4', 'name od2 and resn asp within %s of (name od1 and aspa)'%(self.range.get()*7))
      cmd.select('aspb5', 'name cg and resn asp within %s of (name cg and aspa)'%(self.range.get()*7))
      cmd.select('aspb6', 'name od1 and resn asp within %s of (name od2 and aspa)'%(self.range.get()*7))
      cmd.select('asp', 'byres aspb1 and byres aspb2 and byres aspb3 and byres aspb4 and byres aspb5 and byres aspb6')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(self.range.get()*4.9))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(self.range.get()*4.9))
      cmd.select('arg', 'byres arg1 or byres arg2')
      cmd.select('adenylatekinase', 'p-loop(asp(aspa(arg)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'adenylatekinase')
      cpkadenylatekinase()
      cmd.deselect()
      cmd.orient('adenylatekinase')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys')
      cmd.delete('glya1')
      cmd.delete('glya2')
      cmd.delete('glya3')
      cmd.delete('glya4')
      cmd.delete('glya')
      cmd.delete('glyb')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('aspa')
      cmd.delete('aspb1')
      cmd.delete('aspb2')
      cmd.delete('aspb3')
      cmd.delete('aspb4')
      cmd.delete('aspb5')
      cmd.delete('aspb6')
      cmd.delete('asp')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg')
      
      
      
      
      
      
    def citratesynth(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(self.range.get()*5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('his3', 'name ce1 and resn his within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn ser)'%(self.range.get()*6.5))
      cmd.select('his5', 'name cd2 and resn his within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('his6', 'name nd1 and resn his within %s of (name og and resn ser)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*8))
      cmd.select('his8', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*8.5))
      cmd.select('his9', 'name o and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his10', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('his11', 'byres resn his within %s of his10'%(self.range.get()*8.2))
      cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his10)'%(self.range.get()*5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his10)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name ce1 and his10)'%(self.range.get()*5.5))
      cmd.select('ser4', 'name cb and resn ser within %s of (name ce1 and his10)'%(self.range.get()*6.5))
      cmd.select('ser5', 'name og and resn ser within %s of (name cd2 and his10)'%(self.range.get()*6))
      cmd.select('ser6', 'name og and resn ser within %s of (name nd1 and his10)'%(self.range.get()*7))
      cmd.select('ser7', 'name og and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*12))
      cmd.select('ser8', 'name og and resn ser within %s of (name cg and resn asp)'%(self.range.get()*12))
      cmd.select('ser9', 'name og and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*12))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
      cmd.select('his12', 'byres resn his within %s of ser'%(self.range.get()*12))
      cmd.select('asp1', 'name od2 and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp2', 'name cg and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and his10)'%(self.range.get()*8))
      cmd.select('asp5', 'name cg and resn asp within %s of (name nd1 and his10)'%(self.range.get()*8.5))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name o and his10)'%(self.range.get()*5.5))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6')
      cmd.select('his13', 'byres resn his within %s of asp'%(self.range.get()*8.5))
      cmd.select('his', 'byres his10 or (byres his11 and byres his12 and byres his13)')
      cmd.select('Citrate_Synth', 'his(asp(ser))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Citrate_Synth')
      cpkcitrate()
      cmd.orient('Citrate_Synth')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp')

      
    def tyrosinekinase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('arg3', 'name cz and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('arg4', 'name ne and resn arg within %s of (name cb and resn ala)'%(self.range.get()*6))
      cmd.select('arg5', 'name nh2 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg6', 'name nh2 and resn arg within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*6))
      cmd.select('arg8', 'name cz and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg9', 'name ne and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg10', 'name ne and resn arg within %s of (name cg and resn asp)'%(self.range.get()*6.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5.5))
      cmd.select('asp2', 'name cg and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name od2 and resn asp within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6))
      cmd.select('asp6', 'name cg and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6.5))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9))
      cmd.select('asp8', 'name o and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8))
      cmd.select('asp9', 'name cg and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('ala1', 'name cb and resn ala within %s of (name nh1 and arg)'%(self.range.get()*5))
      cmd.select('ala2', 'name cb and resn ala within %s of (name nh2 and arg)'%(self.range.get()*5.5))
      cmd.select('ala3', 'name cb and resn ala within %s of (name cz and arg)'%(self.range.get()*5.5))
      cmd.select('ala4', 'name cb and resn ala within %s of (name ne and arg)'%(self.range.get()*6))
      cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and asp)'%(self.range.get()*9))
      cmd.select('ala6', 'name cb and resn ala within %s of (name o and asp)'%(self.range.get()*8))
      cmd.select('ala7', 'name cb and resn ala within %s of (name cg and asp)'%(self.range.get()*8))
      cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
      cmd.select('SRC-Kinase', 'ala(asp(arg))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'SRC-Kinase')
      cpktyrokinase()
      cmd.orient('SRC-Kinase')
      cmd.deselect()
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')
      cmd.delete('ala1')
      cmd.delete('ala2')
      cmd.delete('ala3')
      cmd.delete('ala4')
      cmd.delete('ala5')
      cmd.delete('ala6')
      cmd.delete('ala7')
      cmd.delete('ala')

    def hhal(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*10))
      cmd.select('glu2', 'name cd and resn glu within %s of (name cb and resn cys)'%(self.range.get()*10))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name ca and resn cys)'%(self.range.get()*10))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('glu5', 'name cd and resn glu within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('glu6', 'name oe1 and resn glu within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('glu7', 'name cg and resn glu within %s of (name ca and resn phe)'%(self.range.get()*10))
      cmd.select('glu8', 'name cd and resn glu within %s of (name cb and resn phe)'%(self.range.get()*10))
      cmd.select('glu9', 'name ca and resn glu within %s of (name cd1 and resn phe)'%(self.range.get()*7.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9')
      cmd.select('cys1', 'name sg and resn cys within %s of (name nh1 and resn arg)'%(self.range.get()*6))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('cys3', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe2 and glu)'%(self.range.get()*10))
      cmd.select('cys5', 'name cb and resn cys within %s of (name cd and glu)'%(self.range.get()*10))
      cmd.select('cys6', 'name ca and resn cys within %s of (name oe1 and glu)'%(self.range.get()*10))
      cmd.select('cys7', 'name ca and resn cys within %s of (name ca and resn phe)'%(self.range.get()*8.5))
      cmd.select('cys8', 'name cb and resn cys within %s of (name cd2 and resn phe)'%(self.range.get()*9))
      cmd.select('cys9', 'name sg and resn cys within %s of (name cd1 and resn phe)'%(self.range.get()*12))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6))
      cmd.select('arg2', 'name cz and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
      cmd.select('arg3', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*8))
      cmd.select('arg4', 'name ne and resn arg within %s of (name oe2 and glu)'%(self.range.get()*5))
      cmd.select('arg5', 'name cz and resn arg within %s of (name cd and glu)'%(self.range.get()*6))
      cmd.select('arg6', 'name nh2 and resn arg within %s of (name oe1 and glu)'%(self.range.get()*5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name ce1 and resn phe)'%(self.range.get()*10.5))
      cmd.select('arg8', 'name cz and resn arg within %s of (name cz and resn phe)'%(self.range.get()*11.5))
      cmd.select('arg9', 'name nh1 and resn arg within %s of (name ce2 and resn phe)'%(self.range.get()*12))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
      cmd.select('phe1', 'name ca and resn phe within %s of (name cg and glu)'%(self.range.get()*10))
      cmd.select('phe2', 'name cb and resn phe within %s of (name cb and glu)'%(self.range.get()*10))
      cmd.select('phe3', 'name cd1 and resn phe within %s of (name ca and glu)'%(self.range.get()*7.5))
      cmd.select('phe4', 'name ce1 and resn phe within %s of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('phe5', 'name cz and resn phe within %s of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('phe6', 'name ce2 and resn phe within %s of (name nh1 and resn arg)'%(self.range.get()*12))
      cmd.select('phe7', 'name ca and resn phe within %s of (name ca and cys)'%(self.range.get()*8.5))
      cmd.select('phe8', 'name cd2 and resn phe within %s of (name cb and cys)'%(self.range.get()*9))
      cmd.select('phe9', 'name cd1 and resn phe within %s of (name sg and cys)'%(self.range.get()*12))
      cmd.select('phe', 'byres phe1 and byres phe2 and byres phe3 and byres phe4 and byres phe5 and byres phe6 and byres phe7 and byres phe8 and byres phe9')
      cmd.select('hhal', 'glu(arg(phe(cys)))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'hhal')
      cpkhhal()
      cmd.deselect()
      cmd.orient('hhal')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu')
      cmd.delete('phe')
      cmd.delete('phe1')
      cmd.delete('phe2')
      cmd.delete('phe3')
      cmd.delete('phe4')
      cmd.delete('phe5')
      cmd.delete('phe6')
      cmd.delete('phe7')
      cmd.delete('phe8')
      cmd.delete('phe9')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6')
      cmd.delete('cys7')
      cmd.delete('cys8')
      cmd.delete('cys9')

    def betainedehydrogenase(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('cys1', 'name sg and resn cys within %s of (name od1 and resn asn)'%(self.range.get()*8.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cg and resn asn)'%(self.range.get()*8.5))
      cmd.select('cys3', 'name ca and resn cys within %s of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*8))
      cmd.select('cys5', 'name cb and resn cys within %s of (name cb and resn glu)'%(self.range.get()*9))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5')
      cmd.select('glu1', 'name oe1 and resn glu within %s of (name sg and cys)'%(self.range.get()*8))
      cmd.select('glu2', 'name cb and resn glu within %s of (name cb and cys)'%(self.range.get()*9))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*13))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*14))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name oe1 and glu)'%(self.range.get()*13))
      cmd.select('asn2', 'name od1 and resn asn within %s of (name oe2 and glu)'%(self.range.get()*14))
      cmd.select('asn3', 'name od1 and resn asn within %s of (name sg and cys)'%(self.range.get()*8.5))
      cmd.select('asn4', 'name cg and resn asn within %s of (name cb and cys)'%(self.range.get()*8.5))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ca and cys)'%(self.range.get()*8.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5')
      cmd.select('betaine_dehydrogenase', 'cys(asn(glu))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'betaine_dehydrogenase')
      cpkbetaine()
      cmd.deselect()
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn')
      cmd.delete('cys')
      cmd.delete('glu')

    def serotoninacetyl(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('his3', 'name cd2 and resn his within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('his4', 'name cd2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*6))
      cmd.select('his5', 'name ne2 and resn his within %s of (name o and resn leu)'%(self.range.get()*6))
      cmd.select('his6', 'name ce1 and resn his within %s of (name cd1 and resn leu)'%(self.range.get()*10))
      cmd.select('his7', 'name ce1 and resn his within %s of (name cb and resn leu)'%(self.range.get()*9))
      cmd.select('his8', 'name nd1 and resn his within %s of (name og and resn ser)'%(self.range.get()*7.5))
      cmd.select('his9', 'name o and resn his within %s of (name oh and resn tyr)'%(self.range.get()*10))
      cmd.select('his10', 'name cb and resn his within %s of (name oh and resn tyr)'%(self.range.get()*12))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name cd2 and his)'%(self.range.get()*5.5))
      cmd.select('ser4', 'name cb and resn ser within %s of (name cd2 and his)'%(self.range.get()*6)) 
      cmd.select('ser5', 'name og and resn ser within %s of (name nd1 and his)'%(self.range.get()*7.5))
      cmd.select('ser6', 'name og and resn ser within %s of (name o and resn leu)'%(self.range.get()*5))
      cmd.select('ser7', 'name og and resn ser within %s of (name cb and resn leu)'%(self.range.get()*8))
      cmd.select('ser8', 'name cb and resn ser within %s of (name o and resn leu)'%(self.range.get()*5.5))
      cmd.select('ser9', 'name n and resn ser within %s of (name cd2 and his)'%(self.range.get()*5.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
      cmd.select('leu1', 'name o and resn leu within %s of (name ne2 and his)'%(self.range.get()*6))
      cmd.select('leu2', 'name cd1 and resn leu within %s of (name ce1 and his)'%(self.range.get()*10))
      cmd.select('leu3', 'name cb and resn leu within %s of (name ce1 and his)'%(self.range.get()*9))
      cmd.select('leu4', 'name o and resn leu within %s of (name og and ser)'%(self.range.get()*5))
      cmd.select('leu5', 'name cb and resn leu within %s of (name og and ser)'%(self.range.get()*8))
      cmd.select('leu6', 'name o and resn leu within %s of (name cb and ser)'%(self.range.get()*5.5))
      cmd.select('leu7', 'name n and resn leu within %s of (name ce1 and resn his)'%(self.range.get()*7.5))
      cmd.select('leu8', 'byres leu1 and byres leu2 and byres leu3 and byres leu4 and byres leu5 and byres leu6 and byres leu7')
      cmd.select('leu9', 'name n and resn leu within %s of (name o and his)'%(self.range.get()*7))
      cmd.select('leu10', 'name n and resn leu within %s of (name c and his)'%(self.range.get()*6.5))
      cmd.select('leu11', 'name n and resn leu within %s of (name n and his)'%(self.range.get()*8))
      cmd.select('leu12', 'name cd1 and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('leu13', 'name cb and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*5.5))
      cmd.select('leu14', 'name cg and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('leu15', 'name cd1 and resn leu within %s of (name cz and resn tyr)'%(self.range.get()*6.5))
      cmd.select('leu15b', 'name cd1 and resn leu within %s of (name ce1 and resn tyr)'%(self.range.get()*5.5))
      cmd.select('leu16', 'byres leu9 and byres leu15b and byres leu10 and byres leu11 and byres leu12 and byres leu13 and byres leu14 and byres leu15')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name cd1 and leu16)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name cb and leu16)'%(self.range.get()*6.5))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and leu16)'%(self.range.get()*7))
      cmd.select('tyr4', 'name cz and resn tyr within %s of (name cd1 and leu16)'%(self.range.get()*6.5))
      cmd.select('tyr5', 'name oh and resn tyr within %s of (name n and his)'%(self.range.get()*10))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name c and his)'%(self.range.get()*10.2))
      cmd.select('tyr7', 'name ce1 and resn tyr within %s of (name o and ser)'%(self.range.get()*16))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
      cmd.select('Serotonin_transferase', 'his(ser(leu8(leu16(tyr))))')
      cmd.hide('everything')
      cmd.show('cartoon', 'all')
      cmd.color('white', 'all')
      cmd.set('cartoon_transparency', '0.6', 'all')
      cmd.show('sticks', 'Serotonin_transferase')
      cpkseracetyl()
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser')
      cmd.delete('leu1')
      cmd.delete('leu2')
      cmd.delete('leu3')
      cmd.delete('leu4')
      cmd.delete('leu5')
      cmd.delete('leu6')
      cmd.delete('leu7')
      cmd.delete('leu8')
      cmd.delete('leu9')
      cmd.delete('leu10')
      cmd.delete('leu11')
      cmd.delete('leu12')
      cmd.delete('leu13')
      cmd.delete('leu14')
      cmd.delete('leu15')
      cmd.delete('leu15b')
      cmd.delete('leu16')
      cmd.delete('leu')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr')



        


########################################
#       MOTIF SEARCH FUNCTIONS         #
########################################
#Repeated definitions with view alterations removed to allow for quicker parsing



    def serineprotease2(self):
      deletemotif()
      cmd.select('asp1', 'resn asp within %s of resn his' %(self.range.get()*3))
      cmd.select('asp2', 'resn asp within %s of resn ser'%(self.range.get()*7))
      cmd.select('asp', 'byres asp1 and byres asp2') 
      cmd.select('his1', 'resn his within %s of asp' %(self.range.get()*4))
      cmd.select('his2', 'resn his within %s of resn ser' %(self.range.get()*4))
      cmd.select('his', 'byres his1 and byres his2') 
      cmd.select('ser1', 'name og within %s of name ne2' %(self.range.get()*3.5))
      cmd.select('ser2', 'resn ser within %s of asp' %(self.range.get()*7))
      cmd.select('ser', 'byres ser1 and byres ser2') 
      cmd.select('serineprotease', 'ser(his(asp))') 
      cmd.deselect()
      cmd.delete('asp')
      cmd.delete('his')
      cmd.delete('ser')
      cmd.delete('asp1')
      cmd.delete('his1')
      cmd.delete('ser1')
      cmd.delete('asp2')
      cmd.delete('his2')
      cmd.delete('ser2')
    def cyclinkinase2(self):
      self.update(self.p)
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*6.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('glu4', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu5', 'name cd and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu6', 'name oe1 and resn glu within %s of (name cd and resn lys)'%(self.range.get()*5.5))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*6))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name cg and resn lys)'%(self.range.get()*5.5))
      cmd.select('glu9', 'name oe1 and resn glu within %s of (name od1 and resn asp)'%(self.range.get()*10))
      cmd.select('glu10', 'name oe2 and resn glu within %s of (name od1 and resn asp)'%(self.range.get()*10))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10')
      cmd.select('lys1', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*7))
      cmd.select('lys3', 'name nz and resn lys within %s of (name cd and glu)'%(self.range.get()*7))
      cmd.select('lys4', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*6))
      cmd.select('lys5', 'name ce and resn lys within %s of (name cd and resn glu)'%(self.range.get()*6))
      cmd.select('lys6', 'name cd and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*5.5))
      cmd.select('lys7', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*6))
      cmd.select('lys8', 'name cg and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*5.5))
      cmd.select('lys9', 'name nz and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys10', 'name nz and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*6))
      cmd.select('lys11', 'name ce and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys12', 'name ce and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*6.5))
      cmd.select('lys13', 'name cd and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('lys14', 'name cd and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name oe1 and glu)'%(self.range.get()*10))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name oe2 and glu)'%(self.range.get()*10))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nz and lys)'%(self.range.get()*6))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nz and lys)'%(self.range.get()*6))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ce and lys)'%(self.range.get()*6))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name cd and resn lys)'%(self.range.get()*6))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('asp9', 'name cg and resn asp within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('Cyclin_Kinase', 'lys(asp(glu))')
      cmd.deselect()
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys')


    def Blactamase2(self):
      deletemotif()
      cmd.select('lys1', 'name nz and resn lys within %s of (name oh and resn tyr)' %(self.range.get()*5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name cz and resn tyr)' %(self.range.get()*5.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name ce1 and resn tyr)' %(self.range.get()*6.5))
      cmd.select('lys4', 'name nz and resn lys within %s of (name ce2 and resn tyr)' %(self.range.get()*6.5))
      cmd.select('lys5', 'name ce and resn lys within %s of (name oh and resn tyr)' %(self.range.get()*5))
      cmd.select('lys6', 'name ce and resn lys within %s of (name cz and resn tyr)' %(self.range.get()*6))
      cmd.select('lys7', 'name nz and resn lys within %s of (name og and resn ser)' %(self.range.get()*6))
      cmd.select('lys8', 'name nz and resn lys within %s of (name cb and resn ser)' %(self.range.get()*5.2))
      cmd.select('lys9', 'name cb and resn lys within %s of (name cb and resn ser)' %(self.range.get()*9.2))
      cmd.select('lys10', 'name ce and resn lys within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('lys11', 'name nz and resn lys within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('lys12', 'name nz and resn lys within %s of (name oe2 and resn glu)' %(self.range.get()*12.5))
      cmd.select('lys13', 'name ce and resn lys within %s of (name cd and resn glu)' %(self.range.get()*11))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*5))
      cmd.select('tyr2', 'name cz and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*5.5))
      cmd.select('tyr3', 'name ce1 and resn tyr within %s of (name nz and lys)' %(self.range.get()*6.5))
      cmd.select('tyr4', 'name ce2 and resn tyr within %s of (name nz and resn lys)' %(self.range.get()*6.5))
      cmd.select('tyr5', 'name oh and resn tyr within %s of (name ce and resn lys)' %(self.range.get()*5))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name ce and resn lys)' %(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name og and resn ser)' %(self.range.get()*6))
      cmd.select('tyr8', 'name cz and resn tyr within %s of (name og and resn ser)' %(self.range.get()*6.5))
      cmd.select('tyr9', 'name oh and resn tyr within %s of (name cb and resn ser)' %(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s of (name oe1 and resn glu)' %(self.range.get()*10))
      cmd.select('tyr11', 'name oh and resn tyr within %s of (name oe2 and resn glu)' %(self.range.get()*10))
      cmd.select('tyr12', 'name oh and resn tyr within %s of (name cd and resn glu)' %(self.range.get()*10))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12')
      cmd.select('ser1', 'name cb and resn ser within %s of (name nz and lys)' %(self.range.get()*6))
      cmd.select('ser2', 'name og and resn ser within %s of (name nz and resn lys)' %(self.range.get()*6))
      cmd.select('ser3', 'name cb and resn ser within %s of (name cb and resn lys)' %(self.range.get()*8.2))
      cmd.select('ser4', 'name og and resn ser within %s of (name cz and resn tyr)' %(self.range.get()*6.5))
      cmd.select('ser5', 'name cb and resn ser within %s of (name oh and resn tyr)' %(self.range.get()*6.5))
      cmd.select('ser6', 'name og and resn ser within %s of (name oh and tyr)' %(self.range.get()*6))
      cmd.select('ser7', 'name og and resn ser within %s of (name oe1 and resn glu)' %(self.range.get()*12))
      cmd.select('ser8', 'name og and resn ser within %s of (name oe2 and resn glu)' %(self.range.get()*12))
      cmd.select('ser9', 'name cb and resn ser within %s of (name oe1 and resn glu)' %(self.range.get()*11))
      cmd.select('ser10', 'name cb and resn ser within %s of (name oe2 and resn glu)' %(self.range.get()*12.5))
      cmd.select('ser11', 'name og and resn ser within %s of (name cd and resn glu)' %(self.range.get()*12.5))
      cmd.select('ser12', 'name cb and resn ser within %s of (name cd and resn glu)' %(self.range.get()*11.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10 and byres ser11 and byres ser12')
      cmd.select('glu1', 'name oe1 and resn glu within %s of (name ce and lys)' %(self.range.get()*8.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)' %(self.range.get()*9.5))
      cmd.select('glu3', 'name oe2 and resn glu within %s of (name nz and resn lys)' %(self.range.get()*11.2))
      cmd.select('glu4', 'name cd and resn glu within %s of (name ce and resn lys)' %(self.range.get()*10.6))
      cmd.select('glu5', 'name oe1 and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*8.7))
      cmd.select('glu6', 'name oe2 and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*9.7))
      cmd.select('glu7', 'name cd and resn glu within %s of (name oh and resn tyr)' %(self.range.get()*9.6))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and ser)' %(self.range.get()*10.5))
      cmd.select('glu9', 'name oe2 and resn glu within %s of (name og and ser)' %(self.range.get()*10.5))
      cmd.select('glu10', 'name oe1 and resn glu within %s of (name cb and resn ser)' %(self.range.get()*10))
      cmd.select('glu11', 'name oe2 and resn glu within %s of (name cb and resn ser)' %(self.range.get()*11.8))
      cmd.select('glu12', 'name cd and resn glu within %s of (name og and resn ser)' %(self.range.get()*11.8))
      cmd.select('glu13', 'name cd and resn glu within %s of (name cb and resn ser)' %(self.range.get()*11))
      cmd.select('glu14', 'name oe1 and resn glu within %s of (name cg and resn tyr)' %(self.range.get()*7.4))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14')     
      cmd.select('lactamase', 'ser(tyr(glu(lys)))')
      cmd.deselect
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr2')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser11')
      cmd.delete('ser12')
      cmd.delete('ser')
      cmd.delete('glu')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu12')
      cmd.delete('glu13')
      cmd.delete('glu14')
      cmd.deselect()

    def superoxide2(self):
      deletemotif()
      cmd.select('his1', 'byres resn his within %s of elem cu'%(self.range.get()*4))
      cmd.select('arg1', 'byres resn arg within %s of elem cu'%(self.range.get()*6))
      cmd.select('stuff', 'his1 and (byres elem zn around %s)'%(self.range.get()*4))
      cmd.select('stuff1', 'arg1 and (byres elem zn around %s)'%(self.range.get()*6))
      cmd.select('stuff2', 'byres elem cu around %s and his1'%(self.range.get()*4))
      cmd.select('stuff3', 'byres elem cu around %s and arg1'%(self.range.get()*6))
      cmd.select('stuff4', 'stuff and stuff1 and stuff2 and stuff3')
      cmd.select('superoxide', 'byres his1(arg1(stuff4))')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('arg1')
      cmd.delete('stuff')
      cmd.delete('stuff1')
      cmd.delete('stuff2')
      cmd.delete('stuff3')
      cmd.delete('stuff4')

    def metalloprotease2(self):
      deletemotif()
      cmd.select('zn', 'elem zn')
      cmd.select('metalloprotease', 'zn(byres zn around %s)'%(self.range.get()*5))
      cmd.delete('zn')
      cmd.deselect()

    def tyrophos2(self):
      self.update(self.p)
      objects = cmd.get_names('all')
      checkitforthese()
      set_defaults()
      delcrea()
      deletemotif()
      cmd.hide('everything')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(self.range.get()*6.5))
      cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
      cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name og and resn ser)'%(self.range.get()*10))
      cmd.select('arg8', 'name nh1 and resn arg within %s of (name cb and resn ser)'%(self.range.get()*11.2))
      cmd.select('arg9', 'name ne and resn arg within %s of (name ca and resn ser)'%(self.range.get()*9))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and arg)'%(self.range.get()*7))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('asp3', 'name cb and resn asp within %s of (name ne and arg)'%(self.range.get()*6.5))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name c and resn ser)'%(self.range.get()*11))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ca and resn ser)'%(self.range.get()*12))
      cmd.select('asp6', 'name cb and resn asp within %s of (name cb and resn ser)'%(self.range.get()*9.2))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(self.range.get()*12))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*11))
      cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(self.range.get()*10))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('cys1', 'name ca and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys3', 'name sg and resn cys within %s of (name ca and resn ser)'%(self.range.get()*6))
      cmd.select('cys4', 'name c and resn cys within %s of (name od1 and asp)'%(self.range.get()*12))
      cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and asp)'%(self.range.get()*11))
      cmd.select('cys6', 'name sg and resn cys within %s of (name cb and asp)'%(self.range.get()*10))
      cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and arg)'%(self.range.get()*7))
      cmd.select('cys9', 'name sg and resn cys within %s of (name ne and arg)'%(self.range.get()*6.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name nh2 and arg)'%(self.range.get()*10))
      cmd.select('ser2', 'name cb and resn ser within %s of (name nh1 and arg)'%(self.range.get()*11.2))
      cmd.select('ser3', 'name ca and resn ser within %s of (name ne and arg)'%(self.range.get()*9))
      cmd.select('ser4', 'name c and resn ser within %s of (name od2 and asp)'%(self.range.get()*11))
      cmd.select('ser5', 'name ca and resn ser within %s of (name od1 and asp)'%(self.range.get()*12))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cb and asp)'%(self.range.get()*9.2))
      cmd.select('ser7', 'name og and resn ser within %s of (name ca and cys)'%(self.range.get()*6.5))
      cmd.select('ser8', 'name cb and resn ser within %s of (name cb and cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name ca and resn ser within %s of (name sg and cys)'%(self.range.get()*6))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')      
      cmd.select('tyrophos', 'ser(asp(arg(cys)))')
      tycount = cmd.index('tyrophos')
      atcount  = len(tycount)
      if(atcount < 1):
        cmd.hide('everything')
        cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*7))
        cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*7))
        cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(self.range.get()*6.5))
        cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*7))
        cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
        cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6.5))
        cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6')
        cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(self.range.get()*7))
        cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*7))
        cmd.select('asp3', 'name cb and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6.5))
        cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(self.range.get()*12))
        cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*11))
        cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(self.range.get()*10))
        cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp7 and byres asp8 and byres asp9')
        cmd.select('cys4', 'name c and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*12))
        cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*11))
        cmd.select('cys6', 'name sg and resn cys within %s of (name cb and resn asp)'%(self.range.get()*10))
        cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(self.range.get()*7))
        cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and resn arg)'%(self.range.get()*7))
        cmd.select('cys9', 'name sg and resn cys within %s of (name ne and resn arg)'%(self.range.get()*6.5))
        cmd.select('cys', 'byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
        cmd.select('tyrophos', '(asp(arg(cys)))')
        cmd.delete('arg')
        cmd.delete('arg1')
        cmd.delete('arg2')
        cmd.delete('arg3')
        cmd.delete('arg4')
        cmd.delete('arg5')
        cmd.delete('arg6')
        cmd.delete('arg7')
        cmd.delete('arg8')
        cmd.delete('arg9')    
        cmd.delete('ser')
        cmd.delete('ser1')
        cmd.delete('ser2')
        cmd.delete('ser3')
        cmd.delete('ser4')
        cmd.delete('ser5')
        cmd.delete('ser6')
        cmd.delete('ser7')
        cmd.delete('ser8')
        cmd.delete('ser9')
        cmd.delete('asp')
        cmd.delete('asp1')
        cmd.delete('asp2')
        cmd.delete('asp3')
        cmd.delete('asp4')
        cmd.delete('asp5')
        cmd.delete('asp6')
        cmd.delete('asp7')
        cmd.delete('asp8')
        cmd.delete('asp9') 
        cmd.delete('cys')
        cmd.delete('cys1')
        cmd.delete('cys2')
        cmd.delete('cys3')
        cmd.delete('cys4')
        cmd.delete('cys5')
        cmd.delete('cys6')
        cmd.delete('cys7')
        cmd.delete('cys8')
        cmd.delete('cys9')
        cmd.orient('tyrophos')
        cmd.deselect()
      else:
        cmd.delete('arg')
        cmd.delete('arg1')
        cmd.delete('arg2')
        cmd.delete('arg3')
        cmd.delete('arg4')
        cmd.delete('arg5')
        cmd.delete('arg6')
        cmd.delete('arg7')
        cmd.delete('arg8')
        cmd.delete('arg9')    
        cmd.delete('ser')
        cmd.delete('ser1')
        cmd.delete('ser2')
        cmd.delete('ser3')
        cmd.delete('ser4')
        cmd.delete('ser5')
        cmd.delete('ser6')
        cmd.delete('ser7')
        cmd.delete('ser8')
        cmd.delete('ser9')
        cmd.delete('asp')
        cmd.delete('asp1')
        cmd.delete('asp2')
        cmd.delete('asp3')
        cmd.delete('asp4')
        cmd.delete('asp5')
        cmd.delete('asp6')
        cmd.delete('asp7')
        cmd.delete('asp8')
        cmd.delete('asp9') 
        cmd.delete('cys')
        cmd.delete('cys1')
        cmd.delete('cys2')
        cmd.delete('cys3')
        cmd.delete('cys4')
        cmd.delete('cys5')
        cmd.delete('cys6')
        cmd.delete('cys7')
        cmd.delete('cys8')
        cmd.delete('cys9')
        cmd.orient('tyrophos')
        cmd.deselect()

    def carbanhyd2(self):
      deletemotif()
      cmd.select('zn', 'elem zn')
      cmd.select('his', 'resn his within %s of zn'%(self.range.get()*5))
      cmd.select('carbonicanhydrase', 'byres his or zn')
      cmd.delete('zn')
      cmd.delete('his')
      cmd.deselect()

    def betainedehydrogenase2(self):
      deletemotif()
      cmd.select('cys1', 'name sg and resn cys within %s of (name od1 and resn asn)'%(self.range.get()*8.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cg and resn asn)'%(self.range.get()*8.5))
      cmd.select('cys3', 'name ca and resn cys within %s of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*8))
      cmd.select('cys5', 'name cb and resn cys within %s of (name cb and resn glu)'%(self.range.get()*9))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5')
      cmd.select('glu1', 'name oe1 and resn glu within %s of (name sg and cys)'%(self.range.get()*8))
      cmd.select('glu2', 'name cb and resn glu within %s of (name cb and cys)'%(self.range.get()*9))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*13))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*14))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name oe1 and glu)'%(self.range.get()*13))
      cmd.select('asn2', 'name od1 and resn asn within %s of (name oe2 and glu)'%(self.range.get()*14))
      cmd.select('asn3', 'name od1 and resn asn within %s of (name sg and cys)'%(self.range.get()*8.5))
      cmd.select('asn4', 'name cg and resn asn within %s of (name cb and cys)'%(self.range.get()*8.5))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ca and cys)'%(self.range.get()*8.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5')
      cmd.select('betaine_dehydrogenase', 'cys(asn(glu))')
      cmd.deselect()
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn')
      cmd.delete('cys')
      cmd.delete('glu')

    def paplike2(self):
      deletemotif()
      cmd.select('gln1', 'name ne2 and resn gln within %s of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('gln2', 'name cd and resn gln within %s of (name ce1 and resn his)'%(self.range.get()*6.7))
      cmd.select('gln3', 'name oe1 and resn gln within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('gln4', 'name ne2 and resn gln within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('gln5', 'name oe1 and resn gln within %s of (name sg and resn cys)'%(self.range.get()*6.7))
      cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3 and byres gln4 and byres gln5')
      cmd.select('his1', 'name ne2 and resn his within %s of (name ne2 and gln)'%(self.range.get()*7))
      cmd.select('his2', 'name ce1 and resn his within %s of (name cd and gln)'%(self.range.get()*6.7))
      cmd.select('his3', 'name nd1 and resn his within %s of (name oe1 and gln)'%(self.range.get()*7))
      cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn cys)'%(self.range.get()*5.7))
      cmd.select('his5', 'name nd1 and resn his within %s of (name sg and resn cys)'%(self.range.get()*6))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5')
      cmd.select('cys1', 'name cb and resn cys within %s of (name ce1 and his)'%(self.range.get()*5.7))
      cmd.select('cys2', 'name sg and resn cys within %s of (name nd1 and his)'%(self.range.get()*6))
      cmd.select('cys3', 'name cb and resn cys within %s of (name ne2 and gln)'%(self.range.get()*5.5))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and gln)'%(self.range.get()*6.7))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4')
      cmd.select('paplike', 'gln(his(cys))')
      cmd.delete('his')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('gln')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln4')
      cmd.delete('gln5')
      cmd.orient('paplike')
      cmd.deselect()

    def zincfinger2(self):
          deletemotif()
          cmd.select('zn1', 'elem zn')        
          xm = cmd.index('zn1')
          nm  = len(xm)
          if(nm < 1):
              cmd.delete('zn1')
          objects = cmd.get_names('all')
          if 'zn1' in objects:
              cmd.select('zn1', 'elem zn')
              cmd.select('his', 'resn his')
              cmd.select('cys', 'resn cys')
              cmd.select('cys1', 'resn cys around %s'%(self.range.get()*4))
              cmd.select('Zinc_finger', '(resn cys or resn his(and byres cys1))')
              cmd.delete('zn1')
              cmd.delete('his')
              cmd.delete('cys')
              cmd.delete('cys1')
              cmd.deselect()
          
    def aminotransferase2(self):
      deletemotif()
      cmd.select('asp1', 'name od1 and resn asp within %s of (name cb and resn his)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name cg and resn his)'%(self.range.get()*6))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('asp4', 'name cg and resn asp within %s of (name cb and resn his)'%(self.range.get()*6.5))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name nz and resn lys)'%(self.range.get()*9))
      cmd.select('asp8', 'name cg and resn asp within %s of (name nz and resn lys)'%(self.range.get()*9))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp8')
      cmd.select('his1', 'name cb and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('his2', 'name cg and resn his within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('his3', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('his4', 'name cb and resn his within %s of (name cg and asp)'%(self.range.get()*6.5))
      cmd.select('his5', 'name ne2 and resn his within %s of (name od1 and asp)'%(self.range.get()*8))
      cmd.select('his6', 'name cd2 and resn his within %s of (name od1 and asp)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*8))
      cmd.select('his9', 'name ce1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('lys1', 'name nz and resn lys within %s of (name od2 and asp)'%(self.range.get()*9))
      cmd.select('lys2', 'name nz and resn lys within %s of (name cg and asp)'%(self.range.get()*9))
      cmd.select('lys3', 'name nz and resn lys within %s of (name nd1 and his)'%(self.range.get()*7.5))
      cmd.select('lys4', 'name nz and resn lys within %s of (name ne2 and his)'%(self.range.get()*8))
      cmd.select('lys5', 'name nz and resn lys within %s of (name ce1 and his)'%(self.range.get()*7))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5')
      cmd.select('Aminotransferase', 'asp(his(lys))')
      cmd.deselect()
      cmd.delete('his')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('lys')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('asp')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')


    def fisomerase2(self):
      deletemotif()
      cmd.select('his', 'elem mn around %s(elem mn)'%(self.range.get()*5))
      cmd.select('fucoseisomerase', 'byres resn asp and his(byres resn glu and his(elem mn))')
      cmd.deselect()
      cmd.delete('his')

    def glutamine_amidotransferase2(self):
      deletemotif()
      cmd.select('his1', 'name ND1 within %s of name OE2'%(self.range.get()*3))
      cmd.select('his2', 'name NE2 within %s of name SG'%(self.range.get()*3.5))
      cmd.select('his', 'byres his1 and byres his2')
      cmd.select('glu1', 'resn glu within %s of his'%(self.range.get()*3.2))
      cmd.select('glu2', 'resn glu within %s of resn cys'%(self.range.get()*7))
      cmd.select('glu', 'byres glu1 and byres glu2')
      cmd.select('cys1', 'resn cys within %s of his'%(self.range.get()*3.5))
      cmd.select('cys2', 'resn cys within %s of glu'%(self.range.get()*7))
      cmd.select('cys', 'byres cys1 and byres cys2')
      cmd.select('glu_amidotransferase', 'cys(his(glu))')
      cmd.deselect()
      cmd.delete('his')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('glu')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')

    def dnaligase2(self):
      deletemotif()
      cmd.select('amp1', 'resn amp')
      cmd.select('atp1', 'resn atp')
      xp = cmd.index('amp1')
      np  = len(xp)
      if(np < 1):
          cmd.delete('amp1')
      xtp = cmd.index('atp1')
      ntp  = len(xtp)
      if(ntp < 1):
          cmd.delete('atp1')
      objects = cmd.get_names('all')
      if 'amp1' in objects:
          cmd.select('ramp1', 'byres resn amp around %s'%(self.range.get()*7.4))
          cmd.select('lys1', 'byres resn lys and ramp1')
          cmd.select('ramp2', 'byres resn amp around %s'%(self.range.get()*7))
          
          cmd.select('ramp3', 'byres resn amp around %s'%(self.range.get()*5.3))
          cmd.select('asp1', 'ramp3 and(byres resn asp within %s of lys1)'%(self.range.get()*3))
          cmd.select('arg1', 'ramp2 and(byres resn arg within %s of asp1)'%(self.range.get()*5))
          cmd.select('Ligase', 'byres lys1(amp1(byres arg1(byres asp1)))')
          cmd.deselect()
      elif 'atp1' in objects:
          cmd.select('ratp1', 'byres resn atp around %s'%(self.range.get()*7.4))
          cmd.select('lys1', 'byres resn lys and ratp1')
          cmd.select('ratp2', 'byres resn atp around %s'%(self.range.get()*7))
          
          cmd.select('ratp3', 'byres resn atp around %s'%(self.range.get()*5.3))
          cmd.select('asp1', 'ratp3 and(byres resn asp within %s of lys1)'%(self.range.get()*3))
          cmd.select('arg1', 'ratp2 and(byres resn arg within %s of asp1)'%(self.range.get()*5))
          cmd.select('Ligase', 'byres lys1(atp1(byres arg1(byres asp1)))')
          cmd.deselect()
    
      elif 'amp1' or 'atp1' not in objects:
          
          cmd.select('asp1', 'name OD2 within %s of name NE'%(self.range.get()*5.5))
          cmd.select('arg1', 'name NE within %s of name OD2'%(self.range.get()*5.5))
          cmd.select('lys1', 'name NZ within %s of name OD2'%(self.range.get()*9))
          cmd.select('lys4', 'name NZ within %s of name NH2'%(self.range.get()*10))
          cmd.select('arg', 'byres resn arg and arg1')
          cmd.select('asp', 'byres resn asp and asp1')
          cmd.select('lys3', 'byres resn lys and lys1 and lys4')
          cmd.select('Ligase', 'byres arg(asp(lys3))')
          cmd.deselect()
      cmd.orient('Ligase')
      cmd.delete('asp1')
      cmd.delete('arg1')
      cmd.delete('lys1')
      cmd.delete('arg')
      cmd.delete('asp')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys')
      cmd.delete('ratp1')
      cmd.delete('ratp2')
      cmd.delete('ratp3')
      cmd.delete('atp1')
      cmd.delete('ramp1')
      cmd.delete('ramp2')
      cmd.delete('ramp3')
      cmd.delete('lys')
      cmd.delete('amp1')

    def thymidinekinase2(self):
      deletemotif()
      cmd.select('glu1', 'name OE1 and resn glu within %s of name NH2 and resn arg'%(self.range.get()*5))
      cmd.select('glu2', 'resn glu and name OE2 within %s of name NE and resn arg'%(self.range.get()*5))
      cmd.select('glu3', 'resn glu and name OE1 within %s of name NH1 and resn arg'%(self.range.get()*6))
      cmd.select('glu4', 'resn glu and name OE1 within %s of name NE and resn arg'%(self.range.get()*6))
      cmd.select('glu5', 'resn glu and name OE2 within %s of name NH2 and resn arg'%(self.range.get()*5.5))
      cmd.select('glu6', 'resn glu and name oe1 within %s of name CZ and resn arg'%(self.range.get()*5))
      cmd.select('glu7', 'resn glu and name oe2 within %s of name CZ and resn arg'%(self.range.get()*5))
      cmd.select('glu8', 'resn glu and name oe1 within %s of name CD and resn arg'%(self.range.get()*5.8))
      cmd.select('glu9', 'resn glu and name oe2 within %s of name CD and resn arg'%(self.range.get()*5.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres resn glu')
      cmd.select('arg1', 'resn arg and name NH1 within %s of name OE2 and glu'%(self.range.get()*6))
      cmd.select('arg2', 'resn arg and name NE within %s of name OE2 and glu'%(self.range.get()*5.2))
      cmd.select('arg3', 'resn arg and name NH1 within %s of name oe1 and glu'%(self.range.get()*6))
      cmd.select('arg4', 'resn arg and name ne within %s of name oe1 and resn glu'%(self.range.get()*6.5))
      cmd.select('arg5', 'resn arg and name nh2 within %s of name oe2 and resn glu'%(self.range.get()*5.8))
      cmd.select('arg', 'byres resn arg and byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5')
      cmd.select('gly1', 'byres resn gly within %s of arg'%(self.range.get()*6.2))
      cmd.select('gly2', 'byres resn gly within %s of glu'%(self.range.get()*9))
      cmd.select('gly', 'byres resn gly and byres gly1 and byres gly2')
      cmd.select('glu10', 'byres glu within 10 of gly')
      cmd.select('arg10', 'byres arg within 9 of gly')
      cmd.select('Tkinase', 'glu10(arg10(gly))')
      cmd.deselect()
      cmd.orient('Tkinase')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg10')
      cmd.delete('arg')
      cmd.delete('gly1')
      cmd.delete('gly2')
      cmd.delete('gly')
      cmd.delete('thm1')
      cmd.delete('tmp1')
      cmd.delete('tdp1')
      cmd.delete('ttp1')

    def oglycosyl2(self):
      deletemotif()
      cmd.select('tyr', 'name oh within %s of name oe1'%(self.range.get()*3.5))
      cmd.select('glu', 'resn glu within %s of tyr'%(self.range.get()*8))
      cmd.select('o-glycosyl', 'byres tyr or byres glu')
      cmd.delete('tyr')
      cmd.delete('glu')
      cmd.deselect()

    def carboncarbon2(self):
      deletemotif()
      cmd.select('asp1', 'name od1 within %s of name nz'%(self.range.get()*3.5))
      cmd.select('asp2', 'resn asp within %s of name ne2'%(self.range.get()*6))
      cmd.select('asp', 'byres asp1 and byres asp2')
      cmd.select('lys1', 'name nz within %s of asp'%(self.range.get()*6))
      cmd.select('lys2', 'resn lys within %s of resn his'%(self.range.get()*8))
      cmd.select('lys', 'byres lys1 and byres lys2')
      cmd.select('his1', 'name ne2 within %s of name nz'%(self.range.get()*6))
      cmd.select('his2', 'resn his within %s of lys'%(self.range.get()*6))
      cmd.select('his3', 'resn his within %s of asp'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3')
      cmd.select('carboncarbon', 'asp(lys(his))')
      cmd.delete('his1')
      cmd.delete('lys1')
      cmd.delete('glu1')
      cmd.deselect()
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his')
      
      
    def peroxidase2(self):
      deletemotif()
      cmd.select('asn1', 'name od1 within %s of name nd1'%(self.range.get()*8))
      cmd.select('asn2', 'name od1 within %s of name ne2'%(self.range.get()*6))
      cmd.select('asn3', 'name nd2 within %s of name nd1'%(self.range.get()*10))
      cmd.select('asn4', 'name nd2 within %s of name ne2'%(self.range.get()*8))
      cmd.select('asn5', 'name od1 within %s of name nh2'%(self.range.get()*7))
      cmd.select('asn6', 'name od1 within %s of name nh1'%(self.range.get()*8.6))#measure more
      cmd.select('asn7', 'name od1 within %s of name ne'%(self.range.get()*8))
      cmd.select('asn8', 'name nd2 within %s of name nh2'%(self.range.get()*9))
      cmd.select('asn9', 'name nd2 within %s of name nh1'%(self.range.get()*11))#
      cmd.select('asn10', 'name nd2 within %s of name ne'%(self.range.get()*9.8))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10')
      cmd.select('his1', 'name nd1 within %s of name od1'%(self.range.get()*5))
      cmd.select('his2','name ne2 within %s of name od1'%(self.range.get()*5))
      cmd.select('his3', 'name nd1 within %s of name nd2'%(self.range.get()*8))#
      cmd.select('his4', 'name ne2 within %s of name nd2'%(self.range.get()*8.5))#
      cmd.select('his5', 'name ne2 within %s of name ne'%(self.range.get()*5.8))
      cmd.select('his6', 'name ne2 within %s of name nh2'%(self.range.get()*6))#
      cmd.select('his7', 'name ne2 within %s of name nh1'%(self.range.get()*8.2))#
      cmd.select('his8', 'name nd1 within %s of name nh1'%(self.range.get()*7.2))#
      cmd.select('his9', 'name nd1 within %s of name nh2'%(self.range.get()*5.8))
      cmd.select('his10', 'name nd1 within %s of name ne'%(self.range.get()*7))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('arg1', 'name nh2 within %s of name od1'%(self.range.get()*7.5))
      cmd.select('arg2', 'name nh2 within %s of name nd2'%(self.range.get()*9.5))
      cmd.select('arg3', 'name nh2 within %s of name ne2'%(self.range.get()*6))#
      cmd.select('arg4', 'name nh2 within %s of name nd1'%(self.range.get()*6))
      cmd.select('arg5', 'name nh1 within %s of name od1'%(self.range.get()*8))#
      cmd.select('arg6', 'name nh1 within %s of name nd2'%(self.range.get()*10))
      cmd.select('arg7', 'name nh1 within %s of name ne2'%(self.range.get()*8))#
      cmd.select('arg8', 'name nh1 within %s of name nd1'%(self.range.get()*7.4))#
      cmd.select('arg9', 'name ne within %s of name od1'%(self.range.get()*7.2))
      cmd.select('arg10', 'name ne within %s of name nd2'%(self.range.get()*8.9))
      cmd.select('arg11', 'name ne within %s of name ne2'%(self.range.get()*5.9))
      cmd.select('arg12', 'name ne within %s of name nd1'%(self.range.get()*6))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byres arg11 and byres arg12')
      cmd.select('Peroxidase', 'asn(his(arg))')
      cmd.deselect()
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg12')
      cmd.delete('arg')
      
    def trioseisomerase2(self):
      deletemotif()
      cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys2', 'name nz and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('lys4', 'name ce and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys5', 'name ce and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys6', 'name ce and resn lys within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys7', 'name cd and resn lys within %s of (name od1 and resn asn)'%(self.range.get()*6.2))
      cmd.select('lys8', 'name cd and resn lys within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys9', 'name cd and resn lys within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('lys10', 'name nz and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('lys11', 'name nz and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7.5))
      cmd.select('lys12', 'name nz and resn lys within %s of (name ce1 and resn his)'%(self.range.get()*6.7))
      cmd.select('lys13', 'name nz and resn lys within %s of (name cd2 and resn his)'%(self.range.get()*7.5))
      cmd.select('lys14', 'name nz and resn lys within %s of (name cg and resn his)'%(self.range.get()*8))
      cmd.select('lys15', 'name ce and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*6.2))
      cmd.select('lys16', 'name ce and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7.6))
      cmd.select('lys17', 'name ce and resn lys within %s of (name ce1 and resn his)'%(self.range.get()*6.6))
      cmd.select('lys18', 'name ce and resn lys within %s of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('lys19', 'name ce and resn lys within %s of (name cg and resn his)'%(self.range.get()*7.5))
      cmd.select('lys20', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*8.5))
      cmd.select('lys21', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*10))
      cmd.select('lys22', 'name nz and resn lys within %s of (name cd and resn glu)'%(self.range.get()*9.5))
      cmd.select('lys23', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(self.range.get()*9))
      cmd.select('lys24', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(self.range.get()*10.2))
      cmd.select('lys25', 'name ce and resn lys within %s of (name cd and resn glu)'%(self.range.get()*10))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14 and byres lys15 and byres lys16 and byres lys17 and byres lys18 and byres lys19 and byres lys20 and byres lys21 and byres lys22 and byres lys23 and byres lys24 and byres lys25')
      cmd.select('asn1', 'name od1 and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn2', 'name nd2 and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn3', 'name cg and resn asn within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('asn4', 'name od1 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn6', 'name cg and resn asn within %s of (name ce and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn7', 'name od1 and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.2))
      cmd.select('asn8', 'name cg and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s of (name cd and resn lys)'%(self.range.get()*6.5))
      cmd.select('asn10', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*6.3))
      cmd.select('asn11', 'name nd2 and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*6.2))
      cmd.select('asn12', 'name nd2 and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*7.3))
      cmd.select('asn13', 'name nd2 and resn asn within %s of (name nd1 and resn his)'%(self.range.get()*8))
      cmd.select('asn14', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn15', 'name od1 and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*9.2))
      cmd.select('asn16', 'name od1 and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*8.3))
      cmd.select('asn17', 'name cg and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*7.5))
      cmd.select('asn18', 'name cg and resn asn within %s of (name ce1 and resn his)'%(self.range.get()*8.5))
      cmd.select('asn19', 'name cg and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*7.5))
      cmd.select('asn20', 'name nd2 and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*9))
      cmd.select('asn21', 'name nd2 and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*10.5))
      cmd.select('asn22', 'name nd2 and resn asn within %s of (name cd and resn glu)'%(self.range.get()*10.2))
      cmd.select('asn23', 'name cg and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*10))
      cmd.select('asn24', 'name cg and resn asn within %s of (name cd and resn glu)'%(self.range.get()*11))
      cmd.select('asn25', 'name cg and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*11.3))
      cmd.select('asn26', 'name od1 and resn asn within %s of (name oe2 and resn glu)'%(self.range.get()*11))
      cmd.select('asn27', 'name od1 and resn asn within %s of (name cd and resn glu)'%(self.range.get()*11))
      cmd.select('asn28', 'name od1 and resn asn within %s of (name oe1 and resn glu)'%(self.range.get()*12))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11 and byres asn12 and byres asn13 and byres asn14 and byres asn15 and byres asn16 and byres asn17 and byres asn18 and byres asn19 and byres asn20 and byres asn21 and byres asn22 and byres asn23 and byres asn24 and byres asn25 and byres asn26 and byres asn27 and byres asn28')
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*8.5))
      cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(self.range.get()*10))
      cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(self.range.get()*9.5))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*9))
      cmd.select('glu5', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(self.range.get()*10.2))
      cmd.select('glu6', 'name cd and resn glu within %s of (name ce and resn lys)'%(self.range.get()*10))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*9))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*10.5))
      cmd.select('glu9', 'name cd and resn glu within %s of (name nd2 and resn asn)'%(self.range.get()*10.2))
      cmd.select('glu10', 'name oe2 and resn glu within %s of (name cg and resn asn)'%(self.range.get()*10))
      cmd.select('glu11', 'name cd and resn glu within %s of (name cg and resn asn)'%(self.range.get()*11))
      cmd.select('glu12', 'name oe1 and resn glu within %s of (name cg and resn asn)'%(self.range.get()*11.3))
      cmd.select('glu13', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('glu14', 'name cd and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('glu15', 'name oe1 and resn glu within %s of (name od1 and resn asn)'%(self.range.get()*12))
      cmd.select('glu16', 'name oe2 and resn glu within %s of (name ne2 and resn his)'%(self.range.get()*5.6))
      cmd.select('glu17', 'name oe2 and resn glu within %s of (name cd2 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu18', 'name oe2 and resn glu within %s of (name ce1 and resn his)'%(self.range.get()*5.8))
      cmd.select('glu19', 'name oe2 and resn glu within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu20', 'name oe2 and resn glu within %s of (name cg and resn his)'%(self.range.get()*6.6))
      cmd.select('glu21', 'name oe1 and resn glu within %s of (name ne2 and resn his)'%(self.range.get()*6.6))
      cmd.select('glu22', 'name oe1 and resn glu within %s of (name cd2 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu23', 'name oe1 and resn glu within %s of (name ce1 and resn his)'%(self.range.get()*5.8))
      cmd.select('glu24', 'name oe1 and resn glu within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('glu25', 'name oe1 and resn glu within %s of (name cg and resn his)'%(self.range.get()*6.6))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14 and byres glu15 and byres glu16 and byres glu17 and byres glu18 and byres glu19 and byres glu20 and byres glu21 and byres glu22 and byres glu23 and byres glu24 and byres glu25')
      cmd.select('his1', 'name ne2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*6.5))
      cmd.select('his2', 'name nd1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his3', 'name ce1 and resn his within %s of (name nz and resn lys)'%(self.range.get()*6.7))
      cmd.select('his4', 'name cd2 and resn his within %s of (name nz and resn lys)'%(self.range.get()*7.5))
      cmd.select('his5', 'name cg and resn his within %s of (name nz and resn lys)'%(self.range.get()*8))
      cmd.select('his6', 'name ne2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*6.2))
      cmd.select('his7', 'name nd1 and resn his within %s of (name ce and resn lys)'%(self.range.get()*7.6))
      cmd.select('his8', 'name ce1 and resn his within %s of (name ce and resn lys)'%(self.range.get()*6.6))
      cmd.select('his9', 'name cd2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*7))
      cmd.select('his10', 'name cg and resn his within %s of (name ce and resn lys)'%(self.range.get()*7.5))
      cmd.select('his11', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*6.3))
      cmd.select('his12', 'name cd2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*6.2))
      cmd.select('his13', 'name ce1 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*7.3))
      cmd.select('his14', 'name nd1 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his15', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*8))
      cmd.select('his16', 'name ce1 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*9.2))
      cmd.select('his17', 'name cd2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*8.3))
      cmd.select('his18', 'name ne2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('his19', 'name ce1 and resn his within %s of (name cg and resn asn)'%(self.range.get()*8.5))
      cmd.select('his20', 'name cd2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*7.5))
      cmd.select('his21', 'name ne2 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*5.6))
      cmd.select('his22', 'name cd2 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his23', 'name ce1 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*5.8))
      cmd.select('his24', 'name nd1 and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his25', 'name cg and resn his within %s of (name oe2 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his26', 'name ne2 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his27', 'name cd2 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his28', 'name ce1 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*5.8))
      cmd.select('his29', 'name nd1 and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('his30', 'name cg and resn his within %s of (name oe1 and resn glu)'%(self.range.get()*6.6))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13 and byres his14 and byres his15 and byres his16 and byres his17 and byres his18 and byres his19 and byres his20 and byres his21 and byres his22 and byres his23 and byres his24 and byres his25 and byres his26 and byres his27 and byres his28 and byres his29 and byres his30')
      cmd.select('TrioseIsomerase', 'glu(his(asn(lys)))')
      cmd.deselect()
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn12')
      cmd.delete('asn13')
      cmd.delete('asn14')
      cmd.delete('asn15')
      cmd.delete('asn16')
      cmd.delete('asn17')
      cmd.delete('asn18')
      cmd.delete('asn19')
      cmd.delete('asn20')
      cmd.delete('asn21')
      cmd.delete('asn22')
      cmd.delete('asn23')
      cmd.delete('asn24')
      cmd.delete('asn25')
      cmd.delete('asn26')
      cmd.delete('asn27')
      cmd.delete('asn28')
      cmd.delete('asn')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his14')
      cmd.delete('his15')
      cmd.delete('his16')
      cmd.delete('his17')
      cmd.delete('his18')
      cmd.delete('his19')
      cmd.delete('his20')
      cmd.delete('his21')
      cmd.delete('his22')
      cmd.delete('his23')
      cmd.delete('his24')
      cmd.delete('his25')
      cmd.delete('his26')
      cmd.delete('his27')
      cmd.delete('his28')
      cmd.delete('his29')
      cmd.delete('his30')
      cmd.delete('his')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu12')
      cmd.delete('glu13')
      cmd.delete('glu14')
      cmd.delete('glu15')
      cmd.delete('glu16')
      cmd.delete('glu17')
      cmd.delete('glu18')
      cmd.delete('glu19')
      cmd.delete('glu20')
      cmd.delete('glu21')
      cmd.delete('glu22')
      cmd.delete('glu23')
      cmd.delete('glu24')
      cmd.delete('glu25')
      cmd.delete('glu')
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys10')
      cmd.delete('lys11')
      cmd.delete('lys12')
      cmd.delete('lys13')
      cmd.delete('lys14')
      cmd.delete('lys15')
      cmd.delete('lys16')
      cmd.delete('lys17')
      cmd.delete('lys18')
      cmd.delete('lys19')
      cmd.delete('lys20')
      cmd.delete('lys21')
      cmd.delete('lys22')
      cmd.delete('lys23')
      cmd.delete('lys24')
      cmd.delete('lys25')
      cmd.delete('lys')
      
      
              
    def alcoholdehyd2(self):
      deletemotif()
      cmd.select('tyr1', 'name cd1 and resn tyr within %s of (name nd2 and resn asn)'%(self.range.get()*5))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asn)'%(self.range.get()*8))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name nz and resn lys)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('tyr5', 'name ce2 and resn tyr within %s of (name cg and resn lys)'%(self.range.get()*6))
      cmd.select('tyr6', 'name cg and resn tyr within %s of (name nd2 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name cd1 and tyr)'%(self.range.get()*5))
      cmd.select('asn2', 'name nd2 and resn asn within %s of (name oh and tyr)'%(self.range.get()*7))
      cmd.select('asn3', 'name od1 and resn asn within %s of (name oh and tyr)'%(self.range.get()*7))
      cmd.select('asn4', 'name od1 and resn asn within %s of (name ce1 and tyr)'%(self.range.get()*6))
      cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(self.range.get()*5.5))
      cmd.select('asn6', 'name od1 and resn asn within %s5 of (name nz and resn lys)'%(self.range.get()*5.5))
      cmd.select('asn7', 'name nd2 and resn asn within %s of (name og and resn ser)'%(self.range.get()*10))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7')
      cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and asn)'%(self.range.get()*6))
      cmd.select('lys2', 'name ce and resn lys within %s of (name nd2 and asn)'%(self.range.get()*6.5))
      cmd.select('lys3', 'name nz and resn lys within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('lys4', 'name ce and resn lys within %s of (name cz and tyr)'%(self.range.get()*6))
      cmd.select('lys4', 'name nz and resn lys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('lys5', 'name ce and resn lys within %s of (name og and resn ser)'%(self.range.get()*7))
      cmd.select('lys6', 'name cg and resn lys within %s of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys7', 'name cd and resn lys within %s of (name cb and resn ser)'%(self.range.get()*6))
      cmd.select('lys8', 'name cd and resn lys within %s of (name cb and resn asn)'%(self.range.get()*7))
      cmd.select('lys9', 'name ce and resn lys within %s of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('ser2', 'name og and resn ser within %s of (name ce2 and tyr)'%(self.range.get()*6))
      cmd.select('ser3', 'name og and resn ser within %s of (name nz and lys)'%(self.range.get()*8))
      cmd.select('ser4', 'name cb and resn ser within %s of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('ser5', 'name cb and resn ser within %s of (name cd and lys)'%(self.range.get()*6))
      cmd.select('ser6', 'name cb and resn ser within %s of (name od1 and asn)'%(self.range.get()*10))
      cmd.select('ser7', 'name ca and resn ser within %s of (name nd2 and asn)'%(self.range.get()*10))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7')
      cmd.select('alcoholdehyd','ser(tyr(lys(asn)))')
      cmd.deselect()
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('asn')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('lys')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys1')
      cmd.delete('ser')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')

    def aldoreductase2(self):
      deletemotif()
      cmd.select('lys1', 'name cd and resn lys within %s of (name cg and resn his)'%(self.range.get()*6))
      cmd.select('lys2', 'name ce and resn lys within %s of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('lys3', 'name cd and resn lys within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('lys4', 'name nz and resn lys within %s of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('lys5', 'name nz and resn lys within %s of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('lys6', 'name cg and resn lys within %s of (name cz and resn tyr)'%(self.range.get()*8))
      cmd.select('lys7', 'name nz and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('lys8', 'name ce and resn lys within %s of (name od1 and resn asp)'%(self.range.get()*5.5))
      cmd.select('lys9', 'name cg and resn lys within %s of (name ca and resn asp)'%(self.range.get()*9))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
      cmd.select('his1', 'name cg and resn his within %s of (name cd and resn lys)'%(self.range.get()*6))
      cmd.select('his2', 'name ne2 and resn his within %s of (name ce and resn lys)'%(self.range.get()*8))
      cmd.select('his3', 'name nd1 and resn his within %s of (name cd and resn lys)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his5', 'name ce1 and resn his within %s of (name cz and resn tyr)'%(self.range.get()*6))
      cmd.select('his6', 'name nd1 and resn his within %s of (name ce1 and resn tyr)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*10.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name cg and resn asp)'%(self.range.get()*10))
      cmd.select('his9', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys )'%(self.range.get()*5))
      cmd.select('tyr2', 'name ce2 and resn tyr within %s of (name nz and resn lys )'%(self.range.get()*6))
      cmd.select('tyr3', 'name cz and resn tyr within %s of (name cg and resn lys)'%(self.range.get()*8))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr5', 'name cz and resn tyr within %s of (name ce1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr6', 'name ce1 and resn tyr within %s of (name nd1 and resn his)'%(self.range.get()*7))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*7))
      cmd.select('tyr8', 'name cz and resn tyr within %s of (name cb and resn asp)'%(self.range.get()*9))
      cmd.select('tyr9', 'name ce2 and resn tyr within %s of (name ca and resn asp)'%(self.range.get()*8))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nz and resn lys)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name ce and resn lys)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name ca and resn asp within %s of (name cg and resn lys)'%(self.range.get()*9))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*10.5))
      cmd.select('asp5', 'name cg and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*10))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*9))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('asp8', 'name cb and resn asp within %s of (name cz and resn tyr)'%(self.range.get()*9))
      cmd.select('asp9', 'name ca and resn asp within %s of (name ce2 and resn tyr)'%(self.range.get()*8))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('aldoreductase', 'asp(his(lys(tyr)))')
      cmd.deselect()
      cmd.delete('lys')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys9')
      cmd.delete('lys1')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')

    def cistransisomerase2(self):
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*9))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asp)'%(self.range.get()*11))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and resn asp)'%(self.range.get()*9.8))
      cmd.select('tyr4', 'name oh and resn tyr within %s of (name cb and resn asp)'%(self.range.get()*9.8))
      cmd.select('tyr5', 'name cz and resn tyr within %s of (name od2 and resn asp)'%(self.range.get()*10.2))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name od1 and resn asp)'%(self.range.get()*11.5))
      cmd.select('tyr7', 'name oh and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr8', 'name oh and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr9', 'name oh and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr10', 'name cz and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr11', 'name cz and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.8))
      cmd.select('tyr12', 'name cz and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s of (name cd1 and resn ile)'%(self.range.get()*6.3))
      cmd.select('tyr14', 'name ce1 and resn tyr within %s of (name cg1 and resn ile)'%(self.range.get()*6.5))
      cmd.select('tyr15', 'name ce1 and resn tyr within %s of (name cg2 and resn ile)'%(self.range.get()*5.5))
      cmd.select('tyr', 'byres tyr1 and byre tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13 and byres tyr14 and byres tyr15')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name oh and tyr)'%(self.range.get()*8.7))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name oh and tyr)'%(self.range.get()*10.5))
      cmd.select('asp3', 'name cg and resn asp within %s of (name oh and tyr)'%(self.range.get()*9.3))
      cmd.select('asp4', 'name cb and resn asp within %s of (name oh and tyr)'%(self.range.get()*9.3))
      cmd.select('asp5', 'name od2 and resn asp within %s of (name cz and tyr)'%(self.range.get()*10))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name cz and resn tyr)'%(self.range.get()*11.1))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name cg2 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp8', 'name od2 and resn asp within %s of (name cd1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp9', 'name od2 and resn asp within %s of (name cg1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp10', 'name cb and resn asp within %s of (name cd1 and resn ile)'%(self.range.get()*10.8))
      cmd.select('asp11', 'name cb and resn asp within %s of (name cg2 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp12', 'name cb and resn asp within %s of (name cg1 and resn ile)'%(self.range.get()*11.1))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11 and byres asp12')
      cmd.select('ile1', 'name cd1 and resn ile within %s of (name oh and tyr)'%(self.range.get()*6.5))
      cmd.select('ile2', 'name cg1 and resn ile within %s of (name oh and tyr)'%(self.range.get()*6.5))
      cmd.select('ile3', 'name cg2 and resn ile within %s of (name oh and tyr)'%(self.range.get()*5.5))
      cmd.select('ile4', 'name cd1 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*6.5))
      cmd.select('ile5', 'name cg1 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*6.8))
      cmd.select('ile6', 'name cg2 and resn ile within %s of (name cz and resn tyr)'%(self.range.get()*5.5))
      cmd.select('ile7', 'name cd1 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*6.3))
      cmd.select('ile8', 'name cg1 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('ile9', 'name cg2 and resn ile within %s of (name ce1 and resn tyr)'%(self.range.get()*5.5))
      cmd.select('ile10', 'name cg2 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile11', 'name cd1 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile12', 'name cg1 and resn ile within %s of (name od2 and asp)'%(self.range.get()*11.5))
      cmd.select('ile13', 'name cd1 and resn ile within %s of (name cb and asp)'%(self.range.get()*11))
      cmd.select('ile14', 'name cg2 and resn ile within %s of (name cb and resn asp)'%(self.range.get()*11.5))
      cmd.select('ile15', 'name cg1 and resn ile within %s of (name cb and resn asp)'%(self.range.get()*11.5))
      cmd.select('ile', 'byres ile1 and byres ile2 and byres ile3 and byres ile4 and byres ile5 and byres ile6 and byres ile7 and byres ile8 and byres ile9 and byres ile10 and byres ile11 and byres ile12 and byres ile13 and byres ile14 and byres ile15')
      cmd.select('Cis-trans', 'ile(asp(tyr))')
      cmd.deselect()
      cmd.orient('Cis-trans')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr2')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('tyr14')
      cmd.delete('tyr15')
      cmd.delete('tyr')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp11')
      cmd.delete('asp12')
      cmd.delete('asp')
      cmd.delete('ile1')
      cmd.delete('ile2')
      cmd.delete('ile3')
      cmd.delete('ile4')
      cmd.delete('ile5')
      cmd.delete('ile6')
      cmd.delete('ile7')
      cmd.delete('ile8')
      cmd.delete('ile9')
      cmd.delete('ile10')
      cmd.delete('ile11')
      cmd.delete('ile12')
      cmd.delete('ile13')
      cmd.delete('ile14')
      cmd.delete('ile15')
      cmd.delete('ile')
      
    def nadhbinder22(self):
      deletemotif()
      cmd.select('asp1', 'name od2 and resn asp within %s of (name sg and resn cys)'%(self.range.get()*5))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name sg and resn cys)'%(self.range.get()*6.4))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name cb and resn cys)'%(self.range.get()*7.2))
      cmd.select('asp5', 'name cg and resn asp within %s of (name sg and resn cys)'%(self.range.get()*5.5))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('asp8', 'name od1 and resn asp within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('asp9', 'name od1 and resn asp within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('asp10', 'name cg and resn asp within %s of (name og and resn ser)'%(self.range.get()*5.3))
      cmd.select('asp11', 'name cg and resn asp within %s of (name cb and resn ser)'%(self.range.get()*6.4))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11')
      cmd.select('cys1', 'name sg and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('cys3', 'name sg and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*6.4))
      cmd.select('cys4', 'name cb and resn cys within %s of (name od1 and resn asp)'%(self.range.get()*7.2))
      cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.4))
      cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(self.range.get()*8))
      cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*8.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('ser4', 'name cb and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn asp)'%(self.range.get()*5.3))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn asp)'%(self.range.get()*6.4))
      cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(self.range.get()*6.4))
      cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8))
      cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
      cmd.select('NAD-reductase', 'ser(asp(cys))')
      cmd.deselect()
      cmd.orient('NAD-reductase')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp11')
      cmd.delete('asp')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6')
      cmd.delete('cys7')
      cmd.delete('cys8')
      cmd.delete('cys9')
      cmd.delete('cys')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser')
   

    def nadhbinder222(self):
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('glu2', 'name oe2 and resn glu within %s of (name cb and resn cys)'%(self.range.get()*5.5))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('glu4', 'name oe1 and resn glu within %s of (name cb and resn cys)'%(self.range.get()*7.2))
      cmd.select('glu5', 'name cg and resn glu within %s of (name sg and resn cys)'%(self.range.get()*5.5))
      cmd.select('glu6', 'name oe2 and resn glu within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('glu7', 'name oe2 and resn glu within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('glu9', 'name oe1 and resn glu within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('glu10', 'name cg and resn glu within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('glu11', 'name cg and resn glu within %s of (name cb and resn ser)'%(self.range.get()*6.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11')
      cmd.select('cys1', 'name sg and resn cys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys2', 'name cb and resn cys within %s of (name oe2 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys3', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*6.5))
      cmd.select('cys4', 'name cb and resn cys within %s of (name oe1 and resn glu)'%(self.range.get()*7.5))
      cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn glu)'%(self.range.get()*5.5))
      cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(self.range.get()*6.5))
      cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(self.range.get()*7))
      cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(self.range.get()*8))
      cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(self.range.get()*8.5))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('ser1', 'name og and resn ser within %s of (name oe2 and resn glu)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name oe2 and resn glu)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name oe1 and resn glu)'%(self.range.get()*6))
      cmd.select('ser4', 'name cb and resn ser within %s of (name oe1 and resn glu)'%(self.range.get()*7))
      cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn glu)'%(self.range.get()*5.5))
      cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn glu)'%(self.range.get()*6.5))
      cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(self.range.get()*6.5))
      cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(self.range.get()*7))
      cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8))
      cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(self.range.get()*8.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
      cmd.select('NAD-reductase2', 'ser(glu(cys))')
      cmd.deselect()
      cmd.orient('NAD-reductase2')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu10')
      cmd.delete('glu11')
      cmd.delete('glu')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6') 
      cmd.delete('cys7') 
      cmd.delete('cys8')
      cmd.delete('cys9')
      cmd.delete('cys') 
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3') 
      cmd.delete('ser4')
      cmd.delete('ser5') 
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser10')
      cmd.delete('ser')

    def cephdeacetylase2(self):
      deletemotif()
      cmd.select('his1', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*4.5))
      cmd.select('his2', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5))
      cmd.select('his3', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('his4', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his5', 'name ce1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('his6', 'name ne2 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*7))
      cmd.select('his7', 'name ne2 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*6.5))
      cmd.select('his8', 'name ne2 and resn his within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('his9', 'name ce1 and resn his within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('his10', 'name nd1 and resn his within %s of (name cb and resn ala)'%(self.range.get()*6.5))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8.5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9.5))
      cmd.select('asp3', 'name cg and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9.5))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*4.5))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5))
      cmd.select('asp6', 'name cg and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp7', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp8', 'name od1 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*6))
      cmd.select('asp9', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asp10', 'name od2 and resn asp within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10')
      cmd.select('ala1', 'name cb and resn ala within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('ala2', 'name cb and resn ala within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('ala3', 'name cb and resn ala within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('ala4', 'name cb and resn ala within %s of (name od2 and resn asp)'%(self.range.get()*8.5))
      cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and resn asp)'%(self.range.get()*9.5))
      cmd.select('ala6', 'name cb and resn ala within %s of (name cg and resn asp)'%(self.range.get()*9.5))
      cmd.select('ala7', 'name c and resn ala within %s of (name n and resn gln)'%(self.range.get()*2.5))
      cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
      cmd.select('gln1', 'byres resn gln within %s of his'%(self.range.get()*9.5))
      cmd.select('gln2', 'byres resn gln within %s of asp'%(self.range.get()*13.5))
      cmd.select('gln3', 'byres resn gln within %s of ala'%(self.range.get()*3))
      cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3')
      cmd.select('deacetylase', 'his(asp(ala(gln)))')
      cmd.deselect()
      cmd.orient('deacetylase')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp')
      cmd.delete('ala1')
      cmd.delete('ala2')
      cmd.delete('ala3')
      cmd.delete('ala4')
      cmd.delete('ala5')
      cmd.delete('ala6')
      cmd.delete('ala7')
      cmd.delete('ala')
      cmd.delete('gln1')
      cmd.delete('gln2')
      cmd.delete('gln3')
      cmd.delete('gln')
    #hyaluronate/chondroitin lyase

    def chondrolyase2(self):
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s  of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('tyr3', 'name oh and resn tyr within %s  of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s  of (name ne and resn arg)'%(self.range.get()*7))
      cmd.select('tyr5', 'name oh and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*5))
      cmd.select('tyr6', 'name oh and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s  of (name ce1 and resn his)'%(self.range.get()*5))
      cmd.select('tyr8', 'name ce2 and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr9', 'name ce1 and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr11', 'name oh and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr12', 'name ce1 and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
      cmd.select('his1', 'name ne2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his2', 'name ne2 and resn his within %s  of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his3', 'name cd2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s  of (name cg and resn asn)'%(self.range.get()*8))
      cmd.select('his5', 'name ne2 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his6', 'name nd1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his7', 'name ce1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s  of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('his9', 'name ne2 and resn his within %s  of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('his10', 'name ne2 and resn his within %s  of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('his11', 'name ce1 and resn his within %s  of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('his12', 'name nd1 and resn his within %s  of (name nh1 and resn arg)'%(self.range.get()*6.5))
      cmd.select('his13', 'name nd1 and resn his within %s  of (name cd and resn arg)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
      cmd.select('arg1', 'name nh2 and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg2', 'name nh1 and resn arg within %s  of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('arg3', 'name cz and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg4', 'name ne and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh2 and resn arg within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('arg6', 'name cz and resn arg within %s  of (name ce1 and resn his)'%(self.range.get()*7))
      cmd.select('arg7', 'name nh1 and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('arg8', 'name cd and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*9))
      cmd.select('arg9', 'name nh1 and resn arg within %s  of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('arg10', 'name cz and resn arg within %s  of (name cg and resn asn)'%(self.range.get()*12))
      cmd.select('arg11', 'name nh2 and resn arg within %s  of (name nd2 and resn asn)'%(self.range.get()*11.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
      cmd.select('asn1', 'name od1 and resn asn within %s  of (name nh1 and resn arg)'%(self.range.get()*11))
      cmd.select('asn2', 'name cg and resn asn within %s  of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('asn3', 'name nd2 and resn asn within %s  of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('asn4', 'name od1 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asn5', 'name nd2 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn6', 'name od1 and resn asn within %s  of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asn7', 'name cg and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn8', 'name od1 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn10', 'name od1 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn11', 'name nd2 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')
      cmd.select('chondroitinase', 'asn(his(arg(tyr)))')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg')
      
    def hyaluronlyase2(self):
      deletemotif()
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s  of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('tyr3', 'name oh and resn tyr within %s  of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('tyr4', 'name oh and resn tyr within %s  of (name ne and resn arg)'%(self.range.get()*7))
      cmd.select('tyr5', 'name oh and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*5))
      cmd.select('tyr6', 'name oh and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr7', 'name oh and resn tyr within %s  of (name ce1 and resn his)'%(self.range.get()*5))
      cmd.select('tyr8', 'name ce2 and resn tyr within %s  of (name nd1 and resn his)'%(self.range.get()*6))
      cmd.select('tyr9', 'name ce1 and resn tyr within %s  of (name ne2 and resn his)'%(self.range.get()*6))
      cmd.select('tyr10', 'name oh and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr11', 'name oh and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*7.5))
      cmd.select('tyr12', 'name ce1 and resn tyr within %s  of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('tyr13', 'name ce1 and resn tyr within %s  of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
      cmd.select('his1', 'name ne2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his2', 'name ne2 and resn his within %s  of (name nd2 and resn asn)'%(self.range.get()*8))
      cmd.select('his3', 'name cd2 and resn his within %s  of (name od1 and resn asn)'%(self.range.get()*7))
      cmd.select('his4', 'name ne2 and resn his within %s  of (name cg and resn asn)'%(self.range.get()*8))
      cmd.select('his5', 'name ne2 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his6', 'name nd1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('his7', 'name ce1 and resn his within %s  of (name oh and resn tyr)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s  of (name ce2 and resn tyr)'%(self.range.get()*6))
      cmd.select('his9', 'name ne2 and resn his within %s  of (name ce1 and resn tyr)'%(self.range.get()*6))
      cmd.select('his10', 'name ne2 and resn his within %s  of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('his11', 'name ce1 and resn his within %s  of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('his12', 'name nd1 and resn his within %s  of (name nh1 and resn arg)'%(self.range.get()*6.5))
      cmd.select('his13', 'name nd1 and resn his within %s  of (name cd and resn arg)'%(self.range.get()*9))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
      cmd.select('arg1', 'name nh2 and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg2', 'name nh1 and resn arg within %s  of (name oh and tyr)'%(self.range.get()*6))
      cmd.select('arg3', 'name cz and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('arg4', 'name ne and resn arg within %s  of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('arg5', 'name nh2 and resn arg within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('arg6', 'name cz and resn arg within %s  of (name ce1 and resn his)'%(self.range.get()*7))
      cmd.select('arg7', 'name nh1 and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('arg8', 'name cd and resn arg within %s  of (name nd1 and resn his)'%(self.range.get()*9))
      cmd.select('arg9', 'name nh1 and resn arg within %s  of (name od1 and resn asn)'%(self.range.get()*11))
      cmd.select('arg10', 'name cz and resn arg within %s  of (name cg and resn asn)'%(self.range.get()*12))
      cmd.select('arg11', 'name nh2 and resn arg within %s  of (name nd2 and resn asn)'%(self.range.get()*11.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
      cmd.select('asn1', 'name od1 and resn asn within %s  of (name nh1 and resn arg)'%(self.range.get()*11))
      cmd.select('asn2', 'name cg and resn asn within %s  of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('asn3', 'name nd2 and resn asn within %s  of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('asn4', 'name od1 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*7))
      cmd.select('asn5', 'name nd2 and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn6', 'name od1 and resn asn within %s  of (name cd2 and resn his)'%(self.range.get()*7))
      cmd.select('asn7', 'name cg and resn asn within %s  of (name ne2 and resn his)'%(self.range.get()*8))
      cmd.select('asn8', 'name od1 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn9', 'name nd2 and resn asn within %s  of (name oh and resn tyr)'%(self.range.get()*7.5))
      cmd.select('asn10', 'name od1 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn11', 'name nd2 and resn asn within %s  of (name ce1 and resn tyr)'%(self.range.get()*6.5))
      cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')
      cmd.select('Hyaluronate_Lyase', 'asn(his(arg(tyr)))')
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('tyr')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('tyr10')
      cmd.delete('tyr11')
      cmd.delete('tyr12')
      cmd.delete('tyr13')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr8')
      cmd.delete('tyr9')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg11')
      cmd.delete('arg')

    def ACTase2(self):
      deletemotif()
      cmd.select('gln', 'resi 231 and resn gln')
      cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
      cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
      cmd.select('his', 'resi 134 and resn his')
      cmd.select('lys', 'resi 84 and resn lys')
      cmd.select('ser', 'resi 80 and resn ser')
      cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')
      cmd.delete('arg')
      cmd.delete('lys')
      cmd.delete('thr')
      cmd.delete('ser')
      cmd.delete('gln')
      cmd.delete('his')
      
    def exonucleaseiii2(self):
      deletemotif()
      cmd.select('his1', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(self.range.get()*5.5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(self.range.get()*6.5))
      cmd.select('his3', 'name ne2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*5.5))
      cmd.select('his4', 'name cd2 and resn his within %s of (name cg and resn asn)'%(self.range.get()*5.5))
      cmd.select('his5', 'name nd1 and resn his within %s of (name cg and resn asn)'%(self.range.get()*6.5))
      cmd.select('his6', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5))
      cmd.select('his8', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his9', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp2', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp4', 'name cg and resn asp within %s of (name nd1 and resn his)'%(self.range.get()*5.5))
      cmd.select('asp5', 'name od2 and resn asp within %s of (name nd2 and resn asn)'%(self.range.get()*5.7))
      cmd.select('asp6', 'name od1 and resn asp within %s of (name nd2 and resn asn)'%(self.range.get()*6))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name od1 and resn asn)'%(self.range.get()*6))
      cmd.select('asp8', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7')
      cmd.select('asp9', 'byres resn asp within %s of asp8'%(self.range.get()*5.5))
      cmd.select('asp10', 'byres resn asp within %s of his'%(self.range.get()*5.5))
      cmd.select('asp', 'byres asp8 or (byres asp9 and byres asp10)')
      cmd.select('asn1', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn2', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*6.5))
      cmd.select('asn3', 'name cg and resn asn within %s of (name ne2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn4', 'name cg and resn asn within %s of (name cd2 and resn his)'%(self.range.get()*5.5))
      cmd.select('asn5', 'name cg and resn asn within %s of (name nd1 and resn his)'%(self.range.get()*6.5))
      cmd.select('asn6', 'name nd2 and resn asn within %s of (name od2 and resn asp)'%(self.range.get()*5.7))
      cmd.select('asn7', 'name nd2 and resn asn within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('asn8', 'name od1 and resn asn within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('asn9', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8')
      cmd.select('asn10', 'byres resn asn within %s of asn9'%(self.range.get()*8))
      cmd.select('asn11', 'byres resn asn within %s of his'%(self.range.get()*8))
      cmd.select('asn12', 'byres resn asn within %s of asp8'%(self.range.get()*6))
      cmd.select('asn', 'byres asn9 or (byres asn10 and byres asn11 and byres asn12)')
      cmd.select('Exonuclease3', 'his(asp(asn))')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his')
      cmd.delete('asn1')
      cmd.delete('asn2')
      cmd.delete('asn3')
      cmd.delete('asn4')
      cmd.delete('asn5')
      cmd.delete('asn6')
      cmd.delete('asn7')
      cmd.delete('asn8')
      cmd.delete('asn9')
      cmd.delete('asn10')
      cmd.delete('asn11')
      cmd.delete('asn12')
      cmd.delete('asn')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp10')
      cmd.delete('asp')


    def adenylatekinase2(self):
      deletemotif()
      #p-loop first
      cmd.select('lys1', 'name nz and resn lys within %s of (name n and resn gly)'%(self.range.get()*7.5))
      cmd.select('lys2', 'name cg and resn lys within %s of (name c and resn gly)'%(self.range.get()*6))
      cmd.select('lys3', 'name n and resn lys within %s of (name n and resn gly)'%(self.range.get()*5))
      cmd.select('lys4', 'name n and resn lys within %s of (resn gly)'%(self.range.get()*2))
      cmd.select('lys5', 'name c and resn lys within %s of (resn gly)'%(self.range.get()*2))  
      cmd.select('lys6', 'name nz and resn lys within %s of (name od2 and resn asp)'%(self.range.get()*13))
      cmd.select('lys7', 'name nz and resn lys within %s of (name ne and resn arg)'%(self.range.get()*11))
      cmd.select('lys8', 'name nz and resn lys within %s of (name nh2 and resn arg)'%(self.range.get()*9.5))
      cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8')
      cmd.select('glya1', 'name n and resn gly within %s of (name nz and lys)'%(self.range.get()*7.5))
      cmd.select('glya2', 'name ca and resn gly within %s of (name cg and lys)'%(self.range.get()*7))
      cmd.select('glya3', 'name c and resn gly within %s of (name n and lys)'%(self.range.get()*2))
      cmd.select('glya4', 'name n and resn gly within %s of (name nh1 and resn arg)'%(self.range.get()*10))
      cmd.select('glya', 'byres glya1 and byres glya2 and byres glya3 and byres glya4')
      cmd.select('glyb', 'name n and resn gly within %s of (name c and lys)'%(self.range.get()*2))
      cmd.select('p-loop', 'lys(glya(byres glyb))')
      cmd.select('asp1', 'name od2 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('asp2', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(self.range.get()*5))
      cmd.select('asp4', 'name od2 and resn asp within %s of p-loop'%(self.range.get()*15))
      cmd.select('aspa', 'byres asp1 and byres asp2 and byres asp3 and byres asp4')
      cmd.select('aspb1', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('aspb2', 'name cg and resn asp within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('aspb3', 'name od1 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('aspb4', 'name od2 and resn asp within %s of (name od1 and aspa)'%(self.range.get()*7))
      cmd.select('aspb5', 'name cg and resn asp within %s of (name cg and aspa)'%(self.range.get()*7))
      cmd.select('aspb6', 'name od1 and resn asp within %s of (name od2 and aspa)'%(self.range.get()*7))
      cmd.select('asp', 'byres aspb1 and byres aspb2 and byres aspb3 and byres aspb4 and byres aspb5 and byres aspb6')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(self.range.get()*4.9))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(self.range.get()*4.9))
      cmd.select('arg', 'byres arg1 or byres arg2')
      cmd.select('adenylatekinase', 'p-loop(asp(aspa(arg)))')
      cmd.deselect()
      cmd.delete('lys1')
      cmd.delete('lys2')
      cmd.delete('lys3')
      cmd.delete('lys4')
      cmd.delete('lys5')
      cmd.delete('lys6')
      cmd.delete('lys7')
      cmd.delete('lys8')
      cmd.delete('lys')
      cmd.delete('glya1')
      cmd.delete('glya2')
      cmd.delete('glya3')
      cmd.delete('glya4')
      cmd.delete('glya')
      cmd.delete('glyb')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('aspa')
      cmd.delete('aspb1')
      cmd.delete('aspb2')
      cmd.delete('aspb3')
      cmd.delete('aspb4')
      cmd.delete('aspb5')
      cmd.delete('aspb6')
      cmd.delete('asp')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg')
      
      
      
      
      
      
    def citratesynth2(self):
      deletemotif()
      cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(self.range.get()*5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('his3', 'name ce1 and resn his within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn ser)'%(self.range.get()*6.5))
      cmd.select('his5', 'name cd2 and resn his within %s of (name og and resn ser)'%(self.range.get()*6))
      cmd.select('his6', 'name nd1 and resn his within %s of (name og and resn ser)'%(self.range.get()*7))
      cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(self.range.get()*8))
      cmd.select('his8', 'name nd1 and resn his within %s of (name cg and resn asp)'%(self.range.get()*8.5))
      cmd.select('his9', 'name o and resn his within %s of (name od2 and resn asp)'%(self.range.get()*5.5))
      cmd.select('his10', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
      cmd.select('his11', 'byres resn his within %s of his10'%(self.range.get()*8.2))
      cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his10)'%(self.range.get()*5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his10)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name ce1 and his10)'%(self.range.get()*5.5))
      cmd.select('ser4', 'name cb and resn ser within %s of (name ce1 and his10)'%(self.range.get()*6.5))
      cmd.select('ser5', 'name og and resn ser within %s of (name cd2 and his10)'%(self.range.get()*6))
      cmd.select('ser6', 'name og and resn ser within %s of (name nd1 and his10)'%(self.range.get()*7))
      cmd.select('ser7', 'name og and resn ser within %s of (name od2 and resn asp)'%(self.range.get()*12))
      cmd.select('ser8', 'name og and resn ser within %s of (name cg and resn asp)'%(self.range.get()*12))
      cmd.select('ser9', 'name og and resn ser within %s of (name od1 and resn asp)'%(self.range.get()*12))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
      cmd.select('his12', 'byres resn his within %s of ser'%(self.range.get()*12))
      cmd.select('asp1', 'name od2 and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp2', 'name cg and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp3', 'name od1 and resn asp within %s of (name og and ser)'%(self.range.get()*12))
      cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and his10)'%(self.range.get()*8))
      cmd.select('asp5', 'name cg and resn asp within %s of (name nd1 and his10)'%(self.range.get()*8.5))
      cmd.select('asp6', 'name od2 and resn asp within %s of (name o and his10)'%(self.range.get()*5.5))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6')
      cmd.select('his13', 'byres resn his within %s of asp'%(self.range.get()*8.5))
      cmd.select('his', 'byres his10 or (byres his11 and byres his12 and byres his13)')
      cmd.select('Citrate_Synth', 'his(asp(ser))')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his11')
      cmd.delete('his12')
      cmd.delete('his13')
      cmd.delete('his')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp')

      
    def tyrosinekinase2(self):
      deletemotif()
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5))
      cmd.select('arg2', 'name nh2 and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('arg3', 'name cz and resn arg within %s of (name cb and resn ala)'%(self.range.get()*5.5))
      cmd.select('arg4', 'name ne and resn arg within %s of (name cb and resn ala)'%(self.range.get()*6))
      cmd.select('arg5', 'name nh2 and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg6', 'name nh2 and resn arg within %s of (name cg and resn asp)'%(self.range.get()*5.5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(self.range.get()*6))
      cmd.select('arg8', 'name cz and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg9', 'name ne and resn arg within %s of (name od1 and resn asp)'%(self.range.get()*6))
      cmd.select('arg10', 'name ne and resn arg within %s of (name cg and resn asp)'%(self.range.get()*6.5))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10')
      cmd.select('asp1', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5.5))
      cmd.select('asp2', 'name cg and resn asp within %s of (name nh2 and resn arg)'%(self.range.get()*5.5))
      cmd.select('asp3', 'name od2 and resn asp within %s of (name nh2 and arg)'%(self.range.get()*7))
      cmd.select('asp4', 'name od1 and resn asp within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('asp5', 'name od1 and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6))
      cmd.select('asp6', 'name cg and resn asp within %s of (name ne and resn arg)'%(self.range.get()*6.5))
      cmd.select('asp7', 'name od1 and resn asp within %s of (name cb and resn ala)'%(self.range.get()*9))
      cmd.select('asp8', 'name o and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8))
      cmd.select('asp9', 'name cg and resn asp within %s of (name cb and resn ala)'%(self.range.get()*8))
      cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
      cmd.select('ala1', 'name cb and resn ala within %s of (name nh1 and arg)'%(self.range.get()*5))
      cmd.select('ala2', 'name cb and resn ala within %s of (name nh2 and arg)'%(self.range.get()*5.5))
      cmd.select('ala3', 'name cb and resn ala within %s of (name cz and arg)'%(self.range.get()*5.5))
      cmd.select('ala4', 'name cb and resn ala within %s of (name ne and arg)'%(self.range.get()*6))
      cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and asp)'%(self.range.get()*9))
      cmd.select('ala6', 'name cb and resn ala within %s of (name o and asp)'%(self.range.get()*8))
      cmd.select('ala7', 'name cb and resn ala within %s of (name cg and asp)'%(self.range.get()*8))
      cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
      cmd.select('SRC-Kinase', 'ala(asp(arg))')
      cmd.deselect()
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg10')
      cmd.delete('arg')
      cmd.delete('asp1')
      cmd.delete('asp2')
      cmd.delete('asp3')
      cmd.delete('asp4')
      cmd.delete('asp5')
      cmd.delete('asp6')
      cmd.delete('asp7')
      cmd.delete('asp8')
      cmd.delete('asp9')
      cmd.delete('asp')
      cmd.delete('ala1')
      cmd.delete('ala2')
      cmd.delete('ala3')
      cmd.delete('ala4')
      cmd.delete('ala5')
      cmd.delete('ala6')
      cmd.delete('ala7')
      cmd.delete('ala')

    def hhal2(self):
      deletemotif()
      cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(self.range.get()*10))
      cmd.select('glu2', 'name cd and resn glu within %s of (name cb and resn cys)'%(self.range.get()*10))
      cmd.select('glu3', 'name oe1 and resn glu within %s of (name ca and resn cys)'%(self.range.get()*10))
      cmd.select('glu4', 'name oe2 and resn glu within %s of (name ne and resn arg)'%(self.range.get()*5))
      cmd.select('glu5', 'name cd and resn glu within %s of (name cz and resn arg)'%(self.range.get()*6))
      cmd.select('glu6', 'name oe1 and resn glu within %s of (name nh2 and resn arg)'%(self.range.get()*5))
      cmd.select('glu7', 'name cg and resn glu within %s of (name ca and resn phe)'%(self.range.get()*10))
      cmd.select('glu8', 'name cd and resn glu within %s of (name cb and resn phe)'%(self.range.get()*10))
      cmd.select('glu9', 'name ca and resn glu within %s of (name cd1 and resn phe)'%(self.range.get()*7.5))
      cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9')
      cmd.select('cys1', 'name sg and resn cys within %s of (name nh1 and resn arg)'%(self.range.get()*6))
      cmd.select('cys2', 'name cb and resn cys within %s of (name cz and resn arg)'%(self.range.get()*7))
      cmd.select('cys3', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(self.range.get()*8))
      cmd.select('cys4', 'name sg and resn cys within %s of (name oe2 and glu)'%(self.range.get()*10))
      cmd.select('cys5', 'name cb and resn cys within %s of (name cd and glu)'%(self.range.get()*10))
      cmd.select('cys6', 'name ca and resn cys within %s of (name oe1 and glu)'%(self.range.get()*10))
      cmd.select('cys7', 'name ca and resn cys within %s of (name ca and resn phe)'%(self.range.get()*8.5))
      cmd.select('cys8', 'name cb and resn cys within %s of (name cd2 and resn phe)'%(self.range.get()*9))
      cmd.select('cys9', 'name sg and resn cys within %s of (name cd1 and resn phe)'%(self.range.get()*12))
      cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
      cmd.select('arg1', 'name nh1 and resn arg within %s of (name sg and resn cys)'%(self.range.get()*6))
      cmd.select('arg2', 'name cz and resn arg within %s of (name cb and resn cys)'%(self.range.get()*7))
      cmd.select('arg3', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(self.range.get()*8))
      cmd.select('arg4', 'name ne and resn arg within %s of (name oe2 and glu)'%(self.range.get()*5))
      cmd.select('arg5', 'name cz and resn arg within %s of (name cd and glu)'%(self.range.get()*6))
      cmd.select('arg6', 'name nh2 and resn arg within %s of (name oe1 and glu)'%(self.range.get()*5))
      cmd.select('arg7', 'name nh2 and resn arg within %s of (name ce1 and resn phe)'%(self.range.get()*10.5))
      cmd.select('arg8', 'name cz and resn arg within %s of (name cz and resn phe)'%(self.range.get()*11.5))
      cmd.select('arg9', 'name nh1 and resn arg within %s of (name ce2 and resn phe)'%(self.range.get()*12))
      cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
      cmd.select('phe1', 'name ca and resn phe within %s of (name cg and glu)'%(self.range.get()*10))
      cmd.select('phe2', 'name cb and resn phe within %s of (name cb and glu)'%(self.range.get()*10))
      cmd.select('phe3', 'name cd1 and resn phe within %s of (name ca and glu)'%(self.range.get()*7.5))
      cmd.select('phe4', 'name ce1 and resn phe within %s of (name nh2 and resn arg)'%(self.range.get()*10.5))
      cmd.select('phe5', 'name cz and resn phe within %s of (name cz and resn arg)'%(self.range.get()*11.5))
      cmd.select('phe6', 'name ce2 and resn phe within %s of (name nh1 and resn arg)'%(self.range.get()*12))
      cmd.select('phe7', 'name ca and resn phe within %s of (name ca and cys)'%(self.range.get()*8.5))
      cmd.select('phe8', 'name cd2 and resn phe within %s of (name cb and cys)'%(self.range.get()*9))
      cmd.select('phe9', 'name cd1 and resn phe within %s of (name sg and cys)'%(self.range.get()*12))
      cmd.select('phe', 'byres phe1 and byres phe2 and byres phe3 and byres phe4 and byres phe5 and byres phe6 and byres phe7 and byres phe8 and byres phe9')
      cmd.select('hhal', 'glu(arg(phe(cys)))')
      cmd.deselect()
      cmd.orient('hhal')
      cmd.delete('arg1')
      cmd.delete('arg2')
      cmd.delete('arg3')
      cmd.delete('arg4')
      cmd.delete('arg5')
      cmd.delete('arg6')
      cmd.delete('arg7')
      cmd.delete('arg8')
      cmd.delete('arg9')
      cmd.delete('arg')
      cmd.delete('glu1')
      cmd.delete('glu2')
      cmd.delete('glu3')
      cmd.delete('glu4')
      cmd.delete('glu5')
      cmd.delete('glu6')
      cmd.delete('glu7')
      cmd.delete('glu8')
      cmd.delete('glu9')
      cmd.delete('glu')
      cmd.delete('phe')
      cmd.delete('phe1')
      cmd.delete('phe2')
      cmd.delete('phe3')
      cmd.delete('phe4')
      cmd.delete('phe5')
      cmd.delete('phe6')
      cmd.delete('phe7')
      cmd.delete('phe8')
      cmd.delete('phe9')
      cmd.delete('cys')
      cmd.delete('cys1')
      cmd.delete('cys2')
      cmd.delete('cys3')
      cmd.delete('cys4')
      cmd.delete('cys5')
      cmd.delete('cys6')
      cmd.delete('cys7')
      cmd.delete('cys8')
      cmd.delete('cys9')
      
    def serotoninacetyl2(self):
      cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(self.range.get()*4.5))
      cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*5.5))
      cmd.select('his3', 'name cd2 and resn his within %s of (name og and resn ser)'%(self.range.get()*5.5))
      cmd.select('his4', 'name cd2 and resn his within %s of (name cb and resn ser)'%(self.range.get()*6))
      cmd.select('his5', 'name ne2 and resn his within %s of (name o and resn leu)'%(self.range.get()*6))
      cmd.select('his6', 'name ce1 and resn his within %s of (name cd1 and resn leu)'%(self.range.get()*10))
      cmd.select('his7', 'name ce1 and resn his within %s of (name cb and resn leu)'%(self.range.get()*9))
      cmd.select('his8', 'name nd1 and resn his within %s of (name og and resn ser)'%(self.range.get()*7.5))
      cmd.select('his9', 'name o and resn his within %s of (name oh and resn tyr)'%(self.range.get()*10))
      cmd.select('his10', 'name cb and resn his within %s of (name oh and resn tyr)'%(self.range.get()*12))
      cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
      cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his)'%(self.range.get()*4.5))
      cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his)'%(self.range.get()*5.5))
      cmd.select('ser3', 'name og and resn ser within %s of (name cd2 and his)'%(self.range.get()*5.5))
      cmd.select('ser4', 'name cb and resn ser within %s of (name cd2 and his)'%(self.range.get()*6)) 
      cmd.select('ser5', 'name og and resn ser within %s of (name nd1 and his)'%(self.range.get()*7.5))
      cmd.select('ser6', 'name og and resn ser within %s of (name o and resn leu)'%(self.range.get()*5))
      cmd.select('ser7', 'name og and resn ser within %s of (name cb and resn leu)'%(self.range.get()*8))
      cmd.select('ser8', 'name cb and resn ser within %s of (name o and resn leu)'%(self.range.get()*5.5))
      cmd.select('ser9', 'name n and resn ser within %s of (name cd2 and his)'%(self.range.get()*5.5))
      cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
      cmd.select('leu1', 'name o and resn leu within %s of (name ne2 and his)'%(self.range.get()*6))
      cmd.select('leu2', 'name cd1 and resn leu within %s of (name ce1 and his)'%(self.range.get()*10))
      cmd.select('leu3', 'name cb and resn leu within %s of (name ce1 and his)'%(self.range.get()*9))
      cmd.select('leu4', 'name o and resn leu within %s of (name og and ser)'%(self.range.get()*5))
      cmd.select('leu5', 'name cb and resn leu within %s of (name og and ser)'%(self.range.get()*8))
      cmd.select('leu6', 'name o and resn leu within %s of (name cb and ser)'%(self.range.get()*5.5))
      cmd.select('leu7', 'name n and resn leu within %s of (name ce1 and resn his)'%(self.range.get()*7.5))
      cmd.select('leu8', 'byres leu1 and byres leu2 and byres leu3 and byres leu4 and byres leu5 and byres leu6 and byres leu7')
      cmd.select('leu9', 'name n and resn leu within %s of (name o and his)'%(self.range.get()*7))
      cmd.select('leu10', 'name n and resn leu within %s of (name c and his)'%(self.range.get()*6.5))
      cmd.select('leu11', 'name n and resn leu within %s of (name n and his)'%(self.range.get()*8))
      cmd.select('leu12', 'name cd1 and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*6))
      cmd.select('leu13', 'name cb and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*5.5))
      cmd.select('leu14', 'name cg and resn leu within %s of (name oh and resn tyr)'%(self.range.get()*7))
      cmd.select('leu15', 'name cd1 and resn leu within %s of (name cz and resn tyr)'%(self.range.get()*6.5))
      cmd.select('leu15b', 'name cd1 and resn leu within %s of (name ce1 and resn tyr)'%(self.range.get()*5.5))
      cmd.select('leu16', 'byres leu9 and byres leu15b and byres leu10 and byres leu11 and byres leu12 and byres leu13 and byres leu14 and byres leu15')
      cmd.select('tyr1', 'name oh and resn tyr within %s of (name cd1 and leu16)'%(self.range.get()*6))
      cmd.select('tyr2', 'name oh and resn tyr within %s of (name cb and leu16)'%(self.range.get()*6.5))
      cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and leu16)'%(self.range.get()*7))
      cmd.select('tyr4', 'name cz and resn tyr within %s of (name cd1 and leu16)'%(self.range.get()*6.5))
      cmd.select('tyr5', 'name oh and resn tyr within %s of (name n and his)'%(self.range.get()*10))
      cmd.select('tyr6', 'name cz and resn tyr within %s of (name c and his)'%(self.range.get()*10.2))
      cmd.select('tyr7', 'name ce1 and resn tyr within %s of (name o and ser)'%(self.range.get()*16))
      cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
      cmd.select('Serotonin_transferase', 'his(ser(leu8(leu16(tyr))))')
      cmd.deselect()
      cmd.delete('his1')
      cmd.delete('his2')
      cmd.delete('his3')
      cmd.delete('his4')
      cmd.delete('his5')
      cmd.delete('his6')
      cmd.delete('his7')
      cmd.delete('his8')
      cmd.delete('his9')
      cmd.delete('his10')
      cmd.delete('his')
      cmd.delete('ser1')
      cmd.delete('ser2')
      cmd.delete('ser3')
      cmd.delete('ser4')
      cmd.delete('ser5')
      cmd.delete('ser6')
      cmd.delete('ser7')
      cmd.delete('ser8')
      cmd.delete('ser9')
      cmd.delete('ser')
      cmd.delete('leu1')
      cmd.delete('leu2')
      cmd.delete('leu3')
      cmd.delete('leu4')
      cmd.delete('leu5')
      cmd.delete('leu6')
      cmd.delete('leu7')
      cmd.delete('leu8')
      cmd.delete('leu9')
      cmd.delete('leu10')
      cmd.delete('leu11')
      cmd.delete('leu12')
      cmd.delete('leu13')
      cmd.delete('leu14')
      cmd.delete('leu15')
      cmd.delete('leu15b')
      cmd.delete('leu16')
      cmd.delete('leu')
      cmd.delete('tyr1')
      cmd.delete('tyr2')
      cmd.delete('tyr3')
      cmd.delete('tyr4')
      cmd.delete('tyr5')
      cmd.delete('tyr6')
      cmd.delete('tyr7')
      cmd.delete('tyr')




      
#motif options
    def motifoption(self, tag):
      if tag=='Surface Pocket':
        self.surfmotifer()
      elif tag=='Polar Contacts':
        self.motifcontact()
      elif tag=='Hide Contacts':
        self.hidecontact()
      elif tag=='Show Substrate':
        self.showsubstrate()
      elif tag=='Show label':
        self.labelmotif()
      elif tag=='Hide Label':
        self.dellabel()
      elif tag=='Hide Substrate':
        self.hidesubstrate()
        
#Show binding pocket
    def surfmotifer(self):
        objects = cmd.get_names('all')
        cmd.set('transparency', '0.5', 'all')
        try:
            if 'Adjacent' in objects:
                if 'Peroxidase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Peroxidase and !Adjacent')
                if 'carboncarbon' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!carboncarbon and !Adjacent')
                if 'o-glycosyl' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!o-glycosyl and !Adjacent')
                if 'Tkinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Tkinase and !Adjacent')
                if 'Ligase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Ligase and !Adjacent')
                if 'glu_amidotransferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!glu_amidotransferase and !Adjacent')
                if 'fucoseisomerase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!fucoseisomerase and !Adjacent')
                if 'Aminotransferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Aminotransferase and !Adjacent')
                if 'Zinc_finger' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Zinc_finger and !Adjacent')
                if 'paplike' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!paplike and !Adjacent')
                if 'carbonicanhydrase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!carbonicanhydrase and !Adjacent')
                if 'tyrophos' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!tyrophos and !Adjacent')
                if 'metalloprotease' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!metalloprotease and !Adjacent')
                if 'superoxide' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!superoxide and !Adjacent')
                if 'lactamase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!lactamase and !Adjacent')
                if 'serineprotease' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!serineprotease and !Adjacent')
                if 'TrioseIsomerase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!TrioseIsomerase and !Adjacent')
                if 'alcoholdehyd' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!alcoholdehyd and !Adjacent')
                if 'aldoreductase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!aldoreductase and !Adjacent')
                if 'Cis-trans' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Cis-trans and !Adjacent')
                if 'NAD-reductase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!NAD-reductase and !Adjacent')
                if 'NAD-reductase2' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!NAD-reductase2 and !Adjacent')
                if 'deacetylase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!deacetylase and !Adjacent')
                if 'chondroitinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!chondroitinase and !Adjacent')
                if 'Hyaluronate_Lyase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Hyaluronate_Lyase and !Adjacent')
                if 'Cyclin_Kinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Cyclin_Kinase and !Adjacent')
                if 'SRC-Kinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!SRC-Kinase and !Adjacent')
                if 'Serotonin_transferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Serotonin_transferase and !Adjacent')
                if 'deacetylase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!deacetylase and !Adjacent')
                if 'adenylatekinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!adenylatekinase and !Adjacent')
                if 'actase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!actase and !Adjacent')
                if 'Exonuclease3' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Exonuclease3 and !Adjacent')
                if 'Citrate_Synth' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Citrate_Synth and !Adjacent')
                if 'hhal' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!hhal and !Adjacent')
                if 'Exonuclease3' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Exonuclease3 and !Adjacent')
                               
                cpksubstrate()
                cmd.orient('all')
            else:
                if 'Peroxidase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Peroxidase')
                if 'carboncarbon' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!carboncarbon')
                if 'o-glycosyl' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!o-glycosyl')
                if 'Tkinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Tkinase')
                if 'Ligase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Ligase')
                if 'glu_amidotransferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!glu_amidotransferase')
                if 'fucoseisomerase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!fucoseisomerase')
                if 'Aminotransferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Aminotransferase')
                if 'Zinc_finger' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Zinc_finger')
                if 'paplike' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!paplike')
                if 'carbonicanhydrase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!carbonicanhydrase')
                if 'tyrophos' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!tyrophos')
                if 'metalloprotease' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!metalloprotease')
                if 'superoxide' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!superoxide')
                if 'lactamase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!lactamase')
                if 'serineprotease' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!serineprotease')
                if 'TrioseIsomerase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!TrioseIsomerase')
                if 'alcoholdehyd' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!alcoholdehyd')
                if 'aldoreductase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!aldoreductase')
                if 'Cis-trans' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Cis-trans')
                if 'NAD-reductase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!NAD-reductase')
                if 'NAD-reductase2' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!NAD-reductase2')
                if 'deacetylase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!deacetylase')
                if 'chondroitinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!chondroitinase')
                if 'Hyaluronate_Lyase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Hyaluronate_Lyase')
                if 'Cyclin_Kinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Cyclin_Kinase')
                if 'SRC-Kinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!SRC-Kinase')
                if 'Serotonin_transferase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Serotonin_transferase')
                if 'deacetylase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!deacetylase')
                if 'adenylatekinase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!adenylatekinase')
                if 'actase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!actase')
                if 'Exonuclease3' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Exonuclease3')
                if 'Citrate_Synth' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!Citrate_Synth')
                if 'hhal' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!hhal')
                if 'betaine_dehydrogenase' in objects:
                    cmd.show('surface', 'all')
                    cmd.hide('cartoon', 'all')
                    cmd.color('white', '!betaine_dehydrogenase')
                cpksubstrate()
                cmd.orient('all')
        except:
             import tkMessageBox
             tkMessageBox.showinfo('Alert', 'You must select a motif')

#polar contacts

    def motifcontact(self):
      objects = cmd.get_names('all')
      try:
        
        try:
          cmd.dist(self.mot+"_polar_conts",self.mot,self.mot,quiet=1,mode=2,label=0,reset=1)
          cmd.enable(self.mot+"_polar_conts")

        except:
          cmd.dist("motif_polar_conts","motif","motif",quiet=1,mode=2,label=0,reset=1)
          cmd.enable("motif_polar_conts")
          
        if 'Adjacent' in objects:
            cmd.dist('Adjacent_polar_conts','Adjacent','Adjacent',quiet=1,mode=2,label=0,reset=1)
        if 'substrate' in objects:
            cmd.dist(self.mot+"_around_polar_conts",self.mot,"(byobj ("+self.mot+")) and (not ("+self.mot+"))",quiet=1,mode=2,label=0,reset=1)
            cmd.enable(self.mot+"_around_polar_conts")
       
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', "Select a motif first")


    def hidecontact(self):
        objects = cmd.get_names('all')
        try:
          try:
            cmd.delete(self.mot+"_polar_conts")
          except:
            cmd.delete("motif_polar_conts")
          if 'Adjacent' in objects:
            cmd.delete('Adjacent_polar_conts')
          if 'substrate' in objects:
              cmd.delete(self.mot+"_around"+"_polar_conts")
        except:
          import tkMessageBox
          tkMessageBox.showinfo('Alert', "No motif polar contacts to hide")
#develop spot
          
#substrate#
          
    def showsubstrate(self):
      try:
        try:
          
          cmd.select('substrate', 'byres het within 7 of '+self.mot)
          objects = cmd.get_names('all')
          xp = cmd.index('substrate')
          np  = len(xp)
          if(np < 1):
              cmd.delete('substrate')
          if 'substrate' in objects:
              cmd.show('sticks', 'substrate')
              cmd.deselect()
              cpksubstrate()
         
        except:
          cmd.select('substrate', 'byres het within 7 of motif')
          objects = cmd.get_names('all')
          xp = cmd.index('substrate')
          np  = len(xp)
          if(np < 1):
              cmd.delete('substrate')
          if 'substrate' in objects:
              cmd.show('sticks', 'substrate')
              cmd.deselect()
              cpksubstrate()
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', "No substrate found")

    def hidesubstrate(self):
      try:
        cmd.hide('sticks', 'substrate')
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', "No substrate selected")
        
#Labels
        
    def dellabel(self):
      objects = cmd.get_names('all')
      try:
        try:
          cmd.label(self.mot,"''")
        except:
          cmd.label("motif","''")
        if 'Adjacent' in objects:
          cmd.label('byres Adjacent',"''")
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', "No motif labels to hide")

    def labelmotif(self):
      objects = cmd.get_names('all')
      try:
        try:
          cmd.label('''(name ca+C1*+C1' and (byres('''+self.mot+''')))''','''"%s-%s"%(resn,resi)''')
        except:
          cmd.label('''(name ca+C1*+C1' and (byres(motif)))''','''"%s-%s"%(resn,resi)''')
        if 'Adjacent' in objects:
          cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''','''"%s-%s"%(resn,resi)''')
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', "Select a motif first")
        
#bind to menu for motifs
        
    def oxidoreductase(self, tag):
      if tag=='Superoxide Dismutase':
              self.superoxide()
              self.mot='superoxide' 
      elif tag=='Peroxidase':
              self.peroxidase()
              self.mot='Peroxidase'
      elif tag=='Alcohol Dehydrogenase':
              self.alcoholdehyd()
              self.mot= 'alcoholdehyd'
      elif tag=='Aldose Reductase':
              self.aldoreductase()
              self.mot='aldoreductase'
      elif tag=='NAD Reductase':
              self.nadhbinder()
              self.mot='NAD-reductase'
      elif tag=='NAD Reductase2':
              self.nadhbinder2()
              self.mot='NAD-reductase2'
      elif tag=='Betaine aldehyde dehydrogenase':
              self.betainedehydrogenase()
              self.mot='betaine_dehydrogenase'
              

    def transferase(self, tag):
      
      if tag =='Amino Transferase':
              self.aminotransferase()
              self.mot='Aminotransferase'
      elif tag=='Glutamine Amidotransferase':
              self.glutamine_amidotransferase()
              self.mot='glu_amidotransferase'
      elif tag =='Thymidine Kinase':
              self.thymidinekinase()
              self.mot='Tkinase'
      elif tag =='ACTase':
              self.ACTase()
              self.mot='actase'
      elif tag=='Adenylate Kinase':
              self.adenylatekinase()
              self.mot='adenylatekinase'
      elif tag=='SRC Family Kinase':
              self.tyrosinekinase()
              self.mot='SRC-Kinase'
      elif tag=='Hhal Methyltransferase':
              self.hhal()
              self.mot='hhal'
              
      elif tag=='Serotonin Acetyltransferase':
              self.serotoninacetyl()
              self.mot = 'Serotonin_transferase'
      elif tag=='Cyclin Dependent Kinase':
              self.cyclinkinase()
              self.mot = 'Cyclin_Kinase'


    def hydrolase(self, tag):
      if tag =='Serine Protease':
              self.serineprotease()
              self.mot='serineprotease'
      elif tag == 'Papain Like':
              self.paplike()
              self.mot='paplike'
      elif tag == 'Metalloprotease':
              self.metalloprotease()
              self.mot='metalloprotease'
      elif tag == 'Tyrosine Phosphatase':
              self.tyrophos()
              self.mot= 'tyrophos'
      elif tag == 'Beta Lactamase':
              self.Blactamase()
              self.mot='lactamase'
      elif tag == 'O-Glycosyl':
              self.oglycosyl()
              self.mot='o-glycosyl'
      elif tag == 'Cephalosporin deacetylase':
              self.cephdeacetylase()
              self.mot='deacetylase'

    def lyase(self, tag):
      if tag =='Carbonic Anhydrase':
              self.carbanhyd()
              self.mot='carbonicanhydrase'
      elif tag=='Carbon Carbon':
              self.carboncarbon()
              self.mot='carboncarbon'
      elif tag=='Chondroitinase':
              self.chondrolyase()
              self.mot='chondroitinase'
      elif tag =='Hyaluronate-Lyase':
              self.hyaluronlyase()
              self.mot='Hyaluronate_Lyase'
      elif tag=='Exonuclease 3':
              self.exonucleaseiii()
              self.mot='Exonuclease3'
      elif tag=='Citrate Synthase':
              self.citratesynth()
              self.mot='Citrate_Synth'

    def isomerase(self, tag):
      if tag =='Fucose Isomerase':
              self.fisomerase()
              self.mot='fucoseisomerase'
      elif tag =='Triose Phosphate Isomerase':
              self.trioseisomerase()
              self.mot='TrioseIsomerase'
      elif tag=='FK506 Cis-Trans':
              self.cistransisomerase()
              self.mot='Cis-trans'

    def ligase(self, tag):
      if tag =='DNA Ligase':
              self.dnaligase()
              self.mot='ligase'

    def other(self, tag):
      if tag =='Zinc Finger':
              self.zincfinger()
              self.mot='Zinc_finger'
#after appending motif to motif search field allows user to click on it
#and run the motif function
   
    def allmotif(self):
        motif = self.motifbox.getcurselection()
        for item in motif:
          tag = item
        try:
            if len(tag) == 0:
                print 'No selection for double click'
            elif tag == '2-Cyclin Dependent Kinase':
                  self.cyclinkinase()
                  self.mot='Cyclin_Kinase'

            elif tag == '1-Cyclin Dependent Kinase':
                  self.cyclinkinase()
                  self.mot='Cyclin_Kinase'


            elif tag=='1-Betaine aldehyde dehydrogenase':
                  self.betainedehydrogenase()
                  self.mot='betaine_dehydrogenase'
            elif tag=='1-Betaine aldehyde dehydrogenase':
                  self.betainedehydrogenase()
                  self.mot='betaine_dehydrogenase'
            elif tag == '1-Serotonin Acetyltransferase':
                  self.serotoninacetyl()
                  self.mot='Serotonin_transferase'
            elif tag == '2-Serotonin Acetyltransferase':
                  self.serotoninacetyl()
                  self.mot='Serotonin_transferase'
            elif tag =='1-Zinc Finger':
                  self.zincfinger()
                  self.mot='Zinc_finger'
            elif tag =='1-DNA Ligase':
                  self.dnaligase()
                  self.mot='ligase'
            elif tag =='1-Fucose Isomerase':
                  self.fisomerase()
                  self.mot='fucoseisomerase'
            elif tag =='1-Triose Phosphate Isomerase':
                  self.trioseisomerase()
                  self.mot='TrioseIsomerase'
            elif tag=='1-FK506 Cis-Trans':
                  self.cistransisomerase()
                  self.mot='Cis-trans'
            elif tag =='1-Carbonic Anhydrase':
                  self.carbanhyd()
                  self.mot='carbonicanhydrase'
            elif tag=='1-Carbon Carbon':
                  self.carboncarbon()
                  self.mot='carboncarbon'
            elif tag=='1-Chondroitinase':
                  self.chondrolyase()
                  self.mot='chondroitinase'
            elif tag =='1-Hyaluronate-Lyase':
                  self.hyaluronlyase()
                  self.mot='Hyaluronate_Lyase'
            elif tag=='1-Exonuclease 3':
                  self.exonucleaseiii()
                  self.mot='Exonuclease3'
            elif tag=='1-Citrate Synthase':
                  self.citratesynth()
                  self.mot='Citrate_Synth'
            elif tag =='1-Serine Protease':
                  self.serineprotease()
                  self.mot='serineprotease'
            elif tag == '1-Papain Like':
                  self.paplike()
                  self.mot='paplike'
            elif tag == '1-Metalloprotease':
                  self.metalloprotease()
                  self.mot='metalloprotease'
            elif tag == '1-Tyrosine Phosphatase':
                  self.tyrophos()
                  self.mot= 'tyrophos'
            elif tag == '1-Beta Lactamase':
                  self.Blactamase()
                  self.mot='lactamase'
            elif tag == '1-O-Glycosyl':
                  self.oglycosyl()
                  self.mot='o-glycosyl'
            elif tag == '1-Cephalosporin deacetylase':
                  self.cephdeacetylase()
                  self.mot='deacetylase'
            elif tag =='1-Amino Transferase':
                  self.aminotransferase()
                  self.mot='Aminotransferase'
            elif tag=='1-Glutamine Amidotransferase':
                  self.glutamine_amidotransferase()
                  self.mot='glu_amidotransferase'
            elif tag =='1-Thymidine Kinase':
                  self.thymidinekinase()
                  self.mot='Tkinase'
            elif tag =='1-ACTase':
                  self.ACTase()
                  self.mot='actase'
            elif tag=='1-Adenylate Kinase':
                  self.adenylatekinase()
                  self.mot='adenylatekinase'
            elif tag=='1-SRC Family Kinase':
                  self.tyrosinekinase()
                  self.mot='SRC-Kinase'
            elif tag=='1-Hhal Methyltransferase':
                  self.hhal()
                  self.mot='hhal'
            elif tag=='1-Superoxide Dismutase':
                  self.superoxide()
                  self.mot='superoxide' 
            elif tag=='1-Peroxidase':
                  self.peroxidase()
                  self.mot='Peroxidase'
            elif tag=='1-Alcohol Dehydrogenase':
                  self.alcoholdehyd()
                  self.mot= 'alcoholdehyd'
            elif tag=='1-Aldose Reductase':
                  self.aldoreductase()
                  self.mot='aldoreductase'
            elif tag=='1-NAD Reductase':
                  self.nadhbinder()
                  self.mot='NAD-reductase'
            elif tag=='1-NAD Reductase2':
                  self.nadhbinder2()
                  self.mot='NAD-reductase2'
            elif tag =='2-Zinc Finger':
                  self.zincfinger()
                  self.mot='Zinc_finger'
            elif tag =='2-DNA Ligase':
                  self.dnaligase()
                  self.mot='ligase'
            elif tag =='2-Fucose Isomerase':
                  self.fisomerase()
                  self.mot='fucoseisomerase'
            elif tag =='2-Triose Phosphate Isomerase':
                  self.trioseisomerase()
                  self.mot='TrioseIsomerase'
            elif tag=='2-FK506 Cis-Trans':
                  self.cistransisomerase()
                  self.mot='Cis-trans'
            elif tag =='2-Carbonic Anhydrase':
                  self.carbanhyd()
                  self.mot='carbonicanhydrase'
            elif tag=='2-Carbon Carbon':
                  self.carboncarbon()
                  self.mot='carboncarbon'
            elif tag=='2-Chondroitinase':
                  self.chondrolyase()
                  self.mot='chondroitinase'
            elif tag =='2-Hyaluronate-Lyase':
                  self.hyaluronlyase()
                  self.mot='Hyaluronate_Lyase'
            elif tag=='2-Exonuclease 3':
                  self.exonucleaseiii()
                  self.mot='Exonuclease3'
            elif tag=='2-Citrate Synthase':
                  self.citratesynth()
                  self.mot='Citrate_Synth'
            elif tag =='2-Serine Protease':
                  self.serineprotease()
                  self.mot='serineprotease'
            elif tag == '2-Papain Like':
                  self.paplike()
                  self.mot='paplike'
            elif tag == '2-Metalloprotease':
                  self.metalloprotease()
                  self.mot='metalloprotease'
            elif tag == '2-Tyrosine Phosphatase':
                  self.tyrophos()
                  self.mot= 'tyrophos'
            elif tag == '2-Beta Lactamase':
                  self.Blactamase()
                  self.mot='lactamase'
            elif tag == '2-O-Glycosyl':
                  self.oglycosyl()
                  self.mot='o-glycosyl'
            elif tag == '2-Cephalosporin deacetylase':
                  self.cephdeacetylase()
                  self.mot='deacetylase'
            elif tag =='2-Amino Transferase':
                  self.aminotransferase()
                  self.mot='Aminotransferase'
            elif tag=='2-Glutamine Amidotransferase':
                  self.glutamine_amidotransferase()
                  self.mot='glu_amidotransferase'
            elif tag =='2-Thymidine Kinase':
                  self.thymidinekinase()
                  self.mot='Tkinase'
            elif tag =='2-ACTase':
                  self.ACTase()
                  self.mot='actase'
            elif tag=='2-Adenylate Kinase':
                  self.adenylatekinase()
                  self.mot='adenylatekinase'
            elif tag=='2-SRC Family Kinase':
                  self.tyrosinekinase()
                  self.mot='SRC-Kinase'
            elif tag=='2-Hhal Methyltransferase':
                  self.hhal()
                  self.mot='hhal'
            elif tag=='2-Superoxide Dismutase':
                  self.superoxide()
                  self.mot='superoxide' 
            elif tag=='2-Peroxidase':
                  self.peroxidase()
                  self.mot='Peroxidase'
            elif tag=='2-Alcohol Dehydrogenase':
                  self.alcoholdehyd()
                  self.mot= 'alcoholdehyd'
            elif tag=='2-Aldose Reductase':
                  self.aldoreductase()
                  self.mot='aldoreductase'
            elif tag=='2-NAD Reductase':
                  self.nadhbinder()
                  self.mot='NAD-reductase'
            elif tag=='2-NAD Reductase2':
                  self.nadhbinder2()
                  self.mot='NAD-reductase2'

        except:
            import tkMessageBox
            tkMessageBox.showinfo('Alert', 'There is no motif there')
        
    #def custom motif dropdown selection
            
    def set_motifA(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mA = 'gly'
      elif tag=='ala':
              self.mA = 'ala'
      elif tag=='val':
              self.mA = 'val'
      elif tag=='leu':
              self.mA = 'leu'
      elif tag=='ile':
              self.mA = 'ile'
      elif tag=='met':
              self.mA = 'met'
      elif tag=='pro':
              self.mA = 'pro'
      elif tag=='phe':
              self.mA = 'phe'
      elif tag=='tyr':
              self.mA = 'tyr'
      elif tag=='trp':
              self.mA = 'trp'
      elif tag=='ser':
              self.mA = 'ser'
      elif tag=='thr':
              self.mA = 'thr'
      elif tag=='cys':
              self.mA = 'cys'
      elif tag=='lys':
              self.mA = 'lys'
      elif tag=='arg':
              self.mA = 'arg'
      elif tag=='his':
              self.mA = 'his'
      elif tag=='asp':
              self.mA = 'asp'
      elif tag=='glu':
              self.mA = 'glu'
      elif tag=='asn':
              self.mA = 'asn'
      elif tag=='gln':
              self.mA = 'gln'

    def set_motifB(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mB = 'gly'
      elif tag=='ala':
              self.mB = 'ala'
      elif tag=='val':
              self.mB = 'val'
      elif tag=='leu':
              self.mB = 'leu'
      elif tag=='ile':
              self.mB = 'ile'
      elif tag=='met':
              self.mB = 'met'
      elif tag=='pro':
              self.mB = 'pro'
      elif tag=='phe':
              self.mB = 'phe'
      elif tag=='tyr':
              self.mB = 'tyr'
      elif tag=='trp':
              self.mB = 'trp'
      elif tag=='ser':
              self.mB = 'ser'
      elif tag=='thr':
              self.mB = 'thr'
      elif tag=='cys':
              self.mB = 'cys'
      elif tag=='lys':
              self.mB = 'lys'
      elif tag=='arg':
              self.mB = 'arg'
      elif tag=='his':
              self.mB = 'his'
      elif tag=='asp':
              self.mB = 'asp'
      elif tag=='glu':
              self.mB = 'glu'
      elif tag=='asn':
              self.mB = 'asn'
      elif tag=='gln':
              self.mB = 'gln'


    def set_motifC(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mC = 'gly'
      elif tag=='ala':
              self.mC = 'ala'
      elif tag=='val':
              self.mC = 'val'
      elif tag=='leu':
              self.mC = 'leu'
      elif tag=='ile':
              self.mC = 'ile'
      elif tag=='met':
              self.mC = 'met'
      elif tag=='pro':
              self.mC = 'pro'
      elif tag=='phe':
              self.mC = 'phe'
      elif tag=='tyr':
              self.mC = 'tyr'
      elif tag=='trp':
              self.mC = 'trp'
      elif tag=='ser':
              self.mC = 'ser'
      elif tag=='thr':
              self.mC = 'thr'
      elif tag=='cys':
              self.mC = 'cys'
      elif tag=='lys':
              self.mC = 'lys'
      elif tag=='arg':
              self.mC = 'arg'
      elif tag=='his':
              self.mC = 'his'
      elif tag=='asp':
              self.mC = 'asp'
      elif tag=='glu':
              self.mC = 'glu'
      elif tag=='asn':
              self.mC = 'asn'
      elif tag=='gln':
              self.mC = 'gln'

    def set_motifD(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mD = 'gly'
      elif tag=='ala':
              self.mD = 'ala'
      elif tag=='val':
              self.mD = 'val'
      elif tag=='leu':
              self.mD = 'leu'
      elif tag=='ile':
              self.mD = 'ile'
      elif tag=='met':
              self.mD = 'met'
      elif tag=='pro':
              self.mD = 'pro'
      elif tag=='phe':
              self.mD = 'phe'
      elif tag=='tyr':
              self.mD = 'tyr'
      elif tag=='trp':
              self.mD = 'trp'
      elif tag=='ser':
              self.mD = 'ser'
      elif tag=='thr':
              self.mD = 'thr'
      elif tag=='cys':
              self.mD = 'cys'
      elif tag=='lys':
              self.mD = 'lys'
      elif tag=='arg':
              self.mD = 'arg'
      elif tag=='his':
              self.mD = 'his'
      elif tag=='asp':
              self.mD = 'asp'
      elif tag=='glu':
              self.mD = 'glu'
      elif tag=='asn':
              self.mD = 'asn'
      elif tag=='gln':
              self.mD = 'gln'

     #def custom motif dropdown selection
    def set_motifAA(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mAA = 'gly'
      elif tag=='ala':
              self.mAA = 'ala'
      elif tag=='val':
              self.mAA = 'val'
      elif tag=='leu':
              self.mAA = 'leu'
      elif tag=='ile':
              self.mAA = 'ile'
      elif tag=='met':
              self.mAA = 'met'
      elif tag=='pro':
              self.mAA = 'pro'
      elif tag=='phe':
              self.mAA = 'phe'
      elif tag=='tyr':
              self.mAA = 'tyr'
      elif tag=='trp':
              self.mAA = 'trp'
      elif tag=='ser':
              self.mAA = 'ser'
      elif tag=='thr':
              self.mAA = 'thr'
      elif tag=='cys':
              self.mAA = 'cys'
      elif tag=='lys':
              self.mAA = 'lys'
      elif tag=='arg':
              self.mAA = 'arg'
      elif tag=='his':
              self.mAA = 'his'
      elif tag=='asp':
              self.mAA = 'asp'
      elif tag=='glu':
              self.mAA = 'glu'
      elif tag=='asn':
              self.mAA = 'asn'
      elif tag=='gln':
              self.mAA = 'gln'

    def set_motifAB(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mAB = 'gly'
      elif tag=='ala':
              self.mAB = 'ala'
      elif tag=='val':
              self.mAB = 'val'
      elif tag=='leu':
              self.mAB = 'leu'
      elif tag=='ile':
              self.mAB = 'ile'
      elif tag=='met':
              self.mAB = 'met'
      elif tag=='pro':
              self.mAB = 'pro'
      elif tag=='phe':
              self.mAB = 'phe'
      elif tag=='tyr':
              self.mAB = 'tyr'
      elif tag=='trp':
              self.mAB = 'trp'
      elif tag=='ser':
              self.mAB = 'ser'
      elif tag=='thr':
              self.mAB = 'thr'
      elif tag=='cys':
              self.mAB = 'cys'
      elif tag=='lys':
              self.mAB = 'lys'
      elif tag=='arg':
              self.mAB = 'arg'
      elif tag=='his':
              self.mAB = 'his'
      elif tag=='asp':
              self.mAB = 'asp'
      elif tag=='glu':
              self.mAB = 'glu'
      elif tag=='asn':
              self.mAB = 'asn'
      elif tag=='gln':
              self.mAB = 'gln'


    def set_motifAC(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mAC = 'gly'
      elif tag=='ala':
              self.mAC = 'ala'
      elif tag=='val':
              self.mAC = 'val'
      elif tag=='leu':
              self.mAC = 'leu'
      elif tag=='ile':
              self.mAC = 'ile'
      elif tag=='met':
              self.mAC = 'met'
      elif tag=='pro':
              self.mAC = 'pro'
      elif tag=='phe':
              self.mAC = 'phe'
      elif tag=='tyr':
              self.mAC = 'tyr'
      elif tag=='trp':
              self.mAC = 'trp'
      elif tag=='ser':
              self.mAC = 'ser'
      elif tag=='thr':
              self.mAC = 'thr'
      elif tag=='cys':
              self.mAC = 'cys'
      elif tag=='lys':
              self.mAC = 'lys'
      elif tag=='arg':
              self.mAC = 'arg'
      elif tag=='his':
              self.mAC = 'his'
      elif tag=='asp':
              self.mAC = 'asp'
      elif tag=='glu':
              self.mAC = 'glu'
      elif tag=='asn':
              self.mAC = 'asn'
      elif tag=='gln':
              self.mAC = 'gln'

    def set_motifAD(self, tag):
      cmd.deselect()
      if tag=='gly':
              self.mAD = 'gly'
      elif tag=='ala':
              self.mAD = 'ala'
      elif tag=='val':
              self.mAD = 'val'
      elif tag=='leu':
              self.mAD = 'leu'
      elif tag=='ile':
              self.mAD = 'ile'
      elif tag=='met':
              self.mAD = 'met'
      elif tag=='pro':
              self.mAD = 'pro'
      elif tag=='phe':
              self.mAD = 'phe'
      elif tag=='tyr':
              self.mAD = 'tyr'
      elif tag=='trp':
              self.mAD = 'trp'
      elif tag=='ser':
              self.mAD = 'ser'
      elif tag=='thr':
              self.mAD = 'thr'
      elif tag=='cys':
              self.mAD = 'cys'
      elif tag=='lys':
              self.mAD = 'lys'
      elif tag=='arg':
              self.mAD = 'arg'
      elif tag=='his':
              self.mAD = 'his'
      elif tag=='asp':
              self.mAD = 'asp'
      elif tag=='glu':
              self.mAD = 'glu'
      elif tag=='asn':
              self.mAD = 'asn'
      elif tag=='gln':
              self.mAD = 'gln'

              
#Custom motif functions            


    def bimotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mA = self.mA
          mB = self.mB
          cmd.do('sel AA, resn %s within %s of resn %s' % (mA, self.selA.get(), mB))
          cmd.do('sel BB, resn %s within %s of resn %s' % (mB, self.selA.get(), mA))
          cmd.select('motif', 'byres AA | byres BB')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A and B')

    def trimotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mA = self.mA
          mB = self.mB
          mC = self.mC
          cmd.do('sel AA, resn %s within %s of resn %s' % (mA, self.selA.get(), mB))
          cmd.do('sel BB, resn %s within %s of resn %s' % (mB, self.selA.get(), mA))
          cmd.do('sel CC, resn %s within %s of resn %s' % (mC, self.selB.get(), mB))
          cmd.select('motif', 'byres AA | byres BB | byres CC')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
          cmd.delete('CC')
      except:
          import tkMessageBox
          tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A, B, and C')


    def quadmotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mA = self.mA
          mB = self.mB
          mC = self.mC
          mD = self.mD
          cmd.do('sel AA, resn %s within %s of resn %s' % (mA, self.selA.get(), mB))
          cmd.do('sel BB, resn %s within %s of resn %s' % (mB, self.selA.get(), mA))
          cmd.do('sel CC, resn %s within %s of resn %s' % (mC, self.selB.get(), mB))
          cmd.do('sel DD, resn %s within %s of resn %s' % (mD, self.selC.get(), mC))
          cmd.select('motif', 'byres AA | byres BB | byres CC')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
          cmd.delete('CC')
          cmd.delete('DD')
      except:
          import tkMessageBox
          tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')

    def Abimotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mAA = self.mAA
          mAB = self.mAB
          cmd.do('sel AA, resn %s within %s of resn %s' % (mAA, self.selAB.get(), mAB))
          cmd.do('sel BB, resn %s within %s of resn %s' % (mAB, self.selAB.get(), mAA))
          cmd.select('motif', 'byres AA | byres BB')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
      except:
        import tkMessageBox
        tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A and B')

    def Atrimotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mAA = self.mAA
          mAB = self.mAB
          mAC = self.mAC
          cmd.do('sel AA1, resn %s within %s of resn %s' % (mAA, self.selAB.get(), mAB))
          cmd.select('AA2', 'resn %s within %s of resn %s' % (mAA, self.selAC.get(), mAC))
          cmd.select('AA', 'byres AA1 and byres AA2')
          cmd.do('sel BB1, resn %s within %s of resn %s' % (mAB, self.selAB.get(), mAA))
          cmd.select('BB2', 'resn %s within %s of resn %s' % (mAB, self.selBC.get(), mAC))
          cmd.select('BB', 'byres BB1 and byres BB2')          
          cmd.do('sel CC1, resn %s within %s of resn %s' % (mAC, self.selBC.get(), mAB))
          cmd.select('CC2', 'resn %s within %s of resn %s' % (mAC, self.selAC.get(), mAA))
          cmd.select('CC', 'byres CC1 and byres CC2')
          cmd.select('motif', 'byres AA | byres BB | byres CC')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
          cmd.delete('CC')
      except:
          import tkMessageBox
          tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A, B, and C')


    def Aquadmotif(self):
      try:
          self.update(self.p)
          objects = cmd.get_names('all')
          checkitforthese()
          set_defaults()
          delcrea()
          cmd.delete('motif')
          cmd.hide('everything')
          mAA = self.mAA
          mAB = self.mAB
          mAC = self.mAC
          mAD = self.mAD
          cmd.do('sel AA1, resn %s within %s of resn %s' % (mAA, self.selAB.get(), mAB))
          cmd.select('AA2', 'resn %s within %s of resn %s' % (mAA, self.selAC.get(), mAC))
          cmd.select('AA3', 'resn %s within %s of resn %s' % (mAA, self.selAD.get(), mAD))
          cmd.select('AA', 'byres AA1 and byres AA2 and byres AA3')
          cmd.do('sel BB1, resn %s within %s of resn %s' % (mAB, self.selAB.get(), mAA))
          cmd.select('BB2', 'resn %s within %s of resn %s' % (mAB, self.selBC.get(), mAC))
          cmd.select('BB3', 'resn %s within %s of resn %s' % (mAB, self.selBD.get(), mAD))
          cmd.select('BB', 'byres BB1 and byres BB2 and byres BB3')          
          cmd.do('sel CC1, resn %s within %s of resn %s' % (mAC, self.selBC.get(), mAB))
          cmd.select('CC2', 'resn %s within %s of resn %s' % (mAC, self.selAC.get(), mAA))
          cmd.select('CC3', 'resn %s within %s of resn %s' % (mAC, self.selCD.get(), mAD))
          cmd.select('CC', 'byres CC1 and byres CC2 and byres CC3')
          cmd.do('sel DD1, resn %s within %s of resn %s' % (mAD, self.selAD.get(), mAA))
          cmd.select('DD2', 'resn %s within %s of resn %s' % (mAD, self.selBD.get(), mAB))
          cmd.select('DD3', 'resn %s within %s of resn %s' % (mAD, self.selCD.get(), mAC))
          cmd.select('DD', 'byres DD1 and byres DD2 and byres DD3')
          cmd.select('motif', 'byres AA | byres BB | byres CC | byres DD')
          cmd.show('cartoon', 'all')
          cmd.set('cartoon_transparency', '0.5', 'all')
          cmd.show('sticks', 'motif')
          cmd.set('stick_radius','0.5')
          cpkmotif()
          cmd.orient('motif')
          cmd.deselect()
          cmd.delete('AA')
          cmd.delete('BB')
          cmd.delete('CC')
          cmd.delete('DD')
      except:
          import tkMessageBox
          tkMessageBox.showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')
 
    #reset the range sliders   
    def resetmotif(self):
      self.selA.set(4.0)
      self.selB.set(4.0)
      self.selC.set(4.0)
      self.selAB.set(4.0)
      self.selAC.set(4.0)
      self.selAD.set(4.0)
      self.selBC.set(4.0)
      self.selBD.set(4.0)
      self.selCD.set(4.0)

    def resetrange(self):
      self.range.set(1.0)
      
    def setcusmotif(self):
        a = []
        for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
            a.append(object)
        self.motifdrop.setlist(a)

    def runcusmotif(self):
            a = ['']
            for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
                a.append(object)
            motif = self.motifdrop.getcurselection()
            for item in motif:
                tag = item
            try:
               for i in range(1, 100, 1):
                    if a[i] in tag:
                        cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[i])
            except:
                pass
          
        
#No more motifs......Hurray


    #--------------------------------------#
    #			             #
    #COMMANDS" TAB METHODS  #
    #                                                                   #
    #--------------------------------------#	
    # Color the molecule
    def color_cpk(self, str ):
      color_cpk()

    # Attempt to simulate the default PyMOL colorings
    def color_default(self):
	cmd.color("green", "elem C")
	cmd.color("red", "elem O")
	cmd.color("blue", "elem N")
	if script=='1':
                      f.write('''cmd.color("green", "elem C")
cmd.color("red", "elem O")
cmd.color("blue", "elem N")\n''')
    
    # Show ligands as spheres
    def space_fill_ligand(self):
	cmd.select("Bad", "resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c+t+u+HOH+MSE")
	cmd.select("ligand","!Bad")
	cmd.hide("everything", "ligand")
	cmd.show("spheres", "ligand")
	cmd.delete("Bad")
	if script=='1':
                      f.write('''cmd.select("Bad", "resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c+t+u+HOH+MSE")
cmd.select("ligand","!Bad")
cmd.hide("everything", "ligand")
cmd.show("spheres", "ligand")
cmd.delete("Bad")\n''')
	cpkligands()
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
		if script=='1':
                                         f.write('''cmd.do('show everything')\n''')
    	else:
    		cmd.do('hide everything')
    		if script=='1':
                                         f.write('''cmd.do('show everything')\n''')
    		for item in list:
    			self.rep1.invoke(item)
    		for item in list2:
    			self.rep2.invoke(item)

    # Show individual representations
    def show_rep(self, tag):
        try:
            sel = self.sel
            if tag == 'Lines':
                    cmd.show('lines',sel)
                    if script=='1':
                        f.write('cmd.show('"lines"',"'+sel+'")\n')
            elif tag == 'Sticks':
                    cmd.show('sticks', sel)
                    if script=='1':
                        f.write('cmd.show('"sticks"',"'+sel+'")\n')
            elif tag == 'Ribbons':
                    cmd.show('ribbon', sel)
                    if script=='1':
                        f.write('cmd.show('"ribbon"',"'+sel+'")\n')
            elif tag == 'Cartoon':
                    cmd.show('cartoon', sel)
                    if script=='1':
                        f.write('cmd.show('"cartoon"',"'+sel+'")\n')
            elif tag == 'Dots':
                    cmd.show('dots', sel)
                    if script=='1':
                        f.write('cmd.show('"dots"',"'+sel+'")\n')
            elif tag == 'Spheres':
                    cmd.show('spheres', sel)
                    if script=='1':
                        f.write('cmd.show('"spheres"',"'+sel+'")\n')
            elif tag == 'Mesh':
                    cmd.show('mesh', sel)
                    if script=='1':
                        f.write('cmd.show('"mesh"',"'+sel+'")\n')
            elif tag == 'Surface':
                    cmd.show('surface', sel)
                    if script=='1':
                        f.write('cmd.show('"surface"',"'+sel+'")\n')
            elif tag == 'Water':
                    cmd.show('(resn HOH)')
                    cmd.show('spheres', '(resn HOH)')
                    if script=='1':
                        f.write('''cmd.show('(resn HOH)')
cmd.show('spheres', '(resn HOH)')\n''')
            elif tag=='Ball and Stick':
                    cmd.set('sphere_scale', '0.35', sel)
                    cmd.show('spheres',sel)
                    cmd.show('sticks',sel)
                    if script=='1':
                        f.write('''cmd.set('sphere_scale', '0.35', "'''+sel+'''")
cmd.show('spheres',"'''+sel+'''")
cmd.show('sticks',"'''+sel+'''")\n''')
            elif tag=='Polar Contacts':
                    cmd.dist(sel+"_polar_conts",sel,sel,quiet=1,mode=2,label=0,reset=1)
                    cmd.enable(sel+"1CHO_polar_conts")
                    if script=='1':
                        f.write('''cmd.dist(sel+"_polar_conts","'''+sel+'''","'''+sel+'''",quiet=1,mode=2,label=0,reset=1)
cmd.enable('''+sel+'''"1CHO_polar_conts")\n''')

        
                    
        except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'Update Selection!')

      	    
    # Hide individual representations
    def hide_rep(self, tag):
        try:
            sel = self.sel
            if tag == 'Lines':
                    cmd.hide('lines',sel)
                    if script=='1':
                        f.write('''cmd.hide('lines',"'''+sel+'''")\n''')
            elif tag == 'Sticks':
                    cmd.hide('sticks', sel)
                    if script=='1':
                        f.write('''cmd.hide('sticks',"'''+sel+'''")\n''')
            elif tag == 'Ribbons':
                    cmd.hide('ribbon', sel)
                    if script=='1':
                        f.write('''cmd.hide('ribbon',"'''+sel+'''")\n''')
            elif tag == 'Cartoon':
                    cmd.hide('cartoon', sel)
                    if script=='1':
                        f.write('''cmd.hide('cartoon',"'''+sel+'''")\n''')
            elif tag == 'Dots':
                    cmd.hide('dots', sel)
                    if script=='1':
                        f.write('''cmd.hide('dots',"'''+sel+'''")\n''')
            elif tag == 'Spheres':
                    cmd.hide('spheres', sel)
                    if script=='1':
                        f.write('''cmd.hide('spheres',"'''+sel+'''")\n''')
            elif tag == 'Mesh':
                    cmd.hide('mesh', sel)
                    if script=='1':
                        f.write('''cmd.hide('mesh',"'''+sel+'''")\n''')
            elif tag == 'Surface':
                    cmd.hide('surface', sel)
                    if script=='1':
                        f.write('''cmd.hide('surface',"'''+sel+'''")\n''')
            elif tag == 'Water':
                    cmd.hide('(resn HOH)')
                    if script=='1':
                        f.write('''cmd.hide('(resn HOH)')\n''')
            elif tag == 'Everything':
                    cmd.hide('everything', sel)
                    if script=='1':
                        f.write('''cmd.hide('everything',"'''+sel+'''")\n''')
            elif tag=='Ball and Stick':
                    cmd.hide('spheres',sel)
                    cmd.hide('sticks',sel)
                    if script=='1':
                        f.write('''cmd.hide('spheres',"'''+sel+'''")\n''')
                    if script=='1':
                        f.write('''cmd.hide('sticks',"'''+sel+'''")\n''')
            elif tag =='Polar Contacts':
                    cmd.delete(sel+"_polar_conts")
                    if script=='1':
                        f.write(''' cmd.delete("'''+sel+'''_polar_conts")\n''')
            
        except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'Update Selection!')


     #-------------Version 2--------------#
            
    # Set selection of atoms
    #   - initial selection is 'all'
    def set_sel(self, tag):
      cmd.deselect()
      c=re.compile("^Chain")
      if tag=='All':
              self.sel = 'all'
      elif tag=='protein':
              self.sel = 'protein'
      elif tag=='nucleic_acid':
              self.sel = 'nucleic_acid'
      elif tag=='ligands':
              self.sel = 'ligands'
      elif tag=='heme':
              self.sel = 'heme'
      elif tag=='Chain-A':
            self.sel=('Chain-A')
      elif tag=='Chain-A':
            self.sel=('Chain-A')
      elif tag=='Chain-B':
            self.sel=('Chain-B')
      elif tag=='Chain-C':
            self.sel=('Chain-C')
      elif tag=='Chain-D':
            self.sel=('Chain-D')
      elif tag=='Chain-E':
            self.sel=('Chain-E')
      elif tag=='Chain-F':
            self.sel=('Chain-F')
      elif tag=='Chain-G':
            self.sel=('Chain-G')
      elif tag=='Chain-H':
            self.sel=('Chain-H')
      elif tag=='Chain-I':
            self.sel=('Chain-I')
      elif tag=='Chain-J':
            self.sel=('Chain-J')
      elif tag=='Chain-K':
            self.sel=('Chain-K')
      elif tag=='Chain-L':
            self.sel=('Chain-L')
      elif tag=='Chain-M':
            self.sel=('Chain-M')
      elif tag=='Chain-N':
            self.sel=('Chain-N')
      elif tag=='Chain-O':
            self.sel=('Chain-O')
      elif tag=='Chain-P':
            self.sel=('Chain-P')
      elif tag=='Chain-Q':
            self.sel=('Chain-Q')
      elif tag=='Chain-R':
            self.sel=('Chain-R')
      elif tag=='Chain-S':
            self.sel=('Chain-S')
      elif tag=='Chain-T':
            self.sel=('Chain-T')
      elif tag=='Chain-U':
            self.sel=('Chain-U')
      elif tag=='Chain-V':
            self.sel=('Chain-V')
      elif tag=='Chain-W':
            self.sel=('Chain-W')
      elif tag=='Chain-X':
            self.sel=('Chain-X')
      elif tag=='Chain-Y':
            self.sel=('Chain-Y')
      elif tag=='Chain-Z':
            self.sel=('Chain-Z')              
      elif tag=='Not Selected':
        try:
              cmd.select('selection', '!sele')
              cmd.deselect()
              self.sel= 'selection'
        except:
            import tkMessageBox
            tkMessageBox.showinfo("Error", 'No selection has been made')
      elif tag=='hydrophobic':
              self.sel='hydrophobic'
      elif tag=='hydrophilic':
              self.sel='hydrophilic'
      elif tag=='acidic':
              self.sel='acidic'
      elif tag=='basic':
              self.sel='basic'

    # Set selection of atoms
    #   - initial selection is 'all'
    
    def set_sel1(self, tag):
      cmd.deselect()
      c=re.compile("^Chain")
      if tag=='All':
              self.sel1 = 'all'
      elif tag=='protein':
              self.sel1 = 'protein'
      elif tag=='nucleic_acid':
              self.sel1 = 'nucleic_acid'
      elif tag=='ligands':
              self.sel1 = 'ligands'
      elif tag=='heme':
              self.sel1 = 'heme'
      elif tag=='Chain-A':
            self.sel1=('Chain-A')
      elif tag=='Chain-A':
            self.sel1=('Chain-A')
      elif tag=='Chain-B':
            self.sel1=('Chain-B')
      elif tag=='Chain-C':
            self.sel1=('Chain-C')
      elif tag=='Chain-D':
            self.sel1=('Chain-D')
      elif tag=='Chain-E':
            self.sel1=('Chain-E')
      elif tag=='Chain-F':
            self.sel1=('Chain-F')
      elif tag=='Chain-G':
            self.sel1=('Chain-G')
      elif tag=='Chain-H':
            self.sel1=('Chain-H')
      elif tag=='Chain-I':
            self.sel1=('Chain-I')
      elif tag=='Chain-J':
            self.sel1=('Chain-J')
      elif tag=='Chain-K':
            self.sel1=('Chain-K')
      elif tag=='Chain-L':
            self.sel1=('Chain-L')
      elif tag=='Chain-M':
            self.sel1=('Chain-M')
      elif tag=='Chain-N':
            self.sel1=('Chain-N')
      elif tag=='Chain-O':
            self.sel1=('Chain-O')
      elif tag=='Chain-P':
            self.sel1=('Chain-P')
      elif tag=='Chain-Q':
            self.sel1=('Chain-Q')
      elif tag=='Chain-R':
            self.sel1=('Chain-R')
      elif tag=='Chain-S':
            self.sel1=('Chain-S')
      elif tag=='Chain-T':
            self.sel1=('Chain-T')
      elif tag=='Chain-U':
            self.sel1=('Chain-U')
      elif tag=='Chain-V':
            self.sel1=('Chain-V')
      elif tag=='Chain-W':
            self.sel1=('Chain-W')
      elif tag=='Chain-X':
            self.sel1=('Chain-X')
      elif tag=='Chain-Y':
            self.sel1=('Chain-Y')
      elif tag=='Chain-Z':
            self.sel1=('Chain-Z')              
      elif tag=='Not Selected':
              cmd.select('selection', '!sele')
              cmd.deselect()
              self.sel1= 'selection'
      elif tag=='hydrophobic':
              self.sel1='hydrophobic'
      elif tag=='hydrophilic':
              self.sel1='hydrophilic'
      elif tag=='acidic':
              self.sel1='acidic'
      elif tag=='basic':
              self.sel1='basic'

    #preset menubar link functions
              
    def presurf(self, tag):
        if tag=='Surface':
            self.surface_view()
        elif tag=='Surface on Cartoon':
            self.surf_toon()
        elif tag=='Surface on Sticks':
            self.surf_stick()
        elif tag=='Surface on Spheres':
            self.spheresurf()
        elif tag=='Mesh on Sticks':
            self.mesh_stick()
        elif tag=='Dots on Lines':
            self.dot_line()

    def pretoon(self, tag):
        if tag=='Cartoon':
            self.std_view()
        elif tag=='Putty':
            self.show_putty()
        elif tag=='Lines on Cartoon':
            self.stick_toon()
        elif tag=='Color by Chain':
            color_by_chain()

    def preres(self, tag):
        if tag=='Aromatics':
            self.color_aromatics()
        elif tag=='Show Charged':
            self.show_charged()
        elif tag=='Solubility':
            self.view_polarity()

    def prerov(self, tag):
        if tag=='Roving Sticks':
            self.rovingstickers()
        elif tag=='Roving Ball&Sticks':
            self.rovingballstick()
        elif tag=='Roving Spheres':
            self.rovingspheres()
        elif tag=='Roving Lines':
            self.rovinglines()

    def preele(self, tag):
        if tag=='Mesh on Ribbon':
            self.mesh_ribbon()
        elif tag=='Dots on Sticks':
            self.dot_sticks()
        elif tag=='Surface on Lines':
            self.surfinglines()

    def premisc(self, tag):
        if tag=='Hetero Atoms':
            self.show_hetero()
        elif tag=='Chain Contacts':
            self.chain_contact()
        elif tag=='DNA & RNA':
            self.show_dna_rna()
        elif tag=='CPK':
            self.show_cpk()
        elif tag=='Ball & Stick':
            self.ball_and_stick()

    def premovie(self, tag):
          if tag=='Ligand Zoom':
            self.ligandZoom()
          elif tag=='Build Protein':
            self.growProtein()
          elif tag=='Highlight Chains':
            self.highlight_chains()
          elif tag=='Rotate':
            self.rotate_y()
          elif tag=='Chain Pull':
            self.chain_pull()
          elif tag=='Ligand Pull':
            self.Ligand_Pull()
          elif tag=='Surface to Stick':
            self.surface_stick()
          elif tag=='Surface to Cartoon':
            self.surface_cartoon()
          elif tag=='Play':
            self.play()
          elif tag=='Stop':
            self.stop()
          elif tag=='Rewind':
            self.rewind()
         

    #------------------Version 1--------------#
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
        try:
            command = self.commandLine.getvalue()
            if self.cmdType == 'PyMOL':
                cmd.do(command)
                self.commandLine.clear()
            else:
                self.converter.parseIt(command, self.commandLine, self.output)
        except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'Invalid command or you must load the PDB through Pro-MOL')
       
    # Coloring on Selection
    def color_sel(self, tag):
        try:
            sel=self.sel
            if tag=='Red':
                    cmd.color('red', sel)
                    if script=='1':
                        f.write('''cmd.color('red', '''+sel+'''")\n''')
            elif tag=='Green':
                    cmd.color('green', sel)
                    if script=='1':
                        f.write('''cmd.color('green', '''+sel+'''")\n''')
            elif tag=='Orange':
                    cmd.color('orange', sel)
                    if script=='1':
                        f.write('''cmd.color('orange', '''+sel+'''")\n''')
            elif tag=='Yellow':
                    cmd.color('yellow', sel)
                    if script=='1':
                        f.write('''cmd.color('yellow', '''+sel+'''")\n''')
            elif tag=='Blue':
                    cmd.color('blue', sel)
                    if script=='1':
                        f.write('''cmd.color('blue', '''+sel+'''")\n''')
            elif tag=='Violet':
                    cmd.color('violet', sel)
                    if script=='1':
                        f.write('''cmd.color('violet', '''+sel+'''")\n''')
            elif tag=='CPK':
                    cmd.color("oxygen","(elem O and "+sel+")")
                    cmd.color("nitrogen","(elem N and "+sel+")")
                    cmd.color("sulfur","(elem S and "+sel+")")
                    cmd.color("hydrogen","(elem H and "+sel+")")
                    cmd.color("gray","(elem C and "+sel+")")
                    if script=='1':
                        f.write('''cmd.color("oxygen","(elem O and "'''+sel+'''")")
cmd.color("nitrogen","(elem N and "'''+sel+'''")")
cmd.color("sulfur","(elem S and "'''+sel+'''")")
cmd.color("hydrogen","(elem H and "'''+sel+'''")")
cmd.color("gray","(elem C and "'''+sel+'''")")\n''')
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

                            
        except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'Update Selection!')




    #------------------Version 2-----------------#
            
    #--------------------------------------#
    #					   #
    #           SAVE   METHODS             #
    #                                      #
    #--------------------------------------#	 
    def imgSave(self):
    	import tkFileDialog
    	file = tkFileDialog.asksaveasfilename(defaultextension=".png", initialdir="./PyMOL/")
        if len(file)>0:
            cmd.save(file)
            
 
    #------
    #Brett and Charlie's (first attempt) code--------
    #--Ray tracing with an auto calculator for height and width----
    def imgraysave(self):
        import tkFileDialog
        root = Tk()
        root.geometry('226x147+140+140')
        root.title('Ray Trace')
        msg = Message(root, width = 200, text="You must Ray Trace before saving for a higher resolution image ")
        msg.place(x=5, y=5)
        a_label = Label(root, text = "Width")
        name1 = Entry(root, width = 12,)
        name1.insert(0, 640)
        b_label = Label(root, text = "Height")
        name2 = Entry(root, width = 12,)
        a_button = Button(root, text = "Ray Trace")
        a_label.place(x=10,y=50)
        b_button = Button(root, text = "Save")
        name1.place(x=50,y=50)
        b_label.place(x=10,y=80)
        name2.place(x=50,y=80)
        name2.insert(0, 480)
        a_button.place(x=10,y=110)        
        b_button.place(x=80,y=110)
        c_button = Button(root, text = "Auto Calc")
        c_button.place(x=150,y=64)
        d_button = Button(root, text = 'Help')
        d_button.place(x = 150, y=110)
        d_button.configure(width = "8")
        b_button.configure(width = "8")
        a_button.configure(width = "8")
        c_button.configure(width = "8")
        #Help Message Box
        def rthelp(event):
            import tkFileDialog
            import tkMessageBox
            tkMessageBox.showinfo("Help","To save a higher resolution image you \nmust input width and height paramaters.\n \nOr input just width or just height and\n use the Auto Calc button to get the other.\n\n Paramaters should be under 5 digits\n or else Ray Trace may take a long time. \n \nThen click Save to save your image.")
            root.mainloop()
        d_button.bind('<Button-1>', rthelp)
        #Auto Calc Function
        def autocalc(event):
            try:
                if len(name1.get()) >= 1:
                    name2.delete(0,20)
                    name2.insert(0, int(int(name1.get())*.75))
                elif len(name2.get()) >= 1:
                    name1.delete(0,20)
                    name1.insert(0, int(int(name2.get())*1.3333333333333333333333333333))
            
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", "Enter an integer value for width or height")
                root.mainloop()
        c_button.bind('<Button-1>',autocalc)
        #Defines ray trace function
        def raytrace(event):
            try:
                if len(name1.get()) > 3:
                  import tkFileDialog
                  import tkMessageBox
                  tkMessageBox.showinfo("Ray Trace","You have entered a large value. Please be patient.\nClick OK to continue.")         
                  cmd.ray(name1.get(),name2.get())
                  root.mainloop()
                else:
                  cmd.ray(name1.get(),name2.get())
                  root.mainloop()
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", "Enter an integer value for width and height")
                root.mainloop()
        def savestop(event):
            file = tkFileDialog.asksaveasfilename(defaultextension=".png", initialdir="./PyMOL/")
            if len(file)>0:
                cmd.save(file)
            root.destroy()
        a_button.bind('<Button-1>',raytrace)
        b_button.bind('<Button-1>',savestop)         
        root.mainloop()
        
  
        
    #---------Version 1---------------#

    #For future modifications---->Better to use Tcl/Tk methods instead of
    #Megawidgets for button creations and GUI manipulation, not enough time to
    #completely redo though

        
    #--------------------------------------#
    #					   #
    #         UTILITY  METHODS             #
    #                                      #
    #--------------------------------------#	 
    # ADD BUTTONS
    # Create and add buttons to the GUI
    def buttonAdd(self,frame,text,size,cmd,gridrow,gridcol,gridstick):
        #the button
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
    #         Display      METHODS         #
    #                                      #
    #--------------------------------------#
    # handle stereo commands
    def stereo_switch(self, tag):
        if tag == 'Off':
            cmd.stereo('off')
            if script=='1':
                        f.write('''cmd.stereo('off')\n''')
        elif tag == 'Quad':
            cmd.stereo('off')
            cmd.stereo('cross')
            cmd.stereo('quadbuffer')
            cmd.stereo('on')
            if script=='1':
                        f.write('''cmd.stereo('off')
cmd.stereo('cross')
cmd.stereo('quadbuffer')
cmd.stereo('on')\n''')
        elif tag == 'Cross-Eye':
            cmd.stereo('off')
            cmd.stereo('cross')
            cmd.stereo('on')
            if script=='1':
                        f.write('''cmd.stereo('off')
cmd.stereo('cross')
cmd.stereo('on')\n''')
        else:
            cmd.stereo('off')
            cmd.stereo('walleye')
            cmd.stereo('on')
            if script=='1':
                        f.write('''cmd.stereo('off')
cmd.stereo('walleye')
cmd.stereo('on')\n''')
        
    # change background colors
    def bgcolor_switch(self, tag):
        if tag == 'Black':
            cmd.do('bg_color black')
            if script=='1':
                        f.write('''cmd.do('bg_color black')\n''')
        elif tag == 'White':
            cmd.do('bg_color white')
            if script=='1':
                        f.write('''cmd.do('bg_color white')\n''')
        elif tag == 'Grey':
            cmd.do('bg_color grey')
            if script=='1':
                        f.write('''cmd.do('bg_color grey')\n''')
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
        		if script=='1':
                                         f.write('''cmd.set_color('newcolor', '''+colorArray+'''')
cmd.do('bg_color newcolor')\n''')
        else: 
       	    self.do_nothing()
        
    # change the color space
    def cspace_switch(self, tag):
	if tag == 'PyMOL':
	    cmd.space('pymol')
	    if script=='1':
                            f.write('''cmd.space('pymol')\n''')
	elif tag == 'Publications':
	    cmd.space('rgb')
	    if script=='1':
                            f.write('''cmd.space('rgb')\n''')
	else: 
	    cmd.space('cmyk')
	    if script=='1':
                            f.write('''cmd.space('cmyk')\n''')
	    
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
        	if script=='1':
                            f.write('''cmd.show('(resn HOH)')
cmd.show('spheres', '(resn HOH)')\n''')
        else:
        	cmd.hide('(resn HOH)')
        	if script=='1':
                            f.write('''cmd.hide('(resn HOH)')\n''')

    #--------------------------------------#
    #				#
    #         PARSING  METHODS             #
    #                                                                   #
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
    def rotate_y(*args):
        cmd.mset()
        cmd.mset('1','180')
        cmd.util.mroll('1','180','1')
        cmd.mplay()
    cmd.extend('rotate_y',rotate_y)


    # Movie to show locations of each of the chains in the molecule
    #does not run on external pdbs - Brett
    def highlight_chains(*args):
        delcrea()
	cmd.mstop()
	cmd.mclear()
	cmd.mset()
	set_defaults()
	
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
    cmd.extend('highlight_chains',highlight_chains)
    
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
    
    #does not run on external pdbs 
    def ligandZoom(self):
        try:
            delcrea()
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
                set_defaults()
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
                    color_cpk(' and (byres (ligands and '+ids[i]+')around 5)')
                    color_cpk(' and ligands')
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
	except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'You must open the PDB file through Pro-MOL')
     #fixed to work on externally loaded pdbs by Brett and Charlie
    def growProtein(self):
        delcrea()
   	cmd.mstop()
	cmd.mclear()
	cmd.mset()
	self.update(self.p)
    	objects = cmd.get_names('all')
        checkitforthese()
    	if 'protein' in objects:
            set_defaults()
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
    	        cpknucleic()
   	    
    	    if 'rna' in objects:
 	        cmd.show('sticks','rna')
 	        cmd.show('spheres','rna')
    	        cmd.set('sphere_scale','0.4','rna')
    	        color_cpk(' & rna')
    	     	        
    	    # coloring the protein and secondary structures
    	    cmd.color('white', 'protein')
       	    cmd.color('purple', 'helix')
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
    	    cmd.color('blue', 'surface')
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



    	    
    	#---------Version 2--------#
	 
    #--------Haven't you seeen my MOVIES!-----------
	#surface over cartoon movie
    def surface_cartoon(*args):
          delcrea()
          try:
            self = args[0]
            self.update(self.p)
          except:
            pass
          cmd.mstop()
          cmd.mclear()
          cmd.mset()
          cmd.mset('1','60')
          cmd.hide('everything')
          objects = cmd.get_names('all')
          cmd.create('surface','all')                  
          cmd.create('cartoon','all') 
          cmd.show('cartoon', 'cartoon')
          cmd.show('surface', 'surface')
          cmd.color('grey', 'surface')         
          cmd.color('red', 'elem O')
          cmd.color('blue', 'elem N')
          cmd.set("cartoon_fancy_helices", "1")
          cmd.set("cartoon_fancy_sheets", "1")
          cmd.do('mdo 1: set transparency=0.75, surface;')
          cmd.do('mdo 2: set transparency=0.7, surface;')
          cmd.do('mdo 3: set transparency=0.65, surface;')
          cmd.do('mdo 4: set transparency=0.6, surface;')
          cmd.do('mdo 5: set transparency=0.55, surface;')
          cmd.do('mdo 6: set transparency=0.5, surface;')
          cmd.do('mdo 7: set transparency=0.45, surface;')
          cmd.do('mdo 8: set transparency=0.4, surface;')
          cmd.do('mdo 9: set transparency=0.35, surface;')
          cmd.do('mdo 10: set transparency=0.3, surface;')
          cmd.do('mdo 11: set transparency=0.25, surface;')
          cmd.do('mdo 12: set transparency=0.2, surface;')
          cmd.do('mdo 13: set transparency=0.15, surface;')
          cmd.do('mdo 14: set transparency=0.1, surface;')
          cmd.do('mdo 15: set transparency=0.05, surface;')
          cmd.do('mdo 16: set transparency=0, surface;')
          cmd.do('mdo 17: set transparency=0, surface;')
          cmd.do('mdo 19: set transparency=0, surface;')
          cmd.do('mdo 20: set transparency=0, surface;')
          cmd.do('mdo 21: set transparency=0, surface;')
          cmd.do('mdo 22: set transparency=0, surface;')
          cmd.do('mdo 23: set transparency=0, surface;')
          cmd.do('mdo 24: set transparency=0, surface;')
          cmd.do('mdo 25: set transparency=0, surface;')
          cmd.do('mdo 26: set transparency=0, surface;')
          cmd.do('mdo 27: set transparency=0, surface;')
          cmd.do('mdo 28: set transparency=0, surface;')
          cmd.do('mdo 29: set transparency=0.05, surface;')
          cmd.do('mdo 30: set transparency=0.1, surface;')
          cmd.do('mdo 31: set transparency=0.15, surface;')
          cmd.do('mdo 32: set transparency=0.2, surface;')
          cmd.do('mdo 33: set transparency=0.25, surface;')
          cmd.do('mdo 34: set transparency=0.3, surface;')
          cmd.do('mdo 35: set transparency=0.35, surface;')
          cmd.do('mdo 36: set transparency=0.4, surface;')
          cmd.do('mdo 37: set transparency=0.45, surface;')
          cmd.do('mdo 38: set transparency=0.5, surface;')
          cmd.do('mdo 39: set transparency=0.55, surface;')
          cmd.do('mdo 40: set transparency=0.6, surface;')
          cmd.do('mdo 41: set transparency=0.65, surface;')
          cmd.do('mdo 42: set transparency=0.7, surface;')
          cmd.do('mdo 43: set transparency=0.75, surface;')
          cmd.do('mdo 44: set transparency=0.8, surface;')
          cmd.do('mdo 45: set transparency=0.85, surface;')
          cmd.do('mdo 46: set transparency=0.9, surface;')
          cmd.do('mdo 47: set transparency=0.9, surface;')
          cmd.do('mdo 48: set transparency=0.9, surface;')
          cmd.do('mdo 49: set transparency=0.85, surface;')
          cmd.do('mdo 50: set transparency=0.85, surface;')
          cmd.do('mdo 51: set transparency=0.85, surface;')
          cmd.do('mdo 52: set transparency=0.85, surface;')
          cmd.do('mdo 53: set transparency=0.85, surface;')
          cmd.do('mdo 54: set transparency=0.85, surface;')
          cmd.do('mdo 55: set transparency=0.85, surface;')
          cmd.do('mdo 56: set transparency=0.85, surface;')
          cmd.do('mdo 57: set transparency=0.85, surface;')
          cmd.do('mdo 58: set transparency=0.85, surface;')
          cmd.do('mdo 59: set transparency=0.85, surface;')
          cmd.do('mdo 60: set transparency=0.8, surface;')
    cmd.extend('surface_cartoon', surface_cartoon)
   
        #surface over stick movie
    def surface_stick(*args):
      delcrea()
      try:
        self = args[0]
        self.update(self.p)
      except:
        pass
      cmd.mstop()
      cmd.mclear()
      cmd.mset('1','60')
      cmd.hide('everything')
      objects = cmd.get_names('all')
      cmd.create('surface', 'all')                  
      cmd.create('sticks', 'all') 
      cmd.show('sticks', 'sticks')
      color_cpk('& sticks')
      cmd.show('surface', 'surface')
      cmd.color('grey', 'surface')   
      cmd.color('red', 'elem O')
      cmd.color('blue', 'elem N')
      cmd.do('mdo 1: set transparency=0.75, surface;')
      cmd.do('mdo 2: set transparency=0.7, surface;')
      cmd.do('mdo 3: set transparency=0.65, surface;')
      cmd.do('mdo 4: set transparency=0.6, surface;')
      cmd.do('mdo 5: set transparency=0.55, surface;')
      cmd.do('mdo 6: set transparency=0.5, surface;')
      cmd.do('mdo 7: set transparency=0.45, surface;')
      cmd.do('mdo 8: set transparency=0.4, surface;')
      cmd.do('mdo 9: set transparency=0.35, surface;')
      cmd.do('mdo 10: set transparency=0.3, surface;')
      cmd.do('mdo 11: set transparency=0.25, surface;')
      cmd.do('mdo 12: set transparency=0.2, surface;')
      cmd.do('mdo 13: set transparency=0.15, surface;')
      cmd.do('mdo 14: set transparency=0.1, surface;')
      cmd.do('mdo 15: set transparency=0.05, surface;')
      cmd.do('mdo 16: set transparency=0, surface;')
      cmd.do('mdo 17: set transparency=0, surface;')
      cmd.do('mdo 19: set transparency=0, surface;')
      cmd.do('mdo 20: set transparency=0, surface;')
      cmd.do('mdo 21: set transparency=0, surface;')
      cmd.do('mdo 22: set transparency=0, surface;')
      cmd.do('mdo 23: set transparency=0, surface;')
      cmd.do('mdo 24: set transparency=0, surface;')
      cmd.do('mdo 25: set transparency=0, surface;')
      cmd.do('mdo 26: set transparency=0, surface;')
      cmd.do('mdo 27: set transparency=0, surface;')
      cmd.do('mdo 28: set transparency=0, surface;')
      cmd.do('mdo 29: set transparency=0.05, surface;')
      cmd.do('mdo 30: set transparency=0.1, surface;')
      cmd.do('mdo 31: set transparency=0.15, surface;')
      cmd.do('mdo 32: set transparency=0.2, surface;')
      cmd.do('mdo 33: set transparency=0.25, surface;')
      cmd.do('mdo 34: set transparency=0.3, surface;')
      cmd.do('mdo 35: set transparency=0.35, surface;')
      cmd.do('mdo 36: set transparency=0.4, surface;')
      cmd.do('mdo 37: set transparency=0.45, surface;')
      cmd.do('mdo 38: set transparency=0.5, surface;')
      cmd.do('mdo 39: set transparency=0.55, surface;')
      cmd.do('mdo 40: set transparency=0.6, surface;')
      cmd.do('mdo 41: set transparency=0.65, surface;')
      cmd.do('mdo 42: set transparency=0.7, surface;')
      cmd.do('mdo 43: set transparency=0.75, surface;')
      cmd.do('mdo 44: set transparency=0.8, surface;')
      cmd.do('mdo 45: set transparency=0.85, surface;')
      cmd.do('mdo 46: set transparency=0.9, surface;')
      cmd.do('mdo 47: set transparency=0.9, surface;')
      cmd.do('mdo 48: set transparency=0.9, surface;')
      cmd.do('mdo 49: set transparency=0.85, surface;')
      cmd.do('mdo 50: set transparency=0.85, surface;')
      cmd.do('mdo 51: set transparency=0.85, surface;')
      cmd.do('mdo 52: set transparency=0.85, surface;')
      cmd.do('mdo 53: set transparency=0.85, surface;')
      cmd.do('mdo 54: set transparency=0.85, surface;')
      cmd.do('mdo 55: set transparency=0.85, surface;')
      cmd.do('mdo 56: set transparency=0.85, surface;')
      cmd.do('mdo 57: set transparency=0.85, surface;')
      cmd.do('mdo 58: set transparency=0.85, surface;')
      cmd.do('mdo 59: set transparency=0.85, surface;')
      cmd.do('mdo 60: set transparency=0.8, surface;')
    cmd.extend('surface_stick',surface_stick)
   

        #movie that pulls ligands out of  and puts them back in
    def Ligand_Pull(*args):
          delcrea()
          try:
            self.update(self.p)
          except:
            pass
          cmd.mstop()
          cmd.mclear()
          cmd.mset('1','442')
          cmd.hide('everything')
          cmd.remove('resn HOH')
          cmd.color('green', 'all')
          objects = cmd.get_names('all')          
          cmd.select("Bad", "resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c+t+u+HOH+MSE")
          cmd.select("ligand","!Bad")
          cmd.hide("everything", "ligand")
          cmd.show("spheres", "ligand")
	  cmd.show("sticks", "ligand around 6'")
          cmd.set('stick_radius','0.3','ligand around 6')
	  cmd.color('orange', 'ligand')
	  cmd.select("interaction","ligand around 6'")
	  cpkinteraction()
          cmd.delete('interaction')
          cmd.delete("Bad")
          cmd.show('cartoon', "resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR+ACD+ACE+ALB+ALI+ABU+ARO+ASX+BAS+BET+FOR+GLX+HET+HSE+HYP+HYL+ORN+PCA+SAR+TAU+TER+THY+UNK+a+g+c+t+u+HOH+MSE")
          cmd.set("cartoon_fancy_helices", "1")
          cmd.set("cartoon_fancy_sheets", "1")
          cmd.set('cartoon_transparency','0.5')
          cmd.zoom()
          cmd.orient()
          cmd.do('mdo 1: orient')
          cmd.do('mdo 2: translate [2,0,0],ligand;')
          cmd.do('mdo 3: translate [2,0,0],ligand;')
          cmd.do('mdo 4: translate [2,0,0],ligand;')
          cmd.do('mdo 5: translate [2,0,0],ligand;')
          cmd.do('mdo 6: translate [2,0,0],ligand;')
          cmd.do('mdo 7: translate [2,0,0],ligand;')
          cmd.do('mdo 8: translate [2,0,0],ligand;')
          cmd.do('mdo 9: translate [2,0,0],ligand;')
          cmd.do('mdo 10: translate [2,0,0],ligand;')
          cmd.do('mdo 11: translate [2,0,0],ligand;')
          cmd.do('mdo 12: translate [2,0,0],ligand;')
          cmd.do('mdo 13: translate [2,0,0],ligand;')
          cmd.do('mdo 14: translate [2,0,0],ligand;')
          cmd.do('mdo 15: translate [2,0,0],ligand;')
          cmd.do('mdo 16: translate [2,0,0],ligand;')
          cmd.do('mdo 17: translate [2,0,0],ligand;')
          cmd.do('mdo 18: translate [2,0,0],ligand;')
          cmd.do('mdo 19: translate [2,0,0],ligand;')
          cmd.do('mdo 20: translate [2,0,0],ligand;')
          cmd.do('mdo 21: translate [2,0,0],ligand;')
          cmd.do('mdo 22: translate [2,0,0],ligand;')
          cmd.do('mdo 23: translate [2,0,0],ligand;')
          cmd.do('mdo 24: translate [2,0,0],ligand;')
          cmd.do('mdo 25: translate [2,0,0],ligand;')
          cmd.do('mdo 26: translate [2,0,0],ligand;')
          cmd.do('mdo 27: translate [2,0,0],ligand;')
          cmd.do('mdo 28: translate [2,0,0],ligand;')
          cmd.do('mdo 29: translate [2,0,0],ligand;')
          cmd.do('mdo 30: translate [2,0,0],ligand;')
          cmd.do('mdo 31: translate [2,0,0],ligand;')
          cmd.do('mdo 32: translate [2,0,0],ligand;')
          cmd.do('mdo 33: translate [2,0,0],ligand;')
          cmd.do('mdo 34: translate [2,0,0],ligand;')
          cmd.do('mdo 35: translate [2,0,0],ligand;')
          cmd.do('mdo 36: translate [2,0,0],ligand;')
          cmd.do('mdo 37: translate [2,0,0],ligand;')
          cmd.do('mdo 38: translate [2,0,0],ligand;')
          cmd.do('mdo 39: translate [2,0,0],ligand;')
          cmd.do('mdo 40: translate [2,0,0],ligand;')
          cmd.do('mdo 41: translate [2,0,0],ligand;')
          cmd.do('mdo 42: orient')
          cmd.util.mroll('42','222','1')
          cmd.do('mdo 223: translate [-2,0,0],ligand;')
          cmd.do('mdo 224: translate [-2,0,0],ligand;')
          cmd.do('mdo 225: translate [-2,0,0],ligand;')
          cmd.do('mdo 226: translate [-2,0,0],ligand;')
          cmd.do('mdo 227: translate [-2,0,0],ligand;')
          cmd.do('mdo 228: translate [-2,0,0],ligand;')
          cmd.do('mdo 229: translate [-2,0,0],ligand;')
          cmd.do('mdo 230: translate [-2,0,0],ligand;')
          cmd.do('mdo 231: translate [-2,0,0],ligand;')
          cmd.do('mdo 232: translate [-2,0,0],ligand;')
          cmd.do('mdo 233: translate [-2,0,0],ligand;')
          cmd.do('mdo 234: translate [-2,0,0],ligand;')
          cmd.do('mdo 235: translate [-2,0,0],ligand;')
          cmd.do('mdo 236: translate [-2,0,0],ligand;')
          cmd.do('mdo 237: translate [-2,0,0],ligand;')
          cmd.do('mdo 238: translate [-2,0,0],ligand;')
          cmd.do('mdo 239: translate [-2,0,0],ligand;')
          cmd.do('mdo 240: translate [-2,0,0],ligand;')
          cmd.do('mdo 241: translate [-2,0,0],ligand;')         
          cmd.do('mdo 242: translate [-2,0,0],ligand;')
          cmd.do('mdo 243: translate [-2,0,0],ligand;')
          cmd.do('mdo 244: translate [-2,0,0],ligand;')
          cmd.do('mdo 245: translate [-2,0,0],ligand;')
          cmd.do('mdo 246: translate [-2,0,0],ligand;')
          cmd.do('mdo 247: translate [-2,0,0],ligand;')
          cmd.do('mdo 248: translate [-2,0,0],ligand;')
          cmd.do('mdo 249: translate [-2,0,0],ligand;')
          cmd.do('mdo 250: translate [-2,0,0],ligand;')
          cmd.do('mdo 251: translate [-2,0,0],ligand;')
          cmd.do('mdo 252: translate [-2,0,0],ligand;')
          cmd.do('mdo 253: translate [-2,0,0],ligand;')
          cmd.do('mdo 254: translate [-2,0,0],ligand;')
          cmd.do('mdo 255: translate [-2,0,0],ligand;')
          cmd.do('mdo 256: translate [-2,0,0],ligand;')
          cmd.do('mdo 257: translate [-2,0,0],ligand;')
          cmd.do('mdo 258: translate [-2,0,0],ligand;')
          cmd.do('mdo 259: translate [-2,0,0],ligand;')
          cmd.do('mdo 260: translate [-2,0,0],ligand;')
          cmd.do('mdo 261: translate [-2,0,0],ligand;')
          cmd.do('mdo 262: translate [-2,0,0],ligand;')
          cmd.do('mdo 263: orient')
          cmd.util.mroll('264','442','1')
    cmd.extend('ligand_pull',Ligand_Pull)


    #movie that pulls protein chains apart and shows interaction, then puts them together again
    def chain_pull(*args):
          delcrea()
          try:
            self = args[0]
            self.update(self.p)
          except:
            pass
          cmd.mstop()
          cmd.mclear()
          cmd.mset('1', '373')
          cmd.hide('everything')
          cmd.show('mesh', 'all')
          cmd.color('gray40', 'all')
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
          checkforchain()
          cmd.orient()
          objects = cmd.get_names('all')
          chainpulllist = []

          if 'Chain-A' in objects:
            chainpulllist.append('Chain-A')
          if 'Chain-B' in objects:
            chainpulllist.append('Chain-B')
          if 'Chain-C' in objects:
            chainpulllist.append('Chain-C')
          if 'Chain-D' in objects:
            chainpulllist.append('Chain-D')
          if 'Chain-E' in objects:
            chainpulllist.append('Chain-E')           
          if 'Chain-F' in objects:
            chainpulllist.append('Chain-F')
          if 'Chain-G' in objects:
            chainpulllist.append('Chain-G')
          if 'Chain-H' in objects:
            chainpulllist.append('Chain-H')
          if 'Chain-I' in objects:
            chainpulllist.append('Chain-I')
          if 'Chain-J' in objects:
            chainpulllist.append('Chain-J')
          if 'Chain-K' in objects:
            chainpulllist.append('Chain-K')
          if 'Chain-L' in objects:
            chainpulllist.append('Chain-L')
          if 'Chain-M' in objects:
            chainpulllist.append('Chain-M')
          if 'Chain-N' in objects:
            chainpulllist.append('Chain-N')
          if 'Chain-O' in objects:
            chainpulllist.append('Chain-O')
          if 'Chain-P' in objects:
            chainpulllist.append('Chain-P')
          if 'Chain-Q' in objects:
            chainpulllist.append('Chain-Q')
          if 'Chain-R' in objects:
            chainpulllist.append('Chain-R')
          if 'Chain-S' in objects:
            chainpulllist.append('Chain-S')
          if 'Chain-T' in objects:
            chainpulllist.append('Chain-T')
          if 'Chain-U' in objects:
            chainpulllist.append('Chain-U')
          if 'Chain-V' in objects:
            chainpulllist.append('Chain-V')
          if 'Chain-W' in objects:
            chainpulllist.append('Chain-W')
          if 'Chain-X' in objects:
            chainpulllist.append('Chain-X')
          if 'Chain-Y' in objects:
            chainpulllist.append('Chain-Y')
          if 'Chain-Z' in objects:
            chainpulllist.append('Chain-Z')
          
          
          if len(chainpulllist) >1:
            cmd.do('mdo 2: translate [0,0,0],'+chainpulllist[0]+';')
            cmd.do('mdo 3: translate [50,0,0],'+chainpulllist[1]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[1])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >2:
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >3:
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >4:
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >5:
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >6:
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[1])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[1] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')
  
          if len(chainpulllist) >2:
            cmd.do('mdo 4: translate [0,50,0],'+chainpulllist[2]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[2])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >3:
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >4:
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >5:
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >6:
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[2])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[2] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

          if len(chainpulllist) >3:
            cmd.do('mdo 5: translate [0,0,50],'+chainpulllist[3]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[3])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >4:
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >5:
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >6:
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[3])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[3] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

          if len(chainpulllist) >4:
            cmd.do('mdo 6: translate [-50,0,0],'+chainpulllist[4]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[4])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >5:
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >6:
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[4])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[4] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

          if len(chainpulllist) >5:
            cmd.do('mdo 7: translate [0,-50,0],'+chainpulllist[5]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[5])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >6:
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[5])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[5] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

          if len(chainpulllist) >6:
            cmd.do('mdo 8: translate [0,-50,0],'+chainpulllist[5]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[6])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >7:
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[6])
              cpkduh()
              cmd.delete('duh')    
              cmd.do('select duh,' +chainpulllist[6] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

              
          if len(chainpulllist) >7:
            cmd.do('mdo 9: translate [0,0,-50],'+chainpulllist[6]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[7])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >8:
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[7])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[7] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')
            
          if len(chainpulllist) >8:
            cmd.do('mdo 10: translate [-50,0,50],'+chainpulllist[7]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[8])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >9:
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[8])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[8] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')
            
          if len(chainpulllist) >9:
            cmd.do('mdo 11: translate [50,0,50],'+chainpulllist[8]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[9])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
            if len(chainpulllist) >10:
              cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[9])
              cpkduh()
              cmd.delete('duh')
              cmd.do('select duh,' +chainpulllist[9] + ' within 5 of ' + chainpulllist[10])
              cpkduh()
              cmd.delete('duh')

          if len(chainpulllist) >10:
            cmd.do('mdo 12: translate [50,0,-50],'+chainpulllist[10]+';')
            cmd.do('select duh,' +chainpulllist[0] + ' within 5 of ' + chainpulllist[10])
            cpkduh()
            cmd.delete('duh')    
            cmd.do('select duh,' +chainpulllist[10] + ' within 5 of ' + chainpulllist[0])
            cpkduh()
            cmd.delete('duh')
   
          cmd.do('mdo 13: zoom all')
          cmd.util.mroll('14','181','1')

          if len(chainpulllist) >1:
            cmd.do('mdo 183: translate [0,0,0],'+chainpulllist[0]+';')
            cmd.do('mdo 184: translate [-50,0,0],'+chainpulllist[1]+';')
            cmd.zoom()
          if len(chainpulllist) >2:
            cmd.do('mdo 185: translate [0,-50,0],'+chainpulllist[2]+';')
            cmd.zoom()
          if len(chainpulllist) >3:
            cmd.do('mdo 186: translate [0,0,-50],'+chainpulllist[3]+';')
            cmd.zoom()
          if len(chainpulllist) >4:
            cmd.do('mdo 187: translate [50,0,0],'+chainpulllist[4]+';')
            cmd.zoom()
          if len(chainpulllist) >5:
            cmd.do('mdo 188: translate [0,50,0],'+chainpulllist[5]+';')
            cmd.zoom()
          if len(chainpulllist) >6:
            cmd.do('mdo 189: translate [0,0,50],'+chainpulllist[6]+';')
            cmd.zoom()
          if len(chainpulllist) >7:
            cmd.do('mdo 190: translate [50,0,-50],'+chainpulllist[7]+';')
            cmd.zoom()
          if len(chainpulllist) >8:
            cmd.do('mdo 191: translate [-50,0,-50],'+chainpulllist[8]+';')
            cmd.zoom()
          if len(chainpulllist) >9:
            cmd.do('mdo 192: translate [50,0,50],'+chainpulllist[9]+';')
            cmd.zoom()
          if len(chainpulllist) >10:
            cmd.do('mdo 193: translate [-50,0,50],'+chainpulllist[10]+';')
            cmd.do('mdo 194: zoom all')
          cmd.util.mroll('195','373','1')

    cmd.extend('chain_pull',chain_pull)

    #movie controls
    def play(self):
    	cmd.mplay()
    
    def stop(self):
    	cmd.mstop()
    
    def rewind(self):
	cmd.mstop()
        cmd.rewind()

     #Ray Trace Frames   
    def ray(self,r,state):
	import tkMessageBox
     	if state:
     		if tkMessageBox.askyesno('Ray Trace Frames', 'Enabling this feature may '+
     					 'slow own the playback of your movie significantly. '+
     					 'Are you sure that you want to proceed?'):
     			cmd.set('ray_trace_frames','1')
     		else:
     			self.ray.invoke('Ray Trace Frames')
     	else:
     		cmd.set('ray_trace_frames','0')

    def cacheframe(self,r,state):
      if state:
          cmd.set('cache_frames','0')
     
          
          
      else:

          cmd.set('cache_frames', '1')
     
# Copyright Notice
# ================
# 
# The PyMOL Plugin source code in this file is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
# 
# ----------------------------------------------------------------------
# This PyMOL Plugin is Copyright (C) 2004 by Charles Moad <cmoad@indiana.edu>
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
	#f=open('/home/corey/Desktop/workfile', 'a')
	#f.write(pdbCode)
      else:
      	pdbCode=fileLoaded
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
            
            	
            #---------------THIS WAS JUST ADDED---------------------------
            self.p=PDBParser()
            self.p.readFile(outputname)
            self.update(self.p)
            cmd.deselect()

         else:
            tkMessageBox.showerror('Invalid Code',
                                   'You entered an invalid pdb code:' + pdbCode)

         os.remove(filename) # Remove tmp file (leave the pdb)
        		
   
    #------Open Help File---------#
    def help(self):
    	import webbrowser
    	try:
            webbrowser.open('./modules/pmg_tk/startup/Help/EZ-Viz.chm')
        except:
            webbrowser.open('./modules/pmg_tk/startup/Help/EZ-VizWebMain.html')
    			
    #---------------------------------------------------------------#
    #						#
    #                   GUI CREATION METHOD                         #
    #			      (INIT)		#
    #						#
    #						#
    #	             create and organize the interface              #          
    #						#
    #---------------------------------------------------------------#
    def __init__(self, app):
        
        self.pdbCode = ' '  	
        self.p=PDBParser()
        self.converter = ChimeConverter()
        
        # initialize the additional colors
        self.init_color() 
        self.sel1='all'
   
        # create the dialog box which contains the GUI
        parent = app.root
        self.dialog = Pmw.Dialog(parent,buttons = ('Open','Fetch PDB','Clear','Help', 'Thanks' ,'Quit'),
                      title = 'Pro-MOL',command = self.execute)
        
        # set the size of the 
        #self.dialog.geometry('550x550')
     	interior = self.dialog.interior()
 	
 	#TITLE BAR
 	lab = Label(interior, 
 		    text='ProMol \nDeveloped By: Charlie Westin, Brett Hanson & Paul Craig\nVersion 3.02, 2007', 
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
        #         Batch Motif  TAB             #
        #                                      #
        #--------------------------------------#

#Sweet Definitions to get stuff done in Batch TAB

	page = notebook.add("""Batch Motif""")
	group = Pmw.Group(page, tag_text='Enter Location of List')
        group.grid(row=0, column=0, padx=0, pady=0)
        interior=group.interior()
        
        myFormats = [('Text File', '*.txt')]
        
	def openfilename(event):
          filename = askopenfilename()
          entry123.insert(0, filename)
		
	def savefilename(*args):
          filename = asksaveasfilename(filetypes=myFormats,
                                       title="Save Output As...")
          if (file == 0):
            tkMessageBox.showerror('Destination File Error',
                                   'Destination does not exist')
          else:
            return filename
          
        def savefile(filename, fileString):
          newFile = open(filename,"w")
          newFile.write(fileString)
          newFile.close()               
        

        topFrame = Frame(interior)
        bottomFrame = Frame(interior)
                            
	w = Text(interior, height = 3)
        w.insert(END, "\n")
        w.insert(END, "Make a comma separated list of sensitivities")
        w.insert(END, "\n")
	w.insert(END, "Find your text file of molecules.")
        

	w.config(state = DISABLED)

        sensEntry = Entry(interior)
	entry123 = Entry(interior)
	button123 = Button(interior, 
                           text = 'Run')
	browse = Button(interior, text = 'Browse')
	browse.bind('<Button-1>', openfilename);

	w.grid(row = 0, column = 0, columnspan = 2)
        Label(interior, text = 'Sensitivities:').grid(row = 1, column = 0, sticky =  E)
        Label(interior, text = 'File:').grid(row = 2, column = 0, sticky = E)
        sensEntry.grid(row = 1, column = 1, sticky = W)
	entry123.grid(row = 2, column = 1, sticky = W)
	button123.grid(row = 3, column = 0, sticky = E)
	interior.pack()
	browse.grid(row = 3, column = 1, sticky = W)
		
        def myGetPdb(pdbNum):


            pdbCode = pdbNum
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


                #---------------THIS WAS JUST ADDED---------------------------
                self.p=PDBParser()
                self.p.readFile(outputname)
                #self.update(self.p)
                cmd.deselect()

            else:
                tkMessageBox.showerror('Invalid Code',
                           'You entered an invalid pdb code:' + pdbCode)

                os.remove(filename) # Remove tmp file (leave the pdb)

        def batchLoop(*args):
          #f = ''
          ranges = []
          string = ""
          #filename = savefilename(self)
          if (len(args) == 1):
            try:
              f=open(entry123.get())
            except:
              tkMessageBox.showerror('No input file',
                                     'You did not choose an input file yet')
          else:
            try:
              f=open('./temp', 'w')
            except:
              tkMessageBox.showerror('Woops!','Didn\'t work')
            for each in args:
              try:
                float(each)
                ranges.append(float(each))
              except:
                f.write(each + '\n')
          f.close()

          f=open('./temp')

          for line in f.readlines():
            if (len(args) == 1):
              ranges = sensEntry.get().split(',')
            for each in ranges:
              try:
                float(each)
              except ValueError:
                tkMessageBox.showerror('Incorrect Formatting',
                                       'Check the formatting of sensitivities')
                #sensEntry.delete(0,END)
              else:  
                self.range.set(each)
                line = line.strip()
                cmd.delete('all')
                myGetPdb(line)
                motifList = motifchecker(self)
                string += line
                string +='\t' + str(self.range.get()) + '\n'
                for i in motifList:
                  string += '\t'*3 + str(i) + '\n'
                print string
                filename = savefilename(self)
                savefile(filename, string)
        cmd.extend('batchLoop',batchLoop)
        #button123.bind('<Button-1>', batchLoop)
	
    #-------------Version 2----------------#

        #--------------------------------------#
        #			               #
        #            EZ-Viz TAB                #
        #                                      #
        #--------------------------------------#
        
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
          import tkFileDialog
          file = tkFileDialog.askopenfilename(defaultextension=".pml")
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
        
        def populater(event):
            objects = cmd.get_names('all')
            cmd.select('protein','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
            cmd.select('nucleic_acid', 'resn a+t+g+c+u')
            cmd.select('hydrophobic','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
            cmd.select('hydrophilic','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
 	    cmd.select('acidic','resn ASP+GLU')
	    cmd.select('basic','resn ARG+HIS+LYS')
            cmd.select('ligands', 'het')
            cmd.select('heme', 'resn hem')
            cmd.disable('heme')
            cmd.disable('ligands')
            cmd.disable('basic')
            cmd.disable('acidic')
            cmd.disable('hydrophilic')
            cmd.disable('hydrophobic')
            cmd.disable('nucleic_acid')
            cmd.disable('protein')
            checkitforthese()
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
            checkforchain()            
            items=[]
            objects = cmd.get_names('all')
            items.append('All')
            items.append('Not Selected')
            if 'protein' in objects:
              items.append('protein')
            if 'nucleic_acid' in objects:
              items.append('nucleic_acid')
            if 'hydrophobic' in objects:
              items.append('hydrophobic')
            if 'hydrophilic' in objects:
              items.append('hydrophilic')
            if 'acidic' in objects:
              items.append('acidic')
            if 'basic' in objects:
              items.append('basic')
            if 'ligands' in objects:
              items.append('ligands')
            if 'heme' in objects:
              items.append('heme') 
            if 'Chain-A' in objects:
              items.append('Chain-A')
            if 'Chain-B' in objects:
              items.append('Chain-B')
            if 'Chain-C' in objects:
              items.append('Chain-C')
            if 'Chain-D' in objects:
              items.append('Chain-D')
            if 'Chain-E' in objects:
              items.append('Chain-E')           
            if 'Chain-F' in objects:
              items.append('Chain-F')
            if 'Chain-G' in objects:
              items.append('Chain-G')
            if 'Chain-H' in objects:
              items.append('Chain-H')
            if 'Chain-I' in objects:
              items.append('Chain-I')
            if 'Chain-J' in objects:
              items.append('Chain-J')
            if 'Chain-K' in objects:
              items.append('Chain-K')
            if 'Chain-L' in objects:
              items.append('Chain-L')
            if 'Chain-M' in objects:
              items.append('Chain-M')
            if 'Chain-N' in objects:
              items.append('Chain-N')
            if 'Chain-O' in objects:
              items.append('Chain-O')
            if 'Chain-P' in objects:
              items.append('Chain-P')
            if 'Chain-Q' in objects:
              items.append('Chain-Q')
            if 'Chain-R' in objects:
              items.append('Chain-R')
            if 'Chain-S' in objects:
              items.append('Chain-S')
            if 'Chain-T' in objects:
              items.append('Chain-T')
            if 'Chain-U' in objects:
              items.append('Chain-U')
            if 'Chain-V' in objects:
              items.append('Chain-V')
            if 'Chain-W' in objects:
              items.append('Chain-W')
            if 'Chain-X' in objects:
              items.append('Chain-X')
            if 'Chain-Y' in objects:
              items.append('Chain-Y')
            if 'Chain-Z' in objects:
              items.append('Chain-Z')            
            items.sort()
            self.selection.setitems(items)
            self.advancedSelection.setitems(items)
            self.sel = 'All'
            self.sel1 = 'All'


                  
            
        popbtn=Button(interior, text='Update Selection',width=15)
        popbtn.place(x=50, y=32)
        popbtn.bind('<Button-1>', populater)

        #-------------Version 1---------------#
        self.selection = Pmw.OptionMenu(interior,labelpos = 'w',
                   label_text = 'Select:',
                    items = (''),
                    menubutton_width = 10, command = self.set_sel)                       
        self.selection.grid(row=0, column=0, padx=8, pady=0)


        
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

        
        #---------------Version 2-------------#

        #--------------------------------------#
        #			               #
        #            Motifs TAB                #
        #                                      #
        #--------------------------------------#
	page = notebook.add('Motifs')
	notebook.tab('Motifs').focus_set()
	
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
                import tkMessageBox
                tkMessageBox.showinfo('Alert', 'You must load a motif first')
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
                import tkMessageBox
                tkMessageBox.showinfo('Alert', 'You must load a motif first')
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
	
        #--------------------------------------#
        #			                 #
        #           Custom Motifs Tab               #
        #                                        #
        #--------------------------------------#
	page = notebook.add('Custom\nMotifs')
	notebook.tab('Custom\nMotifs').focus_set()
              
 
        #custom group
        group = Pmw.Group(page, tag_text = 'Custom Motifs')
        group.grid(row=0, column=0,columnspan =4, padx=0, pady=0)
        interior = group.interior()
        #menu bars
        selectionAA = Pmw.OptionMenu(interior,label_text = 'Selection A:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifA)
        selectionAA.grid(row=0,column=0,sticky=NW)

        selectionAB = Pmw.OptionMenu(interior,label_text = 'Selection B:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifB)
        selectionAB.grid(row=0,column=1,sticky=NW)

        selectionAC = Pmw.OptionMenu(interior,label_text = 'Selection C:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifC)
        selectionAC.grid(row=0,column=2,sticky=NW)

        selectionAD = Pmw.OptionMenu(interior,label_text = 'Selection D:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifD)
        selectionAD.grid(row=0,column=3,sticky=NW)


        #sliders
        self.selA = Scale(interior, width =8)
        self.selA.configure(troughcolor="#ffffff")
        self.selA.configure(length="80")
        self.selA.configure(orient="horizontal")
        self.selA.configure(resolution="0.25")
        self.selA.configure(to="8.0")    
        self.selA.grid(row=1, column=0, padx=0, pady=0, sticky=NW)
        self.selA.set(4.0)

        self.selB = Scale(interior, width =8)
        self.selB.configure(troughcolor="#ffffff")
        self.selB.configure(length="80")
        self.selB.configure(orient="horizontal")
        self.selB.configure(resolution="0.25")
        self.selB.configure(to="8.0")    
        self.selB.grid(row=1, column=1, padx=0, pady=0, sticky=NW)
        self.selB.set(4.0)

        self.selC = Scale(interior, width =8)
        self.selC.configure(troughcolor="#ffffff")
        self.selC.configure(length="80")
        self.selC.configure(orient="horizontal")
        self.selC.configure(resolution="0.25")
        self.selC.configure(to="8.0")
        self.selC.grid(row=1, column=2, padx=0, pady=0, sticky=NW)
        self.selC.set(4.0)

        #labels
        
        lab1 = Label(interior, text='Range A to B')
        lab1.grid(row = 2, column = 0)
        lab2 = Label(interior, text='Range B to C')
        lab2.grid(row = 2, column = 1)
        lab3 = Label(interior, text='Range C to D')
        lab3.grid(row = 2, column = 2)

        #custom buttons

        self.buttonAdd(interior, 'AB Selection', 15, self.bimotif, 3, 0, 'N,S,E,W')
        self.buttonAdd(interior, 'ABC Selection', 15, self.trimotif, 3, 1, 'N,S,E,W')
        self.buttonAdd(interior, 'ABCD Selection', 15, self.quadmotif, 3, 2, 'N,S,E,W')
        self.buttonAdd(interior, 'Reset', 12, self.resetmotif, 1, 3, 'SW')

        #--------------------------------------#
        #			               #
        #     Addvanced Custom Motifs Tab      #
        #                                      #
        #--------------------------------------#

        #custom group
        group = Pmw.Group(page, tag_text = 'Advanced Custom Motifs')
        group.grid(row=1, column=0,columnspan =4, padx=0, pady=0)
        interior = group.interior()
        #menu bars
        selectionA = Pmw.OptionMenu(interior,label_text = 'Selection A:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifAA)
        selectionA.grid(row=0,column=0,sticky=NW)

        selectionB = Pmw.OptionMenu(interior,label_text = 'Selection B:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifAB)
        selectionB.grid(row=0,column=1,sticky=NW)

        selectionC = Pmw.OptionMenu(interior,label_text = 'Selection C:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifAC)
        selectionC.grid(row=0,column=2,sticky=NW)

        selectionD = Pmw.OptionMenu(interior,label_text = 'Selection D:',labelpos = 'n',
                    items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                    menubutton_width = 8, command=self.set_motifAD)
        selectionD.grid(row=0,column=3,sticky=NW)


        #sliders
        self.selAB = Scale(interior, width =8)
        self.selAB.configure(troughcolor="#ffffff")
        self.selAB.configure(length="100")
        self.selAB.configure(orient="horizontal")
        self.selAB.configure(resolution="0.25")
        self.selAB.configure(to="15")    
        self.selAB.grid(row=1, column=0, padx=0, pady=0, sticky=NW)
        self.selAB.set(4.0)
        
        self.selAC = Scale(interior, width =8)
        self.selAC.configure(troughcolor="#ffffff")
        self.selAC.configure(length="100")
        self.selAC.configure(orient="horizontal")
        self.selAC.configure(resolution="0.25")
        self.selAC.configure(to="15")    
        self.selAC.grid(row=1, column=1,columnspan=2, padx=2, pady=0, sticky=NW)
        self.selAC.set(4.0)
        
        self.selAD = Scale(interior, width =8)
        self.selAD.configure(troughcolor="#ffffff")
        self.selAD.configure(length="100")
        self.selAD.configure(orient="horizontal")
        self.selAD.configure(resolution="0.25")
        self.selAD.configure(to="15")    
        self.selAD.grid(row=1, column=2,columnspan=2, padx=2, pady=0, sticky=NW)
        self.selAD.set(4.0)

        self.selBC = Scale(interior, width =8)
        self.selBC.configure(troughcolor="#ffffff")
        self.selBC.configure(length="100")
        self.selBC.configure(orient="horizontal")
        self.selBC.configure(resolution="0.25")
        self.selBC.configure(to="15")    
        self.selBC.grid(row=3, column=0,columnspan=2, padx=2, pady=0, sticky=NW)
        self.selBC.set(4.0)
        
        self.selBD = Scale(interior, width =8)
        self.selBD.configure(troughcolor="#ffffff")
        self.selBD.configure(length="100")
        self.selBD.configure(orient="horizontal")
        self.selBD.configure(resolution="0.25")
        self.selBD.configure(to="15")    
        self.selBD.grid(row=3, column=1,columnspan=2, padx=2, pady=0, sticky=NW)
        self.selBD.set(4.0)

        self.selCD = Scale(interior, width =8)
        self.selCD.configure(troughcolor="#ffffff")
        self.selCD.configure(length="100")
        self.selCD.configure(orient="horizontal")
        self.selCD.configure(resolution="0.25")
        self.selCD.configure(to="15")
        self.selCD.grid(row=3, column=2,columnspan=2, padx=2, pady=0, sticky=NW)
        self.selCD.set(4.0)

        #labels
        
        lab1 = Label(interior, text='Range A to B')
        lab1.grid(row = 2, column = 0)
        lab2 = Label(interior, text='Range A to C')
        lab2.grid(row = 2, column = 1)
        lab3 = Label(interior, text='Range A to D')
        lab3.grid(row = 2, column = 2)

        lab1 = Label(interior, text='Range B to C')
        lab1.grid(row = 4, column = 0)
        lab2 = Label(interior, text='Range B to D')
        lab2.grid(row = 4, column = 1)
        lab3 = Label(interior, text='Range C to D')
        lab3.grid(row = 4, column = 2)

        #custom buttons

        self.buttonAdd(interior, 'AB Selection', 15, self.Abimotif, 5, 0, 'N,S,E,W')
        self.buttonAdd(interior, 'ABC Selection', 15, self.Atrimotif, 5, 1, 'N,S,E,W')
        self.buttonAdd(interior, 'ABCD Selection', 15, self.Aquadmotif, 5, 2, 'N,S,E,W')
        self.buttonAdd(interior, 'Reset', 12, self.resetmotif, 1, 3, 'SE')

                
        #--------------------------------------#
        #			               #
        #            Ligand Binding                      #
        #                                                               #
        #--------------------------------------#
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
            import tkFileDialog


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
            query_string = tkSimpleDialog.askstring('Advance PDB search',
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
                        tkMessageBox.showinfo('PDB EntryFile',
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
                            tkMessageBox.showinfo('PDB EntryFile','The download is finished')
                            return True
                    except urllib2.URLError:
                        print "Network Error: ",sys.exc_info()[1]
                        tkMessageBox.showerror('Download Error',
                                               'Can not retrieve PDB Entries file.\nPlease check your network connection.')
                        return False
                    except OSError:
                        print "File Error: ",sys.exc_info()[1]
                        tkMessageBox.showerror('File Error',
                                               sys.exc_info()[1])
                        return False
                    except:
                        print "Unexpected error:", sys.exc_info()[1]
                        tkMessageBox.showerror('File Error',
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
                tkMessageBox.showinfo( "MolSheet - ver.%s" % self.VERSION,
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
                self.selected_rgb = "#CCCCCC"

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
                self.selct( start_widget )
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
                    answer = tkMessageBox._show("Save PySS", "The table is modified, save it?",
                                   icon=tkMessageBox.QUESTION, type=tkMessageBox.YESNOCANCEL )
                    if answer == tkMessageBox.CANCEL:
                        return False
                    if answer == tkMessageBox.YES:
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
                    if self.selected:
                        self.selected.configure( bg=self.normal_rgb )
                    self.selct( e.widget )
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
                        tkMessageBox.showinfo('PDB File','Dowloading PDB File %s'%pdbName)
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
                self.selected = widget
                self.selected.configure( bg=self.selected_rgb )
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
                r,c = self.lbls[ self.selected ]
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
                self.selct( self.selected )

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
                    tkMessageBox.showerror('Connection Error',
                                           'Can not retrieve PDB file.\nPlease check your network connection.')
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    tkMessageBox.showerror('Error',
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
                self.update()
        
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
                self.update()
            
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

        nmlab = Label(interior, text = 'Motif Name')
        nmlab.grid(row=1, column =0, sticky = 'n')
        runbtn1 = Button(interior, text = 'Run all Motifs')
        runbtn1.grid(row = 0, column =0, sticky = 'W')
        mobtn = Button(interior, text = 'Motif maker')
        mobtn.grid(row = 0, column = 0, sticky = 'E')
        entz = Entry(interior)

        button333 =Button(interior, text = 'Get Random PDB', width =25)
        button333.grid(row = 3, column = 0, padx = 10, sticky = 'N')
        randent = Entry(interior)

        def randomized(*args):
                cmd.delete('all')
                q = random.randint(1, 41258)
                p = linecache.getline('./modules/pmg_tk/startup/pdb_entry_type.txt', q)
                randent.insert(0,p)
                randent.delete(4,1000)
        
                pdbCode = randent.get()
                
           
                pdbCode = string.upper(pdbCode)
                try:
                    filename = urllib.urlretrieve('http://www.rcsb.org/pdb/cgi/export.cgi/' +
                                                            pdbCode + '.pdb.gz?format=PDB&pdbId=' +
                                                            pdbCode + '&compression=gz')[0]
                except:
                    tkMessageBox.showerror('Connection Error',
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
                        tkMessageBox.showerror('Invalid Code',
                                                      'You entered an invalid pdb code:' + pdbCode,
                                                      parent=app.root)

                    os.remove(filename) # Remove tmp file (leave the pdb)

        cmd.extend('randomized',randomized)
        button333.bind('<Button-1>', randomized)

            

        entcount = Entry(interior)
        def runum(event):#run all the motifs and count the atoms n the Motifs folder
           
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

          
                        

        runbtn1.bind('<Button-1>', runum)
                    
        self.motifdrop = Pmw.ScrolledListBox(interior,
                    items=(),
                    dblclickcommand = self.runcusmotif,
                    listbox_height = 6,                       
                    usehullsize = 1,
                    hull_width = 300,
                    hull_height = 150,)
        self.motifdrop.grid(row=2, column =0)

        def loadmotifer(event):
            root = Tk()
            group = Pmw.Group(root, tag_text='Motif Maker')#And a new group
            group.grid(row=0, column=0, padx=0, pady=0, sticky=NW)
            interior = group.interior()
            
            
    #widgets
            ent1 = Entry(interior, width = 8)
            ent1.grid(row = 0, column =2)

            ent2 = Entry(interior, width = 8)
            ent2.grid(row = 1, column =2)

            ent3 = Entry(interior, width = 8)
            ent3.grid(row = 2, column =2)

            ent4 = Entry(interior, width = 8)
            ent4.grid(row = 3, column =2)

            ent5 = Entry(interior, width = 8)
            ent5.grid(row = 4, column =2)

            lent1 = Label(interior, text = 'Number:')
            lent1.grid(row = 0, column =1)

            lent2 = Label(interior, text =  'Number:')
            lent2.grid(row = 1, column =1)

            lent3 = Label(interior, text =  'Number:')
            lent3.grid(row = 2, column =1)

            lent4 = Label(interior, text =  'Number:')
            lent4.grid(row = 3, column =1)

            lent5 = Label(interior, text =  'Number:')
            lent5.grid(row = 4, column =1)

            ent1B = Entry(interior)

            ent2B = Entry(interior)

            ent3B = Entry(interior)

            ent4B = Entry(interior)

            ent5B = Entry(interior)
            
            but1 = Button(interior, text = 'Make Motif', width = 10)
            but1.grid(row =5, column =3, sticky = 'se')

            popbtn = Button(interior, text = 'Chain Info', width = 10)
            popbtn.grid(row = 5, column = 4, sticky = 'se')
            
            enta = Entry(interior)
            enta.insert(0,0)

            entb = Entry(interior)
            entb.insert(0,0)

            entc = Entry(interior)
            entc.insert(0,0)

            entd = Entry(interior)
            entd.insert(0,0)

            ente = Entry(interior)
            ente.insert(0,0)
            
            enth = Entry(interior)
            enth.insert(0,0)
            
            entnum = Entry(interior)                    
            entnum.insert(0,0)

            bonent1 = Entry(interior)
            bonent1.insert(0,1)

            bonent2 = Entry(interior)
            bonent2.insert(0,1)
            
            bonent3 = Entry(interior)
            bonent3.insert(0,1)
            
            bonent4 = Entry(interior)
            bonent4.insert(0,1)
            
            bonent4 = Entry(interior)
            bonent4.insert(0,1)

            bonent5 = Entry(interior)
            bonent5.insert(0,1)

            ent1F = Entry(interior)
            ent2F = Entry(interior)
            ent3F = Entry(interior)
            ent4F = Entry(interior)



            def set_motif1(tag):
                if tag=='gly':
                    ent1B.delete(0,10)  
                    ent1B.insert(0,'gly')
                elif tag=='ala':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'ala')
                elif tag=='val':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'val')
                elif tag=='leu':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'leu')
                elif tag=='ile':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'ile')
                elif tag=='met':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'met')
                elif tag=='pro':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'pro')
                elif tag=='phe':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'phe')
                elif tag=='tyr':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'tyr')
                elif tag=='trp':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'trp')
                elif tag=='ser':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'ser')
                elif tag=='thr':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'thr')
                elif tag=='cys':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'cys')
                elif tag=='lys':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'lys')
                elif tag=='arg':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'arg')
                elif tag=='his':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'his')
                elif tag=='asp':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'asp')
                elif tag=='glu':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'glu')
                elif tag=='asn':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'asn')
                elif tag=='gln':
                    ent1B.delete(0,10)
                    ent1B.insert(0,'gln')
                elif tag==' ':
                    ent1B.delete(0,10)
                    
            def set_motif2(tag):
                if tag=='gly':
                    ent2B.delete(0,10)  
                    ent2B.insert(0,'gly')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'glyi')
                elif tag=='ala':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'ala')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'alai')
                elif tag=='val':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'val')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'vali')
                elif tag=='leu':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'leu')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'leui')
                elif tag=='ile':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'ile')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'ilei')
                elif tag=='met':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'met')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'meti')
                elif tag=='pro':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'pro')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'proi')
                elif tag=='phe':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'phe')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'phei')
                elif tag=='tyr':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'tyr')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'tyri')
                elif tag=='trp':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'trp')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'trpi')
                elif tag=='ser':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'ser')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'seri')
                elif tag=='thr':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'thr')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'thri')
                elif tag=='cys':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'cys')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'cysi')
                elif tag=='lys':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'lys')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'lysi')
                elif tag=='arg':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'arg')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'argi')
                elif tag=='his':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'his')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'hisi')
                elif tag=='asp':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'asp')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'aspi')
                elif tag=='glu':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'glu')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'glui')
                elif tag=='asn':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'asn')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'asni')
                elif tag=='gln':
                    ent2B.delete(0,10)
                    ent2B.insert(0,'gln')
                    ent1F.delete(0,10)  
                    ent1F.insert(0,'glni')
                elif tag==' ':
                    ent2B.delete(0,10)
                    ent1F.delete(0,10)

            def set_motif3(tag):
                if tag=='gly':
                    ent3B.delete(0,10)  
                    ent3B.insert(0,'gly')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'glyii')
                elif tag=='ala':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'ala')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'alaii')
                elif tag=='val':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'val')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'valii')
                elif tag=='leu':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'leu')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'leuii')
                elif tag=='ile':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'ile')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'ileii')
                elif tag=='met':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'met')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'metii')
                elif tag=='pro':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'pro')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'proii')
                elif tag=='phe':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'phe')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'pheii')
                elif tag=='tyr':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'tyr')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'tyrii')
                elif tag=='trp':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'trp')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'trpii')
                elif tag=='ser':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'ser')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'serii')
                elif tag=='thr':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'thr')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'thrii')
                elif tag=='cys':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'cys')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'cysii')
                elif tag=='lys':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'lys')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'lysii')
                elif tag=='arg':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'arg')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'argii')
                elif tag=='his':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'his')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'hisii')
                elif tag=='asp':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'asp')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'aspii')
                elif tag=='glu':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'glu')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'gluii')
                elif tag=='asn':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'asn')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'asnii')
                elif tag=='gln':
                    ent3B.delete(0,10)
                    ent3B.insert(0,'gln')
                    ent2F.delete(0,10)  
                    ent2F.insert(0,'glnii')
                elif tag==' ':
                    ent3B.delete(0,10)
                    ent2F.delete(0,10)
                    
            def set_motif4(tag):
                if tag=='gly':
                    ent4B.delete(0,10)  
                    ent4B.insert(0,'gly')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'glyiii')
                elif tag=='ala':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'ala')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'alaiii')
                elif tag=='val':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'val')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'valiii')
                elif tag=='leu':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'leu')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'leuiii')
                elif tag=='ile':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'ile')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'ileiii')
                elif tag=='met':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'met')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'metiii')
                elif tag=='pro':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'pro')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'proiii')
                elif tag=='phe':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'phe')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'pheiii')
                elif tag=='tyr':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'tyr')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'tyriii')
                elif tag=='trp':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'trp')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'trpiii')
                elif tag=='ser':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'ser')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'seriii')
                elif tag=='thr':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'thr')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'thriii')
                elif tag=='cys':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'cys')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'cysiii')
                elif tag=='lys':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'lys')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'lysiii')
                elif tag=='arg':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'arg')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'argiii')
                elif tag=='his':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'his')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'hisiii')
                elif tag=='asp':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'asp')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'aspiii')
                elif tag=='glu':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'glu')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'gluiii')
                elif tag=='asn':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'asn')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'asniii')
                elif tag=='gln':
                    ent4B.delete(0,10)
                    ent4B.insert(0,'gln')
                    ent3F.delete(0,10)
                    ent3F.insert(0,'glniii')
                elif tag==' ':
                    ent4B.delete(0,10)

            def set_motif5(tag):
                if tag=='gly':
                    ent5B.delete(0,10)  
                    ent5B.insert(0,'gly')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'glyiiii')
                elif tag=='ala':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'ala')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'alaiiii')
                elif tag=='val':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'val')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'valiiii')
                elif tag=='leu':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'leu')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'leuiiii')
                elif tag=='ile':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'ile')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'ileiiii')
                elif tag=='met':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'met')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'metiiii')
                elif tag=='pro':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'pro')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'proiiii')
                elif tag=='phe':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'phe')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'pheiiii')
                elif tag=='tyr':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'tyr')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'tyriiii')
                elif tag=='trp':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'trp')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'trpiiii')
                elif tag=='ser':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'ser')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'seriiii')
                elif tag=='thr':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'thr')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'thriiii')
                elif tag=='cys':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'cys')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'cysiiii')
                elif tag=='lys':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'lys')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'lysiiii')
                elif tag=='arg':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'arg')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'argiiii')
                elif tag=='his':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'his')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'hisiiii')
                elif tag=='asp':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'asp')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'aspiiii')
                elif tag=='glu':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'glu')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'gluiiii')
                elif tag=='asn':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'asn')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'asniiii')
                elif tag=='gln':
                    ent5B.delete(0,10)
                    ent5B.insert(0,'gln')
                    ent4F.delete(0,10)
                    ent4F.insert(0,'glniiii')
                elif tag==' ':
                    ent5B.delete(0,10)
            
            def checkforchain(event):
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
                if "Chain-''" in objects:
                    x27 = cmd.index("Chain-''")
                    n27 = len(x27)
                    if(n27 < 1):
                        cmd.delete("Chain-''")
            
            def populate(event):
                cmd.remove('resn HOH')
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
                cmd.select("Chain-''", "chain ''")
                checkforchain(event)            
                items=[]
                objects = cmd.get_names('all')
                
                if 'Chain-A' in objects:
                  items.append('Chain-A')
                if 'Chain-B' in objects:
                  items.append('Chain-B')
                if 'Chain-C' in objects:
                  items.append('Chain-C')
                if 'Chain-D' in objects:
                  items.append('Chain-D')
                if 'Chain-E' in objects:
                  items.append('Chain-E')           
                if 'Chain-F' in objects:
                  items.append('Chain-F')
                if 'Chain-G' in objects:
                  items.append('Chain-G')
                if 'Chain-H' in objects:
                  items.append('Chain-H')
                if 'Chain-I' in objects:
                  items.append('Chain-I')
                if 'Chain-J' in objects:
                  items.append('Chain-J')
                if 'Chain-K' in objects:
                  items.append('Chain-K')
                if 'Chain-L' in objects:
                  items.append('Chain-L')
                if 'Chain-M' in objects:
                  items.append('Chain-M')
                if 'Chain-N' in objects:
                  items.append('Chain-N')
                if 'Chain-O' in objects:
                  items.append('Chain-O')
                if 'Chain-P' in objects:
                  items.append('Chain-P')
                if 'Chain-Q' in objects:
                  items.append('Chain-Q')
                if 'Chain-R' in objects:
                  items.append('Chain-R')
                if 'Chain-S' in objects:
                  items.append('Chain-S')
                if 'Chain-T' in objects:
                  items.append('Chain-T')
                if 'Chain-U' in objects:
                  items.append('Chain-U')
                if 'Chain-V' in objects:
                  items.append('Chain-V')
                if 'Chain-W' in objects:
                  items.append('Chain-W')
                if 'Chain-X' in objects:
                  items.append('Chain-X')
                if 'Chain-Y' in objects:
                  items.append('Chain-Y')
                if 'Chain-Z' in objects:
                  items.append('Chain-Z')
                if "Chain-''" in objects:
                  items.append("Chain-''")
               
                items.sort()
                selection.setitems(items)
                selectiona.setitems(items)
                selectionb.setitems(items)
                selectionc.setitems(items)
                selectiond.setitems(items)

            popbtn.bind('<Button-1>', populate)

            chainent = Entry(interior)
            chainent1 = Entry(interior)
            chainent2 = Entry(interior)
            chainent3 = Entry(interior)
            chainent4 = Entry(interior) 

            def bone1(tag):

                if tag=='Off':
                    bonent1.delete(0,1000)
                    bonent1.insert(0,1)
                elif tag=='On':
                    bonent1.delete(0,1000)
                    bonent1.insert(0,2)
                    
            def bone2(tag):

                if tag=='Off':
                    bonent2.delete(0,1000)
                    bonent2.insert(0,1)
                elif tag=='On':
                    bonent2.delete(0,1000)
                    bonent2.insert(0,2)
                    
            def bone3(tag):

                if tag=='Off':
                    bonent3.delete(0,1000)
                    bonent3.insert(0,1)
                elif tag=='On':
                    bonent3.delete(0,1000)
                    bonent3.insert(0,2)
                    
            def bone4(tag):

                if tag=='Off':
                    bonent4.delete(0,1000)
                    bonent4.insert(0,1)
                elif tag=='On':
                    bonent4.delete(0,1000)
                    bonent4.insert(0,2)
                    
            def bone5(tag):

                if tag=='Off':
                    bonent5.delete(0,1000)
                    bonent5.insert(0,1)
                elif tag=='On':
                    bonent5.delete(0,1000)
                    bonent5.insert(0,2)

            def set_sel1(tag):
                cmd.deselect()
                c=re.compile("^Chain")

                if tag=='Chain-A':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-A')
                elif tag=='Chain-B':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-B')
                elif tag=='Chain-C':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-C')
                elif tag=='Chain-D':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-D')
                elif tag=='Chain-E':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-E')
                elif tag=='Chain-F':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-F')
                elif tag=='Chain-G':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-G')
                elif tag=='Chain-H':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-H')
                elif tag=='Chain-I':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-I')
                elif tag=='Chain-J':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-J')
                elif tag=='Chain-K':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-K')
                elif tag=='Chain-L':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-L')
                elif tag=='Chain-M':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-M')
                elif tag=='Chain-N':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-N')
                elif tag=='Chain-O':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-O')
                elif tag=='Chain-P':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-P')
                elif tag=='Chain-Q':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-Q')
                elif tag=='Chain-R':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-R')
                elif tag=='Chain-S':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-S')
                elif tag=='Chain-T':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-T')
                elif tag=='Chain-U':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-U')
                elif tag=='Chain-V':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-V')
                elif tag=='Chain-W':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-W')
                elif tag=='Chain-X':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-X')
                elif tag=='Chain-Y':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-Y')
                elif tag=='Chain-Z':
                    chainent.delete(0,1000)
                    chainent.insert(0,'Chain-Z')
                elif tag=="Chain-''":
                    chainent.insert(0,"Chain-'' ")

            def set_sel2(tag):
                cmd.deselect()
                c=re.compile("^Chain")

                if tag=='Chain-A':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-A')
                elif tag=='Chain-B':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-B')
                elif tag=='Chain-C':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-C')
                elif tag=='Chain-D':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-D')
                elif tag=='Chain-E':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-E')
                elif tag=='Chain-F':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-F')
                elif tag=='Chain-G':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-G')
                elif tag=='Chain-H':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-H')
                elif tag=='Chain-I':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-I')
                elif tag=='Chain-J':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-J')
                elif tag=='Chain-K':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-K')
                elif tag=='Chain-L':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-L')
                elif tag=='Chain-M':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-M')
                elif tag=='Chain-N':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-N')
                elif tag=='Chain-O':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-O')
                elif tag=='Chain-P':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-P')
                elif tag=='Chain-Q':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-Q')
                elif tag=='Chain-R':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-R')
                elif tag=='Chain-S':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-S')
                elif tag=='Chain-T':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-T')
                elif tag=='Chain-U':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-U')
                elif tag=='Chain-V':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-V')
                elif tag=='Chain-W':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-W')
                elif tag=='Chain-X':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-X')
                elif tag=='Chain-Y':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-Y')
                elif tag=='Chain-Z':
                    chainent1.delete(0,1000)
                    chainent1.insert(0,'Chain-Z')
                elif tag=="Chain-''":
                    chainent1.insert(0,"Chain-'' ")

            def set_sel3(tag):
                cmd.deselect()
                c=re.compile("^Chain")

                if tag=='Chain-A':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-A')
                elif tag=='Chain-B':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-B')
                elif tag=='Chain-C':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-C')
                elif tag=='Chain-D':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-D')
                elif tag=='Chain-E':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-E')
                elif tag=='Chain-F':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-F')
                elif tag=='Chain-G':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-G')
                elif tag=='Chain-H':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-H')
                elif tag=='Chain-I':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-I')
                elif tag=='Chain-J':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-J')
                elif tag=='Chain-K':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-K')
                elif tag=='Chain-L':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-L')
                elif tag=='Chain-M':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-M')
                elif tag=='Chain-N':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-N')
                elif tag=='Chain-O':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-O')
                elif tag=='Chain-P':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-P')
                elif tag=='Chain-Q':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-Q')
                elif tag=='Chain-R':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-R')
                elif tag=='Chain-S':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-S')
                elif tag=='Chain-T':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-T')
                elif tag=='Chain-U':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-U')
                elif tag=='Chain-V':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-V')
                elif tag=='Chain-W':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-W')
                elif tag=='Chain-X':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-X')
                elif tag=='Chain-Y':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-Y')
                elif tag=='Chain-Z':
                    chainent2.delete(0,1000)
                    chainent2.insert(0,'Chain-Z')
                elif tag=="Chain-''":
                    chainent2.insert(0,"Chain-'' ")

            def set_sel4(tag):
                cmd.deselect()
                c=re.compile("^Chain")

                if tag=='Chain-A':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-A')
                elif tag=='Chain-B':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-B')
                elif tag=='Chain-C':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-C')
                elif tag=='Chain-D':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-D')
                elif tag=='Chain-E':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-E')
                elif tag=='Chain-F':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-F')
                elif tag=='Chain-G':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-G')
                elif tag=='Chain-H':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-H')
                elif tag=='Chain-I':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-I')
                elif tag=='Chain-J':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-J')
                elif tag=='Chain-K':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-K')
                elif tag=='Chain-L':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-L')
                elif tag=='Chain-M':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-M')
                elif tag=='Chain-N':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-N')
                elif tag=='Chain-O':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-O')
                elif tag=='Chain-P':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-P')
                elif tag=='Chain-Q':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-Q')
                elif tag=='Chain-R':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-R')
                elif tag=='Chain-S':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-S')
                elif tag=='Chain-T':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-T')
                elif tag=='Chain-U':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-U')
                elif tag=='Chain-V':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-V')
                elif tag=='Chain-W':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-W')
                elif tag=='Chain-X':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-X')
                elif tag=='Chain-Y':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-Y')
                elif tag=='Chain-Z':
                    chainent3.delete(0,1000)
                    chainent3.insert(0,'Chain-Z')
                elif tag=="Chain-''":
                    chainent3.insert(0,"Chain-'' ")

            def set_sel5(tag):
                cmd.deselect()
                c=re.compile("^Chain")

                if tag=='Chain-A':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-A')
                elif tag=='Chain-B':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-B')
                elif tag=='Chain-C':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-C')
                elif tag=='Chain-D':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-D')
                elif tag=='Chain-E':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-E')
                elif tag=='Chain-F':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-F')
                elif tag=='Chain-G':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-G')
                elif tag=='Chain-H':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-H')
                elif tag=='Chain-I':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-I')
                elif tag=='Chain-J':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-J')
                elif tag=='Chain-K':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-K')
                elif tag=='Chain-L':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-L')
                elif tag=='Chain-M':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-M')
                elif tag=='Chain-N':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-N')
                elif tag=='Chain-O':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-O')
                elif tag=='Chain-P':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-P')
                elif tag=='Chain-Q':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-Q')
                elif tag=='Chain-R':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-R')
                elif tag=='Chain-S':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-S')
                elif tag=='Chain-T':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-T')
                elif tag=='Chain-U':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-U')
                elif tag=='Chain-V':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-V')
                elif tag=='Chain-W':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-W')
                elif tag=='Chain-X':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-X')
                elif tag=='Chain-Y':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-Y')
                elif tag=='Chain-Z':
                    chainent4.delete(0,1000)
                    chainent4.insert(0,'Chain-Z')
                elif tag=="Chain-''":
                    chainent4.insert(0,"Chain-'' ")

            #Warren Delanos Code

            def get_distance(atom1="pk1",atom2="pk2",state=0,quiet=1):

                atom1 = selector.process(atom1)
                atom2 = selector.process(atom2)

                r = _cmd.get_distance(str(atom1),str(atom2),int(state)-1)
                print " cmd.get_distance: %5.3f Angstroms."%r
                entnum.delete(0,1000)
                entnum.insert(0,r)
                entnum.delete(4,1000)
                return r

                
            def makemotif(event):
                try:
                    if len(ent1.get()) > 1 and len(chainent.get()) < 1:
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', 'Please Select a Chain for Residue 1')
                        interior.mainloop()
                               
                    if len(ent2.get()) > 1 and len(chainent1.get()) < 1:
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', 'Please Select a Chain for Residue 2')
                        interior.mainloop()
                                            
                    if len(ent3.get()) > 1 and len(chainent2.get()) < 1:
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', 'Please Select a Chain for Residue 3')
                        interior.mainloop()
                               
                    if len(ent4.get()) > 1 and len(chainent3.get()) < 1:
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', 'Please Select a Chain for Residue 4')
                        interior.mainloop()

                    if len(ent5.get()) > 1 and len(chainent4.get()) < 1:
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', 'Please Select a Chain for Residue 5')
                        interior.mainloop()

                    else:
                        cmd.remove('resn HOH')
                        import tkFileDialog
                        Q = tkFileDialog.asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                        f=open(Q, 'w')
                        atomlist = ['','C','CA','CB','CD','CD1','CD2','CE','CE1','CE2','CE3','CH2','CG','CG1','CG2','CZ','CZ2','CZ3','N','ND1','ND2','NE','NE1','NE2','NH1','NH2','NZ','O','OD1','OD2','OE1','OE2','OG','OG1','OH','SG','SD']
                        atomlist2 = ['','CB','CD','CD1','CD2','CE','CE1','CE2','CE3','CH2','CG','CG1','CG2','CZ','CZ2','CZ3','ND1','ND2','NE','NE1','NE2','NH1','NH2','NZ','OD1','OD2','OE1','OE2','OG','OG1','OH','SG','SD']
                        resnlist=['']
                        resnlistf=['']
                        resilist=['']

                        if len(ent1B.get()) >0:
                            resnlist.append(ent1B.get())
                            resnlistf.append(ent1B.get())
                            resilist.append(ent1.get())
                        if len(ent2B.get())>0:      
                            resnlist.append(ent2B.get())
                            resnlistf.append(ent1F.get())
                            resilist.append(ent2.get())
                        if len(ent3B.get()) >0:
                            resnlist.append(ent3B.get())
                            resnlistf.append(ent2F.get())
                            resilist.append(ent3.get())
                        if len(ent4B.get()) >0:
                            resnlist.append(ent4B.get())
                            resilist.append(ent4.get())
                            resnlistf.append(ent3F.get())
                        if len(ent5B.get()) >0:
                            resnlist.append(ent5B.get())
                            resilist.append(ent5.get())
                            resnlistf.append(ent4F.get())
                       
                        ente.delete(0,1000)
                        ente.insert(0,0)
                        
                        funrun = True
                        while funrun:
                            try:
                                
                                enta.delete(0,1000)
                                enta.insert(0,0)
                
                                e = int(ente.get()) + 1
                                ente.delete(0,1000)
                                ente.insert(0,e)

                                if e ==1:
                                    if int(bonent1.get())==1:
                                        list =atomlist2
                                    else:
                                        list=atomlist

                                if e ==2:
                                    if int(bonent2.get())==1:
                                        list =atomlist2
                                    else:
                                        list=atomlist

                                if e ==3:
                                    if int(bonent3.get())==1:
                                        list =atomlist2
                                    else:
                                        list=atomlist

                                if e ==4:
                                    if int(bonent4.get())==1:
                                        list =atomlist2
                                    else:
                                        list=atomlist

                                if e ==5:
                                    if int(bonent5.get())==1:
                                        list =atomlist2
                                    else:
                                        list=atomlist

                                print resnlist[e]
                                
                                entd.delete(0,1000)
                                entd.insert(0,0)

                                running = True  
                                
                                while running:
                                    try:

                                        d = int(entd.get()) + 1
                                        entd.delete(0,1000)
                                        entd.insert(0,d)
                                        if resnlist[e] == resnlist[d]:
                                            d = int(entd.get()) + 1
                                            entd.delete(0,1000)
                                            entd.insert(0,d)

                                        if d ==1:
                                            if int(bonent1.get())==1:
                                                list1 =atomlist2
                                            else:
                                                list1=atomlist

                                        if d==2:
                                            if int(bonent2.get())==1:
                                                list1 =atomlist2
                                            else:
                                                list1=atomlist

                                        if d ==3:
                                            if int(bonent3.get())==1:
                                                list1 =atomlist2
                                            else:
                                                list1=atomlist

                                        if d ==4:
                                            if int(bonent4.get())==1:
                                                list1=atomlist2
                                            else:
                                                list1=atomlist

                                        if d ==5:
                                            if int(bonent5.get())==1:
                                                list1 =atomlist2
                                            else:
                                                list1=atomlist
                                                    
                                        entc.delete(0,1000)
                                        entc.insert(0,0)
                                    
                                        print  resnlist[d]
                                        
                                        fastwalk = True
                                        while fastwalk:
                                            try:
                                                
                                                c = int(entc.get()) + 1
                                                entc.delete(0,1000)
                                                entc.insert(0,c)

                                                entb.delete(0,1000)
                                                entb.insert(0,0)   

                                                print atomlist[c]

                                                flojo = True
                                                while flojo:
                                                    
                                                    b = int(entb.get()) + 1
                                                    entb.delete(0,1000)
                                                    entb.insert(0,b)
                                                    
                                                    try:
                                                    
                                                        if resnlist[e] == ent1B.get():
                                                             chain = chainent.get()
                                                        if resnlist[e] == ent2B.get():
                                                             chain = chainent1.get()
                                                        if resnlist[e] == ent3B.get():
                                                             chain = chainent2.get()
                                                        if resnlist[e] == ent4B.get():
                                                             chain = chainent3.get()
                                                        if resnlist[e] == ent5B.get():
                                                             chain = chainent4.get()
                                                        if resnlist[d] == ent1B.get():
                                                            chain2 = chainent.get()
                                                        if resnlist[d] == ent2B.get():
                                                             chain2 = chainent1.get()                                                   
                                                        if resnlist[d] == ent3B.get():
                                                             chain2 = chainent2.get()                                                   
                                                        if resnlist[d] == ent4B.get():
                                                             chain2 = chainent3.get()                                                   
                                                        if resnlist[d] == ent5B.get():
                                                             chain2 = chainent4.get()

                                                            
                                                        get_distance((chain+' and resi '+resilist[e]+' and name '+list[b]), (chain2+' and resi '+resilist[d]+' and name '+list1[c]))
                                                        
                                                        if entnum.get() != '-1':
                                                           
                                                            g = float(entnum.get()) + float(ranger1.get())
                                                            entnum.delete(0,1000)
                                                            entnum.insert(0,g)

                                                            a = int(enta.get()) + 1
                                                            enta.delete(0,1000)
                                                            enta.insert(0,a)

                                                            if e == 2 and d ==1:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-1]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 3 and d ==1:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-2]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 3 and d ==2:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-1]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 4 and d ==1:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-3]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 4 and d ==2:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-2]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 4 and d ==3:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-1]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 5 and d ==1:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-4]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 5 and d ==2:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-3]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 5 and d ==3:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-2]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 5 and d ==4:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-1]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 6 and d ==1:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-5]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 6 and d ==2:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-4]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 6 and d ==3:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-3]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 6 and d ==4:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-2]+')"%('+entnum.get()+'))\n')
                                                                continue
                                                            if e == 6 and d ==4:
                                                                f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and '+resnlist[e-1]+')"%('+entnum.get()+'))\n')
                                                                continue     
                                                            else:
                                                               f.write( 'cmd.select("'+resnlist[e]+''+str(a)+'", "name '+list[b]+' and resn '+resnlist[e]+' within %s of (name '+list1[c]+' and resn '+resnlist[d]+')"%('+entnum.get()+'))\n')
                                                               continue
                                                    except:
                                                        flojo = False
                                            except:
                                                fastwalk = False
                                    except:
                                        j = a
                                        f.write('cmd.select("'+resnlist[e]+'","')
                                        f.write('byres '+resnlist[e]+''+str(a)+' ')
                                        a = int(enta.get()) - 1
                                        enta.delete(0,1000)
                                        enta.insert(0,a)
                                        sprinting = True
                                        while sprinting:
                                        
                                            if a >1:
                                                f.write('and byres '+resnlist[e]+''+str(a)+' ')
                                                a = int(enta.get()) - 1
                                                enta.delete(0,1000)
                                                enta.insert(0,a)
                                            else:
                                               
                                                f.write('and byres '+resnlist[e]+str(a)+'")\n')
                                                sprinting = False
                                        for i in range(j+1):
                                            if i>=1:
                                                f.write('cmd.delete("'+resnlist[e]+str(i)+'")\n')
                                            else:
                                                running = False

                            except:
                                f.write('cmd.select("Motif","')
                                if len(ent1B.get()) >0:
                                     f.write(''+ent1B.get()+'')
                                else:
                                    funrun = False
                                if len(ent2B.get())>0:      
                                   f.write('('+ent2B.get()+'')
                                else:
                                    f.write('")\n')
                                    funrun = False
                                if len(ent3B.get()) >0:
                                    f.write('('+ent3B.get()+'')
                                else:
                                    f.write(')")\n')
                                    funrun = False
                                if len(ent4B.get()) >0:
                                    f.write('('+ent4B.get()+'')
                                else:
                                    f.write('))")\n')
                                    funrun = False
                                if len(ent5B.get()) >0:
                                   f.write('('+ent5B.get()+'')
                                   f.write('))))")\n')
                                elif len(ent4B.get()) >0:
                                   f.write(')))")\n')
                                funrun = False

                    

                    if ent1B.get()!='':
                        f.write("cmd.delete('"+ent1B.get()+"')\n")
                    if ent2B.get()!='':
                        f.write("cmd.delete('"+ent1F.get()+"')\n")
                    if ent3B.get()!='':
                        f.write("cmd.delete('"+ent2F.get()+"')\n")
                    if ent4B.get()!='':
                        f.write("cmd.delete('"+ent3F.get()+"')\n")
                    if ent5B.get()!='':
                        f.write("cmd.delete('"+ent4F.get()+"')\n")

                    f.write('cmd.hide("everything","all")\n')
                    f.write('cmd.show("cartoon", "all")\n')
                    f.write('cmd.set("cartoon_transparency","0.5", "all")\n')
                    f.write('cmd.show("sticks","Motif")\n')
                    f.write('cmd.color("grey","all")\n')
                    f.write('cmd.color("oxygen","(elem O and Motif)")\n')
                    f.write('cmd.color("nitrogen","(elem N and Motif)")\n')
                    f.write('cmd.color("sulfur","(elem S and Motif)")\n')
                    f.write('cmd.color("hydrogen","(elem H and Motif)")\n')
                    f.write('cmd.color("white","(elem C and Motif)")\n')
                    f.write('cmd.deselect()\n')
                    f.write('cmd.orient("Motif")\n')
                    
                   
                    print '\n\n\n\n\n\nMotif Maker\nBy: Brett Hanson and Charlie Westin\n2007\n'+str(int(len(resnlist))-1)+' Amino Acid Motif Written \n\n\n\n\n\n'
                    f.close()
                    interior.mainloop()
                except:
                    interior.mainloop()
                    
            but1.bind('<Button-1>', makemotif)
            
            selection1 = Pmw.OptionMenu(interior,label_text = 'Residue 1:',labelpos = 'w',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command= set_motif1)
            selection1.grid(row = 0, column =0)

            selection2 = Pmw.OptionMenu(interior,label_text = 'Residue 2:',labelpos = 'w',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command= set_motif2)
            selection2.grid(row = 1, column =0)
            
            selection3 = Pmw.OptionMenu(interior,label_text = 'Residue 3:',labelpos = 'w',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command= set_motif3)
            selection3.grid(row = 2, column =0)

            selection4 = Pmw.OptionMenu(interior,label_text = 'Residue 4:',labelpos = 'w',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command=set_motif4)
            selection4.grid(row = 3, column =0)
            
            selection5 = Pmw.OptionMenu(interior,label_text = 'Residue 5:',labelpos = 'w',
                items = (' ','gly', 'ala', 'val','leu', 'ile', 'met','pro', 'phe', 'tyr', 'trp', 'ser', 'thr', 'cys', 'lys', 'arg', 'his', 'asp', 'glu', 'asn', 'gln'),
                menubutton_width = 8, command= set_motif5)
            selection5.grid(row = 4, column =0) 

            selection = Pmw.OptionMenu(interior,labelpos = 'w',
                label_text = 'Chain 1:',
                items = (''),
                menubutton_width = 8, command = set_sel1)                       
            selection.grid(row=0, column=4)

            selectiond = Pmw.OptionMenu(interior,labelpos = 'w',
                label_text = 'Chain 2:',
                items = (''),
                menubutton_width = 8, command = set_sel2)                       
            selectiond.grid(row=1, column=4)

            selectionc = Pmw.OptionMenu(interior,labelpos = 'w',
                label_text = 'Chain 3:',
                items = (''),
                menubutton_width = 8, command = set_sel3)                       
            selectionc.grid(row=2, column=4)

            selectionb = Pmw.OptionMenu(interior,labelpos = 'w',
                label_text = 'Chain 4:',
                items = (''),
                menubutton_width = 8, command = set_sel4)                       
            selectionb.grid(row=3, column=4)

            selectiona = Pmw.OptionMenu(interior,labelpos = 'w',
                label_text = 'Chain 5:',
                items = (''),
                menubutton_width = 8, command = set_sel5)                       
            selectiona.grid(row=4, column=4)


            selection11 = Pmw.OptionMenu(interior,label_text = 'BackBone:',labelpos = 'w',
                items = ('Off', 'On'),
                menubutton_width = 8, command= bone1)
            selection11.grid(row = 0, column =3)
            
            selection12 = Pmw.OptionMenu(interior,label_text = 'BackBone:',labelpos = 'w',
                items = ('Off', 'On'),
                menubutton_width = 8, command= bone2)
            selection12.grid(row = 1, column =3)
            
            selection13 = Pmw.OptionMenu(interior,label_text = 'BackBone:',labelpos = 'w',
                items = ('Off', 'On'),
                menubutton_width = 8, command= bone3)
            selection13.grid(row = 2, column =3)
            
            selection14 = Pmw.OptionMenu(interior,label_text = 'BackBone:',labelpos = 'w',
                items = ('Off', 'On'),
                menubutton_width = 8, command= bone4)
            selection14.grid(row = 3, column =3)
            
            selection15 = Pmw.OptionMenu(interior,label_text = 'BackBone:',labelpos = 'w',
                items = ('Off', 'On'),
                menubutton_width = 8, command= bone5)
            selection15.grid(row =4, column =3)

            framerange = Frame(interior)
            framerange.grid(row=5, column=0,columnspan = 3, sticky = 'e')
            ballrange = Pmw.Balloon(interior)
            ballrange.bind(framerange, 'Changes Precision of Motif Definition\nDefault = 2')
            ranger1 = Scale(framerange, width =8)
            ranger1.configure(troughcolor="#ffffff")
            ranger1.configure(length="160")
            ranger1.configure(orient="horizontal")
            ranger1.configure(resolution="0.1")
            ranger1.configure(to="4.0")    
            ranger1.grid(row=5, column=1,columnspan = 4, sticky = 'e')
            ranger1.set(2)

        
            labrange = Label(interior, text='Precision Factor:')
            labrange.grid(row=5, column=0, sticky='sw')



##            #Next Tab
##            page = notebook.add('Run Motifs')
##            notebook.tab('Run Motifs').focus_set()
            group = Pmw.Group(root, tag_text = 'Run Motif')
            group.grid(row=1, column=0, padx=190, pady=0, sticky = 'NE')
            interior = group.interior()

            def getmotif(ranger):
                import tkFileDialog
                f = tkFileDialog.askopenfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Motifs")
                try:
                    cmd.do('run '+f+'')
                    interior.mainloop()
                except:
                    interior.mainloop()
            openbtn = Button(interior, text= 'Open Motif')
            openbtn.grid()
            openbtn.bind('<Button-1>', getmotif)
            
            

            
                
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
                              import tkMessageBox
                              tkMessageBox.showinfo('Alert', "No motif polar contacts to hide")

                        
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
                            import tkMessageBox
                            tkMessageBox.showinfo('Alert', "No substrate found")
                        
                    elif tag=='Show label':

                     objects = cmd.get_names('all')
                     try:
                                  cmd.label('''(name ca+C1*+C1' and (byres(Motif)))''','''"%s-%s"%(resn,resi)''')
                                  if 'Adjacent' in objects:
                                         cmd.label('''(name ca+C1*+C1' and (byres(Adjacent)))''','''"%s-%s"%(resn,resi)''')
                     except:
                                import tkMessageBox
                                tkMessageBox.showinfo('Alert', "Select a motif first")

                        
                    elif tag=='Hide Label':
                        objects = cmd.get_names('all')
                        try:
                              cmd.label("Motif","''")
                              if 'Adjacent' in objects:
                                  cmd.label('byres Adjacent',"''")
                        except:
                                import tkMessageBox
                                tkMessageBox.showinfo('Alert', "No motif labels to hide")

                                
                    elif tag=='Hide Substrate':
                                      try:
                                        cmd.hide('sticks', 'substrate')
                                      except:
                                        import tkMessageBox
                                        tkMessageBox.showinfo('Alert', "No substrate selected")
                                                

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
            
                           
            showround = Button(frameadj, width = 12, text = 'Adjacent')
            showround.grid(row=1, column=0, padx=1, pady=1, sticky=NW)
            
            def roundres(event):
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
                    import tkMessageBox
                    tkMessageBox.showinfo('Alert', 'You must load a motif first')
                    interior.mainloop()
            showround.bind('<Button-1>', roundres)
            delres = Button(interior, width = 14, text = 'Delete Adjacent')
            delres.grid(row=1, column=1, padx=1, pady=1, sticky=NW)
            def resdel(event):
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
                    import tkMessageBox
                    tkMessageBox.showinfo('Alert', 'You must load a motif first')
                    interior.mainloop()
                
            delres.bind('<Button-1>', resdel)
            def runcusmotif(self):
              a = ['']
              for object in os.listdir('./modules/pmg_tk/startup/Motifs'):
                  a.append(object)
              motif = self.motifdrop.getcurselection()
              for item in motif:
                  tag = item
              try:
                 for i in range(1, 100, 1):
                      if a[i] in tag:
                          cmd.do('run ./modules/pmg_tk/startup/Motifs/'+a[i])
              except:
                  pass
              
           

           
    

                      
       

                     
            


        mobtn.bind('<Button-1>', loadmotifer)

        #--------------------------------------#
        #			                    #
        #           View Options                            #
        #                                                               #
        #--------------------------------------#
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
            if script=='1':
                f.write(''' cmd.set("ambient", '''+str(self.asca.get())+''')\n''')
        stupid.bind('<Button-1>', finickystuff)
        

        #--------------------------------------#
        #			               #
        #             ToolBox TAB                       #
        #                                                               #
        #--------------------------------------#
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
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
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
               
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That PDB is not loaded or entry is not capitalized')
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
            if script=='1':
                f.write('''cmd.set("orthoscopic", "on")\n''')
        orthoon.bind('<Button-1>', turnorthon)
        orthoff = Button(frameorthoff, text = 'Orthoscopic Off',width = 16)
        orthoff.grid(row=1, column=0, padx=2, pady=2, sticky=NW)
        def turnorthoff(event):
            cmd.set("orthoscopic", "off")
            if script=='1':
                f.write('''cmd.set("orthoscopic", "off")\n''')
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
            if script=='1':
                f.write('''cmd.set("field_of_view", '''+setfieldofview.get()+''')\n''')
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
            if script=='1':
                f.write('''cmd.orient('all')\n''')
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
        


        #-------------------------------------------------------------#
        #                                                                                                       #
        #                     Advancd Toolbox Tab                                       #
        #                                                                                                       #
        #-------------------------------------------------------------#

       #------------------Electron Density Group--------------------
        #--------Making more frames, and thusly balloon helps
        #--------Then functions and buttons for all diff. density commands
        


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
            if script=='1':
                f.write('''cmd.hide('everything')
cmd.set('sphere_transparency',0.60)
cmd.set('sphere_color','white') 
cmd.set('auto_sculpt',1)
cmd.mouse('three_button_editing')
cmd.show('sticks')
cmd.show('spheres')
cmd.zoom('all',4)'''/n)
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
                if script=='1':
                    f.write('''cmd.isomesh('map1','map', '''+contour1.get()+''')\n''')
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
                    if script=='1':
                        f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isomesh("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.isomesh('map1','map','''+str(contour1.get())+''')\n''')
                except:
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present')
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
                if script=='1':
                        f.write('''cmd.isodot('map1','map', '''+str(contour1.get())+''')\n''')
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
                    if script=='1':
                        f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isodot("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isodot('map1','map', '''+str(contour1.get())+''')\n''')
               except:
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present')
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
                if script=='1':
                        f.write('''cmd.isosurface('map1','map', '''+contour1.get()+''')\n''')
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
                    if script=='1':
                        f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isosurface("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isosurface('map1','map', '''+str(contour1.get())+''')\n''')
                except:
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present')
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
            if script=='1':
              f.write('''cmd.set("suspend_updates",1,quiet=1)
 cmd.remove("hydro")
 cmd.disable()
 cmd.enable('all')
 cmd.map_new('map',"gaussian","0.75", 'all')
 cmd.set('roving_isomesh', '''+str(rovingradius1.get())+''')
 cmd.set("roving_detail",1)
 cmd.set("stick_radius",0.5)
 cmd.set("roving_sticks",0)
 cmd.set('roving_lines', '''+str(rovingradius1.get())+''')
 cmd.set("roving_polar_contacts",0)
 cmd.set("line_width","3")
 cmd.set("roving_map1_name",'map')
 cmd.isomesh("map1", "map", 9999.0, 'all')
 cmd.set("suspend_updates",0,quiet=1)
 cmd.refresh()
 cmd.delete('rov_s1')
 cmd.set('roving_isosurface',0)\n''')

          except:
            import tkFileDialog
            import tkMessageBox
            tkMessageBox.showinfo("Error", 'No PDB is present')
            interior.mainloop()
        #cmd.extend('roving_density',roving_density)
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
                if script=='1':
                        f.write('''cmd.remove("hydro")
cmd.disable()
cmd.enable('all')                
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.set("roving_detail",1)
cmd.set("roving_origin",1)
cmd.set('roving_lines', 8)
cmd.set("roving_polar_contacts",0)
cmd.set("line_width","3")
cmd.set("roving_map1_name",'map')
cmd.set('roving_isosurface', '''+str(rovingradius1.get())+''')
cmd.show('lines', 'all')
cmd.set('roving_isomesh', '0')
cmd.set('transparency', '0.15')
cmd.delete('rov_1')
cmd.delete('rov_m1')\n''')
               
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'No PDB is present')
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
                if script=='1':
                        f.write(''' cmd.isomesh('map1','map', '''+contour1.get()+''', 'sele')\n''')
            except:
                try:
                    
                    cmd.remove("hydro")      
                    cmd.enable('all')
                    cmd.map_new('map',"gaussian","0.75", 'all')
                    cmd.isomesh('map1','map', contour1.get(), 'sele')
                    if script=='1':
                        f.write('''cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isomesh('map1','map', '''+str(contour1.get())+''', 'sele')\n''')
                    
                except:
                    if script=='1':
                        f.write('''cmd.orient('all')\n''')
                    cmd.orient('all')
                    
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
                    
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
                if script=='1':
                        f.write('''cmd.isodot('map1','map', '''+contour1.get()+''', 'sele')\n''')
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
                    if script=='1':
                        f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isodot("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isodot('map1','map', '''+str(contour1.get())+''', 'sele')
cmd.get_names('all')\n''')
                except:
                    cmd.orient('all')
                    if script=='1':
                        f.write('''cmd.orient('all')\n''')
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
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
                if script=='1':
                        f.write('''cmd.isosurface('map1','map','''+ contour1.get()+''', 'sele')\n''')
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
                    if script=='1':
                        f.write('''cmd.set("suspend_updates",1,quiet=1)
cmd.remove("hydro")      
cmd.enable('all')
cmd.map_new('map',"gaussian","0.75", 'all')
cmd.isosurface("map1", "map", 9999.0, 'all')
cmd.set("suspend_updates",0,quiet=1)
cmd.refresh()
cmd.isosurface('map1','map', '''+str(contour1.get())+''', 'sele')\n''')
                except:
                    cmd.orient('all')
                    if script=='1':
                        f.write('''cmd.orient('all')\n''')
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No PDB is present\nOr there is no selection ('"sele"')')
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
                if script=='1':
                    f.write('''cmd.map_double('map', '1')\n''')
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'No map is present')
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
              import tkFileDialog
              file = tkFileDialog.askopenfilename(defaultextension=".ccp4", initialdir="./PyMOL/")
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()

                    else:
                        cmd.isomesh(nameit.get(),pdbname.get(), contour1.get())
                except:
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present')
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                     elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                     else:
                        cmd.isodot(nameit.get(), pdbname.get(), contour1.get())
                except:
                     import tkFileDialog
                     import tkMessageBox
                     tkMessageBox.showinfo("Error", 'No map is present')
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    else:
                        cmd.isosurface(nameit.get(), pdbname.get(), contour1.get())
                except:
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present')
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()

                    else:
                        cmd.isomesh(nameit.get(),pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                     elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                     else:
                        cmd.isodot(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
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
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo("Error", 'Enter a name for the object')
                        interior.mainloop()
                    elif len(pdbname.get()) < 1:
                        import tkFileDialog
                        import tkMessageBox
                        tkMessageBox.showinfo('Error', "Enter the Map Filename")
                        interior.mainloop()
                    
                    else:
                        cmd.isosurface(nameit.get(), pdbname.get(), contour1.get(), ('sele'))
                except:
                    cmd.orient('all')
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present\n Or there is no selection ("sele")')
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
                    import tkFileDialog
                    import tkMessageBox
                    tkMessageBox.showinfo("Error", 'No map is present')
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

        

      #-----------------------------------------------------#
      #                                                     #
      #                                                     #
      #                 Movie Maker Tab                     #
      #                                                     #
      #-----------------------------------------------------#

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
	
        from pymol import movie 
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
          
          import tkMessageBox
          if int(entl.get())<2:
            if tkMessageBox.askyesno('Load Frames', 'Click yes to load in discrete mode'):
                import tkFileDialog
                file = tkFileDialog.askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
                if len(file)>0:
                  cmd.load(file, "mov", entl.get(), discrete=1)
     	    else:
                import tkFileDialog
                file = tkFileDialog.askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
                if len(file)>0:
                  cmd.load(file, "mov", entl.get())
          else:
            import tkFileDialog
            file = tkFileDialog.askopenfilename(defaultextension=entfilex.get(), initialdir=('./modules/pmg_tk/startup/Movies/ ' + name_mov.get()))
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
                import tkMessageBox
                tkMessageBox.showinfo('Alert!', 'You need to enter the frame number')
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
              import tkFileDialog
              file = tkFileDialog.asksaveasfilename(defaultextension=entfilex.get(), initialdir="./modules/pmg_tk/startup/Movies/ " + name_mov.get(), initialfile= "frame" + enti.get())
              if len(file)>0:
                  cmd.save(file)
              page.mainloop()
            except:
              a = int(enti.get()) + 1
              enti.delete(0,100000)
              enti.insert(0,a)
              import tkFileDialog
              file = tkFileDialog.asksaveasfilename(defaultextension=entfilex.get(), initialdir="./modules/pmg_tk/startup/Movies/ " + name_mov.get(), initialfile= "frame" + enti.get())
              if len(file)>0:
                  cmd.save(file)
            page.mainloop()
          except:
            import tkFileDialog
            import tkMessageBox
            tkMessageBox.showinfo("Error", 'Please enter a movie title')
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
                import tkMessageBox
                tkMessageBox.showinfo('Alert!', 'Enter the amount of frames to be in the movie')
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
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.mask(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()

        def unmaskedman(event):
            try:
              if len(maskent.get()) < 1:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.unmask(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()
        def maskallexcept(event):
            try:
              if len(maskent.get()) < 1:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.mask('All')
                cmd.unmask(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()
        cmd.extend('maskallexcept',maskallexcept)
        def protectallexcept(event):
            try:
              if len(maskent.get()) < 1:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.protect('All')
                cmd.deprotect(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()
        def protectme(event):
            try:
              if len(maskent.get()) < 1:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.protect(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()
        def deprotectme(event):
            try:
              if len(maskent.get()) < 1:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'Please enter the name of an object.')
                interior.mainloop()
              else:
                cmd.deprotect(maskent.get())
            except:
                import tkFileDialog
                import tkMessageBox
                tkMessageBox.showinfo("Error", 'That object is not present')
            interior.mainloop()
        maskbtn.bind('<Button-1>', maskedman)
        unmaskbtn.bind('<Button-1>', unmaskedman)
        maskaebtn.bind('<Button-1>', maskallexcept)
        protectbtn.bind('<Button-1>', protectme)
        deprotectbtn.bind('<Button-1>', deprotectme)
        
        #auto adjust notebook size
 	notebook.setnaturalsize()
 	
        #------Version 1---#
 	
 	#checks to see if there is a file loaded in the viewer prior to the GUI being opened
 	#-----only self.update(self.p) really does anything, not sure why the rest is here---
        self.fileLoaded = ' '
        loadedPDB=cmd.get_names()
        if loadedPDB!=[]:
                self.fileLoaded = loadedPDB[0]
                self.p=PDBParser()
                self.update(self.p)
        self.fileLoaded = ' '
 

 	
 	

    #--------------------------------------#
    #      		                   #
    #   HANDLE BUTTONS AT BOTTOM OF GUI    #
    #    (open, fetch.., help, exit)       #
    #--------------------------------------#         
    def execute(self, result):
        import tkFileDialog
    
        if result == 'Open':
            file=tkFileDialog.askopenfilename(initialdir='./PyMol')
            if file:
            	cmd.load(file)
            	self.pdbCode = file
            	#cmd.select('selection','all')
           	#cmd.deselect()
           	#----Connect to parser to read file------
		self.p=PDBParser()
            	self.p.readFile(file)
            	self.update(self.p)
        elif result == 'Help':
            self.help()
        elif result == 'Fetch PDB':
            self.getPdb()

        elif result == 'Clear':
            cmd.reinitialize()
        elif result == 'Thanks':
            self.acknowledge()
        else:
            self.dialog.withdraw()

# Update all Labels on Information Tab
    def update(self, p):
        chainList=['All','Ligands','Not Selected','Hydrophobic','Hydrophilic']
        self.cmdType = 'PyMOL'
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
            if script=='1':
                f.write('''cmd.create('ligands', "(resn '''+string.strip(hetero)+''')")\n''')
        cmd.select('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
        cmd.disable('protein')	
        cmd.select('nucleic_acid', 'resn a+g+c+t+u')
        cmd.disable('nucleic_acid')
        cmd.select('ligands', 'het')
        cmd.disable('ligands')
        cmd.remove('resn HOH')
        if script=='1':
            f.write('''cmd.select('protein', 'resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.disable('protein')	
cmd.select('nucleic_acid', 'resn a+g+c+t+u')
cmd.disable('nucleic_acid')
cmd.select('ligands', 'het')
cmd.disable('ligands')
cmd.remove('resn HOH')\n''')
        self.populate()
        checkitforthese()
        cmd.orient('all')
    #--------Delete empty selections--------------
    	#Adapted from Kristian Rothers' H-bond script
    def acknowledge(self):
      import webbrowser
      webbrowser.open('./modules/pmg_tk/startup/Thanks.html')

    def checkitforthese(self):
      checktiforthese()


     #---Delete empty Chain selections for Chain Pull Movie------
    def checkforchain(self):
      checkforchain()



    #-------Version 1---------#

    #--------------------------------------------#
    #				    #
    #        "ADVANED" TAB METHODS  #
    #                                                                        #
    #-------------------------------------------#
    
    #------------------------------------------#
    #              Cartoon Functions                    #
    #------------------------------------------#
    
    # Set Cartoon Thickness 
    def cartoon_thickness(self):
        self.populate()
        self.sel1 = ''
        value = self.toonThickness.get()
        cmd.set('cartoon_rect_width', value, 'all') # strands
        cmd.set('cartoon_oval_width', value, 'all') # helices
        if script=='1':
            f.write('''value = '''+str(self.toonThickness.get())+'''
cmd.set('cartoon_rect_width', value, 'all')
cmd.set('cartoon_oval_width', value, 'all')\n''')
        

    # Set Cartoon Width 
    def cartoon_width(self):
        self.populate()
        self.sel1 = ''
        value = self.toonWidth.get()
        cmd.set('cartoon_rect_length', value, 'all') # strands
        cmd.set('cartoon_oval_length', value, 'all') # helices
        if script=='1':
            f.write('''value = '''+str(self.toonWidth.get())+'''
cmd.set('cartoon_rect_length', value, 'all')
cmd.set('cartoon_oval_length', value, 'all')\n''')
            
    # Set Cartoon Transparency
    def cartoon_transparency(self):
        self.populate()
        self.sel1 = ''
        amount=self.cartoonTransparency.get()
        cmd.set('cartoon_transparency', amount, 'all')
        if script=='1':
            f.write('''amount='''+str(self.cartoonTransparency.get())+'''
cmd.set('cartoon_transparency', amount, 'all')\n''')
       
    # Set Cartoon Tube Radius 
    def cartoon_tube_radius(self):
        self.populate()
        self.sel1 = ''
        value = self.toonTubeRadius.get()
        cmd.set('cartoon_tube_radius', value, 'all') # strands
        if script=='1':
            f.write('''value = '''+str(self.toonTubeRadius.get())+'''
cmd.set('cartoon_tube_radius', value, 'all')\n''')
        
    #Set Ribbon Type
    def ribType(self,tag):
        try:
            try:
                if tag == 'Skip':
                        cmd.cartoon('skip', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('skip', '''+self.sel1+''')\n''')
                elif tag == 'Automatic':
                        cmd.cartoon('automatic', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('automatic', '''+self.sel1+''')\n''')
                elif tag == 'Oval':
                        cmd.cartoon('oval', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('oval', '''+self.sel1+''')\n''')
                elif tag == 'Tube':
                        cmd.cartoon('tube', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('tube', '''+self.sel1+''')\n''')
                elif tag == 'Rectangle':
                        cmd.cartoon('rectangle', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('rectangle', '''+self.sel1+''')\n''')
                elif tag == 'Loop':
                        cmd.cartoon('loop', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('loop', '''+self.sel1+''')\n''')
                elif tag == 'Arrow':
                        cmd.cartoon('arrow', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('arrow', '''+self.sel1+''')\n''')
                elif tag == 'Dumbbell':
                        cmd.cartoon('dumbbell', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('dumbbell', '''+self.sel1+''')\n''')
                elif tag == 'Putty':
                        cmd.cartoon('putty', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('putty', '''+self.sel1+''')\n''')
            except:
                self.populate()
                if tag == 'Skip':
                        cmd.cartoon('skip', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('skip', '''+self.sel1+''')\n''')
                elif tag == 'Automatic':
                        cmd.cartoon('automatic', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('automatic', '''+self.sel1+''')\n''')
                elif tag == 'Oval':
                        cmd.cartoon('oval', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('oval', '''+self.sel1+''')\n''')
                elif tag == 'Tube':
                        cmd.cartoon('tube', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('tube', '''+self.sel1+''')\n''')
                elif tag == 'Rectangle':
                        cmd.cartoon('rectangle', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('rectangle', '''+self.sel1+''')\n''')
                elif tag == 'Loop':
                        cmd.cartoon('loop', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('loop', '''+self.sel1+''')\n''')
                elif tag == 'Arrow':
                        cmd.cartoon('arrow', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('arrow', '''+self.sel1+''')\n''')
                elif tag == 'Dumbbell':
                        cmd.cartoon('dumbbell', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('dumbell', '''+self.sel1+''')\n''')
                elif tag == 'Putty':
                        cmd.cartoon('putty', self.sel1)
                        if script=='1':
                            f.write('''cmd.cartoon('putty', '''+self.sel1+''')\n''')
        except:
            import tkMessageBox
            tkMessageBox.showinfo('Error', 'Drop down menu is set to an invalid selection\nYou may need to update selections')
                
    #------------------------------------------#
    #               Sphere Functions           #
    #------------------------------------------#
    # Set Sphere Transparency
    def sphere_transparency(self):
        self.populate()
        self.sel1 = 'all'
        amount=self.sphereTransparency.get()
        cmd.set('sphere_transparency', amount, 'all')
        if script=='1':
            f.write('''amount='''+str(self.sphereTransparency.get())+'''
cmd.set('sphere_transparency', amount, 'all')\n''')
                
    # Set Sphere Size
    def sphereSize(self):
        self.populate()
        self.sel1 = 'all'
        size=self.sphereScale.get()
        cmd.set('sphere_scale', size, 'all')
        if script=='1':
            f.write('''size='''+str(self.sphereScale.get())+'''
cmd.set('sphere_scale', size, 'all')\n''')
      
    #------------------------------------------#
    #              Surface  Functions          #
    #------------------------------------------#       
    # Set Surface Transparency
    def surface_transparency(self):
        self.populate()
        self.sel1 = 'all'
        amount=self.surfaceTransparency.get()
        cmd.set('transparency', amount, 'all')
        if script=='1':
            f.write('''amount='''+str(self.surfaceTransparency.get())+'''
cmd.set('transparency', amount, 'all')\n''')
       
    #------------------------------------------#
    #              Stick  Functions            #
    #------------------------------------------#       
    # Set Stick Transparency
    def stick_transparency(self):
        self.populate()
        self.sel1 = 'all'
        amount=self.stickTransparency.get()
        cmd.set('stick_transparency', amount, 'all')
        if script=='1':
            f.write('''amount='''+str(self.stickTransparency.get())+'''
cmd.set('stick_transparency', amount, 'all')\n''')
        
     # Set Stick Radius
    def stickRad(self):
        self.populate()
        self.sel1 = 'all'
        size=self.stickRadius.get()
        cmd.set('stick_radius',size, 'all')
        if script=='1':
            f.write('''size='''+str(self.stickRadius.get())+'''
cmd.set('stick_radius',size, 'all')\n''')
       


         #------------------------------------------#
        #             Set Default Values                      #
        #------------------------------------------#       
    def set_advanced_defaults(self, tag):
      if tag == 'cartoon':
        
        # apply the changes
        cmd.set('cartoon_rect_length', '1.4', 'all') 
        cmd.set('cartoon_oval_length', '1.4', 'all')
        cmd.set('cartoon_rect_width', '0.3', 'all') 
        cmd.set('cartoon_oval_width', '0.3', 'all') 
        cmd.set('cartoon_tube_radius','0.5','all')
        cmd.set('cartoon_transparency','0.0','all')
        cmd.cartoon('automatic',self.sel1)
        self.toonWidth.set('1.4')
        self.toonThickness.set('0.3')
        self.cartoonTransparency.set('0.0')
        self.toonTubeRadius.set('0.5')
        self.ribbonTypes.invoke(0)
        if script=='1':
          f.write('''cmd.set('cartoon_rect_length', '1.4', 'all') 
cmd.set('cartoon_oval_length', '1.4', 'all')
cmd.set('cartoon_rect_width', '0.3', 'all') 
cmd.set('cartoon_oval_width', '0.3', 'all') 
cmd.set('cartoon_tube_radius','0.5','all')
cmd.set('cartoon_transparency','0.0','all')
cmd.cartoon('automatic','''+self.sel1+''')
self.toonWidth.set('1.4')
self.toonThickness.set('0.3')
self.cartoonTransparency.set('0.0')
self.toonTubeRadius.set('0.5')
self.ribbonTypes.invoke(0)\n''')
                
      elif tag == 'spheres':

        cmd.set('sphere_scale','0.7','all')
        cmd.set('sphere_transparency','0.0','all')
        self.sphereScale.set('0.7')
        self.sphereTransparency.set('0.0')
        if script=='1':
          f.write('''cmd.set('sphere_scale','0.7','all')
cmd.set('sphere_transparency','0.0','all')
self.sphereScale.set('0.7')
self.sphereTransparency.set('0.0')\n''')
                
      elif tag == 'sticks':

        cmd.set('stick_radius','0.2','all')
        cmd.set('stick_transparency','0.0','all')
        self.stickRadius.set('0.2')
        self.stickTransparency.set('0.0')
        if script=='1':
          f.write('''cmd.set('stick_radius','0.2','all')
cmd.set('stick_transparency','0.0','all')
self.stickRadius.set('0.2')
self.stickTransparency.set('0.0')\n''')
                
      elif tag == 'surface':	
        # apply the changes
        cmd.set('transparency','0.0','all')
        self.surfaceTransparency.set('0.0')
        if script=='1':
          f.write('''cmd.set('transparency','0.0','all')
self.surfaceTransparency.set('0.0')\n''')

      elif tag == 'ambient':
        cmd.set('ambient', '0.25', 'all')
        self.asca.set('0.25')
        if script=='1':
          f.write('''cmd.set('ambient', '0.25', 'all')
self.asca.set('0.25')\n''')
    cmd.extend('set_advanced_defaults',set_advanced_defaults)
    #--------Version 2---------#
    #deletes created objects used in various tools to save on memory usage
#     def delcrea(self):
#             object = cmd.get_names('all')
#             if 'surface' in object:
#                 cmd.delete('surface')
#             if 'mesh1' in object:
#                 cmd.delete('mesh1')
#             if 'cartoon' in object:
#                 cmd.delete('cartoon')
#             if 'helix' in object:
#                 cmd.delete('helix')
#             if 'sheets' in object:
#                 cmd.delete('sheets')
#             if 'sticks' in object:
#                 cmd.delete('sticks')
#             if 'rov_1' in object:
#                 cmd.delete('rov_1')
#             if 'rov_m1' in object:
#                 cmd.delete('rov_m1')
#             if 'map1' in object:
#                 cmd.delete('map1')
#             if 'sphere1' in object:
#                 cmd.delete('sphere1')
#             if 'rov_pc' in object:
#                 cmd.delete('rov_pc')
#             if 'rov_s1' in object:
#                 cmd.delete('rov_s1')
#             cmd.set("roving_detail",0)
#             cmd.set("roving_origin",0)
#             cmd.set("roving_sticks",0)
#             cmd.set('roving_spheres',0)
#             cmd.set("roving_polar_contacts",0)
#             cmd.set('roving_lines',0)
#             cmd.delete('rov_1')
#             cmd.set('roving_isosurface',0)
            
    
          #populates the selection list      
    def populate(self):
      letters = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

      objects = cmd.get_names('all')
      cmd.select('protein','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
      cmd.select('nucleic_acid', 'resn a+t+g+c+u')
      cmd.select('hydrophobic','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
      cmd.select('hydrophilic','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
      cmd.select('acidic','resn ASP+GLU')
      cmd.select('basic','resn ARG+HIS+LYS')
      cmd.select('ligands', 'het')
      cmd.select('heme', 'resn hem')
      cmd.disable('heme')
      cmd.disable('ligands')
      cmd.disable('basic')
      cmd.disable('acidic')
      cmd.disable('hydrophilic')
      cmd.disable('hydrophobic')
      cmd.disable('nucleic_acid')
      cmd.disable('protein')
      if script=='1':
        f.write('''objects = cmd.get_names('all')
cmd.select('protein','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.select('nucleic_acid', 'resn a+t+g+c+u')
cmd.select('hydrophobic','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
cmd.select('hydrophilic','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
cmd.select('acidic','resn ASP+GLU')
cmd.select('basic','resn ARG+HIS+LYS')
cmd.select('ligands', 'het')
cmd.select('heme', 'resn hem')
cmd.disable('heme')
cmd.disable('ligands')
cmd.disable('basic')
cmd.disable('acidic')
cmd.disable('hydrophilic')
cmd.disable('hydrophobic')
cmd.disable('nucleic_acid')
cmd.disable('protein')\n''')
      checkitforthese()
      for each in letters:
        cmd.select("Chain-" + each, "chain " + each)

      if script=='1':
        f.write('''cmd.select("Chain-A", "chain A")
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
cmd.select("Chain-Z", "chain Z")\n''')
        checkforchain()            
        items=[]
        objects = cmd.get_names('all')
        items.append('All')
        items.append('Not Selected')
        if 'protein' in objects:
          items.append('protein')
        if 'nucleic_acid' in objects:
          items.append('nucleic_acid')
        if 'hydrophobic' in objects:
          items.append('hydrophobic')
        if 'hydrophilic' in objects:
          items.append('hydrophilic')
        if 'acidic' in objects:
          items.append('acidic')
        if 'basic' in objects:
          items.append('basic')
        if 'ligands' in objects:
          items.append('ligands')
        if 'heme' in objects:
          items.append('heme') 
	#Checks to see if there are chains in objects


        for i in range(len(letters)):
          if 'Chain-' + letters[i] in objects:
            items.append('Chain-' + letters[i])

        self.sel1 = 'All'
        self.sel = 'All'
        items.sort()
        self.selection.setitems(items) 
        self.advancedSelection.setitems(items)

    #-------The End------for now.... 
def write_script(tag):
  if tag == 'Off':
    script ='0'
    
  if tag=='On': #write a scritp
    try:
      script = '1'
      import tkFileDialog
      Q = tkFileDialog.asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Scripts")
      cmd.do('log_open %s,a' %(Q))            
      self.f=open(Q, 'w')
    except:
      pass

def delcrea():
  object = cmd.get_names('all')
  if 'surface' in object:
      cmd.delete('surface')
  if 'mesh1' in object:
      cmd.delete('mesh1')
  if 'cartoon' in object:
      cmd.delete('cartoon')
  if 'helix' in object:
      cmd.delete('helix')
  if 'sheets' in object:
      cmd.delete('sheets')
  if 'sticks' in object:
      cmd.delete('sticks')
  if 'rov_1' in object:
      cmd.delete('rov_1')
  if 'rov_m1' in object:
      cmd.delete('rov_m1')
  if 'map1' in object:
      cmd.delete('map1')
  if 'sphere1' in object:
      cmd.delete('sphere1')
  if 'rov_pc' in object:
      cmd.delete('rov_pc')
  if 'rov_s1' in object:
      cmd.delete('rov_s1')
  cmd.set("roving_detail",0)
  cmd.set("roving_origin",0)
  cmd.set("roving_sticks",0)
  cmd.set('roving_spheres',0)
  cmd.set("roving_polar_contacts",0)
  cmd.set('roving_lines',0)
  cmd.delete('rov_1')
  cmd.set('roving_isosurface',0)
cmd.extend('delcrea',delcrea)


def set_defaults():
  cmd.hide('everything','all')
  cmd.set('transparency','0.0','all')
  cmd.set('cartoon_transparency','0.0','all')
  cmd.set('transparency','0','all')
  cmd.set('sphere_transparency','0.0','all')
  cmd.set('stick_transparency','0.0','all')
  cmd.set('sphere_scale','0.7','all')
  cmd.cartoon('automatic', 'all')
  cmd.set('stick_radius','0.2','all')
  if script == '1':
    f.write('''cmd.hide("everything","all") 
cmd.set("transparency","0.0","all")
cmd.set("cartoon_transparency","0.0","all")
cmd.set("transparency","0","all")
cmd.set("sphere_transparency","0.0","all")
cmd.set("stick_transparency","0.0","all")
cmd.set("sphere_scale","0.7","all")
cmd.cartoon("automatic", "all")
cmd.set("stick_radius","0.2","all")\n''')
  delcrea()
cmd.extend('set_defaults',set_defaults)

def checkforchain():
    objects = cmd.get_names('all')
    if 'Chain-A' in objects:
        x1 = cmd.index('Chain-A')
        n1  = len(x1)
        if(n1 < 1):
            cmd.delete('Chain-A')
            if script=='1':
                f.write('''cmd.delete('Chain-A')\n''')
    if 'Chain-B' in objects:
        x2 = cmd.index('Chain-B')
        n2 = len(x2)
        if(n2 < 1):
            cmd.delete('Chain-B')
            if script=='1':
                f.write('''cmd.delete('Chain-B')\n''')
    if 'Chain-C' in objects:
        x3 = cmd.index('Chain-C')
        n3 = len(x3)
        if(n3 < 1):
            cmd.delete('Chain-C')
            if script=='1':
                f.write('''cmd.delete('Chain-C')\n''')
    if 'Chain-D' in objects:
        x4 = cmd.index('Chain-D')
        n4  = len(x4)
        if(n4 < 1):
            cmd.delete('Chain-D')
            if script=='1':
                f.write('''cmd.delete('Chain-D')\n''')
    if 'Chain-E' in objects:
        x5 = cmd.index('Chain-E')
        n5 = len(x5)
        if(n5 < 1):
            cmd.delete('Chain-E')
            if script=='1':
                f.write('''cmd.delete('Chain-E')\n''')
    if 'Chain-F' in objects:
        x6 = cmd.index('Chain-F')
        n6 = len(x6)
        if(n6 < 1):
            cmd.delete('Chain-F')
            if script=='1':
                f.write('''cmd.delete('Chain-F')\n''')
    if 'Chain-G' in objects:
        x7 = cmd.index('Chain-G')
        n7  = len(x7)
        if(n7 < 1):
            cmd.delete('Chain-G')
            if script=='1':
                f.write('''cmd.delete('Chain-G')\n''')
    if 'Chain-H' in objects:
        x8 = cmd.index('Chain-H')
        n8 = len(x8)
        if(n8 < 1):
            cmd.delete('Chain-H')
            if script=='1':
                f.write('''cmd.delete('Chain-H')\n''')
    if 'Chain-I' in objects:
        x9 = cmd.index('Chain-I')
        n9 = len(x9)
        if(n9 < 1):
            cmd.delete('Chain-I')
            if script=='1':
                f.write('''cmd.delete('Chain-I')\n''')
    if 'Chain-J' in objects:
        x10 = cmd.index('Chain-J')
        n10  = len(x10)
        if(n10 < 1):
            cmd.delete('Chain-J')
            if script=='1':
                f.write('''cmd.delete('Chain-J')\n''')
    if 'Chain-K' in objects:
        x11 = cmd.index('Chain-K')
        n11 = len(x11)
        if(n11 < 1):
            cmd.delete('Chain-K')
            if script=='1':
                f.write('''cmd.delete('Chain-K')\n''')
    if 'Chain-L' in objects:
        x12 = cmd.index('Chain-L')
        n12 = len(x12)
        if(n12 < 1):
            cmd.delete('Chain-L')
            if script=='1':
                f.write('''cmd.delete('Chain-L')\n''')
    if 'Chain-M' in objects:
        x13 = cmd.index('Chain-M')
        n13  = len(x13)
        if(n13 < 1):
            cmd.delete('Chain-M')
            if script=='1':
                f.write('''cmd.delete('Chain-M')\n''')
    if 'Chain-N' in objects:
        x14 = cmd.index('Chain-N')
        n14 = len(x14)
        if(n14 < 1):
            cmd.delete('Chain-N')
            if script=='1':
                f.write('''cmd.delete('Chain-N')\n''')
    if 'Chain-O' in objects:
        x15 = cmd.index('Chain-O')
        n15 = len(x15)
        if(n15 < 1):
            cmd.delete('Chain-O')
            if script=='1':
                f.write('''cmd.delete('Chain-O')\n''')
    if 'Chain-P' in objects:
        x16 = cmd.index('Chain-P')
        n16  = len(x16)
        if(n16 < 1):
            cmd.delete('Chain-P')
            if script=='1':
                f.write('''cmd.delete('Chain-P')\n''')
    if 'Chain-Q' in objects:
        x17 = cmd.index('Chain-Q')
        n17 = len(x17)
        if(n17 < 1):
            cmd.delete('Chain-Q')
            if script=='1':
                f.write('''cmd.delete('Chain-Q')\n''')
    if 'Chain-R' in objects:
        x18 = cmd.index('Chain-R')
        n18 = len(x18)
        if(n18 < 1):
            cmd.delete('Chain-R')
            if script=='1':
                f.write('''cmd.delete('Chain-R')\n''')
    if 'Chain-S' in objects:
        x19 = cmd.index('Chain-S')
        n19  = len(x19)
        if(n19 < 1):
            cmd.delete('Chain-S')
            if script=='1':
                f.write('''cmd.delete('Chain-S')\n''')
    if 'Chain-T' in objects:
        x20 = cmd.index('Chain-T')
        n20 = len(x20)
        if(n20 < 1):
            cmd.delete('Chain-T')
            if script=='1':
                f.write('''cmd.delete('Chain-T')\n''')
    if 'Chain-U' in objects:
        x21 = cmd.index('Chain-U')
        n21 = len(x21)
        if(n21 < 1):
            cmd.delete('Chain-U')
            if script=='1':
                f.write('''cmd.delete('Chain-U')\n''')
    if 'Chain-V' in objects:
        x22 = cmd.index('Chain-V')
        n22 = len(x22)
        if(n22 < 1):
            cmd.delete('Chain-V')
            if script=='1':
                f.write('''cmd.delete('Chain-V')\n''')
    if 'Chain-W' in objects:
        x23 = cmd.index('Chain-W')
        n23 = len(x23)
        if(n23 < 1):
            cmd.delete('Chain-W')
            if script=='1':
                f.write('''cmd.delete('Chain-W')\n''')
    if 'Chain-X' in objects:
        x24 = cmd.index('Chain-X')
        n24 = len(x24)
        if(n24 < 1):
            cmd.delete('Chain-X')
            if script=='1':
                f.write('''cmd.delete('Chain-X')\n''')
    if 'Chain-Y' in objects:
        x25 = cmd.index('Chain-Y')
        n25 = len(x25)
        if(n25 < 1):
            cmd.delete('Chain-Y')
            if script=='1':
                f.write('''cmd.delete('Chain-Y')\n''')
    if 'Chain-Z' in objects:
        x26 = cmd.index('Chain-Z')
        n26 = len(x26)
        if(n26 < 1):
            cmd.delete('Chain-Z')
            if script=='1':
                f.write('''cmd.delete('Chain-Z')\n''')
    if 'Chain-' '' in objects:
        x26 = cmd.index('Chain-' '')
        n26 = len(x26)
        if(n26 < 1):
            cmd.delete('Chain-' '')
            if script=='1':
                f.write('''cmd.delete('Chain-' '')\n''')
cmd.extend('checkforchain',checkforchain)

def deletemotif():

    cmd.delete('p-loop')
    cmd.delete('serineprotease')
    cmd.delete('lactamase')
    cmd.delete('superoxide')
    cmd.delete('metalloprotease')
    cmd.delete('tyrophos')
    cmd.delete('carbonicanhydrase')
    cmd.delete('paplike')
    cmd.delete('Zinc_finger')
    cmd.delete('Aminotransferase')
    cmd.delete('fucoseisomerase')
    cmd.delete('Ligase')
    cmd.delete('o-glycosyl')
    cmd.delete('glu_amidotransferase')
    cmd.delete('Peroxidase')
    cmd.delete('carboncarbon')
    cmd.delete('Tkinase')
    cmd.delete('TrioseIsomerase')
    cmd.delete('alcoholdehyd')
    cmd.delete('Cis-trans')
    cmd.delete('aldoreductase')
    cmd.delete('NAD-reductase')
    cmd.delete('NAD-reductase2')
    cmd.delete('chondroitinase')
    cmd.delete('Hyaluronate_Lyase')
    cmd.delete('deacetylase')
    cmd.delete('p-loop')
    cmd.delete('adenylatekinase')
    cmd.delete('SRC-Kinase')
    cmd.delete('Cyclin_Kinase')
    cmd.delete('Serotonin_transferase')
    cmd.delete('actase')
    cmd.delete('Exonuclease3')
    cmd.delete('Citrate_Synth')
    cmd.delete('hhal')
    cmd.delete('betaine_dehydrogenase')
cmd.extend('deletemotif',deletemotif)

def checkitforthese():
    objects = cmd.get_names('all')
    if 'ligands' in objects:
        xa = cmd.index('ligands')
        na  = len(xa)
        if(na < 1):
            cmd.delete('ligands')
            if script=='1':
                f.write('''cmd.delete('ligands')\n''')
    if 'nucleic_acid' in objects:
        xb = cmd.index('nucleic_acid')
        nb = len(xb)
        if(nb < 1):
            cmd.delete('nucleic_acid')
            if script=='1':
                f.write('''cmd.delete('nucleic_acid')\n''')
    if 'protein' in objects:
        xc = cmd.index('protein')
        nc = len(xc)
        if(nc < 1):
            cmd.delete('protein')
            if script=='1':
                f.write('''cmd.delete('protein')\n''')

    if 'hydrophilic' in objects:
        xd = cmd.index('hydrophilic')
        nd = len(xd)
        if(nd < 1):
            cmd.delete('hydrophilic')

    if 'hydrophobic' in objects:
        xe = cmd.index('hydrophobic')
        ne = len(xe)
        if(ne < 1):
            cmd.delete('hydrophobic')
            if script=='1':
                f.write('''cmd.delete('hydrophobic')\n''')

    if 'acidic' in objects:
        xe = cmd.index('acidic')
        ne = len(xe)
        if(ne < 1):
            cmd.delete('acidic')
            if script=='1':
                f.write('''cmd.delete('acidic')\n''')

    if 'basic' in objects:
        xg = cmd.index('basic')
        ng = len(xg)
        if(ng < 1):
            cmd.delete('basic')
            if script=='1':
                f.write('''cmd.delete('basic')\n''')

    if 'heme' in objects:
        xh = cmd.index('heme')
        nh = len(xh)
        if(nh < 1):
            cmd.delete('heme')
            if script=='1':
                f.write('''cmd.delete('heme')\n''')
cmd.extend('checkitforthese',checkitforthese)


    #------------Had to make cpk definitions for all selections made
    #-----------because couldn't get it to work on self.mot or original cpk+str

def cpkprotein():
  objects = cmd.get_names('all')
  if 'protein' in objects:
    cmd.color("oxygen","(elem O and protein)")
    cmd.color("nitrogen","(elem N and protein)")
    cmd.color("sulfur","(elem S and protein)")
    cmd.color("hydrogen","(elem H and protein)")
    cmd.color("gray","(elem C and protein)")
    if script=='1':
      f.write('''cmd.color("oxygen","(elem O and protein)")
cmd.color("nitrogen","(elem N and protein)")
cmd.color("sulfur","(elem S and protein)")
cmd.color("hydrogen","(elem H and protein)")
cmd.color("gray","(elem C and protein)")\n''')

def cpknucleic():
  objects = cmd.get_names('all')
  if 'nucleic_acid' in objects:
    cmd.color("oxygen","(elem O and nucleic_acid)")
    cmd.color("nitrogen","(elem N and nucleic_acid)")
    cmd.color("sulfur","(elem S and nucleic_acid)")
    cmd.color("hydrogen","(elem H and nucleic_acid)")
    cmd.color("gray","(elem C and nucleic_acid)")
    if script=='1':
      f.write('''cmd.color("oxygen","(elem O and nucleic_acid)")
cmd.color("nitrogen","(elem N and nucleic_acid)")
cmd.color("sulfur","(elem S and nucleic_acid)")
cmd.color("hydrogen","(elem H and nucleic_acid)")
cmd.color("gray","(elem C and nucleic_acid)")\n''')

def cpkligands():
  objects = cmd.get_names('all')
  if 'ligands' in objects:
    cmd.color("oxygen","(elem O and ligands)")
    cmd.color("nitrogen","(elem N and ligands)")
    cmd.color("sulfur","(elem S and ligands)")
    cmd.color("hydrogen","(elem H and ligands)")
    cmd.color("gray","(elem C and ligands)")
    if script=='1':
      f.write('''cmd.color("oxygen","(elem O and ligands)")
cmd.color("nitrogen","(elem N and ligands)")
cmd.color("sulfur","(elem S and ligands)")
cmd.color("hydrogen","(elem H and ligands)")
cmd.color("gray","(elem C and ligands)")\n''')

def cpkduh():
   objects = cmd.get_names('all')
   if 'duh' in objects:
       cmd.color("oxygen","(elem O and duh)")
       cmd.color("nitrogen","(elem N and duh)")
       cmd.color("sulfur","(elem S and duh)")
       cmd.color("hydrogen","(elem H and duh)")
       cmd.color("white","(elem C and duh)")

def cpkinteraction():
  objects = cmd.get_names('all')
  if 'interaction' in objects:
    cmd.color("oxygen","(elem O and interaction)")
    cmd.color("nitrogen","(elem N and interaction)")
    cmd.color("sulfur","(elem S and interaction)")
    cmd.color("hydrogen","(elem H and interaction)")
    cmd.color("gray","(elem C and interaction)")
    if script=='1':
      f.write('''cmd.color("oxygen","(elem O and interaction)")
cmd.color("nitrogen","(elem N and interaction)")
cmd.color("sulfur","(elem S and interaction)")
cmd.color("hydrogen","(elem H and interaction)")
cmd.color("gray","(elem C and interaction)")\n''')

def cpkserineprotease():
   objects = cmd.get_names('all')
   if 'serineprotease' in objects:
       cmd.color("oxygen","(elem O and serineprotease)")
       cmd.color("nitrogen","(elem N and serineprotease)")
       cmd.color("sulfur","(elem S and serineprotease)")
       cmd.color("hydrogen","(elem H and serineprotease)")
       cmd.color("white","(elem C and serineprotease)")

def cpkBlactamase():
 objects = cmd.get_names('all')
 if 'lactamase' in objects:
     cmd.color("oxygen","(elem O and lactamase)")
     cmd.color("nitrogen","(elem N and lactamase)")
     cmd.color("sulfur","(elem S and lactamase)")
     cmd.color("hydrogen","(elem H and lactamase)")
     cmd.color("white","(elem C and lactamase)")

def cpkmotif():
 objects = cmd.get_names('all')
 if 'motif' in objects:
     cmd.color("oxygen","(elem O and motif)")
     cmd.color("nitrogen","(elem N and motif)")
     cmd.color("sulfur","(elem S and motif)")
     cmd.color("hydrogen","(elem H and motif)")
     cmd.color("white","(elem C and motif)")

def cpkmetalloprotease():
 objects = cmd.get_names('all')
 if 'metalloprotease' in objects:
     cmd.color("oxygen","(elem O and metalloprotease)")
     cmd.color("nitrogen","(elem N and metalloprotease)")
     cmd.color("sulfur","(elem S and metalloprotease)")
     cmd.color("hydrogen","(elem H and metalloprotease)")
     cmd.color("white","(elem C and metalloprotease)")

def cpktyrophos():
 objects = cmd.get_names('all')
 if 'tyrophos' in objects:
     cmd.color("oxygen","(elem O and tyrophos)")
     cmd.color("nitrogen","(elem N and tyrophos)")
     cmd.color("sulfur","(elem S and tyrophos)")
     cmd.color("hydrogen","(elem H and tyrophos)")
     cmd.color("white","(elem C and tyrophos)")


def cpkreductase():
 objects = cmd.get_names('all')
 if 'superoxide' in objects:
     cmd.color("oxygen","(elem O and superoxide)")
     cmd.color("nitrogen","(elem N and superoxide)")
     cmd.color("sulfur","(elem S and superoxide)")
     cmd.color("hydrogen","(elem H and superoxide)")
     cmd.color("white","(elem C and superoxide)")

def cpkcarbanhyd():
 objects = cmd.get_names('all')
 if 'carbonicanhydrase' in objects:
     cmd.color("oxygen","(elem O and carbonicanhydrase)")
     cmd.color("nitrogen","(elem N and carbonicanhydrase)")
     cmd.color("sulfur","(elem S and carbonicanhydrase)")
     cmd.color("hydrogen","(elem H and carbonicanhydrase)")
     cmd.color("white","(elem C and carbonicanhydrase)")

def cpkpaplike():
 objects = cmd.get_names('all')
 if 'paplike' in objects:
     cmd.color("oxygen","(elem O and paplike)")
     cmd.color("nitrogen","(elem N and paplike)")
     cmd.color("sulfur","(elem S and paplike)")
     cmd.color("hydrogen","(elem H and paplike)")
     cmd.color("white","(elem C and paplike)")


def cpkzincfinger():
 objects = cmd.get_names('all')
 if 'Zinc_finger' in objects:
     cmd.color("oxygen","(elem O and Zinc_finger)")
     cmd.color("nitrogen","(elem N and Zinc_finger)")
     cmd.color("sulfur","(elem S and Zinc_finger)")
     cmd.color("hydrogen","(elem H and Zinc_finger)")
     cmd.color("white","(elem C and Zinc_finger)")


def cpkaminotransferase():
 objects = cmd.get_names('all')
 if 'Aminotransferase' in objects:
     cmd.color("oxygen","(elem O and Aminotransferase)")
     cmd.color("nitrogen","(elem N and Aminotransferase)")
     cmd.color("sulfur","(elem S and Aminotransferase)")
     cmd.color("hydrogen","(elem H and Aminotransferase)")
     cmd.color("white","(elem C and Aminotransferase)")


def cpkfucoseisomerase():
 objects = cmd.get_names('all')
 if 'fucoseisomerase' in objects:
     cmd.color("oxygen","(elem O and fucoseisomerase)")
     cmd.color("nitrogen","(elem N and fucoseisomerase)")
     cmd.color("sulfur","(elem S and fucoseisomerase)")
     cmd.color("hydrogen","(elem H and fucoseisomerase)")
     cmd.color("white","(elem C and fucoseisomerase)")
     cmd.color('purpleblue', 'elem mn')


def cpkglu_amidotransferase():
 objects = cmd.get_names('all')
 if 'glu_amidotransferase' in objects:
     cmd.color("oxygen","(elem O and glu_amidotransferase)")
     cmd.color("nitrogen","(elem N and glu_amidotransferase)")
     cmd.color("sulfur","(elem S and glu_amidotransferase)")
     cmd.color("hydrogen","(elem H and glu_amidotransferase)")
     cmd.color("white","(elem C and glu_amidotransferase)")


def cpkdnaligase():
  objects = cmd.get_names('all')
  if 'Ligase' in objects:
     cmd.color("oxygen","(elem O and Ligase)")
     cmd.color("nitrogen","(elem N and Ligase)")
     cmd.color("sulfur","(elem S and Ligase)")
     cmd.color("hydrogen","(elem H and Ligase)")
     cmd.color("white","(elem C and Ligase)")

def cpkoglycosyl():
  objects = cmd.get_names('all')
  if 'o-glycosyl' in objects:
     cmd.color("oxygen","(elem O and o-glycosyl)")
     cmd.color("nitrogen","(elem N and o-glycosyl)")
     cmd.color("sulfur","(elem S and o-glycosyl)")
     cmd.color("hydrogen","(elem H and o-glycosyl)")
     cmd.color("white","(elem C and o-glycosyl)")

def cpkcarboncarbon():
  objects = cmd.get_names('all')
  if 'carboncarbon' in objects:
     cmd.color("oxygen","(elem O and carboncarbon)")
     cmd.color("nitrogen","(elem N and carboncarbon)")
     cmd.color("sulfur","(elem S and carboncarbon)")
     cmd.color("hydrogen","(elem H and carboncarbon)")
     cmd.color("white","(elem C and carboncarbon)")

def cpkkinase():
  objects = cmd.get_names('all')
  if 'Tkinase' in objects:
     cmd.color("oxygen","(elem O and Tkinase)")
     cmd.color("nitrogen","(elem N and Tkinase)")
     cmd.color("sulfur","(elem S and Tkinase)")
     cmd.color("hydrogen","(elem H and Tkinase)")
     cmd.color("white","(elem C and Tkinase)")

def cpkperoxidase():
  objects = cmd.get_names('all')
  if 'Peroxidase' in objects:
     cmd.color("oxygen","(elem O and Peroxidase)")
     cmd.color("nitrogen","(elem N and Peroxidase)")
     cmd.color("sulfur","(elem S and Peroxidase)")
     cmd.color("hydrogen","(elem H and Peroxidase)")
     cmd.color("white","(elem C and Peroxidase)")

def cpktriose():
  objects = cmd.get_names('all')
  if 'TrioseIsomerase' in objects:
     cmd.color("oxygen","(elem O and TrioseIsomerase)")
     cmd.color("nitrogen","(elem N and TrioseIsomerase)")
     cmd.color("sulfur","(elem S and TrioseIsomerase)")
     cmd.color("hydrogen","(elem H and TrioseIsomerase)")
     cmd.color("white","(elem C and TrioseIsomerase)")


def cpkalcoholdehyd():
  objects = cmd.get_names('all')
  if 'alcoholdehyd' in objects:
     cmd.color("oxygen","(elem O and alcoholdehyd)")
     cmd.color("nitrogen","(elem N and alcoholdehyd)")
     cmd.color("sulfur","(elem S and alcoholdehyd)")
     cmd.color("hydrogen","(elem H and alcoholdehyd)")
     cmd.color("white","(elem C and alcoholdehyd)")

def cpkaldoreductase():
  objects = cmd.get_names('all')
  if 'aldoreductase' in objects:
     cmd.color("oxygen","(elem O and aldoreductase)")
     cmd.color("nitrogen","(elem N and aldoreductase)")
     cmd.color("sulfur","(elem S and aldoreductase)")
     cmd.color("hydrogen","(elem H and aldoreductase)")
     cmd.color("white","(elem C and aldoreductase)")


def cpkcistrans():
   objects = cmd.get_names('all')
   if 'Cis-trans' in objects:
       cmd.color("oxygen","(elem O and Cis-trans)")
       cmd.color("nitrogen","(elem N and Cis-trans)")
       cmd.color("sulfur","(elem S and Cis-trans)")
       cmd.color("hydrogen","(elem H and Cis-trans)")
       cmd.color("white","(elem C and Cis-trans)")

def cpksubstrate():
   objects = cmd.get_names('all')
   if 'substrate' in objects:
       util.cnc('substrate')
       cmd.color("oxygen","(elem O and substrate)")
       cmd.color("nitrogen","(elem N and substrate)")
       cmd.color("sulfur","(elem S and substrate)")
       cmd.color("hydrogen","(elem H and substrate)")
       cmd.color("gray","(elem C and substrate)")

def cpknadreductase():
   objects = cmd.get_names('all')
   if 'NAD-reductase' in objects:
       cmd.color("oxygen","(elem O and NAD-reductase)")
       cmd.color("nitrogen","(elem N and NAD-reductase)")
       cmd.color("sulfur","(elem S and NAD-reductase)")
       cmd.color("hydrogen","(elem H and NAD-reductase)")
       cmd.color("white","(elem C and NAD-reductase)")

def cpknadreductase2():
   objects = cmd.get_names('all')
   if 'NAD-reductase2' in objects:
       cmd.color("oxygen","(elem O and NAD-reductase2)")
       cmd.color("nitrogen","(elem N and NAD-reductase2)")
       cmd.color("sulfur","(elem S and NAD-reductase2)")
       cmd.color("hydrogen","(elem H and NAD-reductase2)")
       cmd.color("white","(elem C and NAD-reductase2)")

def cpkdeacetylase():
   objects = cmd.get_names('all')
   if 'deacetylase' in objects:
       cmd.color("oxygen","(elem O and deacetylase)")
       cmd.color("nitrogen","(elem N and deacetylase)")
       cmd.color("sulfur","(elem S and deacetylase)")
       cmd.color("hydrogen","(elem H and deacetylase)")
       cmd.color("white","(elem C and deacetylase)")

def cpkchondro():
   objects = cmd.get_names('all')
   if 'chondroitinase' in objects:
       cmd.color("oxygen","(elem O and chondroitinase)")
       cmd.color("nitrogen","(elem N and chondroitinase)")
       cmd.color("sulfur","(elem S and chondroitinase)")
       cmd.color("hydrogen","(elem H and chondroitinase)")
       cmd.color("white","(elem C and chondroitinase)")

def cpkhyaluron():
 objects = cmd.get_names('all')
 if 'Hyaluronate_Lyase' in objects:
     cmd.color("oxygen","(elem O and Hyaluronate_Lyase)")
     cmd.color("nitrogen","(elem N and Hyaluronate_Lyase)")
     cmd.color("sulfur","(elem S and Hyaluronate_Lyase)")
     cmd.color("hydrogen","(elem H and Hyaluronate_Lyase)")
     cmd.color("white","(elem C and Hyaluronate_Lyase)")

def cpkactase():
   objects = cmd.get_names('all')
   if 'actase' in objects:
       cmd.color("oxygen","(elem O and actase)")
       cmd.color("nitrogen","(elem N and actase)")
       cmd.color("sulfur","(elem S and actase)")
       cmd.color("hydrogen","(elem H and actase)")
       cmd.color("white","(elem C and actase)")

def cpkadenylatekinase():
   objects = cmd.get_names('all')
   if 'adenylatekinase' in objects:
       cmd.color("oxygen","(elem O and adenylatekinase)")
       cmd.color("nitrogen","(elem N and adenylatekinase)")
       cmd.color("sulfur","(elem S and adenylatekinase)")
       cmd.color("hydrogen","(elem H and adenylatekinase)")
       cmd.color("white","(elem C and adenylatekinase)")

def cpknuclease():
   objects = cmd.get_names('all')
   if 'Exonuclease3' in objects:
       cmd.color("oxygen","(elem O and Exonuclease3)")
       cmd.color("nitrogen","(elem N and Exonuclease3)")
       cmd.color("sulfur","(elem S and Exonuclease3)")
       cmd.color("hydrogen","(elem H and Exonuclease3)")
       cmd.color("white","(elem C and Exonuclease3)")

def cpkcitrate():
   objects = cmd.get_names('all')
   if 'Citrate_Synth' in objects:
       cmd.color("oxygen","(elem O and Citrate_Synth)")
       cmd.color("nitrogen","(elem N and Citrate_Synth)")
       cmd.color("sulfur","(elem S and Citrate_Synth)")
       cmd.color("hydrogen","(elem H and Citrate_Synth)")
       cmd.color("white","(elem C and Citrate_Synth)")

def cpktyrokinase():
   objects = cmd.get_names('all')
   if 'SRC-Kinase' in objects:
       cmd.color("oxygen","(elem O and SRC-Kinase)")
       cmd.color("nitrogen","(elem N and SRC-Kinase)")
       cmd.color("sulfur","(elem S and SRC-Kinase)")
       cmd.color("hydrogen","(elem H and SRC-Kinase)")
       cmd.color("white","(elem C and SRC-Kinase)")

def cpkhhal():
   objects = cmd.get_names('all')
   if 'hhal' in objects:
       cmd.color("oxygen","(elem O and hhal)")
       cmd.color("nitrogen","(elem N and hhal)")
       cmd.color("sulfur","(elem S and hhal)")
       cmd.color("hydrogen","(elem H and hhal)")
       cmd.color("white","(elem C and hhal)")

def cpkbetaine():
   objects = cmd.get_names('all')
   if 'betaine_dehydrogenase' in objects:
       cmd.color("oxygen","(elem O and betaine_dehydrogenase)")
       cmd.color("nitrogen","(elem N and betaine_dehydrogenase)")
       cmd.color("sulfur","(elem S and betaine_dehydrogenase)")
       cmd.color("hydrogen","(elem H and betaine_dehydrogenase)")
       cmd.color("white","(elem C and betaine_dehydrogenase)")

def cpkseracetyl():
      objects = cmd.get_names('all')
      if 'Serotonin_transferase' in objects:
         cmd.color("oxygen","(elem O and Serotonin_transferase)")
         cmd.color("nitrogen","(elem N and Serotonin_transferase)")
         cmd.color("sulfur","(elem S and Serotonin_transferase)")
         cmd.color("hydrogen","(elem H and Serotonin_transferase)")
         cmd.color("white","(elem C and Serotonin_transferase)")

def cpkcyclinkinase():
   objects = cmd.get_names('all')
   if 'Cyclin_Kinase' in objects:
       cmd.color("oxygen","(elem O and Cyclin_Kinase)")
       cmd.color("nitrogen","(elem N and Cyclin_Kinase)")
       cmd.color("sulfur","(elem S and Cyclin_Kinase)")
       cmd.color("hydrogen","(elem H and Cyclin_Kinase)")
       cmd.color("white","(elem C and Cyclin_Kinase)")

def color_by_chain():
    set_defaults()
    checkitforthese()
    delcrea()
    cmd.hide('all')
    cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
    cmd.show('sticks','resn a+g+c+t+u')
    cmd.set('sphere_scale','0.4','resn u')   
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
    if script=='1':
        f.write('''cmd.hide('all')
cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
cmd.show('sticks','resn a+g+c+t+u')
cmd.set('sphere_scale','0.4','resn u')   
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
cmd.color("aquamarine","chain Z")\n''')

def color_cpk(str):
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
  if script=='1':
    f.write('''cmd.color("carbgray", "(elem C)" + str )
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
cmd.color("helpink", "elem He" + str)\n''')
