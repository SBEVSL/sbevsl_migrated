"""Motif testing script for interacting directly with ProServer. In ProServer.py, 'DEBUG' has been
declared 'True' to bypass imports from promolglobals, which would require GUI. This variable
should be removed before release.

"""

# additional motif imports
import socket, errno
from threading import Thread, Event, Lock, Semaphore, enumerate as enumThreads
from Logger import Logger
from signal import SIGTERM, SIGINT, signal
from cPickle import dumps, loads
from ProSocket import sockListenerThread, sockSendRecv
from ProJob import DefaultProMolJobExecutor

import os, time
import sys

SAMPLE_SIZE = 2
NUM_OF_MOTIFS = 10
PROMOL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVALIDS_DIR = 'InvalidMotifs'
OUTPUT_DIR = 'UnitTests_A'
invalids = []
motifs = []

with open('invalid_motifs_A.txt', 'Ur') as fin:
    invalids = [motif.strip().strip("'") for motif in fin.readlines()]
    
##for file in os.listdir(INVALIDS_DIR):
##    with open(os.path.join(INVALIDS_DIR, file),'Ur') as fin:
##        for line in fin.readlines():
##            invalids.append(line.strip())

#invalidMotifs = [motif.strip() for motif in open('invalid_motifs_10-10-14.txt', 'rU').readlines()]
#validMotifs = [f.rsplit('_',1)[0] for f in os.listdir(os.path.join(PROMOL_DIR, 'Motifs'))]
motifCount = 0
try:
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(PROMOL_DIR, 'Motifs')):
        for file in filenames:
            if file.endswith('.py'):
                motif = file.rsplit('.',1)[0]
                if motif not in invalids:
                    motifs.append(motif)
                    motifCount += 1
                    if motifCount >= NUM_OF_MOTIFS:
                        raise Exception()
except Exception:
    pass
#motifs = [m for m in allMotifs if m.startswith('S') and 'A'+m[1:] in allMotifs]
#motifs = allMotifs[:NUM_OF_MOTIFS]
pdbs = {} #{m[1] : '.'.join(m[2].split('_')) for m in map(lambda x: x.split('_',2), motifs)}
d = 1.1
randomTestSet = []
with open('randomEC.csv','r') as fin:
    fin.readline() # skip header
    num = 0
    while num < SAMPLE_SIZE:
        line = fin.readline().split(',')
        randomTestSet.append([line[0], line[5]])
        num += 1
shutdownEvent = Event()

smHost, smPort = (lambda x: (x[0],int(x[1])))(open('config','r').readline().split('#',1)[0].rsplit('/',1))
hostname = '127.0.0.1'
try: hostname = socket.gethostbyname(socket.gethostname())
except socket.gaierror as err:
    print err
    pass

def shutdown(set=False, timeout=0.0):
    """.. method:: shutdown(set=False)


    """
    global shutdownEvent
    if set:
        shutdownEvent.set()
        return(True)
    else:
        return(shutdownEvent.wait(timeout))

def interruptHandler(signum, frame):
    global shutdownEvent
    """.. method:: interruptHandler(signum, frame)

         This handler will gracefully shutdown the servers and TaskExecutors in response
         to an interrupt signal SIGINT or SIGTERM. The signal handler must be set in the main thread.
    """
    print ' motif_tester.py signal handler called!'
    shutdownEvent.set()

def main():
    
    signal(SIGTERM, interruptHandler)
    signal(SIGINT, interruptHandler)
 
    jobExecutor = DefaultProMolJobExecutor(smPort,
                                       shutdown,
                                       maxSimultaneousBatches=3,
                                       outputDir=OUTPUT_DIR)
    jobExecutor(pdbs=randomTestSet, motifs=motifs, d=d)
    shutdown(True)
    jobExecutor.join()

if __name__ == '__main__':
    START_TIME = time.time()
    print 'Go!'
    try:
        main()
    except Exception as err:
        print 'motif_tester:', err
    finally:
        FINISH_TIME = time.time()
        sec = FINISH_TIME - START_TIME
        min, sec = divmod(sec, 60)
        hrs, min = divmod(min, 60)
        print 'runtime: {}h {}m {}s.'.format(hrs,min,sec)
        print 'mischief managed'
        sys.exit(0)
