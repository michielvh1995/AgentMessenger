import thread
import contract
import message
from agent import Agent

class Broker:
    def __init__(self, cnt):
        self.agents = [Agent(i) for i in range(0,10)]
        self.Contracts = []
        self.ID = "broker"




    def AddContract(self, contract):
        self.Contracts.append(contract)

    def Notify(self, client, message):
        print(message)

    def Run(self):
        """ Run the broker """
        while(True):
            input = raw_input("Message ").split()
            self.Debugger(input)

            if(input[0] == "exit" or input[0] == "e"):
                return 1;


    # Non-final functions
    def Debugger(self, input):
        """ A debug function that checks and handles input """
        if(input[0] == "sh"):
            self.show(input[1])

        if(input[0] == "ac"):        # Add a contract
            if input[1] == "a":
                newC = contract.Contract(self, input[3:])
                msg = message.Message("ac", newC, self.agents[int(input[2])])
                self.agents[int(input[2])].Notify(self, msg)
                self.agents[int(input[2])].Run()
            else:
                newC = Contract(self, input)

            self.Contracts.append(newC)

        if input[0] == "fc":       # Cheat-finish a contract
            if input[1] == "a":
                self.agents[int(input[2])].FinishCtr()
                del self.Contracts[int(input[3])]

    def show(self, what):
        """
            Prints a requested item
        """
        if(what == "agents" or what == "ag"):
            for agent in self.agents:
                print(agent)

        if(what == "ctrs" or what == "c"):
            for contract in self.Contracts:
                print(contract)


b = Broker(10)
b.Run()
