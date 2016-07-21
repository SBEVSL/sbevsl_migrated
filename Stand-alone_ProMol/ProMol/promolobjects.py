from urllib import urlopen
from math import sqrt
import os
from ProMol.promolglobals import FETCH_PATH

BASE_TOLERANCE = 2.0 # this value indicates the amount of 'wiggle room' searing motif have

class Protein:
    '''A protein object for use by ProMol. Can be either a full protein or a motif'''
    def __init__(self):
        self.name = ""
        self.pfam = ""
        self.ec = ""
        self.uniprot = ""
        self.residues = []

    def readMotifFile(self,filename):
        '''Read a ProMol motif file into this protein'''
        self.name = filename.split('\\')[-1].rsplit('.',1)[0]
        self.ec = self.name.split('_')[0]
        if self.name.split('_')[1].startswith('PF'):
            self.pfam = self.name.split('_')[1]
            self.uniprot = "" #in case this protein object was already set as something else
        else:
            self.uniprot = self.name.split('_')[1]
            self.pfam = "" #in case this protein object was already set as something else
        
        pdbfile = open(filename,"r")
        lines = pdbfile.readlines()
        pdbfile.close()
        identifier = lines[0][21:26].strip()
        residue = Residue(lines[0][17:20].strip(),int(lines[0][22:26].strip()),lines[0][21])
        # for future reference: info on coordinate pdb file formatting can be
        # found at http://deposit.rcsb.org/adit/docs/pdb_atom_format.html
        for line in lines:
            if line.startswith("END"):
                self.residues.append(residue)
                break
            elif not line.startswith("ATOM") and not line.startswith("HETATM"):
                continue
            elif identifier!=line[21:26].strip():
                self.residues.append(residue)
                identifier = line[21:26].strip()
                residue = Residue(line[17:20].strip(),                      \
                                  int(line[22:26].strip()),line[21])
            atom = Atom(line[12:16].strip(),float(line[30:38].strip()),     \
                        float(line[38:46].strip()),                         \
                        float(line[46:54].strip()),                         \
                        line[76:78].strip(),line)
            residue.atoms.append(atom)
            if atom.name=="CA":
                residue.setCACoordinates(float(line[30:38].strip()),        \
                                         float(line[38:46].strip()),        \
                                         float(line[46:54].strip()))
        # The following will set up the distances from the CA of each residue
        # to each other type of residue, i.e. each residue will contain a
        # distance dictionary where the keys are the types of residues and the
        # values are a dictionary where the keys are distances and the values
        # are corresponding residues. There technically could be a chance that
        # two residues of the same kind could be the exact same distance from
        # the same residue, but the chances of that seem so insiginificant,
        # doesn't really seem worth taking into account for now.
        for res in self.residues:
            for other in self.residues:
                if res==other:
                    continue
                res.distances[other] = res.CACoordinates.distanceTo(other.CACoordinates)
        
    def getPDB(self,pdbid):
        '''Write this protein as a PDB based of an ID'''
        self.name = pdbid
        if os.path.exists(os.path.join(FETCH_PATH,pdbid.upper()+".pdb")):
            pdbfile = open(os.path.join(FETCH_PATH,pdbid.upper()+".pdb"),"r")
            lines = pdbfile.readlines()
        else:
            pdbfile = urlopen('http://www.rcsb.org/pdb/files/%s.pdb'%pdbid).read()
            lines = pdbfile.split('\n')
            # Stores the pdb in a cache for later use so that don't always have
            # to grab from the internet. 
            newpdbfile = open(os.path.join(FETCH_PATH,pdbid.upper()+".pdb"),"w+")
            for line in lines:
                newpdbfile.write(line + '\n')
            newpdbfile.writelines(lines)
            newpdbfile.close
            
        identifier = ""
        residue = None
        # for future reference: info on pdb file formatting can be found at
        # http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html
        # Currently, this only uses the coordinate section
        for line in lines:
            if line.startswith("END"):
                # Could just be 'END' or 'ENDMDL'. 'END' is just the end of a
                # file. 'ENDMDL' denotes the end of a single structure in files
                # with more than one structures, such as NMR. At this point,
                # just going to take the first of those as the used structure.
                self.residues.append(residue)                
                break
            elif line[17:20].strip()=="HOH":
                #ignore water, who needs that?
                continue                
            elif not line.startswith("ATOM") and not line.startswith("HETATM"):
                continue
            elif identifier=="":
                identifier = line[21:26].strip()
                residue = Residue(line[17:20].strip(),                      \
                                  int(line[22:26].strip()),line[21])
            elif identifier!=line[21:26].strip():
                self.residues.append(residue)
                identifier = line[21:26].strip()
                residue = Residue(line[17:20].strip(),                      \
                                  int(line[22:26].strip()),line[21])
                # This sets the first atom in the set as the CA coordinate,
                # for use in case there is no CA atom in a residue, such as
                # in a heme group
                residue.setCACoordinates(float(line[30:38].strip()),        \
                                         float(line[38:46].strip()),        \
                                         float(line[46:54].strip()))
                
            atom = Atom(line[12:16].strip(),float(line[30:38].strip()),     \
                        float(line[38:46].strip()),                         \
                        float(line[46:54].strip()),                         \
                        line[76:78].strip(),line)
            residue.atoms.append(atom)
            if atom.name=="CA":
                residue.setCACoordinates(float(line[30:38].strip()),        \
                                         float(line[38:46].strip()),        \
                                         float(line[46:54].strip()))

        # The following will set up the distances from the CA of each residue
        # to each other type of residue, i.e. each residue will contain a
        # distance dictionary where the keys are the types of residues and the
        # values are a dictionary where the keys are distances and the values
        # are corresponding residues. There technically could be a chance that
        # two residues of the same kind could be the exact same distance from
        # the same residue, but the chances of that seem so insiginificant,
        # doesn't really seem worth taking into account for now.
        for res in self.residues:
            for other in self.residues:
                if res==other:
                    continue
                if res.distances.has_key(other.name):
                    res.distances[other.name][res.CACoordinates.distanceTo(other.CACoordinates)] = other
                else:
                    res.distances[other.name] = {}
                    res.distances[other.name][res.CACoordinates.distanceTo(other.CACoordinates)] = other

    def searchMotif(self,motif,precision):
        '''Finds a motif within this protein, +/- the given tolerance in angstroms.
Returns a Protein object that is the motif or False if the motif is not found'''
        # Currently, this method does not deal with substitutions or missing residues
        # Matches are exact (within the tolerance of distance given)
        tolerance = BASE_TOLERANCE*precision
        motifResidues = list(motif.residues)
        for queryResidue in self.residues:
            if queryResidue.name!=motifResidues[0].name:
                # This will give us a starting point, we know the first residue
                # is there, we can then search for the rest of the residues
                # from there
                continue
            found = True
            focusedResidue = queryResidue
            foundResidues = list()
            foundResidues.append(focusedResidue)
            for i in range(len(motifResidues)):
                hasDistance = False
                nextResidueDistance = None
                for j in range(i+1,len(motifResidues)):
                    hasDistance = False
                    motifDistance = motifResidues[i].distances[motifResidues[j]]
                    for distance in focusedResidue.distances[motifResidues[j].name].keys():
                        if distance>motifDistance-tolerance and distance<motifDistance+tolerance:
                            hasDistance = True
                            if j==i+1:
                                nextResidueDistance = distance
                            break
                    if not hasDistance:
                        break
                if not hasDistance:
                    break
                focusedResidue = focusedResidue.distances[motifResidues[i+1].name][nextResidueDistance]
                foundResidues.append(focusedResidue)
            if len(foundResidues)==len(motifResidues): #i.e., all residues found
                result = Protein()
                result.name = self.name
                result.pfam = motif.pfam
                result.ec = motif.ec
                result.uniprot = motif.uniprot
                result.residues = foundResidues
                return result
        return False

    def writeMotif(self,filename):
        '''Writes this motif as a motiffile in the given directory.
It overwrites the file if it is already present'''
        print filename
        motifFile = open(filename,"w+")
        atomNumber = 1
        for residue in self.residues:
            line = ''
            for atom in residue.atoms:
                line = atom.line[:6] + str(atomNumber).rjust(5) +                  \
                       atom.line[11:30] + ('%.3f'%(atom.coordinates.x)).rjust(8) + \
                       ('%.3f'%(atom.coordinates.y)).rjust(8) +                    \
                       ('%.3f'%(atom.coordinates.z)).rjust(8) + atom.line[54:]
                atomNumber+=1
                motifFile.write(line)
            if residue==self.residues[-1]:
                motifFile.write('END\n')
            else:
                line = 'TER   ' + str(atomNumber).rjust(5) + '      ' +             \
                       line[17:27] + '\n'
                atomNumber+=1
                motifFile.write(line)
        motifFile.close()
        
class Residue:
    '''Residue objects, generally of amino acids, but could be other types'''
    def __init__(self,name,index,chain):
        self.name = name
        self.index = index
        self.chain = chain
        self.atoms = list()
        self.CACoordinates = None
        self.distances = {}

    def setCACoordinates(self,x,y,z):
        '''Sets the carbon alpha coordinates of this residue'''
        self.CACoordinates = Coordinates(x,y,z)

class Atom:
    '''Atom objects, for any kind of atom'''
    def __init__(self,name,x,y,z,element,pdbline):
        self.name = name
        self.coordinates = Coordinates(x,y,z)
        self.element = element
        self.line = pdbline

    def getCoordinates(self):
        '''Returns the coordinates of this atom object in [x,y,z]'''
        return self.x,self.y,self.z

class Coordinates:
    '''Coordinate object, containing an x, y and z coordinate'''
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self,other):
        '''Returns the distance to another Coordintes object'''
        return sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2)+pow(self.z-other.z,2))
                                         
