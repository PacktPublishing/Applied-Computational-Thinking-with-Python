online_store = {
    "keychain": 0.75,
    "tshirt": 8.50,
    "bottle": 10.00
    }

choicekey = int(input("How many keychains will you be purchasing? If not purchasing keychains, enter 0. "))
choicetshirt = int(input("How many t-shirts will you be purchasing? If not purchasing t-shirts, enter 0. "))
choicebottle = int(input("How many t-shirts will you be purchasing? If not purchasing water bottles, enter 0. "))

if choicekey > 9:
    online_store['keychain'] = 0.65
if choicetshirt > 9:
    online_store['tshirt'] = 8.00
if choicebottle > 9:
    online_store['bottle'] = 8.75

print("You are purchasing " + str(choicekey) + " keychains, " + str(choicetshirt) + " t-shirts, and " + str(choicebottle) + " water bottles.")

perskey = input("Will you personalize the keychains for an additional $1.00 each? Type yes or no. ")
perstshirt = input("Will you personalize the t-shirts for an additional $5.00 each? Type yes or no. ")
persbottle = input("Will you personalize the water bottles for an additional $7.50 each? Type yes or no. ")

if perskey == ("yes" or "Yes"):
    online_store['keychain'] = online_store['keychain'] + 1.00
if perstshirt == ("yes" or "Yes"):
    online_store['tshirt'] = online_store['tshirt'] + 5.00
if persbottle == ("yes" or "Yes"):
    online_store['bottle'] = online_store['bottle'] + 7.50

keychain = online_store['keychain']
tshirt = online_store['tshirt']
bottle = online_store['bottle']

totalkey = choicekey * keychain
totaltshirt = choicetshirt * tshirt
totalbottle = choicebottle * bottle
grandtotal = totalkey + totaltshirt + totalbottle

print("Keychain total: $" + str(totalkey))
print("T-shirt total: $" + str(totaltshirt))
print("Water bottle total: $" + str(totalbottle))
print("Your order total: $" + str(grandtotal))


