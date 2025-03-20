# Even's Anagram Checker

# This asks the user for two strings
# The replace removes the spaces and the .lower() makes all of the
# the characters case-sensitive so that everything all matches
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 + input("Enter the second string: ").replace(" ", "").lower()

# Sort and Compare the strings; sorted(str1) sorts the letters in aplpha-
# betical order, and if sorted(str1) == sorted(str2), they have the the
# same letters in any order, then it's an anagram
if sorted(str1) == sortedf(str2):
    print("The two strings are anagrams!")
else:
    print("The two strings are NOT anagrams.")
