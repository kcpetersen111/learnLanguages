use Socket;
# use IO::Socket::INET;
# use Socket qw(inet_ntoa AF_INET IPPROTO_TCP pack_sockaddr_in);
use strict;
use warnings;
use threads;

sub startClient {

    print "What host would you like to connect to? ";
    my $host = <>;

    print "What port would you like to connect to? ";
    my $port = int(<>);
   
    socket(TO_SERVER, PF_INET, SOCK_STREAM, getprotobyname('tcp'));
    # socket($clientSocket, AF_INET, SOCK_STREAM, IPPROTO_TCP) or die "Could not create socket: $!\n";
    # socket(SOCKET,PF_INET,SOCK_STREAM,getprotobyname('tcp')) or die "Can't create a socket $port\n";

    my $inet = inet_aton($host) or die "Cannot resolve hostname $host\n";
    my $paddr = sockaddr_in($port,$inet);

    connect(TO_SERVER,$paddr) or die "Cannot connect to $host:$port\n";
    # connect(SOCKET, pack_sockaddr_in($port,inet_aton($host))) or die "Can't connect to port $port! \n";

    # @initThreads
    # push(@initThreads, 0);
    # push(@initThreads, 1);


    # threads -> create(\&serverOutPut);


    my $line;
    while ($line = <TO_SERVER>) {
        print "$line\n";
        my $input = <>;
        # print "You: $input\n";
        # my $final = chop($input);
        send(TO_SERVER, $input, 1024);
        # print TO_SERVER "$final\n";
    }
}

sub serverInput {
    my $line;
    while ($line = <TO_SERVER>) {
        print "$line\n";
    }
}

sub serverOutPut {
    my $line;
    while ($line = <TO_SERVER>) {
        print "$line\n";
    }

}

startClient();