# a = 2/0
# print(a)



# a = 2
# b = 0

# try:
#     c = a/b
#     print('The ans is: ',c)
# except:
#     print('You cant divide by zero')



# try:
#     a = int(input('Enter a number: '))
#     print('The Number is: ',a)
# except Exception:
#     print('Invalid')



# try:
#     a = int(input('enter a number: '))
#     print( a%2 == 0)
# except Exception() :
#     print('Invalid')



# def fun(x,y):
#     try:
#         r = x/y     
#         print('The answer is: ',r)
#     except ZeroDivisionError:
#         print('Invalid')
# fun(2,0)


# import sys

# list1 = [0,4,6]
# r = 0
# for i in list1:
#     try:
#         print('The first Entry is:',i)
#         r = 1/int(i)
        
#     except:
#         print('oops',sys.exc_info()[0],'occured')
#         print('Next Entry')
#         print()
#     print('The reciprocal r is',r)


# try:
#     x = int(input('Enter a number: '))
#     y = int(input('Enter a number: '))
#     r = x//y
#     print('The answer is: ',r)
# except ZeroDivisionError:
#     print('You are dividing by Zero')                              ### '//' hya madhe purn ans bhette  point madhe nahi bhetat


# try:
#     n =int(input('enter a no: '))
#     print(n)
# except:
#     print('Invalid')
# else:
#     print('Welcome')
# finally:
#     print('The end of execution')


# try:
#     a = int(input('enter a number: '))
#     print( a%2 == 0)
# except Exception():
#     print('Invalid')
# else:
#     print('I am else block')
# finally:
#     print('the end of code')



'''assert keyboard '''
# a = int(input('enter a number: '))
# b = int(input('enter a number: '))

# assert b != 0,'You are dividing by Zero'
# z = a/b
# print('The answer is',z)



# def first(var):
#     assert len(var) != 0,'The list is Empty'
#     return sum(var)

# scores1 = [20,23,45,67,89]
# print('The sum of scores1 is ',first(scores1))

# scores2 = []
# print('The sum of scores1 is ',first(scores2))


# a = 4
# b = 0
# print ("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"
# print (a / b)


# batch = [40, 26, 39, 30, 25, 21]
# c = 26
  
# for i in batch:
#     assert i >= 26, 'Batch is Rejected'
#     print (str(i) + 'is O.K') 