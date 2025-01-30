board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
turn = 'O'

def isBoardFull():
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                return False
    return True

def isEmpty(row, column):
    if board[row][column] == ' ':
        return True
    return False

def getData():
    row = int(input("Enter Row Number : "))
    column = int(input("Enter Column Number : "))
    return row - 1, column - 1

def checkWinner(turn):
    rows = board
    columns = []
    diagonal1 = []
    diagonal2 = []
    for row in range(3):
        diagonal2.append(board[row][2 - row])
        board_transpose = []
        for i in board:
            board_transpose.append(i[row])
        columns.append(board_transpose)
        for column in range(3):
            if row == column:
                diagonal1.append(board[row][column])
    if [turn,turn,turn] in rows+columns:
        return True
    elif [turn,turn,turn] == diagonal1:
        return True
    elif [turn,turn,turn] == diagonal2:
        return True
    return False

def printBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


while not isBoardFull():
    print(f"{turn}'s Turn ")
    row, column = getData()
    try:
        if isEmpty(row, column):
            board[row][column] = turn
            if turn == 'X':
                turn = 'O'
            elif turn == 'O':
                turn = 'X'
            printBoard()
        else:
            print("Try Again!!")
    except IndexError:
        print("Enter values within 1 and 3")
    if checkWinner('X'):
        print("'X' is winner")
        break
    if checkWinner('O'):
        print("'O' is winner")
        break
