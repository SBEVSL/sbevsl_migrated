'''Manages interactions between core ProMol analysis components and a database'''
import MySQLdb
import datetime
from pmg_tk.startup.ProMol import promolglobals as glb

class resultsManager:

    def __init__(self):
        #Connect to the database and create a cursor to deliver statements
        #Change to accept username/pw as arguments in real version
        #self.db = MySQLdb.connect("localhost", "root", "Alcanest1", "promoldb4")
        self.db = MySQLdb.connect(glb.HOST, glb.UN, glb.PW, glb.DB)
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
        #STOPPED HERE
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
        
