# motif_interface for multiprocess ProMol unit testing

# additional motif imports
import socket, errno
from threading import Thread, Event, Lock
from ProServer import ProServer

# current motif imports
import os, time
# current motif import from promolglobals
glbGUImotifs = {'cancel' : False} # glb.GUI.motifs
glbmatchpairs = [] # glb.matchpairs

# unit test-specific imports/globals
import sys
NUM_OF_MOTIFS = -1
allkeys = [f.split('.')[0] for f in os.listdir(os.path.join(os.path.split(os.getcwd())[0],'Motifs')) if len(f) > 10]

# current motif globals
deltaRange = [float(d)/10.0 for d in range(10, 15, 5)]
rmsdchoice = 1
keys = allkeys[:NUM_OF_MOTIFS]
pdb = '1EB6'
numResultsOfEachQuery = []

# additional motif globals
MULTIPROCESS = True

# additional motif.py methods
def jobResultListener():
    """.. method:: jobResultListener()

       msgmodel == True
    """
    global resultPort, resultPortSetEvent
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1.0)
    sock.bind(('', resultPort)) # OS chooses open port
    resultPort = sock.getsockname()[1]
    print 'resultPort: {0}'.format(resultPort)
    resultPortSetEvent.set()
    sock.listen(5)
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
            print 'jobResultListener: {0}'.format(err)
            sock.close()
            return(1)
        else: # delegate work to new thread
            jrmt = Thread(target=jobResultWorker, args=(new_sock, addr))
            jrmt.start()
            continue # accept loop

def jobResultWorker(sock, addr):
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
                        time.sleep(0.0) # sleep(0.0) should be sufficient, unless removed by compiler
                        continue
                    else: # timeout | worse
                        raise err # to outer except block
                else:
                    if not chunk: # remote socket SHUT_WR sends EOF
                        break # recv loop successfully
                    else:
                        data += chunk
                        continue # recv loop
            sock.sendall('0')
            sock.shutdown(socket.SHUT_WR) 
            sock.close()
            processResultStr(data)
            return(0)
        except socket.error as err:
            sock.close()
            print 'jobResultWorker: {0}'.format(err)
            return(1)

def shutdown(set=False):
    """.. method:: shutdown(set=False)


    """
    global shutdownEvent
    if set is True:
        shutdownEvent.set()
        return(True)
    else:
        return(shutdownEvent.isSet())

def processResultStr(resultStr):
    """.. method:: processResultStr(resultStr)


    """
    global glbGUImotifs, resultMutex, resultCount, found
    resultName, result = resultStr.split('/', 1)
    parsedResult = result.split('\t')
    ldr, mot, rmsds = ([r.strip() for r in parsedResult[0].split(':', 2)])
    #print '{0}, {1}: rmsds= {2}'.format(ldr, mot, rmsds)
    #print 'ldr: {0}, mot: {1}'.format(ldr, mot)
    if ldr != 'None': # process results before entering critical region
        motifStr = '{0}: {1}'.format(ldr, mot)
        resDict = {'res':[(res.split(',')) for res in parsedResult[1:]]}
        rmsdList = [float(n) for n in rmsds.split(',', 2)]
        resultMutex.acquire()
        try: # critical region
            found.append(motifStr)
            #glb.GUI.motifs['csvprep'][pdb][mot] = resDict
            glbGUImotifs[mot] = resDict
            #glb.GUI.motifs['csvprep'][pdb][motifName]['rmsd'] = rmsdList
            glbGUImotifs[mot]['rmsds'] = rmsdList
            resultCount += 1
        finally: # always release the lock
            resultMutex.release()
    else:
        resultMutex.acquire()
        resultCount += 1
        resultMutex.release()
        
# additional motif.py code for motifchecker(). Here it is wrapped in main().
def main():
    if MULTIPROCESS:
        keysL = len(keys)*len(deltaRange)
        lasto, previousLast = 0, 0
        resultPortSetEvent.wait()
        for motif in keys:
            # EC code
            for d in deltaRange:
                server.addTask('127.0.0.1:{0}/{1}\t{2}\t{3}\t{4}'.format(resultPort,
                                                                         pdb, motif, d, rmsdchoice))
        while 1:
            time.sleep(2.0)
            #if glb.GUI.motifs['cancel']:
            if glbGUImotifs['cancel']:
                server.cancelTaskWorker()
                # GUI code
                break
            last = resultCount
            lasto += last - previousLast
            previousLast = last
            # update progress bar code
            print 'Results attained: {0}/{1}'.format(last, keysL)
            if last >= keysL:
                break
        print 'Done. Results attained: {0}/{1}'.format(last, keysL)
        numResultsOfEachQuery.append(len(found))
        #glb.matchpairs.extend([(pdb, pdb)] + [(pdb, result) for result in found])
        glbmatchpairs.extend([(pdb, pdb)] + [(pdb, result) for result in found])
        # unit test-specific code to print results 
        for motifStr in found:
            rmsds  = glbGUImotifs[motifStr.split(': ', 1)[1]]['rmsds']
            print 'Found ...{0:20}...rmsds= {1: 6.5},{2: 6.5},{3: 6.5}'.format(motifStr, *rmsds)
    else: 
        pass # existing motifchecker() code

# additional motif.py globals
if MULTIPROCESS:
    server = ProServer()
    server.start()
    resultPort = 0
    resultPortSetEvent = Event()
    resultMutex = Lock()
    resultCount = 0
    shutdownEvent = Event()
    resultListenerThread = Thread(target = jobResultListener)
    resultListenerThread.start()
    found = []

if __name__ == '__main__':
    time.sleep(2.0)
    print 'Go!'
    main()

# additional motif.py shutdown code
if MULTIPROCESS:
    shutdown(True)
    server.shutdown(True)
    resultListenerThread.join()
    server.join()

print 'mischief managed' # yes, this is an allusion ;)
sys.exit(0)
