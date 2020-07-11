import time

print("Let's play a game. Choose a color to learn your destiny. Choose wisely or you'll have to start over. ")


i = 0
while i < 4:
    color = str(input("Choose a color: red, green, or yellow. "))
    if color == "green":
        print("You must wait 5 seconds to learn your fate.")
        time.sleep(5)
        print("You win! Excellent choice!")
        break
    elif color == "yellow":
        print("You must wait 2 seconds to learn your fate.")
        time.sleep(2)
        print("You lose! You must start over.")
        i = i + 1
    else:
        print("You must wait 4 seconds to learn your fate.")
        time.sleep(4)
        print("You lose! You must start over.")
        i = i + 1

