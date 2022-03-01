import re

# #Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match") 


# import re
# txt = 'the rain in pune'
# x = re.findall('[a-h]',txt)                  ###Find all lower case characters between "a" and "m" :
# print(x)


# import re 
# txt = 'capacity is 50kg'                    ###Find all digit characters:
# x = re.findall('\d',txt)
# print(x)

# import re
# txt = 'hello class'                          ###Search for starts with 'h'and an end with 'o' 
# x = re.findall('h...o',txt)
# print(x)

# import re
# txt = 'hello i am shruti'                                  
# x = re.findall('^hello',txt)
# if x:
#     print('the string is with hello word') 
# else:
#     print('no match')

# import re 
# txt = 'hello i am shruti'
# x = re.findall('shruti$',txt)
# if x:
#     print('the string is end with shruti')
# else:
#     print('no match')

# import re 
# txt = 'the rain in pune falls mainly in pune'
# x = re.findall('falls|string',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'the bird in balcony'
# x = re.findall('\Athe',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re 
# txt = ' the rain falls slowly'
# x = re.findall(r'\bain',txt)
# if x:
#     print('match')
# else:
#     print('no match')


# import re 
# txt = 'the rain falls slowly'
# x = re.findall(r'ain\b',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'the rain falls slowly'
# x = re.findall(r'\Bain',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re 
# txt = 'the rain falls slowly'
# x = re.findall(r'ain\B',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re 
# txt = 'the rain falls slowly at 1pm'
# x = re.findall('\d',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re 
# txt = 'the rain falls slowly' 
# x = re.findall('\D',txt)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'butterflies are beautiful'
# x = re.findall('\s',txt)
# print(x)
# if x:
#     print('match')
# else: 
#     print('no match')

# import re
# txt = 'butterflies are beautiful'
# x = re.findall('\S',txt)
# print(x)
# if  x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'butterflies are beautiful'
# x = re.findall('\w',txt)
# print(x)
# if x:
#     print('match')
# else :
#     print('no match')

# import re
# txt = 'butterflies are beautiful'
# x = re.findall('\W',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'rain falls slow'
# x = re.findall('slowly\Z',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt = 'rain falls slowly at evening'
# x = re.findall('[arn]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at evening'
# x = re.findall('[a-n]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at evening'
# x = re.findall('[^arn]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at 4pm'
# x = re.findall('[0123]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at 9'
# x = re.findall('[0-9]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at 10:15'
# x = re.findall('[0-5][0-9]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='rain falls slowly at EVENING'
# x = re.findall('[a-zA-Z]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')

# import re
# txt ='Tea + bread'
# x = re.findall('[+]',txt)
# print(x)
# if x:
#     print('match')
# else:
#     print('no match')
