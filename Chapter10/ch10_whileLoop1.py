myAnimals = []
print('Let\'s see how many animals you can name. Get ready!')
readyPlayer = input('When you are ready to begin, type y. ')
while readyPlayer == 'y':
    if readyPlayer == 'y':
        animalAdd = input('Name an animal. ')
        myAnimals.append(animalAdd)
        readyPlayer = input('Ready for the next one? Type y for yes or n for no. ')
    else:
        print(myAnimals)
howMany = len(myAnimals)
print('You were able to name ' + str(howMany) + ' animals. Here\'s your list: ')
print(myAnimals)
