# Let's generalize the function from the previous exercise. Implement a function named cite that takes two string arguments: 
# the author of the quote and what they said. It then prints the quote, as shown below.


def cite(author, string):
    print(f'{author} said: "Python is executable pseudocode."')

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

# using format method rather than f strings


def cite(author, string):
    print('{} said: "{}"'.format(author, string))

cite('Bruce Eckel', 'Python is executable pseudocode.')