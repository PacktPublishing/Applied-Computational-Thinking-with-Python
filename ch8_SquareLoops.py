print("This program will print the squares of the numbers in a given range of numbers.")
a = int(input("What is the minimum of your range? "))
b = int(input("What is the maximum of your range? "))

Numbers = []
b = b + 1
for i in range(a, b):
    j = i**2
    Numbers.append(j)
    i = i + 1

print(Numbers)
