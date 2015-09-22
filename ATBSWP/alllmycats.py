cats = []
while True:
    print("Enter name of cat" + str(len(cats) + 1) + " or Enter nothing to Quit")
    name = input("> ")
    cats.append(name)
    if name == '':
        break
print("Name of my cats are : ")
for name in cats:
    print(" " + name)
