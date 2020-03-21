import random as rand
compnumber = rand.randint(1, 100)
usernumber = int(input("Choose a number between 1 and 100. You'll get 5 guesses or you lose! "))

if compnumber == usernumber:
    print("You win!")
else:
    print("You lose!")
