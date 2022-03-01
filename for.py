# list1 = [1,2,3,4,5]
# print(list1[0])
# print(list1[1])

# for i in 'maxgen':
#     print(i,end='/n')


# for i in range(1,10,2):
#     print(i)


# list1 = []
# list2 = []

# for i in range(1,21):
#     if i%2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)

# print('The Even No. is ',list1)
# print('The Odd No. is ',list2)


# # 2 x 1 = 2

# n = int(input('Enter a no. you want: '))

# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')                                  ### f = formatted string###


#1+2+3+4+....+100


# x =  ''
# for i in range(1,101):
#     a = str(i)
#     x = x + '+' + a
# print(x[1:]) 


# s = 0
# a = int(input('enter a no: '))
# for i in range(1,a +1,1):
#     s = s + i
#     print(s)


# for x in ('black','white','pink','blue','red'):
    
#     if x == 'pink':
#         break
#     print(x)
    


# for x in (1,2,3,4,5,6,7,8,9,10):
#     if x == 8:
#         break
#     print(x)


# for x in ('monday','tuesday','wendesday','thursday','friday','saturday'):
#     if x == 'thursday':
        
#         break
#     print(x)


# for x in ('monday','tuesday','wendesday','thursday','friday','saturday'):
#     if x == 'thursday':
#         continue 
#     print(x)


# for x in (1,2,3,4,5):
#     if x == 4:
#         continue
#     print(x)


''' Nested for '''

# list1 = [['mango',1],['banana',2],['strawberry',3],['apple',4],['chiku',5]]
# for i,j in list1:
#     print(i,'and count is',j)



# list1 = [['mango','pink',1],['banana','red',2],['strawberry','black',3],['apple','blue',4],['chiku','white',5]]
# for i,j,k in list1:
#     print(i,j,'and count is',k)



# list1 = [['red','yellow','green',1],['white','black','grey',2],['pink','red','yellow',3]]
# for i,j,k,l in list1:
#     print(i,j,k,'and count is',l)



# list1 = [110,121,125,150,157,165,175,181,190,195,200]
# for i in list1:
#     if i%5 == 0 :
#         print(i) 
#         if i == 190:
#               print(i)
    


# list1 = [1,2,3,4]
# list2 = ['red','yellow','pink','black']
# for i in list1:
#     print(i)
#     for j in list2:
#         print(j)


# list1 = [10,20,30,40,50]
# list2 = ['apple','chiku','strawberry','orange','banana']
# for i in list1:
#      for j in list2:
        #  print(i,j) 
  

  
# list1 = [1,2,3,4,5,6,7,8,9]
# for i in list1:
#     for j in list1:
#         if i + j == 10:
#             print(i,j)



'''Pattern printing'''

# for i in range(1,6):
#     for k in range(6-i-1):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('#',end=' ')
#     print()
        


# for i in range(1,6):
#     #  for k in range(6-i-1):
#     #     print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()



# for i in range(1,6):
#     for k in range(6-i-1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


''' reverse pattern'''  


# for i in range(6,0,-1):
#      for k in range(6,i,-1):
#          print(end=' ')
#      for j in range(1,i+1):
#         print('*',end=' ')
#      print()


# for i in range(6,0,-1):
#     # for k in range(6,i,-1):
#     #     print(end=' ')
#     for j in range(1,i):
#         print('*',end='')
#     print()
    
   
# n = int(input('enter a number '))
# list1 = []
# for i in range(n):
#     list1.append(int(input('enter a element ')))
    
# print(list1)
# for j in list1:
#     print(j)
 

# list1 = []
# list2 = []
# list3 = [1,2,3,4,5,6,7,8,9,10]

# for i in (list3):
#     if i%2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)

# print('The Even No. is ',list1)
# print('The Odd No. is ',list2)


'''# Program to find the sum of all numbers stored in a list
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)'''



# rows = int(input("Enter the number of rows: "))    
# for i in range(rows+1):  
#     for k in range(rows-i-1) :
#          print(' ',end='')
#     for j in range(i):  
#         print(i, end=' ')   
     
#     print(" ")  


# rows = int(input("Enter the number of rows: ")) 
# for i in range(1,rows+1):  
# 	for k in range(rows-i-1) :
# 	    print(' ',end='')
#     for j in range(i):  
# 	    print(i, end=' ')  # print number  
#     print(" ")