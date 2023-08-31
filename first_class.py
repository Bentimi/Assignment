# this is to print a message on the screen
# print("Welcome to Python class")
# Comments: single-line commenting(#) and multi-line commenting("""...""")

# Variables Declaration
"""
BASIC RULES IN VARIABLE DECLARATION.
1. variables should be more descriptive
2. python is case sensitive
3. a vaiable can not start with a number
4. it can only contain alphanumeric character and underscore

MULTIPLE VARIABLE DECLARATION
x,y,z = 20, 40, 35.67
x = 20
y = 40
x, y = 20, 40
print(x)
print(y)
print(x+y+z)

Types of Casing in variable declaration
FirstNameOfTheBoy = "pascal casing"
firstNameOfTheBoy = "camel casing"
first_name_of_the_boy = "snake casing"
"""

# name_of_student = "Yemi"
# address = "Ogbomoso"
# state = "Oyo State"
# age = "78"
# score = "89"
# age_text = str(age)
# print("My name is "+ name_of_student +", I live in " + address +" " + state +" " + " " + age +" " + score)

# Multiple Variable Declaraton:
# """"
# firstName, lastName, age = "Emma", "Arise", 12
# print("My name is " + firstName +" " + lastName +", I am " + str(age) +" years old")
# print(f"My name is {firstName} {lastName}, I am {age} years old")
"""
firstName = input("Firstname: ")
# print(firstName)
course = input("Enter your course: ")
age = int(input("Enter your age: "))
# as integer age = int(input("Enter your age: "))
# as string age = input("Enter your age: ")
print(f"My name is {firstName}, I am studying {course} at SQI, I am {age} years old.")
"""
# """


# Assignments:
#Types of concatenation

"""
ANSWER:
There are two types of concatenation which are;
Format Method
f string Method
1.) Partioned Concatenation: this can contain a mixture of PDSs, PDSEs, and UNIX directories in any order.

2.) Sequential Concatenation: this can be done by using the "+" operator to concatenate or join sequences of same type

"""
#Types of variables
"""
ANSWER:
Types of datatype in Python:
-Numeric: this deals with int(singled integers); long(long integers, they can also be represented in octal and hexadecimal); float(floating point real values); complex(complex numbers)
-Text Type
-Sequence Type(Python list, Pyhton tuple, Python range)
-Boolean : True or False statement or condition
-Set
-Dictionary
"""

# Types of Variables
# Global and Local Variables
# val1 = 10
# val3 = 50
# val2 = 30

"""
function declaration
function definition
function invocation
"""

"""
def addition():
    # This function performs an addition operation
    # global val2
    val2 = 5
    result = val1 + val2
    # return result
    print(f"Your answer is {result}")

def subtract():
    # This function performs substraction operation
    val2 = 5
    ans = val1 - val2
    print(f"Your answer is {ans}")

addition()
subtract()
"""
# Types of Datatypes in Python
# -Numeric: this deals with int(singled integers); long(long integers, they can also be represented in octal and hexadecimal); float(floating point real values); complex(complex numbers)
# -Text Type : Strings
# -Sequence Type(Python list, Pyhton tuple, Python range)
# -Boolean : True or False statement or condition

# Example of Boolean
# val = True # True or False
# print(val)

# -Set : {1, 2, 3, 4, 5, 6}
# val = {1, 2, 3, 4, 5, 6}
# val = {"Orange", "Mango", "Banana"}
# print(type(val))

# Frozenset
# Frozenset Example : ({1, 2, 3, 4, 5, 6})
# _my = frozenset({"Orange", "Mango", "Banana"})
# print(_my)

# -Dictionary : Mapping
# # Examples of Dictionary
# val = {"Name":"Tikiristi", "Occupation":"Data Scientist", "Address":"Ogbomoso", "Age":30}
# # print(val)
# # print(type(val))
# # print(val.keys()) # such as Name...
# # print(val.values())# such as Tikiristi...
# # print(val.items())# such as ([('Name', 'Tikiristi')...]}

