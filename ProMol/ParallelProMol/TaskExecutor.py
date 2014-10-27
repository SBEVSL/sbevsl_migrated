''':mod:`TaskExecutor` --- Script for executing tasks within PyMOL
==================================================

.. module:: TaskExecutor
    :platform: OS X, Windows, Linux
    :synopsis: Script for executing tasks within PyMOL.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

# These imports should be cleaned up
import sys, os, signal, platform, types
resource_available = True
try:
    import resource
except BaseException as err:
    resource_available = False
    print err
import socket, errno
from threading import Thread, Event, Lock
from pymol import cmd, stored
from cPickle import loads, dumps
from time import sleep, clock
from signal import SIGTERM, SIGINT, signal
from collections import Counter
from Logger import Logger
from ProSocket import sockSendRecv
from ProJob import BaseTask, DefaultProMolWorkflow

# log statements should be removed before release
logThread = Logger()
logThread.start()
log = logThread.write

log('TaskExecutor.py has been started in PyMOL.exe!')

AminoHashTable = loads(os.environ['AminoHashTable'])
del os.environ['AminoHashTable']
print 'AHT'
FETCH_PATH = os.environ['FETCH_PATH']
del os.environ['FETCH_PATH']
print 'FP'
exID = chr(int(os.environ['exID']))
print int(os.environ['exID'])
DISTRIBUTED = int(os.environ['DISTRIBUTED'])
del os.environ['DISTRIBUTED']
print DISTRIBUTED

MAX_MEM = 3*(10**8)

class TaskExecutor:
    """.. class:: TaskExecutor

        The TaskExecutor class instantiates the server-side processes within a PyMOL instance.
        Currently, the DefaultProMolWorkflow is supported. 
        
    """
    def __init__(self, taskPort):
        """.. method:: __init__(self, queuePort)

            The TaskExecutor is initialized. The workflows this TaskExecutor can perform are
            instantiated in the workflowDict attribute.
              
        """
        try:
            self.workflowDict = {'DefaultProMolWorkflow' : DefaultProMolWorkflow(AminoHashTable,
                                                                                 FETCH_PATH)}
            print 'wf'
            self.taskPort = taskPort
            print self.taskPort
            self._shutdownEvent = Event()
            print 'se'
            self.returnTask = self.returnTaskToReducer if DISTRIBUTED else self.returnTaskToClient
            print 'rt'
            try: # will not work if this is not the main thread of PyMOL
                signal(SIGTERM, self.interruptHandler)
                signal(SIGINT, self.interruptHandler)
            except Exception as err:
                print 'init TE:', err
            print 'sig'
            while 1: # execute loop
                try: self.executeTask()
                except Exception as err:
                    print 'et:', err
                if resource_available and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > MAX_MEM:
                    log('memory exceeded')
                    self.shutdown(True)
                    sleep(0.5)
                    break
                if self.shutdown():
                    log('shutdown TaskExecutor')
                    break
        finally:
            cmd.quit()

    def interruptHandler(self, signum, frame):
        """.. method:: interruptHandler(self, signum, frame)

            The shutdown handler enables orderly shutdown in response to SIGINT or SIGTERM.
            The signal handler must be declared in the main thread. TaskExecutor may not be in
            the main thread of the PyMOL instance.
    
        """
        log('TaskExecutor: shutdown signal handler called!')
        self.shutdown(True)

    def shutdown(self, set=False, timeout=0.0):
        """.. method:: shutdown(self, set=False)

            If called without arguments, this method returns the current state of the shutdown
            event. If called with a value that is equivalent to the the boolean, True, it will set
            the shutdown event and return true. If called with a keyword argument assigning
            a positive float value to 'timeout.' It will wait 'timeout' seconds or until the shutdown
            event is set (which ever is shorter) before returning the value of the shutdown event.
              
        """
        if set:
            self._shutdownEvent.set()
            return(True)
        else:
            return(self._shutdownEvent.wait(timeout))

    def returnTaskToReducer(self, task):
        """.. method:: returnTask(self, returnAddr, resultStr)

           Returns the task result to ProServer process where results from multiple
           TaskExecutors are reduced/aggregated and returned to the client.
           This is the default behavior of a TaskExecutor initialized by a remote
           ProServer instance.
           
        """
        print 'return to reducer: ',task['Name']
        sockSendRecv('r'+exID+'%s'%task.serialize(), self.taskPort)                   

    def returnTaskToClient(self, task):
        """.. method:: returnTaskToClient(self, returnAddr, resultStr)

           Returns the task result directly to the client. This method will bypass reduction
           of results by the ProServer module. This is the default behavior of a TaskExecutor
           initialized on a local ProServer instance.
           
        """
        sockSendRecv('r%s'%dumps([task.serialize()]), task['Return Address'][1])
        sockSendRecv('r'+exID+'%s'%task['name'], self.taskPort)

    def executeTask(self):
        """.. method:: executeTask(self)

            This method will wait for a task from ProServer, execute the workflow on the task, and
            return the result.
                  
        """
        print 'd%s' % exID
        try:
            taskStr = sockSendRecv('d%s'%exID,port=self.taskPort)
        except Exception as err:
            print 'etd:', err
        if not taskStr:
            print 'no_et'
            return
        print 'et:', taskStr[:10] #p#
        task, motifData = BaseTask.deserializeAugmented(taskStr)
        #p#log('task: %s \nmotifData: %s'%(task['name'],motifData)) #p#
        task['motifData'] = motifData
        task['Total runtime [sec]'] = clock()
        try: self.workflowDict[task['Workflow']](task)
        finally:
            task['Total runtime [sec]'] = clock() - task['Total runtime [sec]']
            #p#print 'task runtime:',task['Total runtime [sec]'] #p#
            try: task['MotifCaller() runtime [%]'] = task['MotifCaller() runtime [sec]']/task['Total runtime [sec]']*100
            except: pass
            del task['motifData']
            Thread(target=self.returnTask, args=(task,)).start()
            cmd.delete(task['Motif'])

def main():
    """.. method:: main()

        The main method instantiates a TaskExecutor with the taskPort value taken from the
        environment variables.
              
    """
    TaskExecutor(int(os.environ['taskPort']))
    sys.exit(0) # this should be superfluous

if __name__ == '__main__':
    main()
