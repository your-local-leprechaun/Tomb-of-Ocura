from basicModule import typeOut, quit
from colorModule import Style, resetColor
import ToO_info as info
from ToO_inventory import Inventory

#Global Room names so we can always have them and have access across classes
global room1
global room2
global room3

class Room:

    def __init__(self, name, description, choices, roomNumber):
        self.name = name
        self.description = description
        self.choices = choices
        self.secret = False
        self.roomNumber = roomNumber
        return

    def __str__(self):
        return f"{self.name}\n  {self.description}\n  {self.choices}"
    
    def changeDescription(self, newDes):
        self.description = newDes
        return
    
    def showDescription(self):
        print()
        typeOut(self.description)
        return
    
    def typeChoices(self):
        print()
        for choice in self.choices:
            typeOut(f"  {choice.title()}")
        print()
        return
    
    def checkChoice(self, choiceCheck) -> bool:
        if choiceCheck in self.choices:
            return True
        else:
            return False
        
    def addChoice(self, newChoice):
        self.choices.append(newChoice)
        return
    
    def removeChoice(self, oldChoice):
        try:
            self.choices.remove(oldChoice)
        except:
            print("---Unable to remove")
        return
    
    def checkSecret(self) -> bool:
        return self.secret
    
    def foundSecret(self):
        self.secret = True
        return
    
    def start(self):
        print()
        typeOut(Style.BOLD + self.name + Style.RESET)
        self.showDescription()
        typeOut("What would you like to do?")
        return

    
    def getInput(self, question="") -> str:
        """
        Deals with all basic inputs, such as quit, inventory, and some room related stuff, such as describe. This way, I don't have to put it in
        each and every room code. All these are based on the room currently in.

        Parameters
        ----------
        question : Str   Any question you would like to print off before asking for input, just like an input() function

        Returns
        -------
        playerInput : Str   This is the players input. If nothing is activated it will return it to be used in runRoom()
        """

        #Print question if around
        if question != "":
            typeOut(question)
        typeOut("> ", end="")
        playerInput = input().lower()

        #Quit
        if playerInput in ["exit", "quit"]:
            quit()
            return None
        
        #Describe
        elif playerInput in ["describe room", "show room", "describe"]:
            self.showDescription()
            return
        
        #Check available Actions
        elif playerInput in ["check", "analyze", "choices", "actions"]:
            self.typeChoices()
            return
        
        #Inventory
        elif playerInput in ["inventory", "backpack", "inv"]:
            print("---Open Inventory")

            #FIX_ME Inventory
            #inv.run()

            return None
        
        #Special Luke Function TP
        elif "tp" in playerInput:
            roomPort = playerInput.replace("tp", "").replace("room", "")
            info.roomNum = roomPort
            runRoom()

        #Return
        else:
            return playerInput

class Room1(Room):
    def __init__(self):
        name = "Jail Cell"
        description = "You are in a small room with a bared door blocking a hallway. There is a key on the floor."
        choices = ["get key", "open door"]
        Room.__init__(self, name, description, choices, 1)
    
    def run(self):
        self.start()
        while True:
            playerInput = self.getInput()
            if playerInput in ["get key", "grab key"] and self.checkChoice("get key"):
                typeOut("\nYou grab the key. It seems like a perfect fit for the door.")
                self.removeChoice("get key")
                inventory.addItems("key")
                self.changeDescription("You are in a room with a bared door blocking your exit.")
            
            #Open door
            elif playerInput in ["open door", "try door", "unlock door"] and self.checkChoice("open door"):
                #Open with success
                if inventory.checkForItem("key"):
                    typeOut("\nYou use the key and open the door. There is a pile of hay to your right, and a hallway to the north.")
                    self.removeChoice("open door")
                    self.addChoice("move north")
                    inventory.removeItem("key")
                    self.changeDescription("You are in a room with an open bared door, there is a pile of hay and a hallway to the north.")
                #Open without success
                else:
                    typeOut("\nYou try and open the door but it is locked. The key on the ground looks like it might fit.")

            #Check Hay (secret)
            elif playerInput in ["check hay", "analyze hay", "inspect hay"] and self.checkChoice("move north") and self.checkSecret() != True:
                typeOut("\nYou check the hay and find a small note.")
                inventory.addItems("note 1")
                self.foundSecret()

            #Move North (1-->2)
            elif playerInput in ["move north", "walk north", "go north"] and self.checkChoice("move north"):
                typeOut("\nYou walk to your north to the next room.")
                try:
                    room2
                except:
                    room2 = Room2()
                room2.run()

            #Catch Case
            elif playerInput == None:
                typeOut("What would you like to do?")

            else:
                typeOut("\n--Invalid Command--")

