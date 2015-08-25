import random
def nchoice(itr, n):
    random_item = []
    i = 0
    while i < n :
        random_item.append(random.choice(itr))
        i = i+1
    return random_item
        
print(nchoice([1,3,4,5], 2))   
    
    