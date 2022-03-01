# def f():
#     print(s)
 
# s = "I love Geeksforgeeks"
# f()



# def f():
#     s = "Me too."
#     print(s)
 
# s = "I love Geeksforgeeks"
# f()
# print(s)



# def f():
#     global s
#     print(s)

#     s ='Me too.'
#     print(s)

# s = 'I love Geeksforgeeks.'
# f()
# print(s)



# a = 1
# #  Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a)
 
# #  Variable 'a' is redefined as a local
# def g():   
#     a = 2
#     print('Inside g() : ', a)
 
# #  Uses global keyword to modify global 'a'
# def h():   
#     global a
#     a = 3
#     print('Inside h() : ', a)
 
# #  Global scope
# print('global : ',a)
# f()
# print('global : ',a)
# g()
# print('global : ',a)
# h()
# print('global : ',a)


# def f():
#     x = "Python"
#     print(x)
#     print(s)
# s = "Tutorialspoint"
# print(s)
# f()



# z = 25
# def func():
#     global z
#     print(z)
# z=20
# func()
# print(z)


# def func(x, y):
#     global a
#     a = 45
#     x,y = y,x
#     b = 33
#     b = 17
#     c = 100
#     print(a,b,x,y)
# a,b,x,y = 3,15,3,4
# func(9,81)
# print (a,b,x,y) 