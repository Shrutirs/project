# age=20
# print(age)

# a = 10                                         ####integer
# print(type(a))

# a = 'Maxgen'                                   ####string
# print(a)

# a = 3.14                                       ####float
# print(type(a))

# z = 1.66666
# print(z)
# print(type(z))

# t = True                                       ####bulley
# print(t)
# print(type(t))

# a = int(input('Enter a no.:'))
# b = int(input('Enter a 2nd no:'))


# a = 10
# b = 20
# c = a + b
# print(c)

# a = 20
# print(type(a))

# a = 'pune'
# print(a)

# a = 0.4
# print(type(a))

# t = False
# print(t)
# 
# a = 15
# b = 20
# c = a + b
# print(c)


'''Datatypes'''

#string

# a = 'maxgen'
# b = 'Maxgen'
# c = 'MAXGEN'


# print(a.capitalize())

# print(b.casefold())

# print(a.upper())

# print(c.lower())

# print(c.isupper())

# print(b.islower())

# print(a.isnumeric())



# '''replace method in string'''

# a = '13.56522,45'
# x = a.replace('.','')
# y = x.replace(',', '')
# print(x)
# print(y)



#2 immutable
# a = 'pune'
# b = 'Pune'
# c = 'PUNE'

# print(a.capitalize())

# print(b.casefold())

# print(c.lower())

# print(c.casefold())

# print(c.islower())

'''list'''

# list1 = [1,2,3,5,6,7,8,9,10,'a','b','red']        ###mutable
# list1.insert(3,4)

# list1.append('blue')                                      ####add single veriable at a time

# list1.append(20)

# list1.extend(['blue',20])                                  ####add multiple veriable at a time

# list1.remove('b')                                          ####remove element by direct veriable
# list1.remove(10)

# list1.pop(8)                                                #### remove veriable by index no
# list1.reverse()

# list2 = [10,2,50,35,67,23]
# list2.sort()
# print(list2)

# 2
# list1 = [1,2,3,4,5,7,8,9,10,'a','b','black']
# list1.insert(5,6)
# list1.append('red')
# list1.extend(['red','white'])
# list1.remove('black')
# list1.pop(9)

# print(list1)


'''Tuple'''

# tuple1 = (1,2,3,4,5,6,7,8,9,10) #immutable
# tuple1 = 1,2,3,4,5,6,7,8,9,10 #immutable


# print(tuple1[2:9])

# print(tuple1[2:9])

# print(tuple1[:9])

# print(tuple1[2:])

# print(tuple1[1:9:2])

# print(tuple1[::3])

# print(tuple1[-6:-1])

# print(tuple1[-10:])

# print(tuple1[::-2])                                 ####subtract no by -1

# print(tuple1[-10::2])

#2
# tuple1 = (10,20,30,40,50,60,70,80,90,100)
# print(tuple1[2:5])
# print(tuple1[1:8])
# print(tuple1[4:])
# print(tuple1[:6])
# print(tuple1[2: : 2])
# print(tuple1[:9:2])
# print(tuple1[-10:-3])
# print(tuple1[-8:-2:2])



# list1 = ['red','green','violet','orange','yellow']
# print(len(list1))
# list1.insert(1,'white')

# list1.remove('orange')
# list1.insert(3,'brown')
# list1.sort()

# print(list1.count('violet'))

'''set'''

#set1 = {1,2,3,4,5} ##mutable unordered
# set2 = {6,7,1,2}
# set1.add(10)
#set1.update('red')
#set1.update(['red']) 
# set1.remove(5)
# set1.pop()
# set1.pop()
# s = set1.union(set2)
#print(set1) 

# set1 = {10,20,30,40,50}
# set1.add(60)
# set1.update('black')
# set1.update(['black'])
# set1.remove(20)
# set1.pop()
# print(set1)


'''  dictionary'''
# dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'} ##mutable
# print(dict1.keys())
# print(dict1.values())

# dict1.update({6:'f'})
# dict1[2] = 'k' 

# dict1.pop(3)

# print(dict1.items())

# dict2 = dict1.copy()
# print(dict1)


# ''dict example''
# dict1 = {1:'rina',2:'ritika',3:'priya',4:'rita'}
# print(dict1.keys())
# print(dict1.values())
# dict1.pop(3)
# dict1[3] = 'diya'
# dict1.update({5:'dipa'})
# print(dict1)


# ''set example''
# set1 = {1,2,3,4,'a','b','c','d','e'}
# set1.add(7)
# set1.update('z','x','v')
# set1.remove('a')
# set1.pop()
# print(set1)

# 6
# a = 1,2,3,4,5
# print(type(a))

#
# Tuple2= "White",10,"Green"
# a,b,c=Tuple2
# print(a)

#
# Tuple3=(1,2,3,4,5,6,7,8,9)
# print(Tuple3[2:5])
# print(Tuple3[:4])
# print(Tuple3[3:])

#
# Tuple4=(10,20,30,40,50)
# print(Tuple4[-1])
# print(Tuple4[-4:-1])
#
# List1 = [4,3,9,7]

# List1[1:4] = [2,8,6]
# print(List1)

#
# List2=['xyz','Zyx','yxz']
# print(max(List2))

#
# a,b,*c,d,e=[1,2,3,4,5,6]
# print(c)

#
# Set1={"Lion","Tiger","Zebra"}
# Set1.update(["Rhino"])
# print(Set1)

#
# Set2={"Lion","Tiger","Zebra"}
# y={"Rhino"}
# Set2.update(y)
# print(Set2)

#
# d = {}

# print(type(d))


# list1 = []

# n = int(input('Enter a element you want'))

# for i in range(n):
#     list1.append(int(input('Enter a no.: ')))

# for i in list1:
#     print(i)



Tuple1= ("Black",[1,2,3],[4,5,6])

print(Tuple1[1][1])