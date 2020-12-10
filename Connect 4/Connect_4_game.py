# File: proj2.py
# Author: Fardeen Yaqub
# Date: 11/1/18
# Section: 30
# E-mail: fyaqub1@umbc.edu
# Description: Program allows a user to play connect 4 with another player or against a computer.
# The user chooses how big they want the board to be and can keep playing until they want to quit. 


#For getting a random number
from random import randint

#constants for height and width
MIN_WIDTH = 5
MIN_HEIGHT = 5

#constants for pieces
PIECE_ONE = "X"
PIECE_TWO = "O"


# getUserChoice() asks the user to select a column to place their piece
#                 and checks if their choice is in the allowed range and
#                 and if they can place their piece in the selected column
# Input:          ; the int width and the 2d list board; the int choice
# Output:         the user made
def getUserChoice(board,width):

    gameBoard = board
    boardWidth = width

    choice = int(input("Enter a column to place your piece in (1 - "+ str(boardWidth) + "): "))

    #Makes sure the user enters a valid width
    while choice < 1 or choice > boardWidth:
        choice = int(input(("Invalid number. Enter a column to place your piece in (1 - " + str(boardWidth) + "): ")))

    #Tells the user that the column is full at the place they chose prompts them to enter a correct column
    while gameBoard[0][choice-1] != "-":
        print("This column is full. Try again")
        choice = int(input("Enter a column to place your piece in (1 - " + str(boardWidth) + "): "))

        while choice < 1 or choice > boardWidth:
            choice = int(input("Invalid number. Enter a column to place your piece in (1 - "+ str(boardWidth)+ "): "))

            
    return int(choice)

    
# makeBoard()  makes the board based on the width and height the user
# Input:       chose; the int width and int height; the 2d list board
# Output:      made by the function
def makeBoard(width,height):
    row = []

    for i in range(width):
        row.append("-")

    board = []
    for i in range(height):
        board.append(row[:])

    return board

# getWidth()   gets the width the user wants and validates if it can
# Input:       be used; no input; the int width
# Output:
def getWidth():
    width = int(input("Enter a width: "))

    #Makes user enter a valid width
    while width < MIN_WIDTH:
        print()
        print("Enter a width of at least",MIN_WIDTH)
        width = int(input("Enter a width: "))

    return int(width)


# getHeight()  gets the height the user wants and validates if it can
# Input:       be used; no input; the int height
# Output:
def getHeight():
    height = int(input("Enter a height: "))

    #Makes user enter a valid height
    while height < MIN_HEIGHT:
        print()
        print("Enter a height of at least",MIN_HEIGHT)
        height = int(input("Enter a height: "))

    return int(height)


# placePiece() places the player's piece in the column the player chose
# Input:       on the board; 2d list board, string player's piece,
# Output:      player's int choice, and int height of the board; the
#              updated 2d list board
def placePiece(board,symbol,choice,height):

    gameBoard = board
    piece = symbol
    flag = False
    count = height-1
    userChoice = choice

    #Places the piece in the column the user chose
    while not flag:
        if gameBoard[count][userChoice-1] != "-":
            count -= 1

        elif gameBoard[count][userChoice-1] == "-":
            board[count][userChoice-1] = piece
            flag = True

    return board


# printBoard() prints the game board; the 2d list board; no return
# Input:
# Output:
def printBoard(board):

    gameBoard = board
    
    for row in gameBoard:
        for col in row:
            print(col,end=" ")
        print()

        
# checkTie() Checks if the game is a tie if the board is filled; the
# Input:     2d list board and the int width; a boolean True if tie
# Output:    or False if not tie
def checkTie(board,width):
    gameBoard = board
    gameWidth = width
    count = 0
    flag = False
    
    while count < width:
        if gameBoard[0][count] != "-":
            flag = True
            count += 1
            
        else:
            flag = False
            return flag

    return flag


# checkWin() Checks if the player or computer won the game; the 2d list
# Input:     board and the player or computer's string piece, int width
# Output:    and int height of the board; a boolean True if win or False
#            if not win
def checkWin(board,symbol,width,height):

    gameBoard = board
    piece = symbol
    count = 0
    row = 0
    col = 0
    check = " "
    count = 0
    winCondition = ""

    #Creates win condition
    while count < 4:
        winCondition += symbol
        count += 1
        
        
    #Checks if horizontal win 
    while col < width:
        row = 0
        while row < height:
            check += gameBoard[row][col]
            row += 1

        col += 1
            
        if winCondition in check:
            return True

        else:
            check = ""

    row = 0
    col = 0

    #Checks if vertical win
    while row < height:
        col = 0
        while col < width:
            check += gameBoard[row][col]
            col += 1
    
        row += 1

        if winCondition in check:
            return True

        else:
            check = ""

    row = 0
    col = 0
   #Checks if diagonol win top to bottom for top half of board 
    while col < width:
        row = 0
        count = 0
        while row < height and col + count < width:
            check += gameBoard[row][col+count]
            row += 1
            count += 1

        col += 1
            
        if winCondition in check:
            return True

        else:
            check = ""

    col = 0
    row = 0
    
    #Checks if diagonal win top to bottom for bottom half of board
    while row < height:
        col = 0
        count = 0
        while col < width and row + count < height:
            check += gameBoard[row+count][col]
            col += 1
            count += 1

        row += 1

        if winCondition in check:
            return True

        else:
            check = ""


    col = width - 1
    row = 0

    #Checks if diagnol win bottom to top for bottom half of board
    while row < height:
        col = width-1
        count = 0
        while col >= 0 and row + count < height:
            check += gameBoard[row+count][col]
            col -= 1
            count += 1

        row += 1

        if winCondition in check:
            return True

        else:
            check = ""

            
    row = 0
    col = width - 1

    #Checks if diagnol win bottom to top for top of board
    while col >= 0:
        row = 0
        count = 0
        while row < height and col + count >= 0:
            check += gameBoard[row][col+count]
            row += 1
            count -= 1

        col -= 1

        if winCondition in check:
            return True

        else:
            check = ""

            
