# combination of both
# the first ask for input
# the second function does not ask for input

first_string = input("Provide the first string: ")
second_string = input("Provide the second string: ") 

if sorted(first_string) == sorted(second_string):
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.") 

# ===========================================================================

def anagram_checker(hello, check):
    if sorted(first_string) == sorted(second_string):
        print("The two strings are anagrams of each other.")
    else:
        print("The two strings are not anagrams of each other.") 

first_string = "hello"
second_string = "check"
anagram_checker(first_string, second_string)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

