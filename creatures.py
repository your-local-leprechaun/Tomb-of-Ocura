# This script will hold all monster classes. Each will use Monster as a starting point, as all monsters have
# certain attributes such as name, 

class Monster():
    food = 'bamboo'

    def __init__(self):
        pass

class Spider():
    def __init__(self, name):
        self.name = name
        self.speed = 3
        self.maxHp = 3
        self.hp = 3
        self.hit = (0, 5)