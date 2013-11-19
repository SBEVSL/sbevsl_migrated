import MySQLdb
import atexit
from ZSI.client import AUTH, Binding
from pmg_tk.startup.ProMol import promolglobals as glb
import tkMessageBox
import platform
import os

class adminManager:

    def __init__(self):

        self.server = None #Use for ZSI Binding object
        
        self.useDB = False #Boolean for whether or not db features are being used
        self.isDB = False #True if this is the host application for a db, else false
        
        self.user = "" #The username for the db connection
        self.pw = "" #pw for the db connection
        self.dbName = "" #Name of the database being used
        self.hostName = "" #Identifier of the server hosting the db
        
        self.token = None #To store a session token
        self.permissions = None
        self.binding = None

        atexit.register(self.exit_logout)

    def toggleDB(self):
        self.useDB = not self.useDB
        if self.useDB:
            
            #USE IN PRODUCTION
            self.hostName = glb.GUI.db_admin['Server'].get()
            self.user = glb.GUI.db_admin['Username'].get()
            self.pw = glb.GUI.db_admin['Password'].get()

            if self.user is 'Username' or self.pw is 'Password':
                self.useDB = not self.useDB
                tkMessageBox.showerror("Connection Attempt Aborted",
                                           "You must enter your username and password" +
                                           "  into the appropriate boxes.")
                return
            
            self.dbName = glb.GUI.db_admin['Database'].get()
            fp = open('tracefile_log.txt', 'w')
            self.binding = Binding(host=self.hostName[8:].split('/')[0],
                                   port=443, ssl=1, url=self.hostName, tracefile=fp)

            print "Successfully connected."
            
            try:
                print "About to try to get a session..."
                sessionInfo = self.binding.login()
                print "RECEIVED"
                print "sessionInfo :", str(sessionInfo)
                if sessionInfo is None:
                    self.useDB = False
                    self.isDB = False
                    tkMessageBox.showerror("Database Connection Failed",
                                           "Failed to connect to the database." +
                                           "  See the PyMOL console for details.")
                    print "Failed with sessionInfo = None"
                    print e
                else:
                    self.token = sessionInfo[0]
                    self.permissions = sessionInfo[1]
                    if self.permissions != "0":
                        self.fullUpdate([])
            except Exception as e:
                self.useDB = False
                self.isDB = False
                tkMessageBox.showerror("Database Connection Failed",
                                       "Failed to connect to the database." +
                                       "  See the PyMOL console for details.")
                print "Failed without getting anything..."
                print e
            else:
                glb.GUI.db_admin['Use Database'].config(text='Disconnect')
                if self.hostName == "localhost":
                    self.isDB = True
                else:
                    self.isDB = False
        else:
            try:
                response = self.binding.logout([self.token])
                if response is None:
                    tkMessageBox.showerror("No active session found")
                else:
                    print "Success"
            except Exception, e:
                print "Logout failed: ", e
            glb.GUI.db_admin['Use Database'].config(text='Connect')
            
    #Experimental...should not use.
    def submitCSVs(self):
        if self.permissions != "2":
            print "You don't have access to that feature."
            return
        
        #List of files in target directory
        PLATFORM = platform.system()
        
        try:
            HOME = os.environ['HOME']
        except KeyError:
            HOME = os.environ['USERPROFILE']
        if PLATFORM == 'Windows':
            OFFSITE = os.path.join(os.environ['AppData'], 'SBEVSL', 'ProMol')
        elif PLATFORM == 'Darwin':
            OFFSITE = os.path.join(HOME, 'Library', 'Application Support', 'SBEVSL',
                'ProMol')
        else:
            OFFSITE = os.path.join(HOME, '.sbevsl', 'ProMol')

        csvdir = os.path.join(OFFSITE, 'CSV')

        files = os.listdir(csvdir)

        #Pick out the files in the directory that are motiffinder results files
        resultFiles = set()
        pdbs = set()
        setsDone = {}
        setsDone['P'] = set()
        setsDone['J'] = set()
        setsDone['A'] = set()
        setsDone['U'] = set()
        setsDone['All'] = set()
        print "Files in submitCSVs:"
        print files
        for f in files:
            if f.startswith('motiffinder') and f.endswith('.csv'):
                fn = f.split('_')
                pid = fn[2].upper()
                if not pid in setsDone[fn[3]] and not pid in setsDone['All']:
                    resultFiles.add(f)
                    setsDone[fn[3]].add(pid)
                    if pid in setsDone['P'] and pid in setsDone['J'] and pid in setsDone['A'] and pid in setsDone['U']:
                        setsDone['All'].add(pid)
                    pdbs.add(pid)

        pdblst = list(pdbs)
        print "PDB List in submitCSVs:"
        print pdblst
        records = self.binding.csvCheck([self.token, pdblst])#[0]
        print "Received records:"
        print records
        ##
        #cur.execute(
        #    """select id, allrun, jrun, prun, myrun from structures
        #    where id in (%s)""",
        #    pdbstr)
        
        #records = cur.fetchall()
        ##
        existing = None
        if records != None and len(records) > 0:
            existing = {}
            existing['P'] = set()
            existing['A'] = set()
            existing['J'] = set()
            existing['U'] = set()
            existing['All'] = set()
            for rec in records:
                if rec[1]:
                    existing['All'].add(rec[0])
                else:
                    if rec[2]:
                        existing['J'].add(rec[0])
                    if rec[3]:
                        existing['A'].add(rec[0])
                    if rec[4]:
                        existing['P'].add(rec[0])
                    if rec[5]:
                        existing['U'].add(rec[0])


        print "Existing:"
        print existing

        #FIX THIS TO UPDATE STRUCTURES WITH THE NEW ONES BEFORE ENTERING RESULTS
        
        #For each result file
        for csv in resultFiles:
            results = {}
            csvname = csv.split('_')
            print "CSV name:"
            print csvname
            if csvname[2].upper() in existing['All'] or csvname[2].upper() in existing[csvname[3]]:
                continue
            #Open it, read its contents into content, then close it

            p = os.path.abspath(csvdir)
            with open(p + '\\' + csv) as f:
                content = f.readlines()
            #Get the precision factor and version
            pfvLine = content[1].split(': ')
            pf = pfvLine[1][:4]
            v = pfvLine[2]
            #Determine if rmsd's were computed
            rmsdchoice = 0
            if content[7].split(',')[3] != '-1':
                rmsdchoice = 1
            #Determine if the run was against all motif sets
            if content[2].split(" ")[1] == 'All':
                allRun = 1
            else:
                allRun = 0
                
            rmsd = None

            #STOPPED HERE
            #Make this function part of the admin manager and change it so queries are not
            #direct.  Use batchentry to enter values.  Write something to perform the above
            #queries in the begining.
            
            for ln in content[7:]:
                data = ln.split(",")

                if rmsd != None and data[1] != "":
                    results[pdb][motif].append(rmsd)
                
                if data[0] != "":
                    pdb = data[0]
                    results[pdb] = {}

                if data[1] != "":
                    specs = []
                    motif = data[1]
                    results[pdb][motif] = [data[2]]
                    if rmsdchoice is 1:
                        rmsd = [data[3], data[4], data[5]]

                results[pdb][motif].append([data[6], data[7], data[8]])

                for mid in data[9:]:
                    results[pdb][mid] = ['NF']

            print "Submitting results:"
            print results
        
            self.submitEntries(pf, v, rmsdchoice, results, allRun)

    def submitQuery(self, pf, v, motifs, pdbs, rmsdchoice):

        results = self.binding.doQuery([self.token, pf, v, list(motifs),
                                           list(pdbs), rmsdchoice])#[0]
        resDict = {}
        
        if results is "Session not found.":
            tkMessageBox.showerror("No active session found")
        elif results is None or len(results) == 0:
            return resDict;
        elif results[0] is None:
            tkMessageBox.showerror("Query failed", "Query failed.  See console.")
        else:
            if len(results) > 0:
                for i in range(0, len(results), 2):
                    pdb = results[i]
                    resDict[pdb] = {}
                    for j in results[i+1]:
                        mid = j[0]
                        res = j[1]
                        resDict[pdb][mid] = res
            if resDict != None:
                print "Received results."
            else:
                print "You must be logged in to query the database."
            return resDict;

    def submitEntries(self, pf, v, rmsdchoice, entries, allrun):
        
        if self.permissions == "0":
            print "You don't have permissions to submit entries."
            return
        
        if rmsdchoice is 1:
            getRmsd = True
        else:
            getRmsd = False
        entryLst = []
        pdbEntryLst = None
        rmsds = None
        ent = None
        for pdb in entries.keys():
            entryLst.append(pdb)
            pdbEntryLst = []
            for mid in entries[pdb].keys():
                if getRmsd and entries[pdb][mid][0] != 'NF':
                    rmsds = []
                    for num in entries[pdb][mid][-1]:
                        rmsds.append(str(num))
                    ent = entries[pdb][mid][0:-1]
                    ent.append(rmsds)
                    pdbEntryLst.append([mid, ent])
                else:
                    pdbEntryLst.append([mid, entries[pdb][mid]])
            entryLst.append(pdbEntryLst)
        try:
            response = self.binding.makeEntry([self.token, pf, v, rmsdchoice, entryLst, allrun])
            if response is None:
                tkMessageBox.showerror("No active session found")
            else:
                print "Upload successful"
        except Exception, e:
            print "Query failed: ", e
            tkMessageBox.showerror("Upload failed.  See console.")   

    def structureUpdate(self, structures):
        
        if self.permissions == "0":
            print "You don't have permissions to update structures..."
            return
        
        try:
            response = self.binding.makeUpdate([self.token, structures, 0])
            if response is None:
                tkMessageBox.showerror("No active session found")
            else:
                print "Update successful"
        except Exception, e:
            print "Update failed: ", e
            tkMessageBox.showerror("Update failed.  See console.")   

    def fullUpdate(self, structures):
        print "Making full update..."
        
        if self.permissions == "0":
            print "You don't have permissions to trigger an update..."
            return

        
        #Use the DBM to update everything
        try:
            print "Sending update queue..."
            print "token: " + str(self.token)
            print "structures: " + str(structures)
            response = self.binding.makeUpdate([self.token, structures, 1])
            print "Update response received:"
            print response
            if response is None:
                tkMessageBox.showerror("Action failed.", "No active session was found.")
            else:
                print "Full update successful"
        except Exception, e:
            print "Update failed: ", e
            tkMessageBox.showerror("Update failed...", "Update failed.  See console.")

    def exit_logout():
        if self.useDB:
            try:
                response = self.binding.logout([self.token])
                if response is None:
                    print "No active session found"
                else:
                    print "Logged out."
            except Exception, e:
                print "Logout failed: ", e
        if not fp.closed:
            fp.close()

            
