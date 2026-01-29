# Python only has 4 data types namely, interger, float, complex, bool

anInt = int(input("Please enter an integer >> "))
aFloat = float(input("Please enter a float >> "))
aComplex = complex(input("Please enter a complex (e.g 3 + 4j)>> "))
aBool = bool(input("Please enter a boolean value >> "))
name = input("Please enter your name")

print("The int is " + str(anInt))
print("The float is " + str(aFloat))
print(f"The complex is {aComplex}")
print("The boolean value is " + str(aBool))
print(f"Thank you {name}")


# A more cleaner way to print numbers is 
# print(f"Your age is {age})