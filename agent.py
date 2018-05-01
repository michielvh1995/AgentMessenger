from threading import Thread
import Queue

import contract
import message

class Agent:
    def __init__(self, id):
        self.msgQ = Queue.Queue();      # Message queue
        self.con = None;

        self.ID = id                    # id

        t = Thread(target = self.Run)   # Thread
        t.daemon = True
        t.start()

    def Notify(self, sender, msg):
        """ Pass a message to this agent and enqueue it into its message queue """
        self.msgQ.put((msg, sender))

        sender.Notify(self, message.Message(200, "Received", sender))

    def Run(self):
        """ Execute the agent-daemon """
        if not self.msgQ.empty():
            msg, sender = self.msgQ.get()

            self.HandleMessage(msg, sender)
            self.msgQ.task_done()
        else:
            # Do whatever
            pass

    def adoptContract(self, contr):
        """ Accapt a contract as active """
        self.c = contr

    def HandleMessage(self, msg, sender):
        if msg.type == message.ctnotif:
            print(message.ctnotif)

        if msg.type == message.ctadopt:
            self.adoptContract(msg)


        return True
