#ProMol Daemon
from ZSI import dispatch
import sessionmanager as sm

#ADMINUSER = "agrier"
#For local test
ADMINUSER = "root"
ADMINPASS = 
HOST = "localhost"
#DATABASE = "ProMol"
#For local test
DATABASE = "promoldb5"
KEY = "password"

MANAGER = sm.SessionManager(HOST, ADMINUSER, ADMINPASS, DATABASE, KEY)

def login():
    #print "In promoldaemon -- login()"
    try:
        creds = dispatch.GetClientBinding().GetAuth()
    except Exception, e:
        print "Failed to get credentials: ", e
    #print "creds:"
    #print str(creds)
    try:
        sessionInfo = MANAGER.requestSession(creds[1], creds[2], HOST, DATABASE)
    except Exception, e:
        print "Failed to generate session: ", e
    print "Got sessionInfo"
    if sessionInfo is None:
        return None
    else:
        print "sessionInfo:"
        print str(sessionInfo)
        return sessionInfo

def logout(token):
    creds = dispatch.GetClientBinding().GetAuth()
    if MANAGER.retireSession(token, creds[1]):
        return "Logout successful"
    else:
        return None

def doQuery(token, pf, v, mids, pids, rmsd):
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None:
        return None
    else:
        return thisSession.query(pf, v, mids, pids, rmsd)

def csvCheck(token, pdbs):
    print "Received structures to query:"
    print pdbs
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None or thisSession.permissions < 2:
        return None
    else:
        print "About to pass structures to session..."
        return thisSession.csvQuery(pdbs)

def makeEntry(token, pf, ver, rmsdOn, entryLst, allRun):
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None or thisSession.permissions is 0:
        return None
    else:
        return thisSession.entry(pf, ver, rmsdOn, entryLst, allRun)

def makeUpdate(token, structures, full):
    creds = dispatch.GetClientBinding().GetAuth()
    print "In promoldaemon -- makeUpdate"
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    print "Got a session..."
    try:
        if thisSession is None or thisSession.permissions is 0:
            print "Session is None!"
            return None
        else:
            print "Calling update on thisSession from makeUpdate."
            return thisSession.update(structures, full)
    except Exception, e:
        print "Failed session assessment:"
        print e

#For Local test
dispatch.AsServer(port=9100, rpc=True)

print "Starting server..."
