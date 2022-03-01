'''single inheritance'''

# class parent1():
#     def __init__(self):
#         self.name = 'Aditya'
#         self.age = 20

#     def call2(self):
#         print('the name is',self.name,'age is',self.age)

# class child1(parent1):
#     def __init__(self):
#         parent1.__init__(self)

#     def call1(self):
#         print(self.name,self.age)

# c = child1()
# c.call1()
# c.call2()



# class animal():
#     def __init__(self):
#         pass
#     def speak(self):
#         print('animal speaking')

# class dog(animal):
#     def __init__(self):
#         animal.__init__(self) 
#     def bark(self):
#         print('dog barking')

# d = dog()
# d.bark()
# d.speak()


# class first():
#     def __init__(self):
#         self.bikename = 'BMW'
#         self.bikeage = 5

# class second(first):
#     def __init__(self):
#         first. __init__(self)
#     def call1(self):
#         print(self.bikename,self.bikeage)

# c = second()
# c.call1()



# class first():
#     def __init__(self):
#         self.bikename ='BMW'
#         self.bikeage = 5
        
# class second(first):
#     def __init__(self):
#         first. __init__(self)
#     def call1(self):
#         print(self.bikename)

# class third(first):
#     def __init__(self):
#         first. __init__(self)
#     def call2(self):
#         print(self.bikeage)

# c = second()
# c.call1()

# d = third()
# d.call2()
        


# class first():
#     def __init__(self):
#         self.bikename ='BMW'
#         self.bikeage = 5
#         self.model = 'A1800'
        
# class second(first):
#     def __init__(self):
#         first. __init__(self)
#     def call1(self):
#         print(self.bikename)

# class third(first):
#     def __init__(self):
#         first. __init__(self)
#     def call2(self):
#         print(self.bikeage)

# class fourth(first):
#     def __init__(self):
#         first. __init__(self)
#     def call3(self):
#         print(self.model)

# c = second()
# c.call1()

# d = third()
# d.call2()

# e = fourth()
# e.call3()

'''Multiple Inheritance'''

# class father():
#     def __init__(self):
#         self.fathername = 'Maxgen'

# class mother():
#      def __init__(self):
#         self.mothername = 'Max'


# class child(father,mother):
#     def __init__(self):
#         father.__init__(self)
#         mother.__init__(self)

#     def show(self):
#         print('The father name is',self.fathername)
#         print('the mothername is',self.mothername) 

# c = child()
# c.show()


# class father():
#     def __init__(self):
#         self.fathername = 'Maxgen'

# class mother():
#     def __init__(self):
#         self.mothername = 'Max'

# class child(father,mother):
#     def __init__(self):
#         father.__init__(self)
#         mother.__init__(self)
#         self.gname = 'Python'

#     def show(self):
#         print('The father name is',self.fathername)
#         print('the mothername is',self.mothername) 

#     def fun(self):
#         print(self.gname)
# c = child()
# c.show()
# c.fun()


# class first():
#     def __init__(self):
#         self.bikename = 'BMW'

# class second():
#     def __init__(self):
#         self.bikeage = 5

# class third():
#     def __init__(self):
#         self.model = 'AT-1800'

# class child(first,second,third):
#     def __init__(self):
#         first. __init__(self)
#         second. __init__(self)
#         third. __init__(self)
#     def max(self):
#         print('the bikename is',self.bikename)
#         print('the bikeage is',self.bikeage)
#         print('the bikemodel is',self.model)

# c = child()
# c.max() 


# class first():
#     def __init__(self):
#         self.bikename = 'BMW'

# class second():
#     def __init__(self):
#         self.bikeage = 5

# class third():
#     def __init__(self):
#         self.model = 'AT-1800'

# class child(first,second,third):
#     def __init__(self):
#         first. __init__(self)
#         second. __init__(self)
#         third. __init__(self)
#     def max(self):
#         print('the bikename is',self.bikename)
#         print('the bikeage is',self.bikeage)
#         print('the bikemodel is',self.model)

# c = child()
# c.max() 


'''Multilevel '''

# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def getName(self):
#         return self.name

# class Child(Parent):
#     def  __init__(self,name,age):
#         Parent.__init__(self,name)
#         self.age = age
#     def getAge(self):
#         return self.age

# class Grandchild(Child):
#     def __init__(self,name,age,location):
#         Child.__init__(self,name,age)
#         self.location=location
#     def getLocation(self):
#         return self.location
# gc = Grandchild("Srinivas",24,"Hyderabad")
# print(gc.getName(), gc.getAge(), gc.getLocation())



# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
 

# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
 
#         Grandfather.__init__(self, grandfathername)
 

# class Son(Father):
#     def __init__(self,sonname, fathername, grandfathername):
#         self.sonname = sonname
 
#         Father.__init__(self, fathername, grandfathername)
 
#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
 
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()


'''encapsulation'''

# class gift:
#     def __init__(self):
#         self.price = 100
#         self.__discounted_price =50

#     def amount(self):
#         return self.price

#     def discount(self):
#         return self.__discounted_price


# t = gift()
# t.price = 1100
# t.__discounted_price = 70
# print(t.amount())
# print(t.discount())
        

# class Base:
#     def __init__(self):
#         self._a = 2
        
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)
 
# obj1 = Derived()         
# obj2 = Base()
# print(obj2._a)


# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "geeksforgeeks"
 
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
# obj1 = Base()
# print(obj1.a)


# class base:
#     def __init__(self): 
#         self.a = 'python is object oriental language'
#         self__c = 'python'

# class num(base):
#     def __init__(self):
#         base. __init__(self)
#         print('calling private member of base')
#         print(self.__c)

# obj1 = base()
# print(obj1.a)


# class base:
#     def __init__(self):
#         self.carname ='BMW'
#         self.__bikename ='R15'

# class fun(base):
#     def __init__(self):
#         base. __init__(self)
#     def show():
#         print('the carname')
#         print(self.__bikename)

# obj = base()
# print(obj.carname)


# class office:
#     def __init__(self):
#         self.employeename = 'shruti'
#         self.__employeesalary = '15k'

# class fun(office):
#     def __init__(self):
#         office.__init__(self)
#         print('the employeename')
#         print('_employeesalary')

# a = office()
# print(a.employeename)


# class speed:
#     def __init__(self):
#         self.speed = 10
#         self.__speed_limit = 20

#     def get_speed(self):
#         return self.speed

#     def get_speed_limit(self):
#         return self.__speed_limit

#     def set_speed_limit(self, new_speed_limit):              ######change private variable
#         return self.__speed_limit == set_speed_limit


# s = speed()
# s.speed = 100
# s.__speed_limit = 20
# s.set_speed_limit = 50
# print(s.get_speed(),s.get_speed_limit()) 
# print(s.set_speed_limit)



# class base:
#     def __init__(self):
#         self.employeename = 'shruti'
#         self.__employeexprience = '2yrs'

# class show(base):
#     def __init__(self):
#         base.__init__(self)
#         print('the employeename is',self.employeename)
#         print('the employeexprience is',self.__employeexprience)

# e = base()
# print(e.employeename) 


# class base:
#     def __init__(self):
#         self.employeename = 'riya'
#         self.__employeexprience = '2yrs'

#     def getemployeename(self):
#         return self.employeename 

#     def get__employeexprience(self):
#         return self.__employeexprience

# e = base()
# e.employeename = 'riya'
# e.__employeexprience = '2yrs'
# print(e.employeename)  