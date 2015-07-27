#!/usr/bin/perl
use strict;
use warnings;


use Text::CSV; #used for csv processing
use File::Basename; #used to grab files from the directory
use DBI;

#initialize db stuffs
my $driver = "mysql";
my $database = "ProMol";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "";

#autocommit is set to zero to automatically rollback if there is an error while running
my $dbh = DBI->connect($dsn, $userid, $password,{AutoCommit=>0}) or die $DBI::errstr;


#initialize csv
my $csv = Text::CSV->new({ sep_char => ',' });

#check for arugment
my $file = $ARGV[0] or die "Need to get CSV\n";

#retrieve pdbid from argument
my $pdbid = $file;
$pdbid =~ s/\_.*//;
$pdbid =~ s/.*\///;
#make sure the pdbid doesn't have any pre stuff

#cut files into 2 seperate files consisting of metadata and results
system("./processCSV",$file);

#the following imports the files consisting of metadata and the results
my $metafile = basename("./".$pdbid."_meta.csv");
my $resultfile = basename("./".$pdbid."_results.csv");

open(my $mdata, '<', $metafile) or die "could not open $metafile \n";
open(my $rdata, '<', $resultfile) or die "could not open $resultfile \n";

my $date;
my $version;
my $PF;
my $motifcount;

while(my $line = <$mdata>){
	chomp $line;
	
	next if($. == 1);
	if($csv->parse($line)){
		my @fields = $csv->fields();
		#retrieves the date from the metadata
		$version = $fields[1];
		$date = $fields[2];
		$PF = $fields[3];
		$motifcount = $fields[5];
	} else {
		warn "Line no parse senioire \n"
	}
}
print "$version, $date, $PF\n";

my $sth = $dbh->prepare("insert into structures
		    (id, rdate, motifcount)
		    values
		    ('$pdbid', '$date', $motifcount)");
$sth->execute() or die $DBI::errstr;
print "structures updated?\n";


while(my $line = <$rdata>){
	chomp $line;

	next if($. == 1);
	if($csv->parse($line)){
		my @fields = $csv->fields();
		
		#the following attempts to check to see if the 
		#motif is already stored within the database
		#if it is not, it checks to see if that motifs set
		#is in the database. Builds the missing information
		#using the data from the csv
		my $sth = $dbh->prepare("select id from motifs 
					where id='$fields[1]'");
		$sth->execute();
		unless(my $mcheck = $sth->fetchrow_array()){

			my $set;
			$set = $fields[2] . " Set";
			my $sth = $dbh->prepare("select id from motifsets
						where id = '$set'");
			$sth->execute();
			if(my $scheck = $sth->fetchrow_array()){
				#work in update with NOW() later
				my $sth = $dbh->prepare("update motifsets 
							set motifcount = motifcount + 1
							where id = '$set'");
				$sth->execute();
			}else{
				my $sth = $dbh->prepare("insert into motifsets
							(id,motifcount,modified)
							values
							('$set',1,NOW())");
				$sth->execute();
			}

			$sth = $dbh->prepare("insert into motifs
					(id,setname,pfam,added,foundin, EC1, EC2, EC3, EC4)
					values
					('$fields[1]','$set','$fields[7]',NOW(),0,'$fields[3]','$fields[4]','$fields[5]','$fields[6]')");
			$sth->execute();

		}
		#fill in the result table
		print "$pdbid\n$fields[1]\n$PF\n$version\n";
		$sth = $dbh->prepare("insert into results
			(pdbid, motif, pf, version,date)
			values
			('$pdbid', '$fields[1]', '$PF', '$version',NOW())");
		$sth->execute() or die $DBI::errstr;
		
		#fill in the result spec table
		my $res = join(' ',@fields[12..(scalar(@fields)-1)]);
		$sth = $dbh->prepare("insert into resultspecs
			(residues, alpha, alpha_beta, total)
			values
			('$res',$fields[11],$fields[10],$fields[9])");
		$sth->execute() or die $DBI::errstr;
		
	}else{
		warn "Line no parse senioire \n"
	}
}

#uploades the structures table to the database
print "done?\n";

#The following commits the database and cleans up the meta and result files
$sth->finish();
$dbh->commit or die $DBI::errstr;
system("rm","./".$pdbid."_meta.csv");
system("rm","./".$pdbid."_results.csv");

