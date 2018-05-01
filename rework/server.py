import message as Mess
from messenger import Messenger
from messageHandler import MessageHandler

def sendConf(data):
    data.send(str(Mess.Confirm))
    data.close()
    print "Confirmation sent and connection closed"

def sendConfKeep(data):
    repl = Mess.Message("confirm", type = "conf", keepAlive = '2', MLen = 1024)
    repl.item = m.item
    data.send(str(repl))
    print "Confirmation sent and connection kept alive"


hand = MessageHandler()
hand.SetKeepAlive(sendConf)
hand.SetKeepAliveTwo(sendConfKeep)

m = Messenger(5007, IP = '127.0.0.1', handler = hand)
m.StartListening()
