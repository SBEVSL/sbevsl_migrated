#ARGS: the socket number

from socket import *
import sys
import commands
import time
import random
import subprocess

def login(client,ip):
	uname = str(client.recv(1024))
	print uname
	client.send('k')
	pword = str(client.recv(1024))
	print pword
	process = commands.getstatusoutput('perl ./login.pl %s %s'%(uname,pword))[0]
	client.send('k')
	print process
	if process == 0:
		client.send('n')
		print ">invalid user"
	else:
		while 1:
			port = random.randint(1000,2000)
			try:		
				s = socket(AF_INET, SOCK_STREAM)
				s.bind((ip,port))
				s.close()
				client.send('y')
				while(client.recv(1024) != 'k'):
					time.sleep(.5)
				client.send('k')
				client.send(str(port))
				print "starting server on port: "+str(port)
				subprocess.Popen(["python","server.py",ip,str(port),'w'])
				break
			except error, e:
				print "address in use"	
		print ">valid user"

def checkdb(client):
	pdbid = client.recv(1024)
	pdbid = pdbid.split('/')[-1]
	pdbid = pdbid.split('\\')[-1]
	print ">pdbid recieved: "+pdbid
	process = commands.getstatusoutput('perl ./exportcsv.pl %s'%(pdbid))[0]
	client.send('k')
	print process
	if process == 0:
		client.send('n')
		print ">file not found"
	else:
		f = open("/home/cameron/%s.csv"%(pdbid),'rb')
		print ">file opened. ready to send"
		client.send('y')
		while(client.recv(1024) != 'k'):
			time.sleep(.5)
		l = f.read(1024)
		while(l):
			print ">writing file"
			client.send(l)
			l = f.read(1024)
		print ">file sent closing connection"
	#process = commands.getstatusoutput('rm ./%s.csv'%(pdbid))
	client.close()

def uploadinfo(client):
	print "waiting for file name"
	fname = client.recv(1024)
	fname = fname.split('/')[-1]
	fname = fname.split('\\')[-1]
	fname = fname.split('_')[0]
	f = open(fname,'wb')
	
	print ">file name read in"
	client.send('k')
	#Reads in the datafile
	l = client.recv(1024)
	
	i = 0;
	while(len(l) > 0):
		i = i + 1024
		print str(i)+" bytes transferred"	
		f.write(l)
		client.send('k')
		l = client.recv(1024)	
		print len(l)
	print "got file"
	f.close()
	print fname
	commands.getstatusoutput('dos2unix %s'%fname)	
	#client.close()
	#Imports the file into the database
	process = commands.getstatusoutput('perl /home/cameron/import.pl %s'%(fname))
	print fname,' added to the server'
	print "client connection closed"

def main():
	port = int(sys.argv[2])
	host = sys.argv[1]
	job = sys.argv[3]
	buf = 1024
	adr = (host,port)

	#Opens up a socket and binds the server
	s = socket(AF_INET,SOCK_STREAM)
	if job == 'w':
		s.settimeout(3600)
	s.bind(adr)
	s.listen(50)

	#Server runs
	while True:
		print 'waiting for connection'
	
		#Accepts the connection
		if job == 'w':
			try:
				client,cadr = s.accept()
			except timeout:
				print "port %s has expired"%(str(port))
				quit()
		else:
			client,cadr = s.accept()
		print '...connected from:',cadr
		
		op = client.recv(512)
		time.sleep(0.5)
		print "command",op," proposed"
		if(job == 'h'):
			if(op == 'l'):
				print "l"
				client.send('k')
				login(client,host)
		elif(op == 'q'):
			start = time.time()
			print "q"
			client.send('k')
			checkdb(client)				
		elif(op == 'u'):
			start = time.time()
			print "u"
			client.send('k')
			uploadinfo(client)
		else:
			start = time.time()
			print "command",op," not processed"
		
	s.close()

main()
