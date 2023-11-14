from TombOfOcura_main import typeOut


def invFull(inv):
    typeOut("\n---Inventory---")
    for item in inv.items:
        print(item.title())

    playerInput = ""
    while playerInput not in["quit", "exit", "leave"]:
        print("\nWhat would you like to do?")
        playerInput = input().lower()
        
        #Check any item in inventory
        if any(item in inv.items for item in playerInput):
            print(playerInput)
    return