# # for key in val.keys():
# #     print(key)

# for x,y in val.items():
#     print(f"{x}:{y}")

#  # -Bytes : b"Hello"
# # #Example of bytes
# # val = b"Hello"# For string
# val = bytes(50)
# print(val)

# -Bytearray
# val = bytearray(5)
# x = bytearray(50)
# x = memoryview(bytes(5))
# print(x)

# -Binary Types : E.g bytearray, bytes...


"""
# Datatypes Conversion
# To check for datatypes use type() function

name = "Yemi"
score = 7.9
age = 45
# print(type(age))
# print(type(score))

# # str() to convert to string type
# print("Type before conversion", type(score))
# print("Type after conversion", type(str(score)))

# # int() to convert to integer type
# print("Type before conversion", type(score))
# print("Type after conversion", type(int(score)))
# print("Actual value after conversion", int(score))

# #  float() to convert to float type
# print("Type before conversion", type(age))
# print("Type after conversion", float(age))

# #  bytes() to convert to bytes type
# print("Type before conversion", type(name))
# print("Type after conversion", type(bytes(name, "utf"))) # "utf-8", "utf-16" and "utf-32" --- Encoding Techniques
# print("Actual value after conversion", bytes(name, "utf"))

# # Conversion/Decoding from Byte to String
# val = bytes(name, "utf")
# n_val = str(val) # Not working
# print(val.decode())

# set() to convert to set type
# tuple() to convert to tuple type
# dict() to convert to dict type
"""


# #Examples of Datatypes in Python
# String (str): ("John", "False", "17", "5.9" "this is my first python class")
# test = "Johnson" #String
# t1 = 5 #Int
# test2 = 4.6 #Float
# val = [1,2,3,4, "one", "two"] #List
# test3 = tuple(val) #Tuple
# #val2 = range(1,10) #Range

#  #print(val2)

#Counting in interval of 2
# val = range(1,11,2)
# for x in val:
#      print (x)

# val = range(1,11)
# for x in val:
#      print (x)

# for x in range(1,111):
#      print (x)

# if type(test) == str:
#     print("They are same")
#  else 
# print("They are different")   

# """
# SurName = "Ogunkunle"
# firstName = "Benjamin"
# middleName = "Timileyin"
# homeTown = "Saki"
# state = "Oyo State"
# country = "Nigeria"
# print("I am "+ SurName + " " + firstName+ " "+ middleName + " by name." " I am a native of " + homeTown +", " + state +", " + country +".")
# """

"""
() - Tuple
[] - List
{} - Dictionary and Set
"""

#python variables
# bottle = ["Water", "salt", "stone"]
# print(type(bottle))

"""
MULTIPLE VARIABLE DECLARATION
x,y,z = 20, 40, 35.67
x = 20
y = 40
x, y = 20, 40
print(x)
print(y)
print(x+y+z)
"""

"""
Assignment:

How to convert bytes to sting
Grading system 
"""


#"""
    # # Types of Operators in Python
    # 1.) Arithmetic Operator: +, -, /, *, %, //, **

    # Example
# fval = 5
# sval = 2
# print(f'for addition {fval + sval}')
# print('for subtraction ' + str(fval - sval))
# print('for multiplication' + str(fval * sval))
# print('for division'+ str(fval / sval))
# print('for modulus '+ str(fval % sval)) # Displays the remainder only
# print('for exponentiation '+ str(fval**2))
# print('for floor division '+ str(fval // sval)) # Displays the whole number instead of the remainder


    # 2.) Assignment Operator: =, +=, -=, /=, *=, //=, %=, **=, etc.
    # 3.) Comparison Operator: ==, !=, >, <, <=, >=
    # 4.)Logical Operator: and, or, not

    # # if money != "yes":
    # # print("I won't be around")
    # # else:
    # # print("I would be around")

    # 5.) Identity operator: is, is not
    # 6.) Membership Operators: in, not in

    # names =

    # 7.) Bitwise Operator: &, |, ^, infinity sign  , <<,>>
#"""

