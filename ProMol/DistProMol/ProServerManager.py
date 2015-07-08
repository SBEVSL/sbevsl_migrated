''':mod:`ProServerManager` --- Lightweight server manager module for distributing ProMol calculations
==================================================

.. module:: ProServerManager
    :platform: OS X
    :synopsis: Lightweight server manager module for distributing ProMol calculations.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''
import socket
from multiprocessing import Process, freeze_support
from threading import Thread, Lock, Event, enumerate, activeCount
from Daemon import daemonize

class ProServerManager:
    """.. class:: ProServerManager

        The ProServerManager class instantiates the manager which maintains remote
        servers and the allocation of work to the remote servers.
    """
    def __init__(self, serverHostList, password, daemon=True):
        if daemon == True: # daemonize server manager process
            returnCode = daemonize()
        self._serverMap = {}
        self._serverString = ''
        self._serverStringLock = Lock()
        self._shutdownEvent = Event()
        self.initServers(serverHostList, password)
        print 'serverString: {0}'.format(self._serverString)
        mrl = Thread(target=self.mapRequestListener, args=(50010,))
        mrl.start()
        self.commandListener(50011) # returns on 'shutdown' command
        self.shutdownServers()
        mrl.join()

    def initServers(self, serverHostList, password):
        """.. method:: initServers(self, serverHostList, password)


        """
        for host in serverHostList:
            try:
                hostIP = socket.gethostbyname(host)
            except socket.gaierror as err:
                print 'serverMapInitException w/ {0}: {1}'.format(host, err)
                continue # skip host and continue with serverHostList
            # init remote servers
            self._serverMap[host] = [hostIP, 50007]
            self._serverString += hostIP+':'+'50007'+'\t'

    def shutdownServers(self):
        """.. method:: shutdownServers(self)


        """
        cmd = 'shutdown'
        for server in self._serverMap.values():
            host, port = server[0], server[1]+1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.settimeout(1.0)
            try:
                sock.connect((host, port))
            except socket.error as err:
                print 'cmdConnectException w/ {0}: {1}'.format(host, err)
                sock.close()
                continue # restart while loop to accept another command
            except socket.timeout:
                print 'cmdConnectTimeout w/ {0}'.format(host)
                sock.close()
                continue # restart while loop to accept another command
            else: # without exception: send command to server manager
                sock.sendall(cmd)
                try:
                    returnCode = sock.recv(1)
                except socket.timeout:
                    print 'cmdReceiveTimeout w/ {0}'.format(host)
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                    continue # restart while loop to accept another command
                else: # cmd received by server where connection was shutdown
                    sock.close()
                    print 'Command sent to {0}: "{1}" w/ return code: {2}'.format(host, cmd, returnCode)
                    continue
        return(0)

    def commandListener(self, port):
        """.. method:: commandListener(self, port)


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
                if self._shutdownEvent.isSet():
                    break # leave while loop and shutdown
                else: # restart while loop to accept connections
                    continue
            else: # without exception: delegate command to worker thread
                ct = Thread(target=self.commandWorker, args=(new_sock, addr))
                ct.start()
        sock.close()
        return(0)

    def commandWorker(self, sock, addr):
        """.. method:: commandWorker(self, sock, addr)


        """
        try:
            data = sock.recv(128)
        except socket.error as err:
            print 'sm_cmdListenerException w/ {0}: {1}'.format(addr, err)
            sock.close()
            return(1) # return unsuccessfully
        except socket.timeout:
            print 'sm_cmdListenerTimeout w/ {0}'.format(addr)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(2) # return unsuccessfully
        else: # without exception: process command
            if 'shutdown' == data:
                self._shutdownEvent.set()
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
            
    def mapRequestListener(self, port):
        """.. method:: mapRequestListener(self, port)


        """
        host = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1.0)
        sock.bind((host, port))
        sock.listen(5)
        print 'Serving map requests on port: {0}'.format(port)
        while 1:
            try:
                new_sock, addr = sock.accept()
            except socket.timeout:
                if self._shutdownEvent.isSet():
                    break # leave while loop and shutdown
                else: # restart while loop to accept connections
                    continue
            else: # without exception: delegate accepted connection to a new thread
                rt = Thread(target=self.mapRequestWorker, args=(new_sock, addr))
                rt.start()
        sock.close()
        return(0)

    def mapRequestWorker(self, sock, addr):
        """.. method:: mapRequestWorker(self, sock, addr)


        """
        try:
            data = sock.recv(1024)
        except socket.error as err:
            print 'mapRequestException w/ {0}: {1}'.format(addr, err)
            sock.close()
            return(1) # return unsuccessfully
        except socket.timeout:
            print 'mapRequestTimeout w/ {0}'.format(addr)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(2) # return unsuccessfully
        else: # without exception: process server map request
            servers = self.serverString()
            print 'Sending servers to {0}'.format(addr)
            sock.sendall(servers)
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            return(0) # return successfully

    def serverString(self):
        """.. method:: serverString(self)


        """
        self._serverStringLock.acquire()
        servers = self._serverString
        self._serverStringLock.release()
        return servers
            
def main():
    """.. method:: main() 


    """
    import sys
    import getpass
    password = getpass.getpass()
    daemonServerManager = True
    if sys.argv[1] == '-d':
        del sys.argv[1] # do not daemonize
        daemonServerManager = False
    manager = ProServerManager(sys.argv[1:], password, daemonServerManager)
    print 'mischief managed'

if __name__ == '__main__':
    freeze_support()
    main()
