import sys, os, socket
from multiprocessing import Process
from threading import Thread
from ProClient import ProClient, JobResult, Job
from time import sleep

NUM_OF_MOTIFS = -1
allkeys = [f.split('.')[0] for f in os.listdir(os.path.join(os.path.split(os.getcwd())[0],'Motifs')) if len(f) > 10]
#rint 'allkeys length: {0}'.format(len(allkeys))
keys = allkeys[:NUM_OF_MOTIFS]
#pdb = '4EZI'
delta = 1.0
resultPort = 50007
DISTRIBUTE=True
smHost, smPort = 'cos-a33003.local', 50010
found = []

# heme job
testFile = '1QLH_trials_1(1).txt'
with open(testFile, 'r') as fin:
    pdb_type = { pdb : lineNum for lineNum, line in enumerate(fin.read().strip().split('\r\n')) for pdb in line.split(',') if lineNum <= 2 }
pdbs = pdb_type.keys()
deltaRange = [float(d)/10.0 for d in range(8, 15, 1)]
#keys = ['M_1nml_1_11_1_5']
##keys = ['M_1dii_1_17_99_1',
##        'M_1fcb_1_1_2_3',
##        'M_1fft_1_10_3_-',
##        'M_1nml_1_11_1_5',
##        'M_1sox_1_8_3_1',
##        'M_2cpo_1_11_1_10',
##        'M_5cox_1_14_99_1',
##        'M_7atj_1_11_1_7',
##        'R_1ezv_1_10_2_2'
##        ]
job = Job({'{0}\t{1}\t{2}'.format(pdb, motif, d) : '{0}\t{1}\t{2}'.format(pdb, motif, d) for motif in keys for d in deltaRange for pdb in pdbs })

try:
    #job = Job({'{0}\t{1}\t{2}'.format(pdb, motif, delta) : '{0}\t{1}\t{2}'.format(pdb, motif, delta) for motif in keys })
    jobSize = job.size()
    resultCollector = JobResult(job)
    listener = resultCollector.listenerThread()
    resultPort = resultCollector.getResultPort()
    client = Process(target=ProClient, args=(resultPort, smHost, smPort, job))
    client.start()
    MAX_STAG = 5
    stag = 0
    con = False
    last = 0
    tasks = 0
    while 1:
        tasks = resultCollector.taskTracker(10.0)
        #print 'Tasks Completed? {0}'.format(tasks)
        if tasks > last and con:
            con = False
        elif tasks <= last and con:
            stag +=1
        elif tasks <= last and not con:
            con = True
        if tasks >= jobSize or stag >= MAX_STAG:
            break
        last = tasks
        print 'Results attained: {0}/{1}'.format(tasks, jobSize)
        if client.exitcode > 0:
            resultCollector.shutdown()
            listener.join()
            client.join()
            raise Warning
    print 'Done. Results attained: {0}/{1}'.format(tasks, jobSize)
    with open(testFile, 'a') as fout:
        for resultName, result in sorted(resultCollector.results(), key=lambda x: x[0]):
            fout.write('\r\n{0}: {1}:: {2}'.format(pdb_type[resultName.split('\t',1)[0]], resultName, result))
            parsedResult = result.split('\t')
            ldr, mot = ([r.strip() for r in parsedResult[0].split(':')])
            #print 'ldr: {0}, mot: {1}'.format(ldr, mot)
            if len(ldr) > 2 or int(ldr) >= 0:
                motifStr = parsedResult[0]
                found.append(motifStr)
                #glb.GUI.motifs['csvprep'][pdb][mot] = {}
                glb_GUI_motifs_csvprep_pdb_ldr_mot_1 = {'res':[(res.split(',')) for res in parsedResult[1:]]}
    for toutName, toutHost in resultCollector.resultsOutstanding():
        try:
            print 'Outstanding: {0}; {1}'.format(toutName,socket.gethostbyaddr(toutHost)[0])
        except socket.error as err:
            print 'OutstandingError: {0}; {1}'.format(toutName, err)
    resultCollector.shutdown(True)
    listener.join()
    client.join()
    print 'mischief managed'
except Warning:
    print 'Job could not be submitted to servers.'
    
sys.exit(0)
