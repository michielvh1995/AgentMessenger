import ast
import message as Mess

class MessageHandler:
    def __init__(self, own = None):
        self.owner = own
        self.keep = 0

    def Parse(self, message):
        """ Turns a received message into an actual message object """
        dict = ast.literal_eval(message)
        head = ast.literal_eval(dict["head"])
        body = ast.literal_eval(dict["body"])

        return Mess.Message(body['m'], type = head['t'], keepAlive = head['c'], MLen = 1024)

    def SetKeepAlive(self, func):
        self.KeepAliveOne = func

    def SetKeepAliveTwo(self, func):
        self.KeepAliveTwo = func

    def SetOwner(self,owner):
        self.owner = owner

    def HandleMessage(self, message, conn):
        """ Do the logic for handling a message """
        m = self.Parse(message)

        self.keep = int(m.keep)

        print "keep: ", self.keep

        if self.keep == 1:
            self.KeepAliveOne(conn)
            self.keep -= 1

        if self.keep == 2:
            self.KeepAliveTwo(conn)


        return m

        if m.text == "kb":
            s = 0
            for i in range(0, 100000000):
                for j in range(0, 100):
                    s += j


class ParsedMessage:
    def __init__(self, head, body):
        self.Head = head
        self.Body = body

        self.KeepA = head['c']
