# to count the occurences of a word in sentence using asyncore
# we can use the codes below.
# the sentence or sentences must be stored inside a story.text and must be in the same folder as this code.

from asyncore import read

def readFile(filename):
    openFile = open("./story.txt", "r")
    readFile = openFile.read()

    # [print new file]
    new = readFile.split()

    # print new
    count = {}
    for i in new:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(readFile("./story.txt"))
    

