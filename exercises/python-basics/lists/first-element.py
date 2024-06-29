
# Write a function that returns the first element of a list provided as an argument. For example:


def first(list):
    if len(list) == 0:
        return

    return list[0]

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))

# Be sure to handle the case where the input list is empty.