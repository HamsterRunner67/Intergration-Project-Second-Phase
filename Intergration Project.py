# Nicholas Lamon
# The program creates and allows you to play Minesweeper
#
#
import random


# Need To Do
# Complete Gameplay Loop - Done
# Add first spot Grace - Done
# Detect Win conditions.


def createGrid(sizeX, sizeY, mines, difficulty):
    # Creates grid based off of parameters
    array = []
    line = []
    for y in range(0, sizeY):
        for x in range(0, sizeX):
            if mines == True:
                ranNum = random.randrange(0, 11)
                if (ranNum <= difficulty):
                    line.append('x')
                else:
                    line.append('O')
            elif mines == False:
                line.append('x')
        array.append(line)
        line = []
    return array


def displayGrid(gridArray):
    # Takes any grid make and displays it

    accumulator = 1
    for y in gridArray:
        for x in y:
            print(x, end=' ')
        print()


def checkBomb(gridArray, coordX, coordY):
    # Creates an Array to find spot on grid
    # Takes the number inside of the coordinate spot and
    # Checks if its a bomb and returns True or False

    # Debug Code
    # print('---------')
    # print(coordX, coordY)

    # Tests Edge Cases of List so it doesnt wrap to other side
    if not (coordX < 0 or coordY < 0 or coordY >= len(gridArray) or coordX >= len(gridArray[coordY])):
        # Defines the line that the numbers is on
        line = gridArray[coordY]
        # print('Coord X',line[coordX])
        # checks if specific coordinate is bomb
        # returns True if its a bomb, False if not
        if (line[coordX] == 'O'):
            return True
        else:
            return False