class Room2(Room):
    def __init__(self):
        name = "Symbol Room"
        description = "".join("This room is full of candles and a star looking symbol painted on the ground. It looks to be made of red paint, or at least what "+
                              "you hope is red paint. To your north is a long hallway, where you swear you see movement. To your east is a closer room, and to your south "+
                              "is the Jail Cell.")
        choices = ["move north", "move east", "move south", "check symbol"]
        Room.__init__(self, name, description, choices, roomNumber=2)

    def run(self):
        self.start()
        while True:
            playerInput = self.getInput()

            #Move North (2 -> 5)
            if playerInput in ["move north", "walk north", "go north"]:
                try:
                    room5
                except:
                    pass

            #Move East (2 -> 3)
            elif playerInput in ["move east", "walk east", "go east"]:
                try:
                    room3
                except:
                    room3 = Room3()
                room3.run()

            #Move South (2 -> 1)
            elif playerInput in ["move south", "walk south", "go south"]:
                try:
                    room1
                except:
                    room1 = Room1()
                room1.run()

            #Check Symbol
            elif playerInput in ["check symbol", "investigate symbol", "analyze symbol", "check floor"]:
                if self.checkChoice("check symbol"):
                    typeOut("\nYou feel as though you've seen this symbol long ago. Its dangerous and powerful. "+
                            "You check and it appears to be red paint on closer inspection")
                    self.removeChoice("check symbol")
                else:
                    typeOut("Its a powerful and dangerous symbol.")

            #Check Candles (Secret)
            elif playerInput in ["check candles", "investigate candles", "analyze candles"] and self.checkSecret != True:
                typeOut("\nYou look closer at the small flickering flames of the candle. Before your eyes, the fire glows until it's as tall as you."+
                        "Within the flame, you see a key. It moves towards you, until the base is out of the flames. You grab it, finding the key isn't even"+
                        " warm. You pocket the secret key.")
                inventory.addItems("secret key")
                self.foundSecret()

            elif playerInput == None:
                typeOut("What would you like to do?")

            else:
                typeOut("\n--Invalid Command--")

class Room3(Room):
    def __init__(self):
        name = "Skeleton and Painting"
        description = "".join("The room you stand in has a sword on the ground with a skeleton. On the east wall, there is a crooked painting. "+
                                "Maybe a fight took place, and the skeleton lost. To your south is another room, and to your west is the room with"+
                                " candles.")
        choices = ["move west", "move south", "get sword"]
        Room.__init__(self, name, description, choices, roomNumber=3)

    def run(self):
        self.start()
        while True:
            playerInput = self.getInput()

            #Move South (3 -> 4)
            if playerInput in ["move south", "walk south", "go south"]:
                typeOut("\nYou walk to the room to the south.")
                try:
                    room4
                except:
                    room4 = Room4()
                room4.run()

            #Move West (3 -> 2)
            elif playerInput in ["move west", "walk west", "go west"]:
                typeOut("\nYou walk into the room to the west.")
                try:
                    room2
                except:
                    room2 = Room2()
                room2.run()

            #Get Sword
            elif playerInput in ["get sword", "grab sword"] and self.checkChoice("get sword"):
                self.removeChoice("get sword")
                typeOut("\nYou pick up the sword. Although basic, it will be useful.")
                inventory.addItems("basic sword")
                if self.checkSecret():
                    self.changeDescription("The room you stand in has a skeleton on the ground, along with a secret passage "+
                                        "to your east. To your west is the candle room, to your south another bright room.")
                else:
                    self.changeDescription("The room you stand in has a skeleton on the ground, along with a tilted painting to the east. "+
                                        "To your west is the candle room, and there is another brightly lit room to your south.")

            #Fix Painting
            elif playerInput in ["fix painting"] and self.checkSecret != True:
                self.foundSecret()
                typeOut("\nYou fix the tilted painting and you hear something click behind it. As you back away, the painting slides to "+
                        "the side revealing a secret entrance.")
                if self.checkChoice("get sword"):
                    self.changeDescription("The room you stand in has a sword on the ground with a skeleton. To your east is a secret passage "+
                                        "while to your west is the candle room. To your south is another brightly lit room.")
                else:
                    self.changeDescription("The room you stand in has a skeleton on the ground, along with a tilted painting to the east. "+
                                        "To your west is the candle room, and there is another brightly lit room to your south.")

            elif playerInput == None:
                typeOut("What would you like to do?")

            else:
                typeOut("--Invalid Command--")

class Room4(Room):
    
    def __init__(self):
        name = "Treasure Room"
        description = "The room is brightly lit and there is a locked chest in the middle of it."
        choices = ["open chest", "move north"]
        Room.__init__(self, name, description, choices, roomNumber="4")

    def run(self):
        self.start()
        while True:
            playerInput = self.getInput()

            #Move North (4 -> 3)
            if playerInput in ["move north", "go north", "walk north"]:
                typeOut("You walk out of the room.")
                try:
                    room3
                except:
                    room3 = Room3()
                room3.run()

            #Open Chest
            elif playerInput in ["open chest", "unlock chest"] and self.checkChoice("open chest") and inventory.checkForItem("secret key"):
                typeOut("\nYou pull out your secret key and unlock the chest. It looks empty for a moment, until you see a small bronze ring. "+
                        "It looks to be the perfect fit for you.")
                self.removeChoice("open chest")
                inventory.removeItem("secret key")
                inventory.addItems("bronze ring")
                self.changeDescription("You are in a brightly lit room with torches on the walls. There is an already opened chest in the middle. "
                                    + "There is a door to your north leading to the skeleton room.")

            else:
                typeOut("\n--Invalid Command--")



if __name__ == "__main__":
    inventory = Inventory()
    room1 = Room1()
    room1.run()