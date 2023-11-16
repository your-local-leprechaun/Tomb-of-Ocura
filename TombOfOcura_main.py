from time import sleep
import sys
import TombOfOcura_Info as info
import TombOfOcura_inv as inv
from colorModule import changeColor

#Basic Functions
def typeOut(message, sleepTime = 0.0, end="new"):
    for char in message:
        print(char, end="")
        sys.stdout.flush()
        sleep(sleepTime)
    if end == "new":
        print()
    else:
        print(end=end)

def getInput(question=""):
    #Print question if around
    if question != "":
        typeOut(question)
    playerInput = input().lower()

    #Quit
    if playerInput in ["exit", "quit"]:
        quit()
        return None
    #Describe
    elif playerInput in ["describe room", "show room"]:
        describeRoom()
        return None
    #Check available Actions
    elif playerInput in ["check", "analyze", "choices", "actions"]:
        showChoices()
        return None
    #Inventory
    elif playerInput in ["inventory", "backpack", "inv"]:
        inv.invFull(inventory)
        return None
    elif "tp" in playerInput:
        roomPort = playerInput.replace("tp", "").replace("room", "")
        info.roomNum = roomPort
        runRoom()
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
            print()
            for item in self.items:
                typeOut(f"{item.title()}")
    
    def addItems(self, items):
        if type(items) == str:
            self.items.append(items)
            typeOut(f"-{items.title()} Added to Inventory-")
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
        description = info.items[item]["description"]
        type = info.items[item]["type"]
        if type == "weapon":
            attack = str(info.items[item]["attack"]) + " Power"
            hit = str(info.items[item]["hit"][0]) + "-" + str(info.items[item]["hit"][1]) + " to Hit"
            typeOut(f"\n{item.title()}\n   Description: {description}\n   "+
                    f"Attack: {attack}\n   Hit: {hit}")
        elif type == "armor":
            defense = str(info.items[item]["defense"]) + " Defense"
            typeOut(f"{item}\n   Description: {description}\n   "+
                    f"Protection: {defense}")
        elif type == "ring":
            typeOut(f"{item}\n   Description: {description}")

    def save(self):
        info.saveData(self.items)

#All Room related functions
def describeRoom():
    room = getRoom()
    print()
    typeOut(info.rooms[room]["description"])
    return

def changeDescription(newDes):
    room = getRoom()
    info.rooms[room]["description"] = newDes
    return

def showChoices():
    room = getRoom()
    print()
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

def foundSecret() -> None:
    room = getRoom()
    try:
        info.rooms[room]["secret"] = True
    except:
        pass

