# Utility functions from motif.py that could be more generally useful
# These used to be nested within other functions (or even other nested
# functions)

from pmg_tk.startup.ProMol import promolglobals as glb

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
