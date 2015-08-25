teachers =   {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']} 
courses = []
for key in teachers:
    courses.append(teachers[key])

all_courses = sum(courses, [])
print(courses)
print(all_courses)