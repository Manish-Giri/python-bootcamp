# create baard
board = [[1,2,3], [4,5,6], [7,8,9]]

'''
Step 1: Write a function that can print out a board.
Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''

def display_board(board):
    for row in board:
        for cell in row:
            print("_ ", end='')
        print()


display_board(board)