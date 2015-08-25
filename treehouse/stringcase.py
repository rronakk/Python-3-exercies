def stringcases(word):
    upper = word.upper()
    lower = word.lower()
    title = word.title()
    reverse = word[::-1]
    return upper, lower, title, reverse

print (stringcases('hello'))