package SWC::Converters::SBEVSL;

use strict;
use SWC::Exception;
use Switch;

    sub new {

        my($class)  = shift;

        my(%params) = @_;

        bless { results => [] }, $class;

    }


sub init {
	my $self = shift;
	my @init = @{ $_[0] };

	push( @{ $self->{results} }, @init );

}


# Accessor method to fetch results
sub get_output {
    my $self = shift;
    return $self->{results};
}


sub convert {
	my $self = shift;
    	my @lines = @{ $_[0] };

   foreach (@lines) { 
	#strip leading and trailing spaces
	$_ =~ s/^\s+//;
	$_ =~ s/\s+$//;

    	#Output converter function mapping with a switch
		my $SBEVSLprefix = ""; #"(VSL|vsl|SBEVSL|sbevsl)";
	
	switch ($_) {

		## Each case will call the output converter's mapped function and push 
		## the return value into the results array.

		#BackBone	
			case /^$SBEVSLprefix\s*backbone\s+.+$/i 	{ push( @{ $self->{results} }, $self->backbone($_) ); }
		#Background
			case /^$SBEVSLprefix\s*background\s+.+$/i 	{ push( @{ $self->{results} }, $self->background($_) ); }
		#Bond
			case /^$SBEVSLprefix\s*bond\s+.+$/i 	{ push( @{ $self->{results} }, $self->bond($_) ); }
		#Cartoon
			case /^$SBEVSLprefix\s*cartoon\s+.+$/i 	{ push( @{ $self->{results} }, $self->cartoon($_) ); }
		#Centre
			case /^$SBEVSLprefix\s*(centre|center)\s+.+$/i 	{ push( @{ $self->{results} }, $self->center($_) ); }
		#Clipboard
			case /^$SBEVSLprefix\s*clipboard\s+.+$/i 	{ push( @{ $self->{results} }, $self->clipboard($_) ); }
		#Colour
			case /^$SBEVSLprefix\s*(colour|color)\s+.+$/i 	{ push( @{ $self->{results} }, $self->color($_) ); }
		#Connect
			case /^$SBEVSLprefix\s*connect\s+.+$/i 	{ push( @{ $self->{results} }, $self->connect($_) ); }
		#CPK
			case /^$SBEVSLprefix\s*CPK\s+.+$/i 	{ push( @{ $self->{results} }, $self->cpk($_) ); }
		#Define
			case /^$SBEVSLprefix\s*define\s+.+$/i 	{ push( @{ $self->{results} }, $self->define($_) ); }
		#Depth
			case /^$SBEVSLprefix\s*depth\s+.+$/i 	{ push( @{ $self->{results} }, $self->depth($_) ); }
		#Dots
			case /^$SBEVSLprefix\s*dots\s+.+$/i 	{ push( @{ $self->{results} }, $self->dots($_) ); }
		#Echo
			case /^$SBEVSLprefix\s*echo\s+.+$/i 	{ push( @{ $self->{results} }, $self->echo($_) ); }
		#English
			case /^$SBEVSLprefix\s*english\s+.+$/i 	{ push( @{ $self->{results} }, $self->english($_) ); }
		#Exit
			case /^$SBEVSLprefix\s*exit\s+.+$/i 	{ push( @{ $self->{results} }, $self->exit($_) ); }
		#French
			case /^$SBEVSLprefix\s*french\s+.+$/i 	{ push( @{ $self->{results} }, $self->french($_) ); }
		#HBonds
			case /^$SBEVSLprefix\s*hbonds\s+.+$/i 	{ push( @{ $self->{results} }, $self->hbonds($_) ); }
		#Help
			case /^$SBEVSLprefix\s*help\s+.+$/i 	{ push( @{ $self->{results} }, $self->help($_) ); }
		#Italian
			case /^$SBEVSLprefix\s*italian\s+.+$/i 	{ push( @{ $self->{results} }, $self->italian($_) ); }
		#Label
			case /^$SBEVSLprefix\s*label\s+.+$/i 	{ push( @{ $self->{results} }, $self->label($_) ); }
		#Load
			case /^$SBEVSLprefix\s*load\s+.+$/i 	{ push( @{ $self->{results} }, $self->load($_) ); }
		#Map
			case /^$SBEVSLprefix\s*map\s+.+$/i 	{ push( @{ $self->{results} }, $self->map($_) ); }
		#Molecule
			case /^$SBEVSLprefix\s*molecule\s+.+$/i 	{ push( @{ $self->{results} }, $self->molecule($_) ); }
		#Monitor
			case /^$SBEVSLprefix\s*monitor\s+.+$/i 	{ push( @{ $self->{results} }, $self->monitor($_) ); }
		#Pause
			case /^$SBEVSLprefix\s*pause\s+.+$/i 	{ push( @{ $self->{results} }, $self->pause($_) ); }
		#Print
			case /^$SBEVSLprefix\s*print\s+.+$/i 	{ push( @{ $self->{results} }, $self->print($_) ); }
		#Quit
			case /^$SBEVSLprefix\s*quit\s+.+$/i 	{ push( @{ $self->{results} }, $self->quit($_) ); }
		#Refresh
			case /^$SBEVSLprefix\s*refresh\s+.+$/i 	{ push( @{ $self->{results} }, $self->refresh($_) ); }
		#Renumber
			case /^$SBEVSLprefix\s*renumber\s+.+$/i 	{ push( @{ $self->{results} }, $self->renumber($_) ); }
		#Reset
			case /^$SBEVSLprefix\s*reset\s+.+$/i 	{ push( @{ $self->{results} }, $self->reset($_) ); }
		#Restrict
			case /^$SBEVSLprefix\s*restrict\s+.+$/i 	{ push( @{ $self->{results} }, $self->restrict($_) ); }
		#Ribbon
			case /^$SBEVSLprefix\s*ribbon\s+.+$/i 	{ push( @{ $self->{results} }, $self->ribbon($_) ); }
		#Rotate case
			case /^$SBEVSLprefix\s*rotate\s+.+$/i	{ push( @{ $self->{results} }, $self->rotate($_) ); }
		#Save
			case /^$SBEVSLprefix\s*save\s+.+$/i 	{ push( @{ $self->{results} }, $self->save($_) ); }
		#Script
			case /^$SBEVSLprefix\s*script\s+.+$/i 	{ push( @{ $self->{results} }, $self->script($_) ); }
		#Select
			case /^$SBEVSLprefix\s*select\s+.+$/i 	{ push( @{ $self->{results} }, $self->select($_) ); }
		#Set
			case /^$SBEVSLprefix\s*set\s+.+$/i 	{ push( @{ $self->{results} }, $self->set($_) ); }
		#Show
			case /^$SBEVSLprefix\s*show\s+.+$/i 	{ push( @{ $self->{results} }, $self->show($_) ); }
		#Slab
			case /^$SBEVSLprefix\s*slab\s+.+$/i 	{ push( @{ $self->{results} }, $self->slab($_) ); }
		#Source
			case /^$SBEVSLprefix\s*source\s+.+$/i 	{ push( @{ $self->{results} }, $self->source($_) ); }
		#Spacefill
			case /^$SBEVSLprefix\s*spacefill\s+.+$/i 	{ push( @{ $self->{results} }, $self->spacefill($_) ); }
		#Spanish
			case /^$SBEVSLprefix\s*spanish\s+.+$/i 	{ push( @{ $self->{results} }, $self->spanish($_) ); }
		#SSBonds
			case /^$SBEVSLprefix\s*ssbonds\s+.+$/i 	{ push( @{ $self->{results} }, $self->ssbonds($_) ); }
		#Star
			case /^$SBEVSLprefix\s*star\s+.+$/i 	{ push( @{ $self->{results} }, $self->star($_) ); }
		#Stereo
			case /^$SBEVSLprefix\s*stereo\s+.+$/i 	{ push( @{ $self->{results} }, $self->stereo($_) ); }
		#Strands
			case /^$SBEVSLprefix\s*strands\s+.+$/i 	{ push( @{ $self->{results} }, $self->strands($_) ); }
		#Structure
			case /^$SBEVSLprefix\s*structure\s+.+$/i 	{ push( @{ $self->{results} }, $self->structure($_) ); }
		#Surface
			case /^$SBEVSLprefix\s*surface\s+.+$/i 	{ push( @{ $self->{results} }, $self->surface($_) ); }
		#Trace
			case /^$SBEVSLprefix\s*trace\s+.+$/i 	{ push( @{ $self->{results} }, $self->trace($_) ); }
		#Translate case
			case /^$SBEVSLprefix\s*translate\s+.+$/i	{ push( @{ $self->{results} }, $self->translate($_) ); }
		#UnBond
			case /^$SBEVSLprefix\s*unbond\s+.+$/i 	{ push( @{ $self->{results} }, $self->unbond($_) ); }
		#Wireframe
			case /^$SBEVSLprefix\s*wireframe\s+.+$/i 	{ push( @{ $self->{results} }, $self->wireframe($_) ); }
		#Write
			case /^$SBEVSLprefix\s*write\s+.+$/i 	{ push( @{ $self->{results} }, $self->write($_) ); }
		#Zap
			case /^$SBEVSLprefix\s*zap\s+.+$/i 	{ push( @{ $self->{results} }, $self->zap($_) ); }
		#Zoom case
			case /^$SBEVSLprefix\s*zoom\s+.+$/i 	{ push( @{ $self->{results} }, $self->zoom($_) ); }

		#error case
			else				{ my $ex = SWC::Exception->new("$_ is not a recognized SBEVSL command!");
					  	  	  $ex->throw();
 							}
    		}
     }

   }

1;