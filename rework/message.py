import ast

class Message:
    def __init__(self, msg, type = 0, keepAlive = '1', MLen = 1024, port = 0):
        # Connection type:
        # exit      = end of sending
        # confirm   = Message received, transmission done
        self.type = type

        # Whether the connection should be kept alive:
        # 0 = not
        # 1 = Give confirmation
        # 2 = keep alive, these are only used for long messages
        self.keep = keepAlive
        self.leng = MLen

        self.text = msg

        # The owner's data
        IP = '127.0.0.1'
        self.receiver = (IP, port)

        # If the message is too long:
        self.count = 0  # the number of messages that will be sent
        self.item = 0   # index of this message in said series

        self.confID = 'asdas'   # The ID of the conversation

        self.header = {
            'cnt': self.count,
            'i': self.item,
            't': type,
            'c': keepAlive,
            'l': MLen,
            'p': port
            }
        self.body = {'m' : msg}


    def __str__(self):
        head = str(self.header)
        body = str(self.body)

        s = {'head' : head, 'body': body}
        return str(s)

def Parse(str):
    """ Parses a message from string to a message """
    dict = ast.literal_eval(str)
    head = ast.literal_eval(dict["head"])
    body = ast.literal_eval(dict["body"])

    return Message(body['m'], type = head['t'], keepAlive = head['c'], MLen = 1024)


Confirm = Message("confirm", type = "conf", keepAlive = '0', MLen = 1024)
Received = Message("received", type = "conf", keepAlive = '0', MLen = 1024)
Receive2 = Message("received", type = "conf", keepAlive = '2', MLen = 1024)

Repeat = Message("repeat", type = "err", keepAlive = '1', MLen = 1024)

Exit = Message("exit", type = "exit", keepAlive = '0', MLen = 1024)
