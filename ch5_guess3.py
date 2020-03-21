import random as rand
compnumber = rand.randint(1, 100)
i = 5
for number in range(5):
    usernumber = int(input("Choose a number between 1 and 100. You have " + str(i) + " guesses left. "))
    if compnumber == usernumber:
        print("You win!")
    else:
        i = i - 1

print("You're out of guesses! You lose! ")

