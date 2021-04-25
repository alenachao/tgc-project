#tic tac toe

# defining variables and functions
Board = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []
turn = 'X'
count = 0

for key in Board:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

printBoard(Board)

# the actual game part
for i in range(10):
    move = input("It's your turn, Player " + turn + ". Where would you like to move? ")
    while True:
        if Board[move] != ' ':
            move = input("That place is already filled. Where would you like to move? ")
        else:
            Board[move] = turn
            printBoard(Board)
            count += 1
            break

    # Checking if player X or O has won
    if count >= 5:
        if Board['7'] == Board['8'] == Board['9'] != ' ' or \
            Board['4'] == Board['5'] == Board['6'] != ' ' or \ 
            Board['1'] == Board['2'] == Board['3'] != ' ' or \
            Board['1'] == Board['4'] == Board['7'] != ' ' or \ 
            Board['2'] == Board['5'] == Board['8'] != ' ' or \ 
            Board['3'] == Board['6'] == Board['9'] != ' ' or \
            Board['7'] == Board['5'] == Board['3'] != ' ' or \ 
            Board['1'] == Board['5'] == Board['9'] != ' ': 
            print("Game Over, Player " + turn + " won!")
            break

    # If neither X nor O wins and the board is full, it is a tie
    if count == 9:
        print("Game Over, it's a tie!")

    # Switching players after each turn
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'
