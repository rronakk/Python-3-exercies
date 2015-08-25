def add_list(num):
    total = 0
    for item in num:
        total = item + total
    return total

amazing = add_list([1, 2, 3])
print(amazing)

