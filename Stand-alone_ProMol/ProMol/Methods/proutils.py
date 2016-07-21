# Utility functions from motif.py that could be more generally useful
# These used to be nested within other functions (or even other nested
# functions)

#from pymol import cmd
from ProMol import promolglobals as glb
import math
from rmsdmaster import calculate_rmsd as calcrmsd
from ProMol import promolobjects as proobjects
import numpy

# Returns the edit distance between its arguments
def levenshteinDistance(x,y):
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
    matrix = [[]]
    for acid in tup:
        newMatrix = []
        for subList in matrix:
            identical = subList[:] # Slice copy as shown on http://docs.python.org/tutorial/controlflow.html section 4.2
            identical.append(acid)
            newMatrix.append(identical)
            if 's' in glb.AminoHashTable[acid]:
                substituted = subList[:]
                substituted.append(glb.AminoHashTable[acid]['s'])
                newMatrix.append(substituted)
        matrix = newMatrix
    return matrix

def align(motif,query):
    '''Modifies the query residue coordinates to overlay with the motif
residue coordinates.'''
    # This code is modeled off the code in rmsd-master written by
    # Kromann and Bratholm, see that package (included) for details
    ignore_hydrogens = True
    atomsM, M = calcrmsd.get_coordinates_protein(motif,ignore_hydrogens)
    atomsQ, Q = calcrmsd.get_coordinates_protein(query,ignore_hydrogens)

    Mc = calcrmsd.centroid(M)
    Qc = calcrmsd.centroid(Q)
    M -= Mc
    Q -= Qc

    Q = calcrmsd.rotate(Q, M) #rotate the query residues onto the motif, so they line up when opened later
    Q += Mc

    #adjust the query residues so that the new coordinates are the correctly rotated on ones
    i = 0
    for residue in query.residues:
        for atom in residue.atoms:
            if ignore_hydrogens and atom.name=='H':
                continue
            atom.coordinates.x, atom.coordinates.y, atom.coordinates.z =        \
                                [Q.item(i),Q.item(i+1),Q.item(i+2)]
            i+=3

def getRMSD(motif, query):
    '''Returns the RMSD between the motif residues and query residues.'''
    # This code is modeled off the code in rmsd-master written by
    # Kromann and Bratholm, see that package (included) for details
    ignore_hydrogens = False
    atomsM, M = calcrmsd.get_coordinates_protein(motif,ignore_hydrogens)
    atomsQ, Q = calcrmsd.get_coordinates_protein(query,ignore_hydrogens)
    
    return calcrmsd.kabsch_rmsd(Q, M)
##        #querySubsetName = 'match_in_{0}'.format(queryPDBCode)
##        querySubsetName = 'match_in_%s'%(queryPDBCode)
##        cmd.select(querySubsetName, motifName)
##        cmd.hide('everything', 'all')
##        if queryPDBCode==motifPDBCode:
##            motifPDBCode = queryPDBCode + "1"
##            cmd.copy(motifPDBCode,queryPDBCode)
##        else:
##            cmd.fetch(motifPDBCode, async=0, path=glb.FETCH_PATH)
##        #motifSubsetName = 'match_in_{0}'.format(motifPDBCode)
##        motifSubsetName = 'match_in_%s'%(motifPDBCode)
##        cmd.select(motifSubsetName, '%s and (%s)' % (motifPDBCode,
##            glb.MOTIFS[motifName]['loci']))
##        cmd.hide('everything', 'all')
##     	
##        #aligns and gets the rmsd of the alignment by all atoms
##        dataAll = cmd.align(motifSubsetName, querySubsetName)  
##        #aligns and gets the rmsd of the alignment by C alpha atoms
##        cmd.select(querySubsetName, motifName+" and name ca")
##        cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
##        glb.MOTIFS[motifName]['loci'], "ca"))
##        dataAlpha = cmd.align(motifSubsetName, querySubsetName)
##        #aligns and gets the rmsd of the alignment by C alpha and C beta atoms
##        cmd.select(querySubsetName, motifName+" and name ca,cb")
##        cmd.select(motifSubsetName, '%s and (%s) and name %s' % (motifPDBCode,
##        glb.MOTIFS[motifName]['loci'], "ca,cb"))
##        dataAlphaBeta = cmd.align(motifSubsetName, querySubsetName)
##        rmsds = []
##        rmsds.append(dataAll[0])
##        rmsds.append(dataAlpha[0])
##        rmsds.append(dataAlphaBeta[0])
##        cmd.delete(motifName)
##        return rmsds


