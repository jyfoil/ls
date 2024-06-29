# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result. How can you fix it?

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# Range starts at 0, need to specify the start if we want the correct outcome, the end of range is exclusive