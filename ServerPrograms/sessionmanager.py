#Session Manager
#Connects individual user requests to corresponding Session objects,
#and manages those Sessions
import MySQLdb
from sets import Set
import promolsession as sessions
import uuid
import time
import threading

class SessionManager:

    def __init__(self, host, user, pw, db, key):
        #Connect to database
        self.db = MySQLdb.connect(host, user, pw, db)
        self.c = self.db.cursor()

        self.hostserver = host
        self.database = db

        #Decryption key
        self.aeskey = key

    def getSession(self, token, user, pw):
        try:

            self.c.execute(
                """select account from sessions
                where token = %s and expires > now()""",
                token)
            account = self.c.fetchone()
            if account is None:
                self.c.execute(
                    """delete from sessions where expires < now()""")
                self.db.commit()
                return None
            elif not account[0] == user:
                return None
            else:     
                self.c.execute(
                    """select permissions
                    from credentials
                    where password = AES_ENCRYPT(%s, %s) and user = %s""",
                    (pw, self.aeskey, user))
                perms = self.c.fetchone()
                if perms is None:
                    return None
                else:
                    return sessions.Session(self.hostserver, user, pw, self.database, perms[0])
 
        except Exception, e:
            print "Failed to retreive session: ", e

    def retireSession(self, token):

        self.c.execute(
            """delete from sessions
            where token = %s""",
            token)
        self.db.commit()

        return True

    def requestSession(self, name, pw):
        self.c.execute(
            """select user from credentials
            where password = AES_ENCRYPT(%s, %s) and user = %s""",
            (pw, self.aeskey, name))
        user = self.c.fetchone()
        if user is None:
            return None
        else:
            self.c.execute(
                """select permissions from credentials
                where user = %s""",
                name)
            permissions = self.c.fetchone()[0]
            newToken = str(uuid.uuid4())
            if permissions == "2":
                time = "240:00:00"
                secs = 864000.0
            else:
                time = "24:00:00"
                secs = 86400.0

            self.c.execute(
                """insert into sessions
                values (%s, %s, now(), addtime(now(), %s))""",
                (newToken, name, time))
            self.db.commit()
                
            deadline = threading.Timer(secs, self.retireSession, [newToken])
            deadline.start()
            return [newToken, permissions]
        
        

        
        
