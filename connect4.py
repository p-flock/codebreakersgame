# connect 4  for codebreakers
import time
import random
import os

def play():
    board = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ',
                                                                    ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    print("Welcome to Connect 4! Why don't you play first?")
    pprint(board)
    while True:
        user_turn(board)
        os.system('clear')
        pprint(board)
        if is_win(board):
            win(True)
            return
        print("The computer is thinking....")
        time.sleep(1)
        computer_move(board)
        os.system('clear')
        pprint(board)
        if is_win(board):
            win(False)
            return


def user_turn(board):
    while True:
        move = get_move() - 1
        if is_valid(board, move):
            break
        else:
            print("that column is full, please choose another move.")

    update_board(board, move, u'\U0001f604')
    return


def is_valid(board, move):
    # check column
    if board[0][move] == ' ':
        return True
    else:
        return False


def pprint(board):
    print("\n")
    for row in board:
        print("\t", end="")
        for col in row:
            if col == ' ':
                print("|", " " + col + " ", end="")
            else:
                print("|", col + " ", end="")
        print("|", end="")
        print()
    print("\t" + "-"*26)
    print("\t|  1 |  2 |  3 |  4 |  5 |")
    return


def get_move():
    return int(input("what column do you want to play on?: "))


def update_board(board, move, symbol):
    for x in range(5)[::-1]:
        if board[x][move] == ' ':
            board[x][move] = symbol
            return board
    return False


def is_win(board):
    # check columns
    win = False
    char = ' '
    for x in range(5):
        win = False
        for y in range(5):
            if board[y][x] != ' ' and board[y][x] == char:
                char = board[y][x]
                win = True
            else:
                win = False
                break
        if win:
            return True

    # check rows
    char = ' '
    for x in range(5):
        win = False
        for y in range(5):
            if board[x][y] != ' ' and board[x][y] == char:
                char = board[x][y]
                win = True
            else:
                win = False
                break
        if win:
            return True

    return False


def win(user_won):
    if user_won:
        print("congratulations! You beat the all-mighty computer")
    else:
        print("Oh no! The computer won...Better luck next time!")

def computer_move(board):
    while True:
        comp_move = int(random.random() * 5)
        if is_valid(board, comp_move):
            break
    update_board(board, comp_move, u'\U0001f621')
    return
