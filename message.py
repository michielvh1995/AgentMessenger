class Message:
    def __init__(self, type, message, target):
        self.type = type
        self.mess = message

    def NewContract(contr, target):
        return Message(Message.ctnotif, contr, target)

# Constants:
# Contracts:
ctnotif = "ctnotif"
ctadopt = "ctadopt"
