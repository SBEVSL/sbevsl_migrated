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
from ProJob import MotifTestJobExecutor

import os, time
import sys

SAMPLE_SIZE = 0
NUM_OF_MOTIFS = None
PROMOL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = 'TestResults'
#validMotifs = [f.rsplit('_',1)[0] for f in os.listdir(os.path.join(PROMOL_DIR, 'Motifs'))]
motifs = [f.split('.')[0] for f in os.listdir(os.path.join(PROMOL_DIR, 'Motifs'))
             if f.startswith('S_1cam') and not f.startswith('M_1hto') ][:NUM_OF_MOTIFS]
#sys.exit()
#motifs = [m for m in allMotifs if m.startswith('S') and 'A'+m[1:] in allMotifs]
#motifs = allMotifs[:NUM_OF_MOTIFS]
pdbs = {} #{m[1] : '.'.join(m[2].split('_')) for m in map(lambda x: x.split('_',2), motifs)}
d = 0.0
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
 
    jobExecutor = MotifTestJobExecutor(smPort,
                                       shutdown,
                                       outputDir=OUTPUT_DIR)
    jobExecutor(motifs=motifs, randomTestSet=randomTestSet, d=d)
    shutdown(True)
    jobExecutor.join()

if __name__ == '__main__':
    START_TIME = time.time()
    print 'Go!'
    try:
        main()
    finally:
        FINISH_TIME = time.time()
        sec = FINISH_TIME - START_TIME
        min, sec = divmod(sec, 60)
        hrs, min = divmod(min, 60)
        print 'runtime: {}h {}m {}s.'.format(hrs,min,sec)
        print 'mischief managed'
        sys.exit(0)
