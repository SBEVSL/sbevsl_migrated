######################################
#-----Automated plugin installer-----#
#              for PyMOL             #
#                                    #
#This program will move plugins for  #
#for PyMOL to their designated paths #
#				     #
#For use only with Python version 3.x#
######################################

import os
import tarfile
import shutil
import gzip

#First thing is to get the specific path to the users pymol

pathExists = 0 #Checker to see if it exists in the users environment
 
print ("Enter the path to your pymol directory:")
print ("Example: /home/bxl15/pymol/")

try:
	pymolPath = input()
except SyntaxError: 
	print ("Syntax Error! Please try again.")
	pymolPath = "" 

#Error checking: Makes sure the string entered is a valid path in the environment
while(pathExists ==  0):
	if(os.path.exists(pymolPath)):
		print ("Path is valid")
		pathExists = 1
	else:
		print ("Path is invalid ,re enter the path to your pymol directory:")
		try:
			pymolPath = input() #The path to the users pymol, if valid.
		except SyntaxError:
			print ("Syntax Error! Please try again.")
		
length = len(pymolPath) #Holds the length of the string pymolPath for further eval.      

if(pymolPath[length-1] != '/'):      #Makes sure the path ends with a '/'
	pymolPath = pymolPath + "/"    	
print ("Path set to: "+ pymolPath)     #Displays Path Variable.

print ("Now we need the path to the plugin you are working with:")
print ("Example: /home/usr/file.type")

pathExists = 0 #Resets path exists so it can be used the same way again.

#Error checking: Makes sure the string entered is enclosed in quotes.
try:
	pluginPath = input()
	pathExists = 1
except SyntaxError:
	print ('Oops!, make sure you use "quotes"')
	pluginPath = ""

#Error ckecking: Makes sure the string entered is a valid path in the environment
while(pathExists == 0):
	#Actual error check
	if(os.path.isfile(tarPath)):
		print ("Path is valid")
		pathExists = 1
	else:
		print ("Path is invalid, please re enter the path to the file")
		
		#If path was invalid, loop until it is valid.
		try:
			pluginPath = input()
			pathExists = 1
		except SyntaxError:
			print ("Oops! remember to use quotes around the path!")

print ("Path to the plugin file is set to: "+pluginPath)
length = len(pluginPath) #length is now the length of pluginPath not pymolPath

#Assigns length the value for the number of characters before the last /
#indicating you are at the actual file name, and not a random spot in the
#path variable
while(pluginPath[length - 1] != '/'):
	length = length - 1

#Sets plug in variable equal to everything after the last /	
pluginFile = pluginPath[length:len(pluginPath)]
print ("The file we are working with is: "+pluginFile)

#Sets a variable for the startup folder of PyMOL
pluginDest = pymolPath + 'modules/pmg_tk/startup/'	

#Checks to see if the file needs to be extracted or just moved.
if('py' in pluginPath):
	print ("You are working with a .py or .pyc file")

	#Copies the file to the startup directory
	print ("Copying file to directory .../startup")
	shutil.copy(pluginPath,pluginDest)

	print ("Your file has been sccessfully moved")
elif('bz2' in pluginPath):
	print("This is a bz2 compressed file")
	
	shutil.copy(pluginPath,pluginDest)
	print ("File copied to "+pluginDest)

	os.chdir(pluginDest)
	print("Directory changed...")

	bz2.decompress(pluginFile)
	print("Extraction complete.")
elif('gz' in pluginPath):
	print ("This is a gzipped tarfile")

	shutil.copy(pluginPath,pluginDest)
	print ("File copied to "+pluginDest)	

	os.chdir(pluginDest)
	print ("Directory changed...")

	tgzFile = tarfile.open(pluginFile, 'r:gz')
	print ("File opened...")

	tgzFile.extractall('.')	
	print("Extraction finished")
elif('tar' in pluginPath):
	print ("You are working with a .tar file")
	
	shutil.copy(pluginPath,pluginDest)
	print("File copied to "+pluginDest)

	os.chdir(pluginDest)
	print("Directory changed...")
	
	tar = tarfile.open(pluginFile)
	tar.extractall()
	tar.close()

	print("Extracting complete.")
else:
	print("Nothing to do")
