import os, sys
from urllib import urlretrieve, urlopen
from collections import Counter
from HTMLParser import HTMLParser

CSA_URL = 'http://www.ebi.ac.uk/thornton-srv/databases/CSA/downloads/CSA_2_0_121113.txt'
CSA_DIR = ''
pdbID_to_EC = {}

class CSALibConstructor():
    
    def __init__(self):
        litEntryNoEC = Counter()
        # construct the pdbID to EC class dictionary from CSA source (apparently incomplete).
        file = urlopen('http://www.ebi.ac.uk/thornton-srv/databases/CSA/BrowseByLit.php')
        CSAHTMLParser().feed(file.read())
        file.close()
        # append the additional CSA entries from Dr. Berstein's list of randomEC pdbs (still incomplete).
        with open('randomEC.csv', 'rU') as fin:
            fin.readline() # advance past header
            for line in fin.readlines():
                pdbID_to_EC[line.split(',',1)[0]] = line.rsplit(',',2)[1]
        # retieve the most recent CSA motif specifications
        try:
            urlretrieve(CSA_URL, 'CSA_2_0_121113.txt')
        except BaseException as err:
            print 'CSA Retrieval Exception:', err
        else:
            motifs = {}
            uniqueMotifs = {}
            multiChains = 0
            evidenceType = Counter()
            with open('CSA_2_0_121113.txt', 'rU') as fin:
                fin.readline() # advance past header
                for line in fin.readlines():
                    pdbID, siteID, resData = line.strip().split(',',2)
                    try:
                        motifs[(pdbID, siteID)].append(resData)
                    except KeyError:
                        motifs[(pdbID, siteID)] = [resData]
            with open('CSA_motif_lib_'+'CSA_2_0_121113.txt'.split('_',1)[1], 'w') as fout:
                for (pdbID, siteID), resDataList in motifs.items():
                    chains = Counter()
                    motifFingerprint = [pdbID]
                    evidence, num, litEntry = None, None, None
                    resStr = ''
                    for resData in resDataList:
                        res, chain, num, chem, evidence, litEntry = resData.split(',')
                        motifFingerprint.append(res+num+litEntry)
                        resStr += '%s\t%s\t%s\t%s\n' % (res.upper(), chain, num, chem)
                        chains[chain] += 1
                    try:
                        ecNum = pdbID_to_EC[litEntry]
                    except KeyError:
                        try: # attempt to retrieve the EC class from the Protein Data Bank.
                            file = urlopen('http://www.rcsb.org/pdb/rest/describeMol?structureId=%s' % litEntry)
                            ecNum = file.read().split('ec="',1)[1].split('"',1)[0]
                        except BaseException as err:
                            print 'x2', err
                            litEntryNoEC[litEntry] += 1
                            ecNum = '-.-.-.-'
                        finally:
                            file.close()
                    finally:
                        ecNumList = ecNum.split('.')
                        while len(ecNumList) < 4:
                            ecNumList.append('-')
                        ecNum = '.'.join(ecNumList)
                        fingerprintStr = ''.join(sorted(motifFingerprint))
                        outputTuple = (siteID, '> %s.%s\t%s\t%s\n%s' % (pdbID, ','.join(sorted(chains.keys())), litEntry, ecNum, resStr))
                        try:
                            uniqueMotifs[fingerprintStr].append(outputTuple)
                        except KeyError:
                            uniqueMotifs[fingerprintStr] = [outputTuple]
                    if len(chains) > 1: multiChains +=1
                    evidenceType[evidence] += 1
                for uniqueMotifList in uniqueMotifs.values():
                    siteID, uniqueMotif = min(uniqueMotifList, key=lambda x: int(x[0]))
                    fout.write(uniqueMotif)                       
            print 'Total motifs:', len(uniqueMotifs)
            print 'LIT:', evidenceType['LIT'], 'HOM:', evidenceType['HOM']
            print 'Multi-chain motifs:', multiChains
            print 'PDBs w/o EC:',len(litEntryNoEC)
            print litEntryNoEC
                    
class CSAHTMLParser(HTMLParser):

    def __init__(self):
        self.table = False
        self.ecData = None
        HTMLParser.__init__(self)
        
    def handle_starttag(self, tag, attrs):
        if tag == 'table' and attrs[0][1] == 'contentspane':
            self.table = True
        if self.table:
            pass #print 'start', tag, attrs

    def handle_endtag(self, tag):
        if self.table:
            pass #print 'end', tag
        if tag == 'table': self.table = False

    def handle_data(self, data):
        #if self.table:
        data = data.strip()
        #print 'data', data, len(data)
        if len(data) == 4:
            self.ecData = data
        if len(data.split('.')) == 4:
            pdbID_to_EC[self.ecData] = data
            #print 'data', data
        


if __name__ == '__main__':
##    file = urlopen('http://www.ebi.ac.uk/Tools/dbfetch/dbfetch/pdbsum/GetPage.pl?pdbcode=1jms&template=protein.html&o=CSA&l=1.1&c=10')
##    file = urlopen('http://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/pdbsum/GetPage.pl?pdbcode=1jms&template=protein.html&o=CSA&l=1.1&c=10')
##    CSAHTMLParser().feed(file.read())
##    file.close()
    CSALibConstructor()
