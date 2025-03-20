# Even's Sentence Reversal

# Ask User for a sentence
# .strip() removes extra spaces from the beginning and the end, making
# sure that the sentence holds the input as a clean string.
sentence = input("Enter a sentence to reverse the words: ").strip()

# Validate the Input
# if not sentence: checks if the user entered nothing, and sentenc.split()
# splits the sentence into words, and len(...) < 2 makes sure there's
# at least two words.
if not sentence:
    print("You didn't enter anything! Try again!.")
elif len(sentence.split()) < 2:
    print("Please enter a full sentence with at least two words.")
else:
# This is going to split the sentence into words, reverse them, and then
# join them back together

# Split (turns the sentence into a list of words)
    words = sentence.split()

# Reverse (reverses the list using Python slicing tactics)
reversed_words = words[::-1]

# Join (joins the words back into a clean sentence)
reversed_sentence = " ".join(reversed_words)

# Print (prints out the results of the reversed sentence)
print(f"Reversed Sentence: {reversed_sentence}")
