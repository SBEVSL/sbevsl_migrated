#ARGS: the socket number

from socket import *
import sys
import commands
import time

def login(client):
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
		client.send('y')
		print ">valid user"

def checkdb(client):
	pdbid = client.recv(1024)
	pdbid = pdbid.split('/')[-1]
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
	fname = client.recv(1024)
	fname = fname.split('_')[0]
	f = open(fname,'wb')
	
	print ">file name read in"
	client.send('k')
	#Reads in the datafile
	l = client.recv(1024)
	
	i = 0;
	while(l):
		i = i + 1024
		print ">recieving...%sb transferred"%str(i)	
		f.write(l)
		l = client.recv(1024)
	f.close()	
	
	#Imports the file into the database
	process = commands.getstatusoutput('perl /home/cameron/import.pl %s'%(fname))
	print fname,' added to the server'
	print "client connection closed"
	client.close()

def main():
	port = int(sys.argv[1])
	host = 'FILL.IN.IP.HERE'
	buf = 1024
	adr = (host,port)

	#Opens up a socket and binds the server
	s = socket(AF_INET,SOCK_STREAM)
	s.bind(adr)
	s.listen(50)

	#Server runs
	while True:
		print 'waiting for connection'
	
		#Accepts the connection
		client,cadr = s.accept()
		print '...connected from:',cadr
		
		op = client.recv(512)
		print "command",op," proposed"
		if(op == 'q'):
			print "q"
			client.send('k')
			checkdb(client)				
		elif(op == 'u'):
			print "u"	
			client.send('k')
			uploadinfo(client)
		elif(op == 'l'):
			print "l"
			client.send('k')
			login(client)
		else:
			print "command",op," not processed"
		
	s.close()

main()

