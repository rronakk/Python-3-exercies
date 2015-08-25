import random
from treehouse.combat import Combat

COLOR = ['yellow', 'red', 'purple', 'green', 'orange']


class Monster(Combat):
    max_hit_point = 1
    min_hit_point = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.hit_point = random.randint(self.min_hit_point, self.max_hit_point)
        self.color = random.choice(COLOR)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP : {}, XP : {}'.format(self.color.title(),
                                                self.__class__.__name__,
                                                self.hit_point,
                                                self.experience)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_point = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_point = 3
    max_hit_point = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'


class Dragon(Monster):
    min_hit_point = 5
    max_hit_point = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaar'


ronak = Dragon()
# ronak.battlecry()
print(ronak)
print(ronak.color)
print(ronak.battlecry()