#!/usr/bin/perl
#
use strict;
use warnings;
use Switch;

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


my @var = ("a".."d");

print "var: @var\n";

my $size = @var;
print "size: $size\n";

push(@var, "e");
push(@var, 2);
print "var: @var\n";
my $pop = pop(@var);
print "pop: $pop\n";
print "var: @var\n";

unshift(@var, "f");
print "var: @var\n";

my $shift = shift(@var);
print "shift: $shift\n";

#slices
my @newarr = @var[1..3];
print "full array: @var\n";
print "slice: @newarr\n";


# splice
splice(@var, 2, 2, "g", "h");  
print "splice: @var\n";

#split

my $string = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z";
print "string: $string\n";
my @split =split('-', $string);
print("split: @split\n");
#join
my $joinString = join('/', @split);
print("join: $joinString\n");

if (defined($joinString)) {
    print("join: $joinString\n");
} else {
    print("join: undef\n");
}

my $splitlen = @split;
if ($splitlen <0){
    print("length of split is less than zero\n");
} elsif ($splitlen == 0) {
    print("length of split is zero\n");
} else {
    print("length of split is more than zero\n");
}

# the unless statement is literally just if with an ! applied
unless (defined($joinString)) {
    print("join: undef\n");
} else {
    print("join: is defined\n");
}


#switch statements are not native to perl and need to be installed and imported with cpan and using
my $switchTest = $split[0];
switch($switchTest) {
    case 'a' { print("first letter is a\n");} 
    case "b" {
        print("first letter is b\n");
    }
    case "c" {
        print("first letter is c\n");
    }
    else {
        print("first letter is not a, b, or c\n");
    }
}

#while loops
my $i = 0;
while ($i < 10) {
    print("i is $i\n");
    $i++;
}

#until loops run until the condition is false
my $j = 0;
until ($j > 10) {
    print("j is $j\n");
    $j++;
}

#for loops same a c syntax
for (my $k = 0; $k <= 10; $k++) {
    print("k is $k\n");
}

#foreach loops
my @array = (0..10);
foreach my $l (@array) {
    print("l is $l\n");
}

#do while loop same as while loop with the do will always run at least once
my $m = 0;
do {
    print("m is $m\n");
    $m++;
} while ($m <= 10);

#operators
#the <=> checks if the first value is less than, equal to, or greater than the second value and will return -1, 0, or 1
#perl supports bitwise comparison operators same as arm assembly
#bitwise operators are: &, |, ^, ~, <<, >>
#logical operators are: and, or, not
#bitwise operators are: &&, ||, !