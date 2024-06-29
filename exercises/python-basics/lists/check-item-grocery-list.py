# We have a grocery list. As we check off items on that list, we want to remove them from the list.

# Write code that removes the items from grocery_list, one by one, until it is empty. I
# f you print the elements you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.


# for _ in grocery_list:
#     index = 0
#     print(grocery_list[index])
#     grocery_list.pop(0)


while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

print(grocery_list)