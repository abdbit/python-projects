import random

thirty = 30
possibleoutcome = ['1','2','3','4','5','6']
randompick = int(random.choice(possibleoutcome))

while randompick < thirty:
   oneplayer = input("Should I roll? (yes/no): ")
   if oneplayer.lower() == "yes":
        randompick = int(random.choice(possibleoutcome))
        print(randompick)
   else:
       print("sorry")
