# lastName = input("Enter your surname: ")
# firstName = input("Enter your first name: ")
# middleName = input("Enter your middle name: ")
# matric = int(input("Matric Number: "))
# level = int(input("Level: "))
# password = input("Password: ")
# userId = input("User ID: ")

# name = (f'{lastName.strip().upper()} {firstName.strip().upper()} {middleName.strip().upper()}')

# questions = ["1.) Asiwaju Bola Ahmed Tinubu is the prsident of Nigeria", "2.) Capital of Nigeria is?","3.) Which state is Ibadan located?", "4.)  Which type of case is WORD", "5.)  Who is the governor of Oyo State?", "6.)  What is the largest city in west africa?", "7.)  Which country has its capital to be Paris?", "8.)  How many geo-political zones are in Nigeria?", "9.)  What is the full meaning of USD?", "10.) As bullock is for bull, capoon is for ______ "]

# options  = ['True or False?', ' ', ' ', 'a.) Lower b.) Upper c.) Sentence d.) toggle ', ' ', ' ', ' ', '', ' ', ' ']

# correct  = ['true', 'abuja', 'oyo', 'b', 'seyi makinde', 'ibadan', 'france', '6', 'united states dollar', 'hen']

# marks = 0


# for list, score, corr in zip(questions, options, correct):
#     print(f'\n{list} {score}\n')
#     answer = input("Choose an option: ")     
#     if corr.startswith(answer.lower().strip()):
#          print(f'\n{answer}\n')
#          marks +=1/len(questions)*100
#     else:
#         print(f'\n{answer}\n') 
# print(f"Hello {name}, you obtained {int(marks)}%")  



# # IMPROVED VERSION USING DICTIONARY
# lastName = input("Last name: ")
# firstName = input("First name: ")
# middleName = input("Middle name: ")
# matric_no = int(input("Matric number: "))
# level = int(input("Level:"))
# userID = (input("UserID: "))
# password = input("Password ")

# name = (f'Surname: {lastName.upper().strip()} First Name :{firstName.upper().strip()} Middle Name: {middleName.upper().strip()}')
# name1 = (f'{lastName.upper().strip()} {firstName.upper().strip()} {middleName.upper().strip()}')

# print(f"""
#         WELCOME TO THIS COMPUTER BASED TEST
#         Hi {name} 
#         USERID: {userID.strip()} 
#         MATRIC NUMBER: {matric_no}
#     """)

# import time
questions = {'TRUE':'Asiwaju Bola Ahmed Tinubu is the president of Nigeria.  True or False?',
            'ABUJA':'Capital of Nigeria is?',
            'OYO':'Which state is Ibadan located?',
            'B':'Which type of case is WORD? a.) Lower b.) Upper c.) Sentence d.) toggle', 
            'SEYI MAKINDE':'Who is the governor of Oyo State?',
            'IBADAN':'What is the largest city in west africa?',
            'FRANCE':'Which country has its capital to be Paris?',
            '6':'How many geo-political zones are in Nigeria?',
            'UNITED STATES DOLLAR':'What is the full meaning of USD?',
            'HEN AND RAM':'As bullock is for bull, capoon and weather(sheep) is for ______ and _______',
    }
# number = 1
# mark = 0
# for answer, quest in questions.items():
#     print(f'\n{number}.) {quest}\n')
#     number +=1
#     inp = input("Answer: ")
#     if inp.upper().strip() == answer:
#         mark +=1
#     # print('please wait...')
#     # time.sleep(1)

# print(f'You obtained {(mark)} of {number -1}')
# print(f'Dear {name1},you obtained {(mark)} of {number -1}')

numberOfStudents = int(input("Number of candidate(s): "))
number = 1
for val in range(numberOfStudents):
    print(f'CANDIDATE NUMBER ({number}) IS REQUIRED TO FILL THIS, THANK YOU.')
    lastName = input("Last name: ")
    firstName = input("First name: ")
    middleName = input("Middle name: ")
    matric_no = int(input("Matric number: "))
    level = int(input("Level:"))
    course = input("Course: ")
    userID = (input("UserID: "))
    password = input("Password ")
    name1 = (f'{lastName.upper().strip()} {firstName.upper().strip()} {middleName.upper().strip()}')
    # details = (f'{name1}, {matric_no}, {course}, {level}, {userID}')
    # val = {number:details}
    name = (f'Surname: {lastName.upper().strip()} First Name :{firstName.upper().strip()} Middle Name: {middleName.upper().strip()}')

    # for value, item in val.items():
    #     print(f"""
    #             WELCOME CANDIDTE NUMBER: {number}.
    #              {value} {item}
    #     """)

    print(f"""
            WELCOME TO THIS COMPUTER BASED TEST CANDIDTE NUMBER: {number}
            Hi {name} 
            USERID: {userID.strip()} 
            MATRIC NUMBER: {matric_no}
        """)
    number +=1

    questions = {'TRUE':'Asiwaju Bola Ahmed Tinubu is the president of Nigeria.  True or False?',
                 'ABUJA':'Capital of Nigeria is?', 
                 'OYO':'Which state is Ibadan located?',
                 'B':'Which type of case is WORD? a.) Lower b.) Upper c.) Sentence d.) toggle', 
                 'SEYI MAKINDE':'Who is the governor of Oyo State?',
                 'IBADAN':'What is the largest city in west africa?',
                 'FRANCE':'Which country has its capital to be Paris?',
                 '6':'How many geo-political zones are in Nigeria?',
                 'UNITED STATES DOLLAR':'What is the full meaning of USD?',
                 'HEN AND RAM':'As bullock is for bull, capoon and weather(sheep) is for ______ and _______'
    }
    listing = 1
    mark = 0
    for answer, quest in questions.items():
        print(f'\n{listing}.) {quest}\n')
        listing +=1
        inp = input("Answer: ")
        if inp.upper().strip() == answer:
            mark +=1
    # print(f'You obtained {(mark)} of {listing -1}')
    print(f'\nDear {name1}, you obtained {(mark)} of {listing -1}\n')
else:
    ''

# scores = (mark,)
# if scores == max(scores) and scores == min(scores):
#     print("Highest")
# else:
#     print(mark)        
# result = max(scores.values())
# result2 = min(scores.values())
# print(result)
# print(result2)


# for  mar in scores:
#     print(f'You obtained {(mar)} of {list -1} has the maximium {max(scores)}')
#     print(f'You obtained {(mar)} of {list -1} has minimium {min(scores)}')    

# for i in range(0, len(scores)):
#     if scores[i] < min:
#         min = scores[i]
#         print('max =' + str(scores))
# print('min =', min(scores))
# for  mar in scores:
    # print(f'You obtained {(mark)} of {list -1} has the max {max(scores)}')
# else:
#     print(f'You obtained {(mark)} of {list -1} has the lowest')    