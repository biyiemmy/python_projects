# These accept inputs from the user!

firstString = input("Enter the first word: ")
secondString = input("Enter the second word: ")

def find_anagram(below, elbow):
    if sorted(firstString) == sorted(secondString):
        print("True")
    else:
        print("False")


find_anagram(firstString, secondString)
