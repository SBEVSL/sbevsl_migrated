
package SWC::Director;

use strict;
use SWC::Exception;


#hash of implemented converters
my %convertors = (
	"pymol" => "SWC::Converters::PyMol",
	#"jmol" => "SWC::Converters::Jmol",
	#"rasmol" => "SWC::Converters::RasMol",
	#"chime" => "SWC::Converters::Chime"
);

#constructor
sub new {
    return bless {
	 input_converter => undef,
        output_converter => undef
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

			#initialization of converter
			$self->{output_converter}->init;

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
    return $self->{output_converter}->get_output;
}
 

# Starts the conversion
sub convert {
    my $self = shift;
    my $lines = $_[0];

    #ignore input converter for now
    #my @newLines = $self->{input_converter}->convert(@lines);

    $self->{output_converter}->convert($lines);

}
 
1;
