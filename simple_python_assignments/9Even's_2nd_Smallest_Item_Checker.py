# Even's 2nd Smallest item finder

# Alright, once again, we need to get the user input
# This is where the user is asked for numbers, and the .strip()
# is used to remove extra spaces from the beginning and the end.
user_input = input("Enter numbers separated by spaces: ").strip()

# Now this will convert the input into a list of numbers
# using the .spit() too break the input down into individual numbers,
# the [int(num) for num in user_input.split()] to convert each one into
# an integer, and then an error message if the user enters a non-number.
try:
    numbers = [int(num) for num in user_input.split()]
except ValueError:
    print("Invalid input! Please enter only numbers.")
    exit()

# This is to make sure there is at least two numbers
if len(numbers) < 2:
    print("Needs at least two numbers to find the second smallest.")
    exit()

# This is where the list is sorted in ascending order to find the
# second smallest number, and then the result is printed.

# Sort
numbers.sort()

# Locate the 2nd-smallest item
smallest = numbers[0]
second_smallest = None

for num in numbers:
    if num > smallest:
        second_smallest = num
        break

# Print the result
if second_smallest is not None:
    print(f"The second-smallest number is: {second_smallest}")
else:
    print("All numbers are the same, no second-smallest exists.")
    

