#ProMol Session
#Session objects are used to do the work on the actual data of interest
import MySQLdb
import time
import datetime
import platform
import os

class Session:

    def __init__(self, host, name, pw, db, perms):
        self.rm = resultsManager(host, name, pw, db)
        self.dbm = databaseManager(host, name, pw, db)
        self.permissions = int(perms)

    def query(self, pf, v, mids, pids, rmsd):
        if rmsd is 1:
            getRmsd = True
        else:
            getRmsd = False
        try:
            self.rm.openCon()
            result = self.rm.batchQuery(pf, v, mids, pids, getRmsd)
            self.rm.close()

            resultLst = []
            pdbResLst = None
            rmsds = None
            res = None
            for pdb in result.keys():
                resultLst.append(pdb)
                pdbResLst = []
                for mid in result[pdb].keys():
                    if getRmsd and result[pdb][mid][0] != 'NF':
                        rmsds = []
                        for num in result[pdb][mid][-1]:
                            rmsds.append(str(num))
                        res = result[pdb][mid][0:-1]
                        res.append(rmsds)
                        pdbResLst.append([mid, res])
                    else:
                        pdbResLst.append([mid, result[pdb][mid]])
                resultLst.append(pdbResLst)
            return resultLst
        except Exception, e:
            print "Query failed: ", e
            return [None, e]

    def csvQuery(self, pids):
        try:
            self.dbm.openCon()
            print "About to query for structures:"
            print pids
            records = self.dbm.structureQuery(pids)
            self.dbm.close()
            return records
        except Exception, e:
            print "Structure query failed: ", e
            return None


    def entry(self, pf, ver, rmsdOn, entryLst, allRun):
        try:
            self.rm.openCon()
            if allRun is 1:
                self.dbm.openCon()
                for i in range(0, len(entryLst), 2):
                    self.dbm.allRun(entryLst[i])
                self.dbm.close()
            result = self.rm.batchEntry(pf, ver, rmsdOn, entryLst)
            self.rm.close()
            return result
        except Exception, e:
            print "Entry failed: ", e
            return e

    def update(self, structures, full):
        try:
            print "Updating..."
            self.dbm.openCon()
            print "Connection opened."
            if full is 1:
                return "Performing full update..."
                print "Performing full update..."
                self.dbm.update(structures)
                print "Full update complete."
            else:
                print "Updating structures..."
                self.dbm.updateStructures(structures)
                print "Structures updated."
            print "Closing connection..."
            self.dbm.close()
            print "Connection closed."
            return "Update completed successfully."
        except Exception, e:
            print "Update failed: ", e
            return e

##########################################################################
##########################################################################

