
package SWC::Director;

use strict;
use SWC::Exception;
use Switch;

my %convertors = (
	"pymol" => "SWC::Converters::PyMol",
	"jmol" => "SWC::Converters::Jmol",
	"rasmol" => "SWC::Converters::RasMol",
	"chime" => "SWC::Converters::Chime"
);


sub new {
    return bless {
	 input_converter => undef,
        output_converter => undef,
	 results => []
    }, shift;
}

# Sets the input converter if the converter module exists and can be loaded, 
# throws exception otherwise
sub set_input_converter {
    	my( $self, $inConverter ) = @_;
	$inConverter = lc($inConverter);

	# If the chosen converter is in the above converter hash list, else throw exception
    	if (exists $convertors{$inConverter}) {

		#if the chosen converter's module can be loaded, else throw excepton
       	if ( eval "require $convertors{$inConverter}" ) {
			my $init;
			#create the converter object
			$self->{input_converter} = $convertors{$inConverter}->new;
		} else {
			my $ex = SWC::Exception->new("$inConverter Convertor could not be loaded!");
			$ex->throw();
		}
	} else {
		my $ex = SWC::Exception->new("$inConverter Convertor doesn't exist!");
		$ex->throw();
	}
}

# Sets the output converter if the converter module exists and can be loaded, 
# throws exception otherwise
sub set_output_converter {
    	my( $self, $outConverter ) = @_;
	$outConverter = lc($outConverter);

	# If the chosen converter is in the above converter hash list, else throw exception
    	if (exists $convertors{$outConverter}) {

		#if the chosen converter's module can be loaded, else throw excepton
       	if ( eval "require $convertors{$outConverter}" ) {

			#create the converter object
			$self->{output_converter} = $convertors{$outConverter}->new;

			#add any initialization commands
			push( @{ $self->{results} }, @{$self->{output_converter}->init} );
		} else {
			my $ex = SWC::Exception->new("$outConverter Converter could not be loaded!");
			$ex->throw();
		}
	} else {
		my $ex = SWC::Exception->new("$outConverter Converter doesn't exist!");
		$ex->throw();
	}
}
 

# Accessor method to fetch results
sub get_output {
    my $self = shift;
    return $self->{results};
}
 

