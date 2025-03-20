# Advanced Vowel Counter
# This function counts vowels in a given phrase (case-insensitive).

def count_vowels(user_phrase):
    """
    Accepts a phrase and returns a dictionary showing
    how many times each vowel appears (A, E, I, O, U).
    Handles both uppercase and lowercase input.
    """
    # Define vowels (handling both uppercase & lowercase)
    vowels = "aeiouAEIOU"
    
    # Initialize dictionary with all vowels set to 0
    vowel_count = {v: 0 for v in "aeiou"}  # Only lowercase keys for simplicity

    # Loop through phrase and count each vowel (case insensitive)
    for char in user_phrase:
        lower_char = char.lower()  # Convert to lowercase for uniform counting
        if lower_char in vowel_count:
            vowel_count[lower_char] += 1  # Increase count

    return vowel_count

# Example usage (User input)
phrase = input("Enter a phrase to analyze vowels: ").strip()
result = count_vowels(phrase)

# Display results
print("\n Vowel Count Breakdown:")
for vowel, count in result.items():
    print(f" {vowel.upper()}: {count}")
