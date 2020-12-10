# File: design3.txt
# Author: Fardeen Yaqub
# Date: 12/1/18
# Section: 30
# E-mail: fyaqub1@umbc.edu
# Description: Program allows the user to play sudoku

#Constants for playing
PLAY = "p"
SOLVE = "s"
UNDO = "u"
SAVE = "s"
QUIT = "q"
MAX = 9

# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ")
    print("  +-------+-------+-------+")

    for i in range(len(board)):
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i])
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1,
                boardRow[0], boardRow[1], boardRow[2],
                boardRow[3], boardRow[4], boardRow[5],
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")

            
# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()


    
# storeFile() reads in and stores a sudoku puzzle from a file
# Input:      fileName; the string text file sudoku game the user wants to play
# Output:     board; the square 2d puzzle (of integers)
def storeFile(fileName):

    board =[]

    #opens the file
    boardLines = open(fileName, "r")

    #loops through the whole file and adds each row to a list
    for i in range(MAX):
       
        lines = boardLines.readline()

        lines = lines.strip()
        lines = lines.split(",")

        board.append(lines)
        

    boardLines.close()

    row = 0
    col = 0

    #Changes any 0 to an under score
    while row <MAX:
        col =0
        while col < MAX:
            if board[row][col] == '0':
                board[row][col] = "_"

            col += 1

        row +=1 

    
    return board


# boardFull() checks if the board is full
# Input:      board; the 2d sudoku board the user is playing
# Output:     boolean; True or False whether or not the board is full
def boardFull(board):

    row = 0
    col = 0

    #Loops through the board checking for empty spaces
    while row < MAX:
        col = 0
        while col < MAX:
            if board[row][col] == "_":
                return False

            else:
                col +=1
        row += 1

    return True
    



# solvePuzzle() solves the sudoku puzzle
# Input:        fileName; the 2d sudoku board the user is playing
#               row; current row of board
#               col; current column of board
#               num; number to add to board
# Output:       solvedBoard; the 2d list solved board
def solvePuzzle(fileName,row,col,num):

    count = 0
    counter = 0

    #Finds the first empty space
    while count < MAX:
        counter = 0
        while counter < MAX:
            if fileName[count][counter] == "_":
                row = count
                col = counter
                count = MAX
                counter = MAX

            counter += 1
        count +=1 

    #When the board is complete
    if boardFull(fileName)== True:
        
        return fileName


    #when the board finds an empty space to place a number
    elif fileName[row][col] == "_":

            
        num = 1
        while num < 10:

            #if the number isn't in the square, row, or column
            if str(num) not in fileName[row] and colChecker(fileName,col,num) == True and squareChecker(fileName,row,col,num) == True:

                #creates a copy of the board
                tempBoard =deepCopy(fileName)

                #adds number to board
                tempBoard[row][col] = str(num)

                #sets solved board equal to result through recursive call
                result = solvePuzzle(tempBoard,row,col,num)
                        
                #if result board is full
                if boardFull(result):
    
                    return result

            num+=1
            
            #Changes the bad number in the board
            fileName[row][col] = "_"

        
    #when an empty slot isn't found
    else:

        if col >= MAX:
            col = 0
            row +=1 

        else:
            col +=1

    return fileName

# colChecker() checks if a number can be placed in a column
# Input:       board; the 2d list sudoku board
#              col; the int col that's being checked
#              num; the number being checked in the column
# Output:      boolean; True or False if the number can be entered
def colChecker(board,col,num):
 
    colList = []

    #creates a list of columns of the board
    for i in range(MAX):
        colList.append(board[i][col])

    #if the number is not in the column
    if str(num) not in colList:
        return True


    return False

