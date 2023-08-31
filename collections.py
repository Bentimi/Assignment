# # COLLECTIONS
    # """
    # LIST [] or list()
    # TUPLE ()
    # SET {}
    # DICT {key:value}
    # """
    # CLASS HAS BOTH FUNCTION AND PROPERTY CHARACTERISTICS

    # List : is a collection which is ordered, changeable, allowa duplicate value, amd the items are indexed

# my_list = list(('shade', 'dare', 'magret', 'femo'))

# my_list = ['shade', 'dare', 'magret', True, False, 12, 12.234, 'energy', 'enery', ['shade', 'dare', 'magret', 'femo']]

# print(my_list)
# print(my_list[9])
# print(my_list[9][-1])

# my_list = ['shade', 'dare', 'magret', True, False, 12, 12.234, 'energy', 'energy']

# print(my_list)
# print(my_list[-1][-1])

# # my_list[0] = 'Tikristi'
# # my_list[0:3] = ('Tikristi', 'Benjamin', 'Richard')
# my_list[0], my_list[-1] =  'Tikristi', 'Richard'
# print(my_list)

# Functions of a List

# # append() # Helps to add another item to the list
# my_list.append("Abimbade")
# print(my_list)

# # index() # Helps to identify the position of an item
# print(my_list.index('dare'))

# # clear() # Clears the item
# my_list.clear()
# print(my_list)

# # count() # counts the number of items in the list
# print(my_list.count('energy'))

# # extend() # merges another list together
# my_list.extend('Abimbade')
# print(my_list)

# # insert() # adds a new item to the list in the index
# my_list.insert(3, 'David')
#print(my_list)

# # pop() # deletes an index
# my_list.pop(2)
# print(my_list)

# # remove() # deletes the item
# my_list.remove('magret')
# print(my_list)

# # del # deletes the items
# del my_list
# print(my_list)

# sort()
# num = [1, 3, 4, 6, 2, 5]
# num.sort()
# print(num)

# list1 = ['shade', 'dare', 'magret', 'femo', 'Shade', 'Dare', 'Magret', 'Femo']
# # list1.sort()
# # list1.sort(key=str.lower)
# # list1.sort(reverse= True)
# print(list1)

# 2.) TUPLE: is a collection which is ordered, indexed, allows duplicate value and unchangeable

# my_tuple = ('shade', 'dare', 'magret', True, False, 12, 12.234, 'energy', 'energy')
# print(my_tuple)

# my_tuple2 = tuple(('shade', 'dare', 'magret', 'femo'))
# print(my_tuple2)

# my_tuple3 = ('rice',)
# print(type(my_tuple3))

# it_is_a_tuple = ("yam",) # or it_is_a_tuple = tuple(("yam"))
# print(type(it_is_a_tuple))

# it_is_not_a_tuple = ("yam")
# print(type(it_is_not_a_tuple))

# UNCHANGEABLE
# my_tuple[1] = "femi"
# print(my_tuple)
# count()

# amount = my_tuple.count('energy')
# print(amount)

# print(my_tuple.index('dare'))

# my_tuple3 = my_tuple + my_tuple2
# print(my_tuple3)

# # UNPACKING
# val = ("banana", "mango", "apple")
# (*val,) = ("banana", "mango", "apple")
# (val1, *val2) = ("banana", "mango", "apple")
# (val1, val2, val3) = ("banana", "mango", "apple")

# print(val)
# print(val1)
# print(val2)
# print(val3)
# print(*val)

# val[2] = "potato"
# print(val)


# # ZIP
# # sys function

# import sys

# name = input("Name: ")
# matric = input("Matric No: ")
# password = input("Password: ")
# username = input("Username: ")

# details = (name, matric, password, username)
# print(f"""
#         welcome {name}
#         press 'enter' to sign in or 1 to exit
# """)

# user = input("Option: ")
# if user != "1":
#     user_inp = input("Enter Username: ")
#     pass_inp = input("Enter Password: ")
#     if user_inp == username and pass_inp == password:
#         print("Start Test")
#     else: 
#         print("Wrong username or password")
# else:
#     print("bye bye")
#     sys.exit()  

# furniture = ['Table', 'Chair', 'Rack', 'Helf']
# price = [100, 50, 80, 40]
# total_amount_spent = 0

# for item, amount in zip(furniture, price):
#     print(f'{item}: ${amount}')
#     user = int(input(f"pay ${amount}: "))
#     if user == amount:
#         print(f"Take your item\n")
#         total_amount_spent += amount
#     else:
#         print("pay the required amount\n")
# print(f'You spent a total amount of ${total_amount_spent}')

