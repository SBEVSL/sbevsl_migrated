''':mod:`TaskExecutor` --- Script for executing tasks within PyMOL
==================================================

.. module:: TaskExecutor
    :platform: OS X, Windows?
    :synopsis: Script for executing tasks within PyMOL.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

ToDo: confirm platform independence of shutdown signalling behavior.
ToDo: determine why pre-compiled OpenPyMOL on Windows 8.1 will
    not run in no GUI batch mode: command line argument, '-c'.

'''

import sys, os, signal
import socket, errno
from threading import Thread, Event, Lock
from pymol import cmd, stored
from time import sleep

# cmd.window('hide') # this did not work

# logging modes for debugging:
#     None : log nothing
#     'stdout' : print to STDOUT 
#     'fileName' : write to file 'fileName'
LOG_MODE = 1

class Logger(Thread):
    def __init__(self, mode=None):
        Thread.__init__(self)
        if not mode:
            return(0)
        elif LOG_MODE == 1:
            print logStr
            return(0)
        elif LOG_MODE == 2:
            with open('te_error.log', 'a') as flog:
                self.flog.write(logStr+'\r\n')
            return(0)
        else: # VERBOSE_LOG is out of range
            return(1)

def log(logStr):
    if not LOG_MODE:
        return(0)
    elif LOG_MODE == 1:
        print logStr
        return(0)
    elif LOG_MODE == 2:
        with open('te_error.log', 'a') as flog:
            flog.write(logStr+'\r\n')
        return(0)
    else: # VERBOSE_LOG is out of range
        return(1)

log('TaskExecutor.py has been started in PyMOL.exe.')
try: # windows machines
    SIGINT = signal.CTRL_C_EVENT
except AttributeError: # unix-like machines
    SIGINT = signal.SIGINT

log('SIGINT: {0}'.format(SIGINT))

MAX_ATTEMPTS = 10 # maximum number of attempts to send a message

#################################################################
# The following global variables and functions have been copied/modified from
# promolglobals.py and motif.py. TaskExecutor.py runs within a PyMOL instance
# and cannot import these components without triggering their package __init__.py
# files. Unfortunately, these functions now exist in two places. A more satisfying solution
# would rip the functions directly from the source code, a la dynamic programming
# languages. This was the 'incremental' (read: 'lazy') approach.
#
# ToDo: increment approach.
# 

FETCH_PATH = ''
MOTIF_DIRS = []
MOTIFS = {}
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
    
    if i in AminoSubsList:
        AminoHashTable[AminoLongList[i]]['s'] = AminoSubsList[i]
        AminoHashTable[AminoList[i]]['s'] = AminoSubsList[i]
        AminoHashTable[AminoShortList[i]]['s'] = AminoSubsList[i]
del i

def loadMotifData():
    """.. method:: loadMotifData()

       Copied/modified from promolglobals.py.
              
    """
    global MOTIFS
    global MOTIF_DIRS
    # path
    for MOTIF_DIR in MOTIF_DIRS:
        motif, motifFile = '', ''
        for file in os.listdir(MOTIF_DIR):
            if file.endswith('.py'):
                motifFile = os.path.join(MOTIF_DIR,file)
                motif = file.rsplit('.',1)[0]
                MOTIFS[motif] = {}
                MOTIFS[motif]['path'] = motifFile
                # resi
                with open(motifFile, 'r') as fin:
                    for line in fin.readlines(): # readlines loop
                        if line[0:4] == 'RESI':
                            resi = line.split(':')[1][0:-1].lower()
                            MOTIFS[motif]['resi'] = resi.split(',')
                            continue
                        elif line[0:4] == 'LOCI':
                            loci = line.split(':')[1][0:-1].split(';')
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
                            MOTIFS[motif]['loci'] = selection
                            break # readlines loop
    
def MotifCaller(motif, d):
    """.. method:: MotifCaller(motif, d)

       Copied/modified from motif.py.

       ToDo:
       .# replace cmd.count_atoms() dependency
       .# replace cmd.select() dependency
    """
    global MOTIFS
    try:
        returncode = execfile(MOTIFS[motif]['path'])
        #log('execFile={0}'.format(returncode))
        if returncode != False:
            if (motif not in cmd.get_names('all')) or (cmd.count_atoms(motif) == 0):
                log('motifCaller({0}): motif not in namespace or count is 0.'.format(motif))
                raise Warning
            else:
                #print("Print the number of residues: ")
                num_residues = cmd.count_atoms("name ca and " + motif)
                #print(num_residues)
                if num_residues < 2:
                    log('motifCaller({0}): fewer than 2 residues'.format(motif))
                    raise Warning
                else: log('motifCaller({0}): {1} residues'.format(motif, num_residues))
        else:
            log('motifCaller({0}): fewer than 2 residues'.format(motif))
            raise Warning
    except Warning:
        return False
    else:
        return True

