class mammals:
     def description(self):
       print("Mammals are vertebrate animals.")
 
     def viviparous(self):
       print("Mammals are viviparous, but some are not.")
 
class monkey(mammals):
     def viviparous(self):
       print("Monkeys are viviparous.")
 
class platypus(mammals):
     def viviparous(self):
       print("The platypus is not viviparous. It's an egg-laying mammal.")
 
obj_mammals = mammals()
obj_monkey = monkey()
obj_platypus = platypus()
 
obj_mammals.description()
obj_mammals.viviparous()
 
obj_monkey.description()
obj_monkey.viviparous()
 
obj_platypus.description()
obj_platypus.viviparous()
