'''Python objects to json'''
# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))



# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.load(x)

# # the result is a Python dictionary:
# print(y["age"])

# import json



# class JLO():

#     def __init__(self):
#         self.data = ''

#     def config(self, json_file=''):
#         try:
#             with open(json_file, 'r') as json_data:
#                 self.data = json.load(json_data)
#         except Exception as e:
#             print('Can\'t read JSON config - ' + str(e))
#             exit(0)


# if __name__ == "__main__":
#     jlo = JLO()
#     jlo.config(json_file='Data_File.json')

#     print('Main')
#     print('================')
#     print(jlo.data)
#     print('================')
#     print(json.dumps(jlo.data,
#                      sort_keys=True, indent=4, separators=(',', ': ')))
#     print('================')