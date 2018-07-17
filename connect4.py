# connect 4  for codebreakers
import time
import random
import os

def play():
    board = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ',
                                                                    ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
    os.system('clear')
    print("Welcome to Connect 5! Why don't you play first?")
    pprint(board)
    game_over = False
    while not game_over:
        user_turn(board)
        os.system('clear')
        pprint(board)
        if is_win(board):
            game_over = True
            win(True)
            return
        print("The computer is thinking....")
        time.sleep(1)
        computer_move(board)
        os.system('clear')
        pprint(board)
        if is_win(board):
            game_over = True
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
        first = True
        for y in range(5):
            if board[y][x] != ' ':
                if first:
                    char = board[y][x]
                    first = False
                elif board[y][x] != char:
                    win = False
                    break
                win = True
            else:
                win = False
                break
        if win:
            return True

    # check rows
    win = False
    char = ' '
    for x in range(5):
        first = True
        for y in range(5):
            if board[x][y] != ' ':
                if first:
                    char = board[x][y]
                    first = False
                elif board[x][y] != char:
                    win = False
                    break
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
        input()
    else:
        print("Oh no! The computer won...Better luck next time!", u'\U0001f4A3')
        input()
    return


def computer_move(board):
    while True:
        comp_move = int(random.random() * 5)
        if is_valid(board, comp_move):
            break
    update_board(board, comp_move, u'\U0001f621')
    return
