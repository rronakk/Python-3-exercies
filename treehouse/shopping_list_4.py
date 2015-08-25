shopping_list_3 = []

def show_help():
    print("\n Separate each item with comma ")
    print("Type DONE when finish adding the list, Type SHOW to see the current list, Type REMOVE to remove item from the list, Type HELP to see this message,")

def show_list():
    count = 1
    for item in shopping_list_3:
        print("\n {} : {}".format(count, item ))
        count+= 1
print("Enter list of item you want to add to shopping cart")
show_help()

def remove_item(idx):
    index = idx -1
    item = shopping_list_3.pop(index)
    print("Remove {}".format(item))


while True:
    new_suff = input("Item : > ")
    if new_suff == "DONE":
        print("\n Here is your list")
        show_list()
        break
    elif new_suff == "SHOW":
        print("\n Here is your list till now")
        show_list()
        continue
    elif new_suff == "HELP":
        show_help()
        continue
    elif new_suff == "REMOVE":
        show_list()
        item_to_remove = input("Enter number to remove : ")
        remove_item(int(item_to_remove))
        continue
    else:
        actual_list = new_suff.split(",")
        index = input("Enter a spot to add a list to a particular position, or Enter to add it at the end of list.")
        if index:
            try:
                spot = int(index) - 1 
                for item in actual_list:
                    shopping_list_3.insert(spot, item.strip())
            except ValueError:
                print("please enter integer")                
        else:
            for item in actual_list:
                shopping_list_3.append(item.strip())
            
            