def count(motif, pdb):
    """.. method:: count(motif,pdb)

        Copied/modified from motif.py

        ToDo: replace cmd.iterate() dependency
    """
    global MOTIFS
    last = None
    ordered = []
    orderedchain = {}
    bannedchain = []
    stored.motif = []
    editdist = []
    cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
    residues = MOTIFS[motif]['resi'] # glb.MOTIFS[motif]['resi']
    residuesl = len(residues)*2
    resList = [] # glb.GUI.motifs['csvprep'][pdb][motif]['res'] = []
    for iteration in stored.motif:
        if last != iteration:
            last = iteration
            resList.append(iteration) # glb.GUI.motifs['csvprep'][pdb][motif]['res'].append(iteration)
            ordered.append(iteration[1].lower())
            if iteration[0] not in orderedchain:
                if iteration[0] not in bannedchain:
                    orderedchain[iteration[0]] = []
                else:
                    continue
            orderedchain[iteration[0]].append(iteration[1].lower())
            if residuesl <= len(orderedchain[iteration[0]]):
                bannedchain.append(iteration[0])
                del orderedchain[iteration[0]]
    if len(orderedchain) == 0 and residuesl <= len(ordered):
        return None
    substitutions = [None]
    if motif[0] == 'J':
        for c in ('asp','glu','asn','gln','thr','ser'):
            if c in residues:
                substitutions = createsubs(residues)
                break
    for chain in orderedchain:
        editdist.append(levDist(residues,orderedchain[chain]))
        for sub in substitutions:
            if sub == None:
                break
            editdist.append(levDist(sub,orderedchain[chain]))
    editdist.append(levDist(residues,ordered))
    for sub in substitutions:
        if sub == None:
            break
        editdist.append(levDist(sub,ordered))
    mini = min(editdist)
    maxi = max(editdist)
    if (residuesl < 6 and mini > 0) or (residuesl < 12 and mini > 1) or \
           (residuesl < 18 and mini > 2) or mini > 3:
        return None
    #glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
    levDistRange = '%s-%s'%(mini,maxi) if mini<maxi else mini
    # Removed storage of precision factor as it is the same for the entire search
    #print 'ldr:{0}, rl:{1}'.format(mini, resList)
    return (levDistRange, resList)

# Returns the edit distance between its arguments
def levDist(x,y):
    """.. method:: levDist(x,y)

       Copied from proutils.py. Formerly, levenshteinDistance().
    """
    w,h = len(x)+1,len(y)+1
    #x+1 rows and y+1 columns
    matrix = [ [None]*h for i in range(w) ]
    for i in range(w):
        matrix[i][0] = i
    for j in range(h):
        matrix[0][j] = j
    for j in range(1,h):
        for i in range(1,w):
            if x[i-1] == y[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                #deletion,insertion,substitution
                matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,
                    matrix[i-1][j-1]+1)
    return matrix[w-1][h-1] #edit distance

# Returns a list of amino acid lists which could be considered
# equivalent to the sequence argument (all possible permutations)
def createsubs(tup):
    """.. method:: createsubs(tup)

        Copied from proutils.py      
    """
    global AminoHashTable
    matrix = [[]]
    for acid in tup:
        newMatrix = []
        for subList in matrix:
            identical = subList[:] # Slice copy as shown on http://docs.python.org/tutorial/controlflow.html section 4.2
            identical.append(acid)
            newMatrix.append(identical)
            if 's' in AminoHashTable[acid]:
                substituted = subList[:]
                substituted.append(AminoHashTable[acid]['s'])
                newMatrix.append(substituted)
        matrix = newMatrix
    return matrix

