
print("Welcome to the Temp Conversion App")

f = float(input("\nWhat is the given temp in degrees Fahrenheit: ")) # 4 decimals, table format

c = round((f -32) * 5/9, 4)
k = round((f -32) * 5/9 + 273.15, 4)

print("\nDegrees Fahrenheit: " + str(f))
print("Degrees Celsius: " + str(c))
print("Degrees Kelvin: " + str(k))