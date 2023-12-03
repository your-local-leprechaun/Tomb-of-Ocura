from basicModule import typeOut
import ToO_main as main

def load():
    file = open("saveData/roomSave.txt", "r")
    allSave = file.read().split("|;|")


    #Begin running from specific room!
    roomNumber = int(allSave[1])
    main.room1 = main.Room1()
    main.room2 = main.Room2()
    main.room3 = main.Room3()
    main.room4 = main.Room4()
    if roomNumber == 1:
        main.main()
    elif roomNumber == 2:
        main.room2.run()
    elif roomNumber == 3:
        main.room3.run()
    elif roomNumber == 4:
        main.room4.run()


typeOut("The Tomb of Ocura\n   1. Start New Game\n   2. Load Game\n   3. Trophies\n   4. Credits")

typeOut("What would you like to do?")
inLoop = True
while inLoop:
    playerInput = input().lower()
    if playerInput in ["1", "start new game", "new game", "start game"]:
        typeOut("Good luck on your adventure through the Tomb of Ocura!!")
        main.main()
    elif playerInput in ["2", "load game", "continue"]:
        try:
            load()
            inLoop=False
        except IndexError:
            typeOut("\n--No Available Load Data--")

    else:
        typeOut("--Invalid Command--")