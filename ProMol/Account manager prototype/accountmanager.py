import MySQLdb
from pmg_tk.startup.ProMol import promolglobals as glb
import platform
import os

class accountManager:

	def __init__(self):
		try:
		    #self.db = MySQLdb.connect(glb.ADMIN.hostName, glb.ADMIN.user, glb.ADMIN.pw, glb.ADMIN.dbName)
		    self.db = MySQLdb.connect("localhost","root","Alcanest1","promoldb4")
		except e:
		    print "could not connect to the database"
		    print e
		self.c = self.db.cursor()

		self.user = ""
		self.pw = ""

	def createAccount(self):
		self.user = glb.GUI.db_admin['newUsername'].get()
		self.pw = glb.GUI.db_admin['newPassword'].get()

		try:
		    self.c.execute(
		    	"""insert into credentials (Username,Password) 
		       	values(%s,%s)"""%(self.user,self.pw))
		except e:
		    print "could not put the information into the database"
		    print e
		
		self.db.commit()
		self.c.close()
		self.db.close()		
		
