import message as Mess
import messenger

l = messenger.Listener(5010, IP= '127.0.0.1')
s = messenger.Sender(5011, IP= '127.0.0.1')

l.StartListening()