def getRMSD(motifName, queryPDBCode, motifPDBCode):
    """.. method:: createsubs(tup)

        Copied / modified from proutils.py
    """
    global MOTIFS
    try:
        querySubsetName = 'match_in_%s'%(queryPDBCode)
        cmd.select(querySubsetName, motifName)
        cmd.hide('everything', 'all')
        cmd.fetch(motifPDBCode, async=0, path=FETCH_PATH)
        motifSubsetName = 'match_in_%s'%(motifPDBCode)
        cmd.select(motifSubsetName, '%s and (%s)' % (motifPDBCode,
                                                     MOTIFS[motifName]['loci']))
        cmd.hide('everything', 'all')
        #aligns and gets the rmsd of the alignment by all atoms
        dataAll = cmd.align(motifSubsetName, querySubsetName)
        #aligns and gets the rmsd of the alignment by C alpha atoms
        cmd.select(querySubsetName, motifName+" and name ca")
        cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
                                                                 MOTIFS[motifName]['loci'], "ca"))
        dataAlpha = cmd.align(motifSubsetName, querySubsetName)
        #aligns and gets the rmsd of the alignment by C alpha and C beta atoms
        cmd.select(querySubsetName, motifName+" and name ca,cb")
        cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
                                                                 MOTIFS[motifName]['loci'], "ca,cb"))
        dataAlphaBeta = cmd.align(motifSubsetName, querySubsetName)
        rmsds = []
        rmsds.append(`dataAll[0]`)
        rmsds.append(`dataAlpha[0]`)
        rmsds.append(`dataAlphaBeta[0]`)
    except BaseException as err:
        log('getRMSD: {0}'.format(err))
    cmd.delete(motifPDBCode) 
    return rmsds

################################################################
# End of global variables and functions copied/modified from
# promolglobals.py and motif.py.
#

