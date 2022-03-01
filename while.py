# n = int(input('enter a number: '))
# s = 0
# i = 1
# while i <= n:
#     s = s + i
#     print(s) 
#     i = i + 1


    
# n = int(input('Enter a no. you want: '))
# i = 1
# while i <= 10:
#     print (f'{n} x {i} = {n * i}') 
#     i = i + 1


    
# list1 = []
# list2 = []
# i = 1
# while i <= 10:
#     if i%2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
#     i = i + 1
# print('The Even No. is ',list1)
# print('The Odd No. is ',list2)



# n = int(input('enter a number '))
# i = 1 
# while i <= n:
#     if  i%2 == 0:
#         print(i,'even number ')
#     else:
#         print(i,'odd number ') 
#     i = i + 1



# count = 0
# while count < 5:
#     print('I love trakking')
#     count = count + 1

# print('    shruti     ')
   

# x =  ''
# i = 1
# while i<=100 :
#     a = str(i)
#     x = x + '+' + a
#     i = i + 1

# print(x[1:])



# n = int(input('enter a number '))
# i = 1
# list1 = []
# while i<=n:
#     list1.append(int(input('enter a element ')))
#     i = i + 1
# print(list1)

# j = 0
# while j < len(list1):
#     print(list1[j])
#     j = j + 1
    

# n = int(input('enter a number '))
# i = 1 
# while i <= n:
#     if i == 5:
#         break
#     print(i)
#     i = i + 1



# list1 = ['monday','tuesday','wendesday','thursday','friday','saturday']
# j = 0
# while j <= len(list1):
#     if j == 4: 
#         continue
#     j = j + 1
#     print(list1[j])

    
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i = i + 1



# i = 0
# while i < 6:
#   i += 1                                              
#   if i == 3:
#     break
#   print(i)


''' else block'''

# n = int(input('enter a number '))
# i = 1
# while i <=n:
#     i = 1 + i
# else :
#     print('i is no longer')


# list1 = ['black','pink','blue','red']
# s = 'red1'
# i = 0
# while i < len(list1):
#     if list1[i] == s:
#         break
#     print(list1[i])
#     i = i + 1
# else :
#     print('Invalid')



# n = int(input('enter a number '))
# i = 1
# while i <= n:
#     if i == 6:
#         break
#     print(i)
#     i = i + 1
# else :
#     print('Invalid')


'''List Comprehension'''

# new = [i for i in range(1,11) if i%2 == 0]
# print(new)


# list1 = ['monday','tuesday','wendesday','thursday','friday','saturday']
# new = [i for i in list1 if 't' in i]
# print(new)


# new = [i for i in range(1,20) if i%2 != 0]
# print(new)


# letters = [ letter for letter in 'Python' ]
# print( letters)


# x = {'chrome': 'browser', 'Windows': 'OS', 'C': 'language'}  
# print(x['Windows'])  



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != 'banana' else 'orange' for x in fruits]
# print(newlist)


'''dictionary Comprehension'''

# dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# new = {(k,v) for k,v in dict1.items() if k > 2 and k%2 != 0}
# print(new)


# k = [1,2,3,4,5]
# v = ['a','b','c','d','e']
# new = {k:v for k,v in zip(k,v)}
# print(new)


# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
# new = {k:v for (k,v) in zip(state, capital)}
# print(new)


# input = [1,2,3,4,5,6,7]
# dict_using_comp = {var:var ** 3 for var in input if var%2 != 0}
# print(dict_using_comp) 