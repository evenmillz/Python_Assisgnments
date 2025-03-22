# Even's String Sorter

# Get the input from the user to obtain the strings the program can sort
#.split() breaks the input into a list of words
words = input("Enter words separated by spaces: ").split()

# This is where we sort the words
# sorted_words = sorted(words, key=len) sorts the words based on their
# length, and key=len tells Python to use the length of each word to sort
sorted_words = sorted(words, key=len)

# This is going to print the words from shortes to longest
print("Words sorted by length:", sorted_words)
