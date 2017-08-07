# create baard
board = [[1,2,3], [4,5,6], [7,8,9]]
player_marker = ''
ai_marker = ''

'''
Step 1: Write a function that can print out a board.
Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''

def display_board(board):
    for row in board:
        for cell in row:
            if cell == 'X' or cell == 'O':
                print(cell + ' ', end='')
            else:
                print("_ ", end='')
        print()


#test function -
display_board(board)

'''
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
'''

def player_input():
    # print("Select: X or O")
    choice = ''
    while True:
        choice = input('Select: X or O \n')
        if choice.lower() == 'x' or choice.lower() == 'o':
            break
        else:
            continue

# test function
# player_input()

'''
Step 3: Write a function that takes, in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''

def place_marker(board, marker, position):
    # global board
    if position in range(1, 4):
        board[0][position-1] = marker
    elif position in range(4,7):
        board[1][position-4] = marker
    elif position in range(7,10):
        board[2][position-7] = marker
    else:
        print("Bad position")
    # print(board)


#
# def player_position():
#     pos = input("Enter position(1-9")
#     pos = int(pos)
#

# test
place_marker(board, 'X', 6)
print()
display_board(board)

