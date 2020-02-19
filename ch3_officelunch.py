#Ask the user for the number of sandwich meals ordered and save as variable.
number_of_sandwiches = int(raw_input("How many sandwich lunches were ordered? "))

#Ask the user for the number of salad meals ordered and save as variable.
number_of_salads = int(raw_input("How many salad lunches were ordered? "))

#Create total_cost variable and save the algorithm for total the new variables.
total_cost = 8.50 * number_of_sandwiches + 7.95 * number_of_salads

#Print the total cost. Don't forget to convert the total_cost to string. 
print("The total cost for the employee lunch is $" + str(total_cost) + ".")

