import Queue

import message

from threading import Thread
from messenger import Messenger


class Agent:
    def __init__(self, sendPort, homePort):
        self.ToSend = Queue.Queue()
        self.messenger = Messenger(homePort, sendPort, IP = '127.0.0.1')

        self.other = sendPort
        self.home = homePort

    def GatherInput(self):
        while True:
            IP = '127.0.0.1'
            port = input("Target IP? ")
            msg = raw_input("Message? ")

            send = message.Message(msg, type = 'test', keepAlive = '1', MLen = 1024, port = self.home)

            self.ToSend.put(((IP, port), send))

    def Start(self):
        self.messenger.StartListening()

        t = Thread(target = self.runLoop)   # Thread
        t.daemon = True
        t.start()

        l = Thread(target = self.GatherInput)
        l.start()

    def runLoop(self):
        """
            Perform actions and handle messages when received.
            If an interesting message pops, open a new connection and reply to it.
        """
        while True:
            if not self.ToSend.empty():
                print(self.ToSend.qsize())
                (target, msg) = self.ToSend.get()

                self.messenger.SendMessage(target[0], target[1], msg)

            if not self.messenger.empty():
                (sender, a) = self.messenger.get()
                print a

                if a.text == "exit":
                    break

                if a.text == "echo":
                    self.messenger.SendMessage(sender[0], sender[1], "echo")

        print "Ended run"
            # .


a = Agent(5008, 5007)
a.Start()
