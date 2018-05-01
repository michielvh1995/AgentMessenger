import socket
import ast
import Queue

import message as Mess

from threading import Thread

# App Ralph Horn over factorio automation

class Messenger:
    def __init__(self, port, owner = None, IP = '127.0.0.1', handler = None):
        self.port = port;
        self.messages = Queue.Queue()
        self.obj = owner
        self.IP = IP;

        # Initiate the port
        self.setSocket()

    def setSocket(self):
        self.sock = socket.socket()
        self.sock.bind((self.IP, self.port))

    def StartListening(self):
        """ Start the thing itself """
        print "starting thread"
        t = Thread(target = self.listenLoop)   # Thread
        t.daemon = True
        t.start()

        t = Thread(target = self.runLoop)   # Thread
        # t.daemon = True
        t.start()

    def runLoop(self):
        """
            Perform actions and handle messages when received.
            If an interesting message pops, open a new connection and reply to it.

            TODO: Move this to the agent class
        """
        while True:
            if not self.messages.empty():
                a = self.messages.get_nowait()
                print a

                if a.text == "exit":
                    break


        return False

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
                self.messages.put(mess, block=True, timeout=None)

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

    def SendMessage(self, ExtIP, ExtPort, Message):
        """
            Unfinished function to send messages to an external

            TODO: Expand this function
        """
        self.sock.connect((ExtIP, ExtPort))

        print "\nConnected"
        self.sock.send(str(Message))

        data = self.sock.recv(1024)
        mess = Mess.Parse(data)

        if mess.keep == '0':
            self.sock.close()
            self.setSocket()

        return data
