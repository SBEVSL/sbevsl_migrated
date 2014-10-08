''':mod:`ProServer` --- Lightweight server module for distributing ProMol calculations
==================================================

.. module:: ProServer
    :platform: OS X, Windows, Linux
    :synopsis: Lightweight server module for distributing ProMol calculations.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''
DEBUG = True # this bypasses the GUI imports and should be removed before release.
__version__ = '1.1'

# These imports should be cleaned up.
import sys, os, platform
import socket, errno
from multiprocessing import cpu_count
import Queue
from collections import Counter
try:
    from threading import Thread, Event, Semaphore, Lock, enumerate as enumThreads
except ImportError:
    from dummy_threading import Thread, Event, Semaphore, Lock, enumerate as enumThreads
try: # Windows machines require CREATE_NEW_PROCESS_GROUP for effective IPC
    from subprocess import CREATE_NEW_PROCESS_GROUP, Popen, STDOUT, call, check_output
except ImportError: 
    from subprocess import Popen, STDOUT, call, check_output
#from pmg_tk.startup.ProMol.promolglobals import MOTIFS, AminoHashTable, FETCH_PATH
from time import sleep
from cPickle import dumps, loads
from copy import deepcopy
from signal import SIGTERM, signal, SIGINT
try:
    from Daemon import daemonize # currently OS X and *NIX only
except: pass
from ProSocket import sockListenerThread, sockRecvCall, sockSendRecv
from ProJob import BaseTask
serial_glb = type('glb', (object,), {'MOTIFS' : {},
                                  'FETCH_PATH' : None,
                                  'CSV_PATH' : None,
                                  'AminoHashTable' : None
                                  })
if __name__ is not '__main__' and not DEBUG:
    import pmg_tk.startup.ProMol.promolglobals as glb
    serial_glb.FETCH_PATH = glb.FETCH_PATH
    serial_glb.CSV_PATH = glb.CSV_PATH
    serial_glb.AminoHashTable = dumps(glb.AminoHashTable)
    for key, value in glb.Motifs.iteritems():
        serial_glb.Motifs['key'] = dumps(value)
else: 
    print '\'promolglobals\' was not imported. ProServer is generating the necessary datastructures.'
    # if no-GUI, these globals must be created
    PLATFORM = platform.system()
    PROMOL_DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        HOME = os.environ['HOME']
        print HOME
    except KeyError:
        HOME = os.environ['USERPROFILE']
        print 'u:',HOME
    if PLATFORM == 'Windows':
        OFFSITE = os.path.join(os.environ['AppData'], 'SBEVSL', 'ProMol')
        print OFFSITE
    elif PLATFORM == 'Darwin':
        OFFSITE = os.path.join(HOME, 'Library', 'Application Support', 'SBEVSL',
            'ProMol')
    else:
        OFFSITE = os.path.join(HOME, '.sbevsl', 'ProMol')
    PDBFOLDER = 'PDBDownloads'
    CSVFOLDER = 'CSV'
    DIRS = ('UserMotifs', PDBFOLDER, CSVFOLDER)#changed folder name to UserMotifs for clarity
    if not os.path.isdir(OFFSITE):
        os.makedirs(OFFSITE)
    for DIR in DIRS:
        DIR = os.path.join(OFFSITE, DIR)
        if not os.path.isdir(DIR):
            os.mkdir(DIR)
    serial_glb.FETCH_PATH = os.path.join(OFFSITE, PDBFOLDER)
    serial_glb.CSV_PATH = os.path.join(OFFSITE, CSVFOLDER)
    MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs')
    USRMOTIFSFOLDER = os.path.join(OFFSITE, 'UserMotifs')
    MOTIF_DIRS = [MOTIFSFOLDER, USRMOTIFSFOLDER]

    #Amino Acid Lists from promolglobals.py
    AminoLongList = ('alanine', 'arginine', 'asparagine', 'aspartate', 'cysteine',
        'glutamine', 'glutamate', 'glycine', 'histidine', 'isoleucine', 'leucine',
        'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine',
        'tryptophan', 'tyrosine', 'valine', 'calcium', 'molybdenum',
        'molybdenum4', 'magnesium', 'zinc', 'manganese', 'sodium',
        'hemes','b12','cub','fes','hea','mos','cua','fco','sf4','f3s','fe2','cfm',
        'clf','hec','cob','c2o','pcd','4mo', 'f43', '3co', 'cobalt', 'nickle', 'iron', 'copper')
    AminoList = ('ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his',
        'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val', 
        'ca', 'mo', '4mo', 'mg', 'zn', 'mn', 'na', 'hem','b12','cub','fes','mos',
        'hea','cua','fco','sf4','f3s','fe2','cfm','clf','hec','cob','c2o','pcd','4mo','f43','3co',
        'co', 'ni', 'fe', 'cu')
    AminoShortList = ('a', 'r', 'n', 'd', 'c', 'q', 'e', 'g', 'h', 'i', 'l', 'k',
        'm', 'f', 'p', 's', 't', 'w', 'y', 'v', 'ca', 'mo', '4mo', 
        'mg', 'zn', 'mn', 'na', 'hem','b12','cub','fes','mos','hea','cua','fco',
        'sf4','f3s','fe2','cfm','clf','hec','cob','c2o','pcd','4mo','f43','3co', 'co', 'ni', 'fe', 'cu')
    AminoSubsList = {
            3:'glu',
            6:'asp',
            5:'asn',
            2:'gln',
            15:'thr',
            16:'ser'
        }
    AminoNumberList = (5, 11, 8, 8, 6, 9, 9, 4, 10, 8, 8, 9, 8, 11, 7, 6, 7, 14, 12,
        7, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49)
    AminoMinimalAtomList = {'ala':('CA', 'CB', 'CG'),
                            'arg':('CZ', 'NE', 'NH1'),
                            'asn':('CG', 'ND2', 'OD1'),
                            'asp':('CG', 'OD1', 'OD2'),
                            'cys':('CA', 'CB', 'SG'),
                            'gln':('CD', 'NE2', 'OE1'),
                            'glu':('CD', 'OE1', 'OE2'),
                            'gly':('CA', 'N', 'O'),
                            'his':('CE1', 'ND1', 'NE2'),
                            'ile':('CD1', 'CG1', 'CG2'),
                            'leu':('CD1', 'CD2', 'CG'),
                            'lys':('CD', 'CE', 'NZ'),
                            'met':('CE', 'CG', 'SD'),
                            'phe':('CD1', 'CE1', 'CZ'),
                            'pro':('CA', 'CB', 'CD'),
                            'ser':('CA', 'CB', 'OG'),
                            'thr':('CA', 'CB', 'OG1'),
                            'trp':('CE2', 'CZ2', 'NE1'),
                            'tyr':('CE1', 'CZ', 'OH'),
                            'val':('CA', 'CB', 'CG1'),
                            'mg':('MG',),
                            'zn':('ZN',),
                            'mn':('MN',),
                            'mo':('MO',),
                            'na':('NA',),
                            'hem':('NA','NB','NC'),
                            'co':('CO',),
                            'ca':('CA',),
                            'ni':('NI',),
                            'fe':('FE',),
                            'fe1':('FE1',),
                            'fe2':('FE2',),
                            'cu':('CU',),
                            'cu1':('CU1',),
                            'cu2':('CU2',)
                            }
    AminoHashTable = {}
    for i in range(0, 29):
        AminoHashTable[AminoLongList[i]] = {}
        AminoHashTable[AminoList[i]] = {}
        AminoHashTable[AminoShortList[i]] = {}

        AminoHashTable[AminoLongList[i]]['l'] = AminoLongList[i]
        AminoHashTable[AminoList[i]]['l'] = AminoLongList[i]
        AminoHashTable[AminoShortList[i]]['l'] = AminoLongList[i]

        AminoHashTable[AminoLongList[i]][3] = AminoList[i]
        AminoHashTable[AminoList[i]][3] = AminoList[i]
        AminoHashTable[AminoShortList[i]][3] = AminoList[i]

        AminoHashTable[AminoLongList[i]][1] = AminoShortList[i]
        AminoHashTable[AminoList[i]][1] = AminoShortList[i]
        AminoHashTable[AminoShortList[i]][1] = AminoShortList[i]
        
        AminoHashTable[AminoLongList[i]][0] = AminoNumberList[i]
        AminoHashTable[AminoList[i]][0] = AminoNumberList[i]
        AminoHashTable[AminoShortList[i]][0] = AminoNumberList[i]

        try:
            AminoHashTable[AminoLongList[i]]['m'] = AminoMinimalAtomList[AminoList[i]]
            AminoHashTable[AminoList[i]]['m'] = AminoMinimalAtomList[AminoList[i]]
            AminoHashTable[AminoShortList[i]]['m'] = AminoMinimalAtomList[AminoList[i]]
        except KeyError: pass
        
        if i in AminoSubsList:
            AminoHashTable[AminoLongList[i]]['s'] = AminoSubsList[i]
            AminoHashTable[AminoList[i]]['s'] = AminoSubsList[i]
            AminoHashTable[AminoShortList[i]]['s'] = AminoSubsList[i]
    del i
    serial_glb.AminoHashTable = dumps(AminoHashTable)

    # this abridged version of loading the motifs should be replaced with the full version.
    MOTIFS = {}
    for MOTIF_DIR in MOTIF_DIRS:
        motif, motifFile = '', ''
        for file in os.listdir(MOTIF_DIR):
            if file.endswith('.py'):
                motifFile = os.path.join(MOTIF_DIR,file)
                motif = file.rsplit('.',1)[0]
                serializedMOTIF = {}
                serializedMOTIF['path'] = motifFile
                # resi
                with open(motifFile, 'r') as fin:
                    for line in fin.readlines(): # readlines loop
                        if line[0:4] == 'RESI':
                            resi = line.split(':')[1][0:-1].strip().lower()
                            serializedMOTIF['resi'] = resi.split(',')
                            continue
                        elif line[0:4] == 'LOCI':
                            loci = line.split(':')[1][0:-1].strip().split(';')
                            selection = ''
                            # Added to prevent crash on bad loci (it happened to us)
                            badLoci = False # Needed to break out twice
                            for loc in loci:
                                if loc == '':
                                    continue
                                # Take each block separated by semicolons and further break it up at hyphens
                                splitlist = loc.split('-')
                                # If there is one and only one hyphen, what's before is the chain and
                                # what's after is the residue numbers; otherwise, it's bad
                                if len(splitlist) == 2:
                                    # This uses automatic list unpacking
                                    chain, numbers = splitlist
                                else:
                                    badLoci = True
                                    break
                                # Starts with the string numbers which is a comma separated list of numbers
                                # from after the hyphen in this section of the loci attribute (sections being separated by semicolons).
                                # (In other words, X,Y,Z where the motif header line is roughly LOCI:...;A-X,Y,Z;...)
                                # Then creates a string called nums which contains each number prefaced by 'resi'
                                # and separated by 'or's, all with spaces in between.  There will be extra spaces
                                # if the initial numbers string contains extra spaces after the commas or elsewhere.
                                # I think the resulting string is a PyMOL selection algebra snippet which, individually,
                                # would select any and all residues in the entire structure matching any of the residue numbers.
                                nums = 'resi %s' % ' or resi '.join(numbers.split(','))
                                # This wraps the resulting string in more algebra that will restrict those matches to only residues on
                                # the chain specified before the hyphen in this section.  It then builds a string called
                                # selection which, after the last iteration, should select the union of all sections of the LOCI attribute
                                # (which would match any and all residues with the proper numbers on the proper chains as specified there).
                                if selection == '':
                                    selection = '(chain %s and (%s))' % (chain, nums)
                                else:
                                    selection = '%s or (chain %s and (%s))' % (selection, chain, nums)
                            if badLoci:
                                break
                            serializedMOTIF['loci'] = selection
                            break # readlines loop
                serial_glb.MOTIFS[motif] = dumps(serializedMOTIF)
print 'motifs imported'
_shutdownEvent = Event()
_hibernationEvent = Event()
ACTIVE_STATE = True
TARE_USERS = 1

# there is a better way to do this. maybe in the platform specific statements above
# and or the config file
validPyMOLExe = ['C:\Python27\PyMOL\PyMOL.exe',
                        '/sw/lib/pymol-py27/bin/pymol',
                        '/opt/pymol-svn/pymol',
                        '/Applications/MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL',
                        '/Users/Shared/MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL',
                        'MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL',
                        'MacPyMOL.app/Contents/MacOS/MacPyMOL'
                        ]
pymol = None
for exe in validPyMOLExe:
    if os.path.isfile(exe):
        pymol = exe
        break
if pymol == None:
    print 'Could not locate PyMOL executable'
    sys.exit(1)
    
taskExecutorPath = os.path.join(os.path.dirname(__file__), 'TaskExecutor.py')
pymol_args = [pymol, '-qxir', taskExecutorPath] # -c has had issues on some windows builds
print pymol_args
MAX_TASKEXECUTORS = 1 #cpu_count()
       
class BaseProServer(Thread):
    """.. class:: BaseProServer(Thread)

        The ProServer class extends Thread and instantiates the server-side processes for
        distributing ProMOL calculations. This is a modified form of the class used to facilitate
        parallel execution of multiple PyMOL instances on a single machine.

    """
    def __init__(self, shutdownFunc=None, distributed=0):
        """.. method:: __init__(self, shutdownFunc=None, distributed=0)

            Initializes ProServer with a function that communicates a shutdown event.
            
        """
        Thread.__init__(self)
        self.localhost = '127.0.0.1'
        self.taskPort = 0
        self.taskPortSetEvent = Event()
        self.queue = Queue.Queue()
        self.taskRestartEvent = {chr(n):Event() for n in range(1,MAX_TASKEXECUTORS+1)}
        self._tasksInProgressMutex = {chr(n):Lock() for n in range(1,MAX_TASKEXECUTORS+1)}
        self._tasksInProgress = {chr(n):{} for n in range(1,MAX_TASKEXECUTORS+1)}
        self.taskQueueCallables = {'d' : self.taskDequeueRequest,
                'r' : self.taskCompletedRequest
                }
        if shutdownFunc is not None: self.shutdown = shutdownFunc
        self.DISTRIBUTED = distributed
        print 'init: ',self.DISTRIBUTED

    def run(self):
        """.. method:: run(self)

            This overrides the Thread class' run() method, which is called by <ProServer instance>.start().
            
        """
        self.initBackgroundThreads()
        logFiles = [open('te{0}_error.log'.format(exID), 'w') for exID in range(1,1+MAX_TASKEXECUTORS)] 
        taskExec = []
        envDict = os.environ.copy()
        envDict['AminoHashTable'] = serial_glb.AminoHashTable
        envDict['FETCH_PATH'] = serial_glb.FETCH_PATH
        taskExecSema = Semaphore(len(logFiles))
        self.taskPortSetEvent.wait()
        envDict['taskPort'] = `self.taskPort`
        envDict['DISTRIBUTED'] = `self.DISTRIBUTED`
        kwargs = {'stderr':STDOUT, 'env':envDict}
        try:
            kwargs['creationflags'] = CREATE_NEW_PROCESS_GROUP
        except NameError:
            pass
        try:
            ##for exID, exLog in enumerate(logFiles):
            while 1:
                taskExecSema.acquire()
                if self.shutdown(timeout=1.0): # slowly initialize full set of TaskExecutors
                    print 'post sema shutdown'
                    break # while loop
                ##envDict['logFile'] = exLog
                exID = None
                for id, ex in enumerate(taskExec):
                    if ex.isAlive() in [False, None]:
                        exID = id+1
                        self.taskRestartEvent[chr(exID)].set() # if a pymol instance crashes ensure its task was completed.
                        kwargs['env']['exID'] = str(exID)
                        kwargs['stdout'] = logFiles[exID-1]
                        taskExec[exID-1] = Thread(target=self.initTaskExecutor, args=(taskExecSema,
                                                                       pymol_args, kwargs))
                        break # for loop
                else: # for loop unbroken
                    if len(taskExec) >= cpu_count():
                        print 'len(taskExec) = {}'.format(len(taskExec))
                        break # while loop
                    else:
                        exID = len(taskExec)+1
                        kwargs['env']['exID'] = str(exID)
                        kwargs['stdout'] = logFiles[exID-1]
                        taskExec.append(Thread(target=self.initTaskExecutor, args=(taskExecSema,
                                                                       pymol_args, kwargs)))
                taskExec[exID-1].setDaemon(True)
                taskExec[exID-1].start()
                print 'taskExec {0}: started.'.format(exID)
        except OSError as err:
            print 'InitPyMOLError: {0}'.format(err)
            sys.exit(1)
        else: pass
        finally:
            for exLog in logFiles:
                exLog.close()

    def initBackgroundThreads(self):
        """.. method:: initBackgroundThreads(self)

            This method launches the task queue listener thread, which handles requests
            to enqueue or dequeue tasks from the queue.
            
        """
        self.taskQueueThread = Thread(target=self.taskQueueListener,name='tql')
        self.taskQueueThread.setDaemon(True)
        self.taskQueueThread.start()

    def initTaskExecutor(self, sema, pymol_args, kwargs):
        """.. method:: initTaskExecutor(self, sema, pymol_args, kwargs)

             Initializes TaskExecutor subprocess.
             
        """
        try:
            ex = Popen(pymol_args, **kwargs)
            while ex.poll() is None and not self.shutdown():
                self.shutdown(timeout=10.0)
        finally:
            try: ex.terminate()
            except BaseException as err:
                print err
            print 'shutdown task executors'
            ex.wait()
            sema.release()           

    def getTaskPort(self):
        """.. method:: getTaskPort(self)

             Waits for the task port to be set by socket initialization, then returns the port number.
             
        """
        self.taskPortSetEvent.wait()
        return self.taskPort

    def addTask(self, task):
        """.. method:: addTask(self, task)

             Allows intra-process tasks to be added to the queue. This is the principle means of
             submitting tasks to a local ProServer instance. The Mofit data are coupled to the task before
             it is enqueued. If and when memory consumption becomes a concern, this coupling
             can be performed after a task is dequeued.
             
        """
        try: self.queue.put(BaseTask.augment(task, serial_glb.MOTIFS[BaseTask.serializedName(task).split('/',2)[1]]))
        except BaseException as err:
            print err
            self.queue.put(task)
        return '0'

    def taskDequeueRequest(self, data, sock, addr):
        """.. method:: taskDequeueRequest(self, data, sock, addr)

            This method handles requests from the TaskExecutors. Each TaskExecutor has an ID.
            When a task is delegated to a TaskExecutor, the task is appended to that executor's
            tasksInProgress list. When a TaskExecutor restarts (for whatever reason), the
            taskRestartEvent for that executor ID is set. When the taskRestartEvent is set, the
            tasksInProgress list is checked to ensure that the task was completed and returned prior
            the TaskExecutor restarting. If not, the task is redeligated for completion.* 

            *Future work: restarting an uncompleted task an indefinite amout of times is bad practice.
            A corrupt task will continue to crash a TaskExecutor indefinitely. ProServer should
            give up on the task after a finite number of attempts.
            
        """
        #p#print 'dequeue',ord(data[1]) #p#
        sock.settimeout(None)
        if self.hibernationEvent():
            self.shutdown(timeout=None)
            return '0'
        replyData = None
        reset = False
        try: reset = self.taskRestartEvent[data[1]].isSet()
        except BaseException: print err
        if self.taskRestartEvent[data[1]].isSet():
            #self._tasksInProgressMutex[data[1]].acquire()
            try: replyData = self._tasksInProgress[data[1]].values()[0]
            except BaseException as err: print err
            finally: pass #self._tasksInProgressMutex[data[1]].release()
            self.taskRestartEvent[data[1]].clear()
            if replyData != None:
                #p#print 'leftovers: ',Task.serializedName(replyData),'sent to',ord(data[1]) #p#
                return replyData
        #p#print 'dequeue post-restart task event' #p#
        while 1:
            try: replyData = self.queue.get(block=True, timeout=1.0)
            except Queue.Empty:
                if self.shutdown(): return '0'
            else:
                self._tasksInProgressMutex[data[1]].acquire()
                try: self._tasksInProgress[data[1]][BaseTask.serializedName(replyData)] = replyData
                except BaseException as err: print err # for observing how this fails
                finally: self._tasksInProgressMutex[data[1]].release()
                return replyData

    def taskCompletedRequest(self, data, sock, addr):
        """.. method:: taskCompletedRequest(self, data, sock, addr)

            When a task has been completed and returned, it is removed from the tasksInProgress
            list for that TaskExecutor.
            
        """
        #taskName, returnAddr = BaseTask.serializedNameAddr(data[2:])
        print taskName,'completed by',ord(data[1]) #p#
        self._tasksInProgressMutex[data[1]].acquire()
        try: del self._tasksInProgress[data[1]][data[2:]]
        finally: self._tasksInProgressMutex[data[1]].release()
        #self.unreturnedResults(add=(returnAddr,[data[2:]]))
        return '0'

    def setTaskPort(self, port):
        """.. method:: setTaskPort(self, port)

            This method is passed as an argument to sockListenerThread when instantiating the
            task queue listener thread. After the operating system assigns a free port to the listener,
            the port number may be passed to the TaskExecutors.
            
        """
        self.taskPort = port
        self.taskPortSetEvent.set()

    def hibernationEvent(self):
        """.. method:: hibernationEvent(self)

            Classes extending ProServer may override this method to support hibernation behavior.
            
        """
        return False
        
    def taskQueueListener(self):
        """.. method:: taskQueueListener(self)

            At server startup, the taskQueueListener binds to a free socket assigned by the
            operating system. It reports that the port number is now available for other threads
            waiting on the taskPortSetEvent. Next, it starts listening for inbound task queue
            requests. The socket will timeout every second to check the status of shutdownEvent. 

        """
        sockListenerThread(portSetTarget=self.setTaskPort,
                           workerCallables=self.taskQueueCallables,
                           shutdownTarget=self.shutdown)

    def cancel(self):
        """.. method:: cancel(self)

            This method provides intra-process access to cancel all the tasks in the queue.
            
        """
        self.cancelTaskWorker()
            
    def cancelTaskWorker(self, cancelReturnAddr=None):
        """.. method:: cancelTaskWorker(self, cancelReturnAddr=None)

             When called without an argument, the entire task queue is cleared. When called with
             a string of tasks to cancel, it will attempt to cancel only those tasks.
             
        """
        self.queue.mutex.acquire()
        taskList = list(self.queue.queue)
        self.queue.queue.clear()
        self.queue.mutex.release()
        if cancelReturnAddr is not None:
            for task in taskList:
                if BaseTask.serializedAddr(task) is not cancelReturnAddr:
                    self.queue.put(task)
