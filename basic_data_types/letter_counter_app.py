
print("Welcome to the Letter Counter App")

name = input("\nWhat is your name: ").title()
print("Hello, " + name + "!")
print("I will count the number of times that a specific letter occurs in a message.")

message = input("Please enter a message: ")
letter = input("Which letter would you like us to count the occurrences of: ")

message = message.lower() # updating message to make it all lowercase
letter = letter.lower() # same here

letter_count = message.count(letter)

print("\n" + name + ", your message has " +str(letter_count) + " " + letter + "'s in it. ")