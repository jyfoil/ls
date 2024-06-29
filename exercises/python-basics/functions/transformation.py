# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

string = 'Captain Ruby'

new_string = string.replace('Ruby', 'Python')

print(new_string)

# Other approach, slice or split the orignla string and concatenate result

# 'Captain Ruby'[:8] + 'Python'

# 'Captain Ruby'.split(' ')[0] + ' Python'