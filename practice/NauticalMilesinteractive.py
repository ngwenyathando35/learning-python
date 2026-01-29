NUM_KILOMETRES = 1.852
NUM_MILES = 1.150779

nauticalMiles = input("Enter nautical miles >> ")
kiloM = int(nauticalMiles) * NUM_KILOMETRES
miles = int(nauticalMiles) * NUM_MILES
print(f"{nauticalMiles} in nautical miles is {miles}")
print(f"{nauticalMiles} in nautilcal kilos is {kiloM}")