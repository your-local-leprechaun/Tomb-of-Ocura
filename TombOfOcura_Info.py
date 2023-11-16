
playerName = "Jae"

items = {
    #Misc
    "key" : {
        "description" : "A basic key used to unlock doors.",
        "type" : "misc"
    },
    "secret key" : {
        "description" : "A key you got when you discovered a secret. Used to unlock mostly chests.",
        "type" : "misc"
    },

    #Notes
    "note 1" : {
        "description" : "--Start of story here.--",
        "type" : "note"
    },

    "basic sword" : {
        "description" : "This is a basic sword. It's nothing special "+
                        "but it'll keep you safe.",
        "type" : "weapon",
        "attack" : 1,
        "hit" : [0,3]
    },
    "Ratty Leather" : {
        "description" : "A leather armor set that's old and ratty. It " +
                        "might not be much, but it should protect you slightly.",
        "type" : "armor",
        "defense" : 1
    },
    "Amethyst Ring" : {
        "description" : "A small ring that seems to fit perfectly. It "+
                        "can boost defense a small amount.",
        "type" : "ring",
        "power" : "+3 Defense"
    },
}

rooms = {
    "room1" : {
        "description" : "You are in a small room, with a bared door blocking a hallway. There is a key on the floor.",
        "choices" : ["get key", "open door"],
        "secret" : False
    },
    "room2" : {
        "description" : "This room is full of candles, and a star looking symbol on the ground. It looks to be painted in red paint, at least you hope its paint."+
                        "To your north is a longer hallway, and you swear you see movement. To your east, a closer room, and to your south, the jail room you"+
                        " started in",
        "choices" : ["move north", "move east", "move south", "check symbol"],
        "secret" : False
    },
    "room3" : {
        "description" : "The room you stand in has a sword on the ground with a skeleton. On the east wall, there is a crooked painting. "+
                        "Maybe a fight took place, and the skeleton lost. To your south is another room, and to your west is the room with"+
                        " candles.",
        "choices" : ["move west", "move south", "get sword"],
        "secret" : False
    },
    "room4" : {
        "description" : "Room 4 description",
        "choices" : ["open chest", "move north"]
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