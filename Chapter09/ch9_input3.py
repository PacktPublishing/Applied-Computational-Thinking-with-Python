#Create the list
names = []
  
#Ask user how many names will be added
name = int(input("How many names will be in the list? ")) 
  
#Iterate to add each name to the list
for i in range(0, name): 
    people = str(input()) 
  
    names.append(people) 
      
print(names) 
