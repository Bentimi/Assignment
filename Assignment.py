"""   
        # CALCULATOR ASSIGNMENT
#Program to calculate area of a right-anled triangle by accepting the iputs at the point of execution 

print("This used to calculate the area of a right-angled triangle")

num1= input("Enter the value of the base: ")
num2 = input("Enter the value of height: ")
c = 1/2
Area = float(c) * float(num1) * float (num2)

print(f"Area of the triangle = {Area}")
"""


"""
#Program to calculate for Qoutient and Remainder
print("This used to calculate for Qoutient and Remainder of a two given numbers")
dividend = input("Enter the value of dividend: ")
divisor = input("Enter the value of divisor: ")

quotient = int(dividend) / int(divisor)
remainder = int(dividend) % int(divisor)

print(f"The qoutient = {int(quotient)}")
print(f"The remainder = {int(remainder)}")
""" 



# """
        # GRADING SYSTEM ASSIGNMENT
    # A Program to display a simple grading system of score by the user

# score = int(input("Enter your score: "))
# if score<=100 and score>=70:
#     print("Your Grade is A")
# elif score<=69 and score>=60:
#     print("Your grade is B")
# elif score<=59 and score>=50:
#     print("Your grade is C")
# elif score<=49 and score>=45:
#     print("Your grade is D")
# elif score<=45 and score>=40:
#     print("Your grade is E")
# elif score<0:
#     print("Invalid Option!")
# else :
#     print("Sorry, You Failed!")
# """


"""
        # GRADING SYSTEM ASSIGNMENT
    # A Program to display a simple grading system of score by the user

score = int(input("Enter your score: "))
if score<=100 and score>=70:
    print("Your Grade is A")
elif score<69 and score>60:
    print("Your grade is B")
elif score<59 and score>50:
    print("Your grade is C")
elif score<49 and score>45:
    print("Your grade is D")
elif score<45 and score>40:
    print("Your grade is E")
elif score<0:
    print("Invalid Option!")
else :
    print("You Failed")
"""


# # GRADING SYSTEM ASSIGNMENT
#     # A Program to display a simple grading system of score
    
#     # Computation
# score = int(input("Enter your score(0 to 100): "))
# if score>=70:
#      print("Your Grade is A")
# elif score>=60:
#     print("Your grade is B")
# elif score>=50:
#     print("Your grade is C")
# elif score>=45:
#     print("Your grade is D")
# elif score>=40:
#     print("Your grade is E")
# elif score<0:
#     print("Invalid Option!")
# else :
#     print("Sorry, You Failed!")


"""# A USSD CODE SYSTEM
    # A Program to display/compute a USSD code system

    # Computation

val = input("Dial *310# for more inquiry: ")
result = val
if result == "*310#":
    print("Welcome")
else:
    print("Sorry, Invalid USSD code \n"
          "Please try again, thank you."
          )
    
transCode = input(
        "1. Check Balance \n"
        "2. Buy Airtime \n"
        "3. Fund Transfer \n"
        "Select transaction: "
    )

if  transCode == "1":
        print("Your account balance is 2000 Naira")
elif transCode == "2":
    print("Your account has been credited with an airtime of 500 Naira") 
    #    print(val=input("Enter the amount of the airtime: "))
    #    print(f"Your account has been credited with an airtime of {val}")
# print(f"Your account has been credited with an airtime of {val}")

elif transCode == "3":
 print("Fund Account")
else:
 print("Sorry, Invalid USSD code \n"
          "Please try again, thank you.")"""

# ""ussd = '*312#'
# user = input("Enter *312# as ussd code: ")
# if user == ussd:
#     print("""
#                 Welcome
#           1. My offer
#           2. Data Bundles
#           *  Next
# """)
#     user = input("Choose your option: ")
    
# # WHEN USERINPUT IS 1    
# if user == '1':
#     print("""
#                 My offer
#           1. #2000 for 3gb
#           2. #500 for 1gb
#           22. back
#           0. Exit
# """)
#     userInput = input('Input your number: ')
#     if userInput == '1':
#         print("You've subscribed #2000 for 3gb")
#     elif userInput == '2':
#         print("You've subscribed #500 for 1gb")
#     elif userInput == '22':
#         print("""
#                     Welcome
#             1. My offer
#             2. Data Bundles
#             *  Next
#     """)
        
