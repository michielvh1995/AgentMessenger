import socket
import ast
import Queue

import message as Mess

from threading import Thread

# App Ralph Horn over factorio automation
class MessengerPrime:
    def __init__(self, port, IP):
        self.port = port;
        self.IP = IP

        self.setSocket()

    def setSocket(self):
        self.sock = socket.socket()
        self.sock.bind((self.IP, self.port))

class Sender(MessengerPrime):
    def SendMessage(self, ExtIP, ExtPort, Message):
        """
            Unfinished function to send messages to an external

            TODO: Expand this function
        """
        self.sock.connect((ExtIP, ExtPort))

        print "\n\nConnected"
        self.sock.send(str(Message))

        if not Message.keep == '0':
            data = self.sock.recv(1024)
            mess = Mess.Parse(data)

        if not Message.keep == '2':
            self.sock.close()
            self.setSocket()
            print 'closed conn'
        # return data

class Listener(MessengerPrime):
    def __init__(self, port, IP):
        MessengerPrime.__init__(self, port, IP)
        self.messages = Queue.Queue()

    def StartListening(self):
        """ Start the thing itself """
        print "starting thread"
        t = Thread(target = self.listenLoop)   # Thread
        # t.daemon = True
        t.start()

    def listenLoop(self):
        """ Actively listen to messages on the port """
        # Listen to the ports and anything connecting to it
        active = True;
        while(active):
            self.sock.listen(1)
            conn, ip = self.sock.accept()
            print "\nConnection from: ", ip

            # The loop once a connection has been established
            while(True):
                msg = conn.recv(1024)

                mess = Mess.Parse(msg)

                # Add the message to the queue
                self.messages.put((ip, mess), block=True, timeout=None)

                # Determine the keep and the related action
                if not mess.keep:
                    # Keep = 0:
                    #   handle the message and send no reply
                    conn.close()
                    print "Closed connection"
                    break;

                elif mess.keep == 1:
                    # Keep = 1:
                    #   Handle the message and send a confirmation
                    conn.send(str(Mess.Received))
                    conn.close()
                    print "Closed connection"
                    break;

                elif mess.keep == 2:
                    # Keep = 2:
                    #   Handle the message, send a confirmation
                    #   Keep the connection alive
                    conn.send(str(Mess.Receive2))
                    print "Connection kept alive"


                # Shutting down
                if mess.text == "exit":
                    active = False
                    conn.send(str(Mess.Exit))
                    conn.close()
                    print "Shutting down"
                    break

                print mess.text

        print "Exit thread"

class Messenger:
    def __init__(self, homePort, sendPort, IP = '127.0.0.1'):
        self.sender = Sender(sendPort, IP)
        self.listener = Listener(homePort, IP)

    def SendMessage(self, ExtIP, ExtPort, Message):
        self.sender.SendMessage(ExtIP, ExtPort, Message)
        print "sent"

    def StartListening(self):
        self.listener.StartListening()

    def empty(self):
        return self.listener.messages.empty()

    def get_nowait(self):
        return self.listener.messages.get_nowait()