# # Using enumerate() to loop through a list with tuple unpacking
# fruits = ["apple", "banana", "cherry"]
# for x, fruit in enumerate(fruits, start=1):
#     print(f"{x}. {fruit}".center(50))

# 3.) SET: A set is a collection which is unordered, unindex, unchangeable and does not accept duplicate values. # It is case sensitive.

# name = {"Habeeb", "Hamid", "Daniel", "Badmus", "Josh", "Sinmi", "Soliu", "Favour", "favour"}

# name1 = set(("Habeeb", "Hamid", "Daniel", "Badmus", "Josh", "Sinmi", " Soliu", "Favour"))

# newName = ('Shade', 'Dare', 'Dare')

# print((name))

# Properties A set can perform

# # add() # Adds an item to the set
# name.add('Mayowa')
# print(name)

# # update() # The variable must not have to be a set. It is better used in strings
# name.update(newName)
# print(name)

# # union() # should be added into a new syntax
# name1 = name.union(newName)
# print(name1)

# # remove()
# name1.remove("Dare")
# print(name1)

# # discard()
# name1.discard("Josh") # If the element does not exist it won't throw error
# print(name1)

# # pop() # discards/removes the last item in the set
# name.pop()
# print(name)
# import time
# for x in name:
#     print(x)
#     print('Wait for the next iteration')
#     time.sleep(2)

# del() # deletes
# name.pop()
# print(name)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9} # It rearranges it from smaller value to higher value
# set2 = {3, 5, 2}
# set3 = {2, 4, 5, 7, 8}

# print(set1)
# print(set2)
# print(set3)

# set4 = set1.union(set2)
# print(set4)

# intersect = set1.intersection(set2)
# intersect = set1.intersection(set2).intersection(set3)
# print(intersect)
# set1.intersection_update(set2)
# print(set1)

# set4 = set2.symmetric_difference(set1) # uncommon items
# print(set4)
# set2.symmetric_difference_update(set1)
# print(set2)

# set4 = set2.difference(set1)
# print(set4)

# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set2))

# DICTIONARY (dict): is a collection which is ordered, changeable but does not allow duplicate and unindexed   
# A dictionary is represented by the  {key : value} or dict((key=value)).

product = {'name':'Damilare', 'course':'Robotics', 'vehicle':'Toyota', 'passengers':60, 'color':'blue'}
# print(type(product))
# print(product['color']) # How to check the value at[] a key
# product['passengers'] = 10 # How to change the values at a particular key
# product['Location'] = 'Ogbomoso' # Adding of another variable
# product.update({'Size': 23, 'Location': 'Oyo'}) # Adding of another variable
# product.pop('color') # pop needs at least an argument for the operation to be perfomed
# product.popitem() # pops the last item in the dictionary
# print(product.get('passengers')) # To print the value of a key
# print(product) 

# print(product.keys())
# x = 1
# for key in product.keys():
#     print(f'Key {x}: {key}')
#     x +=1

# print(product.values())
# y = 1
# for value in product.values():
#     print(f'value {y}: {value}') 
#     y +=1  

# print(product.items())
# z = 1
# for item in product.items():
#     print(f'item {y}: {item}') 
#     z +=1   
    
# print(product.items())
# z = 1
# for key, value in product.items():
#     print(f'''
#             key {z}: {key} and value {z}: {value}
#     ''') 
#     z +=1   

# import time
# Q_and_A = {'B':'1. What is the capital of Oyo state? a.) Ogbomoso b.) Ibadan c.) Ilorin d.) Oyo',
#            'C':'2. What is the capital of Ogun state? a.) Ogbomoso b.) Ibadan c.) Abeokuta d.) Mowe'}
# score = 0
# for ans, ques, in Q_and_A.items():
#     print(ques)
#     user = input("Your Option: ")
#     if user.upper().strip() == ans:
#         score +=1/len(Q_and_A)*100

#     print('Please wait for the next question...')
#     time.sleep(1) 

#     print('Your total score is ', score)   


# studentData = {}
user = int(input("Enter the number of students to be registered: "))
# no = 1
# for x in range(user):
#     name = input(f'Name {no}: ')
#     mat_no = int(input(f"Mat_no {no}: "))
#     course = input(f"Course {no}: ")
#     details = (name, mat_no, course)
#     studentData['DETAILS'] = details
#     x =  [f'Student {no}:{details}']
#     print(studentData)
#     # x = {studentData{details}}
#     # studentData = details
#     # print(x)
#     no +=1

student_info = {}
total_score = {}
x = 1
for x in range(user):
    info = []
    name = input(f'Name {info}: ')
    mat_no = int(input(f"Mat_no {info}: "))
    course = input(f"Course {info}: ")
    info
    student_info[f"student"] 
    x +=1
    total_score.append()