# getComputerChoice() computer randomly chooses a column to place their
# Input:              piece in; the int width and 2d list board; the
# Output:             computer's int column choice
def getComputerChoice(board,width):

    gameBoard = board
    gameWidth = width

    choice = 0

    choice = randint(1,width-1)

    
    while gameBoard[0][choice-1] != "-":
        choice = randint(0,width-1)

        
    return int(choice)


        
def main():


    #variable for user to keep playing
    userPlay = "y"

    print("Welcome to Connect 4!")
    
    while userPlay == "y":

        #get Height of board
        height = getHeight()
        
        #get Width of board
        width = getWidth()
        

        win = False
        tie = False

        playerTurn = True
        playerTwoTurn = False
        computerTurn  = False

        playerChoice = 0
        playerTwoChoice = 0
        computerChoice = 0
        
        #creates the gameBoard
        gameBoard = makeBoard(width,height)

        
        computerPlaying = input("Play against the computer? (y/n): ")

        while computerPlaying != "y" and computerPlaying != "n":
            computerPlaying = input("Play against the computer? (y/n): ")

        print()
        
    
        printBoard(gameBoard)
        
        #Game is player vs player
        if computerPlaying == "n":

            #Keeps playing as long as no one won or there isn't a tie
            while win != True and tie != True:

                #Player one's turn
                if playerTurn == True:
                    print()
                    print("Player 1 what is your choice?")

                    #gets player one's choice and puts it on the board
                    playerChoice = getUserChoice(gameBoard,width)
                    gameBoard = placePiece(gameBoard,PIECE_ONE,playerChoice,height)

                    printBoard(gameBoard)
                    
                    #changes turns
                    playerTurn = False
                    playerTwoTurn = True

                    #Checks if player one won
                    win = checkWin(gameBoard,PIECE_ONE,width,height)

                    if win == True:
                        print("Player 1 wins!")

                #Player two's turn
                elif playerTwoTurn == True:
                    print()
                    print("Player 2 what is your choice?")

                    #gets player two's choice and puts it on the board
                    playerTwoChoice = getUserChoice(gameBoard,width)
                    gameBoard = placePiece(gameBoard,PIECE_TWO,playerTwoChoice,height)

                    printBoard(gameBoard)

                    #changes turn
                    playerTurn = True
                    playerTwoTurn = False

                    #Checks if player two won
                    win = checkWin(gameBoard,PIECE_TWO,width,height)
                    if win == True:
                        print("Player 2 wins!")

                #Check if game is a tie
                tie = checkTie(gameBoard,width)
                if tie == True and win != True:
                    print("The game is a tie!")
                    flag = tie


        #Game is player vs computer
        elif computerPlaying == "y": 

            #Keeps playing as long as no one won or there isn't a tie
            while win != True and tie != True:

                #Player one's turn
                if playerTurn == True:
                    print()
                    print("Player 1 what is your choice?")

                    #gets player one's choice and puts it on the board
                    playerChoice = getUserChoice(gameBoard,width)
                    gameBoard = placePiece(gameBoard,PIECE_ONE,playerChoice,height)
                    
                    printBoard(gameBoard)

                    #changes turns
                    playerTurn = False
                    computerTurn = True

                    #Checks if player one won
                    win = checkWin(gameBoard,PIECE_ONE,width,height)

                    if win == True:
                        print("Player 1 wins!")
                        flag = win

                #Computer's turn
                elif computerTurn == True:
            
                    print()
                    print("It is the computer's turn")

                    #gets computer's choice and puts it on the board
                    computerChoice = getComputerChoice(gameBoard,width)
                    gameBoard = placePiece(gameBoard,PIECE_TWO,computerChoice,height)

                    print("The computer chose column:",computerChoice)
                    

                    printBoard(gameBoard)

                    #changes turns
                    playerTurn = True
                    computerTurn = False

                    #Checks if computer won
                    win = checkWin(gameBoard,PIECE_TWO,width,height)

                    if win == True:
                        print("Computer wins!")
                        flag = win


                #Check if game is a tie
                tie = checkTie(gameBoard,width)
                if tie == True:
                    print("The game is a tie!")
                    flag = tie

                    
        if win == True or tie == True:

            userPlay = input("Would you like to play again? (y/n): ")
            while userPlay != "y" and userPlay != "n":
                userPlay = input("Would you like to play again? (y/n): ")

            print()
            
main()