# x = int(input("Enter a positive integer: "))

# if x%2 == 0:
#     print(f'{x} is even.')
# else:
#     print(f'{x} is odd.')

# val = int(input('Your val: '))
# res = val%2

# if res > 0:
#         print(f"{val} is an odd number")
# else:
#         print(f"{val} is an even number")

# val = int(input('Your val: '))
# res = val/2
# if type(res) == float:
#         print(f"{val} is an odd number")
# else:
#         print(f"{val} is an even number")

"""
Assignment:
Creating USSD Code
*312#
"""

# CONDITIONAL STATEMENT
# var = "tfare"
# if var == "tfare":
#     print("I'm coming to school")
# else:
#     print("I'm not coming")

# ussd = '*310#'
# user = input("Enter *310# as ussd code: ")
# if user == ussd:
#     print("""
#                 Welcome
#           1. My offer
#           2. Data Plan
# """)
#     user = input("Choose your option: ")
# if user == '1':
#     print("""
#                 My offer
#           1. #2000 for 3gb
#           2. #500 for 1gb
#           22. back
# """)
# else:
#     if user == '22':
#        print("""Welcome
#           1. My offer
#           2. Data Plan""")
# elif user == '2':
#     print("""
#                 Data Plan
#           1. Daily plan
#           2. Weekly Plan
#           3. Monthly plan
#           4. Social Bundle
# """
# )
# else: 
#    print("Invalid input")


# PYTHON STRINGS
# Every class element has property and function
                        # 0    1    2   3    4    5         -- indexing
name = 'sunday'    #== ['s', 'u', 'n', 'd', 'a', 'y']

# FUCTIONS
# Parametized and Non-parametized Functions
# print(len(name))    # len is used to know the total number of items, elements or characters
# print(name[-3])     # negative indexing    
# print(name[3:5])    # slicing
# print(name[3:])    # slicing
# print(name[:3])    # slicing

# String Methods / Function

# comment = "commented that This is a python class. It started last week and still continue through this week, the number of people in this class is"
# print(comment.startswith("commented")) # for confirmation
# print(comment.endswith("class is"))

# user = input("Input your Gmail: ")
# if user.endswith("gmail.com"):
#     print("Valid email address")
# else: 
#     print("Invalid email address")

# Strip strips spaces before and at the end of the string(white spaces)

# print('length before strip is', len(comment))
# print('length before strip is', len(comment.strip()))

# user = input("USSD Code: ")
# if user.strip() == '*310#':
#     print("Welcome")
# else:
#     print("Invalid Input")


# Captalize(), lower() and upper()

# order = input("What do you want? ")
# # print(order.upper())  
# if order.strip().capitalize() == "Rice":
#     print("Success")
# else: 
#     print("Failed")


# # replace()
# newval =  comment.replace("commented", "Stated")  # replace COMMENTED with STARTED
# print(comment)
# print(newval)

# # split()
# # print(comment.split()) # changes each word to list  using space
# # print(comment.split('.')) # splitting using "."
# print(comment.lower().split('this')) # splitting using "this"

# # join()  joins characters/words together
# word_split = comment.split()
# print(" ".join(word_split[0:4]))

# # center()  margin-left
# name = "tim bank"
# print(name.center(100))

# # count()
# print(comment.count(" is"))

# # encode()
# print(name.encode())


# in operator  boolean
# val = "weak" in comment
    # print(val)
# val = "weak" not in comment
    # print(val)

# Escape Character (\)
# print('she\s the owner')
# print('she is the\b owner')
# print('she is the\t owner')
# print('she is the\r owner')
# print('she is the\n owner')
# print('she is the\b owner')

# # HOW TO GET A MAXIMIUM AND MINIMUM VALUE
# my = (15, 45, 30)
# result = max(my)
# result2 = min(my)
# print(result)
# print(result2)

# text = "We couldn't find the body"
# val = text.split()
# # print(val)
# print('+'.join(val))

value = [3,5,12,6,2,1,8]
# value.sort(reverse=True)
value.sort()
print(value)