shopping_list = []

def show_help():
    print("What do you want to add to your list ?")
    print("Enter DONE when you are done adding, Enter HELP to see this message, Enter SHOW to see the shopping list")

def add_item(item):
    shopping_list.append(item)
    print("You added {} item".format(len(shopping_list)))

def show_list():
    print("Here is your list")
    for item in shopping_list:
        print (item)

show_help()

while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue  
    
    else:
        add_item(new_item)
        continue

show_list()
