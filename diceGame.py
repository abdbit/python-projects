import random
import os 

possibleOutcomes = ['1','2','3','4','5','6']
maxScore = 300
totalTurns = 30
currentTurns = 0

playerScore = 0
botScore = 0

while(currentTurns < totalTurns):
    print("\nTurn number: " + str(currentTurns + 1))
    promptResponse = input("Wanna roll the dice? (yes/no): ")

    #All options: y, Y, yes, Yes, YES
    if str.find("yYyesYesYES", promptResponse.lower()) != -1:
        diceRollPlayer = int(random.choice(possibleOutcomes))
        diceRollBot = int(random.choice(possibleOutcomes))

        # os.system("cls || clear")

        print("Your roll: " + str(diceRollPlayer), end=" | ")
        print("My roll: " + str(diceRollBot))
        
        playerScore = playerScore + diceRollPlayer
        botScore = botScore + diceRollBot
        
        print("Your score: " + str(playerScore), end=" | ")
        print("My score: " + str(botScore))

        if playerScore >= maxScore or botScore >= maxScore:
          if playerScore > botScore:
              print("You won!")
          elif botScore > playerScore:
               print("Hahaha I won!")
          else:
              print("It's a draw :(")
          break

        currentTurns = currentTurns + 1
    else:
        print("Please enter only 'y' or 'Y' or 'yes' or 'Yes' or 'YES'")

if playerScore > botScore:
    print("You won!")
elif botScore > playerScore:
    print("Hahaha I won!")
else:
    print("It's a draw :(")