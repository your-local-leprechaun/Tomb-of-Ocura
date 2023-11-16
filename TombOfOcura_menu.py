from time import sleep
import sys

def typeOut(message, sleepTime = 0.03, end="new"):
    for char in message:
        print(char, end="")
        sys.stdout.flush()
        sleep(sleepTime)
    if end == "new":
        print()
    else:
        print(f"{end}")

typeOut("The Tomb of Ocura\n   1. Start New Game\n   2. Load Game\n   3. Trophies\n   4. Credits")

typeOut("What would you like to do?")
while True:
    playerInput = input().lower()
    if playerInput in ["1", "start new game", "new game", "start game"]:
        typeOut("Good luck on your adventure through the Tomb of Ocura!!")
        exec(open("TombOfOcura_main.py").read())