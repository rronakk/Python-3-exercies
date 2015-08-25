from pip._vendor.requests import status_codes

teachers =   {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']} 
desired = []
for key in teachers:
    desire1= []
    stats = len(teachers[key])
    desire1.append(key)
    desire1.append(stats)
    desired.append(desire1)

print(desired)
