import sys

filename = (sys.argv)[1]


def loadFileContent(fname):
    with open(fname) as file:
        content = file.read()
    content = content.replace("\n", "")
    return content


def tokenizeContent(content):
    return content.split(';')


tokens = loadFileContent(filename)
fsa = tokenizeContent(tokens)
print(fsa)
