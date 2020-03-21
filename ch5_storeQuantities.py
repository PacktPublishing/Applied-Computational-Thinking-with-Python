online_store = {
    "keychain": 0.75,
    "tshirt": 8.50,
    "bottle": 10.00
    }
keychain = online_store['keychain']
tshirt = online_store['tshirt']
bottle = online_store['bottle']

choicekey = input("How many keychains will you be purchasing? If not purchasing keychains, enter 0. ")
choicetshirt = input("How many t-shirts will you be purchasing? If not purchasing t-shirts, enter 0. ")
choicebottle = input("How many t-shirts will you be purchasing? If not purchasing water bottles, enter 0. ")

print("You are purchasing " + str(choicekey) + " keychains, " + str(choicetshirt) + " t-shirts, and " + str(choicebottle) + " water bottles.")

