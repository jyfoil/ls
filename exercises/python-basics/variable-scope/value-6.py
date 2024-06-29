# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

# prints 1, the initialization of the local a inside the function has no effect on the global variable
# it disappears when the function returns