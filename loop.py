# There are basically two types of loop: 
# 1.) WHILE LOOP
# 2.) FOR LOOP
# Loop is an iteration process until any alternative process.

# # FOR LOOP: iterates over a sequence.
# names = ["Amos", "Elizabeth", "Mary"]
# for name in names:
#     print(f"Welcome {name}")
# num = []
# for x in range(1, 12):
#     print(x)
#     num.append(x)
# print(num)   

# num = []
# for x in range(1, 12, 3): # At step of 3
#     print(x)
#     num.append(x)
# print(num)    

# WHILE LOOP: executes a set of statement as long as a condition is true. It does not iterate over collection

# x = 1
# while x <= 10:
#     print(f'you are welcome to class {x}')
#     x += 1 # remember the increment, if not the loop will continue forever

# x = 10
# while x > 0:
#     print('I will not do it again', x)
#     x -= 1

# ussd = input('Enter ussd code: ')
# while ussd != "*131#":
#     ussd = input('Invalid Input!! Try Again: ')

# print('''
#         1. daily plan
#         2. weekly plan
# ''')  

# #  THE BREAK STATEMENT: this will stop the loop even if the statement is true

# x = 1
# while x < 5:
#     print(x)
#     if x == 3:
#         break
#     x += 1

# x = 10
# while x > 0:
#     print('I will not do it again',x)
#     if x == 5:
#         break
#     x += 1   

# std_name =[]
# x = 1
# while x <= 10:
#     name = input(f'ENter student name {x}, press "done" to quit')
#     if name == "done":
#         break
#     x += 1
#     std_name.append(name)
# print(std_name)

# name_list = []
# while True:
#     print('Type exit to quit')
#     name = input("Your name: ")
#     if name == 'exit':
#         break
#     name_list.append(name)
# print(name_list)    

# The continue statement: this can stop the current iteration and continue with the next

# x = 10
# while x > 0:
#     x -= 1
#     if x == 5:
#         continue
#     print('You are welcome', x)

# x = 10
# while x > 0:
#     x -= 1
#     age = input('Enter your age: ')
#     if int(age) < 18:
#         print('You are too young')
#         continue
#     print('take your ticket', x)

# The else statement: this helps to run