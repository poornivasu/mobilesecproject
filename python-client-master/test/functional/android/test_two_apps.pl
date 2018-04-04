#!/usr/bin/perl -w


my $ret1 = `python weather.py`;
print ("The output of weather app test is: $ret1\n");
sleep (5);

my $ret2 = `python cnn.py`;
print ("The output of cnn app test is: $ret2\n");
sleep (5);
