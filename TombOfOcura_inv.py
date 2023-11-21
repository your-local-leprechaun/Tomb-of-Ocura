from colorModule import *
from TombOfOcura_main import typeOut
import TombOfOcura_info as info

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
        #This is the equipment area! 
        #0 - Weapon, 1 - Armor, 2 - Ring, 3 - Scroll
        self.equipped = ["", "", "", ""]

    def __str__(self) -> str:
        return str(self.items)
    
    def show(self) -> None:
        if len(self.items) <= 0:
            typeOut("You have no items in your Inventory!")
        else:
            print()
            for item in self.items:
                type = info.items[item]["type"].title()
                if item not in self.equipped:
                    printStr = f"{type:7} | {item.title()}"
                else:
                    printStr = f"{type:7}*| {item.title()}"
                typeOut(printStr)
    
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

        #Misc Check
        if type == "misc":
            typeOut(f"\n{item.title()}\n   Description: {description}")

        #Note Check
        elif type == "note":
            typeOut(f"{item.title()}\n   {description}")

        #Weapon Check
        elif type == "weapon":
            attack = str(info.items[item]["attack"]) + " Power"
            hit = str(info.items[item]["hit"][0]) + "-" + str(info.items[item]["hit"][1]) + " to Hit"
            typeOut(f"\n{item.title()}\n   Description: {description}\n   "+
                    f"Attack: {attack}\n   Hit: {hit}")
            
        #Armor Check
        elif type == "armor":
            defense = str(info.items[item]["defense"]) + " Defense"
            typeOut(f"{item}\n   Description: {description}\n   "+
                    f"Protection: {defense}")
        elif type == "ring":
            typeOut(f"{item}\n   Description: {description}")

    def equipmentShow(self):
        typeOut("\n-Equipment-")
        for item in self.equipped:
            if self.equipped[0] != "":
                typeOut(f"Weapon: {item}")
            if self.equipped[1] != "":
                typeOut(f"Armor: {item}")
            if self.equipped[2] != "":
                typeOut(f"Ring: {item}")
        print()

    def equipItem(self, item):
        if info.items[item]["type"] == "weapon":
            try:
                self.equipped[0] = item
                typeOut(f"\n-{item.title()} Equipped-")
            except:
                typeOut("\n-Item Not Found-")

    def unequipItem(self, item):
        if item in self.equipped:
            self.equipped[self.equipped.index(item)] = ""
            typeOut(f"\n-{item.title()} Unequipped-")
        else:
            typeOut("-Item was not Equipped-")

    def save(self):
        info.saveData(self.items)

def invFull(inv):
    changeColor("cyan")
    typeOut("\n---Inventory---")
    inv.show()

    playerInput = ""
    while playerInput not in["quit", "exit", "leave"]:
        typeOut("\nWhat would you like to do?\n> ", end="")
        playerInput = input().lower()
        
        #Check any item in inventory
        if any(word in ["check", "analyze"] for word in playerInput.split()):
            playerInput = playerInput.replace("check ", "").replace("analyze ", "")
            inv.itemInfo(playerInput)

        elif playerInput in ["show items", "show inventory"]:
            inv.show()

        elif "equip" in playerInput and "equipment" not in playerInput and "unequip" not in playerInput:
            playerInput = playerInput.replace("equip ", "")
            inv.equipItem(playerInput)

        elif "unequip" in playerInput:
            playerInput = playerInput.replace("unequip ", "")
            inv.unequipItem(playerInput)

        elif playerInput in ["quit", "exit", "leave"]:
            pass
        
        # #when returning from playerInput it goes a bit wild
        # elif playerInput in inv.items:
        #     pass

        else:
            print("HERE")
            typeOut("--Invalid Command--")
    
    resetColor()
    typeOut("\n---Adventure----")
    return