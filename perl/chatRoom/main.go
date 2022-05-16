package main
import (
	"fmt"
	"log"
	"net"
	"bufio"
)

type Packet struct {
	Sender Person
	Data string
}
type Person struct {
	Conn net.Conn
	Name string
	Scanner *bufio.Scanner
}

func main() {
	//will need to accept connections from new people 
	toServer := make(chan Packet)
	defer close(toServer)
	fromServer := make(chan Packet)
	defer close(fromServer)

	connections := make([]Person, 0)
	
	go acceptConn(toServer,fromServer, &connections)

	log.Println("The server is now online.")

	for {
		//will need to accept data from confections
		

		message := <- toServer

		// fmt.Println("test")
		//will need to send data to all other people
		log.Printf("%s said: %s",message.Sender.Name, message.Data)
		for _,person := range connections{
			if person.Conn != message.Sender.Conn {
				fmt.Fprintf(person.Conn, "%s says: %s\n",message.Sender.Name, message.Data)
			}
		}

	}	
}

func acceptConn(toServer chan Packet, fromServer chan Packet, connections *[]Person){
	ln, err := net.Listen("tcp",":8888")
	if err != nil {
		log.Printf("Error starting up the server: %v\n",err)
		return
	}

	for {
		conn, err := ln.Accept()
		if err != nil{
			log.Printf("Error when someone tries to join: %v\n",err)
		}

		log.Printf("Some one is joining the room.\n")
		fmt.Fprintf(conn,"What is your name?\n")
		
		scanner := bufio.NewScanner(conn)
		scanner.Scan()
		tmpName := scanner.Text()
		log.Printf("%s has joined the room\n",tmpName)
		fmt.Fprintln(conn, "You are now free to talk.\n")

		p1 := Person{
			Conn: conn,
			Name: tmpName,
			Scanner: scanner,
		}

		*connections = append(*connections, p1)

		go handleConnection(toServer,fromServer,p1)
	}
}

func handleConnection(toServer chan Packet, fromServer chan Packet, p1 Person) {
	for {
		fmt.Fprintln(p1.Conn, "What would you like to say?")

		p1.Scanner.Scan()
		input := p1.Scanner.Text()

		newPacket := Packet{
			Sender: p1,
			Data: input,
		}

	
		toServer <- newPacket

		

		
	}
}