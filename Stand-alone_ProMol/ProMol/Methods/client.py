#ARGS: host, port, command, filename

import ProMol.promolglobals as glb
from socket import *
import sys
import time
import os
import md5
from Tkinter import *
port = 5000
	
def login(s):
	global port
	m = md5.new()
	s.send(glb.GUI.db_admin['Username'].get())
	glb.full_run = glb.full_run.get()
	while(s.recv(1024) != 'k'):
		time.sleep(.5)
	m.update(str(glb.GUI.db_admin['Password'].get()))
	s.send(m.hexdigest())
	while s.recv(1024) != 'k':
		time.sleep(.5)
	usrval = s.recv(1024)
	if usrval == 'y':
		s.send('k')
		while s.recv(1024) != 'k':
			time.sleep(.5)
		port = int(s.recv(1024))
		glb.using_db = True;
		print "now using the database"
		print "Sessions expire after one hour of inactivity."
	else:
		print "invalid user"
	s.close();

def query(s,fname):
	global port
	s.send(fname)
	print "query " + str(port)
	while(s.recv(1024) != 'k'):
			time.sleep(.5)
	if(s.recv(1024) == 'y'):
		s.send('k')
		f = open(os.path.join(glb.CSV_PATH,fname+".csv"),'wb')
		
		l = s.recv(1024)
		while(l):
				f.write(l)
				l = s.recv(1024)
		f.close()
		print "wrote "+os.path.join(glb.CSV_PATH,fname+".csv")
		s.close()
		return True
	elif(s.recv(1024) == 'n'):
		print "no file found"
		s.close()
		return False

def upload(s,fname):
	s.send(fname)
	#Opens the file being sent
	print "file name recieved, now sending file"
	f = open(str(fname),'rb')

	l = f.read(1024)
	while (l):
		print l
		print 'sending...'
		while(s.recv(1024) != 'k'):
                        time.sleep(0.25)
		s.send(l)
		l = f.read(1024)
	print 'done sending'
	f.close()
	s.close()

def main(command,arg):
	global port
	host = glb.GUI.db_admin['ip'].get()
	adr = (host,port)
	
	#Connects to the server
	s = socket(AF_INET,SOCK_STREAM)
	try:
		s.connect(adr)
		
		print "sending command", command
	
		if(command == 'q'):
			s.send('q')
			while(s.recv(1024) != 'k'):
				time.sleep(.5)
			print "submitting query"
			return query(s,arg)

		if(command == 'u'):
			s.send('u')
			print "sent u: "+arg
			while(s.recv(1024) != 'k'):
				time.sleep(.5)
			upload(s,arg)
		
		if(command == 'l'):
			s.send('l')
			while(s.recv(1024) != 'k'):
				time.sleep(.5)
			print "logging in"
			login(s)
	except Exception, e:
		print "Session has timed out. Please reconnect to the database."
		glb.full_run = IntVar()
		glb.using_db = False
		
	
