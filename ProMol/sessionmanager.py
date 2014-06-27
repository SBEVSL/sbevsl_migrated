#Session Manager
import MySQLdb
from sets import Set
import promolsession as session
import uuid
import time
import threading

class SessionManager:

    def __init__(self, host, user, pw, db, key):
        #Connect to database
        self.db = MySQLdb.connect(host, user, pw, db)
        self.c = self.db.cursor()

        #To store active session info

        #Dictionary of session tokens => session objects
        self.sessionDict = {}
        #Dictionary of active users => password
        self.userDict = {}

        #Decryption key
        self.aeskey = key

    def getSession(self, token, user, pw):
        #print "In sessionmanager -- getSession"
        #print "token, user, pw:"
        #print str(token)
        #print str(user)
        #print str(pw)
        #print "sessionDict keys:"
        #print str(self.sessionDict.keys())
        #print "userDict:"
        #print str(self.userDict)
        try:
            if token in self.sessionDict.keys() and self.userDict[user] == pw:
                #print "Credentials are valid..."
                thisSession = self.sessionDict[token]
                print "Retreived session..."
                print "Refeshing session..."
                if thisSession.permissions is 0 and thisSession.expiration < time.time():
                    self.retireSession(token, user)
                    print "Attempted to get a stale session.  Session expired."
                    return None
                thisSession.refresh()
                #print "Returning session."
                return thisSession
            else:
                print "getSession returning None..."
                return None
        except Exception, e:
            print "Failed to retreive session: ", e

    def retireSession(self, token, user):
        if token in self.sessionDict.keys():
            del self.sessionDict[token]
            if user != None and user in self.userDict.keys():
                del self.userDict[user]
            return True
        else:
            return False

    def requestSession(self, name, pw, host, db):
        self.c.execute(
            """select AES_DECRYPT(password, %s) from credentials
            where user = %s""",
            (self.aeskey, name))
        password = self.c.fetchone()[0]
        #print "Password: "
        #print password
        if pw != password:
            return None
        else:
            self.c.execute(
                """select permissions from credentials
                where user = %s""",
                name)
            permissions = self.c.fetchone()[0]
            newToken = str(uuid.uuid4())
            self.sessionDict[newToken] = session.Session(newToken, host, name, pw, db,
                                                         permissions)
            self.userDict[name] = pw
            if permissions == "2":
                time = 600000.0
            else:
                time = 60000.0
            deadline = threading.Timer(time, self.retireSession, [newToken, name])
            return [newToken, permissions]
        
        

        
        
