# ussd = '*312#'
# user = input("Enter *312# as ussd code: ")
# if user == ussd:
#     print("""
#             Input any of the numbers for more inquiry:
#             1. My offer
#             2. Data Bundles
#             *  Next
# """)
#     user = input("Choose your option: ")
    
#     # WHEN THE USERINPUT IS 1
#     if user == '1':
#         print("""
#         My Offer
#         1. #2000 for 3gb
#         2. #500 for 1gb
#         22. back
#         **  Menu
#         0. Exit
# """)
#         userInput = input('Input your number: ')
#         if userInput == '1':
#             print("You've subscribed #2000 for 3gb")   
#         elif userInput == '2':
#             print("You've subscribed #500 for 1gb")   
#         elif userInput == '22':
#             print("""
#             Input any of the numbers for more inquiry:
#             1. My offer
#             2. Data Bundles
#             *  Next
#         """) 
            
#         elif userInput == '**':
#             print("""
#                 Input any of the numbers for more inquiry:
#                 1. My offer
#                 2. Data Bundles
#                 *  Next
#     """)  
#         elif userInput == '0':
#             print("""
#                 Thank you so much for your time.
#         """)
#         else:
#             print("Invalid Option")    
#     else:
#         print("Invalid Selection")     

#      # WHEN USER INPUT IS '2'  
# elif user == '2':
#     print("""
#               Data Plan
#               1. Daily plan
#               2. Weekly Plan
#               3. Monthly plan
#               4. Social Bundle
#               22. Back
#     """)     
#     dataInput = input('Input a number: ')
#     if dataInput == '1':
#         print("""
#         1. #100 for 240mb 1day
#         2. #200 for 350mb 1day
#         3. #300 for 500mb 2days
#         4. #500 for 2.5gb 2days
#         5. #700 for 3gb 5days  
#         """)
#         innerdata = input('Input a number: ')
#         if innerdata == '1':
#             print("Successful, ypu've subscribed #100 data for 240mb. Valid for 1day.")
#         elif innerdata == '2':
#             print("Successful, you've subscribed #200 data for 350mb. Valid for 1 day.")
#         elif innerdata == '3':
#             print("Successful, you've subscribed #300 data for 500mb. Valid for 2days.")     
#         elif innerdata == '4':
#             print("Successful, you've subscibed #500 data for 2.5gb. Valid for 2days.")
#         elif innerdata == '5':
#             print("Successful, you've subscibed #700 data for 3gb. Valid for 5days.")
#         else:
#             print("Invalid dataInput1")  

#     elif  dataInput == '2':
#         print("""
#         1. #500 for 1.5gb 7days
#         2. #500 for 750mb 14days
#         3. #1000 for 2gb 2weeks
#         4. #1500 for 4gb 2weeks
#         5. #2000 for 5gb 2weeks         
#     """)
        
#         innerdata = input("Input a number: ")
#         if innerdata == '1':
#             print("Successful, you've subscribed #500 data for 1.5gb. Valid for 7days.")
#         elif innerdata == '2':
#             print("Successful, you've subscribed #500 data for 750mb. Valid for 14days.")
#         elif innerdata == '3':
#             print("Successful, you've subscribed #1000 data for 2gb. Valid for 2weeks.")  
#         elif innerdata == '4':
#             print("Successful, you've subscribed #1500 data for 4gb. Valid for 2weeks.")
#         elif innerdata == '5':    
#             print("Successful, you've subscribed #2000 data for 5gb. Valid for 2weeks.")
#         else:
#             print("Invalid dataInput2")  
#     else:
#         print("invalid")  
# else:
#     print("invalid...")  


# # Multiplication Table of a given range
# val = int(input("Enter any positive integer: "))
# i = int(input("Enter the range: "))

# print('This is the multiplication table of', val, 'within the range of 1 and', i) 

# for var in range(1,i+1):
#     print(val, 'x', var, '=', val*var)

val = {'Omolola': 1, 'Mary': 2}
print(val.items())