import sys
from DFA import DFA
from GUI import Window

automaton = (sys.argv)[1]
stringFile = (sys.argv)[2]


def loadFileContent(fname):
    with open(fname) as file:
        content = file.read()
    content = content.replace("\n", "")
    return content


def tokenizeContent(content):
    content = content.split(';')
    for element in content:
        element = element.strip()
    return content

def printMessage(isAccepted):
    if(isAccepted):
        print(f"String '{string}' is accepted")
    else:
        print(f"String '{string}' is rejected")



tokens = loadFileContent(automaton)
fsaArray = tokenizeContent(tokens)
string = loadFileContent(stringFile)
fsa = DFA(fsaArray)

if(fsa.errorsExist()):
    fsa.printErrors()
else:
    if(fsa.validateString(string)):
        isAccepted = fsa.isStringAccepted(string)
        printMessage(isAccepted)
    else:
        print("Illegal string: character(s) not in alphabet")
    window = Window(fsa)
    window.showFSA()
    



