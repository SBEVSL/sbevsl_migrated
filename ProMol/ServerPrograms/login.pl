#!/usr/bin/perl
use strict;
use warnings;

use DBI;

my $driver = "mysql";
my $database = "ProMol";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "";

my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;

my $uname = $ARGV[0];
my $pass = $ARGV[1];

my $sth = $dbh->prepare("select password from credentials where user = '$uname'");
$sth->execute() or die $DBI::errstr;

if(my $mcheck = $sth->fetchrow_array()){
	if($mcheck eq $pass){
		print "user good\n";
		exit 1;
	}
}
print "user bad\n";
exit 0;

