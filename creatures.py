# This script will hold all Creature classes. Each will use Creature as a starting point, as all Creatures have
# certain attributes such as name, 
from random import randint
from basicModule import typeOut

global player

class Creature:

    def __init__(self, name, maxHp, speed, armor):
        self.name = name
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.speed = speed
        self.armor = armor

    def __str__(self) -> str:
        return f"{self.name}\n  HP:{self.currentHp}/{self.maxHp}\n  Speed:{self.speed}\n  Armor:{self.armor}"
    
    def doesHit(self, hit) -> bool:
        if hit >= self.armor:
            return True
        else:
            if hit == 0:
                typeOut("Critical Miss! ", end="")
            return False

    def damage(self, hit, damage) -> None:
        if self.doesHit(hit):
            self.currentHp -= damage
            if self.currentHp <= 0:
                typeOut(f"{self.name} has been killed!")
            else:
                typeOut(f"{self.name} takes {damage} damage!")
        else:
            typeOut("The attack misses")
        return

class Player(Creature):
    def __init__(self, name="Jae"):
        maxHp = 5
        speed = 2
        armor = 1
        Creature.__init__(self, name, maxHp, speed, armor)

    def load(self):
        pass

    def getInput(self):
        return input().lower()
    
    def checkTarget(self, targetList, target) -> bool:
        for targets in targetList:
            if targets.name == target:
                return True
        return False
    
    def convertTarget(self, targetList, target) -> Creature:
        for targets in targetList:
            if targets.name == target:
                return targets

    def turn(self, fighters):
        print(f"{self.name.title()}'s Turn!")
        playerInput = self.getInput()
        if "attack" in playerInput:
            target = playerInput.replace("attack ", "")
            if self.checkTarget(fighters, target):
                target = self.convertTarget(fighters, target)

                target.damage(2, 10)
            else:
                typeOut("There is no target by that name!")

        print()

class Spider(Creature):
    """
    This is the class for spiders. They only have up to 4 hit points, but its randomized.
    """
    def __init__(self, name):
        maxHp = randint(1,4)
        speed = 4
        armor = 2
        Creature.__init__(self, name, maxHp, speed, armor)

    def turn(self, fighters):
        for fighter in fighters:
            if isinstance(fighter, Player):
                target = fighter

        attacks = [self.bite(target)]
        attacks[randint(0, len(attacks)-1)]
        input()

    #Possible Attacks to Choose from
    def bite(self, target):
        print(f"{self.name.title()} used bite!")

        hit = randint(0, 1)
        damage = randint(1, 1)

        target.damage(hit, damage)

def createPlayer(name ="Jae"):
    player = Player(name)

player = Player()