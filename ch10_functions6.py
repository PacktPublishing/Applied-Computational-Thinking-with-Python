numItem = int(input('What is your maximum number for the list of triples? '))
myList = []
def cost(numItem):
    for x in range(1, numItem + 1):
        newNum = 3 * x
        myList.append(newNum)
    print(myList)    


cost(numItem)
