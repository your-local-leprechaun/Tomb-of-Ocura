from time import sleep
import sys

playerName = "Jae"

items = {
    "Basic Sword" : {
        "Description" : "This is a basic sword. It's nothing special "+
                        "but it'll keep you safe.",
        "Type" : "Weapon",
        "Attack" : 1,
        "Hit" : [0,3]
    },
    "Ratty Leather" : {
        "Description" : "A leather armor set that's old and ratty. It " +
                        "might not be much, but it should protect you slightly.",
        "Type" : "Armor",
        "Defense" : 1
    },
    "Amethyst Ring" : {
        "Description" : "A small ring that seems to fit perfectly. It "+
                        "can boost defense a small amount.",
        "Type" : "Ring",
        "Power" : "+3 Defense"
    },
}

rooms = {
    "room1" : {
        "description" : "You are in a small room, with a bared door blocking a hallway. There is a key on the floor.",
        "choices" : ["get key", "open door"],
        "secret" : False
    }
}

roomNum = 1

def saveData():
    #saves all data needed:
    #   Inventory, room data, room num, player name,
    print("room1")
    pass

def loadData():
    #loads all data if found. All data same as that saved in saveData()
    pass


if __name__ != "__main__":
    pass
    # room1 = Room("room1", "You are in a room that looks like a jail. There are bars and a locked door, with a key on the ground.",
    #              ["get key", "open door"])