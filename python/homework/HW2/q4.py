'''
 (Anagrams) Write a function that checks whether two words are anagrams. 
 Two words are anagrams if they contain the same letters. 
 For example, silent and listen are anagrams. The header of the function is:
 def isAnagram(s1, s2):
 (Hint: Obtain two lists for the two strings. 
 Sort the lists and check if two lists are identical.)
 Write a test program that prompts the user to enter two strings and, if they are anagrams, displays is an anagram; 
 otherwise, it displays is not an anagram.
'''

s1 = input("Enter the first word: ") # let the user  to enter the first word
s2 = input("Enter the second word: ") # let the user  to enter the second word
s1 = str(s1) # change its data type
s2 = str(s2) # change its data type
def isAnagram(s1, s2): # define a funcion to process
    list1 = list(s1) # break into a list
    list1.sort()  # sort the list
    list2 = list(s2) # break into a list
    list2.sort()  # sort the list
    if list1 == list2: # judge
        print("is an anagram") # output
    else: # failed to pass
        print("is not an anagram") # output

isAnagram(s1, s2)  # start the program