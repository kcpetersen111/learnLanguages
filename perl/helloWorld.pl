#!/usr/bin/perl
#
use strict;
use warnings;

# single line comment

=begin
multi line comment
=cut

print "Hello, World!\n";

#double quotes vs single quotes
$a = '10';

print "$a is ten\n";

# the here document

my $var = << "EOF";
this is a here document
$a is ten because this is in double quotes
more text
new line
EOF

print "$var\n";


# scalar = $, array = @, hash = %
print "package: ".__PACKAGE__."\n";

