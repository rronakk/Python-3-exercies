# problem Statement :

"""Write a function named collatz that has one parameter named number.
if number is even, then collatz() should print number//2 and return this value
if numbe is odd, then collatz() should print and return 3*number + 1"""

"""Write a program that let user type in an integer and that keeps calling
collatz() on that number untill function returns the value 1"""


def collatz(number):
    if number % 2 == 0:
        even_number = number // 2
        print(even_number)
        return even_number
    else:
        odd_number = 3 * number + 1
        print(odd_number)
        return odd_number
try:
    user_input = int(input("Enter any number of your choice : "))
    while user_input != 1:
        value = collatz(user_input)
        user_input = value
        if value == 1:
            break
except ValueError:
    print("Please enter valid integer")
