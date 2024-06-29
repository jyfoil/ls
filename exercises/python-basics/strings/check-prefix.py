# Write a function that checks whether a string starts with a specific prefix.


def starts_with(string, prefix):
    count = len(prefix)
    return prefix == string[:count]


def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True