class TaskExecutor:
    """.. class:: TaskExecutor

        The TaskExecutor class instantiates the server-side processes for the PyMOL
        interface.
    """
    def __init__(self, queuePort):
        """.. method:: __init__(self, queuePort)

              
        """
        self.queuePort = queuePort
        self._shutdownEvent = Event()
        self.currPDB = None
        if SIGINT: signal.signal(SIGINT, self.interruptHandler)
        while 1: # execute loop
            returncode = self.executeTask()
            if returncode or self.shutdown():
                #print 'shutdown TaskExecutor'
                cmd.quit()
            else:
                continue # execute loop

    def interruptHandler(self, signum, frame):
        """.. method:: interruptHandler(self, signum, frame)

    
        """
        log('shutdown signal handler called!')
        self.shutdown(True)

    def shutdown(self, set=False):
        """.. method:: shutdown(self, set=False)

              
        """
        if set == True:
            self._shutdownEvent.set()
            return(True)
        else:
            return(self._shutdownEvent.isSet())

    def returnTask(self, returnAddr, resultStr):
        """.. method:: returnTask(self, returnAddr, resultStr)

           Returns the task result to ProServer where results from multiple TaskExecutors
           are reduced and returned to the client.
           
           msgmodel == True
        """
        host = '127.0.0.1'
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS): # attempt loop
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    sock.connect((host, self.queuePort))
                except socket.error as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        #print 'Connection with QueueListener (r) Refused [port#{0}]'.format(self.queuePort)
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err
                else:
                    sock.sendall('r{0}/{1}'.format(returnAddr, resultStr))
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    data = ''
                    while 1: # recv loop
                        try:
                            returncode = sock.recv(1)
                        except socket.error as err:
                            if err.errno is errno.EAGAIN:
                                sleep(0.0) # calling the sleep method should pass enough time
                                continue # recv loop
                            else: # something happened on queue worker end
                                raise err # for outer except to catch
                        else:
                            break # recv loop successfully
                    sock.close()
                    return(0) # return successfully
            except socket.error as err:
                sock.close()
                log('returnTask: {0}'.format(err))
                return(1)
        return(1) # after failing MAX_ATTEMPTS

    def returnTaskToClient(self, returnAddr, resultStr):
        """.. method:: returnTaskToClient(self, returnAddr, resultStr)

           Returns the task result directly to the client. This method will bypass reduction
           of results by the ProServer module.
           
           msgmodel == True
        """
        host, port = returnAddr.rsplit(':',1)
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS): # attempt loop
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    sock.connect((host, int(port)))
                except socket.error as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err
                else:
                    sock.sendall(resultStr)
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    data = ''
                    while 1: # recv loop
                        try:
                            returncode = sock.recv(1)
                        except socket.error as err:
                            if err.errno is errno.EAGAIN:
                                sleep(0.0) # calling the sleep method should pass enough time
                                continue # recv loop
                            else: # something happened on queue worker end
                                raise err # for outer except to catch
                        else:
                            break # recv loop successfully
                    sock.close()
                    return(0) # return successfully
            except socket.error as err:
                sock.close()
                log('returnTask: {0}'.format(err))
                return(1)
        return(1) # after failing MAX_ATTEMPTS

    def dequeueTask(self):
        """.. method:: dequeueTask(self)

           msgmodel == True
        """
        host = '127.0.0.1'
        global MAX_ATTEMPTS
        for attempt in range(MAX_ATTEMPTS): # attempt loop
            try: # outer try/except to ensure socket close
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                try:
                    sock.connect((host, self.queuePort))
                except socket.error as err:
                    if err.errno is errno.ECONNREFUSED: # not listening on remote port
                        sock.close()
                        log('Connection with QueueListener Refused [port#{0}]'.format(self.queuePort))
                        continue # next attempt
                    else: # well... this was unexpected
                        raise err
                else:
                    sock.sendall('d') 
                    sock.shutdown(socket.SHUT_WR) # send EOF to remote socket
                    data = ''
                    while 1: # recv loop
                        try:
                            chunk = sock.recv(1024) # block until queue has tasks
                        except socket.error as err:
                            if err.errno is errno.EAGAIN: # socket is busy
                                log('dequeueTask-recv: {0}'.format(err))
                                sleep(0.0) # sleep(0.0) should surfice, if not removed by compiler 
                                continue # recv loop
                            else: # something happened on queue worker end
                                raise err # for outer except to catch
                        else:
                            if not chunk: # queue socket SHUT_WR sends EOF
                                break # recv loop successfully
                            else:
                                data += chunk
                                continue # recv loop
                    sock.close()
                    return(data) # return successfully
            except socket.error as err:
                sock.close()
                log('dequeueTask: {0}'.format(err))
                if not self.shutdown():
                    continue # next attempt
                else:
                    #print 'dequeueTask: shutdown'
                    return(1)
        return(1) # after failing MAX_ATTEMPTS

    def executeTask(self):
        """.. method:: executeTask(self)

           msgmodel == True
           ToDo: replace cmd.fetch() dependency   
        """
        taskStr = self.dequeueTask()
        if taskStr in ['',1]:
            self.shutdown(True)
            return(1) # execute loop
        else:
            returnAddr, taskBody = taskStr.split('/',1)
            for task in taskBody.split('&'):
                log('task: {0}'.format(task))
                pdb, motif, delta, rmsdchoice = task.split('\t')
                rmsds = '-1,-1,-1'
                if self.currPDB != pdb:
                    cmd.reinitialize()
                    cmd.fetch(pdb, async=0, path=FETCH_PATH)
                    self.currPDB = pdb
                cmd.hide('everything', 'all')
                cmd.remove("all and hydro")
                resultStr = '{0}\t{1}\t{2}/    {3}:{1}:{4}'.format(pdb, motif, delta, 'None', rmsds)
                try:
                    if MotifCaller(motif, float(delta)):
                        try:
                            levDistRange, resList = count(motif,pdb)
                        except BaseException as err:
                            log('count: {0}'.format(err))
                        else:
                            print 'levDistRange={0}'.format(levDistRange)
                            if int(rmsdchoice):
                                try:
                                    rmsds = ','.join(getRMSD(motif, pdb, motif.split('_',2)[1]))
                                except BaseException as err: # restrict after testing code
                                    log('getRMSD: {0}'.format(err))
                            resultStr = '{0}\t{1}\t{2}/    {3}:{1}:{4}{5}'.format(pdb, motif, delta,
                                                                                  levDistRange, rmsds,
                                                                                  reduce(lambda x,y: x+'\t'+','.join(y), resList, ''))
                except BaseException as err: # restrict after testing code
                    log('executeTask: {0}'.format(err))
                self.returnTaskToClient(returnAddr, resultStr)
                cmd.delete(motif)
            return(0)

def main():
    """.. method:: main()

              
    """
    global FETCH_PATH, MOTIF_DIRS
    queuePort = 0
    for attempt in range(5):
        try:
            parsedInput = raw_input().split(',', 3)
            queuePort = int(parsedInput[0])
            MOTIF_DIRS = parsedInput[1:3]
            FETCH_PATH = parsedInput[3]
            log('resultPort: {0}'.format(queuePort))
        except EOFError:
            log('stdin not ready yet')
            continue
        else:
            break
    loadMotifsThread = Thread(target=loadMotifData)
    loadMotifsThread.start()
    loadMotifsThread.join()
    TaskExecutor(queuePort)
    sys.exit(0) # this should be superfluous

if __name__ == '__main__':
    main()
