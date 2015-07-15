#ARGS: host, port, command, filename

import pmg_tk.startup.ProMol.promolglobals as glb
from socket import *
import sys
import time
import os
import md5

def login(s):
	m = md5.new()
	s.send(glb.GUI.db_admin['Username'].get())
	while(s.recv(1024) != 'k'):
		time.sleep(.5)
	m.update(str(glb.GUI.db_admin['Password'].get()))
	s.send(m.hexdigest())
	while s.recv(1024) != 'k':
		time.sleep(.5)
	if s.recv(1024) == 'y':
		glb.using_db = True;
		print "now using the database"
	else:
		print "invalid user"
	s.close();

def query(s,fname):
        fname = fname.split('\\')[-1]
        print fname
	s.send(fname)
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
	s.send(fname.split('/')[-1])

	while(s.recv(1024) != 'k'):
		time.sleep(.5)
	#Opens the file being sent
	print "file name recieved, now sending file"
	f = open(str(fname),'rb')

	l = f.read(1024)
	while (l):

		print 'sending...'
		s.send(l)
		l = f.read(1024)

	print 'done sending'
	f.close()


def main(command,arg):
	host = glb.GUI.db_admin['ip'].get()
	port = 5000
	adr = (host,port)

	
	#Connects to the server
	s = socket(AF_INET,SOCK_STREAM)
	try:
		s.connect(adr)
	except:
		adr = (host,5001)
		try: 
			s.connect(adr)
		except:
			adr = (host,5002)
			s.connect(adr)
	print "sending command", command
	
	if(command == 'q'):
		s.send('q')
		#work in command for Q
		while(s.recv(1024) != 'k'):
			time.sleep(.5)
		print "submitting query"
		return query(s,arg)

	if(command == 'u'):
		s.send('u')
		while(s.recv(1024) != 'k'):
			time.sleep(.5)
		print "beginning upload"
		upload(s,arg)
		
	if(command == 'l'):
		s.send('l')
		while(s.recv(1024) != 'k'):
			time.sleep(.5)
		print "logging in"
		login(s)
