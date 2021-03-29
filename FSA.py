from State import State


class FSA:
    def __init__(self,fsa):
        
        self.numStates = int(fsa[0])
        self.alphabet = fsa[1].split(',')
        self.transitions = fsa[2].replace("(", "").replace(")", "").split(',')
        self.acceptStates = fsa[3].split(',')
        self.acceptStates = [int(i) for i in self.acceptStates]
        self.states = [State(name) for name in range(0, int(self.numStates))]
        self.setAcceptStates()
        self.buildTransitions()
        self.isStringAccepted("xxxxxyxxxyxxxzxxxa")

    
    def getNumStates(self):
        return self.numStates
    
    def getAlphabet(self):
        return self.alphabet

    def getTransitions(self):
        return self.transitions

    def getAcceptStates(self):
        return self.acceptStates

    def setAcceptStates(self):
        for state in self.states:
            if(state.getStateName() in self.acceptStates):
                state.designateAsAccept(True)


    def buildTransitions(self):
        
        for which in range(0,len(self.transitions)):
            transition = self.transitions[which].split(':')
            stateNum = int(transition[0])
            self.states[stateNum].addTransition(transition[2], self.states[ int(transition[1]) ] )


       

    def isStringAccepted(self, string):
        charArr = list(string)
        currState = self.states[0]

        for ch in charArr:
            currState = currState.getNextState(ch)
            #print(currState.getStateName())
            if currState is None:
                print("String is rejected")
                return

        if(currState.isAccepted()):
            print("String is accepted")
        else:
            print("String is rejected")

        

        

        
    
