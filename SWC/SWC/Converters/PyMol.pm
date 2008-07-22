## PyMol converter
package SWC::Converters::PyMol;
 
use strict;
use SWC::Exception;

sub new {
    return bless {
	  selections => {},
	  file => { loaded => 0, type => undef, name => undef }
    }, shift;
}



# Subroutine to setup any required initalization
sub init {
   my $self = shift;
   my @init = ();

   #create some selections
   $self->{selections}->{"VSLselection"} = "'all'";
   $self->{selections}->{"VSLCenterSelection"} = "'all'";

   push ( @init, "cmd.select('VSLCenterSelection', " . $self->{selections}->{"VSLselection"} . + ")" );

   return \@init;
}
 

sub zoom {
    my $self = shift;
    my $line = shift;
    my $val = "";    

    if (m/zoom\s+(off|OFF|false|FALSE)$/) {
	$val = "cmd.zoom('VSLCenterSelection',0)";
    }
    elsif (m/zoom\s+(on|true)$/i) {
       $val = "cmd.zoom('VSLCenterSelection',-25)";
    }
    elsif (m/zoom\s+([0-9]+)$/ ) {
	if ($1 >= 0 && $1 <= 100) {
		$val = "cmd.zoom('VSLCenterSelection',$1)";
       }
    }
	
    return $val;
}
 


sub rotate {
    my $self = shift;
    my $line = shift;
    unless ( m/rotate\s+([xyzXYZ])\s+(-?[0-9]+)$/ ) {
	my $ex = SWC::Exception->new("$line is not a recognized SBEVSL command!");
	$ex->throw();
    }
    my $axis = lc($1);
    my $degrees = $2;
    if( $axis eq 'z' ) {
	$degrees = -1 * $degrees;
    }
    return "cmd.rotate('$axis',$degrees)";
}
 


1;