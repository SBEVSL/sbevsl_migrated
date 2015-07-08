''':mod:`TaskExecutor` --- Script for executing tasks within PyMOL
==================================================

.. module:: TaskExecutor
    :platform: OS X
    :synopsis: Script for executing tasks within PyMOL.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

import sys
import os
import socket
import signal
from threading import Thread, Event, Lock
from pymol import cmd, stored

PROMOL_DIR = '/Users/Shared/MacPyMOLX11Hybrid.app/pymol/modules/pmg_tk/startup/ProMol'
MOTIF = {}
#Amino Acid Lists
AminoLongList = ('alanine', 'arginine', 'asparagine', 'aspartate', 'cysteine',
    'glutamine', 'glutamate', 'glycine', 'histidine', 'isoleucine', 'leucine',
    'lysine', 'methionine', 'phenylalanine', 'proline', 'serine', 'threonine',
    'tryptophan', 'tyrosine', 'valine', 'magnesium', 'zinc', 'manganese', 'sodium', 'hemes',
    'cobalt', 'nickle', 'iron', 'copper')
AminoList = ('ala', 'arg', 'asn', 'asp', 'cys', 'gln', 'glu', 'gly', 'his',
    'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val', 
    'mg', 'zn', 'mn', 'na', 'hem', 'co', 'ni', 'fe', 'cu')
AminoShortList = ('a', 'r', 'n', 'd', 'c', 'q', 'e', 'g', 'h', 'i', 'l', 'k',
    'm', 'f', 'p', 's', 't', 'w', 'y', 'v', 'mg', 'zn', 'mn', 'na', 'hem', 'co', 'ni', 'fe', 'cu')
AminoSubsList = {
        3:'glu',
        6:'asp',
        5:'asn',
        2:'gln',
        15:'thr',
        16:'ser'
    }
AminoNumberList = (5, 11, 8, 8, 6, 9, 9, 4, 10, 8, 8, 9, 8, 11, 7, 6, 7, 14, 12,
    7, 19, 20, 21, 22, 23, 24, 25, 26, 27)

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

def getMotifData(motif):
    """.. method:: getMotifData(motif)

              
    """
    global MOTIF
    global PROMOL_DIR
    # path
    motifFile = ''
    motifDir = os.path.join(PROMOL_DIR, 'Motifs')
    for file in os.listdir(motifDir):
        if file.startswith(motif):
            motifFile = os.path.join(motifDir,file)
            break
    if motifFile == '':
        print 'File for motif: {0} not found.'.format(motif)
        return(1)
    MOTIF['path'] = motifFile
    print 'motifFile: {0}'.format(motifFile)
    # resi
    with open(motifFile, 'r') as file:
        for line in file.readlines():
            if line[0:4] == 'RESI':
                resi = line.split(':')[1][0:-1].lower()
                MOTIF['resi'] = resi.split(',')
                continue
    return(0)
    
def MotifCaller(motif, d):
    """.. method:: MotifCaller(motif, d)

              
    """
    global MOTIF
    try:
        if execfile(MOTIF['path']) != False:
            if (motif not in cmd.get_names('all')) or (cmd.count_atoms(motif) == 0):
                raise Warning
            else:
                #print("Print the number of residues: ")
                num_residues = cmd.count_atoms("name ca and " + motif)
                #print(num_residues)
                if num_residues < 2:
                  raise Warning
        else:
            raise Warning
    except Warning:
        return False
    else:
        return True

def count(motif,pdb):
    """.. method:: count(motif,pdb)

              
    """
    global MOTIF
    last = None
    ordered = []
    orderedchain = {}
    bannedchain = []
    stored.motif = []
    editdist = []
    cmd.iterate(motif, 'stored.motif.append((chain,resn,resi))')
    residues = MOTIF['resi']
    residuesl = len(residues)*2
    # be sure to return csv prep... w/pickling?
    resList = []
    for iteration in stored.motif:
        if last != iteration:
            last = iteration
            resList.append(iteration)
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
    #glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
    levDistRange = '%s-%s'%(mini,maxi) if mini<maxi else mini
    # Removed storage of precision factor as it is the same for the entire search
    return (levDistRange, resList)

# Returns the edit distance between its arguments
def levDist(x,y):
    """.. method:: levDist(x,y)

              
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
        self._shutdownEventLock = Lock()
        signal.signal(signal.SIGINT, self.interruptHandler)
        while 1:
            returncode = self.executeTask()
            if returncode | self.shutdown():
                break
        cmd.quit()

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

    def executeTask(self):
        """.. method:: executeTask(self)

              
        """
        host = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.connect(('',self.queuePort))
            sock.sendall('d')
            task = sock.recv(1024)
            sock.close()
        except socket.error as err:
            print 'exeTaskQueueConnectException: {0}'.format(err)
            sock.close()
            return(1)
        else: # request task from queue
            if self.shutdown():
                print 'exeTaskShutdown2'
                return(0)
            # perform task with promol/pymol
            parsedTask = task.split('\t')
            returnAddr = (parsedTask[0], int(parsedTask[1]))
            pdb = parsedTask[2]
            cmd.fetch(pdb, async=0)
            motif = parsedTask[3]
            delta = float(parsedTask[4])
            returncode = getMotifData(motif)
            cmd.hide('everything', 'all')
            cmd.remove("all and hydro")
            resultString = '    %s: %s'%('-1', motif)
            if self.shutdown():
                print 'exeTaskShutdown3'
                return(0)
            if MotifCaller(motif, delta):
                levDistRange, resList = count(motif,pdb)
                #print 'levDistRange: {0}\nresList: {1}'.format(levDistRange, resList)
                if levDistRange != None:
                    resultString = '    %s: %s'%(levDistRange, motif)
                    resultString = resultString+reduce(lambda x,y: x+'\t'+','.join(y), resList, '')
            if self.shutdown():
                print 'exeTaskShutdown4'
                return(0)
            returncode = self.returnResult(returnAddr, resultString)
            cmd.reinitialize()
            return(0)

    def returnResult(self, returnAddr, resultString):
        """.. method:: returnResult(self, returnAddr, resultString)

              
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.connect(returnAddr)
        except socket.error as err:
            print 'exeTaskClientConnectException: {0}'.format(err)
            sock.close()
            return(1)
        sock.sendall(resultString)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return(0)

def main():
    """.. method:: main()

              
    """
    queuePort = 0
    for attempt in range(5):
        try:
            queuePort = int(raw_input())
            print 'resultPort: {0}'.format(queuePort)
        except EOFError:
            print 'stdin not ready yet'
            continue
        else:
            break
    TaskExecutor(queuePort)
    sys.exit(0)

if __name__ == '__main__':
    main()
