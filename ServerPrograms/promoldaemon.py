#ProMol Daemon
#This program is dispatched by ProMolHandler to handle all requests.
from ZSI import dispatch
import sessionmanager as sm

#These must be filled in with the location of the MySQL server (likely localhost),
#the database to use on that server, credentials with administrative privilages
#on that database, and a secret key for encrypting passwords.
ADMINUSER = "FILL_IN"
ADMINPASS = "FILL_IN"
HOST = "FILL_IN"
DATABASE = "FILL_IN"
KEY = "FILL_IN"

MANAGER = sm.SessionManager(HOST, ADMINUSER, ADMINPASS, DATABASE, KEY)

def login():
    try:
        creds = dispatch.GetClientBinding().GetAuth()
    except Exception, e:
        print "Failed to get credentials: ", e
    try:
        sessionInfo = MANAGER.requestSession(creds[1], creds[2])
    except Exception, e:
        print "Failed to generate session: ", e
    print "Got sessionInfo"
    if sessionInfo is None:
        return None
    else:
        print "sessionInfo:"
        print str(sessionInfo)
        return sessionInfo

def logout(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    if MANAGER.retireSession(token):
        return "Logout successful"
    else:
        return None

def doQuery(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    pf = args[1]
    v = args[2]
    mids = args[3]
    pids = args[4]
    rmsd = args[5]
    
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None:
        return "Session not found."
    else:
        return thisSession.query(pf, v, mids, pids, rmsd)

#This function is still experimental.
def csvCheck(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    pdbs = args[1]
    
    print "Received structures to query:"
    print pdbs
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None or thisSession.permissions < 2:
        return None
    else:
        print "About to pass structures to session..."
        return thisSession.csvQuery(pdbs)

def makeEntry(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    pf = args[1]
    ver = args[2]
    rmsdOn = args[3]
    entryLst = args[4]
    allRun = args[5]
    
    creds = dispatch.GetClientBinding().GetAuth()
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    if thisSession is None or thisSession.permissions is 0:
        return None
    else:
        return thisSession.entry(pf, ver, rmsdOn, entryLst, allRun)

def makeUpdate(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    structures = args[1]
    full = args[2]
    
    creds = dispatch.GetClientBinding().GetAuth()
    print "In promoldaemon -- makeUpdate"
    thisSession = MANAGER.getSession(token, creds[1], creds[2])
    #return "Got a session..."
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

print "Starting server..."
