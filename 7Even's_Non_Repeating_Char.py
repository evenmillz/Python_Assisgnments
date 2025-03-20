# Even's Non-Repeated Char

# Ask the user for a string
# .strip removes the extra spaces from the beginning and the end, making sure
# that the text is holding the user's input as a clean string.
text = input("Enter a string to find the first non-repeated character: ").strip()

# Create a dictionary to store character counts to track each character's count
char_count = {}

# .get(char, 0) + 1 adds 1 to the count, starting at 0 if it's not in the
# dictionary yet.
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Time to find the first Non-repeated character
# Looping through a 2nd time, moving in order, so that the first unique
# character is found.
# The break statement stops the loop once the match is found.
# The else: block runs only if no unique character was found.
for char in text:
    if char_count[char] == 1:
        print(f"The first non-repeated character is: {char}")
        break
else:
    print("No unique character found.")
