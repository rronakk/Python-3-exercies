combo1 = ['swallow', 'snake', 'parrot']
combo2 = 'abc'


combo_list = []
"""
for pos, value in enumerate(combo):
    n = 0
    if n <= len(value):
        print(len(value))  
        v1 = [x[n] for x in combo]
        n = n + 1
    combo_list.append(v1)
print(v1)
print(len(value))
print(combo_list)
"""

for index, value in enumerate(combo1):
    tup = combo1[index], combo2[index]
    combo_list.append(tup)
print(combo_list)
        
    #print (value[0], value[1], value [2])
    
    