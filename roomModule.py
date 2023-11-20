from TombOfOcura_main import typeOut, getRoom
import TombOfOcura_info as info

#All Room related functions
def describeRoom() -> None:
    """
    This types out the description for whatever room you are currently in, based on info doc
    """
    room = getRoom()
    print()
    typeOut(info.rooms[room]["description"])
    return

def changeDescription(newDes) -> None:
    """
    Changes description of room you're in based on parameters

    Parameters
    ----------
    newDes : Str   String that will be the new description for a room
    """
    room = getRoom()
    info.rooms[room]["description"] = newDes
    return

def showChoices() -> None:
    """
    This function types out all the possible choices for your current room
    """
    room = getRoom()
    print()
    for choice in info.rooms[room]["choices"]:
        typeOut(choice.title())
    return

def addChoice(addedChoice) -> None:
    """
    Adds a choice to the choice list for the current room

    Parameters
    ----------
    addedChoice : Str   any string you would like to add to the choice options
    """
    room = getRoom()
    info.rooms[room]["choices"].append(addedChoice)
    return

def removeChoice(removedChoice) -> None:
    """
    Removes choice from choice list in current room

    Parameters
    ----------
    removedChoice : Str   the text of the choice you want removed
    """
    room = getRoom()
    try:
        info.rooms[room]["choices"].remove(removedChoice)
    except:
        print("--Unable to remove--")
    return

def checkChoice(choiceToCheck) -> bool:
    """
    Checks if choice is in the choice list for the current room

    Parameters
    ----------
    choiceToCheck : Str   the string it will check if it's in the list
    """
    room = getRoom()
    if choiceToCheck in info.rooms[room]["choices"]:
        return True
    else:
        return False

def checkSecret() -> bool:
    """
    Checks if secret is true for current room

    Returns
    -------
    bool   True if secret has been found, false if not
    """
    room = getRoom()
    try:
        return info.rooms[room]["secret"]
    except:
        return False

def foundSecret() -> None:
    """
    Changes Secret to be true in room dictionary
    """
    room = getRoom()
    try:
        info.rooms[room]["secret"] = True
    except:
        pass

