def format_string(string, formatter=None):
    '''format a string using a formatter object, which is expected to have
    a format() method that accepts a string'''
    class DefaultFormatter:
        '''format a string in title case'''
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

hello_string = "hello world , I am coming here"

print("input : " + hello_string)
print("output : " + format_string(hello_string))
