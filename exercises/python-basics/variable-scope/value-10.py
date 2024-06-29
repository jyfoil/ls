# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# prints [10, 2, 3]
# this is because in the function, it mutates the global variable b
