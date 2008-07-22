  package SWC::Exception;

  use base qw(Error);
  use overload ('""' => 'stringify');

  sub new
  {
    my $self = shift;
    my $text = "" . shift;
    my @args = ();

    local $Error::Depth = $Error::Depth + 1;
    local $Error::Debug = 1;  # Enables storing of stacktrace

    $self->SUPER::new(-text => $text, @args);
  }

  sub getMessage {
	my $self = shift;
	
	return $self->SUPER::text();
  }

  1;
	