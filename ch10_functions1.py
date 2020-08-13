minNum = int(input('What\'s your minimum number? '))
maxNum = int(input('What\'s your maximum number? '))


def myNumbers(minNum, maxNum):
    myList = []
    for num in range(minNum, maxNum + 1):
        myList.append(num)
    print(myList)


myNumbers(minNum, maxNum)
