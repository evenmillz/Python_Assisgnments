# Largest Element Finder



def find_largest(numbers):
    """
    Takes a list of numbers and returns the largest one.
    Handles empty lists and non-numeric values safely.
    """
    if not numbers:  # Check if the list is empty
        return "The list is empty. Add some numbers, fam."
    
    try:
        max_number = max(numbers)  # Find the max value
        return f"The largest number in the list is: {max_number}"
    
    except TypeError:
        return "Invalid input detected. List must contain only numbers."

# Example usage (User input)
try:
    user_input = input("Enter numbers separated by spaces: ").strip()
    
    # Convert input into a list of numbers
    number_list = [float(i) for i in user_input.split()]
    
    # Call the function and display result
    print(find_largest(number_list))

except ValueError:
    print("Nah, that ain't it. Enter valid numbers only.")
