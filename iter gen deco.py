'''Iterator'''

# list1 = [1,2,3,4,5,6,7,8]
# var = iter(list1)

# print(var.__next__())
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))
# print(next(var))


# list1 = [10,20,30,40,50,60]
# var = iter(list1)
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())
# print(var.__next__())


# a = 'Maxgen'

# d = iter(a)

# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())


# list1 = [1,2,3,4,5,6,7,8,9,10]
# var = iter(list1)
# while True:
#     try:
#         item = next(var)
#         print(item)
#     except StopIteration:
#         break


# num = ('apple','banana','kiwi',)
# var = iter(num)
# while True:
#     try: 
#         item = next(var)
#         print(item)
#     except StopIteration:
#         break 


'''Generator'''

# def allow():
#     a = 'Maxgen'
#     yield a

#     b = 'Hello'
#     yield b

#     c = 'Welcome'
#     yield c

# obj = allow()
# print(next(obj))
# print(next(obj))
# print(next(obj))


# list = [1,2,3,4,5,6,7]   
# # List Comprehension  
# z = [x**3 for x in list]    
# # Generator expression  
# a = (x**3 for x in list)  
# print(a)                                          ####<generator object <genexpr> at 0x000001C3AD409510>==That's the string representation of a generator object. You need to iterate the generator to get values out of it
# print(z)         


# def allow(a):
#     for i in range(1,11):
#         yield a * i
#         i+=1
# for i in allow(5):
#     print(i)


# def simple():  
#     for i in range(10):  
#         if(i%2==0):  
#          yield i   
# for i in simple():  
#     print(i)  



# def multiple_yield():  
#     str1 = "First String"  
#     yield str1  
  
#     str2 = "Second string"  
#     yield str2  
  
#     str3 = "Third String"  
#     yield str3  
# obj = multiple_yield()  
# print(next(obj))  
# print(next(obj))  
# print(next(obj))  


# list = [1,2,3,4,5,6,7]   
# z = [x**3 for x in list]    
# a = (x**3 for x in list)  
  
# print(a)  
# print(z)  



# list = [1,4,8,10]  
  
# z = (x**3 for x in list)  
  
# print(next(z))  
# print(next(z))  
# print(next(z))  
# print(next(z))  



'''Decorator'''
''' Decorators are used to add some design patterns to a function without changing its structure.
Decorators generally are defined before the function they are enhancing.
To apply a decorator we first define the decorator function.
Then we write the function it is applied to and simply add the decorator function above the function
 it has to be applied to. For this, we use the @ symbol before the decorator.'''

# def first(msg):
#     print(msg)

# first('Hello')

# second = first
# second('Hello')



# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# def ordinary():
#     print("I am ordinary")

# new = make_pretty(ordinary)
# new()



# def our_decorator(func):
#     def function_wrapper(x):
#         print(" Before calling " + func.__name__)
#         func(x)
#         print(" After calling " + func.__name__)
#     return function_wrapper

# @our_decorator
# def Riya(x):
#     print("Hi, Riya has been called with " + str(x))

# Riya("Harry")




# def our_decorator(func):      # func is function to be decorated by decorator
  
#   def wrapper(x):             # x is parameter which is passed in func
#     if x%2==0:
#       return func(x)
#     else:
#       raise Exception("number should be even")
#   return wrapper

# @ our_decorator
# def func(x):                 # actual function 
#   print(x,"is even")
# func(2)
# func(1)

# ' if you do not want to use @'
# func=our_decorator(func)
# func(2)
