#!/usr/bin/perl

# taken from the Exercism go programming practice

# Parse and evaluate simple math word problems returning the answer as
# an integer.

use warnings;
use strict;

sub main {
    my $first = "";
    my $operation = "";
    my $second = "";

    my $length = @_;
    my $curr = "";
    for (my $i =0; $i<$length;$i++) {
        # print "test $_[$i]\n";
        # $curr = shift;
        $curr = $_[$i];

        if ($curr =~ /[^\p{L}\d\s@#]/ and $operation eq ""){
            $operation = $curr;
        } elsif ($curr =~ /[\p{N}]/ and $second eq ""){
            if ($first eq ""){
                $first = $curr;
            } elsif ($operation eq "") {
                print "That is not a valid string.\n";
                return;
            } else {

                if ($operation eq "+"){
                    my $temp = int($first) + int($curr);
                    $operation = "";
                    $first = sprintf("%s",$temp);
                } elsif ($operation eq "-"){
                    my $temp = int($first) - int($curr);
                    $operation = "";
                    $first = sprintf("%s",$temp);
                } elsif ($operation eq "*") {
                    my $temp = int($first) * int($curr);
                    $operation = "";
                    $first = sprintf("%s",$temp);
                } else {
                    my $temp = int($first) / int($curr);
                    $operation = "";
                    $first = sprintf("%s",$temp);
                }

            }
        }


    }
    print "The answer is $first\n";
}

my $str = "this is a test 3 / 3 + 2 - 5 + 20";
my @temparr = split(" ", $str);
main(@temparr);