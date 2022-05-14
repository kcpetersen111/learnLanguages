#!/usr/bin/perl

use strict;
use warnings;

#will take two parameters and create a random number between the two parameters
sub random_number {
    # my $len = @_;
    # if ($len != 2){
    #     print "Incorect number of arguments";
    #     return -1;
    # }
    my $low = $_[0];
    my $high = $_[1];
    my $random = int(rand($high-$low+1)) + $low;
    return $random;
    }

sub main {
    print "How many players are going to try to guess the closest number?\n";
    my $input = <>;
    my @players = (1..int($input));
    print "What would you like the low number to be? ";
    my $low = <>;
    print "What would you like the high number to be? ";
    my $high = <>;
    my $numToGet = random_number($low,$high);
    my $guess;
    # print "$numToGet";
    while (1 == 1) {
        foreach my $play (@players) {
            print "It is time for player $play to guess\n";
            $guess = <>;
            if ($guess == $numToGet) {
                print "That was correct!!! You win player $play\n";
                return;
            } elsif ($guess > $numToGet){
                print "That was too high\n";
            } elsif ($guess < $numToGet){
                print "That was too low\n";
            }

            # print "$play\n";
        } 
    }
}
sub wrapper {
    while (1 == 1) {
        main();
        print "Would you like to play again?(yes/no) ";
        my $cont = <>;
        # print "$cont";
        if ($cont ne "yes\n") {
            return;
        } 
    }
}

wrapper();