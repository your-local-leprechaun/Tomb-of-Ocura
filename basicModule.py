import sys
from time import sleep

def typeOut(message, sleepTime=0.01, end="\n") -> None:
    """
    My favorite function. Shows the text typing out rather than just appearing. Very fun to use
    and makes anything look better in my eyes

    Parameters
    ----------
    message : Str   The text you want printed out
    sleepTime : Float   Amount of time you want in between each character
    end : Str   Changes how the sentence ends, just like a normal print function
    """
    for char in message:
        print(char, end="")
        sys.stdout.flush()
        sleep(sleepTime)
    print(end, end="")
    return

def save():
    from ToO_inventory import inv
    from ToO_info import playerName, roomNum, rooms
    #saves all data needed:
    #   Inventory, room data, room num, player name,

    #Room Saves
    file = open("saveData/roomSave.txt", "w")
    for room in rooms:
        if room.roomNumber <= roomNum:
            file.write(f"{room.description}||{room.choices}||{room.secret}//\n")
    
    file.write("\n|;|\n")

    #Room Number Save
    file.write(str(roomNum))
    file.write("\n|;|\n")

    #Inventory Items save
    for item in inv.items:
        file.write(f"{item}||")

    file.write("\n|;|\n")

    file.close()
    pass

def check():
    from ToO_inventory import inv
    print(str(inv))

def death():
    pass

def quit() -> None:
    """
    Allows a quit to happen rather than having to break a billion times as we're running lots of functions, this would be easier. Also
    asks if sure which is good.
    """
    typeOut("\nAre you sure you want to quit? (y/n)\nProgress will not be saved currently")
    playerInput = input().lower()
    if playerInput in ["yes", "y", "exit"]:
        save()
        typeOut("Hope you come back soon!")
        sys.exit()
    else:
        return