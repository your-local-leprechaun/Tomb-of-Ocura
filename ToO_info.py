
playerName = "Jae"

rooms = []

roomNum = 1

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

    #Weapons
    "basic sword" : {
        "description" : "This is a basic sword. It's nothing special "+
                        "but it'll keep you safe.",
        "type" : "weapon",
        "attack" : 1,
        "hit" : [0,3]
    },

    #Armor
    "Ratty Leather" : {
        "description" : "A leather armor set that's old and ratty. It " +
                        "might not be much, but it should protect you slightly.",
        "type" : "armor",
        "defense" : 1
    },

    #Rings
    "bronze ring" : {
        "description" : "A small ring that seems to fit perfectly. It "+
                        "can boost defense a small amount.",
        "type" : "ring",
        "power" : "+2 Defense"
    },

    #Magic
}