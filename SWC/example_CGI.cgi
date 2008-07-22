#!/usr/local/bin/perl -w

use lib '/home/amc8507/modules/builder';

use strict;
use CGI qw(:standard :html3);
use SWC::Director;
use Error qw(:try);
use SWC::Exception;

#Set up some variables
my($text, $from, $to);


$text = param("text");
$from = lc(param("from"));
$to = lc(param("to"));

print header;
print start_html("SWC");

try {
    my $converter = SWC::Director->new();
    $converter->set_output_converter("pymol");

    #split textarea into array of lines
    my @lines = split(/\n/, $text);

    $converter->convert(\@lines);

    my @output = @ { $converter->get_output() };

    foreach (@output) { 
	print "$_<br/>";
    }

} catch SWC::Exception with {
    my $ex = shift;
    print("SBEVSL Exception occurred - " . $ex->getMessage() . "\n");
    return 0;
};



print end_html;
