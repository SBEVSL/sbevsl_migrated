import atexit
import smtplib
from ZSI.client import AUTH, Binding
from pmg_tk.startup.ProMol import promolglobals as glb
mailserver = smtplib.SMTP('smtp.gmai.com',587)

class accountCreator:

	def __init__(self):
		#need to put stuff here
		self.server = None

		self.useDB = False
		self.isDB = False

		self.user = ''
		self.pw = ''
		self.email = ''

	def enterAccount(self):
		self.useDB = not self.useDB
        if self.useDB:

        	self.user = glb.GUI.db_admin['New Username'].get()
        	self.pw = glb.GUI.db_admin[''].get()
        	self.email = 


mailserver.login("email","pass")

msg = "\nmessage"
mailserver.sendmail("you@gmail.com","target@email.com",msg)

#http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email