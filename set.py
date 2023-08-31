# A calculator to calculate set
print("""
        CHOOSE THE NUMBER OF ELEMENTS YOU WANT IN A EACH SET
        1.) 2x2
        2.) 2x3
        3.) 3x2
        4.) 3x3
        5.) 3x4
        6.) 4x3
        7.) 4x4
""")
select = int(input("Select a number: "))


# WHEN SELECT IS 1
if select == 1:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")    
    
# WHEN SELECT IS 2 
elif select == 2:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")) }

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!") 

# WHEN SELECT IS 3 
elif select == 3:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: "))}

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")  

# WHEN SELECT IS 4 
elif select == 4:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")  
                 
# WHEN SELECT IS 5 
elif select == 5:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: "))}

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")  

# WHEN SELECT IS 6 
elif select == 6:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: "))}

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: "))}

    print("""
            ENTER THE CALCULATION YOU WANT TO PERFORM
            1.) Union of the set
            2.) Intersection
            3.) Difference
    """)
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")       

elif select == 7:
    print("The First Set")
    inp1 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: ")) }

    print("\nThe Second Set\n")
    inp2 = {int(input("Enter the first set: ")), int(input("Enter the second set: ")), int(input("Enter the third set: ")), int(input("Enter the forth set: ")) }

    print("""
        ENTER THE CALCULATION YOU WANT TO PERFORM
        1.) Union of the set
        2.) Intersection
        3.) Difference
          """)
    
    user = int(input("Select a number: "))
    if user == 1:
        union = inp1.union(inp2)
        print(f'The union of {inp1} and {inp2} = {union}')
    elif user == 2:
        intersect = inp1.intersection(inp2)
        print(f'The intersection of {inp1} and {inp2} = {intersect}')
    elif user == 3:
        print("""
                ENTER THE ONE TO FIND ITS DIFFERENCE:
                1.) Set A - Set B
                2.) Set B - Set A
        """)
        inner = int(input("Enter a number: "))
        if inner == 1:
            difference1 = inp1.difference(inp2)
            print(f'The differnce of {inp1} and {inp2} = {difference1}')
        elif inner == 2:    
            difference2 = inp2.difference(inp1)
            print(f'The differnce of {inp1} and {inp2} = {difference2}')
        else:
            print("Invalid Input!")
else:
    print("Invalid Input")
