
print("Welcome to the MPH to MPS Conversion App")

mph = float(input("\nWhat is your speed in miles per hour: "))
conversion = mph * .44704

mps = float(round(conversion, 2)) # 2 is for 2 decimal cases

print("Your speed in mps is: " + str(mps))
