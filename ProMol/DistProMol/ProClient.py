''':mod:`ProClient` --- Lightweight client module for distributing ProMol calculations
==================================================

.. module:: ProClient
    :platform: OS X
    :synopsis: Lightweight client module for distributing ProMol calculations.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import sys
import socket, ssl, errno
from multiprocessing import Process, freeze_support
from threading import Thread, Lock, Event, Semaphore
from random import choice
# imports for debugging
from time import sleep

MAX_ATTEMPTS = 10 # maximum attempts to send a message
BATCH_SIZE = 10

class ProClient:
    """.. class:: ProClient

        The ProClient class instantiates the client-side processes for distributing ProMOL calculations.
    """
    def __init__(self, resultPort, serverManagerHost, serverManagerPort, job):
        """.. method:: __init__(self, serverManagerHost, serverManagerPort, job)


        """
        self.smHost = serverManagerHost
        self.smPort = serverManagerPort
        self.resultPort = resultPort
        returnCode = self.getServerHostList()
        if returnCode: 
            sys.exit(1) # exit unsuccessfully: [errno=1] server manager error
        returnCode = self.submitJob(job)
        #sleep(5.0)
        #self.cancelTasks()
        if returnCode:
            sys.exit(2) # exit unsuccessfully: [errno=2] job submit error
        sys.exit(0) # exit successfully!

    def getServerHostList(self):
        """.. method:: getServerHostList(self)

           msgmodel == True
        """
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS): # attempt loop
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.settimeout(10.0) # [seconds] 'escape hatch'
                try:
                    sock.connect((self.smHost, self.smPort))
                except socket.error as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        print 'Connection with host: {0} Refused.'.format(self.smHost)
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err
                else:
                    sock.sendall('r') 
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    serverStr = ''
                    while 1: # recv loop
                        try:
                            chunk = sock.recv(1024)
                        except socket.error as err:
                            if err.errno is errno.EAGAIN:
                                #print 'sock.recv: {0}'.format(err)
                                sleep(0.0) # calling the sleep method should pass enough time
                                continue # recv loop
                            else: # something happened on the remote end
                                raise err # for outer except to catch
                        else:
                            if not chunk: # remote socket SHUT_WR sends EOF
                                break # recv loop successfully
                            else:
                                serverStr += chunk
                                continue # recv loop
                    sock.close()
                    #print 'serverStr: {0}'.format(serverStr)
                    if serverStr in ['', '1']:
                        continue # next attempt
                    else:
                        self.serverHostList = [ tuple(host.split(':')) for host in serverStr.strip().split('\t') ]
                        #for host, port in self.serverHostList:
                        #    print '{0}:{1}'.format(host,port)
                        return(0) # successfully
            except socket.error as err:
                sock.close()
                print 'getServerHostList: {0}'.format(err)
                continue # next attempt
        return(1) # return unsuccessfully after MAX_ATTEMPTS
    
    # send task to server
    def submitJob(self, job):
        """.. method:: submitJob(self, job)

           msgmodel == True
        """
        submitThreads = []
        for taskBody in job:
            task = 'e{0}/{1}'.format(self.resultPort, taskBody)
            #print 'task: {0}'.format(task)
            #self.submitPool.acquire()
            #self.submitPool.release()
            st = Thread(target=self.submitTask, args=(task, job))
            st.start()
            submitThreads.append(st)
        for thread in submitThreads:
            thread.join()
        print 'submit threads joined'

    def submitTask(self, task, job):
        #self.submitPool.acquire()
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS):
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                host = choice(self.serverHostList) # randomly choose host from server list
                sock.settimeout(10.0) # [seconds] 'escape hatch'
                try:
                    sock.connect((host[0], int(host[1])))
                except BaseException as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        print 'Connection w/ {0}: Refused. [{1}]'.format(socket.gethostbyaddr(host[0])[0],task[:30])
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err # --> outer except block
                else:
                    sock.sendall(task) 
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    returncode = None
                    while 1: # recv loop
                        try:
                            returncode = sock.recv(1)
                        except BaseException as err:
                            if err.errno is errno.EAGAIN:
                                #print 'sock.recv: {0}'.format(err)
                                sleep(0.0) # calling the sleep method should pass enough time
                                continue # recv loop
                            else: # something happened on the remote end
                                raise err # --> outer except block
                        else:
                            break # recv loop successfully
                    sock.close()
                    if returncode != '0':
                        continue # next attempt
                    else:
                        job.taskSentTo(task.split('/',1)[1], host[0])
                        #print '{0} sent to: {1}'.format(task[:30], socket.gethostbyaddr(host[0])[0])
                        #self.submitPool.release()
                        return(0) # attempt loop successfully
            except BaseException as err: # outer except block
                sock.close()
                print 'submitJob w/ {0} and {1}: {2}'.format(socket.gethostbyaddr(host[0])[0], task[:30], err)
                continue # next attempt
        print 'task: {0} not submitted'.format(task[:30])
        #self.submitPool.release()
        return(1)

    def cancelTasks(self, tasks=None):
        """.. method:: cancelTasks(self, tasks)

           msgmodel == True
        """
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS): # attempt loop
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.settimeout(10.0) # [seconds] 'escape hatch'
                try:
                    sock.connect((self.smHost, self.smPort))
                except socket.error as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        print 'CancelTasks with host: {0} Refused.'.format(self.smHost)
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err
                else:
                    sock.sendall('c{0}'.format(self.resultPort))
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    returncode = ''
                    while 1: # recv loop
                        try:
                            returncode = sock.recv(1)
                        except socket.error as err:
                            if err.errno is errno.EAGAIN:
                                #print 'sock.recv: {0}'.format(err)
                                sleep(0.0) # calling the sleep method should pass enough time
                                continue # recv loop
                            else: # something happened on the remote end
                                raise err # for outer except to catch
                        else:
                            break # recv loop successfully
                    sock.close()
                    #print 'serverStr: {0}'.format(serverStr)
                    if returncode in ['', '1']:
                        continue # next attempt
                    else:
                        return(0) # successfully
            except socket.error as err:
                sock.close()
                print 'cancelTasks: {0}'.format(err)
                continue # next attempt
        return(1) # return unsuccessfully after MAX_ATTEMPTS       

class JobResult:
    """.. class:: JobResult

        The JobResult class instantiates the client-side processes for compiling the results retruned
        from server-side ProMOL calculations.
    """
    def __init__(self, job):
        """.. method:: __init__(self, job, port)


        """
        self.job = job
        self.host, self.port = '', 0
        self.resultPortSetEvent = Event()
        self._shutdownEvent = Event()
        self._shutdownEventLock = Lock()
                      
    def jobResultListener(self):
        """.. method:: jobResultListener(self)

           msgmodel == True
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##        sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
##                               ca_certs=None,
##                               cert_reqs=ssl.CERT_NONE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1.0)
        sock.bind((self.host, 0)) # OS chooses open port
        self.port = sock.getsockname()[1]
        print 'port: {0}'.format(self.port)
        self.resultPortSetEvent.set()
        sock.listen(5)
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
                print 'jobResultListener: {0}'.format(err)
                sock.close()
                return(1)
            else: # delegate work to new thread
##                new_sock = ssl.wrap_socket(new_sock, server_side=True, certfile=None,
##                                           keyfile=None, ssl_version=ssl.PROTOCOL_SSLv23)
                jrmt = Thread(target=self.jobResultWorker, args=(new_sock, addr))
                jrmt.start()
                continue # accept loop

    def getResultPort(self):
        self.resultPortSetEvent.wait()
        return self.port

    def shutdown(self, set=False):
        """.. method:: shutdown(self, set=False)


        """
        if set is True:
            self._shutdownEventLock.acquire()
            self._shutdownEvent.set()
            self._shutdownEventLock.release()
            return(True)
        else:
            self._shutdownEventLock.acquire()
            set = self._shutdownEvent.isSet()
            self._shutdownEventLock.release()
            return(set)

    def listenerThread(self):
        """.. method:: listenerThread(self)


        """
        listener = Thread(target=self.jobResultListener)
        listener.start()
        return listener

    def jobResultWorker(self, sock, addr):
        """.. method:: jobResultWorker(self, sock, addr)

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
                        #print 'worker: {0}'.format(err)
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
            # verify data
            sock.sendall('0')
            sock.shutdown(socket.SHUT_WR) 
            sock.close()
            #print 'ResultData: {0}'.format(data) # do something with data received
            self.job.addResults(data)
            return(0)
        except socket.error as err:
            sock.close()
            print 'jobResultWorker: {0}'.format(err)
            return(1) 
      

    def taskTracker(self, timeout=0.0):
        """.. method:: taskTracker(self)


        """
        return self.job.taskTracker(timeout)

    def resultsMissed(self):
        """.. method:: resultsMissed(self)


        """
        return self.job.resultsMissed()

    def tasksComplete(self):
        """.. method::  tasksComplete(self)


        """
        return self.job.tasksComplete()

    def results(self, timeout=60.0):
        """.. method::  results(self, timeout=60.0)


        """
        return self.job.results(timeout)

    def resultsOutstanding(self, taskName=None):
        return self.job.resultsOutstanding(taskName)
        
class Job:
    """.. class:: Job

        The Job class instantiates the list of tasks to be completed by remote
        server processes.
    """
    def __init__(self, taskDict={}, batchsize = BATCH_SIZE):
        """.. method:: __init__(self, taskList=[])


        """
        self.BATCH_SIZE = batchsize
        self._taskDict = taskDict
        self._taskDictLock = Lock()
        self._resultDict = {}
        self._resultDictLock = Lock()
        self._resultsOutstanding = { taskName : '' for taskName in taskDict.keys() }
        self._resultsOutstandingLock = Lock()
        self._tasksComplete = 0
        self._tasksCompleteLock = Lock()
        self._taskCompletedEvent = Event()
        self._resultsReadyEvent = Event()

    def addTask(self, task):
        """.. method:: addTask(self, task)


        """
        self._taskDictLock.acquire()
        self._taskDict[task[0]] = [task[1]]
        self._taskDictLock.release()
        self._resultsOutstandingLock.acquire()
        self._resultsOutstanding.append(task[0])
        self._resultsOutstandingLock.release()

    def __iter__(self):
        """.. method:: __iter__(self)


        """
        for index in range(0, len(self._taskDict), self.BATCH_SIZE):
            yield '&'.join(self._taskDict.values()[index:index+self.BATCH_SIZE])

    def tasks(self):
        return self._taskDict.items()

    def addResults(self, resultStr):
        """.. method:: addResult(self, result)


        """
        #print 'addResult: {0}'.format(resultString)
        totalTasks = 0
        for result in resultStr.split('&'): # parse individual task results
            taskName, taskResult = result.split('/')
            self._resultDictLock.acquire()
            self._resultDict[taskName] = taskResult
            self._resultDictLock.release()
            self.resultsOutstanding(taskName)
            totalTasks+=1
        #self.incTasksComplete(totalTasks)

    def results(self, timeout=60.0):
        """.. method:: results(self)


        """
        self._resultsReadyEvent.wait(timeout)
        return self._resultDict.items()

    def size(self):
        """.. method:: size(self)


        """
        self._taskDictLock.acquire()
        return len(self._taskDict)
        self._taskDictLock.release()

    def taskSentTo(self, task, host):
        self._resultsOutstandingLock.acquire()
        for taskName in task.split('&'):
            self._resultsOutstanding[taskName] = host
        self._resultsOutstandingLock.release()
##        for taskName in task.split('&'):
##            try:
##                print '{0} sent to {1}'.format(taskName, socket.gethostbyaddr(host)[0])
##            except:
##                print '{0} sent to h: {1}'.format(taskName, host)

    def taskTracker(self, timeout=0.0):
        """.. method:: taskTracker(self)


        """
        self._taskCompletedEvent.wait(timeout)
        return self.tasksComplete()

    def resultsOutstanding(self, taskName=None):
        """.. method:: incResultsMissed(self)


        """
        if taskName:
            self._resultsOutstandingLock.acquire()
            try:
                del self._resultsOutstanding[taskName]
            except BaseException as err:
                print '{0} already returned: [{1}]'.format(taskName, err)
                self._resultsOutstandingLock.release()
            else:
                numOutstanding = len(self._resultsOutstanding)
                self._resultsOutstandingLock.release()
                self.incTasksComplete()
                if not numOutstanding:
                    self._resultsReadyEvent.set()
        else:
            self._resultsOutstandingLock.acquire()
            outstanding = self._resultsOutstanding.items()
            self._resultsOutstandingLock.release()
            return outstanding

    def incTasksComplete(self, numOfTasks=1):
        """.. method:: incTasksComplete(self)


        """
        self._tasksCompleteLock.acquire()
        self._tasksComplete += numOfTasks
        tasksComplete = self._tasksComplete
        self._tasksCompleteLock.release()
        self._taskCompletedEvent.set()
        self._taskCompletedEvent.clear()

    def resultsMissed(self):
        """.. method:: resultsMissed(self)


        """
        self._resultsMissedLock.acquire()
        missed = self._resultsMissed
        self._resultsMissedLock.release()
        return missed

    def tasksComplete(self):
        """.. method:: tasksComplete(self)


        """
        self._tasksCompleteLock.acquire()
        tasks = self._tasksComplete
        self._tasksCompleteLock.release()
        return tasks

def main():
    """.. method:: main()


    """
    serverManagerHost = sys.argv[1]
    serverManagerPort = int(sys.argv[2])
    job = ['e\t50007\ttask {0}'.format(i) for i in range(0,3)]
    client = Process(target=ProClient,args=(serverManagerHost, serverManagerPort, job))
    client.start()
    result = JobResult(job, 50007)
    client.join()

if __name__ == '__main__':
    freeze_support()
    main()
