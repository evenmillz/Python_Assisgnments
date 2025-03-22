# Factorial Finder 
# This script calculates the factorial of a number with proper handling.

# Function that calculates the factorial
def get_factorial(n):
    """
    Calculates the factorial of a given number.
    Keeps it clean, keeps it accurate.
    """
    if n < 0:
        return "Factorials don't work for negative numbers, fam."
    elif n == 0:
        return "The factorial of 0 is always 1."
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return f"The factorial of {n} is {fact}."

# Main loop that handles user input
while True:
    try:
        # Gets input from user and cleans it up
        user_input = input("Enter a whole number to get its factorial (or type 'exit' to bounce): ").strip()

        # Lets the user exit cleanly
        if user_input.lower() == 'exit':
            print("Peace out! Factorial Finder shutting down.")
            break  # Ends the program

        # Converts the input to an integer
        num = int(user_input)

        # Calls the function and displays the result
        print(get_factorial(num))

    except ValueError:
        # Handles invalid input (letters, symbols, decimals)
        print("Nah, that ain't it. Enter a valid whole number.")
