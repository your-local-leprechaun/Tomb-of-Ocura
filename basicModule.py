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

def getLine(saveFile, roomNumber) -> str:
    lines = open(f"saveData\{saveFile}", "r").readlines()
    return lines[roomNumber - 1]

def replaceLine(saveFile, lineNumber, replacement):
    try:
        lines = open(f"saveData\{saveFile}", "r").readlines()
        lines[lineNumber-1] = replacement + "\n"
        out = open(f"saveData\{saveFile}", 'w')
        out.writelines(lines)
        out.close()
    except IndexError:
        lineCreation = ""
        #Number of rooms == the number in range!
        for i in range(10):
            lineCreation += "\n"

        file = open(f"saveData\{saveFile}", "w")
        file.write(lineCreation)
        file.close()

        lines = open(f"saveData\{saveFile}", "r").readlines()
        lines[lineNumber-1] = replacement + "\n"
        out = open(f"saveData\{saveFile}", 'w')
        out.writelines(lines)
        out.close()

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
    
if __name__ == "__main__":
    replaceLine("roomSave.txt", 10, "Change to this")