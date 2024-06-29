# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# unboundlocalerror, in python when we try to reference a variable it always assumes local when we have a reassignment
# this is why we get an error, if a = 2 was not present, we would print the global a variable
# use global if we want to print global a and reassign global a

