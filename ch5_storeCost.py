online_store = {
    "keychain": 0.75,
    "tshirt": 8.50,
    "bottle": 10.00
    }

choicekey = int(input("How many keychains will you be purchasing? If not purchasing keychains, enter 0. "))
choicetshirt = int(input("How many t-shirts will you be purchasing? If not purchasing t-shirts, enter 0. "))
choicebottle = int(input("How many t-shirts will you be purchasing? If not purchasing water bottles, enter 0. "))

print("You are purchasing " + str(choicekey) + " keychains, " + str(choicetshirt) + " t-shirts, and " + str(choicebottle) + " water bottles.")

if choicekey > 9:
    online_store['keychain'] = 0.65
if choicetshirt > 9:
    online_store['tshirt'] = 8.00
if choicebottle > 9:
    online_store['bottle'] = 8.75

keychain = online_store['keychain']
tshirt = online_store['tshirt']
bottle = online_store['bottle']

print(online_store)
