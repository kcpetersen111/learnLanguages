#!/usr/bin/perl
use strict;
use warnings;

sub main {
    print " Hi! This program will calculate your caloric balance for the day!
Before we can start, I need some information about you. Be honest! :)\n

What is your gender (f or m)? ";
    my $gender = <STDIN>;
    print "What is your age? ";
    my $age = <STDIN>;
    print "What is your height in inches? ";
    my $height = <STDIN>;
    print "What is your weight in pounds? ";
    my $weight = <STDIN>;

    our $dailyTotal;
    if ($gender eq "f\n"){
        $dailyTotal = 655 + (4.7 * $height) + (4.35 * $weight) - (4.7 * $age);
    } else {
        $dailyTotal = 66 + (12.7 * $height) + (6.23 * $weight) - (6.8 * $age);
    }
    print "Your daily caloric balance is $dailyTotal calories.\n";

    while(1<2){
        print "What would you like to do?\n[f] Record food\n[e] Record exercise\n[q] Quit\n";
        my $choice = <STDIN>;
        my $chomped = chomp($choice);
        if ($choice eq "f"){
            recordFood();
        } elsif ($choice eq "e"){
            recordExercise();
        } elsif ($choice eq "q"){
            print "Goodbye!\n";
            return;
        } else {
            print "Invalid choice\n";
        }
    }
}
sub recordExercise() {
    print "How many calories did you burn? ";
    my $cal = <STDIN>;
    our $dailyTotal = $dailyTotal + $cal;
    print "You can now eat $dailyTotal calories today.\n";
}
sub recordFood(){
    print "How many calories did you eat? ";
    my $calories = <STDIN>;
    our $dailyTotal -= $calories;
    print "You have $dailyTotal calories left.\n";
}

main()