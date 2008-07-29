## PyMol converter
package SWC::Converters::PyMol;
 
use strict;
use SWC::Exception;

#Inherirance
use SWC::Converters::SBEVSL;
our @ISA = qw(SWC::Converters::SBEVSL);


sub new {

        my($class) = shift;

        my(%params) = @_;

	 #create superclass object
        my($self) = new SWC::Converters::SBEVSL(@_);

	 #bless the object into the subclass
        return(bless($self, $class));
}



# Subroutine to setup any required initalization

sub init {
   my $self = shift;
   my @init = ();

   #selection tracking
   $self->{selections} = {};

   #loaded file tracking
   $self->{file} = { loaded => 0, type => undef, name => undef };


   #create some selections
   $self->{selections}->{"VSLselection"} = "'all'";
   $self->{selections}->{"VSLCenterSelection"} = "'all'";


   $self->{periodictable} =    {'hydrogen'=> 'h','helium'=> 'he','lithium'=> 'li','beryllium'=> 'be','boron'=> 'b','carbon'=> 'c',
                                'nitrogen'=> 'n','oxygen'=> 'o','flourine'=> 'f','neon'=> 'ne','sodium'=> 'na','magnesium'=> 'mg',
                                'aluminum'=> 'al','silicon'=> 'si','phosphorus'=> 'p','sulfur'=> 's','chlorine'=> 'cl','argon'=> 'ar',
                                'potassium'=> 'k','calcium'=> 'ca','scandium'=> 'sc','titanium'=> 'ti','vanadium'=> 'v',
                                'chromium'=> 'cr','manganese'=> 'mn','iron'=> 'fe','cobalt'=> 'co','nickel'=> 'ni','copper'=> 'cu',
                                'zinc'=> 'zn','gallium'=> 'ga','germanium'=> 'ge','arsenic'=> 'as','selenium'=> 'se','bromine'=> 'br',
                                'krypton'=> 'kr','rubidium'=> 'rb','strontium'=> 'sr','yttrium'=> 'y','zirconium'=> 'zr',
                                'niobium'=> 'nb','molybdenum'=> 'mo','technetium'=> 'tc','ruthenium'=> 'ru','rhodium'=> 'rh',
                                'palladium'=> 'pd','silver'=> 'ag','cadmium'=> 'cd','indium'=> 'in','tin'=> 'sn','antimony'=> 'sb',
                                'tellurium'=> 'te','iodine'=> 'i','xenon'=> 'xe','cesium'=> 'cs','barium'=> 'ba','lanthanum'=> 'la',
                                'cerium'=> 'ce','praseodymium'=> 'pr','neodymium'=> 'nd','promethium'=> 'pm','samarium'=> 'sm',
                                'europium'=> 'eu','gadolinium'=> 'gd','terbium'=> 'tb','dysprosium'=> 'dy','holmium'=> 'ho',
                                'erbium'=> 'er','thulium'=> 'tm','ytterbium'=> 'yb','lutetium'=> 'lu','hafnium'=> 'hf',
                                'tantalum'=> 'ta','tungsten'=> 'w','rhenium'=> 're','osmium'=> 'os','iridium'=> 'ir','platinum'=> 'pt',
                                'gold'=> 'au','mercury'=> 'hg','thallium'=> 'tl','lead'=> 'pb','bismuth'=> 'bi','polonium'=> 'po',
                                'astatine'=> 'at','radon'=> 'rn','francium'=> 'fr','radium'=> 'ra','actinium'=> 'ac','thorium'=> 'th',
                                'protactinium'=> 'pa','uranium'=> 'u','neptunium'=> 'np','plutonium'=> 'pu','americium'=> 'am',
                                'curium'=> 'cm','berkelium'=> 'bk','californium'=> 'cf','einsteinium'=> 'es',
                                'fermium'=> 'fm','mendelevium'=> 'md','nobelium'=> 'no','lawrencium'=> 'lr',
                                'rutherfordium'=> 'rf','dubnium'=> 'db','seaborgium'=> 'sg','bohrium'=> 'bh','hassium'=> 'hs',
                                'meitnerium'=> 'mt'};


   $self->{predefinedlists} = {'acidic'=> ' resn asp+glu ',
                               'acyclic'=> ' resn met+ile+val+leu+ala+gly+ser+gln+thr+asn+cys+lys+arg+asp+glu ',
                               'aliphatic'=> ' resn gly+ala+leu+val+ile ',
                               'alpha'=> ' name ca ',
                               'amino'=> ' resn gln+asn+asp+glu+arg+lys+his+thr+cys+tyr+ser+gly+trp+phe+pro+leu+val+ile+met',
                               'aromatic'=> ' resn his+tyr+tr+phe+pro ',
                               'basic'=> ' resn arg+lys+his ',
                               'buried'=> ' resn ala+leu+val+ile+phe+cys+met+trp ',
                               'charged'=> ' resn asp+glu+arg+lys+his ',
                               'cyclic'=> ' resn pro+phe+trp+tyr+his ',
                               'cystine'=> ' (byres (((all) & r. CYS+CYX & n. SG) & bound_to ((all) & r. CYS+CYX & n. SG))) & n. CA+CB+SG',
                               'helix'=> ' ss h ',
                               'hetero'=> ' hetatm ',
                               'hydrophobic'=> ' resn ala+leu+val+ile+met+trp+phe+pro ',
                               'large'=> ' resn glu+arg+lys+his+gln+tyr+leu+ile+met+trp+phe ',
                               'medium'=> ' resn val+thr+asp+asn+pro+cys ',
                               'small'=> ' resn gly+ala+ser ',
                               'neutral'=> ' resn asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro ',
                               'nucleic'=> ' resn a+t+c+g ',
                               'polar'=> ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+ser+gly+tyr ',
                               'protein'=> ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro ',
                               'purine'=> ' resn a+g ',
                               'pyrimidine'=> ' resn c+t ',
                               'selected'=> ' VSLselection ',
                               'sheet'=> ' ss s ',
                               'backbone'=> ' name o1p+o2p+o3p+p+c1*+c2*+c3*+c4*+c5*+o2*+o3*+o4*+o5*+c+o+n+ca ',
                               'sidechain'=> ' resn asp+glu+arg+lys+his+asn+thr+cys+gln+tyr+ser+gly+ala+leu+val+ile+met+trp+phe+pro+a+t+c+g and not name o1p+o2p+o3p+p+c1*+c2*+c3*+c4*+c5*+o2*+o3*+o4*+o5*+c+o+n+ca ',
                               'surface'=> ' resn gly+ser+thr+lys+asp+asn+glu+pro+arg+gln+tyr+his ',
                               'turn'=> ' ss 1 ',
		                 'water'=> ' resn hoh '};

   $self->{aminolist} = {'gly' => 1, 'ala' => 1, 'val' => 1,'leu' => 1, 'ile' => 1, 'met' => 1,'pro' => 1, 'phe' => 1, 'tyr' => 1,
                         'trp' => 1, 'ser' => 1, 'thr' => 1, 'cys' => 1, 'lys' => 1, 'arg' => 1, 'his' => 1, 'asp' => 1, 'glu' => 1,
                         'asn' => 1, 'gln' => 1};


   #add a command to the results
   push ( @init, "cmd.select('VSLCenterSelection', " . $self->{selections}->{"VSLselection"} . + ")" );

   #REQUIRED - send the commands to the superclass to add to the results
   $self->SUPER::init(\@init);

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
 


sub select {
    my $self = shift;
    my $line = shift;
    my $retVal = "select failed";    

    #remove select from line
    $line =~ s/^select//;


 #parentheses
    if( $line =~ m/\s+\((.*)\)\s+(.*)/ ) {
	$retVal = $self->select($1) . " " . $self->select($2);
    }
 #AND
    elsif( $line =~ m/^\s*(.*)\s*and\s+(.*)/ ) {
	if( $1 ne "" && $2 ne "" ) {
		$retVal = $self->select($1) . " AND " . $self->select($2);
	}
	elsif( $1 eq "" ) {
		$retVal = " AND " . $self->select($2);
	}
	elsif ( $2 eq "" ) {
		my $ex = SWC::Exception->new("Malformed select statement near: $line");
		$ex->throw();
	}
    }
 #OR
    elsif( $line =~ m/^\s*(.*)\s+or\s+(.*)/ ) {
	$retVal = $self->select($1) . " OR " . $self->select($2);
    }
 #groupno selector
    elsif( $line =~ m/groupno\s+(.*)\s+([0-9]+)/ ) {
	$retVal = "resi $1 $2";
    }
 #ERROR
    else {
	my $selectEx = SWC::Exception->new("Malformed select statement near: $line");
	$selectEx->throw();
    }

    return $retVal;
}

1;
