# Write a function that checks whether a string is empty or not. For example:

def is_empty(string):
    return False if len(string) > 1 else True

# def is_empty(s):
#     return s == ''

# def is_empty(s):
#     return len(s) == 0

# def is_empty(s):
#     return not s

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

