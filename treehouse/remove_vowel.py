''' Give a list
remove vowel from each item in the list, untill we get exception
print out the list without vowel, with first alphabet in each word capital
'''
words = ['hello', 'ronak', 'ray', 'jaanu']
vowel = list('aeiou')
output=[]

for item in words:
    name = list(item.lower())
    for vw in vowel:
        while True:
            try:
                name.remove(vw)
            except:
                break
    output.append("".join(name).capitalize())
    
print(output)

            
    
