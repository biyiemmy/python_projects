# to print out what it is inside the story.text on the console or output.
# we can use the codes below

def read_file_content(filename): 
    f = open(filename, "r")
    data = f.read()
    print(data)

filename = "./story.txt"
read_file_content(filename)


