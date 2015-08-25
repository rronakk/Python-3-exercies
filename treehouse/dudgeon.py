import random

ROOMS = [(0.0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]
def get_loc():
    player_loc = random.choice(ROOMS)
    door_loc = random.choice(ROOMS)
    monster_loc = random.choice(ROOMS)
    
    if player_loc == monster_loc == door_loc:
        return get_loc()
    
    return player_loc, door_loc, monster_loc

player, door, monster = get_loc()

if player == door:
    print("you are lucky, and land in right room")
elif player == monster:
    print("You are unlucky, and land in wrong room")
else:
    print("let the game begin")
    print(player)

def get_move(player):
    move = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if player[0] == 0:
        move.remove('UP')
    if player[0] == 2:
        move.remove('DOWN')
    if player[1] == 0:
        move.player('LEFT')
    if player[1] == 1:
        move.player('RIGHT')
        
print("{}".format(move))

    
        
    