# squareChecker() checks if a number can be placed in the square
# Input:          board; the 2d list sudoku board the user is playing
#                 row; the int row that's being checked
#                 col; the int col that's being checked
#                 num; the number being placed in the square
# Output:         boolean: True or False if the number can be entered
def squareChecker(board,row,col,num):

    squareList = []
    count = 0
    colPosition =0
    rowPosition = 0

    #creates a list with the top left square of the board
    if col >= 0 and col <=2 and row >= 0 and row <= 2:
        colPosition = 0
        rowPosition = 0
        while count < 9:
            if colPosition != 3:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 3:
                rowPosition += 1
                colPosition = 0


    #creates a list with the middle top square of the board
    elif col >=3 and col <=5 and row >= 0 and row <=2:
        colPosition = 3
        rowPosition = 0
        while count < 9:
            if colPosition != 6:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1

            elif colPosition == 6:
                rowPosition +=1 
                colPosition = 3

    #creates a list with the top right square of the board
    elif col >=6 and col <=8 and row >= 0 and row <= 2:
        colPosition = 6
        rowPosition = 0
        while count < 9:
            if colPosition != 9:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 9:
                rowPosition += 1
                colPosition = 6

    #creates a list with the middle left square of the board
    elif col >= 0 and col <=2 and row >= 3 and row <= 5:
        colPosition = 0
        rowPosition = 3
        while count < 9:
            if colPosition != 3:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 3:
                rowPosition += 1
                colPosition = 0

    #creates a list with the middle square of the board
    elif col >=3 and col <=5 and row >=3 and row <= 5:
        colPosition = 3
        rowPosition = 3
        while count < 9:
            if colPosition != 6:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 6:
                rowPosition += 1
                colPosition = 3

                
    #creates a list with the middle right square of the board
    elif col >=6 and col <=8 and row >=3 and row <= 5:
        colPosition = 6
        rowPosition = 3
        while count < 9:
            if colPosition != 9:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1

            elif colPosition == 9:
                rowPosition += 1
                colPosition = 6

                
    #creates a list with the top right square of the board            
    elif col >= 0 and col <=2 and row >=6 and row <= 8:
        colPosition = 0
        rowPosition = 6
        while count < 9 and row <=8:
            if colPosition != 3:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 3:
                rowPosition += 1
                colPosition = 0

                
    #creates a list with the middle bottom square of the board
    elif col >=3 and col <=5 and row >= 6 and row <= 8:
        colPosition = 3
        rowPosition = 6
        while count < 9 and row <=8:
            if colPosition != 6:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 6:
                rowPosition += 1
                colPosition = 3

                
    #creates a list with the bottom right square of the board
    elif col >=6 and col <=8 and row >= 6 and row <= 8:
        colPosition = 6
        rowPosition = 6
        while count < 9 and row <=8:
            if colPosition != 9:
                squareList.append(board[rowPosition][colPosition])
                colPosition+= 1
                count += 1
                    
            elif colPosition == 9:
                rowPosition += 1
                colPosition = 6


    #checks if the number is not in the list 
    if str(num) not in squareList:
        
        return True

    return False


# placeNumber() let's the user enter a number onto the board by asking the
#               row, column, and number they want to place
# Input:        board; the 2d list sudoku board
#               row; the int row the user wants to enter a number in
#               col; the int col the user wants to enter a number in
#               num; the int num the user wants to enter
# Output:       updatedBoard; the updated 2d list sudoku board
def placeNumber(board,row,col,num):

    #checks if the user can place a number on the board if there is an empty space
    if board[row][col] == '0' or board[row][col] == "_":
        board[row][col] = num

    else:

        print("You can't put a number here")

    return board


# correctCheck()   Checks if the number the user entered is correct
# Input:           board; the 2d list sudoku board the user is playing
#                  solvedBoard; the 2d list solved sudoku board
#                  row; int row user chose
#                  col; int col user chose
#                  num; the number the user chose
# Output:          correct; the boolean True or False based on placement
def correctCheck(solvedBoard,row,col,num):

    #compares the solved board number to the number the user chose
    if solvedBoard[row][col] != str(num):
        return False

    else:
        return True
    

# checkRow() Checks if the user entered numbers correctly in rows
# Input:     board; the 2d list sudoku board
#            solvedBoard; the 2d list solved sudoku board
# Output:    result: the boolean True or False if rows are correct
def checkRow(board,solvedBoard):

    count = 0
    counter = 0
    check = False

    #loops through the board and checks if the rows are the same as the solved board
    while count < MAX:
        while counter < MAX:
            if str(board[count][counter]) == str(solvedBoard[count][counter]):
                check = True
                counter +=1
        
            else:
                return False

        count += 1

    return check


