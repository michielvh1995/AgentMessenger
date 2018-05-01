from threading import Thread

from messenger import Messenger
from messenger import Sender

class Agent:
    def __init__(self, sendPort, homePort):
        self.messenger = Messenger(homePort, sendPort, IP = '127.0.0.1')

    def Start(self):
        self.messenger.StartListening()

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
            if not self.messenger.empty():
                (sender, a) = self.messenger.get_nowait()
                print a

                if a.text == "exit":
                    break

                if a.text == "echo":
                    self.messenger.SendMessage(sender[0], sender[1], "echo")
            # .


a = Agent(5008, 5007)
a.Start()
