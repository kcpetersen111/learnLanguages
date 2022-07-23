#!/usr/bin/perl

use strict;
use warnings;


sub fizzbuzz {
    my $n = shift;
    for (my $i = 1; $i<=$n; $i++){
        if($i % 15 == 0){
            print ("FizzBuzz\n");
        } elsif ( $i % 5 == 0){
            print("Buzz\n");
        } elsif ($i % 3 == 0){
            print("Fizz\n");
        } else{
            print($i,"\n");
        }
    }
}

our $input = <>;
fizzbuzz($input)