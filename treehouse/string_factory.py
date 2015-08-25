dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]
                                                                                
string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts,string):
    string_list = []
    for item in dicts:
        s1 = string.format(**item)
        string_list.append(s1)
    return string_list

print(string_factory(dicts, string))