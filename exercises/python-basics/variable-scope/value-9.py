# What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# prints 7, when global a is passed as an argument, the argument copies it to its own local variable
# it increments its own local variable and the global remains unchanged