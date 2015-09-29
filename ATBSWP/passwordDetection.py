""" Write a program which takes password string from user, and returns if password matches the following requirement
It should contain :
8 characters long
both Upper case and lower case character
at least 1 digit
"""

import re

passwordRegex = re.compile(r'''(
    ^                         # Start anchor
    (?=.*[A-Z])               # Ensure string has 1 uppercase letters.
    (?=.*[0-9])               # Ensure string has one digits.
    (?=.*[a-z])               # Ensure string has three lowercase letters.
    .{8,}                     # Ensure string is of length 8.
    $                         # End anchor.
    )''', re.VERBOSE)


password = input("Please enter your password to check its validity \n: ")

def validatePassword(password):
    match = passwordRegex.search(password)

    if match != None:
        print('Your password is strong, and match all requirement')
    else:
        print('Your password do not satisfy the requirements.')

validatePassword(password)
