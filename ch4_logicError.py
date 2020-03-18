number = int(input("Pick a number between 1 and 20. "))
if number < 10:
    if number < 6:
        print("Why such a small number?")
    else:
        print("Well, less than 10 but greater than 5. I'll take it.")
if number < 21:
    if number < 16:
        print("You like values that are greater than 10, but not too much greater. I guess that's fine.")
    else:
        print("I like larger numbers myself too.")
else:
    print("That number isn't between 0 and 20. Run the program and try again.")
