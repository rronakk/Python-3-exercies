import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("my number is 551-574-8144")
print(phoneNumRegex.search("my number is 551-574-8144").group())
print(re.compile(r'\d\d\d-\d\d\d-\d\d\d\d').search("my number is 551-574-8144").group())


phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search("my number is 551-574-8144")
print(mo1.group(1))
print(mo1.group(2))

area_code, number = mo1.groups()
print("areacode: " + area_code)
print("real number: " + number)

batregex = re.compile(r'bat(man|mobile|copter|bat)')
mo2 = batregex.search('batmobile')
print(mo2.group())

"""
Notes :

? - optional
* - none or more, optional
+ - atleast one , not optional
"""
