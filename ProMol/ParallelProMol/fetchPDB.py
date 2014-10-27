import os, sys
from urllib import urlretrieve
from time import clock

PDB_URLS = ['http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat={0[0]}&compression=NO&structureId={1}',
            'http://mirrors.rit.edu/pdb/data/structures/divided/{0[0]}/{1[1]}{1[2]}/{0[1]}{1}{0[2]}'
            ]
PDB_DIR = os.path.join('PDBDownloads','')
FILE_FORMAT = ('pdb', 'pdb', '.pdb') #('mmCIF','', '.cif.gz') 
MAX_FILES = 1000
PARE_SIZE = 500

class PDBRetriever():

    def __init__(self, pdb_url=None, pdb_dir=None):
        global PDB_URL, PDB_DIR
        if pdb_url is not None:
            PDB_URL = pdb_url
        if pdb_dir is not None:
            PDB_DIR = os.path.join(pdb_dir, '')

    def getPDB(self, pdb):
        fetch_time = clock()
        for pdb_url in PDB_URLS:
            try:
                #print pdb_url.format(FILE_FORMAT, pdb)
                urlretrieve(pdb_url.format(FILE_FORMAT, pdb), '%s%s' % (PDB_DIR, pdb+FILE_FORMAT[2]))
            except Exception as err:
                print 'PDB Retrieval Exception: %s\nurl: %s' % (err, pdb_url)
                continue
            else:
                return True
            finally:
                pass
                #print 'fetch time [sec]:', clock() - fetch_time
        else:
            return False

