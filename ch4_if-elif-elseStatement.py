number = int(input("Pick a number between 1 and 20. "))
if number < 10:
    print("That's less than 10.")
elif number < 21:
    print("That's between 10 and 20.")
else:
    print("That number isn't between 0 and 20. Run the program and try again.")
