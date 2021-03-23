class FSA:
    def __init__(self,fsa):
        self.numStates = int(fsa[0])
        self.alphabet = fsa[1].split(',')
        self.transitions = fsa[2].replace("(", "").replace(")", "").split(',')
        self.acceptStates = fsa[3].split(',')
        self.acceptStates = [int(i) for i in self.acceptStates]
    
    def getNumStates(self):
        return self.numStates
    
    def getAlphabet(self):
        return self.alphabet

    def getTransitions(self):
        return self.transitions

    def getAcceptStates(self):
        return self.acceptStates