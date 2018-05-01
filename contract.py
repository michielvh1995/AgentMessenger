import message

class Contract:
    def __init__(self, contractor, msg):
        self.type = msg[0]
        self.Ctr = contractor

        self.completed = False

        self.goal = msg[1]

    def __str__(self):
        head = "contract: {"
        head += " contractor: " + str(self.Ctr.ID)
        head += ", type: " + self.type
        head += " | "
        body = "body: {" +self.goal + " } }"
        return head + body

    # This is a temporary function
    def updatePart(self):
        """ Update a part of the contract """
        self.completed = True;

        if(self.completed):
            self.Ctr.Notify(message.Message('c', True, self), "Contract");
