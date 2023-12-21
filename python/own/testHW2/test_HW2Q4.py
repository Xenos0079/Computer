# (Anagrams) Write a function that checks whether two words are anagrams. 
# Two words are anagrams if they contain the same letters. 
# For example, silent and listen are anagrams. The header of the function is:
# def isAnagram(s1, s2):
# (Hint: Obtain two lists for the two strings. 
# Sort the lists and check if two lists are identical.)
# Write a test program that prompts the user to enter two strings and, if they are anagrams, displays is an anagram; 
# otherwise, it displays is not an anagram.
s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")
s1 = str(s1)
s2 = str(s2)
def isAnagram(s1, s2):
    list1 = list(s1)
    list1.sort()
    # print(list1)
    # print(list1.sort)
    list2 = list(s2)
    # print(list2)
    list2.sort()
    # print(list2)
    if list1 == list2:
        print("is an anagram")
    else:
        print("is not an anagram")

isAnagram(s1, s2)