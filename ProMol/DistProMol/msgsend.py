import socket, errno, signal
from time import sleep

def interruptHandler(signum, frame):
    pass

signal.signal(signal.SIGINT, interruptHandler)

MAX_ATTEMPTS = 10
job = ['Hello, this is a job -- task number {0}. I hope the whole message is received.'.format(i) for i in range(1,500)]
host = 'cos-a33004.main.ad.rit.edu'
for task in job: # task loop
    for attempt in range(MAX_ATTEMPTS): # attempt loop
        try: # outer try/except to ensure socket close
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.settimeout(10.0) # [seconds] 'escape hatch'
            try:
                sock.connect((host, 50007))
            except socket.error as err:
                if err.errno is errno.ECONNREFUSED: # not listening on remote port
                    sock.close()
                    print 'Connection with host: {0} Refused.'.format(host)
                    continue # next attempt
                else: # well... this was unexpected
                    raise err
            else:
                sock.sendall(task) 
                sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                returncode = None
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
                if returncode != '0':
                    continue # next attempt
                else:
                    print 'Task sent: {0}\nreturncode: {1}'.format(task, returncode)
                    break # attempt loop successfully
        except socket.error as err:
            sock.close()
            print 'send: {0}'.format(err)
            continue # next attempt

