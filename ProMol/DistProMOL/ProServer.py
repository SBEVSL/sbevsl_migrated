''':mod:`ProServer` --- Lightweight server module for distributing ProMol calculations
==================================================

.. module:: ProServer
    :platform: OS X, Windows? 
    :synopsis: Lightweight server module for distributing ProMol calculations.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import sys, os, signal, platform
import socket, errno
from multiprocessing import cpu_count
import Queue, copy
from threading import Thread, Event
from subprocess import Popen, PIPE, STDOUT
#from pmg_tk.startup.ProMol.promolglobals import MOTIFSFOLDER, USRMOTIFSFOLDER, FETCH_PATH
from time import sleep

MAX_ATTEMPTS = 10 # maximum attempts to send a message

# debugging globals to supplement promolglobals imports
PLATFORM = platform.system()
PROMOL_DIR_PATH = os.path.split(os.path.dirname(__file__))[0]
try:
    HOME = os.environ['HOME']
except KeyError:
    HOME = os.environ['USERPROFILE']
if PLATFORM == 'Windows':
    OFFSITE = os.path.join(os.environ['AppData'], 'SBEVSL', 'ProMol')
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
FETCH_PATH = os.path.join(OFFSITE, PDBFOLDER)
CSV_PATH = os.path.join(OFFSITE, CSVFOLDER)
MOTIFSFOLDER = os.path.join(PROMOL_DIR_PATH, 'Motifs')
USRMOTIFSFOLDER = os.path.join(OFFSITE, 'UserMotifs')

# proserver globals
# there is probably a way to retrieve this path through PyMOL or cmd.
validPyMOLExe = ['C:\Program Files\PyMOL\PyMOL\PyMOL.exe',
                 'C:\Python27\PyMOL\PyMOL.exe',
                        '/Applications/MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL',
                        '/Users/Shared/MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL' 
                        ]
pymol = None
for exe in validPyMOLExe:
    if os.path.isfile(exe):
        pymol = exe
        break
if pymol == None:
    print 'Could not locate PyMOL executable'
    sys.exit(1)
taskExecutorPath = os.path.join(PROMOL_DIR_PATH, 'DistProMol', 'TaskExecutor.py')
#taskExecutorPath = os.path.join(PROMOL_DIR_PATH, 'TaskExecutor.py')
pymol_args = [pymol, '-qxir', taskExecutorPath] # -c has had issues
print pymol_args

try: # windows machines
    SIGINT = signal.CTRL_C_EVENT
except AttributeError: # unix-like machines
    SIGINT = signal.SIGINT
       
class ProServer(Thread):
    """.. class:: ProServer

        The ProServer class instantiates the server-side processes for distributing
        ProMOL calculations. This is a modified form of the class used to facilitate
        multiprocess ProMol on a single machine.

        ToDo: Refactor these kernel components into a 'base' class. The server for
        distributed computing will extend the base class.
    """
    def __init__(self):
        """.. method:: __init__(self)

            Initializes ProServer
        """
        Thread.__init__(self)
        self.localhost = '127.0.0.1'
        self.taskPort = 0
        self.taskPortSetEvent = Event()
        self.queue = Queue.Queue()
        self.hibernateEvent = Event()
        self._shutdownEvent = Event()

    def run(self):
        """.. method:: __init__(self)

            This overrides the Thread class' run() method, which is called by threadObject.start().
        """
        global pymol_args
        taskQueueThread = Thread(target=self.taskQueueListener,name='tql')
        taskQueueThread.start()
        logFiles = [open('/Users/D@rK KniGhT/te{0}_error.log'.format(exID), 'w') for exID in range(cpu_count())]
        taskExec = []
        self.taskPortSetEvent.wait()
        infoStr = ','.join([`self.taskPort`, MOTIFSFOLDER, USRMOTIFSFOLDER, FETCH_PATH])
        for exID, exLog in enumerate(logFiles):
            try:
                taskExec.append(Popen(pymol_args, stdin=PIPE, stdout=exLog, stderr=STDOUT))
                print 'taskExec {0}: started.'.format(taskExec[exID].pid)
            except OSError as err:
                print 'InitPyMOLError: {0}'.format(err)
                sys.exit(1)
            else:
                taskExec[exID].stdin.write(infoStr)
                taskExec[exID].stdin.close()
                print 'taskExec {0}: port# {1}  communicated'.format(exID, self.taskPort)
                continue
        while not self._shutdownEvent.wait(1.0): pass
        for ex in taskExec:
            os.kill(ex.pid, SIGINT) 
        print 'taskExec signalled'
        for ex in taskExec:
            ex.wait()
        for exLog in logFiles:
            exLog.close()
        taskQueueThread.join()

    def getTaskPort(self):
        """.. method:: getTaskPort(self)

            Waits for the task port to be set by socket initialization, then returns the port number.
        """
        self.taskPortSetEvent.wait()
        return self.taskPort

    def addTask(self, task):
        """.. method:: addTask(self, task)

             Allows intra-process tasks to be added to the queue.
        """
        self.queue.put(task)

    def interruptHandler(self, signum, frame):
        """.. method:: interruptHandler(signum, frame)

             This handler will gracefully shutdown the server and TaskExecutors in response
             to an interrupt signal SIGINT. The signal handler must be set in the main thread.
        """
        #print ' main signal handler called!'
        self.shutdown(True)

    def shutdown(self, set=False):
        """.. method:: shutdown(self, set=False)

            The shutdown method wears two hats. If called with the boolean argument 'True',
            if sets the shutdownEvent variable and returns True. When called without arguments,
            shutdown() returns the present state of the shutdownEvent variable.
        """
        if set == True:
            self._shutdownEvent.set()
            return(True)
        else:
            return(self._shutdownEvent.isSet())

    def taskQueueWorker(self, sock, addr):
        """.. method:: taskQueueWorker(self, sock, addr)

            TaskQueueWorker processes the task queue requests. These enclude requests from
            clients to enqueue a batch of tasks. Requests from TaskExecutors to dequeue a batch
            of tasks. Requests from TaskExecutors to reduce and return results to clients.

            msgmodel == True
        """
        sock.settimeout(10.0) # [seconds] 'escape hatch'
        data = '' 
        try: # outer try/except to ensure socket close
            while 1: # recv loop
                try:
                    chunk = sock.recv(1024)
                except socket.error as err:
                    if err.errno == errno.EAGAIN:  # remote socket not SHUT_WR | close: recv will timeout
                        sleep(0.0) # calling the sleep method should pass enough time
                        continue
                    else: # timeout | worse
                        raise err # for outer except to catch
                else:
                    if not chunk: # remote socket SHUT_WR sends EOF
                        break # recv loop successfully
                    else:
                        data += chunk
                        continue # recv loop
            if data[0] == 'e': # enqueue tasks
                #print 'Enqueue', '{0}/{1}'.format(addr[0], data[1:])
                self.queue.put('{0}:{1}'.format(addr[0], data[1:]))
                sock.sendall('0')
                sock.shutdown(socket.SHUT_WR)
                sock.close()
                return(0)
            elif data[0] == 'd': # dequeue tasks
                #print 'Dequeue', addr
                while 1: # dequeue loop
                    try:
                        replyData = self.queue.get(block=True, timeout=1.0)
                    except Queue.Empty:
                        if not self.shutdown():
                            continue # dequeue loop
                        else:
                            sock.close()
                            return(0)
                    else: # send task to executor
                        sock.sendall(replyData)
                        sock.shutdown(socket.SHUT_WR)
                        sock.close()
                        return(0)
            elif data[0] == 'r': # return tasks
                self.unreturnedResults(add=(data[1:].split('/',1)))
                sock.sendall('0')
                sock.shutdown(socket.SHUT_WR)
                sock.close()
                return(0)
            else:
                sock.sendall('1')
                sock.shutdown(socket.SHUT_WR)
                sock.close()
                return(0)
        except socket.error as err:
            sock.close()
            print 'taskQueueWorker: {0}'.format(err)
            return(1)
        
    def taskQueueListener(self):
        """.. method:: taskQueueListener(self)

            At server startup, the taskQueueListener binds to a free socket assigned by the
            operating system. It reports that the port number is now available for other threads
            waiting on the taskPortSetEvent. Next, it starts listening for inbound task queue
            requests. The socket timesout every second to check the status of shutdownEvent. 

            msgmodel == True
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1.0)
        sock.bind(('', self.taskPort))
        self.taskPort = sock.getsockname()[1]
        self.taskPortSetEvent.set()
        sock.listen(5)
        print 'Listening on Port: {0}'.format(self.taskPort)
        while 1: # accept loop
            try:
                new_sock, addr = sock.accept()
            except socket.timeout:
                if not self.shutdown():
                    continue # accept loop
                else:
                    sock.close()
                    return(0)
            except socket.error as err:
                print 'taskQueueListener: {0}'.format(err)
                sock.close()
                return(1)
            else: # delegate work to new thread
                qt = Thread(target=self.taskQueueWorker, args=(new_sock, addr),name='tqw')
                qt.start() # to join? or not to join?
                continue # accept loop
            
    def cancelTaskWorker(self, cancelStr=None):
        """.. method:: cancelTaskWorker(self, cancelStr)

             When called without an argument, the entire task queue is cleared. When called with
             an string of tasks to cancel, it will attempt to cancel only those tasks.
        """
        self.queue.mutex.acquire()
        taskDeque = copy.copy(self.queue.queue)
        self.queue.queue.clear()
        self.queue.mutex.release()
        if cancelStr:
            for task in taskDeque:
                if not task.startswith(cancelStr):
                    self.queue.put(task)
        
def main():
    """.. method:: main()


    """
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        pass # do not daemonize
    else:
        returnCode = daemonize()
    
    ProServer()
    print 'server shutdown'
    sys.exit(0)
 
if __name__ == '__main__':
    main()
