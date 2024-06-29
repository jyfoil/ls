# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

# int(input())

# the input from the user is a string
# '10' * 5 = string concatenation
# thus '1010101010'
# change the string input to a int

print(f"The result is {multiply_by_five(number)}!")