# checkCol() Checks if the user entered numbers correctly in columns
# Input:     board; the 2d list sudoku board
#            solvedBoard; the 2d list solved sudoku board
# Output:    result: the boolean True or False if columns are correct
def checkCol(board,solvedBoard):

    count = 0
    counter = 0
    check = False

    #loops through the board and checks if the columns are the same as the solved board
    while count < MAX:
        while counter < MAX:
            if str(board[counter][count]) == str(solvedBoard[counter][count]):
                check = True
                counter +=1

            else:
                return False

        count += 1

    return check


# undoMove() Allows the user to undo their most recent move
# Input:     board; the 2d list sudoku board
#            userMoves; 2d list containing users choices
# Ouput:     updatedBoard; the 2d list updated board
def undoMove(board,userMoves):

    lastIndex = len(userMoves)-1
    
    #removes the number from the board
    board[userMoves[lastIndex][len(userMoves[lastIndex])-2]][userMoves[lastIndex][len(userMoves[lastIndex])-1]] = "_"

    
    #removes the row and col from the list
    userMoves.remove(userMoves[lastIndex])
        
    return board


# storeChoice() Stores the row and col the user chooses
# Input:        row; int row user chose
#               col; int col user chose
# Ouput:        choices; list that contains the users choices
def storeChoice(row,col,choices):

    userChoice = []
    
    #adds row and col and num to list choices
    userChoice.append(row)
    userChoice.append(col)

    choices.append(userChoice)

    return choices


# checkPlacement() Checks if user can enter number in chosen position
# Input:           board; the 2d list sudoku board
#                  row; the int row the user chose
#                  col; int col the user chose
#                  num; int num the user chose
# Ouput:           result: boolean True or False if user can place number
def checkPlacement(board,row,col,num):

    result = True

    #If there is already a number in the cell
    if board[row][col] != '0' and board[row][col] != "_":
        print("There is already a number in that cell! Try again.")
        return False

    #If there is already a number in the square
    if squareChecker(board,row,col,num) == False:
        print("The number",num,"is already in that square")
        result= False

    #If there is already a number in the row
    if str(num) in board[row]:
        print("The number",num,"is already in that row")
        result= False

    
    #If there is already a number in the column
    if colChecker(board,col,num) == False:
        print("The number",num,"is already in that column")
        result= False
            
    
    return result


# deepCopy() Creates a deep copy of the sudoku game board
# Input:     board; the sudoku game board
# Output:    copiedBoard; the deep copied sudoku board
def deepCopy(board):

    
    row = 0
    col = 0
    boardList =[]
    copiedBoard = []

    #loops through the board and creates a copy of it
    while row < len(board):
        boardList = []
        col = 0
        while col < len(board[row]):
            boardList.append(board[row][col])

            col += 1
            
        row += 1
        copiedBoard.append(boardList)

    return copiedBoard
    
          
