from sys import stdout
from time import sleep

def typeOut(message, sleepTime=0.0, end="\n") -> None:
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
        stdout.flush()
        sleep(sleepTime)
    print(end, end="")
    return

def quit() -> None:
    """
    Allows a quit to happen rather than having to break a billion times as we're running lots of functions, this would be easier. Also
    asks if sure which is good.
    """
    typeOut("\nAre you sure you want to quit? (y/n)\nProgress will not be saved currently")
    playerInput = input().lower()
    if playerInput in ["yes", "y", "exit"]:
        typeOut("Hope you come back soon!")
        exit()
    else:
        return