eggs = (int(input("Please enter the number of eggs >> ")))

numDozen = int(eggs / 12)
numEggs = int(eggs % 12)

dozenPrice = numDozen * 3.25
eggPrice = numEggs * 0.45

price = dozenPrice + eggPrice

print(f"You ordered {eggs} eggs. That's {numDozen} dozen + at $3.25 per dozen and {numEggs} loose eggs at 45 cents each for a total of ${price}")