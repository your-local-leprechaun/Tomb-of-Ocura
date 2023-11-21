#This script hold all the classes for every single creature in the game. 
#Use it to create instances of the creature you want while fighting or anything else

class Spider():
    def __init__(self, name):
        self.name = name
        self.speed = 3
        self.maxHp = 3
        self.hp = 3
        self.hit = (0, 5)