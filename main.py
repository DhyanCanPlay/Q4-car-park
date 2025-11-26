grid = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
         ]  

def options (x):
    if x == 1:
        grid = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
        print("Reset Success")
        menu()
        
        
    elif x == 2:
        print("-----CAR REMOVE-----")
        rmcarRow = input("Enter row of the car: ")
        rmcarCol = input("Enter col of the car: ")
        menu()
    elif x == 3:
        print("exeuted option 3")
        menu()
    elif x == 4:
        
        for row in grid:
            print(" | ".join(row)) 
            print("   ")
        menu()
    elif x == 5:
        print("exeuted option 5")
        menu()
    
    




def menu():
    print("--------------- MENU ---------------")
    print("1. reset all spaces in the car park  to empty ")
    print("2. remove a car")
    print("3. add a car")
    print("4. Display the car park grid")
    print("5. Quit ")
    print("select an option")
    option = int(input("Enter a choice(1-5):  "))
    options(option)
    

menu()
