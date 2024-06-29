# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# prints 2, the global keyword tells the function to assume a refers to the global variable thus it reassigns the global variable a to 2