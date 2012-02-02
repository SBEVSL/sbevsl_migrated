# Levenshtein Distance API with Equivalence Options
# Incorporates the standard Levenshtein distance calculation function
# by Mario Rosa from ProMOL as lDistBasic(x, y)
#
# Copyright 2012 Rochester Institute of Technology
# Created by Cyprian Corwin (cwc4619@rit.edu <mailto:cwc4619@rit.edu>)
# Licensed under the GPL License
# 
#  work supported in part by the SBEVSL project at
#  Dowling College and at Rochester Institute of Technology under
#  Grant Number R15GM078077 from the National Institute Of General
#  Medical Sciences. The content is solely the responsibility of the
#  authors and does not necessarily represent the official views of
#  the National Institute Of General Medical Sciences or the National
#  Institutes of Health.
# 
# /**********************************************************************
#  *                                                                    *
#  * YOU MAY REDISTRIBUTE THIS COMPONENT UNDER THE TERMS OF THE GPL     *
#  *                                                                    *
#  **********************************************************************/
# 
# /*************************** GPL NOTICES ******************************
#  *                                                                    *
#  * This program is free software; you can redistribute it and/or      *
#  * modify it under the terms of the GNU General Public License as     *
#  * published by the Free Software Foundation; either version 2 of     *
#  * (the License, or (at your option) any later version.               *
#  *                                                                    *
#  * This program is distributed in the hope that it will be useful,    *
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of     *
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the      *
#  * GNU General Public License for more details.                       *
#  *                                                                    *
#  * You should have received a copy of the GNU General Public License  *
#  * along with this program; if not, write to the Free Software        *
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA           *
#  * 02111-1307  USA                                                    *
#  *                                                                    *
#  **********************************************************************/
#

# Substitution dictionaries

# Any substitution dictionary used with this API must be of the
# following format:
# [(res1a, res1b), (res2a, res2b), (res3a, res3b), ..., (resNa, resNb)]
# where resNa and resNb are strings that can be considered equivalent
# for any whole number N.  Additionally, all of these strings MUST
# be in all lower case, or it won't work.  (I call it a substitution
# dictionary, but it is not actually a Python dictionary, but rather
# a list of ordered pairs (2-tuples).)

# This is the standard substitution dictionary.
standardSubPairs = [('asn', 'gln'), ('asp', 'glu'), ('ser', 'thr')]

# This can be passed in as the dictionary to cause isSubstitutible
# to always return False, substitution to always return None, and
# canonicalResidue and canonicalSequence to only convert to lower case
# and not perform any substitutions.
unSubPairs = [(None, None)]

# This lDistBasic function was copied from ProMOL and renamed
def lDistBasic(x,y):
    '''Returns the edit distance between its arguments'''
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
    
def isSubstitutible(residueTLA, subpairs = standardSubPairs):
    '''Given a residue 3-letter abbreviation, return True if it has
    a substitution available; accept either upper or lower case.'''
    # First make it match the format of subpairs
    smallTLA = residueTLA.lower()
    # Return true if any of the pairs in subpairs contain the residue
    return any([(smallTLA in eachpair) for eachpair in subpairs])
    
def substitution(residueTLA, subpairs = standardSubPairs):
    '''Given a residue 3-letter abbreviation, return its substitution
    if one exists, otherwise None; accept either upper or lower case.'''
    if isSubstitutible(residueTLA, subpairs):
        smallTLA = residueTLA.lower()
        # Should return a list of two tuples (I don't mean 2-tuples!),
        # one containing the first members of each pair, the other
        # containing the other members of the corresponding pairs
        # The asterisk is to convert subpairs from a single list
        # argument to multiple varargs like zip requires
        parallel = zip(*subpairs)
        assert len(parallel) == 2, 'Zipping the residue dictionary yielded something not of length 2.'
        # The amino acid requested could have been either first or
        # second in its pair; return whichever one it wasn't
        whichListIndex = 0 if smallTLA in parallel[0] else 1
        startList = parallel[whichListIndex]
        otherList = parallel[1 - whichListIndex]
        position = startList.index(smallTLA)
        retVal = otherList[position]
    else:
        retVal = None
    return retVal
    
