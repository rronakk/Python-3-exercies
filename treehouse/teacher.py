# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
"""
def most_classes(teachers):
    max_count = 0
    for key in teachers:
        count = len(teachers[key])
        if count > max_count:
            max_count = count
            great_teacher = key
    return great_teacher
"""     
teachers =   {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']} 