def main():


    userPick = ""
    boardCheck = False
    saveFile = ""

    # int to store user's choice
    userRow = 0
    userCol = 0
    userNum = 0

    numPlacement = False
    
    #win conditions
    rowWin = False
    colWin = False
    squareWin = False


    #variable to store user's choices
    userChoice = []

    
    #Ask for name of board file user wants to play with and store it
    fileName = input("Enter the filename of the Sudoku Puzzle: ")
    gameBoard = storeFile(fileName)

    
    #copy of game board
    copyBoard = deepCopy(gameBoard)

    #print the board the user choose
    prettyPrint(gameBoard)

    #the solved sudoku board
    solvedBoard = solvePuzzle(copyBoard,0,0,1)
    
    #Ask if user wants to play or solve
    userPick = input("play (" +PLAY + ") or solve ("+SOLVE+")? ")

    
    while userPick != PLAY and userPick != SOLVE:
        userPick = input("Do you want to play or solve: ")

        
    #if user chose to solve
    if userPick == SOLVE:

        #print solved board
        prettyPrint(solvedBoard)

    #elif user chose to play
    elif userPick == PLAY:
             
        #Ask if user wants correctness checking
        userPick = input("correctness checking? (y/n): ")

        while userPick != "y" and userPick != "n":
            userPick = input("Incorrect input. Correctness checking? (y/n): ")

        #is user wants correctness checking
        if userPick == "y":
            boardCheck = True

        #while row win is False, col win is False, square win is False and user choice not equals quit
        while (rowWin == False or colWin == False) and boardFull(gameBoard)==False and userPick != "q":
             
            #print board
            prettyPrint(gameBoard)

            #give menu options (play,save,undo,quit)
            userPick = input("play number ("+PLAY+"), save ("+SAVE+"), undo ("+UNDO+"), or quit ("+QUIT+"):")
                        

            #if user chooses to play
            if userPick == PLAY:
                    
                #Ask user for row,col,and square to place piece
                userRow = int(input("Enter a row number (1-9): "))
                userCol = int(input("Enter a column number (1-9): "))
                userNum = int(input("Enter a number to place in cell (" + str(userRow) +","+ str(userCol) +"): "))

                        
                #while user chooses invalid place to put number
                while (userRow < 1 or userRow > MAX) or (userCol < 1 or userCol > MAX) or (userNum < 1 or userNum > MAX):

                    
                    
                    #Ask user for row,col,and square to place piece
                    if userRow < 1 or userRow > MAX:
                        
                        userRow = int(input("Enter a row number (1-9): "))

                    elif userCol < 1 or userCol > 9:
                        print("Invalid column")
                        userCol = int(input("Enter a column number (1-9): "))

                    elif userNum < 1 or userNum > 9:
                        userNum = int(input("You must enter a value in the range 1 to 9. Enter a new value: "))

                            
                #if user chose correctness checking
                if boardCheck == True:

                    #if user num is in wrong place
                    if correctCheck(solvedBoard,userRow-1,userCol-1,userNum) == False:

                        #Tell user their choice is wrong
                        print("OOPS!",userNum,"does not belong in position ("+str(userRow)+","+str(userCol)+")!")

                    #elif user num is in correct place
                    else:
                        
                        #store user choice
                        userChoice = storeChoice(userRow-1,userCol-1,userChoice)

                        #Place number on board
                        gameBoard = placeNumber(gameBoard,userRow-1,userCol-1,userNum)

                        
                #if user didn't choose correctness checking
                elif boardCheck == False:
                    print()
                    numPlacement = checkPlacement(gameBoard,userRow-1,userCol-1,userNum)
                    
                    #if user can't place their number
                    if numPlacement == False:
                        numPlcement = False
                        
                    #if user can place number
                    elif numPlacement == True:
                               
                        #store user choice
                        userChoice = storeChoice(userRow-1,userCol-1,userChoice)

                        #place number on board
                        gameBoard = placeNumber(gameBoard,userRow-1,userCol-1,userNum)
                        

                #checks if user won
                rowWin = checkRow(gameBoard,solvedBoard)
                colWin = checkCol(gameBoard,solvedBoard)


            #if user chooses to save

            elif userPick == SAVE:
                
                #save user board
                saveFile = input("Enter the filename you want to save to: ")
                savePuzzle(gameBoard,saveFile)


            #if user chooses to undo
            elif userPick == UNDO:
                if len(userChoice) == 0:
                    print("There are no moves to undo!")
                    
                else:
                    #undo the user's last choice

                    lastIndex = len(userChoice)-1

                    removeNum = gameBoard[userChoice[lastIndex][len(userChoice[lastIndex])-2]][userChoice[lastIndex][len(userChoice[lastIndex])-1]]
                    removeRow = userChoice[lastIndex][len(userChoice[lastIndex])-2] +1
                    removeCol = userChoice[lastIndex][len(userChoice[lastIndex])-1] +1

                    print("Removed the",removeNum,"you played at position (" +str(removeRow)+ ","+ str(removeCol)+ ").")
                    
                    gameBoard = undoMove(gameBoard,userChoice)
                    


    #if user quit playing
    if userPick == QUIT:
        print("Good bye! Here is the final board:")
        prettyPrint(gameBoard)

    

    #elif user won
    elif rowWin == True and colWin == True:
        
        prettyPrint(gameBoard)
        print("You win!")

main()
