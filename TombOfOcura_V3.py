from time import sleep
import sys
import TombOfOcura_Info as info

#Basic Functions
def typeOut(message, sleepTime = 0.03, end="new", color=""):
    for char in message:
        print(char, end="")
        sys.stdout.flush()
        sleep(sleepTime)
    if end == "new":
        print()
    else:
        print(" ", end=" ")

def getInput(question=""):
    if question != "":
        typeOut(question)
    playerInput = input()
    if playerInput in ["exit", "quit"]:
        typeOut("Are you sure you want to quit?")
        playerInput = input()
        while True:
            if playerInput in ["y", "yes", "exit", "quit"]:
                quit()
            else:
                return
    elif playerInput in ["inventory", "backpack", "inv"]:
        inventory()
    else:
        return playerInput

#All Inventory Related Functions
class Inventory():
    """
    Inventory creates an inventory that can show items, equip and unequip items, as well as a few other things

    Functions
    ---------
    __init__() creates empty list (items) when inventory is created

    __str__() returns the list of all items without anything fancy

    show() outputs all items in a nicer looking manor

    addItems() adds items to items list in inventory

    removeItems() removes items from items list in inventory

    itemInfo() outputs data based on the dictionary in Info
    """
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        return str(self.items)
        
    def show(self) -> None:
        if len(self.items) <= 0:
            typeOut("You have no items in your Inventory!")
        else:
            for item in self.items:
                typeOut(f"   {item}")
    
    def addItems(self, items):
        if type(items) == str:
            self.items.append(items)
        else:
            for item in items:
                self.items.append(item)

    def removeItem(self, items):
        if type(items) == str:
            self.items.remove(items)
        else:
            for item in items:
                self.items.remove(item)

    def checkForItem(self, item) -> bool:
        for object in self.items:
            if object == item:
                return True
            else:
                return False

    def itemInfo(self, item):
        description = info.items[item]["Description"]
        type = info.items[item]["Type"]
        if type == "Weapon":
            attack = str(info.items[item]["Attack"]) + " Power"
            hit = str(info.items[item]["Hit"][0]) + "-" + str(info.items[item]["Hit"][1]) + " to Hit"
            typeOut(f"{item}\n   Description: {description}\n   "+
                    f"Attack: {attack}\n   Hit: {hit}")
        elif type == "Armor":
            defense = str(info.items[item]["Defense"]) + " Defense"
            typeOut(f"{item}\n   Description: {description}\n   "+
                    f"Protection: {defense}")
        elif type == "Ring":
            typeOut(f"{item}\n   Description: {description}")

    def save(self):
        info.saveData(self.items)

#All Room related functions
def describeRoom(room):
    typeOut(info.rooms[room]["description"])
    return

def changeDescription(room, newDes):
    info.rooms[room]["description"] = newDes
    return

def typeChoices(room):
    for choice in info.rooms[room]["choices"]:
        typeOut(choice.title())
    return

def addChoice(room, addedChoice):
    info.rooms[room]["choices"].append(addedChoice)
    return

def removeChoice(room, removedChoice):
    try:
        info.rooms[room]["choices"].remove(removedChoice)
    except:
        print("--Unable to remove--")
    return

def checkChoice(room, choiceToCheck) -> bool:
    if choiceToCheck in info.rooms[room]["choices"]:
        return True
    else:
        return False

#Main Running Rooms
def runRoom():

    #Room 1
    if info.roomNum == 1:
        inLoop = True
        while inLoop:
            if input() == "1":
                pass
            else:
                inLoop = False

runRoom()