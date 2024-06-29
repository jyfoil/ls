# Write a function that counts the number of occurrences of a substring in a string.

def count_substrings(string, occurence):
    return string.count(occurence)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0