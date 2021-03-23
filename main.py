import sys

filename = (sys.argv)[1]


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


tokens = loadFileContent(filename)
fsa = tokenizeContent(tokens)
print(fsa)
