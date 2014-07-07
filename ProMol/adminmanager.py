#import MySQLdb
import atexit
from ZSI.client import AUTH, Binding
from pmg_tk.startup.ProMol import promolglobals as glb
#from pmg_tk.startup.ProMol import databasemanager as dbm
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
            #self.hostName = glb.GUI.db_admin['Server'].get()
            #self.user = glb.GUI.db_admin['Username'].get()
            #self.pw = glb.GUI.db_admin['Password'].get()
            #self.dbName = glb.GUI.db_admin['Database'].get()
            #self.binding = Binding(url=self.hostName)

            #USE FOR REMOTE SERVER TESTING
            self.hostName = 'https://oldmomtong.rit.edu/agrier/ProMolHandler.py'
            self.user = ''
            self.pw = ''
            self.dbName = 'ProMol'
            #fp = open('C:\Program Files (x86)\PyMOL\PyMOL\modules\pmg_tk\startup', 'a')
            #self.binding = Binding(host='129.21.205.207', port=443, ssl=1,
            #                       url=self.hostName, tracefile=fp)
            self.binding = Binding(host='129.21.205.207', port=443, ssl=1,
                                   url=self.hostName)
            self.binding.SetAuth(AUTH.zsibasic, self.user, self.pw)
            #host used to be '129.21.205.204'

            print "Successfully connected."
            #USE FOR LOCAL SERVER TESTING
            #self.hostName = 'http://localhost:9100'
            #self.user = 'root'
            #self.pw = 'Alcanest1'
            #self.dbName = 'promoldb5'
            #self.binding = Binding(url=self.hostName)
            #self.binding.SetAuth(AUTH.zsibasic, self.user, self.pw)
            
            try:
                print "About to try to get a session..."
                sessionInfo = self.binding.login()#[0]
                print "RECEIVED"
                print "sessionInfo :", str(sessionInfo)
                if sessionInfo is None:
                    self.useDB = False
                    self.isDB = False
                    #print "Failed to connect to the database: Invalid credentials."
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
                #fp.close()
                self.useDB = False
                self.isDB = False
                #print "Failed to connect to the database: ", e
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
                    #tkMessageBox.showerror("Success", response)
            except Exception, e:
                print "Logout failed: ", e
            glb.GUI.db_admin['Use Database'].config(text='Connect')
            

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
                    if pid in setsDone['P'] and pid in setsDone['J'] and pid in setsDone['U']:
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
                        existing['P'].add(rec[0])
                    if rec[4]:
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

        #print "Results:"
        #print results
        #return resDict
        
        if results is "Session not found.":
            tkMessageBox.showerror("No active session found")
        elif results is None or len(results) == 0:
            return resDict;
        elif results[0] is None:
            #print "Query failed: ", e
            tkMessageBox.showerror("Query failed", "Query failed.  See console.")
        else:
            #print "result:"
            #print str(results)
            if len(results) > 0:
                for i in range(0, len(results), 2):
                    pdb = results[i]
                    #print "pdb:"
                    #print str(pdb)
                    resDict[pdb] = {}
                    for j in results[i+1]:
                        mid = j[0]
                        #print "mid:"
                        #print str(mid)
                        res = j[1]
                        resDict[pdb][mid] = res
            if resDict != None:
                print "Received results."
                #print str(resDict)
            else:
                print "You must be logged in to query the database."
            return resDict;

    def submitEntries(self, pf, v, rmsdchoice, entries, allrun):
        
        if self.permissions == "0":
            print "You don't have permissions to submit entries."
            return
        
        #tkMessageBox.showerror("Got the RMSD value.", "In submitEntries.")
        #print "entries dictionary:"
        #print str(entries)
        if rmsdchoice is 1:
            getRmsd = True
        else:
            getRmsd = False
        entryLst = []
        pdbEntryLst = None
        rmsds = None
        ent = None
        #tkMessageBox.showerror("Got the RMSD value.", "About to parse entries for export...")
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
            #print "Entry: "
            #print pdbEntryLst
        try:
            #tkMessageBox.showerror("Got the RMSD value.", "Exporting entries...")
            response = self.binding.makeEntry([self.token, pf, v, rmsdchoice, entryLst, allrun])#[0]
            if response is None:
                tkMessageBox.showerror("No active session found")
            else:
                print "Upload successful"
                #tkMessageBox.showerror("Success", "Results uploaded successfully.")
        except Exception, e:
            print "Query failed: ", e
            tkMessageBox.showerror("Upload failed.  See console.")   

    def structureUpdate(self, structures):
        
        if self.permissions == "0":
            print "You don't have permissions to update structures..."
            return
        
        try:
            response = self.binding.makeUpdate([self.token, structures, 0])#[0]
            if response is None:
                tkMessageBox.showerror("No active session found")
            else:
                print "Update successful"
                #tkMessageBox.showerror("Success", "Update successful.")
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
            #if len(structures) is 0:
            #    structures = ["None"]
            response = self.binding.makeUpdate([self.token, structures, 1])#[0]
            print "Update response received:"
            print response
            if response is None:
                tkMessageBox.showerror("Action failed.", "No active session was found.")
            else:
                print "Full update successful"
                #tkMessageBox.showerror("Success", "Update successful.")
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
                    #tkMessageBox.showerror("Success", response)
            except Exception, e:
                print "Logout failed: ", e
        #if not fp.closed:
        #    fp.close()

            
