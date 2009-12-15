from pymol import selector, util, cmd, movie
from cmd import *
from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename
from tkColorChooser import askcolor
from tkSimpleDialog import askstring
from tkMessageBox import *
import Pmw
import re
import os
import urllib
import urllib2
import StringIO
import gzip
import time
import types
import random
import linecache

global PYMOL_PATH
global PROMOL_PATH
global Photos
global script
global AminoMenuList
global AminoList
global AlphaSequence
global alphaSequence

try:
	PYMOL_PATH=os.environ['PYMOL_PATH']
except KeyError:
	PYMOL_PATH='./'
PROMOL_PATH="%smodules/pmg_tk/startup/"%(PYMOL_PATH)

Pmw.initialise()

#Amino Acid Abbre List for Menus
AminoMenuList = ('','ala','arg','asn','asp','cys','gln','glu','gly','his','ile','leu','lys','met','phe','pro','ser','thr','trp','tyr','val')
#Amino Acid Array for validation
AminoList = ('ala','arg','asn','asp','cys','gln','glu','gly','his','ile','leu','lys','met','phe','pro','ser','thr','trp','tyr','val')

for x in AminoList:
	for y in ('3D','2D'):
		Photos["%s%s"%(x,y)] = PhotoImage(file="%sAminoPics/%s%s.gif"%(PROMOL_PATH,x,y))

#A - Z
AlphaSequence = [ "%c"%(x) for x in range(ord('A'), ord('Z')+1)]
#a - z
alphaSequence = [ "%c"%(x) for x in range(ord('a'), ord('z')+1)]


def ProMol(pymol,userClick):
	ProMol = PGUI(pymol,userClick)

