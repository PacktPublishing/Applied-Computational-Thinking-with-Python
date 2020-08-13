numItem = int(input('What is your maximum number for the list of triples? '))
def cost(numItem):
    while numItem > 0:
        print(numItem * 3)
        numItem -= 1


cost(numItem)
