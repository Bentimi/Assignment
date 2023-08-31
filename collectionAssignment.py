import sys

lastName = input("Enter your surname: ")
firstName = input("Enter your first name: ")
middleName = input("Enter your middle name: ")
matric = int(input("Matric Number: "))
level = int(input("Level: "))
password = input("Password: ")
userId = input("User ID: ")

name = (f'{lastName.strip().upper()} {firstName.strip().upper()} {middleName.strip().upper()}')

# Q1 = ['1.) Asiwaju Bola Ahmed Tinubu is the prsident of Nigeria']
# Q2 = ['2.) Capital of Nigeria is?']
# Q3 = ['3.) Which state is Ibadan located?']
# Q4 = ['4.)  Which type of case is WORD']
# Q5 = ['5.)  Who is the governor of Oyo State?']
# Q6 = ['6.)  What is the largest city in west africa?']
# Q7 = ['7.)  Which country has its capital to be Paris?']
# Q8 = ['8.)  How many geo-political zones are in Nigeria?']
# Q9 = ['9.)  What is the full meaning of USD?']
# Q10 = ['10.) As bullock is for bull, capoon is for ______ ']
# questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
questions = ["1.) Asiwaju Bola Ahmed Tinubu is the prsident of Nigeria", "2.) Capital of Nigeria is?","3.) Which state is Ibadan located?", "4.)  Which type of case is WORD", "5.)  Who is the governor of Oyo State?", "6.)  What is the largest city in west africa?", "7.)  Which country has its capital to be Paris?", "8.)  How many geo-political zones are in Nigeria?", "9.)  What is the full meaning of USD?", "10.) As bullock is for bull, capoon is for ______ "]
options  = ['True or False?', ' ', ' ', 'a.) Lower b.) Upper c.) Sentence d.) toggle ', ' ', ' ', ' ', '6', ' ', ' ']
marks = 0

print(f"""
        Welcome 
        NAME: {name}          
        MATRIC NUMBER: {matric}    
        USER ID: {userId.strip()}     
        LEVEL: {level}
    press ANY key to continue or 0 to exit
""")

user = input("Option: ")
if user != "0":
    user_ID = input("Enter User ID: ")
    pass_word = input("Enter Password: ")
    if user_ID.strip()  == user_ID and pass_word.strip() == password.strip():
        print("Press NEXT to continue or EXIT to terminate.")

        user2 = input("Option: ")
        if user2.strip().upper() == 'NEXT':
            
                print("""
                  Are you ready for the test?
                  if yes, type YES or NO to terminate
                  if no, type NO to terminate
                      
                      Thank you!
            """) 
                user3 = input("Option: ")
                if user3.strip().upper() == "YES":
                    for list, score in zip(questions, options):
                        print(f'{list} {score}')
                        inp = input("Answers: ")
                        if inp.strip().capitalize() == 'True':
                            print(f'\nNext Question Please\n')
                            marks +=1
                        elif inp.strip().capitalize() == 'Abuja':
                            print(f'\nNext Question Please\n')
                            marks +=1
                        elif inp.strip().capitalize() == 'Oyo':
                            print(f'\nNext Question Please\n')
                            marks +=1
                        elif inp.strip().lower() == 'b' or inp.strip().lower() == 'upper' or inp.strip().lower() == 'b.) upper':
                            print(f'\nNext Question Please\n')
                            marks +=1
                        elif inp.strip().upper() == 'SEYI MAKINDE':
                            print(f'\nNext Question Please\n')
                            marks +=1
                        elif inp.strip().capitalize() == 'Ibadan':
                            print(f'\nNext Question Please\n')
                            marks +=1    
                        elif inp.strip().capitalize() == 'France':
                            print(f'\nNext Question Please\n')
                            marks +=1  
                        elif inp.strip() == '6':
                            print(f'\nNext Question Please\n')
                            marks +=1             
                        elif inp.strip().lower() == 'united states dollar':
                            print(f'\nNext Question Please\n')
                            marks +=1    
                        elif inp.strip().capitalize() == 'Hen':
                            print(f'\nNext Question Please\n')
                            marks +=1    
                        else:
                            print("Question")    
                    print(f'You obtained {marks} out of 10 marks')
                else:
                    print("Take care.")
        
        else:
            print("Error")
    else:
        print("EXIT")     
else:
    print("Sorry, you left the page!")
    sys.exit()   



    # """
    # QUESTIONS:
    # 1.) Asiwaju Bola Ahmed Tinubu is the prsident of Nigeria. 
    # True or False?
    # 2.) Capital of Nigeria is?
    # 3.) Which state is Ibadan located?
    # 4.) Which type of case is WORD?
    # a.) Lower b.) Upper c.) Sentence d.) toggle 
    # 5.) Who is the governor of Oyo State?
    # 6.) What is the largest city in west africa?
    # 7.) Which country has its capital to be Paris?
    # 8.) How many geo-political zones are in Nigeria?
    # 9.) What is the full meaning of USD?
    # 10.) As bullock is for bull, capoon and weather is for ______ and _______
    # """        


    # """
#     # QUESTIONS AND THE GRADINGS
# Q1 = ['1.) Asiwaju Bola Ahmed Tinubu is the prsident of Nigeria']
# Q2 = ['2.) Capital of Nigeria is?']
# Q3 = ['3.) Which state is Ibadan located?']
# Q4 = ['4.)  Which type of case is WORD']
# Q5 = ['5.)  Who is the governor of Oyo State?']
# Q6 = ['6.)  What is the largest city in west africa?']
# Q7 = ['7.)  Which country has its capital to be Paris?']
# Q8 = ['8.)  How many geo-political zones are in Nigeria?']
# Q9 = ['9.)  What is the full meaning of USD?']
# Q10 = ['10.) As bullock is for bull, capoon is for ______ ']
# questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
# options  = ['True or False?', ' ', ' ', 'a.) Lower b.) Upper c.) Sentence d.) toggle ', ' ', ' ', ' ', '7', ' ', ' ']
# marks = 0

# """
# for list, score in zip(questions, options):
#     print(f'{list} {score}')
#     inp = input("Answers: ")
#     if inp.strip().capitalize() == 'True':
#         print(f'\nNext Question Please\n')
#         marks +=1
#     elif inp.strip().capitalize() == 'Abuja':
#         print(f'\nNext Question Please\n')
#         marks +=1
#     elif inp.strip().capitalize() == 'Oyo':
#         print(f'\nNext Question Please\n')
#         marks +=1
#     elif inp.strip().lower() == 'b' or inp.strip().capitalize() == 'upper' or inp.strip().capitalize() == 'b.) upper':
#         print(f'\nNext Question Please\n')
#         marks +=1
#     elif inp.strip().upper() == 'SEYI MAKINDE':
#         print(f'\nNext Question Please\n')
#         marks +=1
#     elif inp.strip().capitalize() == 'Ibadan':
#         print(f'\nNext Question Please\n')
#         marks +=1    
#     elif inp.strip().capitalize() == 'France':
#         print(f'\nNext Question Please\n')
#         marks +=1  
#     elif inp.strip() == '7':
#         print(f'\nNext Question Please\n')
#         marks +=1             
#     elif inp.strip().lower() == 'united states dollar':
#         print(f'\nNext Question Please\n')
#         marks +=1    
#     elif inp.strip().capitalize() == 'Hen':
#         print(f'\nNext Question Please\n')
#         marks +=1    
#     else:
#         print("Question")    
# print(f'You obtained {marks} out of 10 marks')
# else:
# print("Take care.")
# """