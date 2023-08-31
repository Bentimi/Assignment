import sys
ussd = '*312#'
main = input("Enter *312#' to continue: ")
def first():
    if main == ussd:
        print('''
                Choose any of the following to continue
                1. My Offer
                2. Data Bundles
                **  Next
        ''')
        user = input("Choose an option to continue: ")
        if user == '1':
            second()
        elif user == '2':
            third()
        elif user == '**':
            next()    
    else:
        print('Invalid Input! Try again')
        first()

# WHEN USER INPUT IS 1        
def second():
    print("""
            MY OFFER
            1.  #2000 for 3gb
            2.  #500 for 1gb
            22. Menu  
            0.  Exit
    """)
    userInput = input('Choose an option: ')
    if userInput == '1':
        print("You've subscribed #2000 for 3gb")
    elif userInput == '2':
        print("You've subscribed #500 for 1gb")
    elif userInput == '22':
        first()
    elif userInput == '0':
        print("Process Terminated!")
        sys.exit()
    else: 
        print("Invalid Input! Try Again")
        second()    

# WHEN USER INPUT IS 2        
def third():
    print("""
            DATA PLAN
            1.  Daily Plan
            2.  Weekly Plan
            3.  Monthly Plan
            4.  Social Bundle
            99. Menu
            0.  Exit
    """)
    dataInput = input('Choose an option: ')
    if dataInput == '1':
        print("""
                DAILY PLAN
                1.  #100 for 240mb 1day
                2.  #200 for 350mb 1day
                3.  #300 for 500mb 2days
                4.  #500 for 2.5gb 2days
                5.  #700 for 3gb 5days
                99. Menu
                00. Back
                0.  Exit 
        """)
        innerdata = input('Choose an option: ')
        if innerdata == '1':
            print("Successful, ypu've subscribed #100 data for 240mb. Valid for 1day.")
        elif innerdata == '2':
            print("Successful, you've subscribed #200 data for 350mb. Valid for 1 day.")
        elif innerdata == '3':
            print("Successful, you've subscribed #300 data for 500mb. Valid for 2days.")     
        elif innerdata == '4':
            print("Successful, you've subscibed #500 data for 2.5gb. Valid for 2days.")
        elif innerdata == '5':
            print("Successful, you've subscibed #700 data for 3gb. Valid for 5days.")
        elif innerdata == '99':
            first()
        elif innerdata == '00':
            third()
        elif innerdata == '0':
            print('Invalid Input! Try Again')
            sys.exit()
        else:
            print("Invalid Input!") 
            third()
    elif dataInput == '2':
        print("""
                WEEKLY PLAN
                1. #500 for 1.5gb 7days
                2. #500 for 750mb 14days
                3. #1000 for 2gb 2weeks
                4. #1500 for 4gb 2weeks
                5. #2000 for 5gb 2weeks  
                99. Menu
                00. Back
                0.  Exit 
                """)
        innerdata = input("Choose an option: ")
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
        elif innerdata == '99':
            first()
        elif innerdata == '00':
            third()
        elif innerdata == '0':
            print('Invalid Input! Try Again')
            sys.exit()    
        else:
            print("Invalid Input! Try Again")
            third()
    elif dataInput == '3':
        print("""
                MONTHLY PLAN
                1. #1000 for 1.5gb 30days
                2. #1500 for 2.5gb 30days
                3. #2000 for 3gb 30days
                4. #2500 for 4gb 30days
                5. #3000 for 10gb 30days 
                99. Menu
                00. Back
                0.  Exit 
        """)
        innerdata = input("Choose an option: ")
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
        elif innerdata == '99':
            first()
        elif innerdata == '00':
            third()
        elif innerdata == '0':
            print('Invalid Input! Try Again')
            sys.exit()    
        else:
            print("Invalid Input! Try Again")
            third()
    elif dataInput == '4':
        print("""
                SOCIAL BUNDLE
              
                WTF
                1. #100 for 500mb 30days
                2. #50 for 200mb 14days
                TIKTOK
                3. #200 for 3gb 3hrs
                4. #500 for 10gb 3hrs
                YOUTUBE
                5. #100 for 5gb 1hr
                6. #200 for 10gb 1hr 
                99. Menu
                00. Back
                0.  Exit 
        """)
        innerdata = input("Choose an option: ")
        if innerdata == "1":
            print("Successful, your WTF #100 for 500mb is activated. Valid for 30days.")
        elif innerdata == "2":
            print("Successful, your WTF #50 for 200mb is activated. Valid for 14days.")  
        elif innerdata == "3":
            print("Successful, your TIKTOK #200 for 3gb is activated. Valid for 3hrs.") 
        elif innerdata == "4":
            print("Successful, your TIKTOK #500 for 10gb is activated. Valid for 3hrs.")
        elif innerdata == "5":
            print("Successful, your YOUTUBE #100 for 5gb is activated. Valid for 1hr.")
        elif innerdata == "6":
            print("Successful, your YOUTUBE #200 for 10gb is activated. Valid for 1hr.")
        elif innerdata == '99':
            first()
        elif innerdata == '00':
            third()
        elif innerdata == '0':
            print('Invalid Input! Try Again')
            sys.exit()    
        else:
            print("Invalid Input! Try Again")
            third()
    elif dataInput == '99':
        first()
    elif dataInput == '0':
        print('Process Terminated!')
        sys.exit()
    else:
        print('Invalid Input! Try Again')
        third()

# WHEN USER INPUT IS **
def next():
    print("""
            1.  #100 for 240mb 1day
            2.  #200 for 350mb 1day
            3.  #500 for 1.5gb 7day
            4.  #500 for 750mb 14days
            5.  #1000 for 2gb 2weeks
            6.  #1000 for 1.5gb 30days
            7.  #1500 for 2.5gb 30days
            99. Menu
            0.  Exit
        """)
    nextInput = input('Choose an option: ')
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
    elif nextInput == "99":
        first()
    elif nextInput == "0":
        print("Process Terminated!")
        sys.exit()
    else:
            print("Invalid Input! Try Again")
            next()
first()    