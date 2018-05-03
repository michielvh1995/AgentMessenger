import message as Mess
from messenger import Sender

def CloseConn(data):
    data.close()
    print "Connection closed"

port = 5004

n = Sender(port,  IP = "127.0.0.1")
print "Initiated at port", port

while(True):
    m = raw_input("Message? \n")
    keep = 1

    if m[-1] == '2':
        keep = 2

    ms = Mess.Message(m, keepAlive = keep)

    # Send the message and accapt the answer
    data = n.SendMessage("127.0.0.1", 5007, ms)
    mess = Mess.Parse(data)

    print "Message type received:", mess.type

    if(m == "exit"):
        break;
