"""Create a program to find email & phone number from clipboard.
and display it to user """

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                      # Area Code
    (\s|\-|\.)?                             # Separator
    (\d{3})                                 # first 3 digit
    (\s|\-|\.)                              # Separator
    (\d{4})                                 # Last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?          # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+                        # username
    @                                       # @symbol
    [a-zA-Z0-9.-]+                          # domain
    (\.[a-zA-Z]{2,4})                       # dot-something‰
    )''', re.VERBOSE)


text = str(pyperclip.paste())
match = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum = 'x' + groups[8]
    match.append(phoneNum)

for groups in emailRegex.findall(text):
    match.append(groups[0])

if len(match) > 0 :
    desiredText = '\n'.join(match)
    pyperclip.copy(desiredText)
    print('copied to clipboard')
    print(desiredText)
else:
    print('No Phone numbers or Email address found')