class resultsManager:

    def __init__(self, host, user, pw, dbName):
        #Connect to the database and create a cursor to deliver statements
        self.host = host
        self.user = user
        self.pw = pw
        self.dbName = dbName

        self.db = None
        self.c = None
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
        self.residueBuffer.append((chain, resname, resnum, pid.upper(), mid))

    def addRMSD(self, allAtoms, A, AB, pid, mid):
        self.rmsdBuffer.append((allAtoms, A, AB, pid.upper(), mid))
    
    def inputFinished(self):
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
        for r in self.resultsBuffer:
            self.c.execute(
                """select pdbid, motif, pf, version from results
                where pdbid = %s and motif = %s and pf = %s and version = %s""",
                r)
            existingResults.extend(self.c.fetchall())
        for r in self.resultsBuffer:
            if r not in existingResults:
                entries.append(self.entryBuffer[self.resultsBuffer.index(r)])
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
        for res in self.residueBuffer:
            resultInfo = (maxID, res[3], res[4])
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
        if len(residueEntries) > 0:
            if not residueEntries[0][3] == 0:
                self.c.executemany(
                    """insert into resultspecs (chain, name, number, resultid)
                    values (%s, %s, %s, %s)""",
                    residueEntries)
            self.db.commit()
        self.residueBuffer = []


        self.c.execute(
            """select id from results
            where id not in (select distinct resultid from resultrmsd)""")
        nonRmsdIDs = self.c.fetchall() #List of resultid's without corresponding rmsd entries
        idLst = [] #List of resultid's without corresponding rmsd entries, reformatted
        for row in nonRmsdIDs:
            idLst.append(row[0])
        for dist in self.rmsdBuffer:
            if len(idLst) == 0:
                break
            resultInfo = (idLst, dist[3], dist[4])
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
            rmsdEntries.append((dist[0], dist[1], dist[2], resultID))
            idLst.remove(resultID)
        if len(rmsdEntries) > 0:
            if not rmsdEntries[0][0] == -1:
                self.c.executemany(
                    """insert into resultrmsd (total, alpha, alpha_beta, resultid)
                    values (%s, %s, %s, %s)""",
                    rmsdEntries)
            self.db.commit()
        self.rmsdBuffer = []


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
        noRMSD = ['-1.0', '-1.0', '-1.0']
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
                    if not pid in results.keys():
                        results[pid] = {}
                    resultLst = [result[1]]
                    if result[1] == 'NF':
                        #If the result is NF, store it and move on
                        results[pid][mid] = resultLst
                        continue
                    else:
                        #Otherwise, get the chain/name/number info
                        specs = self.getResidues(result[2])
                        for residueInfo in specs:
                            #Enter these one at a time for each residue
                            resultLst.append(residueInfo)
                        if getRmsd:
                            #If rmsds are being used, query the db
                            rmsds = self.getRMSD(result[2])
                            if rmsds[0]:
                                #If there was an rmsd entry, add it
                                resultLst.append(rmsds[1:])
                            else:
                                #Otherwise, store the place holder value
                                resultLst.append(noRMSD)
                        #Add the result to dictionary
                        results[pid][mid] = resultLst
        #Return the dictionary
        return results

    def batchEntry(self, pf, ver, rmsdOn, entryLst):
        if not rmsdOn is 1:
            rmsdOn = False
        pfv = [pf, ver]
        for i in range(0, len(entryLst), 2):
            pid = entryLst[i]
            for j in entryLst[i+1]:
                mid = j[0]
                res = j[1]
                if res[0] != 'NF':
                    if res[0] != 'RMSD':
                        #If the result is positive, enter the lev. dist.
                        self.addR(pid, mid, res[0], pfv)
                        for specs in res[1:-1]:
                            #Enter chain/name/number info for the result
                            self.addSpec(specs[0], specs[1], specs[2], pid, mid)
                    if rmsdOn:
                        #If rmsds are being used, the last entry in the result
                        #is the rmsd values.  Enter these.
                        self.addRMSD(res[-1][0],
                                     res[-1][1],
                                     res[-1][2], pid, mid)
                    else:
                        #If rmsds arent being used, the last item is
                        #another chain/name/number.  Enter this.
                        self.addSpec(res[-1][0],
                                     res[-1][1],
                                     res[-1][2], pid, mid)
                else:
                    #If the result was NF, enter a negative result
                    self.addR(pid, mid, 'NF', pfv)

        self.inputFinished()

        return "Database entries made successfully."

    def openCon(self):
        #The connect must be closed when this function is called or
        #a an error '_mysql_exception.ProgrammingError' is generated
        self.db = MySQLdb.connect(self.host, self.user, self.pw, self.dbName)
        self.c = self.db.cursor()
    
    def close(self):
        self.c.close()
        self.db.close()


##########################################################################
##########################################################################

