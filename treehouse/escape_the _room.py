#Requirements :

#Ask the player how many rooms he wants to play the game in, has to be symmetrical - done
# Draw the map of rooms - done
# Give user random location
# place monster in random location
# place a door at random location to escape
# Show user available moves, based on Location
# Keep moving until you find the door
# Show Monster and door location, if user quit
# Show Monster location, if you escape or Door location if monster eats you.

import random 

size = 4

def create_room(size):
    room = []
    xAxis = size
    yAxis = size 
    for x in range(xAxis):
        for y in range(yAxis):
            cell = (x,y)
            room.append(cell)
    return room 


def draw_room(room):
    n =0
    while n < size:
        for i in range(size):
            print("|_", end = '' )
        print()
        n +=1

def get_location(room):
    player = random.choice(room)
    monster = random.choice(room)
    door = random.choice(room)
    
 #   if player == monster == door :
  #      return get_location(room)
    
    return player, monster, door

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == size:
        moves.remove('DOWN')
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == size:
        moves.remove('RIGHT')
    
    return moves

print("Welcome to The Great Escape")
print("You need to avoid monster, and find the door to escape")
room = input("how many cells you want to play in ? Each cell is of 1 sq feet : ")
draw_room(room)
cell = create_room(int(room))
player, monster, door = get_location(cell)
print(player, monster, door)
available_moves = get_moves(player)
print(available_moves)
move = input("Select your move {}".format(available_moves))

def make_move(player):
    if move in available_moves:
        if move == 'LEFT':
            player[1] -=1
        elif move == 'RIGHT':
            player[1] +=1
        elif move == 'DOWN':
            player[0] +=1
        elif move == 'UP':
            player[0] -=1
    else:
        print("You hit a dead wall..Invalid move")
    return player

new_postion = make_move(player)

print(new_postion)
        
        


"""
while True:
    
    move = input("> ")
"""               