from basicModule import typeOut
from ToO_inventory import Inventory
from creatures import Player, Spider
from colorModule import changeColor


class Fight:
    
    def __init__(self, fighters):
        changeColor("red")
        fighters.sort(key = lambda x:x.speed)
        while True:
            for key, fighter in enumerate(fighters):
                print(key)
                if fighter.currentHp <= 0:
                    fighters.remove(fighter)
                    key -= 1
                else:
                    fighter.turn(fighters)

def testFight():
    Fight([Spider("spider 1"), Spider("spider 2"), Player("jae")])

if __name__ == "__main__":
    testFight()