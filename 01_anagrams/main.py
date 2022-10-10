# These does not accept input from user

firstString = "hello"
secondString = "check"

def find_anagram(hello, check):
    if sorted(firstString) == sorted(secondString):
        print("True")
    else:
        print("False") 

find_anagram(firstString, secondString) 

# -----------------------------------------------------------------------------------------------------------------------------------=

firstString = "below"
secondString = "elbow"

def find_anagram(below, elbow):
    if sorted(firstString) == sorted(secondString):
        print("True")
    else:
        print("False") 

find_anagram(firstString, secondString) 

