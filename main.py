""""
The goal of this project is to create a random password generator that outputs a password of 8 characters
The password will meet the following criteria;
2 Upper case
2 Lower case
2 Special characters
2 digits (0-9)

the selection will then be randomised based on the characters selected
"""

import random


"""
This function is used to shuffle the characters produced below
the parameter will consist of the 8 letters
it will then be split into a list
the list will then be shuffled using the random module
the return type will be a list
"""
def shuffle(temppw):
    templist = list(temppw)
    random.shuffle(templist)
    return templist

"""
The variables are characters based on ascii characters
it uses the random module to get an int in a range, this range depends on which character we wish to recieve
the chosen int will then be used with the chr function which will return a unicode character based on the parameter passed
"""
upperCase1 = chr(random.randrange(65, 90))
upperCase2 = chr(random.randrange(65, 90))

lowerCase1 = chr(random.randrange(97, 122))
lowerCase2 = chr(random.randrange(97, 122))

specialChar1 = chr(random.randrange(33, 47))
specialChar2 = chr(random.randrange(33, 47))

digit1 = chr(random.randrange(48, 57))
digit2 = chr(random.randrange(48, 57))

# adding all the characters together
unShuffledPW = upperCase1 + upperCase2 + lowerCase1 + lowerCase2 + specialChar1 + specialChar2 + digit1 + digit2

print(unShuffledPW)
"""
the aggregated password is passed to the shuffle function, returning a list
joining the characters from the returned list into a string
"""
password = ''.join(shuffle(unShuffledPW))
print(password)

