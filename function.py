# PYTHON FUNCTION: It also allows source to repeat multiple times(iteration)

# Stages of function:
# 1.) Function declaration: def functionName(): [for a function without parameter] OR
                           #def functionName(param_a, param_b): [for a function with parameter]
# 2.) Function definition: print("I'm a function")
# 3.) Function invocation:

# def parameter(): 
#     print("I am a fuction")
# parameter()

# Types of Function:
# 1.) A Parameterized Function: Allows parameter or value(argument) in it 
# Example: 
# def print_name(name):
#     print('My name is', name)
# print_name('Benjamin')

# 2.) Non-parametized Function: Has no value(argument) in it
# Example:
# def parameter(): 
#     print("I am a fuction")
# parameter()

# Additon
def addition(add1, add2=1):
    add = add1 + add2
    print(add)
# addition(10)    

def addd(val1, val2):
    val = val1 + val2
    print(val)
# addd(val1=(int(input('First Value: '))), val2=(int(input('Second Value: '))))  

# def sum(val1=(int(input('First Value: '))), val2=(int(input('Second Value: ')))):
#     print(val1 + val2)
# sum()

def addition(add1, add2=1):
    add = add1 + add2
    return add # return keeps the value while print displays the value
# print('The sum is, ',addition(10))

import sys
def landingPage():
    print("""
            WELCOME
            1. Sign In 
            2. Sign Up
            3. Exit
        """)
    user = (input("Choose an option: "))
    user
    if user == "1":
        signIn()
    elif user == "2":
        signUp()
    elif user == "3":
         print('Terminated!')
         sys.exit()    
    else:
        print('Invalid Input')
        landingPage()       
    

def signIn():
    print(f"""
                SIGN IN OPTIONS 
                1. To continue
                2. Haven't Gotten an account?
                0. Back  
        """) 
    inp = (input("Choose Option: "))
    if inp == '1':
        name = input('Enter your name: ') 
        email = input('Email: ')
        phoneNumber = int(input('Phone Number: ')) 
        print(f'''
                Welcome 
                Name: {name.upper()}    Email: {email.strip()}      Phone Number: {phoneNumber}
        ''')
        signIn_Inner()
    elif inp == '2':
        signUp()    
    elif inp == '0':
        landingPage()

def signIn_Inner():
    inp = input('How can we be of help to you? ')
    print(f"""
                Your request is {inp.capitalize()}.\n
                Would get back later. Thank you.
          """)
def signUp():   
   print('''
                SIGN UP OPTIONS
                1.  To continue
                2.  For More Inquiry
                3.  Menu
                00. Exit
        ''')
   inp2 = (input("Choose Option: "))
   if inp2 == '1':
       print("""
                You are welcome
                1. To enter your details
                0. Back
             """)
       inp2 = (input("Choose Option: "))
       if inp2 == '1':
           name = input('Enter your name: ') 
           email = input('Email: ')
           phoneNumber = int(input('Phone Number: ')) 
           gender = input('Gender: ')
           marital = input('Marital Status: ')
           age = int(input('Age: '))
           print(f'''
                    Welcome 
                    Name: {name.upper()}    Email: {email.strip()}      Phone Number: {phoneNumber}
                    Gender: {gender.capitalize()}   Marital Status: {marital.capitalize()}  Age: {age}
           ''')
           print('Press any key to continue and 00 to exit')
           inp3 = (input("Choose Option: "))
           if inp3 == '00':
                print('Terminated!')
                sys.exit()
           else:
            signIn_Inner() 

   elif inp2 == '2':
       print("Error") 
       sys.exit
   elif inp2 == '3':
       landingPage()    
   elif inp2 == '00':      
        print('Exit')
        sys.exit
   else:
       print('Invalid Input!')
       signUp()

def signUp_Inner():
    pass           
landingPage()


# RECCURSSIVE FUNCTION:
