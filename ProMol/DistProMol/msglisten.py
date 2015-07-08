import socket, errno
import signal
from threading import Thread, Event, Lock
from time import sleep

shutdownEvent = Event()
shutdownEventLock = Lock()

def worker(sock, addr):
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
        print 'Data: {0}'.format(data) # do something with data received
        return(0)
    except socket.error as err:
        sock.close()
        print 'worker: {0}'.format(err)
        return(1)       
            
def listener(port):
    host = ''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1.0)
    sock.bind((host, port))
    sock.listen(5)
    print 'Listening on Port: {0}'.format(port)
    while 1: # accept loop
        try:
            new_sock, addr = sock.accept()
        except socket.timeout:
            if not shutdown():
                continue # accept loop
            else:
                sock.close()
                return(0)
        except socket.error as err:
            print 'listener: {0}'.format(err)
            sock.close()
            return(1)
        else: # delegate work to new thread
            qt = Thread(target=worker, args=(new_sock, addr))
            qt.start()
            #sleep(10.0)
            continue # accept loop

def interruptHandler(signum, frame):
    shutdown(True)

def shutdown(set=False):
    if set is True:
        shutdownEventLock.acquire()
        shutdownEvent.set()
        shutdownEventLock.release()
        return(True)
    else:
        shutdownEventLock.acquire()
        set = shutdownEvent.isSet()
        shutdownEventLock.release()
        return(set)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, interruptHandler)
    listener(50007)
