print("The votes for Blue are in.")
blues = 0
with open("ch8_survey.txt") as file:
    for line in file:
        line = line.strip()
        name, color = line.split(' - ')
        if color == "Blue":
            blues = blues + 1
print(blues)

        