def __init__(self):
	self.menuBar.addmenuitem('Plugin', 'command',
							 'Easy GUI',
							 label = 'ProMOL 3.03',
							 command = lambda s=self : ProMol(s,1))
	ProMol(self,0)

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
	
		selections={'dna':'resn a+g+c+t+u',
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
			self.results.appendtext('Error:	Chime command not recognized.\n\n')
	
	self.cmdLine.clear()
	#self.cmdLine.focus_force()
	#-----------------------------------------#
	#		Chime Conversion Methods		 #
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
		 		pymSelect = 'PyMOL: select '+selections[self.args[1]]+'\n\n'
		 		self.results.appendtext(pymSelect)
		 		cmd.select(selections[self.args[1]])
			else:
		 		self.results.appendtext('Usage: select [selection]')
		except:
			showinfo('Error', 'That is not a supported command')
	
	# 'individual command' conversions
	def convert_individual(self):
		pymShow = 'PyMOL: '+self.individuals[self.command]+'\n\n'
		cmd.do(self.individuals[self.command])
		self.results.appendtext(pymShow)

'''
	PGUI CLASS
	The look and feel of the Gui.
'''
class PGUI:
	
	
	script = 0
	def show_dna_rna(*args):
		
		points = 0
		delcrea()
		try:
			self = args[0]
			update()
		except:
			pass
		objects = cmd.get_names('all')
		checkitforthese()
		try:
			cmd.set('cartoon_ring_mode' ,'1')
			if 'nucleic_acid' in objects:
				set_defaults()
				if 'protein' in objects:
					cmd.show('cartoon','protein')
					cmd.color('gray60','protein')
				if 'ligands' in objects:
					cmd.show('spheres','ligands')
					cmd.set('sphere_transparency','0.4','ligands')
					cmd.set('sphere_scale','0.4','ligands')
					cmd.color('orange', 'ligands')
				if 'nucleic_acid' in objects:
					cmd.show('cartoon', 'nucleic_acid')
					cmd.color('lightblue','resn a')
					cmd.color('orange','resn c')
					cmd.color('salmon','resn g')
					cmd.color('palegreen','resn t')
					cmd.color('paleyellow', 'resn u')
					points = points + 3
			if points == 3:
				showinfo('Nucleic Acid Key','Adenine = light blue\nCytosine = orange\nGuanine = salmon red\nThymine = light green\nUracil = light yellow')
			else:
				showinfo("Error", "There is no DNA or RNA in this molecule.")
		except:
			if 'nucleic_acid' in objects:
				set_defaults()
				if 'protein' in objects:
					cmd.show('cartoon','protein')
					cmd.color('gray60','protein')
				if 'ligands' in objects:
					cmd.show('spheres','ligands')
					cmd.set('sphere_transparency','0.4','ligands')
					cmd.set('sphere_scale','0.4','ligands')
					cmd.color('orange', 'ligands')
				if 'nucleic_acid' in objects:
					cmd.show('cartoon', 'nucleic_acid')
					cmd.color('lightblue','resn a')
					cmd.color('orange','resn c')
					cmd.color('salmon','resn g')
					cmd.color('palegreen','resn t')
					cmd.color('paleyellow', 'resn u')
					points = points + 3
			if points == 3:
				showinfo('Nucleic Acid Key','Adenine = light blue\nCytosine = orange\nGuanine = salmon red\nThymine = light green\nUracil = light yellow')
			else:
				showinfo("Error", "There is no DNA or RNA in this molecule.")
	cmd.extend('show_dna_rna',show_dna_rna)
	
	
	# default view
	def std_view(self):
		try:
			update()
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
			cpkligands()
			cmd.show('cartoon', 'resn a+t+g+c+u')
			cmd.color('limegreen','resn a+t+g+c+u')
		except:
			update()
			checkitforthese()
			set_defaults()
			delcrea()
			self.populate()
			cmd.show('cartoon','resn GLY+PRO+ALA+VAL+LEU+ILE+MET+CYS+PHE+TYR+TRP+HIS+LYS+ARG+GLN+ASN+GLU+ASP+SER+THR')
			cmd.color("red", "ss h")
			cmd.color("yellow", "ss s")
			cmd.color("cyan", "ss l+\'\'")
			cmd.show('spheres','het')
			cpkligands()
			cmd.show('cartoon', 'resn a+t+g+c+u')
			cmd.color('limegreen','resn a+t+g+c+u')
	
	# show hetero atoms
	def show_hetero(*args):
		try:
			self = args[0]
		except:
			pass
		try:
			
			delcrea()
			cmd.remove('resn HOH')
				update()
				objects = cmd.get_names('all')
				checkitforthese()
			if 'ligands' in objects:
				set_defaults()
			if 'protein' in objects:
				cmd.show('cartoon', 'protein')
				cmd.set('cartoon_transparency','0.7','protein')
			if 'nucleic_acid' in objects:
				cmd.set('cartoon_ring_mode', '1')
				cmd.show('cartoon','nucleic_acid')
				cmd.set('cartoon_transparency','0.7','nucleic_acid')
				cmd.color('cyan', 'nucleic_acid')
				cmd.show('spheres','ligands')
				cmd.set('sphere_transparency','0.1','ligands')
				cmd.show("sticks", "ligands around 6'")
				cmd.set('stick_radius','0.3','ligands around 6')
				cmd.color('orange','ligands')
				cmd.select("interaction","ligands around 6'")
				cpkinteraction()
				cmd.set('stick_transparency', '0.1', 'interaction')
				cmd.disable('interaction')
			else:
				showinfo("Error", "There are no hetero atoms in this molecule.")
		except:
			
			delcrea()
			cmd.remove('resn HOH')
			update()
			objects = cmd.get_names('all')
			checkitforthese()
			if 'ligands' in objects:
		 		set_defaults()
				if 'protein' in objects:
					cmd.show('cartoon', 'protein')
					cmd.set('cartoon_transparency','0.7','protein')
			if 'nucleic_acid' in objects:
				cmd.show('cartoon','nucleic_acid')
				cmd.set('cartoon_transparency','0.7','nucleic_acid')
				cmd.color('cyan', 'nucleic_acid')
			cmd.show('spheres','ligands')
			cmd.set('sphere_transparency','0.1','ligands')
			cmd.show("sticks", "ligands around 6'")
			cmd.set('stick_radius','0.3','ligands around 6')
			cmd.color('orange','ligands')
			cmd.select("interaction","ligands around 6'")
			cpkinteraction()
			cmd.set('stick_transparency', '0.1', 'interaction')
			cmd.disable('interaction')
		else:
			showinfo("Error", "There are no hetero atoms in this molecule.")
	cmd.extend('show_hetero',show_hetero)
	
	# ball and stick view
	def ball_and_stick(*args):
		try:
			self = args[0]
		except:
			pass
		update()
		objects = cmd.get_names('all')
		checkitforthese()
		set_defaults()
		delcrea()
		cmd.set("stick_radius","0.1","all")
		cmd.set("sphere_scale","0.3","all")
		if 'protein' in objects:
			cmd.show('spheres','protein')
			cmd.show('sticks','protein')
			cpkprotein()
		if 'nucleic_acid' in objects:
			try:
				cmd.set('cartoon_ring_mode', '1')
				cmd.show('cartoon','resn a+g+c+t+u')
				cmd.show('spheres','resn a+g+c+t+u')
				cmd.show('sticks','resn a+g+c+t+u')
				cpknucleic()
			except:
				cmd.show('cartoon','resn a+g+c+t+u')
				cpknucleic()
		if 'ligands' in objects:
			cmd.show('spheres','ligands')
			cmd.color('orange', 'ligands')
	cmd.extend('ball_and_stick',ball_and_stick)
	
	# show the surface of the molecule
	def surface_view(*args):
		delcrea()
		update()
		objects = cmd.get_names('all')
		checkitforthese()
		set_defaults()
		cmd.show('surface','all')
		cpkprotein()
	cmd.extend('surface_view',surface_view)
	
	
	# show the polarities of the molecule
	def view_polarity(*args):
		delcrea()
		update()
		checkitforthese()
		set_defaults()
		objects = cmd.get_names('all')
		if 'protein' in objects:
			cmd.show('surface', 'protein')
		cmd.color('red','resn ALA+ILE+LEU+MET+PHE+PRO+TRP+VAL')
		cmd.color('blue','resn THR+SER+ARG+ASN+ASP+GLN+GLU+HIS+LYS')
		cmd.show('spheres','het')
		cmd.color('green','het')
		try:
			cmd.set('cartoon_ring_mode' ,'1')
		except:
			cmd.color('green','het')
		cmd.show('cartoon','resn a+g+c+t+u')
		cpknucleic()
		
		showinfo('Info', 'Red = Hydrophobic\nBlue = Hydrophilic')
	
	cmd.extend('solubility', view_polarity)
	
	# putty representation
	def show_putty(*args):
		try:
			try:
				self = args[0]
				update()
			except:
				pass
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
			cpknucleic()
		except:
			showinfo('Error', 'Putty is not supported by this version of PyMol\nTry downloading the newest version to troubleshoot this problem')
	cmd.extend('putty',show_putty)
	
	# aromatics view
	def color_aromatics(*args):
		update()
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
		cmd.deselect()
	cmd.extend('color_aromatics',color_aromatics)
	
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
			update()
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
		if 'protein' in objects:
			showinfo('Charge Info', 'Blue = Positively charged Amino Acids\nRed = Negatively charged Amino Acids')
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
	cmd.extend('surf_over_toon',surf_toon)

	
	
	def surf_stick(*args):
		delcrea()
		update()
		checkitforthese()
		cmd.hide('everything')
		cmd.show('stick','all')
		cmd.select('surface', 'all')
		cmd.do('show surface, all')
		cmd.do('set transparency, 0.5, surface')
		cmd.delete('surface')
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
	cmd.extend('mesh_over_stick',mesh_stick)
	
	def stick_toon(*args):
		delcrea()
		cmd.hide('everything')
		cmd.show('lines')
		cmd.create('cartoon', 'all')
		cmd.show('cartoon', 'cartoon')
		cmd.color('salmon', 'cartoon')
		cmd.color('cyan', 'resn a+t+u+g+c')
	cmd.extend('stick_and_cartoon',stick_toon)
	
	
	def dot_line(*args):
		delcrea()
		cmd.set('dot_density', '3')
		cmd.hide('everything')
		cmd.remove('resn HOH')
		cmd.hide('everything')
		cmd.show('lines')
		cmd.show('dots', 'all')
	cmd.extend('dot_line',dot_line)
	
	def rovingstickers(*args):
		cmdRovStick = ' '
		
		try:
		cmdRovStick = float(args[0])
		except:
		pass
		try:
		self = args[0]
		except:
		print 'Usage: roving_stick # (# is value between 0 and 20)'
		
		update()
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
		cpkprotein()
		cpknucleic()
		cpkligands()
	cmd.extend('roving_stick',rovingstickers)
	
	def rovinglines(*args):
		cmdRovLine = ''
		print len(args)
		#This next construction looks strange, I know, but this way it executes
		#the default settings if the user does not specifiy range!
		#Don't Worry. I plan on fixing this.
		try:
		cmdRovLine = float(args[0])
		except:
		pass
		try:
		self = args[0]
		except:
		print 'Usage: roving_line # (# is value between 0 and 20)'
		
		update()
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
		cpkprotein()
		cpknucleic()
		cpkligands()
	cmd.extend('roving_line', rovinglines)
	
	def rovingballstick(*args):
		cmdRovBall = ''
		
		try:
		cmdRovBall = float(args[0])
		except:
		pass
		try:
		self = args[0]
		except:
		print 'Usage: roving_ballstick # (# is value between 0 and 20)'
		update()
		
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
		cpkprotein()
		cpknucleic()
		cpkligands()
	cmd.extend('roving_ballstick',rovingballstick)
	
	
	def rovingspheres(*args):
		cmdRovSphere = ''
		
		try:
		cmdRovSphere = float(args[0])
		except:
		pass
		try:
		self = args[0]
		except:
		print 'Usage: roving_sphere # (# is value between 0 and 20)'
		
		update()
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
		update()
		except:
		pass
		objects = cmd.get_names('all')
		checkitforthese()
		set_defaults()
		delcrea()
		cmd.set("sphere_scale","0.7","all")
		cmd.show('spheres','all')
		cpkprotein()#stopped here
		cpkligands()
		cpknucleic()
	cmd.extend('show_cpk',show_cpk)
	
	def spheresurf(*args):
		try:
		self = args[0]
		update()
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
		cpkprotein()
		cpknucleic()
		cpkligands()
	cmd.extend('surf_over_spheres',spheresurf)
		#-----------Electron Density Presets----------------#
	
	def mesh_ribbon(self):
		try:
			delcrea()
			try:
					cmd.hide('everything')
					cmd.isomesh('map1','map', contour1.get())
			
			except:
					try:
						cmd.set("suspend_updates",1,quiet=1)
						cmd.remove("hydro")
						cmd.map_new('map',"gaussian","0.75", 'all')
						cmd.set("suspend_updates",0,quiet=1)
						cmd.refresh()
						cmd.isomesh('map1','map', '1')
					
					except:		
						showinfo("Error", 'No PDB is present')
					cmd.show('ribbon', 'all')
			cmd.show('lines', 'all')
			cmd.color('red', 'all')
			cmd.color('purpleblue', 'map1')
		except:
			cmd.show('lines', 'all')
			showinfo('Alert', 'Protein must be present')
	cmd.extend('mesh_ribbon',mesh_ribbon)
	
	def dot_sticks(*args):
		 try:
			 delcrea()
			 cmd.hide('everything')
			 try:
				cmd.set("suspend_updates",1,quiet=1)
				cmd.remove("hydro")
				cmd.enable('all')
				cmd.map_new('map',"gaussian","0.75", 'all')
				cmd.isodot("map1", "map", 9999.0, 'all')
				cmd.set("suspend_updates",0,quiet=1)
				cmd.refresh()
				cmd.isodot('map1','map', '1')
			 except:
				
				showinfo("Error", 'No PDB is present')
			 
			 cmd.show('sticks', 'all')
			 cmd.color('blue', 'all')
			 cmd.color('red', 'map1')
		 except:
			cmd.show('lines', 'all')
			showinfo('Alert', 'Protein must be present')
	cmd.extend('dot_sticks',dot_sticks)
	
	def surfinglines(*args):
		
		try:
			cmd.hide('everything')
			update()
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
			except:
				cmd.show('lines', 'all')
				showinfo("Error", 'No PDB is present')
		except:
			cmd.show('lines', 'all')
			showinfo('Alert', 'Protein must be present')
	cmd.extend('surfinglines',surfinglines)

#------------------Motif stuff---------------------
	def deletemotif(self):
		deletemotif()


#----------Motif definitions consisting of measuring atom to atom between different
		#	amino acid residues and allowing them to be altered by a slider
		
	def motifCaller(self,motif,camera): pass
	
	def byResidue(self,selection,num):
		byres, delete = '', ''
		numbers = range(1,num)
		for number in numbers:
			if number == num:
				byres = str.join((byres,'byres ',selection,number))
				delete = str.join((delete,selection,number))
			else:
				byres = str.join((byres,'byres ',selection,number,' and '))
				delete = str.join((delete,selection,number,', '))
		cmd.do('select %s, %s'%(selection, byres))
		cmd.do('delete %s'%(delete))

	def delSelections(self,*selections):
		delete = ''
		i = 1
		selecLen = len(selections)
		for selection in selections:
			if i = selecLen:
				delete = str.join((delete,selection,number))
			else:
				delete = str.join((delete,selection,number,', '))
			i+=1
		cmd.do('delete %s'%(delete))

	def serineprotease(self,motifRange):
		update()#updates list of molecular groups
		checkitforthese()#sees if objects are in objects
		set_defaults()#sets defaults
		delcrea()#deletes created objects
		deletemotif()#deletes previous motif
		cmd.select('asp1', 'resn asp within %s of resn his'%(motifRange*3)) #selects aspartate within 3 of histidine
		cmd.select('asp2', 'resn asp within %s of resn ser'%(motifRange*7))
		cmd.select('asp', 'byres asp1 and byres asp2')
		cmd.select('his1', 'resn his within %s of asp'%(motifRange*4))
		cmd.select('his2', 'resn his within %s of resn ser'%(motifRange*4))
		cmd.select('his', 'byres his1 and byres his2')
		cmd.select('ser1', 'name og within %s of name ne2'%(motifRange*3.5))
		cmd.select('ser2', 'resn ser within %s of asp'%(motifRange*7))
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
	
	
	def Blactamase(self,motifRange):
		cmd.select('lys1', 'name nz and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('lys2', 'name nz and resn lys within %s of (name cz and resn tyr)'%(motifRange*5.5))
		cmd.select('lys3', 'name nz and resn lys within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('lys4', 'name nz and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6.5))
		cmd.select('lys5', 'name ce and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('lys6', 'name ce and resn lys within %s of (name cz and resn tyr)'%(motifRange*6))
		cmd.select('lys7', 'name nz and resn lys within %s of (name og and resn ser)'%(motifRange*6))
		cmd.select('lys8', 'name nz and resn lys within %s of (name cb and resn ser)'%(motifRange*5.2))
		cmd.select('lys9', 'name cb and resn lys within %s of (name cb and resn ser)'%(motifRange*9.2))
		cmd.select('lys10', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*11))
		cmd.select('lys11', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*11))
		cmd.select('lys12', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*12.5))
		cmd.select('lys13', 'name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*11))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13')
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys)'%(motifRange*5))
		cmd.select('tyr2', 'name cz and resn tyr within %s of (name nz and resn lys)'%(motifRange*5.5))
		cmd.select('tyr3', 'name ce1 and resn tyr within %s of (name nz and resn lys)'%(motifRange*6.5))
		cmd.select('tyr4', 'name ce2 and resn tyr within %s of (name nz and lys)'%(motifRange*6.5))
		cmd.select('tyr5', 'name oh and resn tyr within %s of (name ce and resn lys)'%(motifRange*5))
		cmd.select('tyr6', 'name cz and resn tyr within %s of (name ce and resn lys)'%(motifRange*6))
		cmd.select('tyr7', 'name oh and resn tyr within %s of (name og and resn ser)'%(motifRange*6))
		cmd.select('tyr8', 'name cz and resn tyr within %s of (name og and resn ser)'%(motifRange*6.5))
		cmd.select('tyr9', 'name oh and resn tyr within %s of (name cb and resn ser)'%(motifRange*6))
		cmd.select('tyr10', 'name oh and resn tyr within %s of (name oe1 and resn glu)'%(motifRange*10))
		cmd.select('tyr11', 'name oh and resn tyr within %s of (name oe2 and resn glu)'%(motifRange*10))
		cmd.select('tyr12', 'name oh and resn tyr within %s of (name cd and resn glu)'%(motifRange*10))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12')
		cmd.select('ser1', 'name cb and resn ser within %s of (name nz and resn lys)'%(motifRange*6))
		cmd.select('ser2', 'name og and resn ser within %s of (name nz and resn lys)'%(motifRange*6))
		cmd.select('ser3', 'name cb and resn ser within %s of (name cb and lys)'%(motifRange*8.2))
		cmd.select('ser4', 'name og and resn ser within %s of (name cz and resn tyr)'%(motifRange*6.5))
		cmd.select('ser5', 'name cb and resn ser within %s of (name oh and resn tyr)'%(motifRange*6.5))
		cmd.select('ser6', 'name og and resn ser within %s of (name oh and tyr)'%(motifRange*6))
		cmd.select('ser7', 'name og and resn ser within %s of (name oe1 and resn glu)'%(motifRange*12))
		cmd.select('ser8', 'name og and resn ser within %s of (name oe2 and resn glu)'%(motifRange*12))
		cmd.select('ser9', 'name cb and resn ser within %s of (name oe1 and resn glu)'%(motifRange*11))
		cmd.select('ser10', 'name cb and resn ser within %s of (name oe2 and resn glu)'%(motifRange*12.5))
		cmd.select('ser11', 'name og and resn ser within %s of (name cd and resn glu)'%(motifRange*12.5))
		cmd.select('ser12', 'name cb and resn ser within %s of (name cd and resn glu)'%(motifRange*11.5))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10 and byres ser11 and byres ser12')
		cmd.select('glu1', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*8.5))
		cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*9.5))
		cmd.select('glu3', 'name oe2 and resn glu within %s of (name nz and lys)'%(motifRange*11.2))
		cmd.select('glu4', 'name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*10.6))
		cmd.select('glu5', 'name oe1 and resn glu within %s of (name oh and resn tyr)'%(motifRange*8.7))
		cmd.select('glu6', 'name oe2 and resn glu within %s of (name oh and resn tyr)'%(motifRange*9.7))
		cmd.select('glu7', 'name cd and resn glu within %s of (name oh and resn tyr)'%(motifRange*9.6))
		cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and resn ser)'%(motifRange*10.5))
		cmd.select('glu9', 'name oe2 and resn glu within %s of (name og and resn ser)'%(motifRange*10.5))
		cmd.select('glu10', 'name oe1 and resn glu within %s of (name cb and resn ser)'%(motifRange*10))
		cmd.select('glu11', 'name oe2 and resn glu within %s of (name cb and resn ser)'%(motifRange*11.8))
		cmd.select('glu12', 'name cd and resn glu within %s of (name og and resn ser)'%(motifRange*11.8))
		cmd.select('glu13', 'name cd and resn glu within %s of (name cb and ser)'%(motifRange*11))
		cmd.select('glu14', 'name oe1 and resn glu within %s of (name cg and tyr)'%(motifRange*7.4))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14')
		cmd.select('lactamase', 'ser(tyr(glu(lys)))')
		cmd.show('sticks', 'lactamase')
	
	def superoxide(self,motifRange):
		cmd.select('his1', 'byres resn his within %s of elem cu'%(motifRange*4))
		cmd.select('arg1', 'byres resn arg within %s of elem cu'%(motifRange*6))
		cmd.select('stuff', 'his1 and (byres elem zn around %s)'%(motifRange*4))
		cmd.select('stuff1', 'arg1 and (byres elem zn around %s)'%(motifRange*6))
		cmd.select('stuff2', 'byres elem cu around %s and his1'%(motifRange*4))
		cmd.select('stuff3', 'byres elem cu around %s and arg1'%(motifRange*6))
		cmd.select('stuff4', 'stuff and stuff1 and stuff2 and stuff3')
		cmd.select('superoxide', 'byres his1(arg1(stuff4))')
		cmd.show('sticks', 'superoxide')
		cmd.show('spheres', 'elem cu')
		cmd.show('spheres', 'elem zn')
	
	def metalloprotease(self,motifRange):
		cmd.select('zn', 'elem zn')
		cmd.select('metalloprotease', 'zn(byres zn around %s)'%(motifRange*5))
		cmd.show('sticks', 'metalloprotease')
		cmd.show('sphere', 'zn')
		cmd.delete('zn')
	
	def tyrophos(self,motifRange):
		cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(motifRange*7))
		cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(motifRange*7))
		cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(motifRange*6.5))
		cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(motifRange*7))
		cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(motifRange*7))
		cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(motifRange*6.5))
		cmd.select('arg7', 'name nh2 and resn arg within %s of (name og and resn ser)'%(motifRange*10))
		cmd.select('arg8', 'name nh1 and resn arg within %s of (name cb and resn ser)'%(motifRange*11.2))
		cmd.select('arg9', 'name ne and resn arg within %s of (name ca and resn ser)'%(motifRange*9))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
		cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and arg)'%(motifRange*7))
		cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and arg)'%(motifRange*7))
		cmd.select('asp3', 'name cb and resn asp within %s of (name ne and arg)'%(motifRange*6.5))
		cmd.select('asp4', 'name od2 and resn asp within %s of (name c and resn ser)'%(motifRange*11))
		cmd.select('asp5', 'name od1 and resn asp within %s of (name ca and resn ser)'%(motifRange*12))
		cmd.select('asp6', 'name cb and resn asp within %s of (name cb and resn ser)'%(motifRange*9.2))
		cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(motifRange*12))
		cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(motifRange*11))
		cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(motifRange*10))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
		cmd.select('cys1', 'name ca and resn cys within %s of (name og and resn ser)'%(motifRange*6.5))
		cmd.select('cys2', 'name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('cys3', 'name sg and resn cys within %s of (name ca and resn ser)'%(motifRange*6))
		cmd.select('cys4', 'name c and resn cys within %s of (name od1 and asp)'%(motifRange*12))
		cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and asp)'%(motifRange*11))
		cmd.select('cys6', 'name sg and resn cys within %s of (name cb and asp)'%(motifRange*10))
		cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and arg)'%(motifRange*7))
		cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and arg)'%(motifRange*7))
		cmd.select('cys9', 'name sg and resn cys within %s of (name ne and arg)'%(motifRange*6.5))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
		cmd.select('ser1', 'name og and resn ser within %s of (name nh2 and arg)'%(motifRange*10))
		cmd.select('ser2', 'name cb and resn ser within %s of (name nh1 and arg)'%(motifRange*11.2))
		cmd.select('ser3', 'name ca and resn ser within %s of (name ne and arg)'%(motifRange*9))
		cmd.select('ser4', 'name c and resn ser within %s of (name od2 and asp)'%(motifRange*11))
		cmd.select('ser5', 'name ca and resn ser within %s of (name od1 and asp)'%(motifRange*12))
		cmd.select('ser6', 'name cb and resn ser within %s of (name cb and asp)'%(motifRange*9.2))
		cmd.select('ser7', 'name og and resn ser within %s of (name ca and cys)'%(motifRange*6.5))
		cmd.select('ser8', 'name cb and resn ser within %s of (name cb and cys)'%(motifRange*7))
		cmd.select('ser9', 'name ca and resn ser within %s of (name sg and cys)'%(motifRange*6))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
		cmd.select('tyrophos', 'ser(asp(arg(cys)))')
		tycount = cmd.index('tyrophos')
		atcount	= len(tycount)
		if(atcount < 1):
			cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and resn asp)'%(motifRange*7))
			cmd.select('arg2', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(motifRange*7))
			cmd.select('arg3', 'name ne and resn arg within %s of (name cb and resn asp)'%(motifRange*6.5))
			cmd.select('arg4', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(motifRange*7))
			cmd.select('arg5', 'name nh1 and resn arg within %s of (name cb and resn cys)'%(motifRange*7))
			cmd.select('arg6', 'name ne and resn arg within %s of (name sg and resn cys)'%(motifRange*6.5))
			cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg6')
			cmd.select('asp1', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(motifRange*7))
			cmd.select('asp2', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*7))
			cmd.select('asp3', 'name cb and resn asp within %s of (name ne and resn arg)'%(motifRange*6.5))
			cmd.select('asp7', 'name od1 and resn asp within %s of (name c and resn cys)'%(motifRange*12))
			cmd.select('asp8', 'name od2 and resn asp within %s of (name cb and resn cys)'%(motifRange*11))
			cmd.select('asp9', 'name cb and resn asp within %s of (name sg and resn cys)'%(motifRange*10))
			cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp7 and byres asp8 and byres asp9')
			cmd.select('cys4', 'name c and resn cys within %s of (name od1 and resn asp)'%(motifRange*12))
			cmd.select('cys5', 'name cb and resn cys within %s of (name od2 and resn asp)'%(motifRange*11))
			cmd.select('cys6', 'name sg and resn cys within %s of (name cb and resn asp)'%(motifRange*10))
			cmd.select('cys7', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(motifRange*7))
			cmd.select('cys8', 'name cb and resn cys within %s of (name nh1 and resn arg)'%(motifRange*7))
			cmd.select('cys9', 'name sg and resn cys within %s of (name ne and resn arg)'%(motifRange*6.5))
			cmd.select('cys', 'byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
			cmd.select('tyrophos', '(asp(arg(cys)))')
			cmd.show('sticks', 'tyrophos')
		else:
			cmd.show('sticks', 'tyrophos')
	
	def carbanhyd(self,motifRange):
		cmd.select('zn', 'elem zn')
		cmd.select('his', 'resn his within %s of zn'%(motifRange*5))
		cmd.select('carbonicanhydrase', 'byres his or zn')
		cmd.delete('zn')
		cmd.delete('his')
	
	def paplike(self,motifRange):
		cmd.select('gln1', 'name ne2 and resn gln within %s of (name ne2 and resn his)'%(motifRange*7))
		cmd.select('gln2', 'name cd and resn gln within %s of (name ce1 and resn his)'%(motifRange*6.7))
		cmd.select('gln3', 'name oe1 and resn gln within %s of (name nd1 and resn his)'%(motifRange*7))
		cmd.select('gln4', 'name ne2 and resn gln within %s of (name cb and resn cys)'%(motifRange*5.5))
		cmd.select('gln5', 'name oe1 and resn gln within %s of (name sg and resn cys)'%(motifRange*6.7))
		cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3 and byres gln4 and byres gln5')
		cmd.select('his1', 'name ne2 and resn his within %s of (name ne2 and gln)'%(motifRange*7))
		cmd.select('his2', 'name ce1 and resn his within %s of (name cd and gln)'%(motifRange*6.7))
		cmd.select('his3', 'name nd1 and resn his within %s of (name oe1 and gln)'%(motifRange*7))
		cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn cys)'%(motifRange*5.7))
		cmd.select('his5', 'name nd1 and resn his within %s of (name sg and resn cys)'%(motifRange*6))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5')
		cmd.select('cys1', 'name cb and resn cys within %s of (name ce1 and his)'%(motifRange*5.7))
		cmd.select('cys2', 'name sg and resn cys within %s of (name nd1 and his)'%(motifRange*6))
		cmd.select('cys3', 'name cb and resn cys within %s of (name ne2 and gln)'%(motifRange*5.5))
		cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and gln)'%(motifRange*6.7))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4')
		cmd.select('paplike', 'gln(his(cys))')
	
	def zincfinger(self,motifRange):
		cmd.select('zn1', 'elem zn')
		xm = cmd.index('zn1')
		nm	= len(xm)
		if(nm < 1):
			cmd.delete('zn1')
		objects = cmd.get_names('all')
		if 'zn1' in objects:
			cmd.select('zn1', 'elem zn')
			cmd.select('his', 'resn his')
			cmd.select('cys', 'resn cys')
			cmd.select('cys1', 'resn cys around %s'%(motifRange*4))
			cmd.select('Zinc_finger', '(resn cys or resn his(and byres cys1))')

	def aminotransferase(self,motifRange):
		cmd.select('asp1', 'name od1 and resn asp within %s of (name cb and resn his)'%(motifRange*5))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name cg and resn his)'%(motifRange*6))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*7))
		cmd.select('asp4', 'name cg and resn asp within %s of (name cb and resn his)'%(motifRange*6.5))
		cmd.select('asp5', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asp6', 'name od1 and resn asp within %s of (name cd2 and resn his)'%(motifRange*7))
		cmd.select('asp7', 'name od2 and resn asp within %s of (name nz and resn lys)'%(motifRange*9))
		cmd.select('asp8', 'name cg and resn asp within %s of (name nz and resn lys)'%(motifRange*9))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp8')
		cmd.select('his1', 'name cb and resn his within %s of (name od1 and resn asp)'%(motifRange*5))
		cmd.select('his2', 'name cg and resn his within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('his3', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*7))
		cmd.select('his4', 'name cb and resn his within %s of (name cg and asp)'%(motifRange*6.5))
		cmd.select('his5', 'name ne2 and resn his within %s of (name od1 and asp)'%(motifRange*8))
		cmd.select('his6', 'name cd2 and resn his within %s of (name od1 and asp)'%(motifRange*7))
		cmd.select('his7', 'name nd1 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('his8', 'name ne2 and resn his within %s of (name nz and resn lys)'%(motifRange*8))
		cmd.select('his9', 'name ce1 and resn his within %s of (name nz and resn lys)'%(motifRange*7))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
		cmd.select('lys1', 'name nz and resn lys within %s of (name od2 and asp)'%(motifRange*9))
		cmd.select('lys2', 'name nz and resn lys within %s of (name cg and asp)'%(motifRange*9))
		cmd.select('lys3', 'name nz and resn lys within %s of (name nd1 and his)'%(motifRange*7.5))
		cmd.select('lys4', 'name nz and resn lys within %s of (name ne2 and his)'%(motifRange*8))
		cmd.select('lys5', 'name nz and resn lys within %s of (name ce1 and his)'%(motifRange*7))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5')
		cmd.select('Aminotransferase', 'asp(his(lys))')
	
	def fisomerase(self,motifRange):
		cmd.select('his', 'elem mn around %s(elem mn)'%(motifRange*5))
		cmd.select('fucoseisomerase', 'byres resn asp and his(byres resn glu and his(elem mn))')
	
	def glutamine_amidotransferase(self,motifRange):
		cmd.select('his1', 'name ND1 within %s of name OE2'%(motifRange*3))
		cmd.select('his2', 'name NE2 within %s of name SG'%(motifRange*3.5))
		cmd.select('his', 'byres his1 and byres his2')
		cmd.select('glu1', 'resn glu within %s of his'%(motifRange*3.2))
		cmd.select('glu2', 'resn glu within %s of resn cys'%(motifRange*7))
		cmd.select('glu', 'byres glu1 and byres glu2')
		cmd.select('cys1', 'resn cys within %s of his'%(motifRange*3.5))
		cmd.select('cys2', 'resn cys within %s of glu'%(motifRange*7))
		cmd.select('cys', 'byres cys1 and byres cys2')
		cmd.select('glu_amidotransferase', 'cys(his(glu))')
	
	def dnaligase(self,motifRange):
		cmd.select('amp', 'resn amp')
		cmd.select('atp', 'resn atp')
		if(len(cmd.index('amp')) >= 1):
			cmd.select('amp1', 'resn amp around %s'%(motifRange*7.4))
			cmd.select('lys', 'resn lys and amp1')
			cmd.select('amp2', 'resn amp around %s'%(motifRange*7))	
			cmd.select('amp3', 'resn amp around %s'%(motifRange*5.3))
			cmd.select('asp', 'amp3 and(resn asp within %s of lys)'%(motifRange*3))
			cmd.select('arg', 'amp2 and(resn arg within %s of asp)'%(motifRange*5))
			cmd.select('Ligase', 'byres lys(amp(arg(asp)))')
		elif(len(cmd.index('atp')) >= 1):
			cmd.select('atp1', 'resn atp around %s'%(motifRange*7.4))
			cmd.select('lys', 'resn lys and atp1')
			cmd.select('atp2', 'resn atp around %s'%(motifRange*7))
			cmd.select('atp3', 'resn atp around %s'%(motifRange*5.3))
			cmd.select('asp', 'atp3 and(resn asp within %s of lys)'%(motifRange*3))
			cmd.select('arg', 'atp2 and(resn arg within %s of asp)'%(motifRange*5))
			cmd.select('Ligase', 'byres lys(atp(arg(asp)))')
		elif(len(cmd.index('amp')) < 1 and len(cmd.index('atp')) < 1):
			cmd.select('asp1', 'name OD2 within %s of name NE'%(motifRange*5.5))
			cmd.select('arg1', 'name NE within %s of name OD2'%(motifRange*5.5))
			cmd.select('lys1', 'name NZ within %s of name OD2'%(motifRange*9))
			cmd.select('lys2', 'name NZ within %s of name NH2'%(motifRange*10))
			cmd.select('arg', 'resn arg and arg1')
			cmd.select('asp', 'resn asp and asp1')
			cmd.select('lys', 'resn lys and lys1 and lys2')
			cmd.select('Ligase', 'byres arg(asp(lys))')
	
	def thymidinekinase(self,motifRange):
		cmd.select('glu1', 'name OE1 and resn glu within %s of name NH2 and resn arg'%(motifRange*5))
		cmd.select('glu2', 'resn glu and name OE2 within %s of name NE and resn arg'%(motifRange*5))
		cmd.select('glu3', 'resn glu and name OE1 within %s of name NH1 and resn arg'%(motifRange*6))
		cmd.select('glu4', 'resn glu and name OE1 within %s of name NE and resn arg'%(motifRange*6))
		cmd.select('glu5', 'resn glu and name OE2 within %s of name NH2 and resn arg'%(motifRange*5.5))
		cmd.select('glu6', 'resn glu and name oe1 within %s of name CZ and resn arg'%(motifRange*5))
		cmd.select('glu7', 'resn glu and name oe2 within %s of name CZ and resn arg'%(motifRange*5))
		cmd.select('glu8', 'resn glu and name oe1 within %s of name CD and resn arg'%(motifRange*5.8))
		cmd.select('glu9', 'resn glu and name oe2 within %s of name CD and resn arg'%(motifRange*5.5))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres resn glu')
		cmd.select('arg1', 'resn arg and name NH1 within %s of name OE2 and glu'%(motifRange*6))
		cmd.select('arg2', 'resn arg and name NE within %s of name OE2 and glu'%(motifRange*5.2))
		cmd.select('arg3', 'resn arg and name NH1 within %s of name oe1 and glu'%(motifRange*6))
		cmd.select('arg4', 'resn arg and name ne within %s of name oe1 and resn glu'%(motifRange*6.5))
		cmd.select('arg5', 'resn arg and name nh2 within %s of name oe2 and resn glu'%(motifRange*5.8))
		cmd.select('arg', 'byres resn arg and byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5')
		cmd.select('gly1', 'byres resn gly within %s of arg'%(motifRange*6.2))
		cmd.select('gly2', 'byres resn gly within %s of glu'%(motifRange*9))
		cmd.select('gly', 'byres resn gly and byres gly1 and byres gly2')
		cmd.select('glu10', 'byres glu within 10 of gly')
		cmd.select('arg10', 'byres arg within 9 of gly')
		cmd.select('Tkinase', 'glu10(arg10(gly))')
	
	def oglycosyl(self,motifRange):
		cmd.select('asp1', 'name od1 and resn asp within %s of (name oe1 and resn glu)'%(motifRange*9.5))
		cmd.select('notasp', 'resn asp within %s of resn glu'%(4.5/motifRange))
		cmd.select('asp', 'asp1 and (byres not notasp)')
		cmd.select('glu1', 'name oe1 and resn glu within %s of (name od1 and resn asp)'%(motifRange*9.5))
		cmd.select('glu0', 'resn glu within %s of resn asp'%(4.5/motifRange))
		cmd.select('glu', 'byres glu1 and (not glu0)')
		cmd.select('o-glycosyl', 'byres asp | byres glu')
	
	def carboncarbon(self,motifRange):
		cmd.select('asp1', 'name od1 within %s of name nz'%(motifRange*3.5))
		cmd.select('asp2', 'resn asp within %s of name ne2'%(motifRange*6))
		cmd.select('asp', 'byres asp1 and byres asp2')
		cmd.select('lys1', 'name nz within %s of asp'%(motifRange*6))
		cmd.select('lys2', 'resn lys within %s of resn his'%(motifRange*8))
		cmd.select('lys', 'byres lys1 and byres lys2')
		cmd.select('his1', 'name ne2 within %s of name nz'%(motifRange*6))
		cmd.select('his2', 'resn his within %s of lys'%(motifRange*6))
		cmd.select('his3', 'resn his within %s of asp'%(motifRange*9))
		cmd.select('his', 'byres his1 and byres his2 and byres his3')
		cmd.select('carboncarbon', 'asp(lys(his))')
	
	def peroxidase(self,motifRange):
		cmd.select('asn1', 'name od1 within %s of name nd1'%(motifRange*8))
		cmd.select('asn2', 'name od1 within %s of name ne2'%(motifRange*6))
		cmd.select('asn3', 'name nd2 within %s of name nd1'%(motifRange*10))
		cmd.select('asn4', 'name nd2 within %s of name ne2'%(motifRange*8))
		cmd.select('asn5', 'name od1 within %s of name nh2'%(motifRange*7))
		cmd.select('asn6', 'name od1 within %s of name nh1'%(motifRange*8.6))#measure more
		cmd.select('asn7', 'name od1 within %s of name ne'%(motifRange*8))
		cmd.select('asn8', 'name nd2 within %s of name nh2'%(motifRange*9))
		cmd.select('asn9', 'name nd2 within %s of name nh1'%(motifRange*11))#
		cmd.select('asn10', 'name nd2 within %s of name ne'%(motifRange*9.8))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10')
		cmd.select('his1', 'name nd1 within %s of name od1'%(motifRange*5))
		cmd.select('his2','name ne2 within %s of name od1'%(motifRange*5))
		cmd.select('his3', 'name nd1 within %s of name nd2'%(motifRange*8))#
		cmd.select('his4', 'name ne2 within %s of name nd2'%(motifRange*8.5))#
		cmd.select('his5', 'name ne2 within %s of name ne'%(motifRange*5.8))
		cmd.select('his6', 'name ne2 within %s of name nh2'%(motifRange*6))#
		cmd.select('his7', 'name ne2 within %s of name nh1'%(motifRange*8.2))#
		cmd.select('his8', 'name nd1 within %s of name nh1'%(motifRange*7.2))#
		cmd.select('his9', 'name nd1 within %s of name nh2'%(motifRange*5.8))
		cmd.select('his10', 'name nd1 within %s of name ne'%(motifRange*7))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
		cmd.select('arg1', 'name nh2 within %s of name od1'%(motifRange*7.5))
		cmd.select('arg2', 'name nh2 within %s of name nd2'%(motifRange*9.5))
		cmd.select('arg3', 'name nh2 within %s of name ne2'%(motifRange*6))#
		cmd.select('arg4', 'name nh2 within %s of name nd1'%(motifRange*6))
		cmd.select('arg5', 'name nh1 within %s of name od1'%(motifRange*8))#
		cmd.select('arg6', 'name nh1 within %s of name nd2'%(motifRange*10))
		cmd.select('arg7', 'name nh1 within %s of name ne2'%(motifRange*8))#
		cmd.select('arg8', 'name nh1 within %s of name nd1'%(motifRange*7.4))#
		cmd.select('arg9', 'name ne within %s of name od1'%(motifRange*7.2))
		cmd.select('arg10', 'name ne within %s of name nd2'%(motifRange*8.9))
		cmd.select('arg11', 'name ne within %s of name ne2'%(motifRange*5.9))
		cmd.select('arg12', 'name ne within %s of name nd1'%(motifRange*6))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byres arg11 and byres arg12')
		cmd.select('Peroxidase', 'asn(his(arg))')
	
	def trioseisomerase(self,motifRange):
		cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and resn asn)'%(motifRange*7.5))
		cmd.select('lys2', 'name nz and resn lys within %s of (name nd2 and resn asn)'%(motifRange*7.5))
		cmd.select('lys3', 'name nz and resn lys within %s of (name cg and resn asn)'%(motifRange*7.5))
		cmd.select('lys4', 'name ce and resn lys within %s of (name od1 and resn asn)'%(motifRange*6.5))
		cmd.select('lys5', 'name ce and resn lys within %s of (name nd2 and resn asn)'%(motifRange*6.5))
		cmd.select('lys6', 'name ce and resn lys within %s of (name cg and resn asn)'%(motifRange*6.5))
		cmd.select('lys7', 'name cd and resn lys within %s of (name od1 and resn asn)'%(motifRange*6.2))
		cmd.select('lys8', 'name cd and resn lys within %s of (name cg and resn asn)'%(motifRange*6.5))
		cmd.select('lys9', 'name cd and resn lys within %s of (name nd2 and resn asn)'%(motifRange*6.5))
		cmd.select('lys10', 'name nz and resn lys within %s of (name ne2 and resn his)'%(motifRange*6.5))
		cmd.select('lys11', 'name nz and resn lys within %s of (name nd1 and resn his)'%(motifRange*7.5))
		cmd.select('lys12', 'name nz and resn lys within %s of (name ce1 and resn his)'%(motifRange*6.7))
		cmd.select('lys13', 'name nz and resn lys within %s of (name cd2 and resn his)'%(motifRange*7.5))
		cmd.select('lys14', 'name nz and resn lys within %s of (name cg and resn his)'%(motifRange*8))
		cmd.select('lys15', 'name ce and resn lys within %s of (name ne2 and resn his)'%(motifRange*6.2))
		cmd.select('lys16', 'name ce and resn lys within %s of (name nd1 and resn his)'%(motifRange*7.6))
		cmd.select('lys17', 'name ce and resn lys within %s of (name ce1 and resn his)'%(motifRange*6.6))
		cmd.select('lys18', 'name ce and resn lys within %s of (name cd2 and resn his)'%(motifRange*7))
		cmd.select('lys19', 'name ce and resn lys within %s of (name cg and resn his)'%(motifRange*7.5))
		cmd.select('lys20', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*8.5))
		cmd.select('lys21', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*10))
		cmd.select('lys22', 'name nz and resn lys within %s of (name cd and resn glu)'%(motifRange*9.5))
		cmd.select('lys23', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(motifRange*9))
		cmd.select('lys24', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*10.2))
		cmd.select('lys25', 'name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*10))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14 and byres lys15 and byres lys16 and byres lys17 and byres lys18 and byres lys19 and byres lys20 and byres lys21 and byres lys22 and byres lys23 and byres lys24 and byres lys25')
		cmd.select('asn1', 'name od1 and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('asn2', 'name nd2 and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('asn3', 'name cg and resn asn within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('asn4', 'name od1 and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
		cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
		cmd.select('asn6', 'name cg and resn asn within %s of (name ce and resn lys)'%(motifRange*6.5))
		cmd.select('asn7', 'name od1 and resn asn within %s of (name cd and resn lys)'%(motifRange*6.2))
		cmd.select('asn8', 'name cg and resn asn within %s of (name cd and resn lys)'%(motifRange*6.5))
		cmd.select('asn9', 'name nd2 and resn asn within %s of (name cd and resn lys)'%(motifRange*6.5))
		cmd.select('asn10', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*6.3))
		cmd.select('asn11', 'name nd2 and resn asn within %s of (name cd2 and resn his)'%(motifRange*6.2))
		cmd.select('asn12', 'name nd2 and resn asn within %s of (name ce1 and resn his)'%(motifRange*7.3))
		cmd.select('asn13', 'name nd2 and resn asn within %s of (name nd1 and resn his)'%(motifRange*8))
		cmd.select('asn14', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asn15', 'name od1 and resn asn within %s of (name ce1 and resn his)'%(motifRange*9.2))
		cmd.select('asn16', 'name od1 and resn asn within %s of (name cd2 and resn his)'%(motifRange*8.3))
		cmd.select('asn17', 'name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*7.5))
		cmd.select('asn18', 'name cg and resn asn within %s of (name ce1 and resn his)'%(motifRange*8.5))
		cmd.select('asn19', 'name cg and resn asn within %s of (name cd2 and resn his)'%(motifRange*7.5))
		cmd.select('asn20', 'name nd2 and resn asn within %s of (name oe2 and resn glu)'%(motifRange*9))
		cmd.select('asn21', 'name nd2 and resn asn within %s of (name oe1 and resn glu)'%(motifRange*10.5))
		cmd.select('asn22', 'name nd2 and resn asn within %s of (name cd and resn glu)'%(motifRange*10.2))
		cmd.select('asn23', 'name cg and resn asn within %s of (name oe2 and resn glu)'%(motifRange*10))
		cmd.select('asn24', 'name cg and resn asn within %s of (name cd and resn glu)'%(motifRange*11))
		cmd.select('asn25', 'name cg and resn asn within %s of (name oe1 and resn glu)'%(motifRange*11.3))
		cmd.select('asn26', 'name od1 and resn asn within %s of (name oe2 and resn glu)'%(motifRange*11))
		cmd.select('asn27', 'name od1 and resn asn within %s of (name cd and resn glu)'%(motifRange*11))
		cmd.select('asn28', 'name od1 and resn asn within %s of (name oe1 and resn glu)'%(motifRange*12))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11 and byres asn12 and byres asn13 and byres asn14 and byres asn15 and byres asn16 and byres asn17 and byres asn18 and byres asn19 and byres asn20 and byres asn21 and byres asn22 and byres asn23 and byres asn24 and byres asn25 and byres asn26 and byres asn27 and byres asn28')
		cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(motifRange*8.5))
		cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*10))
		cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(motifRange*9.5))
		cmd.select('glu4', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(motifRange*9))
		cmd.select('glu5', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*10.2))
		cmd.select('glu6', 'name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*10))
		cmd.select('glu7', 'name oe2 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*9))
		cmd.select('glu8', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*10.5))
		cmd.select('glu9', 'name cd and resn glu within %s of (name nd2 and resn asn)'%(motifRange*10.2))
		cmd.select('glu10', 'name oe2 and resn glu within %s of (name cg and resn asn)'%(motifRange*10))
		cmd.select('glu11', 'name cd and resn glu within %s of (name cg and resn asn)'%(motifRange*11))
		cmd.select('glu12', 'name oe1 and resn glu within %s of (name cg and resn asn)'%(motifRange*11.3))
		cmd.select('glu13', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(motifRange*11))
		cmd.select('glu14', 'name cd and resn glu within %s of (name od1 and resn asn)'%(motifRange*11))
		cmd.select('glu15', 'name oe1 and resn glu within %s of (name od1 and resn asn)'%(motifRange*12))
		cmd.select('glu16', 'name oe2 and resn glu within %s of (name ne2 and resn his)'%(motifRange*5.6))
		cmd.select('glu17', 'name oe2 and resn glu within %s of (name cd2 and resn his)'%(motifRange*6.5))
		cmd.select('glu18', 'name oe2 and resn glu within %s of (name ce1 and resn his)'%(motifRange*5.8))
		cmd.select('glu19', 'name oe2 and resn glu within %s of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('glu20', 'name oe2 and resn glu within %s of (name cg and resn his)'%(motifRange*6.6))
		cmd.select('glu21', 'name oe1 and resn glu within %s of (name ne2 and resn his)'%(motifRange*6.6))
		cmd.select('glu22', 'name oe1 and resn glu within %s of (name cd2 and resn his)'%(motifRange*6.5))
		cmd.select('glu23', 'name oe1 and resn glu within %s of (name ce1 and resn his)'%(motifRange*5.8))
		cmd.select('glu24', 'name oe1 and resn glu within %s of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('glu25', 'name oe1 and resn glu within %s of (name cg and resn his)'%(motifRange*6.6))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11 and byres glu12 and byres glu13 and byres glu14 and byres glu15 and byres glu16 and byres glu17 and byres glu18 and byres glu19 and byres glu20 and byres glu21 and byres glu22 and byres glu23 and byres glu24 and byres glu25')
		cmd.select('his1', 'name ne2 and resn his within %s of (name nz and resn lys)'%(motifRange*6.5))
		cmd.select('his2', 'name nd1 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('his3', 'name ce1 and resn his within %s of (name nz and resn lys)'%(motifRange*6.7))
		cmd.select('his4', 'name cd2 and resn his within %s of (name nz and resn lys)'%(motifRange*7.5))
		cmd.select('his5', 'name cg and resn his within %s of (name nz and resn lys)'%(motifRange*8))
		cmd.select('his6', 'name ne2 and resn his within %s of (name ce and resn lys)'%(motifRange*6.2))
		cmd.select('his7', 'name nd1 and resn his within %s of (name ce and resn lys)'%(motifRange*7.6))
		cmd.select('his8', 'name ce1 and resn his within %s of (name ce and resn lys)'%(motifRange*6.6))
		cmd.select('his9', 'name cd2 and resn his within %s of (name ce and resn lys)'%(motifRange*7))
		cmd.select('his10', 'name cg and resn his within %s of (name ce and resn lys)'%(motifRange*7.5))
		cmd.select('his11', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*6.3))
		cmd.select('his12', 'name cd2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*6.2))
		cmd.select('his13', 'name ce1 and resn his within %s of (name nd2 and resn asn)'%(motifRange*7.3))
		cmd.select('his14', 'name nd1 and resn his within %s of (name nd2 and resn asn)'%(motifRange*8))
		cmd.select('his15', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*8))
		cmd.select('his16', 'name ce1 and resn his within %s of (name od1 and resn asn)'%(motifRange*9.2))
		cmd.select('his17', 'name cd2 and resn his within %s of (name od1 and resn asn)'%(motifRange*8.3))
		cmd.select('his18', 'name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*7.5))
		cmd.select('his19', 'name ce1 and resn his within %s of (name cg and resn asn)'%(motifRange*8.5))
		cmd.select('his20', 'name cd2 and resn his within %s of (name cg and resn asn)'%(motifRange*7.5))
		cmd.select('his21', 'name ne2 and resn his within %s of (name oe2 and resn glu)'%(motifRange*5.6))
		cmd.select('his22', 'name cd2 and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.5))
		cmd.select('his23', 'name ce1 and resn his within %s of (name oe2 and resn glu)'%(motifRange*5.8))
		cmd.select('his24', 'name nd1 and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.5))
		cmd.select('his25', 'name cg and resn his within %s of (name oe2 and resn glu)'%(motifRange*6.6))
		cmd.select('his26', 'name ne2 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.6))
		cmd.select('his27', 'name cd2 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.5))
		cmd.select('his28', 'name ce1 and resn his within %s of (name oe1 and resn glu)'%(motifRange*5.8))
		cmd.select('his29', 'name nd1 and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.5))
		cmd.select('his30', 'name cg and resn his within %s of (name oe1 and resn glu)'%(motifRange*6.6))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13 and byres his14 and byres his15 and byres his16 and byres his17 and byres his18 and byres his19 and byres his20 and byres his21 and byres his22 and byres his23 and byres his24 and byres his25 and byres his26 and byres his27 and byres his28 and byres his29 and byres his30')
		cmd.select('TrioseIsomerase', 'glu(his(asn(lys)))')
	
	def alcoholdehyd(self,motifRange):
		cmd.select('tyr1', 'name cd1 and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*5))
		cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asn)'%(motifRange*8))
		cmd.select('tyr3', 'name oh and resn tyr within %s of (name nz and resn lys)'%(motifRange*6))
		cmd.select('tyr4', 'name oh and resn tyr within %s of (name og and resn ser)'%(motifRange*5.5))
		cmd.select('tyr5', 'name ce2 and resn tyr within %s of (name cg and resn lys)'%(motifRange*6))
		cmd.select('tyr6', 'name cg and resn tyr within %s of (name nd2 and resn asn)'%(motifRange*6.5))
		cmd.select('tyr7', 'name oh and resn tyr within %s of (name cb and resn ser)'%(motifRange*5.5))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
		cmd.select('asn1', 'name nd2 and resn asn within %s of (name cd1 and tyr)'%(motifRange*5))
		cmd.select('asn2', 'name nd2 and resn asn within %s of (name oh and tyr)'%(motifRange*7))
		cmd.select('asn3', 'name od1 and resn asn within %s of (name oh and tyr)'%(motifRange*7))
		cmd.select('asn4', 'name od1 and resn asn within %s of (name ce1 and tyr)'%(motifRange*6))
		cmd.select('asn5', 'name nd2 and resn asn within %s of (name ce and resn lys)'%(motifRange*5.5))
		cmd.select('asn6', 'name od1 and resn asn within %s5 of (name nz and resn lys)'%(motifRange*5.5))
		cmd.select('asn7', 'name nd2 and resn asn within %s of (name og and resn ser)'%(motifRange*10))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7')
		cmd.select('lys1', 'name nz and resn lys within %s of (name od1 and asn)'%(motifRange*6))
		cmd.select('lys2', 'name ce and resn lys within %s of (name nd2 and asn)'%(motifRange*6.5))
		cmd.select('lys3', 'name nz and resn lys within %s of (name oh and tyr)'%(motifRange*6))
		cmd.select('lys4', 'name ce and resn lys within %s of (name cz and tyr)'%(motifRange*6))
		cmd.select('lys4', 'name nz and resn lys within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('lys5', 'name ce and resn lys within %s of (name og and resn ser)'%(motifRange*7))
		cmd.select('lys6', 'name cg and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6))
		cmd.select('lys7', 'name cd and resn lys within %s of (name cb and resn ser)'%(motifRange*6))
		cmd.select('lys8', 'name cd and resn lys within %s of (name cb and resn asn)'%(motifRange*7))
		cmd.select('lys9', 'name ce and resn lys within %s of (name ce1 and resn tyr)'%(motifRange*6))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
		cmd.select('ser1', 'name og and resn ser within %s of (name oh and tyr)'%(motifRange*6))
		cmd.select('ser2', 'name og and resn ser within %s of (name ce2 and tyr)'%(motifRange*6))
		cmd.select('ser3', 'name og and resn ser within %s of (name nz and lys)'%(motifRange*8))
		cmd.select('ser4', 'name cb and resn ser within %s of (name oh and tyr)'%(motifRange*6))
		cmd.select('ser5', 'name cb and resn ser within %s of (name cd and lys)'%(motifRange*6))
		cmd.select('ser6', 'name cb and resn ser within %s of (name od1 and asn)'%(motifRange*10))
		cmd.select('ser7', 'name ca and resn ser within %s of (name nd2 and asn)'%(motifRange*10))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7')
		cmd.select('alcoholdehyd','ser(tyr(lys(asn)))')
	
	def aldoreductase(self,motifRange):
		cmd.select('lys1', 'name cd and resn lys within %s of (name cg and resn his)'%(motifRange*6))
		cmd.select('lys2', 'name ce and resn lys within %s of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('lys3', 'name cd and resn lys within %s of (name nd1 and resn his)'%(motifRange*7))
		cmd.select('lys4', 'name nz and resn lys within %s of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('lys5', 'name nz and resn lys within %s of (name ce2 and resn tyr)'%(motifRange*6))
		cmd.select('lys6', 'name cg and resn lys within %s of (name cz and resn tyr)'%(motifRange*8))
		cmd.select('lys7', 'name nz and resn lys within %s of (name od1 and resn asp)'%(motifRange*5))
		cmd.select('lys8', 'name ce and resn lys within %s of (name od1 and resn asp)'%(motifRange*5.5))
		cmd.select('lys9', 'name cg and resn lys within %s of (name ca and resn asp)'%(motifRange*9))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9')
		cmd.select('his1', 'name cg and resn his within %s of (name cd and resn lys)'%(motifRange*6))
		cmd.select('his2', 'name ne2 and resn his within %s of (name ce and resn lys)'%(motifRange*8))
		cmd.select('his3', 'name nd1 and resn his within %s of (name cd and resn lys)'%(motifRange*7))
		cmd.select('his4', 'name ne2 and resn his within %s of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('his5', 'name ce1 and resn his within %s of (name cz and resn tyr)'%(motifRange*6))
		cmd.select('his6', 'name nd1 and resn his within %s of (name ce1 and resn tyr)'%(motifRange*7))
		cmd.select('his7', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*10.5))
		cmd.select('his8', 'name ne2 and resn his within %s of (name cg and resn asp)'%(motifRange*10))
		cmd.select('his9', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*9))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name nz and resn lys )'%(motifRange*5))
		cmd.select('tyr2', 'name ce2 and resn tyr within %s of (name nz and resn lys )'%(motifRange*6))
		cmd.select('tyr3', 'name cz and resn tyr within %s of (name cg and resn lys)'%(motifRange*8))
		cmd.select('tyr4', 'name oh and resn tyr within %s of (name ne2 and resn his)'%(motifRange*6))
		cmd.select('tyr5', 'name cz and resn tyr within %s of (name ce1 and resn his)'%(motifRange*6))
		cmd.select('tyr6', 'name ce1 and resn tyr within %s of (name nd1 and resn his)'%(motifRange*7))
		cmd.select('tyr7', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(motifRange*7))
		cmd.select('tyr8', 'name cz and resn tyr within %s of (name cb and resn asp)'%(motifRange*9))
		cmd.select('tyr9', 'name ce2 and resn tyr within %s of (name ca and resn asp)'%(motifRange*8))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9')
		cmd.select('asp1', 'name od1 and resn asp within %s of (name nz and resn lys)'%(motifRange*5))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name ce and resn lys)'%(motifRange*5.5))
		cmd.select('asp3', 'name ca and resn asp within %s of (name cg and resn lys)'%(motifRange*9))
		cmd.select('asp4', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*10.5))
		cmd.select('asp5', 'name cg and resn asp within %s of (name ne2 and resn his)'%(motifRange*10))
		cmd.select('asp6', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*9))
		cmd.select('asp7', 'name od2 and resn asp within %s of (name oh and resn tyr)'%(motifRange*7))
		cmd.select('asp8', 'name cb and resn asp within %s of (name cz and resn tyr)'%(motifRange*9))
		cmd.select('asp9', 'name ca and resn asp within %s of (name ce2 and resn tyr)'%(motifRange*8))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
		cmd.select('aldoreductase', 'asp(his(lys(tyr)))')
	
	def cistransisomerase(self,motifRange):
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name od2 and resn asp)'%(motifRange*9))
		cmd.select('tyr2', 'name oh and resn tyr within %s of (name od1 and resn asp)'%(motifRange*11))
		cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and resn asp)'%(motifRange*9.8))
		cmd.select('tyr4', 'name oh and resn tyr within %s of (name cb and resn asp)'%(motifRange*9.8))
		cmd.select('tyr5', 'name cz and resn tyr within %s of (name od2 and resn asp)'%(motifRange*10.2))
		cmd.select('tyr6', 'name cz and resn tyr within %s of (name od1 and resn asp)'%(motifRange*11.5))
		cmd.select('tyr7', 'name oh and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.5))
		cmd.select('tyr8', 'name oh and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.5))
		cmd.select('tyr9', 'name oh and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
		cmd.select('tyr10', 'name cz and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.5))
		cmd.select('tyr11', 'name cz and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.8))
		cmd.select('tyr12', 'name cz and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
		cmd.select('tyr13', 'name ce1 and resn tyr within %s of (name cd1 and resn ile)'%(motifRange*6.3))
		cmd.select('tyr14', 'name ce1 and resn tyr within %s of (name cg1 and resn ile)'%(motifRange*6.5))
		cmd.select('tyr15', 'name ce1 and resn tyr within %s of (name cg2 and resn ile)'%(motifRange*5.5))
		cmd.select('tyr', 'byres tyr1 and byre tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13 and byres tyr14 and byres tyr15')
		cmd.select('asp1', 'name od2 and resn asp within %s of (name oh and tyr)'%(motifRange*8.7))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name oh and tyr)'%(motifRange*10.5))
		cmd.select('asp3', 'name cg and resn asp within %s of (name oh and tyr)'%(motifRange*9.3))
		cmd.select('asp4', 'name cb and resn asp within %s of (name oh and tyr)'%(motifRange*9.3))
		cmd.select('asp5', 'name od2 and resn asp within %s of (name cz and tyr)'%(motifRange*10))
		cmd.select('asp6', 'name od1 and resn asp within %s of (name cz and resn tyr)'%(motifRange*11.1))
		cmd.select('asp7', 'name od2 and resn asp within %s of (name cg2 and resn ile)'%(motifRange*11.1))
		cmd.select('asp8', 'name od2 and resn asp within %s of (name cd1 and resn ile)'%(motifRange*11.1))
		cmd.select('asp9', 'name od2 and resn asp within %s of (name cg1 and resn ile)'%(motifRange*11.1))
		cmd.select('asp10', 'name cb and resn asp within %s of (name cd1 and resn ile)'%(motifRange*10.8))
		cmd.select('asp11', 'name cb and resn asp within %s of (name cg2 and resn ile)'%(motifRange*11.1))
		cmd.select('asp12', 'name cb and resn asp within %s of (name cg1 and resn ile)'%(motifRange*11.1))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11 and byres asp12')
		cmd.select('ile1', 'name cd1 and resn ile within %s of (name oh and tyr)'%(motifRange*6.5))
		cmd.select('ile2', 'name cg1 and resn ile within %s of (name oh and tyr)'%(motifRange*6.5))
		cmd.select('ile3', 'name cg2 and resn ile within %s of (name oh and tyr)'%(motifRange*5.5))
		cmd.select('ile4', 'name cd1 and resn ile within %s of (name cz and resn tyr)'%(motifRange*6.5))
		cmd.select('ile5', 'name cg1 and resn ile within %s of (name cz and resn tyr)'%(motifRange*6.8))
		cmd.select('ile6', 'name cg2 and resn ile within %s of (name cz and resn tyr)'%(motifRange*5.5))
		cmd.select('ile7', 'name cd1 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*6.3))
		cmd.select('ile8', 'name cg1 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('ile9', 'name cg2 and resn ile within %s of (name ce1 and resn tyr)'%(motifRange*5.5))
		cmd.select('ile10', 'name cg2 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
		cmd.select('ile11', 'name cd1 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
		cmd.select('ile12', 'name cg1 and resn ile within %s of (name od2 and asp)'%(motifRange*11.5))
		cmd.select('ile13', 'name cd1 and resn ile within %s of (name cb and asp)'%(motifRange*11))
		cmd.select('ile14', 'name cg2 and resn ile within %s of (name cb and resn asp)'%(motifRange*11.5))
		cmd.select('ile15', 'name cg1 and resn ile within %s of (name cb and resn asp)'%(motifRange*11.5))
		cmd.select('ile', 'byres ile1 and byres ile2 and byres ile3 and byres ile4 and byres ile5 and byres ile6 and byres ile7 and byres ile8 and byres ile9 and byres ile10 and byres ile11 and byres ile12 and byres ile13 and byres ile14 and byres ile15')
		cmd.select('Cis-trans', 'ile(asp(tyr))')
	
	def nadhbinder(self,motifRange):
		cmd.select('asp1', 'name od2 and resn asp within %s of (name sg and resn cys)'%(motifRange*5))
		cmd.select('asp2', 'name od2 and resn asp within %s of (name cb and resn cys)'%(motifRange*5.5))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name sg and resn cys)'%(motifRange*6.4))
		cmd.select('asp4', 'name od1 and resn asp within %s of (name cb and resn cys)'%(motifRange*7.2))
		cmd.select('asp5', 'name cg and resn asp within %s of (name sg and resn cys)'%(motifRange*5.5))
		cmd.select('asp6', 'name od2 and resn asp within %s of (name og and resn ser)'%(motifRange*4.5))
		cmd.select('asp7', 'name od2 and resn asp within %s of (name cb and resn ser)'%(motifRange*5.5))
		cmd.select('asp8', 'name od1 and resn asp within %s of (name og and resn ser)'%(motifRange*6))
		cmd.select('asp9', 'name od1 and resn asp within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('asp10', 'name cg and resn asp within %s of (name og and resn ser)'%(motifRange*5.3))
		cmd.select('asp11', 'name cg and resn asp within %s of (name cb and resn ser)'%(motifRange*6.4))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10 and byres asp11')
		cmd.select('cys1', 'name sg and resn cys within %s of (name od2 and resn asp)'%(motifRange*5))
		cmd.select('cys2', 'name cb and resn cys within %s of (name od2 and resn asp)'%(motifRange*5.5))
		cmd.select('cys3', 'name sg and resn cys within %s of (name od1 and resn asp)'%(motifRange*6.4))
		cmd.select('cys4', 'name cb and resn cys within %s of (name od1 and resn asp)'%(motifRange*7.2))
		cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn asp)'%(motifRange*5.5))
		cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(motifRange*6.4))
		cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(motifRange*8))
		cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*8.5))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
		cmd.select('ser1', 'name og and resn ser within %s of (name od2 and resn asp)'%(motifRange*4.5))
		cmd.select('ser2', 'name cb and resn ser within %s of (name od2 and resn asp)'%(motifRange*5.5))
		cmd.select('ser3', 'name og and resn ser within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('ser4', 'name cb and resn ser within %s of (name od1 and resn asp)'%(motifRange*7))
		cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn asp)'%(motifRange*5.3))
		cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn asp)'%(motifRange*6.4))
		cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(motifRange*6.4))
		cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(motifRange*7))
		cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(motifRange*8))
		cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(motifRange*8.5))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
		cmd.select('NAD-reductase', 'ser(asp(cys))')

	def nadhbinder2(self,motifRange):
		cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(motifRange*6.5))
		cmd.select('glu2', 'name oe2 and resn glu within %s of (name cb and resn cys)'%(motifRange*5.5))
		cmd.select('glu3', 'name oe1 and resn glu within %s of (name sg and resn cys)'%(motifRange*6.5))
		cmd.select('glu4', 'name oe1 and resn glu within %s of (name cb and resn cys)'%(motifRange*7.2))
		cmd.select('glu5', 'name cg and resn glu within %s of (name sg and resn cys)'%(motifRange*5.5))
		cmd.select('glu6', 'name oe2 and resn glu within %s of (name og and resn ser)'%(motifRange*4.5))
		cmd.select('glu7', 'name oe2 and resn glu within %s of (name cb and resn ser)'%(motifRange*5.5))
		cmd.select('glu8', 'name oe1 and resn glu within %s of (name og and resn ser)'%(motifRange*6))
		cmd.select('glu9', 'name oe1 and resn glu within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('glu10', 'name cg and resn glu within %s of (name og and resn ser)'%(motifRange*5.5))
		cmd.select('glu11', 'name cg and resn glu within %s of (name cb and resn ser)'%(motifRange*6.5))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10 and byres glu11')
		cmd.select('cys1', 'name sg and resn cys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
		cmd.select('cys2', 'name cb and resn cys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
		cmd.select('cys3', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(motifRange*6.5))
		cmd.select('cys4', 'name cb and resn cys within %s of (name oe1 and resn glu)'%(motifRange*7.5))
		cmd.select('cys5', 'name sg and resn cys within %s of (name cg and resn glu)'%(motifRange*5.5))
		cmd.select('cys6', 'name sg and resn cys within %s of (name og and resn ser)'%(motifRange*6.5))
		cmd.select('cys7', 'name sg and resn cys within %s of (name cb and resn ser)'%(motifRange*7))
		cmd.select('cys8', 'name cb and resn cys within %s of (name og and resn ser)'%(motifRange*8))
		cmd.select('cys9', 'name cb and resn cys within %s of (name cb and resn ser)'%(motifRange*8.5))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
		cmd.select('ser1', 'name og and resn ser within %s of (name oe2 and resn glu)'%(motifRange*4.5))
		cmd.select('ser2', 'name cb and resn ser within %s of (name oe2 and resn glu)'%(motifRange*5.5))
		cmd.select('ser3', 'name og and resn ser within %s of (name oe1 and resn glu)'%(motifRange*6))
		cmd.select('ser4', 'name cb and resn ser within %s of (name oe1 and resn glu)'%(motifRange*7))
		cmd.select('ser5', 'name og and resn ser within %s of (name cg and resn glu)'%(motifRange*5.5))
		cmd.select('ser6', 'name cb and resn ser within %s of (name cg and resn glu)'%(motifRange*6.5))
		cmd.select('ser7', 'name og and resn ser within %s of (name sg and resn cys)'%(motifRange*6.5))
		cmd.select('ser8', 'name cb and resn ser within %s of (name sg and resn cys)'%(motifRange*7))
		cmd.select('ser9', 'name og and resn ser within %s of (name cb and resn cys)'%(motifRange*8))
		cmd.select('ser10', 'name cb and resn ser within %s of (name cb and resn cys)'%(motifRange*8.5))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9 and byres ser10')
		cmd.select('NAD-reductase2', 'ser(glu(cys))')
	
	def cephdeacetylase(self,motifRange):
		cmd.select('his1', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*4.5))
		cmd.select('his2', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*5))
		cmd.select('his3', 'name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*5.5))
		cmd.select('his4', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
		cmd.select('his5', 'name ce1 and resn his within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('his6', 'name ne2 and resn his within %s of (name od1 and resn asp)'%(motifRange*7))
		cmd.select('his7', 'name ne2 and resn his within %s of (name od2 and resn asp)'%(motifRange*6.5))
		cmd.select('his8', 'name ne2 and resn his within %s of (name cb and resn ala)'%(motifRange*5.5))
		cmd.select('his9', 'name ce1 and resn his within %s of (name cb and resn ala)'%(motifRange*5.5))
		cmd.select('his10', 'name nd1 and resn his within %s of (name cb and resn ala)'%(motifRange*6.5))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
		cmd.select('asp1', 'name od2 and resn asp within %s of (name cb and resn ala)'%(motifRange*8.5))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name cb and resn ala)'%(motifRange*9.5))
		cmd.select('asp3', 'name cg and resn asp within %s of (name cb and resn ala)'%(motifRange*9.5))
		cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(motifRange*4.5))
		cmd.select('asp5', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5))
		cmd.select('asp6', 'name cg and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
		cmd.select('asp7', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*5.5))
		cmd.select('asp8', 'name od1 and resn asp within %s of (name ce1 and resn his)'%(motifRange*6))
		cmd.select('asp9', 'name od1 and resn asp within %s of (name ne2 and resn his)'%(motifRange*7))
		cmd.select('asp10', 'name od2 and resn asp within %s of (name ne2 and resn his)'%(motifRange*6.5))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9 and byres asp10')
		cmd.select('ala1', 'name cb and resn ala within %s of (name ne2 and resn his)'%(motifRange*5.5))
		cmd.select('ala2', 'name cb and resn ala within %s of (name ce1 and resn his)'%(motifRange*5.5))
		cmd.select('ala3', 'name cb and resn ala within %s of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('ala4', 'name cb and resn ala within %s of (name od2 and resn asp)'%(motifRange*8.5))
		cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and resn asp)'%(motifRange*9.5))
		cmd.select('ala6', 'name cb and resn ala within %s of (name cg and resn asp)'%(motifRange*9.5))
		cmd.select('ala7', 'name c and resn ala within %s of (name n and resn gln)'%(motifRange*2.5))
		cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
		cmd.select('gln1', 'byres resn gln within %s of his'%(motifRange*9.5))
		cmd.select('gln2', 'byres resn gln within %s of asp'%(motifRange*13.5))
		cmd.select('gln3', 'byres resn gln within %s of ala'%(motifRange*3))
		cmd.select('gln', 'byres gln1 and byres gln2 and byres gln3')
		cmd.select('deacetylase', 'his(asp(ala(gln)))')
	#hyaluronate/chondroitin lyase
	
	def chondrolyase(self,motifRange):
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(motifRange*6))
		cmd.select('tyr2', 'name oh and resn tyr within %s	of (name nh1 and resn arg)'%(motifRange*5))
		cmd.select('tyr3', 'name oh and resn tyr within %s	of (name cz and resn arg)'%(motifRange*6))
		cmd.select('tyr4', 'name oh and resn tyr within %s	of (name ne and resn arg)'%(motifRange*7))
		cmd.select('tyr5', 'name oh and resn tyr within %s	of (name ne2 and resn his)'%(motifRange*5))
		cmd.select('tyr6', 'name oh and resn tyr within %s	of (name nd1 and resn his)'%(motifRange*6))
		cmd.select('tyr7', 'name oh and resn tyr within %s	of (name ce1 and resn his)'%(motifRange*5))
		cmd.select('tyr8', 'name ce2 and resn tyr within %s	of (name nd1 and resn his)'%(motifRange*6))
		cmd.select('tyr9', 'name ce1 and resn tyr within %s	of (name ne2 and resn his)'%(motifRange*6))
		cmd.select('tyr10', 'name oh and resn tyr within %s	of (name od1 and resn asn)'%(motifRange*7.5))
		cmd.select('tyr11', 'name oh and resn tyr within %s	of (name nd2 and resn asn)'%(motifRange*7.5))
		cmd.select('tyr12', 'name ce1 and resn tyr within %s	of (name od1 and resn asn)'%(motifRange*6.5))
		cmd.select('tyr13', 'name ce1 and resn tyr within %s	of (name nd2 and resn asn)'%(motifRange*6))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
		cmd.select('his1', 'name ne2 and resn his within %s	of (name od1 and resn asn)'%(motifRange*7))
		cmd.select('his2', 'name ne2 and resn his within %s	of (name nd2 and resn asn)'%(motifRange*8))
		cmd.select('his3', 'name cd2 and resn his within %s	of (name od1 and resn asn)'%(motifRange*7))
		cmd.select('his4', 'name ne2 and resn his within %s	of (name cg and resn asn)'%(motifRange*8))
		cmd.select('his5', 'name ne2 and resn his within %s	of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('his6', 'name nd1 and resn his within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('his7', 'name ce1 and resn his within %s	of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('his8', 'name nd1 and resn his within %s	of (name ce2 and resn tyr)'%(motifRange*6))
		cmd.select('his9', 'name ne2 and resn his within %s	of (name ce1 and resn tyr)'%(motifRange*6))
		cmd.select('his10', 'name ne2 and resn his within %s	of (name nh2 and resn arg)'%(motifRange*8))
		cmd.select('his11', 'name ce1 and resn his within %s	of (name cz and resn arg)'%(motifRange*7))
		cmd.select('his12', 'name nd1 and resn his within %s	of (name nh1 and resn arg)'%(motifRange*6.5))
		cmd.select('his13', 'name nd1 and resn his within %s	of (name cd and resn arg)'%(motifRange*9))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
		cmd.select('arg1', 'name nh2 and resn arg within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('arg2', 'name nh1 and resn arg within %s	of (name oh and tyr)'%(motifRange*6))
		cmd.select('arg3', 'name cz and resn arg within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('arg4', 'name ne and resn arg within %s	of (name oh and resn tyr)'%(motifRange*7))
		cmd.select('arg5', 'name nh2 and resn arg within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('arg6', 'name cz and resn arg within %s	of (name ce1 and resn his)'%(motifRange*7))
		cmd.select('arg7', 'name nh1 and resn arg within %s	of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('arg8', 'name cd and resn arg within %s	of (name nd1 and resn his)'%(motifRange*9))
		cmd.select('arg9', 'name nh1 and resn arg within %s	of (name od1 and resn asn)'%(motifRange*11))
		cmd.select('arg10', 'name cz and resn arg within %s	of (name cg and resn asn)'%(motifRange*12))
		cmd.select('arg11', 'name nh2 and resn arg within %s	of (name nd2 and resn asn)'%(motifRange*11.5))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
		cmd.select('asn1', 'name od1 and resn asn within %s	of (name nh1 and resn arg)'%(motifRange*11))
		cmd.select('asn2', 'name cg and resn asn within %s	of (name cz and resn arg)'%(motifRange*11.5))
		cmd.select('asn3', 'name nd2 and resn asn within %s	of (name nh2 and resn arg)'%(motifRange*10.5))
		cmd.select('asn4', 'name od1 and resn asn within %s	of (name ne2 and resn his)'%(motifRange*7))
		cmd.select('asn5', 'name nd2 and resn asn within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asn6', 'name od1 and resn asn within %s	of (name cd2 and resn his)'%(motifRange*7))
		cmd.select('asn7', 'name cg and resn asn within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asn8', 'name od1 and resn asn within %s	of (name oh and resn tyr)'%(motifRange*7.5))
		cmd.select('asn9', 'name nd2 and resn asn within %s	of (name oh and resn tyr)'%(motifRange*7.5))
		cmd.select('asn10', 'name od1 and resn asn within %s	of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('asn11', 'name nd2 and resn asn within %s	of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')
		cmd.select('chondroitinase', 'asn(his(arg(tyr)))')
	
	def hyaluronlyase(self,motifRange):
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name nh2 and resn arg)'%(motifRange*6))
		cmd.select('tyr2', 'name oh and resn tyr within %s	of (name nh1 and resn arg)'%(motifRange*5))
		cmd.select('tyr3', 'name oh and resn tyr within %s	of (name cz and resn arg)'%(motifRange*6))
		cmd.select('tyr4', 'name oh and resn tyr within %s	of (name ne and resn arg)'%(motifRange*7))
		cmd.select('tyr5', 'name oh and resn tyr within %s	of (name ne2 and resn his)'%(motifRange*5))
		cmd.select('tyr6', 'name oh and resn tyr within %s	of (name nd1 and resn his)'%(motifRange*6))
		cmd.select('tyr7', 'name oh and resn tyr within %s	of (name ce1 and resn his)'%(motifRange*5))
		cmd.select('tyr8', 'name ce2 and resn tyr within %s	of (name nd1 and resn his)'%(motifRange*6))
		cmd.select('tyr9', 'name ce1 and resn tyr within %s	of (name ne2 and resn his)'%(motifRange*6))
		cmd.select('tyr10', 'name oh and resn tyr within %s	of (name od1 and resn asn)'%(motifRange*7.5))
		cmd.select('tyr11', 'name oh and resn tyr within %s	of (name nd2 and resn asn)'%(motifRange*7.5))
		cmd.select('tyr12', 'name ce1 and resn tyr within %s	of (name od1 and resn asn)'%(motifRange*6.5))
		cmd.select('tyr13', 'name ce1 and resn tyr within %s	of (name nd2 and resn asn)'%(motifRange*6))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7 and byres tyr8 and byres tyr9 and byres tyr10 and byres tyr11 and byres tyr12 and byres tyr13')
		cmd.select('his1', 'name ne2 and resn his within %s	of (name od1 and resn asn)'%(motifRange*7))
		cmd.select('his2', 'name ne2 and resn his within %s	of (name nd2 and resn asn)'%(motifRange*8))
		cmd.select('his3', 'name cd2 and resn his within %s	of (name od1 and resn asn)'%(motifRange*7))
		cmd.select('his4', 'name ne2 and resn his within %s	of (name cg and resn asn)'%(motifRange*8))
		cmd.select('his5', 'name ne2 and resn his within %s	of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('his6', 'name nd1 and resn his within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('his7', 'name ce1 and resn his within %s	of (name oh and resn tyr)'%(motifRange*5))
		cmd.select('his8', 'name nd1 and resn his within %s	of (name ce2 and resn tyr)'%(motifRange*6))
		cmd.select('his9', 'name ne2 and resn his within %s	of (name ce1 and resn tyr)'%(motifRange*6))
		cmd.select('his10', 'name ne2 and resn his within %s	of (name nh2 and resn arg)'%(motifRange*8))
		cmd.select('his11', 'name ce1 and resn his within %s	of (name cz and resn arg)'%(motifRange*7))
		cmd.select('his12', 'name nd1 and resn his within %s	of (name nh1 and resn arg)'%(motifRange*6.5))
		cmd.select('his13', 'name nd1 and resn his within %s	of (name cd and resn arg)'%(motifRange*9))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10 and byres his11 and byres his12 and byres his13')
		cmd.select('arg1', 'name nh2 and resn arg within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('arg2', 'name nh1 and resn arg within %s	of (name oh and tyr)'%(motifRange*6))
		cmd.select('arg3', 'name cz and resn arg within %s	of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('arg4', 'name ne and resn arg within %s	of (name oh and resn tyr)'%(motifRange*7))
		cmd.select('arg5', 'name nh2 and resn arg within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('arg6', 'name cz and resn arg within %s	of (name ce1 and resn his)'%(motifRange*7))
		cmd.select('arg7', 'name nh1 and resn arg within %s	of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('arg8', 'name cd and resn arg within %s	of (name nd1 and resn his)'%(motifRange*9))
		cmd.select('arg9', 'name nh1 and resn arg within %s	of (name od1 and resn asn)'%(motifRange*11))
		cmd.select('arg10', 'name cz and resn arg within %s	of (name cg and resn asn)'%(motifRange*12))
		cmd.select('arg11', 'name nh2 and resn arg within %s	of (name nd2 and resn asn)'%(motifRange*11.5))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10 and byre arg11')
		cmd.select('asn1', 'name od1 and resn asn within %s	of (name nh1 and resn arg)'%(motifRange*11))
		cmd.select('asn2', 'name cg and resn asn within %s	of (name cz and resn arg)'%(motifRange*11.5))
		cmd.select('asn3', 'name nd2 and resn asn within %s	of (name nh2 and resn arg)'%(motifRange*10.5))
		cmd.select('asn4', 'name od1 and resn asn within %s	of (name ne2 and resn his)'%(motifRange*7))
		cmd.select('asn5', 'name nd2 and resn asn within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asn6', 'name od1 and resn asn within %s	of (name cd2 and resn his)'%(motifRange*7))
		cmd.select('asn7', 'name cg and resn asn within %s	of (name ne2 and resn his)'%(motifRange*8))
		cmd.select('asn8', 'name od1 and resn asn within %s	of (name oh and resn tyr)'%(motifRange*7.5))
		cmd.select('asn9', 'name nd2 and resn asn within %s	of (name oh and resn tyr)'%(motifRange*7.5))
		cmd.select('asn10', 'name od1 and resn asn within %s	of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('asn11', 'name nd2 and resn asn within %s	of (name ce1 and resn tyr)'%(motifRange*6.5))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8 and byres asn9 and byres asn10 and byres asn11')
		cmd.select('Hyaluronate_Lyase', 'asn(his(arg(tyr)))')
	
	def ACTase(self,motifRange):
		showinfo('Info', 'This motif is based on sequence not position')
		cmd.select('gln', 'resi 231 and resn gln')
		cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
		cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
		cmd.select('his', 'resi 134 and resn his')
		cmd.select('lys', 'resi 84 and resn lys')
		cmd.select('ser', 'resi 80 and resn ser')
		cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')
	
	def ACTase2(self,motifRange):
		cmd.select('gln', 'resi 231 and resn gln')
		cmd.select('arg', 'resi 167 and resn arg(resi 229 and resn arg)')
		cmd.select('thr', 'resi 55 and resn thr(resi 53 and resn thr)')
		cmd.select('his', 'resi 134 and resn his')
		cmd.select('lys', 'resi 84 and resn lys')
		cmd.select('ser', 'resi 80 and resn ser')
		cmd.select('actase', 'gln(arg(thr(his(lys(ser)))))')
	
	def exonucleaseiii(self,motifRange):
		cmd.select('his1', 'name ne2 and resn his within %s of (name nd2 and resn asn)'%(motifRange*5.5))
		cmd.select('his2', 'name ne2 and resn his within %s of (name od1 and resn asn)'%(motifRange*6.5))
		cmd.select('his3', 'name ne2 and resn his within %s of (name cg and resn asn)'%(motifRange*5.5))
		cmd.select('his4', 'name cd2 and resn his within %s of (name cg and resn asn)'%(motifRange*5.5))
		cmd.select('his5', 'name nd1 and resn his within %s of (name cg and resn asn)'%(motifRange*6.5))
		cmd.select('his6', 'name ce1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
		cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*5))
		cmd.select('his8', 'name nd1 and resn his within %s of (name od1 and resn asp)'%(motifRange*5.5))
		cmd.select('his9', 'name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*5.5))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
		cmd.select('asp1', 'name od2 and resn asp within %s of (name ce1 and resn his)'%(motifRange*5.5))
		cmd.select('asp2', 'name od2 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
		cmd.select('asp4', 'name cg and resn asp within %s of (name nd1 and resn his)'%(motifRange*5.5))
		cmd.select('asp5', 'name od2 and resn asp within %s of (name nd2 and resn asn)'%(motifRange*5.7))
		cmd.select('asp6', 'name od1 and resn asp within %s of (name nd2 and resn asn)'%(motifRange*6))
		cmd.select('asp7', 'name od1 and resn asp within %s of (name od1 and resn asn)'%(motifRange*6))
		cmd.select('asp8', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7')
		cmd.select('asp9', 'byres resn asp within %s of asp8'%(motifRange*5.5))
		cmd.select('asp10', 'byres resn asp within %s of his'%(motifRange*5.5))
		cmd.select('asp', 'byres asp8 or (byres asp9 and byres asp10)')
		cmd.select('asn1', 'name nd2 and resn asn within %s of (name ne2 and resn his)'%(motifRange*5.5))
		cmd.select('asn2', 'name od1 and resn asn within %s of (name ne2 and resn his)'%(motifRange*6.5))
		cmd.select('asn3', 'name cg and resn asn within %s of (name ne2 and resn his)'%(motifRange*5.5))
		cmd.select('asn4', 'name cg and resn asn within %s of (name cd2 and resn his)'%(motifRange*5.5))
		cmd.select('asn5', 'name cg and resn asn within %s of (name nd1 and resn his)'%(motifRange*6.5))
		cmd.select('asn6', 'name nd2 and resn asn within %s of (name od2 and resn asp)'%(motifRange*5.7))
		cmd.select('asn7', 'name nd2 and resn asn within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('asn8', 'name od1 and resn asn within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('asn9', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5 and byres asn6 and byres asn7 and byres asn8')
		cmd.select('asn10', 'byres resn asn within %s of asn9'%(motifRange*8))
		cmd.select('asn11', 'byres resn asn within %s of his'%(motifRange*8))
		cmd.select('asn12', 'byres resn asn within %s of asp8'%(motifRange*6))
		cmd.select('asn', 'byres asn9 or (byres asn10 and byres asn11 and byres asn12)')
		cmd.select('Exonuclease3', 'his(asp(asn))')
	
	def cyclinkinase(self,motifRange):
		cmd.select('glu1', 'name oe2 and resn glu within %s of (name nz and resn lys)'%(motifRange*6.5))
		cmd.select('glu2', 'name oe1 and resn glu within %s of (name nz and resn lys)'%(motifRange*7))
		cmd.select('glu3', 'name cd and resn glu within %s of (name nz and resn lys)'%(motifRange*7))
		cmd.select('glu4', 'name oe1 and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
		cmd.select('glu5', 'name cd and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
		cmd.select('glu6', 'name oe1 and resn glu within %s of (name cd and resn lys)'%(motifRange*5.5))
		cmd.select('glu7', 'name oe2 and resn glu within %s of (name ce and resn lys)'%(motifRange*6))
		cmd.select('glu8', 'name oe1 and resn glu within %s of (name cg and resn lys)'%(motifRange*5.5))
		cmd.select('glu9', 'name oe1 and resn glu within %s of (name od1 and resn asp)'%(motifRange*10))
		cmd.select('glu10', 'name oe2 and resn glu within %s of (name od1 and resn asp)'%(motifRange*10))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9 and byres glu10')
		cmd.select('lys1', 'name nz and resn lys within %s of (name oe2 and resn glu)'%(motifRange*6.5))
		cmd.select('lys2', 'name nz and resn lys within %s of (name oe1 and resn glu)'%(motifRange*7))
		cmd.select('lys3', 'name nz and resn lys within %s of (name cd and glu)'%(motifRange*7))
		cmd.select('lys4', 'name ce and resn lys within %s of (name oe1 and resn glu)'%(motifRange*6))
		cmd.select('lys5', 'name ce and resn lys within %s of (name cd and resn glu)'%(motifRange*6))
		cmd.select('lys6', 'name cd and resn lys within %s of (name oe1 and resn glu)'%(motifRange*5.5))
		cmd.select('lys7', 'name ce and resn lys within %s of (name oe2 and resn glu)'%(motifRange*6))
		cmd.select('lys8', 'name cg and resn lys within %s of (name oe1 and resn glu)'%(motifRange*5.5))
		cmd.select('lys9', 'name nz and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('lys10', 'name nz and resn lys within %s of (name od2 and resn asp)'%(motifRange*6))
		cmd.select('lys11', 'name ce and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('lys12', 'name ce and resn lys within %s of (name od2 and resn asp)'%(motifRange*6.5))
		cmd.select('lys13', 'name cd and resn lys within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('lys14', 'name cd and resn lys within %s of (name od2 and resn asp)'%(motifRange*7))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8 and byres lys9 and byres lys10 and byres lys11 and byres lys12 and byres lys13 and byres lys14')
		cmd.select('asp1', 'name od1 and resn asp within %s of (name oe1 and glu)'%(motifRange*10))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name oe2 and glu)'%(motifRange*10))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name nz and lys)'%(motifRange*6))
		cmd.select('asp4', 'name od2 and resn asp within %s of (name nz and lys)'%(motifRange*6))
		cmd.select('asp5', 'name od1 and resn asp within %s of (name ce and lys)'%(motifRange*6))
		cmd.select('asp6', 'name od2 and resn asp within %s of (name ce and resn lys)'%(motifRange*6.5))
		cmd.select('asp7', 'name od1 and resn asp within %s of (name cd and resn lys)'%(motifRange*6))
		cmd.select('asp8', 'name od2 and resn asp within %s of (name cd and resn lys)'%(motifRange*7))
		cmd.select('asp9', 'name cg and resn asp within %s of (name cd and resn lys)'%(motifRange*7))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
		cmd.select('Cyclin_Kinase', 'lys(asp(glu))')
	
	def adenylatekinase(self,motifRange):
		#p-loop first
		cmd.select('lys1', 'name nz and resn lys within %s of (name n and resn gly)'%(motifRange*7.5))
		cmd.select('lys2', 'name cg and resn lys within %s of (name c and resn gly)'%(motifRange*6))
		cmd.select('lys3', 'name n and resn lys within %s of (name n and resn gly)'%(motifRange*5))
		cmd.select('lys4', 'name n and resn lys within %s of (resn gly)'%(motifRange*2))
		cmd.select('lys5', 'name c and resn lys within %s of (resn gly)'%(motifRange*2))
		cmd.select('lys6', 'name nz and resn lys within %s of (name od2 and resn asp)'%(motifRange*13))
		cmd.select('lys7', 'name nz and resn lys within %s of (name ne and resn arg)'%(motifRange*11))
		cmd.select('lys8', 'name nz and resn lys within %s of (name nh2 and resn arg)'%(motifRange*9.5))
		cmd.select('lys', 'byres lys1 and byres lys2 and byres lys3 and byres lys4 and byres lys5 and byres lys6 and byres lys7 and byres lys8')
		cmd.select('glya1', 'name n and resn gly within %s of (name nz and lys)'%(motifRange*7.5))
		cmd.select('glya2', 'name ca and resn gly within %s of (name cg and lys)'%(motifRange*7))
		cmd.select('glya3', 'name c and resn gly within %s of (name n and lys)'%(motifRange*2))
		cmd.select('glya4', 'name n and resn gly within %s of (name nh1 and resn arg)'%(motifRange*10))
		cmd.select('glya', 'byres glya1 and byres glya2 and byres glya3 and byres glya4')
		cmd.select('glyb', 'name n and resn gly within %s of (name c and lys)'%(motifRange*2))
		cmd.select('p-loop', 'lys(glya(byres glyb))')
		cmd.select('asp1', 'name od2 and resn asp within %s of (name ne and resn arg)'%(motifRange*5))
		cmd.select('asp2', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name nh1 and resn arg)'%(motifRange*5))
		cmd.select('asp4', 'name od2 and resn asp within %s of p-loop'%(motifRange*15))
		cmd.select('aspa', 'byres asp1 and byres asp2 and byres asp3 and byres asp4')
		cmd.select('aspb1', 'name od2 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5))
		cmd.select('aspb2', 'name cg and resn asp within %s of (name cz and resn arg)'%(motifRange*6))
		cmd.select('aspb3', 'name od1 and resn asp within %s of (name ne and resn arg)'%(motifRange*5))
		cmd.select('aspb4', 'name od2 and resn asp within %s of (name od1 and aspa)'%(motifRange*7))
		cmd.select('aspb5', 'name cg and resn asp within %s of (name cg and aspa)'%(motifRange*7))
		cmd.select('aspb6', 'name od1 and resn asp within %s of (name od2 and aspa)'%(motifRange*7))
		cmd.select('asp', 'byres aspb1 and byres aspb2 and byres aspb3 and byres aspb4 and byres aspb5 and byres aspb6')
		cmd.select('arg1', 'name nh1 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(motifRange*4.9))
		cmd.select('arg2', 'name nh2 and resn arg within %s of (name od1 and asp or name od2 and asp)'%(motifRange*4.9))
		cmd.select('arg', 'byres arg1 or byres arg2')
		cmd.select('adenylatekinase', 'p-loop(asp(aspa(arg)))')
	
	def citratesynth(self,motifRange):
		cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(motifRange*5))
		cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(motifRange*5.5))
		cmd.select('his3', 'name ce1 and resn his within %s of (name og and resn ser)'%(motifRange*5.5))
		cmd.select('his4', 'name ce1 and resn his within %s of (name cb and resn ser)'%(motifRange*6.5))
		cmd.select('his5', 'name cd2 and resn his within %s of (name og and resn ser)'%(motifRange*6))
		cmd.select('his6', 'name nd1 and resn his within %s of (name og and resn ser)'%(motifRange*7))
		cmd.select('his7', 'name nd1 and resn his within %s of (name od2 and resn asp)'%(motifRange*8))
		cmd.select('his8', 'name nd1 and resn his within %s of (name cg and resn asp)'%(motifRange*8.5))
		cmd.select('his9', 'name o and resn his within %s of (name od2 and resn asp)'%(motifRange*5.5))
		cmd.select('his10', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9')
		cmd.select('his11', 'byres resn his within %s of his10'%(motifRange*8.2))
		cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his10)'%(motifRange*5))
		cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his10)'%(motifRange*5.5))
		cmd.select('ser3', 'name og and resn ser within %s of (name ce1 and his10)'%(motifRange*5.5))
		cmd.select('ser4', 'name cb and resn ser within %s of (name ce1 and his10)'%(motifRange*6.5))
		cmd.select('ser5', 'name og and resn ser within %s of (name cd2 and his10)'%(motifRange*6))
		cmd.select('ser6', 'name og and resn ser within %s of (name nd1 and his10)'%(motifRange*7))
		cmd.select('ser7', 'name og and resn ser within %s of (name od2 and resn asp)'%(motifRange*12))
		cmd.select('ser8', 'name og and resn ser within %s of (name cg and resn asp)'%(motifRange*12))
		cmd.select('ser9', 'name og and resn ser within %s of (name od1 and resn asp)'%(motifRange*12))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
		cmd.select('his12', 'byres resn his within %s of ser'%(motifRange*12))
		cmd.select('asp1', 'name od2 and resn asp within %s of (name og and ser)'%(motifRange*12))
		cmd.select('asp2', 'name cg and resn asp within %s of (name og and ser)'%(motifRange*12))
		cmd.select('asp3', 'name od1 and resn asp within %s of (name og and ser)'%(motifRange*12))
		cmd.select('asp4', 'name od2 and resn asp within %s of (name nd1 and his10)'%(motifRange*8))
		cmd.select('asp5', 'name cg and resn asp within %s of (name nd1 and his10)'%(motifRange*8.5))
		cmd.select('asp6', 'name od2 and resn asp within %s of (name o and his10)'%(motifRange*5.5))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6')
		cmd.select('his13', 'byres resn his within %s of asp'%(motifRange*8.5))
		cmd.select('his', 'byres his10 or (byres his11 and byres his12 and byres his13)')
		cmd.select('Citrate_Synth', 'his(asp(ser))')
	
	def tyrosinekinase(self,motifRange):
		cmd.select('arg1', 'name nh1 and resn arg within %s of (name cb and resn ala)'%(motifRange*5))
		cmd.select('arg2', 'name nh2 and resn arg within %s of (name cb and resn ala)'%(motifRange*5.5))
		cmd.select('arg3', 'name cz and resn arg within %s of (name cb and resn ala)'%(motifRange*5.5))
		cmd.select('arg4', 'name ne and resn arg within %s of (name cb and resn ala)'%(motifRange*6))
		cmd.select('arg5', 'name nh2 and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('arg6', 'name nh2 and resn arg within %s of (name cg and resn asp)'%(motifRange*5.5))
		cmd.select('arg7', 'name nh2 and resn arg within %s of (name od2 and resn asp)'%(motifRange*6))
		cmd.select('arg8', 'name cz and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('arg9', 'name ne and resn arg within %s of (name od1 and resn asp)'%(motifRange*6))
		cmd.select('arg10', 'name ne and resn arg within %s of (name cg and resn asp)'%(motifRange*6.5))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9 and byres arg10')
		cmd.select('asp1', 'name od1 and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5.5))
		cmd.select('asp2', 'name cg and resn asp within %s of (name nh2 and resn arg)'%(motifRange*5.5))
		cmd.select('asp3', 'name od2 and resn asp within %s of (name nh2 and arg)'%(motifRange*7))
		cmd.select('asp4', 'name od1 and resn asp within %s of (name cz and resn arg)'%(motifRange*6))
		cmd.select('asp5', 'name od1 and resn asp within %s of (name ne and resn arg)'%(motifRange*6))
		cmd.select('asp6', 'name cg and resn asp within %s of (name ne and resn arg)'%(motifRange*6.5))
		cmd.select('asp7', 'name od1 and resn asp within %s of (name cb and resn ala)'%(motifRange*9))
		cmd.select('asp8', 'name o and resn asp within %s of (name cb and resn ala)'%(motifRange*8))
		cmd.select('asp9', 'name cg and resn asp within %s of (name cb and resn ala)'%(motifRange*8))
		cmd.select('asp', 'byres asp1 and byres asp2 and byres asp3 and byres asp4 and byres asp5 and byres asp6 and byres asp7 and byres asp8 and byres asp9')
		cmd.select('ala1', 'name cb and resn ala within %s of (name nh1 and arg)'%(motifRange*5))
		cmd.select('ala2', 'name cb and resn ala within %s of (name nh2 and arg)'%(motifRange*5.5))
		cmd.select('ala3', 'name cb and resn ala within %s of (name cz and arg)'%(motifRange*5.5))
		cmd.select('ala4', 'name cb and resn ala within %s of (name ne and arg)'%(motifRange*6))
		cmd.select('ala5', 'name cb and resn ala within %s of (name od1 and asp)'%(motifRange*9))
		cmd.select('ala6', 'name cb and resn ala within %s of (name o and asp)'%(motifRange*8))
		cmd.select('ala7', 'name cb and resn ala within %s of (name cg and asp)'%(motifRange*8))
		cmd.select('ala', 'byres ala1 and byres ala2 and byres ala3 and byres ala4 and byres ala5 and byres ala6 and byres ala7')
		cmd.select('SRC-Kinase', 'ala(asp(arg))')
	
	def hhal(self,motifRange):
		cmd.select('glu1', 'name oe2 and resn glu within %s of (name sg and resn cys)'%(motifRange*10))
		cmd.select('glu2', 'name cd and resn glu within %s of (name cb and resn cys)'%(motifRange*10))
		cmd.select('glu3', 'name oe1 and resn glu within %s of (name ca and resn cys)'%(motifRange*10))
		cmd.select('glu4', 'name oe2 and resn glu within %s of (name ne and resn arg)'%(motifRange*5))
		cmd.select('glu5', 'name cd and resn glu within %s of (name cz and resn arg)'%(motifRange*6))
		cmd.select('glu6', 'name oe1 and resn glu within %s of (name nh2 and resn arg)'%(motifRange*5))
		cmd.select('glu7', 'name cg and resn glu within %s of (name ca and resn phe)'%(motifRange*10))
		cmd.select('glu8', 'name cd and resn glu within %s of (name cb and resn phe)'%(motifRange*10))
		cmd.select('glu9', 'name ca and resn glu within %s of (name cd1 and resn phe)'%(motifRange*7.5))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4 and byres glu5 and byres glu6 and byres glu7 and byres glu8 and byres glu9')
		cmd.select('cys1', 'name sg and resn cys within %s of (name nh1 and resn arg)'%(motifRange*6))
		cmd.select('cys2', 'name cb and resn cys within %s of (name cz and resn arg)'%(motifRange*7))
		cmd.select('cys3', 'name ca and resn cys within %s of (name nh2 and resn arg)'%(motifRange*8))
		cmd.select('cys4', 'name sg and resn cys within %s of (name oe2 and glu)'%(motifRange*10))
		cmd.select('cys5', 'name cb and resn cys within %s of (name cd and glu)'%(motifRange*10))
		cmd.select('cys6', 'name ca and resn cys within %s of (name oe1 and glu)'%(motifRange*10))
		cmd.select('cys7', 'name ca and resn cys within %s of (name ca and resn phe)'%(motifRange*8.5))
		cmd.select('cys8', 'name cb and resn cys within %s of (name cd2 and resn phe)'%(motifRange*9))
		cmd.select('cys9', 'name sg and resn cys within %s of (name cd1 and resn phe)'%(motifRange*12))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5 and byres cys6 and byres cys7 and byres cys8 and byres cys9')
		cmd.select('arg1', 'name nh1 and resn arg within %s of (name sg and resn cys)'%(motifRange*6))
		cmd.select('arg2', 'name cz and resn arg within %s of (name cb and resn cys)'%(motifRange*7))
		cmd.select('arg3', 'name nh2 and resn arg within %s of (name ca and resn cys)'%(motifRange*8))
		cmd.select('arg4', 'name ne and resn arg within %s of (name oe2 and glu)'%(motifRange*5))
		cmd.select('arg5', 'name cz and resn arg within %s of (name cd and glu)'%(motifRange*6))
		cmd.select('arg6', 'name nh2 and resn arg within %s of (name oe1 and glu)'%(motifRange*5))
		cmd.select('arg7', 'name nh2 and resn arg within %s of (name ce1 and resn phe)'%(motifRange*10.5))
		cmd.select('arg8', 'name cz and resn arg within %s of (name cz and resn phe)'%(motifRange*11.5))
		cmd.select('arg9', 'name nh1 and resn arg within %s of (name ce2 and resn phe)'%(motifRange*12))
		cmd.select('arg', 'byres arg1 and byres arg2 and byres arg3 and byres arg4 and byres arg5 and byres arg6 and byres arg7 and byres arg8 and byres arg9')
		cmd.select('phe1', 'name ca and resn phe within %s of (name cg and glu)'%(motifRange*10))
		cmd.select('phe2', 'name cb and resn phe within %s of (name cb and glu)'%(motifRange*10))
		cmd.select('phe3', 'name cd1 and resn phe within %s of (name ca and glu)'%(motifRange*7.5))
		cmd.select('phe4', 'name ce1 and resn phe within %s of (name nh2 and resn arg)'%(motifRange*10.5))
		cmd.select('phe5', 'name cz and resn phe within %s of (name cz and resn arg)'%(motifRange*11.5))
		cmd.select('phe6', 'name ce2 and resn phe within %s of (name nh1 and resn arg)'%(motifRange*12))
		cmd.select('phe7', 'name ca and resn phe within %s of (name ca and cys)'%(motifRange*8.5))
		cmd.select('phe8', 'name cd2 and resn phe within %s of (name cb and cys)'%(motifRange*9))
		cmd.select('phe9', 'name cd1 and resn phe within %s of (name sg and cys)'%(motifRange*12))
		cmd.select('phe', 'byres phe1 and byres phe2 and byres phe3 and byres phe4 and byres phe5 and byres phe6 and byres phe7 and byres phe8 and byres phe9')
		cmd.select('hhal', 'glu(arg(phe(cys)))')
	
	def betainedehydrogenase(self,motifRange):
		cmd.select('cys1', 'name sg and resn cys within %s of (name od1 and resn asn)'%(motifRange*8.5))
		cmd.select('cys2', 'name cb and resn cys within %s of (name cg and resn asn)'%(motifRange*8.5))
		cmd.select('cys3', 'name ca and resn cys within %s of (name nd2 and resn asn)'%(motifRange*7.5))
		cmd.select('cys4', 'name sg and resn cys within %s of (name oe1 and resn glu)'%(motifRange*8))
		cmd.select('cys5', 'name cb and resn cys within %s of (name cb and resn glu)'%(motifRange*9))
		cmd.select('cys', 'byres cys1 and byres cys2 and byres cys3 and byres cys4 and byres cys5')
		cmd.select('glu1', 'name oe1 and resn glu within %s of (name sg and cys)'%(motifRange*8))
		cmd.select('glu2', 'name cb and resn glu within %s of (name cb and cys)'%(motifRange*9))
		cmd.select('glu3', 'name oe1 and resn glu within %s of (name nd2 and resn asn)'%(motifRange*13))
		cmd.select('glu4', 'name oe2 and resn glu within %s of (name od1 and resn asn)'%(motifRange*14))
		cmd.select('glu', 'byres glu1 and byres glu2 and byres glu3 and byres glu4')
		cmd.select('asn1', 'name nd2 and resn asn within %s of (name oe1 and glu)'%(motifRange*13))
		cmd.select('asn2', 'name od1 and resn asn within %s of (name oe2 and glu)'%(motifRange*14))
		cmd.select('asn3', 'name od1 and resn asn within %s of (name sg and cys)'%(motifRange*8.5))
		cmd.select('asn4', 'name cg and resn asn within %s of (name cb and cys)'%(motifRange*8.5))
		cmd.select('asn5', 'name nd2 and resn asn within %s of (name ca and cys)'%(motifRange*8.5))
		cmd.select('asn', 'byres asn1 and byres asn2 and byres asn3 and byres asn4 and byres asn5')
		cmd.select('betaine_dehydrogenase', 'cys(asn(glu))')
	
	def serotoninacetyl(self,motifRange):
		cmd.select('his1', 'name ne2 and resn his within %s of (name og and resn ser)'%(motifRange*4.5))
		cmd.select('his2', 'name ne2 and resn his within %s of (name cb and resn ser)'%(motifRange*5.5))
		cmd.select('his3', 'name cd2 and resn his within %s of (name og and resn ser)'%(motifRange*5.5))
		cmd.select('his4', 'name cd2 and resn his within %s of (name cb and resn ser)'%(motifRange*6))
		cmd.select('his5', 'name ne2 and resn his within %s of (name o and resn leu)'%(motifRange*6))
		cmd.select('his6', 'name ce1 and resn his within %s of (name cd1 and resn leu)'%(motifRange*10))
		cmd.select('his7', 'name ce1 and resn his within %s of (name cb and resn leu)'%(motifRange*9))
		cmd.select('his8', 'name nd1 and resn his within %s of (name og and resn ser)'%(motifRange*7.5))
		cmd.select('his9', 'name o and resn his within %s of (name oh and resn tyr)'%(motifRange*10))
		cmd.select('his10', 'name cb and resn his within %s of (name oh and resn tyr)'%(motifRange*12))
		cmd.select('his', 'byres his1 and byres his2 and byres his3 and byres his4 and byres his5 and byres his6 and byres his7 and byres his8 and byres his9 and byres his10')
		cmd.select('ser1', 'name og and resn ser within %s of (name ne2 and his)'%(motifRange*4.5))
		cmd.select('ser2', 'name cb and resn ser within %s of (name ne2 and his)'%(motifRange*5.5))
		cmd.select('ser3', 'name og and resn ser within %s of (name cd2 and his)'%(motifRange*5.5))
		cmd.select('ser4', 'name cb and resn ser within %s of (name cd2 and his)'%(motifRange*6))
		cmd.select('ser5', 'name og and resn ser within %s of (name nd1 and his)'%(motifRange*7.5))
		cmd.select('ser6', 'name og and resn ser within %s of (name o and resn leu)'%(motifRange*5))
		cmd.select('ser7', 'name og and resn ser within %s of (name cb and resn leu)'%(motifRange*8))
		cmd.select('ser8', 'name cb and resn ser within %s of (name o and resn leu)'%(motifRange*5.5))
		cmd.select('ser9', 'name n and resn ser within %s of (name cd2 and his)'%(motifRange*5.5))
		cmd.select('ser', 'byres ser1 and byres ser2 and byres ser3 and byres ser4 and byres ser5 and byres ser6 and byres ser7 and byres ser8 and byres ser9')
		cmd.select('leu1', 'name o and resn leu within %s of (name ne2 and his)'%(motifRange*6))
		cmd.select('leu2', 'name cd1 and resn leu within %s of (name ce1 and his)'%(motifRange*10))
		cmd.select('leu3', 'name cb and resn leu within %s of (name ce1 and his)'%(motifRange*9))
		cmd.select('leu4', 'name o and resn leu within %s of (name og and ser)'%(motifRange*5))
		cmd.select('leu5', 'name cb and resn leu within %s of (name og and ser)'%(motifRange*8))
		cmd.select('leu6', 'name o and resn leu within %s of (name cb and ser)'%(motifRange*5.5))
		cmd.select('leu7', 'name n and resn leu within %s of (name ce1 and resn his)'%(motifRange*7.5))
		cmd.select('leu8', 'byres leu1 and byres leu2 and byres leu3 and byres leu4 and byres leu5 and byres leu6 and byres leu7')
		cmd.select('leu9', 'name n and resn leu within %s of (name o and his)'%(motifRange*7))
		cmd.select('leu10', 'name n and resn leu within %s of (name c and his)'%(motifRange*6.5))
		cmd.select('leu11', 'name n and resn leu within %s of (name n and his)'%(motifRange*8))
		cmd.select('leu12', 'name cd1 and resn leu within %s of (name oh and resn tyr)'%(motifRange*6))
		cmd.select('leu13', 'name cb and resn leu within %s of (name oh and resn tyr)'%(motifRange*5.5))
		cmd.select('leu14', 'name cg and resn leu within %s of (name oh and resn tyr)'%(motifRange*7))
		cmd.select('leu15', 'name cd1 and resn leu within %s of (name cz and resn tyr)'%(motifRange*6.5))
		cmd.select('leu15b', 'name cd1 and resn leu within %s of (name ce1 and resn tyr)'%(motifRange*5.5))
		cmd.select('leu16', 'byres leu9 and byres leu15b and byres leu10 and byres leu11 and byres leu12 and byres leu13 and byres leu14 and byres leu15')
		cmd.select('tyr1', 'name oh and resn tyr within %s of (name cd1 and leu16)'%(motifRange*6))
		cmd.select('tyr2', 'name oh and resn tyr within %s of (name cb and leu16)'%(motifRange*6.5))
		cmd.select('tyr3', 'name oh and resn tyr within %s of (name cg and leu16)'%(motifRange*7))
		cmd.select('tyr4', 'name cz and resn tyr within %s of (name cd1 and leu16)'%(motifRange*6.5))
		cmd.select('tyr5', 'name oh and resn tyr within %s of (name n and his)'%(motifRange*10))
		cmd.select('tyr6', 'name cz and resn tyr within %s of (name c and his)'%(motifRange*10.2))
		cmd.select('tyr7', 'name ce1 and resn tyr within %s of (name o and ser)'%(motifRange*16))
		cmd.select('tyr', 'byres tyr1 and byres tyr2 and byres tyr3 and byres tyr4 and byres tyr5 and byres tyr6 and byres tyr7')
		cmd.select('Serotonin_transferase', 'his(ser(leu8(leu16(tyr))))')

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
			 
			 showinfo('Alert', 'You must select a motif')

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
		
		showinfo('Alert', "Select a motif first")
	
	
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
			
			showinfo('Alert', "No motif polar contacts to hide")
#develop spot

#substrate#
	
	def showsubstrate(self):
		try:
		try:
			
			cmd.select('substrate', 'byres het within 7 of '+self.mot)
			objects = cmd.get_names('all')
			xp = cmd.index('substrate')
			np	= len(xp)
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
			np	= len(xp)
			if(np < 1):
				cmd.delete('substrate')
			if 'substrate' in objects:
				cmd.show('sticks', 'substrate')
				cmd.deselect()
				cpksubstrate()
		except:
		
		showinfo('Alert', "No substrate found")
	
	def hidesubstrate(self):
		try:
		cmd.hide('sticks', 'substrate')
		except:
		
		showinfo('Alert', "No substrate selected")

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
		
		showinfo('Alert', "No motif labels to hide")
	
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
		
		showinfo('Alert', "Select a motif first")

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
			
			showinfo('Alert', 'There is no motif there')
	
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
			update()
			objects = cmd.get_names('all')
			checkitforthese()
			set_defaults()
			delcrea()
			cmd.delete('motif')
			cmd.hide('everything')
			mA = self.mA
			mB = self.mB
			cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
			cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
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
		
		showinfo('Alert', 'You must select an amino acid for menus A and B')
	
	def trimotif(self):
		try:
			update()
			objects = cmd.get_names('all')
			checkitforthese()
			set_defaults()
			delcrea()
			cmd.delete('motif')
			cmd.hide('everything')
			mA = self.mA
			mB = self.mB
			mC = self.mC
			cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
			cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
			cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
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
			
			showinfo('Alert', 'You must select an amino acid for menus A, B, and C')
	
	
	def quadmotif(self):
		try:
			update()
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
			cmd.do('sel AA, resn %s within %s of resn %s'%(mA, selA.get(), mB))
			cmd.do('sel BB, resn %s within %s of resn %s'%(mB, selA.get(), mA))
			cmd.do('sel CC, resn %s within %s of resn %s'%(mC, selB.get(), mB))
			cmd.do('sel DD, resn %s within %s of resn %s'%(mD, selC.get(), mC))
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
			
			showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')
	
	def Abimotif(self):
		try:
			update()
			objects = cmd.get_names('all')
			checkitforthese()
			set_defaults()
			delcrea()
			cmd.delete('motif')
			cmd.hide('everything')
			mAA = self.mAA
			mAB = self.mAB
			cmd.do('sel AA, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
			cmd.do('sel BB, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
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
		
		showinfo('Alert', 'You must select an amino acid for menus A and B')
	
	def Atrimotif(self):
		try:
			update()
			objects = cmd.get_names('all')
			checkitforthese()
			set_defaults()
			delcrea()
			cmd.delete('motif')
			cmd.hide('everything')
			mAA = self.mAA
			mAB = self.mAB
			mAC = self.mAC
			cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
			cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
			cmd.select('AA', 'byres AA1 and byres AA2')
			cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
			cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
			cmd.select('BB', 'byres BB1 and byres BB2')
			cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
			cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
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
			
			showinfo('Alert', 'You must select an amino acid for menus A, B, and C')
	
	
	def Aquadmotif(self):
		try:
			update()
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
			cmd.do('sel AA1, resn %s within %s of resn %s'%(mAA, selAB.get(), mAB))
			cmd.select('AA2', 'resn %s within %s of resn %s'%(mAA, selAC.get(), mAC))
			cmd.select('AA3', 'resn %s within %s of resn %s'%(mAA, selAD.get(), mAD))
			cmd.select('AA', 'byres AA1 and byres AA2 and byres AA3')
			cmd.do('sel BB1, resn %s within %s of resn %s'%(mAB, selAB.get(), mAA))
			cmd.select('BB2', 'resn %s within %s of resn %s'%(mAB, selBC.get(), mAC))
			cmd.select('BB3', 'resn %s within %s of resn %s'%(mAB, selBD.get(), mAD))
			cmd.select('BB', 'byres BB1 and byres BB2 and byres BB3')
			cmd.do('sel CC1, resn %s within %s of resn %s'%(mAC, selBC.get(), mAB))
			cmd.select('CC2', 'resn %s within %s of resn %s'%(mAC, selAC.get(), mAA))
			cmd.select('CC3', 'resn %s within %s of resn %s'%(mAC, selCD.get(), mAD))
			cmd.select('CC', 'byres CC1 and byres CC2 and byres CC3')
			cmd.do('sel DD1, resn %s within %s of resn %s'%(mAD, selAD.get(), mAA))
			cmd.select('DD2', 'resn %s within %s of resn %s'%(mAD, selBD.get(), mAB))
			cmd.select('DD3', 'resn %s within %s of resn %s'%(mAD, selCD.get(), mAC))
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
			
			showinfo('Alert', 'You must select an amino acid for menus A, B, C, and D')
	
	#reset the range sliders
	def resetmotif(self):
		selA.set(4.0)
		selB.set(4.0)
		selC.set(4.0)
		selAB.set(4.0)
		selAC.set(4.0)
		selAD.set(4.0)
		selBC.set(4.0)
		selBD.set(4.0)
		selCD.set(4.0)
	
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
	#						 #
	#COMMANDS" TAB METHODS	#
	#																	 #
	#--------------------------------------#
	# Color the molecule
	def color_cpk(self, str ):
		color_cpk()
	
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
	cpkligands()
	cmd.deselect()
	
	# create additional colors
	# (adopted from some code written by
	#	Kevin Galens and Jamie Duke at RIT)
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
		try:
			sel = sel
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
			elif tag=='Polar Contacts':
				cmd.dist(sel+"_polar_conts",sel,sel,quiet=1,mode=2,label=0,reset=1)
				cmd.enable(sel+"1CHO_polar_conts")		
		except:
			showinfo('Error', 'Update Selection!')
	
	
	# Hide individual representations
	def hide_rep(self, tag):
		try:
			sel = sel
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
			elif tag =='Polar Contacts':
				cmd.delete(sel+"_polar_conts")
			except:
				showinfo('Error', 'Update Selection!')
	 
	 
	 #-------------Version 2--------------#
	
	# Set selection of atoms
	#	 - initial selection is 'all'
	def set_sel(self, tag):
		cmd.deselect()
		c=re.compile("^Chain")
		if tag=='All':
				sel = 'all'
		elif tag=='protein':
				sel = 'protein'
		elif tag=='nucleic_acid':
				sel = 'nucleic_acid'
		elif tag=='ligands':
				sel = 'ligands'
		elif tag=='heme':
				sel = 'heme'
		elif tag=='Chain-A':
			sel=('Chain-A')
		elif tag=='Chain-A':
			sel=('Chain-A')
		elif tag=='Chain-B':
			sel=('Chain-B')
		elif tag=='Chain-C':
			sel=('Chain-C')
		elif tag=='Chain-D':
			sel=('Chain-D')
		elif tag=='Chain-E':
			sel=('Chain-E')
		elif tag=='Chain-F':
			sel=('Chain-F')
		elif tag=='Chain-G':
			sel=('Chain-G')
		elif tag=='Chain-H':
			sel=('Chain-H')
		elif tag=='Chain-I':
			sel=('Chain-I')
		elif tag=='Chain-J':
			sel=('Chain-J')
		elif tag=='Chain-K':
			sel=('Chain-K')
		elif tag=='Chain-L':
			sel=('Chain-L')
		elif tag=='Chain-M':
			sel=('Chain-M')
		elif tag=='Chain-N':
			sel=('Chain-N')
		elif tag=='Chain-O':
			sel=('Chain-O')
		elif tag=='Chain-P':
			sel=('Chain-P')
		elif tag=='Chain-Q':
			sel=('Chain-Q')
		elif tag=='Chain-R':
			sel=('Chain-R')
		elif tag=='Chain-S':
			sel=('Chain-S')
		elif tag=='Chain-T':
			sel=('Chain-T')
		elif tag=='Chain-U':
			sel=('Chain-U')
		elif tag=='Chain-V':
			sel=('Chain-V')
		elif tag=='Chain-W':
			sel=('Chain-W')
		elif tag=='Chain-X':
			sel=('Chain-X')
		elif tag=='Chain-Y':
			sel=('Chain-Y')
		elif tag=='Chain-Z':
			sel=('Chain-Z')
		elif tag=='Not Selected':
		try:
				cmd.select('selection', '!sele')
				cmd.deselect()
				sel= 'selection'
		except:
			
			showinfo("Error", 'No selection has been made')
		elif tag=='hydrophobic':
				sel='hydrophobic'
		elif tag=='hydrophilic':
				sel='hydrophilic'
		elif tag=='acidic':
				sel='acidic'
		elif tag=='basic':
				sel='basic'
	
	# Set selection of atoms
	#	 - initial selection is 'all'
	
	def set_sel1(self, tag):
		cmd.deselect()
		c=re.compile("^Chain")
		if tag=='All':
				sel1 = 'all'
		elif tag=='protein':
				sel1 = 'protein'
		elif tag=='nucleic_acid':
				sel1 = 'nucleic_acid'
		elif tag=='ligands':
				sel1 = 'ligands'
		elif tag=='heme':
				sel1 = 'heme'
		elif tag=='Chain-A':
			sel1=('Chain-A')
		elif tag=='Chain-A':
			sel1=('Chain-A')
		elif tag=='Chain-B':
			sel1=('Chain-B')
		elif tag=='Chain-C':
			sel1=('Chain-C')
		elif tag=='Chain-D':
			sel1=('Chain-D')
		elif tag=='Chain-E':
			sel1=('Chain-E')
		elif tag=='Chain-F':
			sel1=('Chain-F')
		elif tag=='Chain-G':
			sel1=('Chain-G')
		elif tag=='Chain-H':
			sel1=('Chain-H')
		elif tag=='Chain-I':
			sel1=('Chain-I')
		elif tag=='Chain-J':
			sel1=('Chain-J')
		elif tag=='Chain-K':
			sel1=('Chain-K')
		elif tag=='Chain-L':
			sel1=('Chain-L')
		elif tag=='Chain-M':
			sel1=('Chain-M')
		elif tag=='Chain-N':
			sel1=('Chain-N')
		elif tag=='Chain-O':
			sel1=('Chain-O')
		elif tag=='Chain-P':
			sel1=('Chain-P')
		elif tag=='Chain-Q':
			sel1=('Chain-Q')
		elif tag=='Chain-R':
			sel1=('Chain-R')
		elif tag=='Chain-S':
			sel1=('Chain-S')
		elif tag=='Chain-T':
			sel1=('Chain-T')
		elif tag=='Chain-U':
			sel1=('Chain-U')
		elif tag=='Chain-V':
			sel1=('Chain-V')
		elif tag=='Chain-W':
			sel1=('Chain-W')
		elif tag=='Chain-X':
			sel1=('Chain-X')
		elif tag=='Chain-Y':
			sel1=('Chain-Y')
		elif tag=='Chain-Z':
			sel1=('Chain-Z')
		elif tag=='Not Selected':
				cmd.select('selection', '!sele')
				cmd.deselect()
				sel1= 'selection'
		elif tag=='hydrophobic':
				sel1='hydrophobic'
		elif tag=='hydrophilic':
				sel1='hydrophilic'
		elif tag=='acidic':
				sel1='acidic'
		elif tag=='basic':
				sel1='basic'
	
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
			
			showinfo('Error', 'Invalid command or you must load the PDB through Pro-MOL')
	
	# Coloring on Selection
	def color_sel(self, tag):
		try:
			sel=sel
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
					cmd.color("oxygen","(elem O and "+sel+")")
					cmd.color("nitrogen","(elem N and "+sel+")")
					cmd.color("sulfur","(elem S and "+sel+")")
					cmd.color("hydrogen","(elem H and "+sel+")")
					cmd.color("gray","(elem C and "+sel+")")
			elif tag=='Other':
					color=askcolor(parent=self.int, title="Selection Color Chooser")
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
			
			showinfo('Error', 'Update Selection!')


	
	
	#------------------Version 2-----------------#
	
	#--------------------------------------#
	#						 #
	#			 SAVE	 METHODS			 #
	#										#
	#--------------------------------------#
	def imgSave(self):
		
		file = asksaveasfilename(defaultextension=".png", initialdir="./PyMOL/")
		if len(file)>0:
			cmd.save(file)
	
	
	#------
	#Brett and Charlie's (first attempt) code--------
	#--Ray tracing with an auto calculator for height and width----
	def imgraysave(self):
		
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
			
			
			showinfo("Help","To save a higher resolution image you \nmust input width and height paramaters.\n \nOr input just width or just height and\n use the Auto Calc button to get the other.\n\n Paramaters should be under 5 digits\n or else Ray Trace may take a long time. \n \nThen click Save to save your image.")
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
				
				
				showinfo("Error", "Enter an integer value for width or height")
				root.mainloop()
		c_button.bind('<Button-1>',autocalc)
		#Defines ray trace function
		def raytrace(event):
			try:
				if len(name1.get()) > 3:
					
					
					showinfo("Ray Trace","You have entered a large value. Please be patient.\nClick OK to continue.")
					cmd.ray(name1.get(),name2.get())
					root.mainloop()
				else:
					cmd.ray(name1.get(),name2.get())
					root.mainloop()
			except:
				
				
				showinfo("Error", "Enter an integer value for width and height")
				root.mainloop()
		def savestop(event):
			file = asksaveasfilename(defaultextension=".png", initialdir="./PyMOL/")
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
	#						 #
	#		 UTILITY	METHODS			 #
	#										#
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
		labels = btn_labels	 #the list of labels passed in by the user
		
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
		space = Label(frame, text='			')
		space.grid(row=gridrow, column=gridcol)
	
	#--------------------------------------#
	#						 #
	#		 Display		METHODS		 #
	#										#
	#--------------------------------------#
	# handle stereo commands
	def stereo_switch(self, tag):
		if tag == 'Off':
			cmd.stereo('off')
		elif tag == 'Quad':
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
			color=askcolor(parent=self.int, title="Background Color Chooser")
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
	
	#--------------------------------------#
	#				#
	#		 PARSING	METHODS			 #
	#																	 #
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
	#						 #
	#			 MOVIE METHODS				#
	#										#
	#--------------------------------------#
	def rotate_y(*args):
		cmd.mset()
		cmd.mset('1','180')
		cmd.util.mroll('1','180','1')
		cmd.mplay()
	cmd.extend('rotate',rotate_y)
	
	
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
			
			cmd.mstop()
			cmd.mclear()
			cmd.mset()
			q=360
			ids = self.p.idList
			if len(ids)==0:
				showinfo("Ligand Zoom", "Sorry this PDB file contains no ligands and cannot be made into a movie")
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
					cmd.do('mdo '+str((q+1))+':set sphere_transparency, 0.1, ligands; set cartoon_transparency, 0.9, all;	show spheres, (ligands and '+ids[i]+'); show sticks, (ligands and '+ids[i]+');')
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
			
			showinfo('Error', 'You must open the PDB file through Pro-MOL')
	
	cmd.extend('ligand_zoom',ligandZoom)
	 #fixed to work on externally loaded pdbs by Brett and Charlie
	def growProtein(*args):
		delcrea()
	 	cmd.mstop()
	cmd.mclear()
	cmd.mset()
		
		try:
			self = args[0]
			update()
		except:
			pass
		
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
	cmd.extend('build_protein', growProtein)


		
		
		#---------Version 2--------#
	
	#--------Haven't you seeen my MOVIES!-----------
	#surface over cartoon movie
	def surface_cartoon(*args):
			delcrea()
			try:
			self = args[0]
			update()
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
		update()
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
		
		
		#movie that pulls ligands out of	and puts them back in
	def Ligand_Pull(*args):
			delcrea()
			try:
			update()
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
			update()
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
	 	
	 	if state:
	 		if askyesno('Ray Trace Frames', 'Enabling this feature may '+
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
#						All Rights Reserved
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
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.	IN
# NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------
	
	
	def getPdb(self):
		
		if self.fileLoaded ==' ':
			pdbCode = askstring('PDB Loader Service',
										 'Please enter a 4-digit pdb code:')
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
			update()
			cmd.deselect()
		 
		 else:
			showerror('Invalid Code',
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
	#					 GUI CREATION METHOD						 #
	#					(INIT)		#
	#						#
	#						#
	#				 create and organize the interface				#
	#						#
	#---------------------------------------------------------------#
	def __init__(self, pymol, userClick):	
		# create the dialog box which contains the GUI
		parent = pymol.root
		self.dialog = Pmw.Dialog(parent,buttons = ('Open','Fetch PDB','Clear','Help', 'Thanks' ,'Quit'),
						title = 'Pro-MOL',command = self.execute)
		if(!userClick):
			self.execute('Quit')
		self.converter = ChimeConverter()
		
		# initialize the additional colors
		self.init_color()
		sel1='all'
	 	interior = self.dialog.interior()
 		#TITLE BAR
 		lab = Label(interior,
 			text='ProMol \nDeveloped By: Charlie Westin, Brett Hanson & Paul Craig\nVersion 3.02, 2007',
 			background='#000066', foreground='white')
 		lab.pack(expand=0, fill='x', padx=4, pady=0)
		
		# Create the notebook to hold the tabs
		notebook = Pmw.NoteBook(interior)
		notebook.pack(fill='both', expand=1, padx=10, pady=10)
		from Tabs import welcome, batch-motif, ez-viz, motifs, custom-motifs, motif-maker, view, toolbox, advanced-toolbox, movie-maker
 		notebook.setnaturalsize()

	#--------------------------------------#
	#									 #
	#	 HANDLE BUTTONS AT BOTTOM OF GUI	#
	#	(open, fetch.., help, exit)		 #
	#--------------------------------------#
	def execute(self, result):
		if result == 'Open':
			file=askopenfilename(initialdir='./PyMol')
			if file:
				cmd.load(file)
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
	def update(self):
		chainList=['All','Ligands','Not Selected','Hydrophobic','Hydrophilic']
		cmd.disable('protein')
		cmd.select('nucleic_acid', 'resn a+g+c+t+u')
		cmd.disable('nucleic_acid')
		cmd.select('ligands', 'het')
		cmd.disable('ligands')
		cmd.remove('resn HOH')
		populate()
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
	#					#
	#		"ADVANED" TAB METHODS	#
	#																		#
	#-------------------------------------------#
	
	#------------------------------------------#
	#				Cartoon Functions					#
	#------------------------------------------#
	
	# Set Cartoon Thickness
	def cartoon_thickness(self):
		self.populate()
		sel1 = ''
		value = self.toonThickness.get()
		cmd.set('cartoon_rect_width', value, 'all') # strands
		cmd.set('cartoon_oval_width', value, 'all') # helices
	
	
	# Set Cartoon Width
	def cartoon_width(self):
		self.populate()
		sel1 = ''
		value = self.toonWidth.get()
		cmd.set('cartoon_rect_length', value, 'all') # strands
		cmd.set('cartoon_oval_length', value, 'all') # helices
	
	# Set Cartoon Transparency
	def cartoon_transparency(self):
		self.populate()
		sel1 = ''
		amount=self.cartoonTransparency.get()
		cmd.set('cartoon_transparency', amount, 'all')
	
	# Set Cartoon Tube Radius
	def cartoon_tube_radius(self):
		self.populate()
		sel1 = ''
		value = self.toonTubeRadius.get()
		cmd.set('cartoon_tube_radius', value, 'all') # strands
	
	#Set Ribbon Type
	def ribType(self,tag):
		try:
			try:
				if tag == 'Skip':
						cmd.cartoon('skip', sel1)
				elif tag == 'Automatic':
						cmd.cartoon('automatic', sel1)
				elif tag == 'Oval':
						cmd.cartoon('oval', sel1)
				elif tag == 'Tube':
						cmd.cartoon('tube', sel1)
				elif tag == 'Rectangle':
						cmd.cartoon('rectangle', sel1)
				elif tag == 'Loop':
						cmd.cartoon('loop', sel1)
				elif tag == 'Arrow':
						cmd.cartoon('arrow', sel1)
				elif tag == 'Dumbbell':
						cmd.cartoon('dumbbell', sel1)
				elif tag == 'Putty':
						cmd.cartoon('putty', sel1)
			except:
				self.populate()
				if tag == 'Skip':
						cmd.cartoon('skip', sel1)
				elif tag == 'Automatic':
						cmd.cartoon('automatic', sel1)
				elif tag == 'Oval':
						cmd.cartoon('oval', sel1)
				elif tag == 'Tube':
						cmd.cartoon('tube', sel1)
				elif tag == 'Rectangle':
						cmd.cartoon('rectangle', sel1)
				elif tag == 'Loop':
						cmd.cartoon('loop', sel1)
				elif tag == 'Arrow':
						cmd.cartoon('arrow', sel1)
				elif tag == 'Dumbbell':
						cmd.cartoon('dumbbell', sel1)
				elif tag == 'Putty':
						cmd.cartoon('putty', sel1)
		except:
			
			showinfo('Error', 'Drop down menu is set to an invalid selection\nYou may need to update selections')
	
	#------------------------------------------#
	#				 Sphere Functions			 #
	#------------------------------------------#
	# Set Sphere Transparency
	def sphere_transparency(self):
		self.populate()
		sel1 = 'all'
		amount=self.sphereTransparency.get()
		cmd.set('sphere_transparency', amount, 'all')
	
	# Set Sphere Size
	def sphereSize(self):
		self.populate()
		sel1 = 'all'
		size=self.sphereScale.get()
		cmd.set('sphere_scale', size, 'all')
	
	#------------------------------------------#
	#				Surface	Functions			#
	#------------------------------------------#
	# Set Surface Transparency
	def surface_transparency(self):
		self.populate()
		sel1 = 'all'
		amount=self.surfaceTransparency.get()
		cmd.set('transparency', amount, 'all')
	
	#------------------------------------------#
	#				Stick	Functions			#
	#------------------------------------------#
	# Set Stick Transparency
	def stick_transparency(self):
		self.populate()
		sel1 = 'all'
		amount=self.stickTransparency.get()
		cmd.set('stick_transparency', amount, 'all')
	 
	 # Set Stick Radius
	def stickRad(self):
		self.populate()
		sel1 = 'all'
		size=self.stickRadius.get()
		cmd.set('stick_radius',size, 'all')
	 
		 #------------------------------------------#
		#			 Set Default Values						#
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
			cmd.cartoon('automatic',sel1)
			self.toonWidth.set('1.4')
			self.toonThickness.set('0.3')
			self.cartoonTransparency.set('0.0')
			self.toonTubeRadius.set('0.5')
			self.ribbonTypes.invoke(0)
		
		elif tag == 'spheres':
		
			cmd.set('sphere_scale','0.7','all')
			cmd.set('sphere_transparency','0.0','all')
			self.sphereScale.set('0.7')
			self.sphereTransparency.set('0.0')

		
		elif tag == 'sticks':
		
			cmd.set('stick_radius','0.2','all')
			cmd.set('stick_transparency','0.0','all')
			self.stickRadius.set('0.2')
			self.stickTransparency.set('0.0')
		
		elif tag == 'surface':
			# apply the changes
			cmd.set('transparency','0.0','all')
			self.surfaceTransparency.set('0.0')
		
		elif tag == 'ambient':
			cmd.set('ambient', '0.25', 'all')
			self.asca.set('0.25')
	cmd.extend('set_advanced_defaults',set_advanced_defaults)
			
			
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
		checkitforthese()
		for each in letters:
			cmd.select("Chain-" + each, "chain " + each)
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
		
		sel1 = 'All'
		sel = 'All'
		items.sort()
		selection.setitems(items)
		self.advancedSelection.setitems(items)
	
	#-------The End------for now....
def write_script(tag):
	if tag == 'Off':
	script ='0'
	if tag=='On': #write a scritp
	try:
		script = '1'
		Q = asksaveasfilename(defaultextension=".py", initialdir="./modules/pmg_tk/startup/Scripts")
		cmd.do('log_open %s,a'%(Q))
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
	delcrea()
cmd.extend('set_defaults',set_defaults)

def checkforchain():
	objects = cmd.get_names('all')
	if 'Chain-A' in objects:
		x1 = cmd.index('Chain-A')
		n1	= len(x1)
		if(n1 < 1):
			cmd.delete('Chain-A')
	if 'Chain-' '' in objects:
		x26 = cmd.index('Chain-' '')
		n26 = len(x26)
		if(n26 < 1):
			cmd.delete('Chain-' '')
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
		na	= len(xa)
		if(na < 1):
			cmd.delete('ligands')
	if 'nucleic_acid' in objects:
		xb = cmd.index('nucleic_acid')
		nb = len(xb)
		if(nb < 1):
			cmd.delete('nucleic_acid')
	if 'protein' in objects:
		xc = cmd.index('protein')
		nc = len(xc)
		if(nc < 1):
			cmd.delete('protein')
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
	if 'acidic' in objects:
		xe = cmd.index('acidic')
		ne = len(xe)
		if(ne < 1):
			cmd.delete('acidic')
	if 'basic' in objects:
		xg = cmd.index('basic')
		ng = len(xg)
		if(ng < 1):
			cmd.delete('basic')
	if 'heme' in objects:
		xh = cmd.index('heme')
		nh = len(xh)
		if(nh < 1):
			cmd.delete('heme')
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

def populate(*args):
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
	checkitforthese()
	for each in letters:
		cmd.select("Chain-" + each, "chain " + each)

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
	for i in range(len(letters)):
	if 'Chain-' + letters[i] in objects:
		items.append('Chain-' + letters[i])
	
	sel1 = 'All'
	sel = 'All'
	items.sort()
	#selection.setitems(items)
	#self.advancedSelection.setitems(items)
cmd.extend('populate',populate)


def update():
	chainList=['All','Ligands','Not Selected','Hydrophobic','Hydrophilic']
	cmd.disable('protein')
	cmd.select('nucleic_acid', 'resn a+g+c+t+u')
	cmd.disable('nucleic_acid')
	cmd.select('ligands', 'het')
	cmd.disable('ligands')
	cmd.remove('resn HOH')
	populate()
	checkitforthese()
	cmd.orient('all')
cmd.extend('update',update)
