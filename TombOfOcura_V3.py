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
    room = "room" + str(info.roomNum)
    if question != "":
        typeOut(question)
    playerInput = input().lower()
    if playerInput in ["exit", "quit"]:
        quit()
        return None
    elif playerInput in ["describe room", "show room"]:
        describeRoom(room)
        return None
    elif playerInput in ["check", "analyze", "choices", "actions"]:
        showChoices(room)
        return None
    elif playerInput in ["inventory", "backpack", "inv"]:
        inventory()
        return None
    else:
        return playerInput

def getRoom() -> str:
    """
    Simply this function creates the pointer to the dictionary we need in a lot of these. Call this rather than always
    having to make the string from scratch
    """
    return "room"+str(info.roomNum)

def quit():
    typeOut("\nAre you sure you want to quit? (y/n)\nProgress will not be saved currently")
    playerInput = input().lower()
    if playerInput in ["yes", "y", "exit"]:
        typeOut("Hope you come back soon!")
        exit()
    else:
        return

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
def describeRoom():
    room = getRoom()
    typeOut(info.rooms[room]["description"])
    return

def changeDescription(newDes):
    room = getRoom()
    info.rooms[room]["description"] = newDes
    return

def showChoices():
    room = getRoom()
    for choice in info.rooms[room]["choices"]:
        typeOut(choice.title())
    return

def addChoice(addedChoice):
    room = getRoom()
    info.rooms[room]["choices"].append(addedChoice)
    return

def removeChoice(removedChoice):
    room = getRoom()
    try:
        info.rooms[room]["choices"].remove(removedChoice)
    except:
        print("--Unable to remove--")
    return

def checkChoice(choiceToCheck) -> bool:
    room = getRoom()
    if choiceToCheck in info.rooms[room]["choices"]:
        return True
    else:
        return False

def checkSecret() -> bool:
    room = getRoom()
    try:
        return info.rooms[room]["secret"]
    except:
        return False

#Main Running Rooms
def runRoom():
    room = "room" + str(info.roomNum)
    typeOut(info.rooms[room]["description"])
    typeOut("What would you like to do?")
    while True:
        playerInput = getInput()
        if playerInput != None:
            #Room1
            if room == "room1":
                #Get Key
                if playerInput in ["get key", "grab key"]:
                    typeOut("\nYou grab the key. It seems like a perfect fit for the door.")
                    inventory.addItems("key")
                    changeDescription("You are in a room with a bared door blocking your exit.")
                
                #Open door
                elif playerInput in ["open door", "try door", "unlock door"]:
                    #Open with success
                    if inventory.checkForItem("key"):
                        typeOut("\nYou use the key and open the door. There is a pile of hey to your right, and a hallway to the north.")
                        addChoice("move north")
                        inventory.removeItem("key")
                        changeDescription("You are in a room with an open bared door, there is a pile of hay and a hallway to the north.")
                    #Open without success
                    else:
                        typeOut("\nYou try and open the door but it is locked. The key on the ground looks like it might fit.")

                #Check Hay (secret)
                elif playerInput in ["check hay", "analyze hay", "inspect hay"] and checkChoice("move north") and checkSecret() != True:
                    typeOut("\nYou check the hay")

                #Move North (1-->2)
                elif playerInput in ["move north", "walk north"]:
                    typeOut("\nYou walk to your north to the next room.")
                    info.roomNum = 2
                    runRoom()

            
            #Room2
            if room == "room2":
                pass

                    
        else:
            typeOut("\nWhat would you like to do?")

inventory = Inventory()
runRoom()