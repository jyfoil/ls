# Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

print(numbers.items())

for pair in numbers.items():
    print(f'A {pair[0]} number is {pair[1]}.')

# Better solution

for key, value in numbers.items():
    print(f"A {key} number is {value}.")