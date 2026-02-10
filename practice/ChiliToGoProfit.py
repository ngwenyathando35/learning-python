adultMealPrice = 7
childMealPrice = 4
adultMealCostToProduce = 4.35
childMealCostToProduce = 3.10

numChildMeal = int(input("How many child meals do you want >>"))
numAdultMeal = int(input("How many adult means you want >>"))

totalAdultMeal = adultMealPrice * numAdultMeal
totalChildMeal = childMealPrice * numChildMeal
grandTotal = totalAdultMeal + totalChildMeal
childMealProfit = totalChildMeal - (childMealCostToProduce * numChildMeal)
adultMealProfit = totalAdultMeal - (adultMealCostToProduce * numAdultMeal)
profit = childMealProfit + adultMealProfit

print(f"The total money collected for the childrens meals is ${totalChildMeal}")
print(f"The total money collected for the adult meals is ${totalAdultMeal}")
print(f"The profit is ${profit}")