def scan3x3Grid(gridArray, coordX, coordY):
    totalBombs = 0

    ##The code is going to scan a 3x3 area around a selected coordinate
    # and count up how many bombs there are to display a number

    # TOP LEFT
    if (checkBomb(gridArray, coordX - 1, coordY - 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # TOP MIDDLE
    if (checkBomb(gridArray, coordX, coordY - 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # TOP RIGHT
    if (checkBomb(gridArray, coordX + 1, coordY - 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # MIDDLE LEFT
    if (checkBomb(gridArray, coordX - 1, coordY) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # MIDDLE RIGHT
    if (checkBomb(gridArray, coordX + 1, coordY) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # BOTTOM LEFT
    if (checkBomb(gridArray, coordX - 1, coordY + 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1
    # BOTTOM MIDDLE
    if (checkBomb(gridArray, coordX, coordY + 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1

    # BOTTOM RIGHT
    if (checkBomb(gridArray, coordX + 1, coordY + 1) == True):
        # print('added bomb')
        totalBombs = totalBombs + 1

    return totalBombs


# def gracePeriod(hiddenGrid, workingGrid, coordX, coordY):
#    #OLD GRACE PERIOD METHOD - DOES NOT WORK
#
#    # TOP LEFT
#    workingGrid[coordY - 1][coordX - 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX - 1, coordY - 1) != True and not coordX - 1 < 0 and coordY - 1 < 0):
#        workingGrid[coordY - 1][coordX - 1] = str(scan3x3Grid(hiddenGrid, coordX - 1, coordY - 1))
#        print('JDSFKKLFASJFLKJASKFKLASF', workingGrid[coordY - 1][coordX - 1])
#    # TOP MIDDLE
#    workingGrid[coordY - 1][coordX] = 'x'
#    if (checkBomb(hiddenGrid, coordX, coordY - 1) != True and not coordX < 0 and coordY - 1 < 0):
#        workingGrid[coordY - 1][coordX] = str(scan3x3Grid(hiddenGrid, coordX, coordY - 1))
#    # TOP RIGHT
#    workingGrid[coordY - 1][coordX + 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX + 1, coordY - 1) != True and not coordX + 1 < 0 and coordY - 1 < 0):
#        workingGrid[coordY - 1][coordX + 1] = str(scan3x3Grid(hiddenGrid, coordX + 1, coordY - 1))
#    # MIDDLE LEFT
#    workingGrid[coordY][coordX - 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX - 1, coordY) != True and not coordX - 1 < 0 and coordY < 0):
#        workingGrid[coordY][coordX - 1] = str(scan3x3Grid(hiddenGrid, coordX - 1, coordY))
#    # MIDDLE RIGHT
#    workingGrid[coordY][coordX + 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX + 1, coordY) != True and not coordX + 1 < 0 and coordY < 0):
#        workingGrid[coordY][coordX + 1] = str(scan3x3Grid(hiddenGrid, coordX + 1, coordY))
#    # BOTTOM LEFT
#    workingGrid[coordY + 1][coordX - 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX - 1, coordY + 1) != True and not coordX - 1 < 0 and coordY + 1 < 0):
#        workingGrid[coordY + 1][coordX - 1] = str(scan3x3Grid(hiddenGrid, coordX - 1, coordY + 1))
#    # BOTTOM MIDDLE
#    workingGrid[coordY + 1][coordX] = 'x'
#    if (checkBomb(hiddenGrid, coordX, coordY + 1) != True and not coordX < 0 and coordY + 1 < 0):
#        workingGrid[coordY + 1][coordX] = str(scan3x3Grid(hiddenGrid, coordX, coordY + 1))
#    # BOTTOM RIGHT
#    workingGrid[coordY + 1][coordX + 1] = 'x'
#    if (checkBomb(hiddenGrid, coordX + 1, coordY + 1) != True and not coordX + 1 < 0 and coordY + 1 < 0):
#        workingGrid[coordY + 1][coordX + 1] = str(scan3x3Grid(hiddenGrid, coordX + 1, coordY + 1))


def newGracePeriod(hiddenGrid, workingGrid, coordX, coordY):
    # print('hidden grid y length', len(hiddenGrid))
    # print('hidden grid x length', len(hiddenGrid[coordY]))

    # In a three by three grid it checks
    # the amount of bombs for each spot
    # This is to make the game easier
    # earlier on.
    for y in range(-1, 2):
        for x in range(-1, 2):
            newCoordX = coordX + x
            newCoordY = coordY + y
            # (newCoordX, newCoordY)
            # print(0 > newCoordY)
            if (0 <= newCoordY <= len(hiddenGrid) and 0 <= newCoordX <= len(hiddenGrid[newCoordY])):
                hiddenGrid[newCoordY][newCoordX] = 'x'
                # if not(coordX < 0 or coordY < 0 or coordY >= len(hiddenGrid) or coordX >= len(hiddenGrid[coordY])):
                # print('ran')
                workingGrid[newCoordY][newCoordX] \
                    = scan3x3Grid(hiddenGrid, newCoordX, newCoordY)


def clickPoint(hiddenGrid, workingGrid, coordX, coordY, gracePeriodCounter):
    # Defines the Grid
    hiddenLine = hiddenGrid[coordY]
    workingLine = workingGrid[coordY]

    # Check if grace period is active
    # Makes sure you cant get out on first click
    if (gracePeriodCounter > 0):
        print('counter', gracePeriodCounter)
        hiddenLine[coordX] = 'x'
        newGracePeriod(hiddenGrid, workingGrid, coordX, coordY)

    # Detects if the spot is a bomb, if so it ends the game
    # If not a bomb it scans the area and changes

    if (hiddenLine[coordX] == 'O'):
        endGame()
    elif (hiddenLine[coordX] == 'x'):
        # Sets the coordinate on the Visible grid to the total bombs
        workingLine[coordX] = scan3x3Grid(hiddenGrid, coordX, coordY)


def flagPoint(gridArray, coordX, coordY):
    # Flags a point as a bomb
    line = gridArray[coordY]
    if (line[coordX] == 'x'):
        line[coordX] = 'F'
    elif (line[coordX] == 'F'):
        line[coordX] = 'x'


# Need To Write Help Screen
def helpScreen():
    print('---------------------------------------')
    print('In Minesweeper the objective is to flag all the bombs  \n'
          ' that are found on the map. When a point is selected \n'
          ' it tells you the amount of bombs that \n'
          ' are in a 3 x 3 area around the spot. If you \n'
          ' hit a bomb you lose and if you flag all the \n'
          ' mines you win. The top left is the origin of \n'
          ' the grid and it goes X coord first and then Y coord. \n'
          ' For example to select the middle of a 10x10grid\n '
          'you would type s 5 5 and to flag it you type f 5 5.\n '
          'Once you flag a point you can un-flag the point at anytime.\n')
    print('---------------------------------------')
    main()



# Basic Logic:
# Create hiddenGrid and Grid full of x's based off of settings
# Gameplay Loop:
# Ask for Command Ex. Check 1 1 or Flag 1 1
# Take command and translate it to grid spot
# Push through check spot or flag with the grid and coord arguments.
# End game if bomb, loop back if not.
# Check if all bombs have a flag
def gameplayLoop(hiddenGrid, workingGrid, gracePeriodCounter):
    displayGrid(workingGrid)
    error = True
    while (error == True):
        answer = input("Type 'S' Select Point Or 'F' to Flag a Point "
                       "(Ex. S 1 1 or F 1 1)")
        command = answer.split(' ')
        try:
            # Makes sure the other options are numbers
            command[1] = int(int(command[1]) - 1)
            command[2] = int(int(command[2]) - 1)
        except:
            print('Enter A valid Number for grid coordinates')
        else:
            # Detects whether to flag or select
            if (command[0].lower() == 's'):
                # Confirms that the number is in the range of the grid.
                if (len(workingGrid[command[2]]) >= int(command[1]) >= 0
                        and len(workingGrid) >= int(command[2]) >= 0):
                    # Runs The Select Command
                    clickPoint(hiddenGrid, workingGrid, command[1], command[2], gracePeriodCounter)
                    error = False
                else:
                    print('Please enter a value in the range of the grid.')
            elif (command[0].lower() == 'f'):
                if (len(workingGrid[command[2]]) >= int(command[1]) >= 0
                        and len(workingGrid) >= int(command[2]) >= 0):
                    # Runs the Flag Command
                    flagPoint(workingGrid, command[1], command[2])
                    error = False
                else:
                    print('Please enter a value in the range of the grid.')
            else:
                print("Invalid Answer:")


def startGame():
    # Opens settings and puts information into a list
    # takes the info and creates the grids based off it
    # Runs the Win Loop
    settings = []
    f = open('settings.txt', 'r')
    settings.append(int(f.readline().rstrip()))
    settings.append(int(f.readline().rstrip()))
    settings.append(int(f.readline().rstrip()))
    f.close()
    gracePeriodCount = 1
    hiddenGrid = createGrid(settings[0], settings[1], True, settings[2])
    workingGrid = createGrid(settings[0], settings[1], False, settings[2])
    win = False
    while (win == False):
        gameplayLoop(hiddenGrid, workingGrid, gracePeriodCount)
        gracePeriodCount = gracePeriodCount - 1
        checkWin(hiddenGrid, workingGrid)


##Completed
def changeSettings():
    settings = []
    f = open('settings.txt', 'r')
    settings.append(f.readline().rstrip())
    settings.append(f.readline().rstrip())
    settings.append(f.readline().rstrip())
    # print(settings)
    f.close()
    print('Your Settings are currently set to:')
    print('Grid Size: ', settings[0], 'x', settings[1], sep='')
    print('Current Difficulty is:', settings[2])
    # Gets the X Grid size while making sure user enters correct response
    f = open('settings.txt', 'w')
    print('What do you want the X grid size to be? (5-100)')
    error = True
    while (error == True):
        try:
            answer = int(input(':'))
        except:
            print('Please enter a number 5-100')
        else:
            if (answer <= 100 and answer >= 5):
                f.write(str(answer) + '\n')
                error = False
            else:
                print('Please enter a number 5-100')
    # Gets the Y grid size while making sure user enters correct response
    print('What do you want the Y grid size to be? (5-100)')
    error = True
    while (error == True):
        try:
            answer = int(input(':'))
        except:
            print('Please enter a number 5-100')
        else:
            if (answer <= 100 and answer >= 5):
                f.write(str(answer) + '\n')
                error = False
            else:
                print('Please enter a number 5-100')
    # Gets the Difficulty making the answer is correct
    print('What do you want the Difficulty to be?'
          '(1-10, 1 = Impossible, 10 = Instant Win)')
    error = True
    while (error == True):
        try:
            answer = int(input(':'))
        except:
            print('Please enter a number 1-10')
        else:
            if (answer <= 10 and answer >= 1):
                f.write(str(answer) + '\n')
                error = False
            else:
                print('Please enter a number 1-10')
    f.close()
    main()

def calculator():
    answer = input('Input a number')
    try:
        answer = int(answer)
    except:
        calculator()
    else:
        print(answer**2,'is your number squared')
        print(answer*2,'is your number times 2')
        print(answer/2,'is your number divided by 2')
        print(answer // 2, 'is your number floor divided by 2')
        if(answer%2==0):
            print('your number is even')
        else:
            print('your number is odd')
        print(str(answer)*10, 'is your number printed 10 times' )
        main()



def startup():
    print('Welcome To Minesweeper')
    print("If you don't know how to Play type 'Help' if you want to play"
          "type 'Play' if you want to change default settings"
          " type 'Settings', for the extra requirements type 'calculator'.\n If you want to stop "
          "playing you can type 'Quit'")
    correctAnswer = False
    while (correctAnswer == False):
        answer = input(':')
        if (answer.lower() == 'help'):
            correctAnswer = True
            helpScreen()
        elif (answer.lower() == 'play'):
            correctAnswer = True
            startGame()
        elif (answer.lower() == 'settings'):
            correctAnswer = True
            changeSettings()
        elif (answer.lower() == 'quit'):
            quit()
        elif (answer.lower() == 'calculator'):
            correctAnswer = True
            calculator()
        else:
            print('Type a valid answer')

def main():
    try:
        # Looks if a settings file already exists
        f = open('settings.txt', 'x')
    except:
        # If it exists it will keep old settings
        print('Old settings detected, Keeping those')
        print('-----------------')
    else:
        # If not it will set the default settings
        f.close()
        f = open('settings.txt', 'w')
        # gridX
        f.write('10\n')
        # gridY
        f.write('10\n')
        # Difficulty
        f.write('7\n')
        f.close()
    startup()


def winGame():
    print('----------------')
    print('YOU WON!')
    validAnswer = False
    while (validAnswer == False):
        answer = input("Type 'P' to play again with same settings"
                       " or type 'R' to go back to main menu.")
        if (answer.lower() == 'p'):
            validAnswer = True
            startGame()
        elif (answer.lower() == 'r'):
            validAnswer = True
            main()
        else:
            print('Invalid Answer')


def endGame():
    print('----------------')
    print('You Lost!')
    validAnswer = False
    while (validAnswer == False):
        answer = input("Type 'P' to play again with same settings"
                       " or type 'R' to go back to main menu.")
        if (answer.lower() == 'p'):
            validAnswer = True
            startGame()
        elif (answer.lower() == 'r'):
            validAnswer = True
            main()
        else:
            print('Invalid Answer')


def checkWin(hiddenGrid, workingGrid):
    correctFlags = 0
    totalBombs = 0
    for y in range(0, len(hiddenGrid)):
        for x in range(0, len(hiddenGrid)):
            if (hiddenGrid[y][x] == 'O' and workingGrid[y][x] == 'F'):
                correctFlags = correctFlags + 1
            if (hiddenGrid[y][x] == 'O'):
                totalBombs = totalBombs + 1
    if (correctFlags == totalBombs):
        winGame()


main()
