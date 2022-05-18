#!/usr/bin/perl

use strict;
use warnings;

package Person; #Person will be a class
#new will need a class, name, age, height, and weight
sub new {
    my $class = shift;
    my $self = {
        _name => shift,
        _age => shift,
        _height => shift,
        _weight => shift,
    };
    bless $self, $class;
    return $self;
}

my $Person1 = Person->new("John", "30", "6'2", "160");
my $temp = $Person1->{_name};
print "Name: $temp\n";
print "Age: $Person1->{_age}\n";
print "Height: $Person1->{_height}\n"; 