import random

possibleoutcome = ['1','2','3','4','5','6']
randompick = int(random.choice(possibleoutcome))

while playerturns < 30:
   oneplayer = input("Should I roll? (yes/no): ")
   if oneplayer.lower() == "yes":
        randompick = int(random.choice(possibleoutcome))
        print("Your roll: " + randompick)
        playerturns = int( 0 + randompick)
        print("Your score: " + playerturns)
   else:
       print("Check the spell")


