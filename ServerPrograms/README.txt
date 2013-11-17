The files in this directory are only needed for setting up and hosting an instance of the ProMol Server.  If you're not 
creating/hosting your own instance, the contents of this directory may be ignored.

1.)  Place all of these .py files in the intended URI/directory on the server.
2.)  Modify the apache config. file and specify ProMolHandler as the handler for requests at that URI
3.)  Put a Motifs and UserMotifs directory somewhere on the server, and make sure they contain files named after every motif
4.)  In all of these files (.py and .sql) look for the text FILL_IN.  Where you find it, you will need to fill in some information specific to your setup.
5.)  Run the .sql script in mysql to create a the database.