import random
from tkFileDialog import askopenfile
import os


id_chain = {}
id_ecnum = {}
id_motif = {}

def read_pdb_list():
    # the file path must be changed to work on mac and linux: 
    #infile = open("C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\pdb_list.txt", "r")
    try:
        infile = open(os.path.join(os.path.dirname(__file__).replace('\n',''),"pdb_list.txt"), "r")
    except:
        infile = askopenfile(mode='r',title="pdb_list.txt, list of PDB ids")
    
    pdb_list = set()
    for line in infile:
        line = line.strip("\n")
        line = line.strip(',')
        data = line.split(",")
        for id in data:
            pdb_list.add(id.strip(" "))
    infile.close()
    print "\nIDs in PBD list:",len(pdb_list)
    return pdb_list
		
def read_motif_definitions(pdb_list):
    # read file lit_lib that contains information on EC number, motif, and homologues
    # lib_file = open("C:\Program Files\PyMOL\PyMOL\modules\pmg_tk\startup\ProMol\lit_lib_23.txt", "r")
    try:
        lib_file = open(os.path.join(os.path.dirname(__file__).replace('\n',''),"lit_lib_23.txt"), "r")
    except:
        lib_file = askopenfile(mode='r',title="lit_lib_23.txt, EC number, motif, and homologues")
    
    content = lib_file.readlines()
    lib_file.close()

    pdbid = ""
    motif = []

    not_in_lib = []
    will_generate = []
	
    for line in content:
        line = line.strip('\r\n')
        line_data = []
        if line.startswith('>'):
            line_data = line.split('\t')
            id_ch = line_data[0].split('.')
            pdbid = id_ch[0][2:6]
            chain = id_ch[1]
            ecnum = line_data[1].strip(' ')
            if pdbid in pdb_list:
                id_chain.update({pdbid: chain})
                id_ecnum.update({pdbid: ecnum})
            motif = []
        else:
            res = line.split('\t')
            motif.append(res)
            if pdbid in pdb_list:
                will_generate.append(pdbid)
                id_motif.update({pdbid: motif})
    for id in pdb_list:
        if id not in will_generate:
                not_in_lib.append(id)
				
    print "Stored", len(id_motif), "motif definitions"
    
    if len(will_generate) != len(pdb_list):
        print "PDB IDs not in library (",len(not_in_lib),"):"
        out = ""
        for id in not_in_lib:
            out += id + ","
        out = out.strip(",")
        print out + "\n"		

def getPDBlist():
    pdblist = []
    for k, v in id_ecnum.items():
	    pdblist.append(k)
    return pdblist
		
def getEcNumber(pdb_id):
    if pdb_id in id_ecnum: 
        return id_ecnum.get(pdb_id)
    else:
        return 'N/A'

def getChain(pdb_id):
    if pdb_id in id_chain: 
        return id_chain.get(pdb_id)
    else:
        return 'N/A'

def getMotif(pdb_id):
    if pdb_id in id_motif: 
        return id_motif.get(pdb_id)
    else:
        return 'N/A'
	
def init():
    pdb_list = read_pdb_list()
    read_motif_definitions(pdb_list)

init()
