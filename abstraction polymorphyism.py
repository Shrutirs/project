'''Abstraction'''
### Abstraction is used to hide the internal functionality of the function from the users.
###The users only interact with the basic implementation of the function, but inner working is hidden


# from abc import ABC,abstractmethod
  
# class Polygon(ABC):   
  
#    @abstractmethod   
#    def sides(self):   
#       pass  
  
# class Triangle(Polygon):   
#    def sides(self):   
#       print("Triangle has 3 sides")   
  

# class Pentagon(Polygon):   
#    def sides(self):   
#       print("Pentagon has 5 sides")    
  
# # Driver code   
# t = Triangle()   
# t.sides()   

# p = Pentagon()   
# p.sides()   
     
# Python program showing
# abstract base class work


# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass

# class Human(Animal):
#     def move(self):
#         print("I can walk and run")

# class Snake(Animal):
#     def move(self):
#         print("I can crawl")

# class Dog(Animal):
#     def move(self):
#         print("I can bark")

# class Lion(Animal):
# 	def move(self):
# 		print("I can roar")
		
# # Driver code
# R = Human()
# R.move()

# K = Snake()
# K.move()

# R = Dog()
# R.move()

# K = Lion()
# K.move()



# from abc import ABC, abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def fun(self):
#         pass

# class cat(animal):
#     def fun(self):
#         print('cat talk')

# class fish(animal):
#     def fun(self):
#         print('fish swim')

# class monkey(animal):
#     def fun(self):
#         print('monkey climb the tree')


# b = cat()
# b.fun()

# c = fish()
# c.fun()

# d = monkey()
# d.fun()


# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def mileage():
#         pass

# class bike(ABC):
#     @abstractmethod
#     def average():
#         pass

# class duster(car):
#     def mileage(self):
#         print('the mileage is 25km')

# class tesla(car):
#     def mileage(self):
#         print('the mileage is 20km')

# class Renault(car):
#     def mileage(self):
#         print('the mileage is 22km')

# class BMW(bike):
#     def average(self):
#         print('the average')

# a = duster()
# a.mileage()

# b = tesla()
# b.mileage()

# c = Renault()
# c.mileage()

# d = BMW()
# d.average()



'''Polymorphism'''
# ####poly with for loop
# class Car():
#     def bmw(self):
#         print('The german company')
#     def audi(self):
#         print('The French Company')
#     def Polo(self):
#         print('The UK company')

# class Truck():
#     def bmw(self):
#         print('The american company')
#     def audi(self):
#         print('The Italian company')
#     def Polo(self):
#         print('The Indian company')


# c = Car()
# t = Truck()
# for country in (c,t):                                         ###### country or use 'i'
#     country.bmw()
#     country.audi()
#     country.Polo()


######poly with inheritance
# class Car():

#     def gear(self):
#         print('Every vehicle has 5 gears')

#     def wheel(self):
#         print('car has 4 wheels')

# class BMW(Car):
#     def wheel(self):
#         print('BMW bike has 2 wheels')

# class Audi(Car):
#     def wheel(self):
#         print('Audi car has 6 wheels')

# c = Car()
# b = BMW()
# a = Audi()


# a.wheel()
# a.gear()

# c.wheel()
# c.gear()

# b.wheel()
# b.gear()


######poly with functions
# class Car():
#     def bmw(self):
#         print('The german company')
#     def audi(self):
#         print('The French Company')
#     def Polo(self):
#         print('The UK company')

# class Truck():
#     def bmw(self):
#         print('The american company')
#     def audi(self):
#         print('The Italian company')
#     def Polo(self):
#         print('The Indian company')


# def fun(car):
#     car.bmw()
#     car.audi()
#     car.Polo()

# c = Car() 
# t = Truck()

# fun(c)
# fun(t) 



# class animal():
#     def cat(self):
#         print('cat talk')

#     def dog(self):
#         print('dog bark')
    
#     def monkey(self):
#         print('climb')

# class bird():
#     def cat(self):
#         print('cats are friendly')
    
#     def dog(self):
#         print('dogs are loving')

#     def monkey(self):
#         print('climbing the tree')

# a = animal()
# b = bird()

# for i in (a,b):
#     i.cat()
#     i.dog()
#     i.monkey()



# class car():
#     def mileage(self):
#         print('the mileage is 15km')
    
#     def average(aelf):
#         print('the average is 10km')

# class suzuki(car):
#     def mileage(self):
#         print('the mileage is 20km')

# class bmw(car):
#     def mileage(self):
#         print('the mileage is 25km')

# a = car()
# b = suzuki()
# c = bmw()

# a.mileage()
# a.average()

# b.mileage()
# b.average()

# c.mileage()
# c.average() 



# class animal():
#     def cat(self):
#         print('cat talk')

#     def dog(self):
#         print('dog bark')
    
#     def monkey(self):
#         print('climb')

# class bird():
#     def cat(self):
#         print('cats are friendly')
    
#     def dog(self):
#         print('dogs are loving')

#     def monkey(self):
#         print('climbing the tree')


# def fun(animal):
#     animal.cat()
#     animal.dog()
#     animal.monkey()

# a = animal()
# b = bird()

# fun(a) 
# fun(b) 