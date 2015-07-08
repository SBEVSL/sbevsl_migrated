''':mod:`ProServer` --- Lightweight server module for distributing ProMol calculations
==================================================

.. module:: ProServer
    :platform: OS X
    :synopsis: Lightweight server module for distributing ProMol calculations.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import sys
import os
import socket
import getpass
import signal
from multiprocessing import Process, freeze_support
import Queue
from threading import Thread, Event, Lock
from subprocess import Popen, PIPE
from Daemon import daemonize
# debugging imports
from time import sleep

shutdownEvent = Event()
shutdownEventLock = Lock()
       
class ProServer:
    """.. class:: ProServer

        The ProServer class instantiates the server-side processes for distributing
        ProMOL calculations.
    """
    def __init__(self):
        """.. method:: __init__(self)

            Initializes ProServer
        """
        self.localhost = ''
        self.localport = 50007
        self.queue = Queue.Queue()
        self._shutdownEvent = Event()
        self._shutdownEventLock = Lock()
        self.taskQueueListener(self.localport)

    def interruptHandler(self, signum, frame):
        """.. method:: interruptHandler(self, signum, frame)

              
        """
        print 'signal handler called!'
        self.shutdown(True)

    def shutdown(self, set=False):
        """.. method:: shutdown(self, set=False)

               
        """
        if set == True:
            self._shutdownEventLock.acquire()
            self._shutdownEvent.set()
            self._shutdownEventLock.release()
            return(True)
        else:
            self._shutdownEventLock.acquire()
            set = self._shutdownEvent.isSet()
            self._shutdownEventLock.release()
            return(set)

    def taskQueueWorker(self, sock, addr):
        """.. method:: taskQueueWorker(self, sock, addr)


        """
        data = sock.recv(1024)
        if not data:
            sock.close()
            return(1)
        elif data[0] == 'e':
            print 'Enqueue', '{0}\t{1}'.format(addr[0],data[2:])
            self.queue.put('{0}\t{1}'.format(addr[0],data[2:]))
            sock.sendall(data)
        elif data[0] == 'd':
            print 'Dequeue', addr
            while 1:
                try:
                    replyData = self.queue.get(block=True, timeout=1.0)
                except Queue.Empty:
                    if self.shutdown():
                        print 'taskQueueWorkerShutdown'
                        sock.shutdown(socket.SHUT_RDWR)
                        sock.close()
                        return(0)
                    else:
                        continue # restart while loop and wait for task
                else: # send task to executor
                    sock.sendall(replyData)
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    return(0)
        else: # data[0] is not a valid command
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(2)
   
    def taskQueueListener(self, port):
        """.. method:: taskQueueListener(self, port)


        """
        host = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1.0)
        sock.bind((host, port))
        sock.listen(5)
        print 'Listening on Port: {0}'.format(port)
        while 1:
            try:
                new_sock, addr = sock.accept()
            except socket.timeout:
                if self.shutdown():
                    print 'taskQueueListenerShutdown'
                    sock.close()
                    return(0)
                else: # restart while loop and connect to task queue
                    continue
            except socket.error as err:
                print 'taskQueueListenerException: {0}'.format(err)
                sock.close()
                return(1)
            else: # push task on queue: delegated to a new thread
                qt = Thread(target=self.taskQueueWorker, args=(new_sock, addr))
                qt.start()

def commandListener(port):
    """.. method:: commandListener(port)


    """
    host = ''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1.0)
    sock.bind((host, port))
    sock.listen(5)
    print 'Listening for commands on port: {0}'.format(port)
    while 1:
        try:
            new_sock, addr = sock.accept()
        except socket.timeout:
            if shutdown():
                break # leave while loop and shutdown
            else: # restart while loop to accept connections
                continue
        else: # without exception: delegate command to worker thread
            ct = Thread(target=commandWorker, args=(new_sock, addr))
            ct.start()
    sock.close()
    return(0)

def commandWorker(sock, addr):
    """.. method:: commandWorker(sock, addr)


    """
    try:
        data = sock.recv(128)
    except socket.error as err:
        print 's_cmdListenerException w/ {0}: {1}'.format(addr, err)
        sock.close()
        return(1) # return unsuccessfully
    except socket.timeout:
        print 's_cmdListenerTimeout w/ {0}'.format(addr)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return(2) # return unsuccessfully
    else: # without exception: process command
        if 'shutdown' == data:
            shutdown(True)
            sock.sendall('0')
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(0) # return successfully
        else:
            print 'Invalid command from {0}: "{1}"'.format(addr, data)
            sock.sendall('1')
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(3) # return unsuccessfully

def interruptHandler(signum, frame):
    """.. method:: interruptHandler(signum, frame)


    """
    print 'signal handler called!'
    shutdown(True)

def shutdown(set=False):
    """.. method:: shutdown(set=False)


    """
    if set == True:
        shutdownEventLock.acquire()
        shutdownEvent.set()
        shutdownEventLock.release()
        return(True)
    else:
        shutdownEventLock.acquire()
        set = shutdownEvent.isSet()
        shutdownEventLock.release()
        return(set)
        
def main():
    """.. method:: main()


    """
    if sys.argv[1] == '-d':
        pass # do not daemonize
    else:
        returnCode = daemonize()
    PROMOL_DIR = '/Users/Shared/MacPyMOLX11Hybrid.app/pymol/modules/pmg_tk/startup/ProMol'
    pymol = '/Users/Shared/MacPyMOLX11Hybrid.app/Contents/MacOS/MacPyMOL'
    promol = os.path.join(PROMOL_DIR, 'DistProMol', 'TaskExecutor.py')
    args = [pymol, '-cr', promol]
    signal.signal(signal.SIGINT, interruptHandler)
    server = Process(target=ProServer)
    server.start()
    try:
        taskExec = Popen(args, stdin=PIPE)
    except OSError as err:
        print 'InitPyMOLError: {0}'.format(err)
        sys.exit(1)
    else:
        taskExec.stdin.write('50007')
        taskExec.stdin.close()
        print 'port communicated'
        commandListener(50008) # commandListener() returns on 'shutdown' command
        taskExec.send_signal(signal.SIGINT)
        os.kill(server.pid, signal.SIGINT)
        taskExec.wait()
    server.join()
    print 'mischief managed'

if __name__ == '__main__':
    freeze_support()
    main()