#     elif userInput == '**':
#         print("""
#                     Welcome
#             1. My offer
#             2. My Area
#             3. Data Bundles
#             *  Next
#     """)
#     elif userInput == '0':
#         print("""
#             Thank you so much for your time.
#     """)
#     elif userInput == '*':
#         print("""
#                 1. #100 for 240mb 1day
#                 2. #200 for 350mb 1day
#                 3. #500 for 1.5gb 7day
#                 4. #500 for 750mb 14days
#                 5. #1000 for 2gb 2weeks
#                 6. #1000 for 1.5gb 30days
#                 7. #1500 for 2.5gb 30days
#     """)
#         nextInput = input('Input your number: ')
#     #     re_input1 = input("Choose your option: ")
#         if nextInput == "*":
#             print("""
#                         My offer
#                 1. #2000 for 3gb
#                 2. #500 for 1gb
#                 22. back
#                 **  Menu
#                 0. Exit
#         """)
#         else:
#             print('none')
#     else:
#         print("Invalid Input")
#         nextInput = input('Input your number: ')
# # #     re_input1 = input("Choose your option: ")
# # if nextInput == "*":
# #     print("""
# #                 My offer
# #           1. #2000 for 3gb
# #           2. #500 for 1gb
# #           22. back
# #           **  Menu
# #           0. Exit
# # """)

# #     re_input2 = input('Input your number')
# #     userInput = input('Input your number')
# # if userInput == '1':
# #     print("You've subscribed #2000 for 3gb")
# # elif userInput == '2':
# #     print("You've subscribed #500 for 1gb")
 
# # WHEN USERINPUT IS 2
# # elif user == '2':
# #      print("""
# #                 Data Plan
# #           1. Daily plan
# #           2. Weekly Plan
# #           3. Monthly plan
# #           4. Social Bundle
# # """)
# # userInput = input('Input your number: ')
# # if userInput == '1':
# #     print("""
# #     1. #100 for 240mb 1day
# #     2. #200 for 350mb 1day
# #     3. #300 for 500mb 2days
# #     4. #500 for 2.5gb 2days
# #     5. #700 for 3gb 5days  
# #     """)
# # elif userInput == '2':
# #     print("""
# #     1. #500 for 1.5gb 7day
# #     2. #500 for 750mb 14days
# #     3. #1000 for 2gb 2weeks
# #     4. #1500 for 4gb 2weeks
# #     5. #2000 for 5gb 2weeks  
# #     """)
# # elif userInput == '3':
# #     print("""
# #     1. #1000 for 1.5gb 30days
# #     2. #1500 for 2.5gb 30days
# #     3. #2000 for 3gb 30days
# #     4. #2500 for 4gb 30days
# #     5. #3000 for 10gb 30days 
# #     """)
    
# else: 
#     print("Invalid input")
""

ussd = '*312#'
user = input("Enter *312# as ussd code: ")
if user == ussd:
    print("""
                Welcome
          1. My offer
          2. Data Bundles
          *  Next
""")
    user = input("Choose your option: ")
    
    # WHEN USERINPUT IS 1    
    if user == '1':
        print("""
                    My offer
              1. #2000 for 3gb
              2. #500 for 1gb
              22. back
              **  Menu
              0. Exit
    """)
        userInput = input('Input your number: ')
        if userInput == '1':
            print("You've subscribed #2000 for 3gb")
        elif userInput == '2':
            print("You've subscribed #500 for 1gb")
        elif userInput == '22':
            print("""
                    My offer
              1. #2000 for 3gb
              2. #500 for 1gb
              22. back
              **  Menu
              0. Exit
    """)

        elif userInput == '**':
            print("""
                    Welcome
              1. My offer
              2. My Area
              3. Data Bundles
              *  Next
    """)
        elif userInput == '0':
            print("""
            Thank you so much for your time.
    """)
        else:
            print("Invalid Option")
            
 
