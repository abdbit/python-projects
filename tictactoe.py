import random

#################### FUNCTIONS

def printGameMap(gameMap):
    for i in range(len(gameMap)):
        for j in range(len(gameMap[i])):
            print("(" + gameMap[i][j] + ") ", end="")
        print() #print a newline

def mapPlayerInput(playerInput):
    #home-work
    #do input sanitation, exit on out of bounds
    
    inputMap = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    return inputMap[playerInput-1]

#################### GLOBALS

#array of arrays
tikTacToeMap = [['', '', ''], \
                ['', '', ''], \
                ['', '', '']]
    
#################### GAME LOOP

while(True):
    # printGameMap(tikTacToeMap)
    # print()

    playerOne = input("Position for 'X' (1 to 9): ")
    #check for repetition, don't overwrite

    playerOneRow = mapPlayerInput(int(playerOne))[0]
    playerOneCol = mapPlayerInput(int(playerOne))[1]
    tikTacToeMap[playerOneRow][playerOneCol] = 'X'
    print()
    printGameMap(tikTacToeMap)
    print()

    #ask ChatGPT to check who won

    playerTwo = input("Position for 'O' (1 to 9): ")
    #check for repetition, don't overwrite

    playerTwoRow = mapPlayerInput(int(playerTwo))[0]
    playerTwoCol = mapPlayerInput(int(playerTwo))[1]
    tikTacToeMap[playerTwoRow][playerTwoCol] = 'O'
    print()
    printGameMap(tikTacToeMap)
    print()

    #ask ChatGPT to check who won

    # print(mapPlayerInput(int(playerOne)))
    # print(mapPlayerInput(int(playerTwo)))

   






#     # print("(" + str(a1) + ") " + "(" + str(b1) + ") " + "(" + str(c1) + ")" + "\n"
#     #   "(" + str(a2) + ") " + "(" + str(b2) + ") " + "(" + str(c2) + ") " + "\n" 
#     #   "(" + str(a3) + ") " + "(" + str(b3) + ") " + "(" + str(c3) + ") " )

# if yourTurn == a1: 
#     print("(" + str("X") + ") " + "(" + str(b1) + ") " + "(" + str(c1) + ")" + "\n"
#       "(" + str(a2) + ") " + "(" + str(b2) + ") " + "(" + str(c2) + ") " + "\n" 
#       "(" + str(a3) + ") " + "(" + str(b3) + ") " + "(" + str(c3) + ") " )

# elif yourTurn == b1:
#     print("(" + str(a1) + ") " + "(" + str("X") + ") " + "(" + str(c1) + ")" + "\n"
#       "(" + str(a2) + ") " + "(" + str(b2) + ") " + "(" + str(c2) + ") " + "\n" 
#       "(" + str(a3) + ") " + "(" + str(b3) + ") " + "(" + str(c3) + ") " )

# else:
#     print("check the spelling")           