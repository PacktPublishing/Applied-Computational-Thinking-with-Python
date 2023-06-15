P = float(input("How much are you planning on depositing? "))
r = float(input("What monthly compound rate will it be paid out? "))
t = float(input("How many years will the money be deposited? "))
n = float(input("At what rate will the interest compound per year? "))
#Convert the rate to a decimal for the formula by dividing by 100
r = r/100
A = P * (1 + r/n)**(n*t)
A = round(A, 2)
print("Total after " + str(t) + " years: ")
print(A)
