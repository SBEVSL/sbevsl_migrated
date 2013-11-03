#ProMol Daemon
from ZSI import dispatch
import sessionmanager as sm

ADMINUSER = "fill_in"

ADMINPASS = "fill_in"
HOST = "fill_in"
DATABASE = "fill_in"

KEY = "fill_in"

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

def logout(**kwargs):
    args = kwargs.values()[0]
    token = args[0]
    creds = dispatch.GetClientBinding().GetAuth()
    if MANAGER.retireSession(token, creds[1]):
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
        return None
    else:
        return thisSession.query(pf, v, mids, pids, rmsd)

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
#dispatch.AsServer(port=9100, rpc=True)

print "Starting server..."
