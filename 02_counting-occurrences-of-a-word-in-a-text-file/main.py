# to count the occurences of a word in sentence.
# we can use the codes below.
# the sentence or sentences must be stored inside a story.text and must be in the same folder as this code.

from fileinput import filename

def read_file_content(filename):
    with open("./story.txt") as file_object:
        filename = file_object.read()
        return filename


def count_words():
    text = read_file_content("./story.txt")
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words())