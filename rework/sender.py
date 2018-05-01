import message as Mess
import messageHandler
from messenger import Messenger

def CloseConn(data):
    data.close()
    print "Connection closed"

port = 5004
mh = messageHandler.MessageHandler()
mh.SetKeepAlive(CloseConn)

n = Messenger(port, IP = "127.0.0.1", handler = mh)
print "Initiated at port", port

while(True):
    #ip = input("IP?")
    #po = input("Port?")
    m = raw_input("Message? \n")
    keep = 1

    if m[-1] == '2':
        keep = 2

    ms = Mess.Message(m, keepAlive = keep)

    # Send the message and accapt the answer
    data = n.SendMessage("127.0.0.1", 5007, ms)
    mess = mh.Parse(data)

    print "Message type received:", mess.type

    if(m == "exit"):
        break;
