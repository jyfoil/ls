# Write a for loop that iterates over the elements of the list cities and prints the length of each string. 
# If the element is None, use the continue statement to skip forward to the next iteration without printing anything.

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    print(len(city))

# We use None because it is a singleton (objects that can only be created once by design)
# Therefore any None objecgt is always the same object in memory
