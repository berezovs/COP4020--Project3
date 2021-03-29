class State:
    def __init__(self, stateName):
        self.stateName = stateName
        self.transitions = []
        self.isAccept = False
    
    def designateAsAccept(self, isAccept):
        self.isAccept = isAccept

    def getStateName(self):
        return self.stateName
    
    def addTransition(self,symbol, state):
        self.transitions.append([symbol, state])

    def isAccepted(self):
        return self.isAccept

    def getTransitions(self):
        return self.transitions

    def getNextState(self, symbol):
        for transition in self.transitions:
            if(transition[0]==symbol):
                return transition[1]
        return None