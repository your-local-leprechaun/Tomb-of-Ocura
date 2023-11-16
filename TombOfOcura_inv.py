from TombOfOcura_main import typeOut
from colorModule import *


def invFull(inv):
    changeColor("blue")
    typeOut("\n---Inventory---")
    inv.show()

    playerInput = ""
    while playerInput not in["quit", "exit", "leave"]:
        typeOut("\nWhat would you like to do?")
        playerInput = input().lower()
        
        #Check any item in inventory
        if any(word in ["check", "analyze"] for word in playerInput.split()):
            playerInput = playerInput.replace("check ", "").replace("analyze ", "")
            inv.itemInfo(playerInput)

        elif playerInput in ["show items", "show inventory"]:
            inv.show()

        else:
            typeOut("--Invalid Command--")
    
    resetColor()
    typeOut("\n---Adventure----")
    return