#!/usr/bin/perl


#you will need an sql driver the one I use is sqlite3

#to connect the db to perl
use DBI;
db = DBI->connect("dbi:mysql:database=test;host=localhost", "root", "root");

# to execute a query
$query = "SELECT * FROM test";
$result = $db->do($query);

# to prepare a query

$query = "SELECT * FROM test WHERE id = ?";
$sth = $db->prepare($query);

# to execute a prepared query
$sth->execute(1);

# to get the next row of a query
$row = $sth->fetchrow_array();
# can also have it become a pointer to an array or a hash or a pointer to a hash

# gets an error from the database engine
$error = $sth->errstr();

# when you are done you need to disconnect from the database
$sth->disconnect();