from flask import Flask, render_template, request
import random

app = Flask(__name__)

def initialize_game():
    global board, turn, winner
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    turn = 'O'
    winner = None

def isBoardFull():
    for row in board:
        if ' ' in row:
            return False
    return True

def isEmpty(row, column):
    return board[row][column] == ' '

def isDraw():
    if isBoardFull():
        return True
    return False

def checkWinner(turn):
    for i in range(3):
        if all([cell == turn for cell in board[i]]):
            return True
        if all([board[j][i] == turn for j in range(3)]):
            return True
    if all([board[i][i] == turn for i in range(3)]) or all([board[i][2-i] == turn for i in range(3)]):
        return True
    return False

def get_coordinates(num):
    if 1 <= num <= 9:
        row = (num - 1) // 3
        col = (num - 1) % 3
        return row, col
    else:
        raise ValueError("Number must be between 1 and 9")

@app.route('/')
def home_page():
    return render_template('index.html')

initialize_game()
@app.route('/game-human', methods=['GET','POST'])
def game_human():
    global turn, winner
    tie = False
    if request.method == 'POST':
        if 'reset' in request.form:
            initialize_game()
        elif not winner:
            value = request.form.get('button')
            if value:
                num = int(value)
                row, col = get_coordinates(num)
                if isEmpty(row, col):
                    board[row][col] = turn
                    if checkWinner(turn):
                        winner = ['true',turn]
                    elif isDraw():
                        winner = 'draw'
                    else:
                        turn = 'X' if turn == 'O' else 'O'

    return render_template('game-human.html', board=board, turn=turn, winner=winner, tie=tie)


@app.route('/game-computer', methods=['GET', 'POST'])
def game_computer():
    global turn, winner
    tie = False
    if request.method == 'POST':
        if 'reset' in request.form:
            initialize_game()
        elif not winner:
            value = request.form.get('button')
            if value:
                num = int(value)
                row, col = get_coordinates(num)
                if isEmpty(row, col):
                    board[row][col] = turn
                    if checkWinner(turn):
                        winner = ['true', turn]
                    elif isDraw():
                        winner = 'draw'
                    else:
                        turn = 'X' if turn == 'O' else 'O'

                        # Computer move
                        if not winner and turn == 'X':
                            computer_move()

    return render_template('game-computer.html', board=board, turn=turn, winner=winner, tie=tie)


def computer_move():
    global turn, winner
    available_moves = [(r, c) for r in range(3) for c in range(3) if isEmpty(r, c)]
    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = 'X'
        if checkWinner('X'):
            winner = ['true', 'X']
        elif isDraw():
            winner = 'draw'
        else:
            turn = 'O'

if __name__ == '__main__':
    app.run(debug=True)
