numQuarts = int(input("Please enter the number of quarts >> "))
MAX_NUM_QUARTS_IN_GALLON = 4
gallonsNeeded = int(numQuarts/MAX_NUM_QUARTS_IN_GALLON)
quartsNeeded = numQuarts % MAX_NUM_QUARTS_IN_GALLON

print(f"A job that needs {numQuarts} quarts requires {gallonsNeeded} gallons plus {quartsNeeded} quarts")