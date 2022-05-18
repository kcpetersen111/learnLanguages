#!/usr/bin/perl

# When cells divide, their DNA replicates too. Sometimes during this
# process mistakes happen and single pieces of DNA get encoded with
# the incorrect information. If we compare two strands of DNA and
# count the differences between them we can see how many mistakes
# occurred. This is known as the "Hamming Distance".

# We read DNA using the letters C,A,G and T. Two strands might look
# like this:

#     GAGCCTACTAACGGGAT
#     CATCGTAATGACGGCCT
#     ^ ^ ^  ^ ^    ^^

# They have 7 differences, and therefore the Hamming Distance is 7.

# The Hamming Distance is useful for lots of things in science, not
# just biology, so it's a nice phrase to be familiar with :)

# ## Implementation notes

# The Hamming distance is only defined for sequences of equal length,
# so an attempt to calculate it between sequences of different lengths
# should not work.

# This exercise is taken from the go exercism

use strict;
use warnings;

sub hamming {
    my $first = shift;
    my $second = shift;
    my $count = 0;
    my @firstArr = split("",$first);
    my @secondArr = split("",$second);

    for (my $i = 0; $i<@firstArr; $i++) {
        if ($firstArr[$i] ne $secondArr[$i]) {
            $count++;
        }
    }
    return $count;
}

sub main {
    my $f = <>;
    my $s = <>;
    if (length($f) != length($s)){
        print("The strings must be equal\n")
        return;
    }
    my $count = hamming($f,$s);
    print ("$count\n");
}
main()