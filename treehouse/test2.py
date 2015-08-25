
def sillycase(word):

    first_half = word[:round(len(word)/2)]
    #second_half = word[:]
    second_half = word[round(len(word)/2):]
    return first_half.lower() + second_half.upper()
  
print(sillycase("treehouse"))