# Starts the conversion
sub convert {
    my $self = shift;
    my @lines = @{ $_[0] };

    #ignore these for now
    #my @newLines = $self->{input_converter}->convert(@lines);
    #$self->{output_converter}->convert(\@lines);

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
			case /^$SBEVSLprefix\s*backbone\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->backbone($_) ); }
		#Background
			case /^$SBEVSLprefix\s*background\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->background($_) ); }
		#Bond
			case /^$SBEVSLprefix\s*bond\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->bond($_) ); }
		#Cartoon
			case /^$SBEVSLprefix\s*cartoon\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->cartoon($_) ); }
		#Centre
			case /^$SBEVSLprefix\s*(centre|center)\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->center($_) ); }
		#Clipboard
			case /^$SBEVSLprefix\s*clipboard\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->clipboard($_) ); }
		#Colour
			case /^$SBEVSLprefix\s*(colour|color)\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->color($_) ); }
		#Connect
			case /^$SBEVSLprefix\s*connect\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->connect($_) ); }
		#CPK
			case /^$SBEVSLprefix\s*CPK\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->cpk($_) ); }
		#Define
			case /^$SBEVSLprefix\s*define\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->define($_) ); }
		#Depth
			case /^$SBEVSLprefix\s*depth\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->depth($_) ); }
		#Dots
			case /^$SBEVSLprefix\s*dots\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->dots($_) ); }
		#Echo
			case /^$SBEVSLprefix\s*echo\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->echo($_) ); }
		#English
			case /^$SBEVSLprefix\s*english\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->english($_) ); }
		#Exit
			case /^$SBEVSLprefix\s*exit\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->exit($_) ); }
		#French
			case /^$SBEVSLprefix\s*french\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->french($_) ); }
		#HBonds
			case /^$SBEVSLprefix\s*hbonds\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->hbonds($_) ); }
		#Help
			case /^$SBEVSLprefix\s*help\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->help($_) ); }
		#Italian
			case /^$SBEVSLprefix\s*italian\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->italian($_) ); }
		#Label
			case /^$SBEVSLprefix\s*label\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->label($_) ); }
		#Load
			case /^$SBEVSLprefix\s*load\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->load($_) ); }
		#Map
			case /^$SBEVSLprefix\s*map\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->map($_) ); }
		#Molecule
			case /^$SBEVSLprefix\s*molecule\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->molecule($_) ); }
		#Monitor
			case /^$SBEVSLprefix\s*monitor\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->monitor($_) ); }
		#Pause
			case /^$SBEVSLprefix\s*pause\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->pause($_) ); }
		#Print
			case /^$SBEVSLprefix\s*print\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->print($_) ); }
		#Quit
			case /^$SBEVSLprefix\s*quit\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->quit($_) ); }
		#Refresh
			case /^$SBEVSLprefix\s*refresh\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->refresh($_) ); }
		#Renumber
			case /^$SBEVSLprefix\s*renumber\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->renumber($_) ); }
		#Reset
			case /^$SBEVSLprefix\s*reset\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->reset($_) ); }
		#Restrict
			case /^$SBEVSLprefix\s*restrict\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->restrict($_) ); }
		#Ribbon
			case /^$SBEVSLprefix\s*ribbon\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->ribbon($_) ); }
		#Rotate case
			case /^$SBEVSLprefix\s*rotate\s+.+$/i	{ push( @{ $self->{results} }, $self->{output_converter}->rotate($_) ); }
		#Save
			case /^$SBEVSLprefix\s*save\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->save($_) ); }
		#Script
			case /^$SBEVSLprefix\s*script\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->script($_) ); }
		#Select
			case /^$SBEVSLprefix\s*select\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->selectt($_) ); }
		#Set
			case /^$SBEVSLprefix\s*set\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->set($_) ); }
		#Show
			case /^$SBEVSLprefix\s*show\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->show($_) ); }
		#Slab
			case /^$SBEVSLprefix\s*slab\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->slab($_) ); }
		#Source
			case /^$SBEVSLprefix\s*source\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->source($_) ); }
		#Spacefill
			case /^$SBEVSLprefix\s*spacefill\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->spacefill($_) ); }
		#Spanish
			case /^$SBEVSLprefix\s*spanish\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->spanish($_) ); }
		#SSBonds
			case /^$SBEVSLprefix\s*ssbonds\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->ssbonds($_) ); }
		#Star
			case /^$SBEVSLprefix\s*star\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->star($_) ); }
		#Stereo
			case /^$SBEVSLprefix\s*stereo\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->stereo($_) ); }
		#Strands
			case /^$SBEVSLprefix\s*strands\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->strands($_) ); }
		#Structure
			case /^$SBEVSLprefix\s*structure\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->structure($_) ); }
		#Surface
			case /^$SBEVSLprefix\s*surface\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->surface($_) ); }
		#Trace
			case /^$SBEVSLprefix\s*trace\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->trace($_) ); }
		#Translate case
			case /^$SBEVSLprefix\s*translate\s+.+$/i	{ push( @{ $self->{results} }, $self->{output_converter}->translate($_) ); }
		#UnBond
			case /^$SBEVSLprefix\s*unbond\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->unbond($_) ); }
		#Wireframe
			case /^$SBEVSLprefix\s*wireframe\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->wireframe($_) ); }
		#Write
			case /^$SBEVSLprefix\s*write\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->write($_) ); }
		#Zap
			case /^$SBEVSLprefix\s*zap\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->zap($_) ); }
		#Zoom case
			case /^$SBEVSLprefix\s*zoom\s+.+$/i 	{ push( @{ $self->{results} }, $self->{output_converter}->zoom($_) ); }

		#error case
			else				{ my $ex = SWC::Exception->new("$_ is not a recognized SBEVSL command!");
					  	  	  $ex->throw();
 							}
    		}
     }


}
 
1;