class databaseManager:

    def __init__(self, host, user, pw, dbName):
        #Create db connection and cursor
        self.host = host
        self.user = user
        self.pw = pw
        self.dbName = dbName

        self.dbc = None
        self.cur = None
        

    def updateStructuresFully(self, pdbs):
        pdbids = []
        for pdb in pdbs:
            pdbids.append(pdb.strip().upper())
        #Get the pdbids from the results table
        self.cur.execute(
            """select distinct pdbid from results
            where pdbid not in (select id from structures)""")
        dbpdbs = self.cur.fetchall()
        dbids = []
        if not dbpdbs == None:
            for pdb in dbpdbs:
                dbids.append(pdb[0])
            pdbids.extend(dbids)
    
        if len(pdbids) > 0:
            self.cur.executemany(
                """insert ignore into structures (id)
                values (%s)""",
                pdbids)
            self.dbc.commit()
        #Check the results table for all hits for each pdbid
        #from the structures table
        self.cur.execute(
            """select id from structures""")
        allIDs = self.cur.fetchall()
        pids = []
        if not allIDs == None:
            for i in allIDs:
                pids.append(i[0])
        for i in pids:
            self.cur.execute(
                """select distinct motif from results
                where pdbid = %s and result != 'NF'""",
                i)
            hits = self.cur.fetchall()
            #Check the motifcount for each pdbid in the structures table
            #and make sure the counts match.  If they don't, update
            #the structures table
            count = 0
            if hits != None and len(hits) > 0:
                count = len(hits)
            else:
                count = 0
            self.cur.execute(
                """select motifcount from structures
                where id = %s""",
                i)
            resultCount = self.cur.fetchone()
            pcount = None;
            if not resultCount[0] == None:
                pcount = int(resultCount[0])
            if not count == pcount:
                self.cur.execute(
                    """update structures
                    set motifcount = %s
                    where id = %s""",
                    (count, i))
                
        self.dbc.commit()
        #Check the date the results in the results table for each
        #id and for each type of motif (j, p, other).  Update the
        #run dates in the structures table.
        #the allrun date has to be update at the time of the run
        for i in pids:
            self.cur.execute(
                """select max(date) from results
                where motif like %s
                and pdbid = %s""",
                ('J%', i))
            jdateresult = self.cur.fetchone()
            self.cur.execute(
                """select max(date) from results
                where motif like %s
                and pdbid = %s""",
                ('P%', i))
            pdateresult = self.cur.fetchone()
            self.cur.execute(
                """select max(date) from results
                where motif like %s
                and pdbid = %s""",
                ('N%', i))
            ndateresult = self.cur.fetchone()
            self.cur.execute(
                """select max(date) from results
                where motif not like %s
                and motif not like %s
                and motif not like %s
                and pdbid = %s""",
                ('J%', 'P%', 'N%', i))
            udateresult = self.cur.fetchone()
            jdate = None
            pdate = None
            ndate = None
            udate = None
            if not jdateresult[0] == None:
                jdate = str(jdateresult[0])
            if not pdateresult[0] == None:
                pdate = str(pdateresult[0])
            if not ndateresult[0] == None:
                ndate = str(ndateresult[0])
            if not udateresult[0] == None:
                udate = str(udateresult[0])
            if not jdate == None:
                self.cur.execute(
                    """update structures
                    set jrun = %s
                    where id = %s""",
                    (jdate, i))
            if not pdate == None:
                self.cur.execute(
                    """update structures
                    set prun = %s
                    where id = %s""",
                    (pdate, i))
            if not ndate == None:
                self.cur.execute(
                    """update structures
                    set nrun = %s
                    where id = %s""",
                    (ndate, i))
            if not udate == None:
                self.cur.execute(
                    """update structures
                    set myrun = %s
                    where id = %s""",
                    (udate, i))
        self.dbc.commit()
        
        
    def updateMotifsFully(self):

        #get the names of all the motifs
        #Fill these in with the absolute file paths of these two folders,
        #which must be present on the server and contain all motifs
        motfolder = "/FILL_IN/Motifs")
        usrmotfolder = "/FILL_IN/UserMotifs")
        
        motnames = []
        motfiles = os.listdir(motfolder)
        for motfile in motfiles:
            if motfile.endswith('.py'):
                motnames.append(motfile.split('.')[0])
        usrmotfiles = os.listdir(usrmotfolder)
        for usrmotfile in usrmotfiles:
            if usrmotfile.endswith('.py'):
                motnames.append(usrmotfile.split('.')[0])
        #Make sure all of the motifs are in the motifs table
        #if they're not, update the table to include motif names, their
        #sets (as determined by their names) and todays date
        self.cur.execute(
            """select id from motifs""")
        midresults = self.cur.fetchall()
        mids = []
        if not midresults == None:
            for m in midresults:
                mids.append(m[0])
        newMotifs = []
        for name in motnames:
            if name not in mids:
                newMotifs.append(name)

        for motif in newMotifs:
            if motif[0] == 'J':
                setName = 'J Set'
            elif motif[0] == 'P':
                setName = 'P Set'
            elif motif[0] == 'N':
                setName = 'N Set'
            else:
                setName = 'User Set'
            self.cur.execute(
                """insert into motifs (id, setname, added)
                values (%s, %s, curdate())""",
                (motif, setName))
        self.dbc.commit()
        #Check the results table for all hits from each motif in the motifs
        #table.  Count the hits and update the foundin field for the motif.
        self.cur.execute(
            """select id from motifs""")
        midresults = self.cur.fetchall()
        mids = []
        if not midresults == None:
            for m in midresults:
                mids.append(m[0])
        for mid in mids:
            self.cur.execute(
                """select count(distinct pdbid) from results
                where motif = %s and result != 'NF'""",
                mid)
            countr = self.cur.fetchone()
            count = 0
            if not countr == None:
                count = int(countr[0])
            self.cur.execute(
                """update motifs
                set foundin = %s where id = %s""",
                (count, mid))
        self.dbc.commit()

    def updateMotifSetsFully(self):
        #Count the motifs from the motifs table for each set
        #and update the set's count.  If any motifs date added
        #is newer than the modified date in the motifs table,
        #update the modified date to the motif's date.
        #If the count has gone down, set the modified date to
        #today's date.
        self.cur.execute(
            """select setname, count(id), max(added) from motifs
            group by setname""")
        motifResults = self.cur.fetchall()
        motifSet = []
        motifCount = []
        motifDate = []
        if not motifResults == None:
            for m in motifResults:
                motifSet.append(m[0])
                motifCount.append(int(m[1]))
                motifDate.append(m[2])
        self.cur.execute(
            """select id, motifcount, modified from motifsets""")
        setResults = self.cur.fetchall()
        setID = []
        setCount = []
        setDate = []
        for r in setResults:
            setID.append(r[0])
            setCount.append(int(r[1]))
            setDate.append(r[2])
        for s in setID:
            i = setID.index(s)
            try:
                j = motifSet.index(s)
            except ValueError:
                continue
            if (not motifCount[j] == setCount[i]):
                self.cur.execute(
                    """update motifsets
                    set modified = curdate(),
                    motifcount = %s
                    where id = %s""",
                    (motifCount[j], s))
            if (motifDate[j] > setDate[i]):
                self.cur.execute(
                    """update motifsets
                    set modified = curdate()
                    where id = %s""",
                    s)
        self.dbc.commit()

    def update(self, pdbs):
        print "Updating"
        self.updateStructuresFully(pdbs)
        print "Updated structures fully"
        self.updateMotifsFully()
        print "Update motifs fully"
        self.updateMotifSetsFully()
        print "Updated motif sets fully"
        
    def updateStructures(self, pdbs):
        #Add structures to db
        pdbids = []
        for pdb in pdbs:
            pdbids.append(pdb.strip().upper())
        if len(pdbids) > 0:
            self.cur.executemany(
                """insert ignore into structures (id)
                values (%s)""",
                pdbids)
            self.dbc.commit()


    def allRun(self, pdb):
        #update the allrun date for the protein
        #to todays date
        pdbid = pdb.upper()
        self.cur.execute(
            """update structures
            set allrun = curdate()
            where id = %s""",
            pdbid)
        self.dbc.commit()

    def structureQuery(self, pdbs):

        print "In DBM, about to query for structures in:"
        print pdbs
        
        records = []
        
        for pdb in pdbs:           
            self.cur.execute(
                """select id, allrun, jrun, prun, myrun from structures
                where id = %s""",
                pdb)

            result = self.cur.fetchone()
            if result == None:
                continue
            
            record = [result[0]]
            for date in result:
                if not date == None:
                    record.append(1)
                else:
                    record.append(0)

            records.append(record)
            
        print "Records:"
        print records
        return records

    def openCon(self):
        #The connect must be closed when this function is called or
        #a an error '_mysql_exception.ProgrammingError' is generated
        self.dbc = MySQLdb.connect(self.host, self.user, self.pw, self.dbName)
        self.cur = self.dbc.cursor()
    
    def close(self):
        self.cur.close()
        self.dbc.close()
