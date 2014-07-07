'''Manages interactions between core ProMol analysis components and a database'''
import MySQLdb
import datetime
from pmg_tk.startup.ProMol import promolglobals as glb
#from pmg_tk.startup.ProMol import adminmanager as adm

class resultsManager:

    def __init__(self):
        #Connect to the database and create a cursor to deliver statements
        #Change to accept username/pw as arguments in real version
        #self.db = MySQLdb.connect("localhost", "", "", "promoldb4")
        self.db = MySQLdb.connect(glb.ADMIN.hostName, glb.ADMIN.user, glb.ADMIN.pw, glb.ADMIN.dbName)
        self.c = self.db.cursor()
        #A buffer to store individual results as they are generated
        self.resultsBuffer = []
        self.entryBuffer = []
        self.residueBuffer = []
        self.rmsdBuffer = []

    #Accepts the key pieces of information about each protein:motif result
    def addR(self, pid, mid, score, pv):
        self.resultsBuffer.append((str(pid).upper(), str(mid), float(pv[0]), float(pv[1])))
        self.entryBuffer.append((str(pid).upper(), str(mid), float(pv[0]),
                                 float(pv[1]), str(score), str(datetime.date.today())))

    def getResults(self, pid, mid, pv):
        query = (str(pid).upper(), str(mid), pv[0], pv[1])
        self.c.execute(
            """select result, id from results
            where pdbid = %s and motif = %s and pf = %s and version = %s""",
            query)
        result = self.c.fetchone()
        if result == None:
            return [False]
        else:
            return [True, result[0], result[1]]

    def getResidues(self, specID):
        self.c.execute(
            """select chain, name, number from resultspecs
            where resultid = %s""",
            specID)
        residues = self.c.fetchall()
        return residues

    def getRMSD(self, rmsdID):
        self.c.execute(
            """select total, alpha, alpha_beta from resultrmsd
            where resultid = %s""",
            rmsdID)
        RMSD = self.c.fetchone()
        if RMSD == None:
            return [False]
        elif RMSD[0] == None:
            return [False]
        else:
            return [True, RMSD[0], RMSD[1], RMSD[2]]
        
    def addSpec(self, chain, resname, resnum, pid, mid):
        #print "Adding the following values to the Spec buffer..."
        #print "chain: " + repr(chain)
        #print "name: " + repr(resname)
        #print "number: " + repr(resnum)
        #print "pid: " + pid.upper()
        #print "mid: " + repr(mid)
        self.residueBuffer.append((chain, resname, resnum, pid.upper(), mid))

    def addRMSD(self, allAtoms, A, AB, pid, mid):
        #print "Adding the following values to the RMSD buffer..."
        #print "allAtoms: " + repr(allAtoms)
        #print "A: " + repr(A)
        #print "AB: " + repr(AB)
        #print "pid: " + pid.upper()
        #print "mid: " + repr(mid)
        self.rmsdBuffer.append((allAtoms, A, AB, pid.upper(), mid))
    
    def inputFinished(self):
        #print "INPUT FINISHED"
        entries = []
        existingResults = []
        residueEntries = []
        rmsdEntries = []
        self.c.execute(
            """select max(id) from results""")
        maxID = self.c.fetchone()
        if maxID == None:
            maxID = 0
        elif maxID[0] == None:
            maxID = 0
        else:
            maxID = maxID[0]
        #print "MAXID = " + repr(maxID)
        #print "LENGTH OF resultsBuffer: " + repr(len(self.resultsBuffer))
        #retrieve existing matching results
        for r in self.resultsBuffer:
            self.c.execute(
                """select pdbid, motif, pf, version from results
                where pdbid = %s and motif = %s and pf = %s and version = %s""",
                r)
            existingResults.extend(self.c.fetchall())
        #print "LENGTH OF existingResults: " + repr(len(existingResults))                                    
        #enter in novel results
        for r in self.resultsBuffer:
            if r not in existingResults:
                entries.append(self.entryBuffer[self.resultsBuffer.index(r)])
        #print "LENGTH OF ENTRIES: " + repr(len(entries)) 
        if len(entries) > 0:
            self.c.executemany(
                """insert into results (pdbid, motif, pf, version, result, date)
                values (%s, %s, %s, %s, %s, %s)""",
                entries)
            #Commit the changes to the database
            self.db.commit()
        #Clear buffers
        self.resultsBuffer = []
        self.entryBuffer = []
        #print "ABOUT TO ADD RESIDUES"
        for res in self.residueBuffer:
            resultInfo = (maxID, res[3], res[4])
            #print "resultInfo = %s, %s, %s"%(resultInfo[0], resultInfo[1], resultInfo[2])
            self.c.execute(
                """select id from results
                where id > %s and pdbid = %s and motif = %s""",
                resultInfo)
            resultID = self.c.fetchone()
            if resultID == None:
                continue
            elif resultID[0] == None:
                continue
            else:
                resultID = resultID[0]
            residueEntries.append((res[0], res[1], res[2], resultID))
        #print "LENGTH OF RESIDUE ENTRIES: " + repr(len(residueEntries))
        if len(residueEntries) > 0:
            if not residueEntries[0][3] == 0:
                #print "Adding the following values to resultSpecs..."
                #print "chain: " + repr(residueEntries[0][0])
                #print "name: " + repr(residueEntries[0][1])
                #print "number: " + repr(residueEntries[0][2])
                #print "resultid: " + repr(residueEntries[0][3])
                self.c.executemany(
                    """insert into resultspecs (chain, name, number, resultid)
                    values (%s, %s, %s, %s)""",
                    residueEntries)
                #print "ABOUT TO COMMIT RESIDUE ENTRIES"
            self.db.commit()
        self.residueBuffer = []
        #print "ABOUT TO ADD RMSDs"
        #print "Length of rmsdBuffer = %s"%(len(self.rmsdBuffer))


        self.c.execute(
            """select id from results
            where id not in (select distinct resultid from resultrmsd)""")
        nonRmsdIDs = self.c.fetchall() #List of resultid's without corresponding rmsd entries
        #print "Length of nonRmsdIDs = %s"%(len(nonRmsdIDs))
        idLst = [] #List of resultid's without corresponding rmsd entries, reformatted
        for row in nonRmsdIDs:
            idLst.append(row[0])
        for dist in self.rmsdBuffer:
            if len(idLst) == 0:
                break
            resultInfo = (idLst, dist[3], dist[4])
            #print "resultInfo = %s, %s, %s"%(resultInfo[0], resultInfo[1], resultInfo[2])
            if len(idLst) > 1:
                self.c.execute(
                    """select id from results
                    where id in %s and pdbid = %s and motif = %s""",
                    resultInfo)
            else:
                self.c.execute(
                    """select id from results
                    where id = %s""",
                    resultInfo[0])
            resultID = self.c.fetchone()
            if resultID == None:
                continue
            elif resultID[0] == None:
                continue
            else:
                resultID = resultID[0]
            #print "resultID = %s"%(resultID)
            rmsdEntries.append((dist[0], dist[1], dist[2], resultID))
            idLst.remove(resultID)
        #print "LENGTH OF RMSD ENTRIES: " + repr(len(rmsdEntries))
        if len(rmsdEntries) > 0:
            if not rmsdEntries[0][0] == -1:
                #print "Adding the following values to resultRMSD..."
                #print "total: " + repr(rmsdEntries[0][0])
                #print "alpha: " + repr(rmsdEntries[0][1])
                #print "alpha_beta: " + repr(rmsdEntries[0][2])
                #print "resultid: " + repr(rmsdEntries[0][3])
                self.c.executemany(
                    """insert into resultrmsd (total, alpha, alpha_beta, resultid)
                    values (%s, %s, %s, %s)""",
                    rmsdEntries)
                #print "ABOUT TO COMMIT RMSD ENTRIES"
            self.db.commit()
        self.rmsdBuffer = []
        
        #Close the cursor and the database
        #Move these lines to a close function as this class gains
        #additional capabitities.
        self.c.close()
        self.db.close()

    #Below here is for client-server web-based database functions

    def batchQuery(self, pf, v, mids, pids, getRmsd):

        #Results are put into a dictionary within a dictionary.
        #If there wasn't a db entry for the pdb:motif pair,
        #no entry is made into the dictionary.
        #The dictionary's first key is a pdbid.
        #Its second key is a motif name.  The value of the combination
        #of keys is the corresponding result.
        #An individual result is stored as a list.
        #The first item is always a Levenshtein distance or 'NF'
        #If 'NF', it is the only item in the list.
        #Otherwise, it is followed by a list of lists.
        #Each list (except the last one, if RMSDs are being used)
        #contains chain/name/number info for each residue.
        #If RMSDs are being used, the final list contains the RMSD values
        #if any were found.  If not, this list contains [-1, -1, -1]. 
        
        #To store the result of an individual query
        result = None
        #To store the chain/name/number for the residues of a result
        specs = [None]
        #To store the rmsds of a result
        rmsds = [False]
        #To store all results information
        results = {}
        #To be given as the RMSD values when no RMSD values were
        #found in the database, but the pdb:motif pair was a hit.
        noRMSD = [-1, -1, -1]
        #Format precision factor and version into a list.
        pv = [pf, v]
        #For each structure
        for pid in pids:
            #Try each motif
            for mid in mids:
                #Query the database
                result = self.getResults(pid, mid, pv)
                if not result[0]:
                    #If there's no db entry, move on
                    continue
                else:
                    #Otherwise, set the first item in results to
                    #the levenshtein distance, or NF, meaning this
                    #query has been computed before, and the motif was
                    #not found, not that there was no entry in the db
                    results[pid] = {}
                    result = [result[1]]
                    if result[1] == 'NF':
                        #If the result is NF, store it and move on
                        results[pid][mid] = result
                        continue
                    else:
                        #Otherwise, get the chain/name/number info
                        specs = self.getResidues(result[2])
                        for residueInfo in specs:
                            #Enter these one at a time for each residue
                            result.append(residueInfo)
                        if getRmsd:
                            #If rmsds are being used, query the db
                            rmsds = self.getRMSD(result[2])
                            if rmsds[0]:
                                #If there was an rmsd entry, add it
                                result.append(rmsds[1:])
                            else:
                                #Otherwise, store the place holder value
                                result.append(noRMSD)
                        #Add the result to dictionary
                        results[pid][mid] = result
        #Return the dictionary
        return results

    def batchEntry(self, pf, ver, rmsdOn, entries):
        #Format precision factor and version
        pfv = [pf, ver]
        for pid in entries.keys():
            #For each structure
            for mid in entries[pid].keys():
                #For each motif associate with that structure
                if entries[pid][mid][0] != 'NF':
                    if len(entries[pid][mid]) > 1:
                        #If the result is positive, enter the lev. dist.
                        self.addR(pid, mid, entries[pid][mid][0], pfv)
                        for specs in entries[pid][mid][1:-1]:
                            #Enter chain/name/number info for the result
                            self.addSpec(specs[0], specs[1], specs[2], pid, mid)
                    if rmsdOn:
                        #If rmsds are being used, the last entry in the result
                        #is the rmsd values.  Enter these.
                        self.addRMSD(entries[pid][mid][-1][0],
                                     entries[pid][mid][-1][1],
                                     entries[pid][mid][-1][2], pid, mid)
                    else:
                        #If rmsds arent being used, the last item is
                        #another chain/name/number.  Enter this.
                        self.addSpec(entries[pid][mid][-1][0],
                                     entries[pid][mid][-1][1],
                                     entries[pid][mid][-1][2], pid, mid)
                else:
                    #If the result was NF, enter a negative result
                    rm.addR(pid, mid, 'NF', pfv)
                    rm.addRMSD(-1, -1, -1, pid, mid)
                    
                #Consider adding a way to do dm.allRun(pid) here

        rm.inputFinished()

        #Consider adding a dm.update() call here

        return "Database update complete."

                            
        
            
        
