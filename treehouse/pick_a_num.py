import random


def computer_choice():
    return random.randint(1, 10)


def user_choice():
    num = input("Guess a number between 1 to 10: ")
    return int(num)

def game_rules():
    print("Welcome to Guess a number game")
    print("Guess a number between 1 to 10, if your guess matches the number guessed by computer, You win")
    print("You get only 5 chances to guess")
    
def game():
    count = 1
    game_rules()
    actual_num = computer_choice()
    while True:
        if count <= 5 :
            guess_num = user_choice()                 
            if guess_num == actual_num: 
                print("Bravo! you nailed it in {} attempt" .format(count)) 
                break
            elif guess_num <= actual_num:
                print("Your number is lower than actual number, Please try again.")   
                print("you made {} attempt".format(count))
                count+=1
                continue
            elif guess_num >= actual_num:
                print("your number is greater than actual number, Please try again")
                print("you made {} attempt".format(count))
                count+=1
                continue
        else:
            print("You exceeded your allowed attempt")
            break


game()
            

        
        
    
    

