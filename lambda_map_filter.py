'''Lambda'''
#Syntax
#  = lambda a , b : a + b


# c = lambda a,b : a+b
# print(c(10,20))


# a = lambda c ,d ,e : c * d * e
# print(a(10,5,20)) 


# x = lambda a : a + 10
# print(x(5))


# x = lambda a,b: a * b
# print(x(5,10))


# x = lambda a,b,c : a + b + c 
# print(x(10,15,20))


'''map'''

# def addition(x):
#     return x + x

# num = [20,40,30,15,50]
# new = list(map(addition, num))
# print(new)


# num = [20,40,30,15,50]
# new = list(map(lambda x : x + x , num))
# print(new)


# a = [20,60]
# b = [50,100]
# var = list(map(lambda a,b:a + b,a,b))
# print(var) 

# a = [20,30]
# b = [10,40]
# num = list(map(lambda a,b:a*b, a,b ))
# print(num)


# a = [50,100]
# b = [60,30]
# num = list(map(lambda a,b :a/b,a,b ))
# print(num)


'''filter'''

# def num (a):
#     return a%2 == 0 
# list1 = [1,2,3,4,5,6,7,8,9,1]
# var = list(filter(num, list1))
# print(var)



# list1 = [1,2,3,4,5,6,7,8,9,10]
# var = list(filter(a:a%2==0, list1))
# print(var) 



# var = list(filter(lambda a:a%2==0, range(1,20)))
# print(var)



# def fun (a):
#     return a%2 != 0
# list1 =[10,15,20,25,30,35,40,45,50,55,60]
# num = list(filter(fun,list1))
# print(num)



# list1 =[10,15,20,25,30,35,40,45,50,55,60]
# num = list(filter(lambda a:a%2 != 0,list1))
# print(num)



# num =list(filter(lambda a:a%2 != 0,range(10,20)))
# print(num)

'''reduce'''

# from functools import reduce
# def sum(a,b):
#     return a + b


# list1 = [4,24,12,59,60]
# new = reduce(sum,list1)
# print(new)


# from functools import reduce

# def sum(a,b):
#     return a + b
# print(reduce(sum,[4,24,12,59,60]))



# from functools import reduce

# list1 = [10,5,20,50,30]
# new = reduce(lambda a , b: a if a > b else b,list1)
# print(new)


# import functools
# list1 = [10,5,20,50,30]
# print(functools.reduce(lambda a , b: a if a > b else b,list1))


# from functools import reduce
# def sum(a,b):
#     return a+b
# print(reduce(sum,[10,20,15,11,22]))


# from functools import reduce
# def sub(a,b):
#     return a-b
# print(reduce(sub,[10,20,15,11,22]))


# from functools import reduce
# list1 = [10,12,14,15,20,21]
# print(reduce(lambda a , b : a if a > b else b,list1))
