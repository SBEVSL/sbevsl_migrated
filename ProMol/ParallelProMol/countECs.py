import os
from collections import Counter

RMSD_THRESHOLD_SUPER = 0.1
RMSD_THRESHOLD_CEALIGN = 0.1

MOTIFS_DIR = os.path.join(os.path.split(os.path.split(os.path.abspath(__file__))[0])[0], 'Motifs')
RESULTS_DIR = 'TestResultsEC'
INVALIDS_DIR = 'InvalidMotifs'

ec_count = 0
invalid_count = 0
ecs = Counter()
ec_nums_complete = []
totalMotifs = 0

for file in os.listdir(RESULTS_DIR):
    ec_num = file.rsplit('_',1)[0][2:]
    ec_nums_complete.append(ec_num)
    ecs[ec_num] += 1
print 'ECs finished:', len(ec_nums_complete), ec_nums_complete[0]

print 'Total ECs:', sum(ecs.values())

for file in os.listdir(INVALIDS_DIR):
    with open(os.path.join(INVALIDS_DIR, file),'Ur') as fin:
        ec_num = file.rsplit('_',1)[0][2:]
        ecs[ec_num] -= 1
        invalid_count += len(fin.readlines())
        
print 'InvalidMotifs:', invalid_count 

for (dirpath, dirnames, filenames) in os.walk(MOTIFS_DIR):
    if len(filenames) > 0 and filenames[0].startswith('S'):
        ec_num = '_'.join(dirpath.rsplit('\\',4)[-4:])
        totalMotifs += len(filenames)
        if ec_num not in ec_nums_complete:
            print ec_num
            ec_count += 1

print 'Total ECs:', len(ecs), 'Unrepresented ECs:', len(filter(lambda x: x <= 0, ecs.values()))
print 'ECs unfinished:', ec_count
print 'Total Motifs:', totalMotifs
print 'Verified Motifs:', totalMotifs - invalid_count

        
