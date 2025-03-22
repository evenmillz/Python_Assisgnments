# def is used to define the new function, which is 
# named 'fibonacci_series'
# (n) is a parameter that the function takes and uses as 
# the maximum number the fibbonacie series will be generated to
def fibonacci_series(n):

    # This initializes the first two fiboncacci numbers, simultaneously 
    # assigning the value 0 to a and 1 to b, where a represents the current
    # number and b represents the next number coming up in the series
    a, b = 0, 1
    
    # This creates an empty list to store the fibonacci series, called
    # named 'fibonacci_list', because you have to have somewhere to store
    # the numbers once they have been generated. 
    fibonacci_list = []

    # This is a while loop that generates the fibonacci numbers
    # and it continues to loop through for however long the condition
    # is true.
    # a <= n: is saying that the loop is going to continue to run for the 
    # duration of 'a' being less than or equal to the 'n'.
    while a <= n:

        # This adds whatever the present of 'a' is to 'n'
        fibonacci_list.append(a)

        # And this updates the fibonacci numbers by sending 'a'
        # to get the value of 'b', and the 'b' to get the value
        # of 'a' + 'b'. This is the math on how fibonacci even goes down.
        a, b = b, a + b

    # This returns the fibonacci list, ending the function and gives the 
    # list back to where the function was called to 
    return fibonacci_list

# Now this right here is the part of the code for the user input. It is going to include
# ensuring the user is entering a positive number, so that there aren't any
# monkey wrenches being thrown into the mix. The 'int()' converts the input into an integer, 
# because it is a string by default. 
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a positive integer.")

# Else statement to determine if the input is legit, and then the 'result + fibonacci_series(n)'
# calls the function using the users input, which is 'n', and then puts the list up into the result.
else: 
    result = fibonacci_series(n)
    print(f"Fibonaccie series up to {n}: {result}")
