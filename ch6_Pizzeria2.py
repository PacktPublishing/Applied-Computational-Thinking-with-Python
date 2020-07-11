#Get input for your variables for size and sauce first. 

size_choice = str(input("Is this a personal or family pizza? Type 1 for personal and 2 for family. "))

sauce_choice = str(input("Which sauce would you like? Marinara or garlic cream? Type m for marinara and g for garlic cream. "))
if sauce_choice == "g":
    sauce = "garlic cream"
else:
    sauce = "marinara"

#The cheese choice will dictate a few more options. Define the variable first.                
cheese_choice = str(input("Would you like cheese on your pizza? Type y for yes and n for no. "))
                
#Toppings need to happen whether or not you want cheese. 
if cheese_choice == "y":
    cheese2_choice = str(input("Would you like regular cheese or extra cheese? Type r for regular and e for extra cheese. "))
    if cheese2_choice == "r":
        cheese = "regular cheese"
    else:
        cheese = "extra cheese"
    toppings1_input = str(input("Would you like mushrooms on your pizza? Type y for yes and n for no. "))
    if toppings1_input == "y":
        toppings1 = "mushrooms"
    else:
        toppings1 = "no mushrooms"
else:
    cheese = "no cheese"
    

if cheese_choice == "n":
    toppings1_input = str(input("Would you like mushrooms on your pizza? Type y for yes and n for no. "))
    if toppings1_input == "y":
        toppings1 = "mushrooms"
    else:
        toppings1 = "no mushrooms"

ready_end = str(input("Do you need to make any changes? Type y for yes and n for no. "))
if ready_end == "y":
    size_choice = str(input("Is this a personal or family pizza? Type 1 for personal and 2 for family. "))

    sauce_choice = str(input("Which sauce would you like? Marinara or garlic cream? Type m for marinara and g for garlic cream. "))
    if sauce_choice == "g":
        sauce = "garlic cream"
    else:
        sauce = "marinara"
                
    cheese_choice = str(input("Would you like cheese on your pizza? Type y for yes and n for no. "))

    if cheese_choice == "y":
        cheese2_choice = str(input("Would you like regular cheese or extra cheese? Type r for regular and e for extra cheese. "))
        if cheese2_choice == "r":
            cheese = "regular cheese"
        else:
            cheese = "extra cheese"
        toppings1_input = str(input("Would you like mushrooms on your pizza? Type y for yes and n for no. "))
        if toppings1_input == "y":
            toppings1 = "mushrooms"
        else:
            toppings1 = "no mushrooms"
    else:
        cheese = "no cheese"
        

    if cheese_choice == "n":
        toppings1_input = str(input("Would you like mushrooms on your pizza? Type y for yes and n for no. "))
        if toppings1_input == "y":
            toppings1 = "mushrooms"
        else:
            toppings1 = "no mushrooms"
    print("You want a " + size_choice + " pizza with " + sauce + " sauce, " + cheese + ", and " + toppings1 + ".")
else:
     print("You want a " + size_choice + " pizza with " + sauce + " sauce, " + cheese + ", and " + toppings1 + ".")
