'''4 types of functions

1. Positional
2. keyword
3. Default
4. variable Length '''


'''Positional'''

# def first(name,age):
#     print(name)
#     print(age)

# first('Maxgen', 12)   



# def second(carname,model):
#     print(carname,model)

# second('City', 'TW-180')


## def new (flowername,colour):
#     print(flowername,colour)

# new('rose','red')



## def first(studentname,classname):
#     print(studentname,classname)
# first('riya','fifth')


# def new(email,password):
#     print(email,password)
# new('shrutis@gmail.com','1234')

'''Keyword'''

# def first(name,age):
#     print(name, age)

# first(name='Maxgen', age=12)



# def fun(class1,div):
#     print(class1,div)

# fun(div='A',class1='FY')


# def fun(flowername,colour):
#     print(flowername,colour)

# fun(flowername='rose',colour='pink')


# def first(carname,model):
#     print(carname,model)
# first(carname='city',model='AT 160')


# def second(project,time):
#     print(project,time)

# second(project='sale',time='20')


'''**kwargs in keyword '''
# def num(**kwargs):
#     print(kwargs)
# num(salary = 10000, city ='pune', name = 'maxgen',age = 20)


# def var(**kwargs):
#     print(kwargs)
# var(place ='maxgen',city = 'pune',name = 'python',salary = 15000, age = 18)



'''default'''

# def first(name,age=12,city='Pune'):
#     print(name,age)
#     print(city)

# first('Maxgen','14','nashik')



# def second(project,time,day='20'):
#     print(project,time,day)

# second('sale','2days')



'''variable length or Arbitary Arguments'''

# def car(*name,model):
#     print(name)
#     print(model)
# car('city','verna','Q7','Maybach',model='A8')


# def new(project,*title):
#     print(project)
#     print(title)
# new('sales','marketing','A25','A1800')
  

# def new(sports,*names):
#     print(sports)
#     print(names) 
# new('cricket','football','hockey','kho-kho')

'''*args in variable length '''
# def num (*args):
#     print(args)
# num('a','b','c',1,2,3,4,5)


# def num (*args):
#     print(*args)
# num('a','b','c',1,2,3,4,5)  


'''recursive function'''


# def factorial (x):
#     if x == 1:
#         return 1
#     else :
#         return (x*factorial(x-1))
# num = 5
# print('the factorial of', num,'is', factorial(num))


# def Recur_facto(n, a = 1): 
    
#     if (n == 0): 
#         return a 
    
#     return Recur_facto(n - 1, n * a) 
# print(Recur_facto(6))                                       ########logic of this numerical factorial of 6 [6*5*4*3*2*1=720]


# def factorial(n):
#     if n == 1:
#         print(n)
#         return 1
#     else:
#        print(n,'*',end=' ')
   
#     return n * factorial(n-1)  

# factorial(3)


