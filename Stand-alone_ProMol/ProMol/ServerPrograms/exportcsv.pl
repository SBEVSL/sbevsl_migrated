#!/usr/bin/perl
use strict;
use warnings;

use Text::CSV;
use DBI;

my $driver = "mysql";
my $database = "ProMol";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "";


my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;

my $search = $ARGV[0];

if(-e "$search.csv"){
	system("rm $search.csv")
}

my $sth = $dbh->prepare("select id from structures where id='$search'");
$sth->execute() or die $DBI::errstr;

if(my $mcheck = $sth->fetchrow_array()){
	my $sth = $dbh->prepare("select pdbid,motif,residues,ec1,ec2,ec3,ec4,pf,total,alpha,alpha_beta
			from results
			left join resultspecs on results.id=resultspecs.id
			left join motifs on results.motif=motifs.id 
			where pdbid='$search'
			into outfile '$search.tmp'
			fields terminated by ','
			lines terminated by '\n'");
	$sth->execute() or die $DBI::errstr;
	$sth->finish();
	open(FILE,">","$search.csv");
	print FILE "pdbid,motif,residues,ec1,ec2,ec3,ec4,total,alpha,alpha_beta\n";
	close FILE;
	system("cat /var/lib/mysql/ProMol/$search.tmp >> $search.csv");
	print "file found\n";
	system("rm /var/lib/mysql/ProMol/$search.tmp");
	exit 1;
}

print "no file found\n";
exit 0;


