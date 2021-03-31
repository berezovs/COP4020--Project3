from State import State
from Error import Error


class DFA:
    def __init__(self, fsa):

        self.numStates = int(fsa[0])
        self.alphabet = [e.strip() for e in fsa[1].split(',')]
        self.transitions = fsa[2].replace("(", "").replace(")", "").split(',')
        self.acceptStates = [int(i) for i in (fsa[3].split(','))]
        self.states = [State(name) for name in range(0, int(self.numStates))]
        self.errors = []

        self.setAcceptStates()
        self.buildTransitions()

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
        for which in range(0, len(self.transitions)):
            transition = self.transitions[which].split(':')
            stateNum = int(transition[0])
            if(self.validateTransition(transition)):
                self.states[stateNum].addTransition(
                    transition[2], self.states[int(transition[1])])
            else:
                self.errors.append(Error("Transitions are not valid."))

    def validateTransition(self, transition):
        return transition[2] in self.alphabet

    def errorsExist(self):
        return (len(self.errors) > 0)

    def printErrors(self):
        for error in self.errors:
            print(error.getMessage())

    def isStringAccepted(self, string):
        charArr = list(string)
        currState = self.states[0]

        for ch in charArr:
            currState = currState.getNextState(ch)
            if currState is None:
                return False

        if(currState.isAccepted()):
            return True
        else:
            return False

    def validateString(self, string):
        for char in string:
            if not char in self.alphabet:
                return False
        return True
