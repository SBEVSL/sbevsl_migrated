''':mod:`ProSocket` --- A module for abstracting the common socket use patterns of parallel and distributed ProMol.
========================================================================

.. module:: ProJob
    :platform: OS X, Windows, Linux
    :synopsis: A module for abstracting the common socket use patterns of parallel and distributed ProMol

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''
import socket, errno, ssl, hmac, hashlib, os
from uuid import getnode 
from threading import Thread
from time import sleep

USE_SSL = False
USE_HMAC = False
MAX_SEND_ATTEMPTS = 10
PREFIX_LENGTH = 3
MAX_MESSAGE_LENGTH = reduce(lambda s,i: s+255*255**i,range(PREFIX_LENGTH),0)
SSL_VERSION = ssl.PROTOCOL_SSLv23
if not ssl.RAND_status(): ssl.RAND_add(os.urandom(),0.1)

def sockRecvCall(sock, addr, callablesDict=None, timeout=10.0, use_hmac=USE_HMAC):
    """.. method:: sockRecvCall(sock, addr, callablesDict=None, timeout=10.0, use_hmac=USE_HMAC)

        This method takes a connected socket as an argument. Waits to receive data. Passes
        the data to callables for processing, and sends a returncode.

    """
    sock.settimeout(timeout)
    data, prefix, replyData = '', '', '0' 
    try:
        while len(prefix) < PREFIX_LENGTH:
            try: chunk = sock.recv(PREFIX_LENGTH-len(prefix))
            except socket.error as err:
                if err.errno == errno.EAGAIN: sleep(0.01)
                else: raise
            else:
                if not chunk: break
                prefix += chunk
        dataLength = prefixToDataLength(prefix)
        #p#print dataLength #p#
        while len(data) < dataLength:
            try: chunk = sock.recv(min([dataLength-len(data), 2048]))
            except socket.error as err:
                if err.errno == errno.EAGAIN: sleep(0.01)
                else: raise
            else:
                if not chunk: break
                data += chunk
        #p#print 'recv', dataLength, data[:10] #p#
        if callablesDict:
            #p#print data[0] #p#
            try: replyData = callablesDict[data[0]](data,sock,addr)
            except KeyError: replyData = '1'
            #p#print data[0],`dataLengthToPrefix(replyData)`, replyData[:10] #p#
            sock.sendall(dataLengthToPrefix(replyData)+replyData)
    finally:
        sock.close()
        return data

def sockListenerThread(shutdownTarget,
                       workerTarget=sockRecvCall,
                       workerCallables=None,
                       addr=('',0),
                       portSetTarget=None,
                       timeout=1.0,
                       use_ssl=USE_SSL,
                       use_hmac=USE_HMAC):
    """.. method:: sockListenerThread(shutdownTarget,
                       workerTarget=sockRecvCall,
                       workerCallables=None,
                       addr=('',0),
                       portSetTarget=None,
                       timeout=1.0,
                       use_ssl=USE_SSL,
                       use_hmac=USE_HMAC):

        This method initalizes a listener socket, which accepts connnections from other sockets,
        and launches a worker thread to interact with the new connection.

    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(timeout)
        sock.bind(addr) 
        if portSetTarget: portSetTarget(sock.getsockname()[1])
        sock.listen(5)
        while 1:
            try:
                new_sock, client_addr = (lambda s,a: (ssl.wrap_socket(s,
                                                                      server_side=True,
                                                                      certfile='cert.pem',
                                                                      ca_certs='cert.pem',
                                                                      cert_reqs=ssl.CERT_REQUIRED,
                                                                      ssl_version=SSL_VERSION),a)
                                         if use_ssl else (s,a))(*sock.accept())
            except socket.timeout:
                if shutdownTarget(): break
            except ssl.SSLError as err:
                print err
                break
            except socket.error as err:
                print 'sockListenerThread: {0}'.format(err)
                break
            else:
                #p#print 'connection w/ ',client_addr #p#
                Thread(target=workerTarget, args=(new_sock, client_addr, workerCallables), name='wt').start()
    finally: sock.close()

def sockSendRecv(data,
                 port,
                 host='127.0.0.1',
                 callablesDict=None,
                 timeout=None,
                 use_ssl=USE_SSL,
                 use_hmac=USE_HMAC):
    """.. method:: sockSendRecv(data,
                 port,
                 host='127.0.0.1',
                 callablesDict=None,
                 timeout=None,
                 use_ssl=USE_SSL,
                 use_hmac=USE_HMAC):

        This method connects of a specified listening socket, sends data, and waits to receive
        a reply.

    """
    try:
        sock = (lambda s: ssl.wrap_socket(s,
                                          certfile='cert.pem',
                                          ca_certs='cert.pem',
                                          cert_reqs=ssl.CERT_REQUIRED)
                if use_ssl else s)(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(timeout)
        for attempt in range(MAX_SEND_ATTEMPTS): # attempt loop
            try: sock.connect((host, port))
            except ssl.SSLError as err:
                print err
                return '1'
            except socket.error as err:
                if err.errno is errno.ECONNREFUSED: print 'sockSendRecv: Connection Refused.'
                else: raise
            else:
                #p#print 'send:',`dataLengthToPrefix(data)`, data[:min([len(data),10])] #p#
                sock.sendall(dataLengthToPrefix(data)+data)
                return sockRecvCall(sock, addr=(host,port), callablesDict=callablesDict, timeout=timeout)
        else: return '1'
    finally: sock.close()

def dataLengthToPrefix(data):
    """.. method:: dataLengthToPrefix(data)

        This method encodes length of the data as characters. The number of characters in the
        prefix is specified by the global variable, 'PREFIX_LENGTH'. Currently, the default is
        three characters. If the data length exceeds the MAX_MESSAGE_LENGTH, a warning
        message is printed to STDOUT.

    """
    dataLength = len(data)
    if dataLength > MAX_MESSAGE_LENGTH: print 'Warning: message is too large!'
    return reduce(lambda s,i: s+chr(dataLength//255**i%255),range(PREFIX_LENGTH),'')

def prefixToDataLength(prefix):
    """.. method:: prefixToDataLength(prefix)

        This method decodes the prefix into the length of the subsequent data.

    """
    return reduce(lambda s,(i,c): s+ord(c)*255**i,enumerate(prefix),0)

def createSSLCertificate():
    """.. method:: 

        T

    """
    pass