#Main Running Rooms
def runRoom():
    room = "room" + str(info.roomNum)
    print()
    typeOut(info.rooms[room]["description"])
    typeOut("What would you like to do?")
    while True:
        playerInput = getInput()
        if playerInput != None:

            #Room1
            if room == "room1":
                #Get Key
                if playerInput in ["get key", "grab key"] and checkChoice("get key"):
                    typeOut("\nYou grab the key. It seems like a perfect fit for the door.")
                    removeChoice("get key")
                    inventory.addItems("key")
                    changeDescription("You are in a room with a bared door blocking your exit.")
                
                #Open door
                elif playerInput in ["open door", "try door", "unlock door"] and checkChoice("open door"):
                    #Open with success
                    if inventory.checkForItem("key"):
                        typeOut("\nYou use the key and open the door. There is a pile of hay to your right, and a hallway to the north.")
                        removeChoice("open door")
                        addChoice("move north")
                        inventory.removeItem("key")
                        changeDescription("You are in a room with an open bared door, there is a pile of hay and a hallway to the north.")
                    #Open without success
                    else:
                        typeOut("\nYou try and open the door but it is locked. The key on the ground looks like it might fit.")

                #Check Hay (secret)
                elif playerInput in ["check hay", "analyze hay", "inspect hay"] and checkChoice("move north") and checkSecret() != True:
                    typeOut("\nYou check the hay and find a small note. You add it to your inventory.")
                    inventory.addItems("note 1")
                    foundSecret()

                #Move North (1-->2)
                elif playerInput in ["move north", "walk north", "go north"] and checkChoice("move north"):
                    typeOut("\nYou walk to your north to the next room.")
                    info.roomNum = 2
                    runRoom()

                else:
                    typeOut("\n--Invalid Command--")

            
            #Room2
            elif room == "room2":
                #Move North (2 -> 5)
                if playerInput in ["move north", "walk north", "go north"]:
                    info.roomNum = 5
                    runRoom()

                #Move East (2 -> 3)
                elif playerInput in ["move east", "walk east", "go east"]:
                    info.roomNum = 3
                    runRoom()

                #Move South (2 -> 1)
                elif playerInput in ["move south", "walk south", "go south"]:
                    info.roomNum = 1
                    runRoom()

                #Check Symbol
                elif playerInput in ["check symbol", "investigate symbol", "analyze symbol"]:
                    if checkChoice("check symbol"):
                        typeOut("\nYou feel as though you've seen this symbol long ago. Its dangerous and powerful. "+
                                "You check and it appears to be red paint on closer inspection")
                        removeChoice("check symbol")
                    else:
                        typeOut("Its a powerful and dangerous symbol.")

                #Check Candles (Secret)
                elif playerInput in ["check candles", "investigate candles", "analyze candles"] and checkSecret != True:
                    typeOut("\nYou look closer at the small flickering flames of the candle. Before your eyes, the fire glows until it's as tall as you."+
                            "Within the flame, you see a key. It moves towards you, until the base is out of the flames. You grab it, finding the key isn't even"+
                            " warm. You pocket the secret key.")
                    inventory.addItems("secret key")
                    foundSecret()

                else:
                    print("\n--Invalid Command--")


            #Room 3
            if room == "room3":
                
                #Move South (3 -> 4)
                if playerInput in ["move south", "walk south", "go south"]:
                    info.roomNum = 4
                    typeOut("You walk to the room to the south.")
                    runRoom()

                #Move West (3 -> 2)
                elif playerInput in ["move west", "walk west", "go west"]:
                    info.roomNum = 2
                    typeOut("You walk into the room to the west.")
                    runRoom()

                #Get Sword
                elif playerInput in ["get sword", "grab sword"] and checkChoice("get sword"):
                    removeChoice("get sword")
                    typeOut("\nYou pick up the sword. Although basic, it will be useful.")
                    inventory.addItems("basic sword")
                    if checkSecret():
                        changeDescription("The room you stand in has a skeleton on the ground, along with a secret passage "+
                                            "to your east. To your west is the candle room, to your south another bright room.")
                    else:
                        changeDescription("The room you stand in has a skeleton on the ground, along with a tilted painting to the east. "+
                                            "To your west is the candle room, and there is another brightly lit room to your south.")

                #Fix Painting
                elif playerInput in ["fix painting"] and checkSecret != True:
                    foundSecret()
                    typeOut("You fix the tilted painting and you hear something click behind it. As you back away, the painting slides to "+
                            "the side revealing a secret entrance.")
                    if checkChoice("get sword"):
                        changeDescription("The room you stand in has a sword on the ground with a skeleton. To your east is a secret passage "+
                                            "while to your west is the candle room. To your south is another brightly lit room.")
                    else:
                        changeDescription("The room you stand in has a skeleton on the ground, along with a tilted painting to the east. "+
                                            "To your west is the candle room, and there is another brightly lit room to your south.")

                else:
                    typeOut("--Invalid Command--")
            
            #Room 4
            elif room == "room4":

                #Move North
                if playerInput in ["move north", "go north", "walk north"]:
                    typeOut("You walk out of the room.")
                    info.roomNum = 3
                    runRoom()

                #Open Chest
                if playerInput in ["open chest", "unlock chest"] and checkChoice("open chest") and inventory.checkForItem("secret key"):
                    typeOut("You pull out your secret key and unlock the chest. It looks empty for a moment, until you see a small bronze ring. "+
                            "It looks to be the perfect fit for you.")
                    removeChoice("open chest")
                    inventory.removeItem("secret key")

        else:
            typeOut("\nWhat would you like to do?")

if __name__ == "__main__":
    inventory = Inventory()
    runRoom()