firstName = input("Enter your first name: ")
print(firstName.capitalize().strip())
middleName = input("Enter your middle name: ")
print(middleName.capitalize().strip())
lastName = input("Enter your last name: ")
print(lastName.capitalize().strip())
divison = input("Are you a student or staff? ")
print(divison.strip().capitalize())

        # FOR STUDENT
if divison.strip().capitalize() == "Student":
    print("Valid Input")
    
    email = input("Enter your email address: ")
    if email.endswith("@gmail.com"):
        print("Valid Email")
    else:
        print("Invalid Email")
    phone_number = input("Enter your phone number: ")
    if len(phone_number.strip()) == 11:
        print("Valid Number!")
    else:
        print("Invalid Number.")    
    department = input("Enter your department: ")
    print(department.strip().capitalize())
    level = input("Enter your level: ")
    print(level.strip().capitalize())
    maritalStatus = input("Your Marital Status: ")
    print(maritalStatus.strip().capitalize())
    age = input("Your age: ")
    print(age.strip())
    numberOfKids = input("Number of Kids: ")
    print(numberOfKids.strip().upper())
    nextOfKin = input("Your next of kin: ")
    print(nextOfKin.capitalize().strip())
    passWord = input("Your password: ")
    print(passWord.strip())
    yourComment = input("Comment Here...")
    print(yourComment.strip().capitalize())

        # FOR STAFF
elif divison.strip().capitalize() == "Staff": 
    print("Valid Input") 
    email = input("Enter your email address: ")
    if email.endswith("@gmail.com"):
        print("Valid Email")
    else:
        print("Invalid Email")
    phone_number = input("Enter your phone number: ")
    if len(phone_number.strip()) == int(11):
        print("Valid Number!")
    else:
        print("Invalid Number.")    
    department = input("Enter your department: ")
    print(department.strip().capitalize())
    maritalStatus = input("Your Marital Status: ")
    print(maritalStatus.strip().capitalize())
    age = input("Your age: ")
    print(age.strip())
    numberOfKids = input("Number of Kids: ")
    print(numberOfKids.strip().capitalize())
    nextOfKin = input("Your next of kin: ")
    print(nextOfKin.upper())
    experience = input("What is your year of experience? ")
    print(experience.strip().capitalize())
    passWord = input("Your password: ")
    print(passWord.strip())
    yourComment = input("Comment Here...")
    print(yourComment.strip().capitalize())
else:
    print("Invalid Input") 

if divison.strip().capitalize() == "Student":
    # outPut_student = "COLLECTION OF BIO-DATA"
    print (f"""
        Please Check if your input or Details are Correct. Thank you!
        
        NAME:
        {firstName.capitalize().strip()} {middleName.capitalize().strip()} {lastName.capitalize().strip()}

        CATERGORY:
        {divison.strip().capitalize()}     

        AGE:                 
        {age.strip()} 

        PHONE NUMBER:    
        {phone_number.strip()}             
                        
        EMAIL:              
        {email}             

        DEPARTMENT:
        {department.strip().capitalize()}

        MARITAL STATUS:
        {maritalStatus.strip().capitalize()}

        NUMBER OF KIDS:
        {numberOfKids.strip().capitalize()}

        NEXT OF KIN:
        {nextOfKin.upper().strip()}
                            
        USER PASSWORD:
        {passWord.strip()}

        USER COMMENT:
        {yourComment.strip().capitalize()}
""") 
else:
    # outPut_STAFF = "COLLECTION OF BIO-DATA"
    print (f"""
        Please Check if your input or Details are Correct. Thank you!
        
        NAME:
        {firstName.capitalize().strip()} {middleName.capitalize().strip()} {lastName.capitalize().strip()}

        CATERGORY:
        {divison.strip().capitalize()}  

        AGE:         
        {age.strip()} 

        PHONE NUMBER: 
        {phone_number.strip()}            
                        
        EMAIL:              
        {email}             

        DEPARTMENT:
        {department.strip().capitalize()}

        MARITAL STATUS:
        {maritalStatus.strip().capitalize()}

        EXPERIENCE:
        {experience.strip().capitalize()}   

        NUMBER OF KIDS:
        {numberOfKids.strip().capitalize()}

        NEXT OF KIN:
        {nextOfKin.upper().strip()}                

        USER PASSWORD:
        {passWord.strip()}

        USER COMMENT:
        {yourComment.strip().capitalize()}
""")  


