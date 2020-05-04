#!/usr/bin/perl

$username = $ARGV[0];

$username =~ tr/a-z/A-Z/;
$username =~ s/\s.*//;

@out = `egrep "^$username" ./userdb.txt 2>&1`;
print("egrep '^$username' ./userdb.txt 2>&1\n");
print("@out\n");
# `egrep "^{}" ./userdb.txt 2>&1`
	  
