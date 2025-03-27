import random

possibleoutcome = ['1','2','3','4','5','6']

oneplayer = input("Wanna roll the dice? (yes/no): ")   
if oneplayer.lower() == "yes" or "Yes" or "YES":
     randompick = int(random.choice(possibleoutcome))
     print("Your roll: " + str(randompick))
     playerturns = randompick
     print("Your score: " + str(playerturns + randompick))
else:
     print("Check the spell")


