'''Maintains non-result database tables and mediates user-db interaction'''
import MySQLdb
import datetime
import os
from pmg_tk.startup.ProMol import promolglobals as glb
#from pmg_tk.startup.ProMol import adminmanager as adm

class databaseManager:

    def __init__(self):
        #Create db connection and cursor
        self.dbc = MySQLdb.connect(glb.ADMIN.hostName, glb.ADMIN.user, glb.ADMIN.pw, glb.ADMIN.dbName)
        self.cur = self.dbc.cursor()

    def updateStructuresFully(self, pdbs):
        #Get existing ids from structures table
        self.cur.execute(
            """select id from structures""")
        IDresults = self.cur.fetchall()
        existingIDs = []
        if not IDresults == None:
            for i in IDresults:
                if not i == None:
                    existingIDs.append(i[0])
        #Get any ids from the text box in the gui
        #and convert them to uppercase
        #pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
        pdbids = []
        if not (len(pdbs) == 1 and pdbs[0] == ''):
            for pdb in pdbs:
                pdbids.append(pdb.strip().upper())
        #Get the pdbids from the results table
        self.cur.execute(
            """select distinct pdbid from results""")
        dbpdbs = self.cur.fetchall()
        dbids = []
        if not dbpdbs == None:
            for pdb in dbpdbs:
                dbids.append(pdb[0])
        pdbids.extend(dbids)
        IDentries = []
        #If there are any new ids from the text box or the results table,
        #add them to the structures table
        for p in pdbids:
            if p not in existingIDs:
                IDentries.append((p))
        if len(IDentries) > 0:
            self.cur.executemany(
                """insert into structures (id)
                values (%s)""",
                IDentries)
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
        #Check the motifs folder in pymol and the usermotifs folder in sbevsl
        #get the names of all the motifs
        motfolder = glb.MOTIFSFOLDER
        usrmotfolder = glb.USRMOTIFSFOLDER
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
        oldMotifs = []
        for mid in mids:
            if mid not in motnames:
                oldMotifs.append(mid)
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
        for motif in oldMotifs:
            self.cur.execute(
                """delete from motifs
                where id = %s""",
                motif)
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
        self.updateStructuresFully(pdbs)
        self.updateMotifsFully()
        self.updateMotifSetsFully()
        
    def updateStructures(self, pdbs):
        #Get the ids from the gui and convert them to uppercase
        #pdbs = glb.GUI.motifs['multipdb'].get(1.0,'1.end').split(',')
        pdbids = []
        for pdb in pdbs:
            pdbids.append(pdb.strip().upper())
        #Get the ids from structures table
        self.cur.execute(
            """select id from structures""")
        IDresults = self.cur.fetchall()
        existingIDs = []
        if not IDresults == None:
            for i in IDresults:
                if not i == None:
                    existingIDs.append(i[0])
        #If any of the ids from the gui aren't in the structures table, add them
        IDentries = []
        for p in pdbids:
            if p not in existingIDs:
                IDentries.append((p))
        if len(IDentries) > 0:
            self.cur.executemany(
                """insert into structures (id)
                values (%s)""",
                IDentries)
            self.dbc.commit()

        #Maybe only do this in updateStructuresFully...
        
        #Check the results table for analyses of all structures in the table
        #and get the date of the analysis for each motif set and
        #update the structures table
        
        #Get the count of the hit for each protein in the structures table
        #from results and update the hits count

    #def updateMotifs(self):
        
        #Maybe on do this in updateMotifsFully...
        
        #Get the found in value from results for each motif in the
        #table and compare to the motif's foundin value in the table.
        #Update as needed.

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

    def openCon(self):
        #The connect must be closed when this function is called or
        #a an error '_mysql_exception.ProgrammingError' is generated
        self.dbc = MySQLdb.connect(glb.ADMIN.hostName, glb.ADMIN.user, glb.ADMIN.pw, glb.ADMIN.dbName)
        self.cur = self.dbc.cursor()
    
    def close(self):
        self.cur.close()
        self.dbc.close()
