"""
Add a score method to Game that takes a player argument that'll be either 1 or 2.
 Increase that player's value in self.current_score by 1. 
 You'll need to adjust the index (i.e. player = 1 means self.current_score[0] needs to increase).
 
"""

class Game:
    def __init__(self):
        self.current_score = [0, 0]
        
    def score(self, player):  
        if player == 1:
            self.current_score[0] += 1
        
        else:
            self.current_score[1] += 1
   


