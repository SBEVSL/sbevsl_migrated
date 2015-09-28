from pymol import cmd
from pymol import stored
from pymol import CmdException ### going to be catching this one in the process
import Tkinter as tk
import Pmw
import os
import re
import time
import math
import tkFileDialog
from shutil import copy
from tkFileDialog import asksaveasfile, askdirectory, askopenfile, askopenfilename
from tkSimpleDialog import askstring
from tkColorChooser import askcolor
from tkMessageBox import showinfo, showerror, askyesno
from collections import OrderedDict
from Tkinter import *
from pmg_tk.startup.treewidgets import widget, node, texttree
from pmg_tk.startup.treewidgets.constants import *
import Tkinter as tk
import pmg_tk.startup.ProMol.promolglobals as glb
import pmg_tk.startup.ProMol.load_csa_lit as lib
import pmg_tk.startup.ProMol.Methods.proutils as proutils
import pmg_tk.startup.ProMol.Methods.motifset as motifset
INDIVIDUAL_CSV_HEADER_LENGTH = 7
CSVMergeInfo = {}
numResultsOfEachQuery = []
orderedMotif = []
pdbsl = 0
Pmw.initialise()

class AutoMotifMaker:

    ms_atoms = 0

    atomlist = {}
    ### backbone off aka just side chains from beta carbon onwards
    atomlist[0] = {'ala':('CB',), # First comma added by Kip to make it a tuple
                   'arg':('CB','CG','CD','NE','CZ','NH1','NH2'),
                   'asn':('CB','CG','OD1','ND2'),
                   'asp':('CB','CG','OD1','OD2'),
                   'cys':('CB','SG'),
                   'gln':('CB','CG','CD','OE1','NE2'),
                   'glu':('CB','CG','CD','OE1','OE2'),
                   'gly':(),
                   'his':('CB','CG','ND1','CD2','CE1','NE2'),
                   'ile':('CB','CG1','CG2','CD1'),
                   'leu':('CB','CG','CD1','CD2'),
                   'lys':('CB','CG','CD','CE','NZ'),
                   'met':('CB','CG','SD','CE'),
                   'phe':('CB','CG','CD1','CD2','CE1','CE2','CZ'),
                   'pro':('CB','CG','CD'),
                   'ser':('CB','OG'),
                   'thr':('CB','OG1','CG2'),
                   'trp':('CB','CG','CD1','CD2','NE1','CE2','CE3','CZ2','CZ3','CH2'),
                   'tyr':('CB','CG','CD1','CD2','CE1','CE2','CZ','OH'),
                   'val':('CB','CG1','CG2'),
                   'mg':('MG',),
                   'zn':('ZN',),
                   'mn':('MN',),
                   'na':('NA',),
                   'hem':('FE','CHA','CHB','CHC','CHD','NA','C1A','C2A','C3A','C4A','CMA','CAA','CBA','CGA','O1A','O2A','NB','C1B','C2B','C3B','C4B','CMB','CAB','CBB','NC','C1C','C2C','C3C','C4C','CMC','CAC','CBC','ND','C1D','C2D','C3D','C4D','CMD','CAD','CBD','CGD','O1D','O2D'),
                   'co':('CO',),
                   'ni':('NI',),
                   'fe':('FE',),
                   'cu':('CU',)}
    atomlist[1] = ('O','C','CA','N') ### backbone on
    
    def __init__(self):
        pass

    def automate(self):
    
        # Hide the PyMOL viewer window
        # This not only increases the search speed, sometimes significantly,
        # but also may prevent the user from accidentally interfering with
        # automatic selections
        cmd.window('hide')
    
        # Text file to contain information about generated motifs, i.e., motif definition,
        # backbone and tolerance parameters. The report indicates if the motif was not saved.
        # An example of the report file entry (the ">" header lines: pdb [1jms], tolerance [1.2], 
		# number of chains on which the motif was found [1], ec code [2.7.7.31]; 
		# subsequent lines: residue name, chain, residue number, and whether the bbn was on or off):
        # >	1jms	1.2	1	2.7.7.31
        # NA	A	702	Off
        # MG	A	701	Off
        # ASP	A	434	On		
        reportfile = open(glb.pathmaker(('report','.txt'),root=glb.AUTOMOTIFSFOLDER), 'w')
        
		# List of PDB IDs for which the program will attempt to generate auto motifs:
        pdblist = lib.getPDBlist()
		
		# Auto generate the motifs for for the pdb id list 
        self.autoGenerate(pdblist, reportfile)
        reportfile.close()

        cmd.window('show')
        print ' ...done :)'
    
	# A function that tells id the residue is a metal ion
    def isMetal(self, res):
        metals = ('MG','ZN','MN','NA','HEM','CO','NI','FE','CU')
        if res in metals:
            return True
        else:
            return False		
	
	# This is the main function here, calls all others. It loads the motifs from the library,
	# orders the residue in the order of decreasing pairwise distance and calls the motif testing
	# and saving functions which were borrowed from motif.py module.  
    def autoGenerate(self, pdblist, reportfile):

        pdblistlen = len(pdblist)
        
        for i in range(0, pdblistlen):
            glb.GUI.motif_maker['selfTest'].select()
            motifstr = [] ### to be compared with matching subset
            saved = False
        
            id = pdblist[i]
            ecnum = lib.getEcNumber(id)
            
            if ecnum.startswith('0'):
                ecnum = '7.0.0.0' ### a fictional EC number
            
            if ecnum != 'N/A':
                print ' Generating motif ',i+1,' of ',pdblistlen,' on ',id
                glb.GUI.motif_maker['pdb'].delete(0, END)
                glb.GUI.motif_maker['pdb'].insert(END, id)
                print ' Acquiring library information...'
                self.getLibraryMotif()
                
                ### motif maker on self
                print ' Testing motif on ',id,' ...' 
                self.testAutoMotif()
                motif = lib.getMotif(id)
				
                for res in motif:
                    resn = res[0]
                    resi = res[1]
                    resstr = resn + ' ' + resi
                    motifstr.append(resstr)
                
                print 'Motif String: ',str(motifstr)
                
				### a section of PDB file describing the matching subset:
                pdbstr = cmd.get_pdbstr('matching_subset')
				
				### a string representation of the matching subset to be compared to the
				### string representation of the motif:
                msstr = self.process_pdbstr(pdbstr)
				
				### number of chains in the matching subset:
                numchains = 1
                
                ### have to have this in the try block to skip through CmdException
                ### the CmdException is thrown when PyMOL is unable to fetch the pdb file
                ### that in turn happens when a structure is superseded by other 
                ### structure, as 1oux is superseded by 1r51
                try:
                    numchains = len(cmd.get_chains(id))
                    print ' Number of chains obtained: ',str(numchains)
                except CmdException:
                    reportfile.write('>' + '\t' + id + '\t'+ 'not saved, CmdException' + '\n')
                    print "Can't get the number of chains ... :("
                
                match = self.check_match(msstr, motifstr, numchains)
                    
                if match:
                    print ' Writing report file and saving motif...'
                    self.saveAutoMotif()
                    self.write_report(reportfile, id, numchains, len(motif))
                    saved = True
                else:
                    ### a lot of extra residues in matching subset means that the motif is too flexible
                    ### we have two options here to make the motif more stringent, turn the backbones 'On'
                    ### for all residue is the first thing to do, then start lowering the tolerance
                    ### we don't strive to eliminate all extra residues in the motif, but rather find it
                    ### somewhere in the middle, where the number of extra residues is not too large, and the
                    ### tolerance is not too small as excessively low tolerance makes the motif too stringent
                    
                    ### now we're going to turn all the backbones on and see if it make any difference
                
                    print ' Motif and matching subset are not equal, motif not saved...'
                    print ' Turning backbones on for all residues, except metal ions...'
                    
                    for i in range(0, len(motif)):
                        if not self.isMetal(motif[i][0]):
                            glb.GUI.motif_maker['backbone'][i+1].delete(0, END)
                            glb.GUI.motif_maker['backbone'][i+1].insert(0, 'On')
                
                    print ' Retesting motif on ',id,' after turning all backbones on...'
                    self.testAutoMotif()
                
                    pdbstr_bbnon = cmd.get_pdbstr('matching_subset')
                    msstr_bbnon = self.process_pdbstr(pdbstr_bbnon)
                    
					### check if the matching subset is equal to the motif definition
                    match = self.check_match(msstr_bbnon, motifstr, numchains)
                    
                    if match:
                
                        print ' Motif and matching subset are equal after including backbone...'
                        print ' Writing report file and saving motif...'
                        self.write_report(reportfile, id, numchains, len(motif))
                        self.saveAutoMotif()
                        saved = True
                            
                    else:

                        ### apparently the backbone atoms did not help, leave them on and start lowering tolerance
                        ### the first thing to do here is to see if it'll make any difference at all
                        
                        print ' Motif not saved after including backbone, try lowering tolerance...'    
                        
                        ### this block will lower the tolerance to the minimum and see if we have a chance of equating
                        ### matching subset to the catalytic site
                        tolerance = 0.50 # this may not have to be so low, will consider in generating the metal ion motifs
                        glb.GUI.motif_maker['pf'].delete(0,tk.END)
                        glb.GUI.motif_maker['pf'].insert(0,str(tolerance))
                        self.testAutoMotif()
                        pdbstr_tol_test = cmd.get_pdbstr('matching_subset')
                        #print pdbstr_tol_test
                        msstr_tol_test = self.process_pdbstr(pdbstr_tol_test)
                        print "msstr: ", msstr_tol_test
                        print "motifstr: ", motifstr
                        worthit = False
                        if len(msstr_tol_test) < len(msstr_bbnon):
						    ### check if the matching subset is equal to the motif definition
                            match = self.check_match(msstr_tol_test, motifstr, numchains)
                            if match:
                                worthit = True
                                print ' Lowering tolerance should work...'
                            else:
                                print ' Lowering tolerance will not work, motif will not be saved...'                            
                        
                        if worthit:
                            decrement = 0.1
                            tolerance = 2.00
                            while tolerance >= 0.50:
                                tolerance -= decrement
                                #reportfile.write('# ADJUSTMENT: Decreased tolerance to ' + str(tolerance))                            
                                glb.GUI.motif_maker['pf'].delete(0,tk.END)
                                glb.GUI.motif_maker['pf'].insert(0,str(tolerance))
                            
                                print ' Retesting motif with backbones on and tolerance of ',str(tolerance) 
                            
                                self.testAutoMotif()

                                pdbstr_tol = cmd.get_pdbstr('matching_subset')
                                msstr_tol = self.process_pdbstr(pdbstr_tol)
                                
                                if len(msstr_tol) < len(msstr_bbnon):
                                    print ' It is now better than it was, checking if there is a match...'

									### check if the matching subset is equal to the motif definition
                                    match = self.check_match(msstr_tol, motifstr, numchains)                        
                
                                    if match:
                                        print ' Motif and matching subset are equal after lowering tolerance...'
                                        print ' Writing report file and saving motif...'
                                        self.write_report(reportfile, id, numchains, len(motif))
                                        self.saveAutoMotif()
                                        saved = True
                                        break
                        else:
                            reportfile.write('>' + '\t' + id + '\t'+ 'not saved' + '\n')                
    
    def write_report(self, reportfile, id, numchains, motiflen):
        reportfile.write('>' + '\t' + id + '\t' + str(self.pf) + '\t' + str(numchains) + '\t' + lib.getEcNumber(id) + '\n')
        for i in range(0, motiflen):
            resn = glb.GUI.motif_maker['resn'][i+1].get()
            chain = glb.GUI.motif_maker['chain'][i+1].get()
            resi = glb.GUI.motif_maker['resi'][i+1].get()
            bbn = glb.GUI.motif_maker['backbone'][i+1].get()
            reportfile.write(resn + '\t' + chain + '\t' + resi + '\t' + bbn + '\n')
    
    def count_chains(self, msstr):
        chainlist = []
        for resstr in msstr:
            if resstr[4:5] not in chainlist:
                chainlist.append(resstr[4:5])
        return len(chainlist)
    
    def check_match(self, msstr, motifstr, numchains):
    
        ### this block will preprocess both msstr and motifstr so they are the same format
        ### we only need to compare the residue types and numbers of the two lists, it should
        ### be enough to determine if they are equal, or if the same motif is found in more
        ### than one chains
        norm_msstr = [] ### normalized version of matching subset string
        for resstr in msstr:
            upper = len(resstr)
            norm_resstr = resstr[0:3].strip(" ") + ' ' + resstr[5:upper].strip(' ')
            norm_msstr.append(norm_resstr) ### take only the type and the number

        ### the following compares the string representations of motif and matching substrate
        ### residue, it determines if they contain same residues, or if the same motif is found in
        ### multiple chains
        if len(norm_msstr) == len(motifstr):
            for resstr in motifstr:
                if resstr not in norm_msstr:
                    return False
            return True
        elif len(norm_msstr) == len(motifstr)*numchains: ### could mean that we have the same motif on multiple chains
            for resstr in norm_msstr:
                if resstr not in motifstr:
                    return False
            return True
        else:
            return False
    
    def process_pdbstr(self, pdbstr):
        msstr = []
        lines = pdbstr.split('\n')
        print str(len(lines)), 'lines in pdbstr'
        
        for line in lines:
            if line.startswith('ATOM') or line.startswith('HETATM'):
                resstr = line[17:27].strip(' ')
                if resstr not in msstr:
                    msstr.append(resstr)
        return msstr
    
    def getLibraryMotif(self):
    
        self.doCommonSetup()
        self.resetRows()
        glb.GUI.motif_maker['pf'].delete(0,tk.END)
        glb.GUI.motif_maker['pf'].insert(0,'2.00')
        #glb.GUI.motif_maker['pdb'].delete(0,tk.END)
        glb.GUI.motif_maker['ec'].delete(0,tk.END)
    
        for i in range(1,11):
            glb.GUI.motif_maker['resn'][i].delete(0, END)
            glb.GUI.motif_maker['chain'][i].delete(0, END)
            glb.GUI.motif_maker['resi'][i].delete(0, END)

        pdb_id = glb.GUI.motif_maker['pdb'].get()
        ecnum = lib.getEcNumber(pdb_id)
        
        if ecnum.startswith('0'):
            print 'ecnum: ',ecnum
            ecnum = '7.0.0.0'
            print 'ecnum: ',ecnum
        
        glb.GUI.motif_maker['ec'].insert(END, ecnum)
        
        if ecnum != 'N/A':
            motif = lib.getMotif(pdb_id)
            if len(motif) < 2 or len(motif) > 10:
                return False
            chain = lib.getChain(pdb_id)
            
			# we will not do it for metal ion motifs
            do_order = True
            for res in motif:
                if not self.isMetal(res[0]):
                    do_order = False
                    break
            if do_order and len(motif) > 2:
                motif = self.orderByDistance(motif, pdb_id)            
            
            for i in range(0, len(motif)):
                glb.GUI.motif_maker['resn'][i+1].insert(END, motif[i][0])
                glb.GUI.motif_maker['chain'][i+1].insert(END, chain)
                glb.GUI.motif_maker['resi'][i+1].insert(END, motif[i][1])
                # backbone is turned on in the following cases:
                # N : backbone amide
                # SN : sidechain and backbone amide
                # O : backbone carbonyl
                # SO : sidechain and backbone carbonyl
                # SNO : sidechain, backbone amide, and backbone carbonyl
                if len(motif[i]) == 2:
                    motif[i].append('X')
                if motif[i][2] == 'N' or motif[i][2] == 'O' or motif[i][2] == 'SN' or motif[i][2] == 'SNO' or motif[i][2] == 'SO':
                    glb.GUI.motif_maker['backbone'][i+1].delete(0, END)
                    glb.GUI.motif_maker['backbone'][i+1].insert(0, 'On')
                if motif[i][0] == 'GLY':
                    glb.GUI.motif_maker['backbone'][i+1].delete(0, END)
                    glb.GUI.motif_maker['backbone'][i+1].insert(0, 'On')
            
            return True
        else:
            return False
    
    def getBBNparameters(self, motif):
        motiflen = len(motif)
        bbnparam = {}
        for i in range(0, motiflen):
            bbn = glb.GUI.motif_maker['backbone'][i+1].get()
            bbnparam.update({motif[i][1]: bbn})
        return bbnparam                  
    
    def getOrderedDist(self, motif, id):
        distDict = {}
        orderedDistDict = {}
        resilist = []
        chain = lib.getChain(id)
        for res in motif:
            resilist.append(res[1])
            
        for res_1 in motif:
            for res_2 in motif:
                if res_1[1] != res_2[1]:
                    
                    if res_1[0] == 'GLY':
                        atom_1 = 'CA'
                    elif self.isMetal(res_1[0]):
						atom_1 = res_1[0]
                    else:
                        atom_1 = 'CB'
						
                    if res_2[0] == 'GLY':
                        atom_2 = 'CA'
                    elif self.isMetal(res_2[0]):
                        atom_2 = res_2[0]
                    else:
                        atom_2 = 'CB'
                    
                    cmd.reinitialize()               
                    cmd.fetch(id, async=0, path=glb.FETCH_PATH)
                    dstr = chain+'/'+res_1[1]+'/'+atom_1 + ' and ' + chain+'/'+res_2[1]+'/'+atom_2
                    try:
                        d = cmd.get_distance(chain+'/'+res_1[1]+'/'+atom_1, chain+'/'+res_2[1]+'/'+atom_2)
                        distDict.update({res_1[1] + '_' + res_2[1]: d})
                    except CmdException:
                        print "Can't calculate distance between ",dstr," ... :("

        orderedDistDict = OrderedDict(sorted(distDict.items(), key=lambda x: x[1]))
        return orderedDistDict
    
	# This function is very messy
    def orderByDistance(self, motif, id):
        ordMotif = []
        distDict = {}
        orderedDistDict = {}
        resilist = []
        chain = 'a'
        atom = 'CB'
        
        for res in motif:
            resilist.append(res[1])
            
        orderedDistDict = self.getOrderedDist(motif, id)
        
        if len(orderedDistDict) != (len(motif) - 1)*(len(motif)):
            return motif
        
        resipairs = []
        for k, v in orderedDistDict.items():
            resipairs.append(k)
        
        pair_1 = resipairs[0]
        pair_2 = resipairs[1]
        d_1 = 0
        d_2 = 0
        maybenext = []
        sofar = []
        
        for k, v in orderedDistDict.items():
            if ((pair_1 != k) and (pair_2 != k)):
                if (k.split('_')[0] == pair_1.split('_')[1]):
                    d_1 = v
                    maybenext.append(k)
                elif (k.split('_')[0] == pair_2.split('_')[1]):                    
                    d_2 = v
                    maybenext.append(k)
            
        if (d_1 > d_2):
            nextpair = maybenext[0]
        else:
            nextpair = maybenext[1]
        
        if (pair_1.split('_')[1] == nextpair.split('_')[0]):
            sofar.append(pair_1.split('_')[0])
            sofar.append(pair_1.split('_')[1])
            sofar.append(nextpair.split('_')[1])
        elif (pair_2.split('_')[1] == nextpair.split('_')[0]):
            sofar.append(pair_2.split('_')[0])
            sofar.append(pair_2.split('_')[1])
            sofar.append(nextpair.split('_')[1])

        for k, v in orderedDistDict.items():
            if (len(sofar) != len(resilist)):
                if k.split('_')[1] not in sofar: 
                    sofar.append(k.split('_')[1])                
        
        for resi in sofar:
            for res in motif:
                if (resi == res[1]):
                    ordMotif.append(res)

        return ordMotif
    
    ### following code is copied from MotifMaker in motif.py
    ### ===============================================================
    
    # Maybe this should go in init()
    # But this is the initial refactoring from procedural code
    def doCommonSetup(self):
        glb.GUI.motif_maker['file'] = None
        glb.GUI.motif_maker['wait'] = []
        glb.GUI.motif_maker['motif'] = []
        glb.GUI.motif_maker['order'] = []
        self.pf = glb.GUI.motif_maker['pf'].get()
        self.pdb = glb.GUI.motif_maker['pdb'].get().lower()
        self.ecen = glb.GUI.motif_maker['ec'].get()
        self.resn = {}
        self.resi = {}
        self.backbone = {}
        self.chain = {}
        self.excepLoop = 0
        self.exceptions = ''
        self.ec = ''
        self.name = ''
        self.skip = {}
        self.numberOfAcids = 0
        cmd.reinitialize()

    def resetRows(self):
        for i in range(1,11):
            glb.GUI.motif_maker['resn'][i].delete(0,tk.END)
            glb.GUI.motif_maker['resi'][i].delete(0,tk.END)
            glb.GUI.motif_maker['chain'][i].delete(0,tk.END)
            if glb.GUI.motif_maker['backbone'][i].get() == 'On':
                glb.GUI.motif_maker['backbone'][i].invoke('buttonup')
        
    # replaces write(string != None)
    def buildAutoMotif(self, string):
        glb.GUI.motif_maker['motif'].append(string)
    
    # Replaces write(open=True) with mode = 0 or 4
    def openAutoMotifForTesting(self):
        glb.GUI.motif_maker['motif'] = []
        return True
    
    def openAutoMotifForSaving(self):
        """
        if os.path.exists(glb.pathmaker((self.name,'.py'),root=glb.USRMOTIFSFOLDER)) or os.path.exists(glb.pathmaker((self.name,'.py'),root=glb.MOTIFSFOLDER)):
            answer = askyesno('Motif Exists', 
            'A motif has already been made for EC:%s on PDB:%s.\n'%(self.ec,self.pdb)+
            'Are you sure you want to replace it?')
            if answer == False:
                 return False
        """
        glb.GUI.motif_maker['file'] = open(glb.pathmaker((self.name,'.py'),root=glb.AUTOMOTIFSFOLDER), 'w')
        return True
    
    # Replaces write(close=True) with mode=0 or 4
    def closeAutoMotifForTesting(self):
        if glb.GUI.motif_maker['radio'].get() == 1:
            cmd.reinitialize()
            cmd.fetch(glb.GUI.motif_maker['testpdb'].get(), async=0, path=glb.FETCH_PATH)
            glb.update()
        elif glb.GUI.motif_maker['radio'].get() == 2:
            glb.randompdb()

        d = 1
        
        lines = ''.join(glb.GUI.motif_maker['motif']).split('\n')
        for line in lines:
            if line != '':
                eval(line)
        cmd.select('matching_subset', self.name)
        # I think here it's OK to delete the motif name
        cmd.delete(self.name)
        cmd.deselect()
        return True

    # Replaces write(close=True) with mode=2
    def closeAutoMotifForExporting(self):
        if glb.GUI.motif_maker['file'] != None:
            glb.GUI.motif_maker['file'].writelines(glb.GUI.motif_maker['motif'])
            glb.GUI.motif_maker['file'].close()                        
        else:
            print 'No file written'
        return True
        
    def closeAutoMotifForSaving(self):
        self.closeAutoMotifForExporting()
        glb.loadMotifs(glb.AUTOMOTIFSFOLDER)
        return True
        
    def getlocistr(self):
        locistr = ''
        tmpdict = {}
        for item in glb.GUI.motif_maker['order']:
            if item[1] not in tmpdict:
                tmpdict[item[1]] = []
            tmpdict[item[1]].append(item[2])
        for chain in tmpdict:
            locistr = '%s%s-%s;' % (locistr, chain.lower(), ','.join(tmpdict[chain]))
        return locistr
    
    def getresnstr(self):
        tmplist = []
        for item in glb.GUI.motif_maker['order']:
            tmplist.append(item[0])
        return ','.join(tmplist)
    
    def addresn(self,x,y,z):
        glb.GUI.motif_maker['order'].append((x, y, z))
        try:
            glb.GUI.motif_maker['order'].sort(key=lambda item: (item[1],int(item[2])))
        except TypeError:
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(int(x[2]), int(y[2])))
            glb.GUI.motif_maker['order'].sort(lambda x,y: cmp(x[1], y[1]))
        return x
    
    def acceptresn(self,x,y,z):
        if len(x) == 0:
            return ''
        try:
            x = x.lower()
            newresn = glb.AminoHashTable[x][3]
        except KeyError:
            return None
        return self.addresn(newresn,y,z)
        
    # Depends on doCommonSetup() already being called
    # Returns false if input was bad
    def validateInput(self):
    
        cmd.fetch(self.pdb, async=0, path=glb.FETCH_PATH)
        if (self.pdb not in cmd.get_names('all')) or (cmd.count_atoms(self.pdb) == 0):
            #self.exceptions += 'Could not fetch {0}'.format(self.pdb)
            self.exceptions += 'Could not fetch %s'%(self.pdb)
        glb.update()
        preecs = self.ecen.split(',')
        for preec in preecs:
            try:
                eclist = preec.split('.')
                ec1,ec2,ec3,ec4 = eclist
            except ValueError:
                self.exceptions += 'Please enter a correct EC code with periods.\n'
            else:
                if len(ec1) != 1 or int(ec1) < 1 or int(ec1) > 7:
                    self.exceptions += 'The first number in an EC code has to be >= 1 and <= 7.\n'
                if len(ec2) > 2 or len(ec2) < 1:
                    self.exceptions += 'The second number in an EC code has to be at most two digits.\n'
                if len(ec3) > 2 or len(ec3) < 1:
                    self.exceptions += 'The third number in an EC code has to be at most two digits.\n'
                if len(ec4) > 3 or len(ec4) < 1:
                    self.exceptions += 'The fourth number in an EC code has to be at most three digits.\n'
        self.ec = self.ecen.replace('.','_').replace(',','_').replace(' ','')
        self.skip = {}
        self.skip[0] = 0
        for i in range(1,11):
            # The old way of storing what order they were in is too complicated
            # This will try to set it once in the GUI and forget it
            g = i
            self.resi[g] = glb.GUI.motif_maker['resi'][g].get().strip()
            self.backbone[g] = glb.GUI.motif_maker['backbone'][g].get()
            self.chain[g] = glb.GUI.motif_maker['chain'][g].get().strip()
            self.resn[g] = self.acceptresn(glb.GUI.motif_maker['resn'][g].get().strip(),self.chain[g],self.resi[g])
            self.skip[g] = False
            if self.resn[g] == '' and self.resi[g] == '' and self.chain[g] == '':
                ### this gives us the ability to skip whole blocks
                self.skip[g] = True
                self.skip[0] += 1
            elif self.resn[g] != '' and self.resi[g] != '' and self.chain[g] != '':
                if self.resn[g] == None:
                    self.exceptions += 'Residue %s is not recongnized.\n'%(g)
                elif cmd.count_atoms('%s/%s`%s/'%(self.chain[g],self.resn[g],self.resi[g])) == 0:
                    self.exceptions += 'There is no %s at number %s on chain %s.\n'%(self.resn[g],self.resi[g],self.chain[g])
                elif self.resn[g] == 'gly' and self.backbone[g] == 'Off':
                    self.exceptions += 'Please turn on the backbone for glycine residue %s\n'%(g)
                self.excepLoop +=1
            else:    
                if self.resn[g] == '':
                    self.exceptions += 'Please enter a residue type for residue %s\n'%(g)
                if self.resi[g] == '':
                    self.exceptions += 'Please enter a number for residue %s\n'%(g)
                if self.chain[g] == '':
                    self.exceptions += 'Please select a chain for residue %s\n.'%(g)
                self.excepLoop +=1
        if self.excepLoop < 2:
            # exception = True
            self.exceptions += 'Motifs require that 2 or more residues be entered.'
        if self.exceptions != '' and self.exceptions != '\n':
            #showerror('Error', 'The following errors have occurred:\n'+self.exceptions)
            return False
        return True
        
    # Replaces makemotif(0) and makemotif(4)
    def testAutoMotif(self):
        #print 'Testing motif from AutoMotifMaker'
        if self.makeAutoMotifWrapper(self.openAutoMotifForTesting, self.closeAutoMotifForTesting):
            #print 'Motif {0} with {1} amino acids was run.'.format(self.name, self.numberOfAcids)
            print 'Motif %s with %s amino acids was run.'%(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    def saveAutoMotif(self):
        if self.makeAutoMotifWrapper(self.openAutoMotifForSaving, self.closeAutoMotifForSaving):
            #print 'Motif {0} saved to user motifs folder with {1} amino acids.'.format(self.name, self.numberOfAcids)
            print 'Motif %s saved to user motifs folder with %s amino acids.'%(self.name, self.numberOfAcids)
            return True
        else:
            return False
    
    # Fault-tolerant wrapper
    def makeAutoMotifWrapper(self, openFunction, closeFunction):
        retVal = False
        try:
            retVal = self.makeAutoMotifCore(openFunction, closeFunction)
        except IOError, problem:
            print problem
        finally:
            if glb.GUI.motif_maker['file'] != None:
                if not glb.GUI.motif_maker['file'].closed:
                    glb.GUI.motif_maker['file'].close()
        return retVal
    
    # Replaces most of makemotif(0, 1, 2, 4)
    # But don't call directly!
    def makeAutoMotifCore(self, openFunction, closeFunction):
        self.doCommonSetup()
        if self.validateInput():
            self.name = 'A_%s_%s'%(self.pdb,self.ec)
            self.buildAutoMotif("'''\n")
            self.buildAutoMotif("FUNC:%s\n"%(self.name))
            self.buildAutoMotif("PDB:%s\n"%(self.pdb))
            self.buildAutoMotif("EC:%s\n"%(self.ec.replace('_','.')))
            self.buildAutoMotif("RESI:%s\n"%(self.getresnstr()))
            self.buildAutoMotif("LOCI:%s\n"%(self.getlocistr()))
            self.buildAutoMotif("'''\n")
            if not openFunction():
                return False
            ### atomlist dict was declared here before, it was made global so other methods can see it
            resnlist = ['']### residue list
            resnlistf = ['']### residue list with appended 'i', making them unique
            resilist = ['']### residue id list. Based on sequence number.
            chainlist = ['']### chain list
            bonelist = ['']### backbone list
            count = 0;
            numOfi = {}
            for i in range(1,11):
                # This is the second place this was changed:
                # From:
                # g = glb.GUI.motif_maker['curorder'][i]
                # To:
                g = i
                if not self.skip[g]:
                    if self.resn[g] not in numOfi:
                        numOfi[self.resn[g]] = 0
                    resnlist.append(self.resn[g])
                    resilist.append(self.resi[g])
                    resnlistf.append(self.resn[g]+('i'*(numOfi[self.resn[g]])))
                    chainlist.append(self.chain[g])
                    bonelist.append(self.backbone[g])
                    numOfi[self.resn[g]] += 1
            
            ### This loop will increment through the amino acids. The amino acid we are looking
            ### at right now is specified by the e variable. The a variable will count the
            ### number of times it is compared to the carbons in the other amino acids. And is
            ### used later on to print the "byres" and select line, and delete line below.
            resnlen = (len(resnlist)-1)
            e = 0
            while e < resnlen:
                #print 'looking at: ', e
                a = 0
                e += 1
                ### select stuff explained later on
                selectlimit = 50
                selectstart = 1 ### where to start selection
                selectlimiter = 1 ### limit defined as a/selectlimit
                selectextra = [] ### add to selection at the end
                deleteextra = [] ### add to deletion at the end
                
                if bonelist[e] == 'Off':###just sidechains
                    bList=self.atomlist[0][resnlist[e]]
                else:### sidechain with backbone
                    bList=self.atomlist[0][resnlist[e]]+self.atomlist[1]
                
                ### This loop will increment through the amino acids that we want
                ### to compare to the amino acid we want to find. The amino acid
                ### being compared is specified by the d variable.
                # d is also a variable used in closeMotifForTesting(), but
                # the fact that it has gone out of and back into scope
                # shouldn't matter here (they used to be in the same function)
                
                d = 0
                while d < resnlen:
                    d += 1
                    ### The following line: compare amino acids
                    ### If they are the same, then lets increment one.
                    if resnlistf[e] == resnlistf[d]:
                        d += 1
                        if d > resnlen:
                            continue
                    
                    if bonelist[d] == 'Off':###just sidechains
                        cList=self.atomlist[0][resnlist[d]]
                    else:### sidechain with backbone
                        cList=self.atomlist[0][resnlist[d]]+self.atomlist[1]
                    ### This loop increments through all the carbons
                    ### in the amino acid we want to find.
                    for eachB in bList:
                        ### This loop increments through all the carbons
                        ### in the other amino acids that we are want to
                        ### compare with.
                        for eachC in cList:
                            ### Gets the distance between our atoms in our selected amino acids.
                            rstr = ""+chainlist[e]+'/'+resilist[e]+'/'+eachB + ' and ' + chainlist[d]+'/'+resilist[d]+'/'+eachC
                            try:
                                r = cmd.get_distance(chainlist[e]+'/'+resilist[e]+'/'+eachB,chainlist[d]+'/'+resilist[d]+'/'+eachC)
                                ### The precision factor
                                ### The ranger is the slider that is moved.
                                ### r is set by the get_distance above.
                                g = '%.2f' %(float(r) + float(self.pf))
                            except CmdException:
                                print 'CmdException handled in makeMotifCore ... '
                                print rstr
                            
                            a += 1
                            
                            ### apparently pymol cannot handle over a number
                            ### between 248 and 264 selections at one time.
                            ### This fixes that by making sure we do not pass
                            ### "selectlimit" selections at one time.
                            if float(selectlimiter) < (float(a)/float(selectlimit)):
                                self.buildAutoMotif("cmd.select('%s%s',' "%(resnlistf[e],(selectlimiter*selectlimit)))
                                for i in range(selectstart,a):
                                    if i==(a-1):
                                        self.buildAutoMotif("br. %s%s')\n"%(resnlistf[e],i))
                                    else:
                                        self.buildAutoMotif("br. %s%s&"%(resnlistf[e],i))
                                for i in range(selectstart,a):
                                    if i==(a-1):
                                        pass
                                    else:
                                        self.buildAutoMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
                                selectextra.append('%s%s&'%(resnlistf[e],(selectlimiter*selectlimit)))
                                deleteextra.append("cmd.delete('%s%s')\n"%(resnlistf[e],(selectlimiter*selectlimit)))
                                selectlimiter += 1
                                selectstart += selectlimit
                            ### e > d is all the combinations of residues
                            ### that would already have one of the residues
                            ### found in the motif, therefore the second
                            ### amino acid does not need an r. (resn)
                            ### property selection, as it is already a selection.
                            if e > d:
                                self.buildAutoMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&%s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlistf[d],g))
                            else:
                                self.buildAutoMotif("cmd.select('%s%s', 'n. %s&r. %s w. %%s of n. %s&r. %s'%%(d*%s))\n"%(resnlistf[e],a,eachB,resnlist[e],eachC,resnlist[d],g))
                self.buildAutoMotif("cmd.select('%s',' "%(resnlistf[e]))
                if selectextra != []:
                    self.buildAutoMotif(''.join(selectextra))
                for i in range(selectstart,a+1):
                    if i==a:
                        self.buildAutoMotif("br. %s%s')\n"%(resnlistf[e],i))
                    else:
                        self.buildAutoMotif('br. %s%s&'%(resnlistf[e],i))
                for x in deleteextra:
                    self.buildAutoMotif(x)
                for i in range(selectstart,a+1):
                    self.buildAutoMotif("cmd.delete('%s%s')\n"%(resnlistf[e],i))
        
            resnlistfstr = ""
            for i in range(1,resnlen+1):
                if i == resnlen:
                    resnlistfstr += resnlistf[i]
                else:
                    resnlistfstr += resnlistf[i]+'|'
            self.buildAutoMotif("cmd.select('%s', '%s')\n"%(self.name,resnlistfstr))
            for i in range(1,resnlen+1):
                self.buildAutoMotif("cmd.delete('%s')\n"%(resnlistf[i]))
            self.numberOfAcids = len(resnlist) - 1
            closeFunction()
            return True