def canonicalSub(residueTLA, subpairs = standardSubPairs):
    '''If a residue is substitutible in the specified dictionary,
    return the same thing for both (the amino acid and its substitution
    in sorted order, separated by a slash), otherwise just the residue;
    in all cases, convert to lower case.  This will be used for
    substitution equivalence (not order equivalence), and should always
    return the same result for either of any two substitutible strings.'''
    smallTLA = residueTLA.lower()
    if isSubstitutible(smallTLA, subpairs):
        retVal = '/'.join(sorted((smallTLA, substitution(smallTLA, subpairs))))
    else:
        retVal = smallTLA
    return retVal
    
def canonicalSubs(sequenceTLAs, subpairs = standardSubPairs):
    '''Converts an entire sequence of residues to their canonical form
    for substitution equivalence, leaving the order the same.'''
    # This is a Python list comprehension
    return [canonicalSub(eachTLA, subpairs) for eachTLA in sequenceTLAs]
    
def sequenceToLowercase(sequenceTLAs):
    '''Simply converts every element in the sequence to lower case
    (assuming they are strings; more generally, replaces each element
    with the return value from its lower() method), and returns the
    resulting sequence as a list.'''
    return [item.lower() for item in sequenceTLAs]

def countOccurrences(seq):
    '''Returns a sequence of the same length as seq,
    with each element from seq replaced by a 2-tuple whose first
    slot contains the item from seq and whose second slot contains
    the number of times that element has been encountered so far in
    the sequence, starting from the beginning (element 0).'''
    occurrences = dict()
    returnValue = list()
    for element in seq:
        previousNumber = occurrences[element] if element in occurrences else 0
        newNumber = previousNumber + 1
        occurrences[element] = newNumber
        returnValue.append((element, newNumber))
    return returnValue

def canonicalOrder(sequenceA, sequenceB):
    '''Returns a 2-tuple containing the two sequences re-ordered so that
    all shared elements come first in sorted order, followed by all
    remaining elements in sorted order.'''
    # Assign each occurrence of an item a different identifier
    # (unique only among all copies of the item on the same sequence)
    # This is so that when we convert to a set, multiple occurrences
    # are not condensed into one, but we can still intersect the two
    # lists
    aToOrder = countOccurrences(sequenceA)
    bToOrder = countOccurrences(sequenceB)
    # Start with the elements shared between the two lists
    commonElements = set(aToOrder).intersection(set(bToOrder))
    commonPrefix = sorted(list(commonElements))
    # Tack on the elements unique to each list
    aToOrder = commonPrefix + sorted(list(set(aToOrder) - set(bToOrder)))
    bToOrder = commonPrefix + sorted(list(set(bToOrder) - set(aToOrder)))
    # Finally, strip out the counting indices (this has a side effect of
    # converting the sequences to tuples, but it shouldn't matter!)
    aToOrder = zip(*aToOrder)[0]
    bToOrder = zip(*bToOrder)[0]
    return (aToOrder, bToOrder)
    
def lDistWithOptions(sequenceA, sequenceB, orderEquiv = False, subsEquiv = False, subpairs = standardSubPairs):
    '''Returns a modified Levenshtein distance with options.
    orderEquiv, if True (False by default), means that, for example,
    [A, B] and [B, A] will report a distance of 0 instead of 2.
    If set to True, the order of residues does not matter, and [A, B]
    and [B, A] will be considered equivalent (the presence and number of
    occurrences is all that matters).  subsEquiv, if True (False
    by default) means that X and the substitution of X are considered
    equivalent and will not increase the reported distance by 1, as
    would normally happen.  If left as False, if a residue in one
    sequence has been replaced by its substitution in the other, the
    reported distance will increase by 1 (being substitutible doesn't
    count for anything).  If order equivalence is selected, the order
    used for comparison will be all common elements first in sorted
    order, followed by all remaining elements in sorted order.'''
    # It is VERY important that the lists be reordered AFTER
    # substitution equivalence canonicalization is applied, if both are
    # selected, because otherwise we could still end up with the same
    # items in a different order.
    # Not sure what effect assigning to parameters might have outside
    # the function; I could look it up, or just do it this way
    tweakA = sequenceA
    tweakB = sequenceB
    # Apply substitution equivalence if desired
    if subsEquiv:
        tweakA = canonicalSubs(tweakA, subpairs)
        tweakB = canonicalSubs(tweakB, subpairs)
    else:
        # I could have used unSubPairs, but this seemed more efficient
        tweakA = sequenceToLowercase(tweakA)
        tweakB = sequenceToLowercase(tweakB)
    
    # Now apply order equivalence if desired
    if orderEquiv:
        tweakA, tweakB = canonicalOrder(tweakA, tweakB)
        
    return lDistBasic(tweakA, tweakB)
