# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, 
# then use the resulting error message to determine exactly what is wrong. 
# (You don't have to fix this code.)

# While this error message doesn't include a helpful little up-arrow, 
# the line of code just prior to the error message is the code where the error was raised. 
# In this case, the specific text of the error message suggests that you are trying to 
# concatenate an integer with a string. Diving more deeply into tweet + 5, 
# we can see that tweet is the name of a str object and 5 is an int object. 
# We can't concatenate a str and an int, so the TypeError gets raised.