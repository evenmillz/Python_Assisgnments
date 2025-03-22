# Even's Pangram Checker

# STEP 1
# This asks the user for a sentence
# .lower() makes everything lowercase so uppercase and lowercase letters
# are all treated the same
sentence = input("Enter a sentence to check if it's a pangram: ").lower()

# STEP 2
# Define the alphabet, referencing all 26 letters
# set abc.....xyz to make a set of unique letters to compare against
alphabet = set("abcdefghijklmnopqrstuvwxyz")

# STEP 3
# Creates an empty set for tracking found letters, making a place to store the letters found
# and using set() to store letters without duplicates
found_letters = set()

# STEP 4
# This is where the program loops through each letter in the sentence and adds
# it to found_letters
for char in sentence:
    if char in alphabet:
        found_letters.add(char)

# Check if all of the letters were found
if found_letters == alphabet:
    print("The Sentence is a pangram!")
else:
    print("The sentence is NOT a pangram.")