#  WHEN USERINPUT IS 2
    elif user == '2':
         print("""
              Data Plan
              1. Daily plan
              2. Weekly Plan
              3. Monthly plan
              4. Social Bundle
            """)
    dataInput = input('Input a number: ')
    if dataInput == '1':
                 print("""
                    1. #100 for 240mb 1day
                    2. #200 for 350mb 1day
                    3. #300 for 500mb 2days
                    4. #500 for 2.5gb 2days
                    5. #700 for 3gb 5days  
                    """)
    innerdata = input("Input a number: ")
    if innerdata == "1":
        print("Successful, you've subscribed #100 data for 240mb. Valid for 1day.")
    elif innerdata == "2":
        print("Successful, you've subscribed #200 data for 350mb. Valid for 1day.")  
    elif innerdata == "3":
        print("Successful, you've subscribed #300 data for 500mb. Valid for 2days.") 
    elif innerdata == "4":
            print("Successful, you've subscribed #500 data for 2.5gb. Valid for 2days.")
    elif innerdata == "5":
        print("Successful, you've subscribed #700 data for 3gb. Valid for 5days.")
    else:
            print("Invalid dataInput1")
                        
                
    elif dataInput == '2':
        print("""
        1. #500 for 1.5gb 7days
        2. #500 for 750mb 14days
        3. #1000 for 2gb 2weeks
        4. #1500 for 4gb 2weeks
        5. #2000 for 5gb 2weeks  
        """)
        innerdata = input("Input a number: ")
        if innerdata == "1":
            print("Successful, you've subscribed #500 data for 1.5gb. Valid for 7days.")
        elif innerdata == "2":
            print("Successful, you've subscribed #500 data for 750mb. Valid for 14days.")  
        elif innerdata == "3":
            print("Successful, you've subscribed #1000 data for 2gb. Valid for 2weeks.") 
        elif innerdata == "4":
            print("Successful, you've subscribed #1500 data for 4gb. Valid for 2weeks.")
        elif innerdata == "5":
            print("Successful, you've subscribed #2000 data for 5gb. Valid for 2weeks.")
        else:
            print("Invalid dataInput2")    
    elif dataInput == '3':
        print("""
        1. #1000 for 1.5gb 30days
        2. #1500 for 2.5gb 30days
        3. #2000 for 3gb 30days
        4. #2500 for 4gb 30days
        5. #3000 for 10gb 30days 
        """)
        innerdata = input("Input a number: ")
        if innerdata == "1":
            print("Successful, you've subscribed #1000 data for 1.5gb. Valid for 30days.")
        elif innerdata == "2":
            print("Successful, you've subscribed #1500 data for 2.5gb. Valid for 30days.")  
        elif innerdata == "3":
            print("Successful, you've subscribed #2000 data for 3gb. Valid for 30days.") 
        elif innerdata == "4":
            print("Successful, you've subscribed #2500 data for 4gb. Valid for 30days.")
        elif innerdata == "5":
            print("Successful, you've subscribed #3000 data for 10gb. Valid for 30days.")
        else:
            print("Invalid dataInput3")    
    # else:
    #     print("Gbera")    
     
    # WHEN USERINPUT IS '*'
elif user == '*':
     print("""
                    1. #100 for 240mb 1day
                    2. #200 for 350mb 1day
                    3. #500 for 1.5gb 7day
                    4. #500 for 750mb 14days
                    5. #1000 for 2gb 2weeks
                    6. #1000 for 1.5gb 30days
                    7. #1500 for 2.5gb 30days
        """)
    nextInput = input('Input your number: ')
    if nextInput == "1":
            print("Successful, you've subscribed #100 data for 240mb. Valid for 1day.")
        elif nextInput == "2":
            print("Successful, you've subscribed #200 data for 350mb. Valid for 1day.")  
        elif nextInput == "3":
            print("Successful, you've subscribed #500 data for 1.5gb. Valid for 7days.")
        elif nextInput == "4":
            print("Successful, you've subscribed #500 data for 750mb. Valid for 14days.")
        elif nextInput == "5":
            print("Successful, you've subscribed #1000 data for 2gb. Valid for Weeks.")    
        elif nextInput == "6":
            print("Successful, you've subscribed #1000 data for 1.5gb. Valid for 30days.")
        elif nextInput == "7":
            print("Successful, you've subscribed #1500 data for 2.5gb. Valid for 30days.") 
    else:
            print("On colos")
else: 
    print("Invalid input")