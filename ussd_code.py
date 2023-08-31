user = input('Enter *310# for your data plan: ')
# while #user != '*310#':
while user != '*310#':
    user == int(input('Try again: ')) 
print('''
        1. Daily Plan
        2. Weekly Plan
        3. Monthly Plan
    ''') 
inp_1 = int(input('Option: '))
if inp_1 == '1':
    print('''
            DAILY PLAN
            1. #100 for 240mb 1day
            2. #200 for 350mb 1day
            3. #300 for 500mb 2days
            4. #500 for 2.5gb 2days
            5. #700 for 3gb 5days 
            ''')
elif inp_1 == '2':
    print('''
            1. #500 for 1.5gb 7days
            2. #500 for 750mb 14days
            3. #1000 for 2gb 2weeks
            4. #1500 for 4gb 2weeks
            5. #2000 for 5gb 2weeks
        ''') 
    # else:
        #     print('Invalid') 
# else:
#      user = int(input('Try again: '))              
# break            