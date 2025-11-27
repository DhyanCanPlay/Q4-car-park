
grid = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
         ]
grid1 = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
         ]


def options (x ,grid, grid1):
    if x == 1:
        
        grid = grid1
        print("Reset Success")
        print(grid)
        menu()
        



    elif x == 2:
        print("-----CAR REMOVE-----")
        rmcarRow = int(input("Enter row of the car: ")) - 1
        rmcarCol = int(input("Enter col of the car: ")) - 1
        grid[rmcarRow][rmcarCol] = "-"
        #return grid
        menu()
        
        menu()
    elif x == 3:
        print("-----CAR ADD-----")
        rmcarRow = int(input("Enter row of the car: ")) - 1
        rmcarCol = int(input("Enter col of the car: ")) - 1
        numPlate = str(input("Enter Licence Plate Number: "))
        grid[rmcarRow][rmcarCol] = numPlate
        #return grid
        menu()
    elif x == 4:
        print(grid)
        for row in grid:
            print(" | ".join(row))
            print("   ")
        menu()
    elif x == 5:
        print("stopping program")
        exit()
        
        menu()
    else:
        print("Enter a valid option")
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
    options(option, grid, grid1)


menu()
