"""Ask user to enter shopping list, untill he enter done.
print the total number of items in the list, after each addition.
print all the items in the shopping list.


1. Change it by printing comma between list 
2. take input separate by comma, and print out as comma.

"""

#shopping_list=list()

print("What should we pick up at store Enter each item separated by comma?")
print("Enter DONE , when you are done adding the list")

#while True
new_item= input("> ")

usr_shopping_list= new_item.split(",")
"""   
    if new_item == "DONE":
        break
    
    shopping_list.append(new_item)
    print("You have {} items added".format(len(shopping_list)))
    continue
"""
print("Here is your list")
""" printing regularly 
for items in shopping_list:
   print(items)
"""

user_shopping_list = ",".join(usr_shopping_list)
print(user_shopping_list)

    
    
    