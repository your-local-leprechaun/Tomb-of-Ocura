import os
os.system("")

class Style():
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"

def changeColor(color) -> None:
    if color == "red":
        print(Style.RED, end="")
    elif color == "black":
        print(Style.BLACK, end="")
    elif color == "green":
        print(Style.GREEN, end="")
    elif color == "yellow":
        print(Style.YELLOW, end="")
    elif color == "blue":
        print(Style.BLUE, end="")
    elif color == "magenta":
        print(Style.MAGENTA, end="")
    elif color == "cyan":
        print(Style.CYAN, end="")
    return

def resetColor() -> None:
    print(Style.RESET, end="")