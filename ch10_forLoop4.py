print('This program will provide a list of cubes for you. ')
minRange = int(input('What\'s the minimum for your range? '))
maxRange = int(input('What\'s the maximum for your range? '))
listOfCubes = []

for value in range(minRange, maxRange+1):
    number = value**3
    listOfCubes.append(number)

print('Your list of cubes in the range(' + str(minRange) + ', ' \
      +str(maxRange) + ') is: ')
print(listOfCubes)
