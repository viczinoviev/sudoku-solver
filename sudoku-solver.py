#Initial state of board in form of a list of list of ints    
board = [
    [7, 0, 8, 0, 6, 0, 0, 2, 1],
    [0, 0, 0, 2, 0, 0, 4, 0, 0],
    [0, 0, 1, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 4, 6, 0, 0, 0, 5, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [4, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 9, 5, 0, 0, 0, 1, 6]
]

#Solves board through testing numbers and backtracking until
#the board is completely filled.
#Takes board as input and modifies the board
def solve(board):
    find = findEmpty(board)
    #Base case
    #Solution must be found if there is no more empty spots
    if not find:
        return True
    else:
        row, column = find
    
    for i in range(1, 10):
        #Assume that i is the solution for position(row, column)
        if check(board, (row, column), i):
            board[row][column] = i

            #Recursion: move onto next cell
            if solve(board):
                return True
            
            #Assumption was incorrect, backtrack and repeat
            board[row][column] = 0
    
    return False

#Checks if placing num on board at position(row, column) is legal
#Returns bool
def check(board, position, num):
    #Check row
    for i in range(len(board[position[0]])):
        if board[position[0]][i] == num and i != position[1]:
            return False
    #Check column
    for j in range(len(board)):
        if board[j][position[1]] == num and j != position[0]:
            return False

    #Find 3x3 grid where position lives
    gridy = (position[0] // 3) * 3
    gridx = (position[1] // 3) * 3

    #Check 3x3 grid
    for i in range(gridy, gridy + 3):
        for j in range(gridx, gridx + 3):
            if board[i][j] == num and (i, j) != position:
                return False
    return True

#Finds the first empty spot(0) on the board searching top to bottom, left to right.
#Takes a board as input, returns tuple (row, column). Returns None if no empty spot is found.
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

#Prints out the sudoku board, taking a board as input
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end="")

solve(board)
printBoard(board)