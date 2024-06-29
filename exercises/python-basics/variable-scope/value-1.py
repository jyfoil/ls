# What will the following code do and why? Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)

# will print 20
# in python variables initialized in a if block can be accessed outside of that block


if False:
    my_new_value = 42

print(my_new_value)

# error variable does not exist from global scope because the if block does not run