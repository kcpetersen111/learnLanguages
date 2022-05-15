use Socket;
use strict;
use warnings;


sub startClient {

    print "What host would you like to connect to? ";
    my $host = <>;

    print "What port would you like to connect to? ";
    my $port = <>;

    socket(SOCKET,PF_INET,SOCK_STREAM,(getprotobyname('tcp'))[2]) or die "Can't create a socket $port\n";

    my $inet = inet_aton($host);

    connect(SOCKET, pack_sockaddr_in($port,$inet)) or die "Can't connect to port $port! \n";

    my $line;
    while ($line = <SOCKET>) {
        print "$line\n";
    }
}

startClient();