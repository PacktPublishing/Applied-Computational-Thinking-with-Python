print("This program will print the even numbers for any range of numbers provided.")

endpoint1 = int(input("What is the lower endpoint of your range? "))
endpoint2 = int(input("What is the upper endpoint of your range? "))

endpoint2 = endpoint2 + 1

evenNumbers = []

for i in range(endpoint1, endpoint2):
    if i % 2 == 0:
        evenNumbers.append(i)
        i = i + 1
        
print(evenNumbers)
