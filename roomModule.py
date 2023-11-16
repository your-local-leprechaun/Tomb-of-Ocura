from TombOfOcura_main import typeOut, getRoom
import TombOfOcura_info as info

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

