import os, sys
from collections import Counter

PROMOL_DIR = ''
numOfFiles = 1
duplicateCount = Counter()

allMotifPDBs = [len(open(os.path.join(dirpath, f), 'Ur').readlines()) \
                for (dirpath, dirnames, filenames) in os.walk(os.path.join(PROMOL_DIR,'TestResultsEC_Comb')) \
                for f in filenames if f.endswith('.txt') and len(f) > 10]
print sum(allMotifPDBs) - len(allMotifPDBs)
sys.exit(0)
##with open('pdb_list.txt','w') as fout:
##    for pdb_ec in allMotifPDBs:
##        fout.write('%s,%s\n' % (pdb_ec[0], pdb_ec[1]))
print allMotifPDBs[0], len(allMotifPDBs)
allPDBs = [pdb_ec for pdb_ec in map(lambda x: tuple(x.split(',',1)), open('pdb_list.txt','rU').read().split('\n')) \
           if pdb_ec not in allMotifPDBs]
print allPDBs[0], len(allPDBs)
for pdb_ec in allPDBs:
    duplicateCount[pdb_ec] += 1
print 'unique:',len(duplicateCount),'duplicates:',len(filter(lambda x: x[1] > 1, duplicateCount.items())) 
allPDBs = duplicateCount.keys()
numOfPDBsPerFile = len(allPDBs)/numOfFiles
for n in range(numOfFiles):
    with open('pdb_list{0}.txt'.format(n+1), 'w') as fout:
        print len(allPDBs[n*numOfPDBsPerFile: (n+1)*numOfPDBsPerFile])
        fout.write('\n'.join([','.join(pdb_ec) for pdb_ec in allPDBs[n*numOfPDBsPerFile: (n+1)*numOfPDBsPerFile]]))
