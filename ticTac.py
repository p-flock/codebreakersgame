from random import random
import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

########win Flags##########
Win = 1
Draw = -1
Running = 0
Stop = 1
###########################

Game = Running
Mark = 'X'
turn = 1
def keepPlaying():
    global board
    global Game
    global turn
    response = input("want to play again? Y/N?" + "\n")
    if response in ["y", "Y", "YES", "yes"]:
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        Game = Running
        turn = 1
        return play()
    else:
        return
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))


def checkWin():
    global Game
    if (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game=Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game=Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=Win
    elif (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game=Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game=Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game=Win
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game=Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=Win
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game = Running


def play():
    global Game
    global turn
    global Mark
    while(Game == Running):
        Game = Running
        os.system('clear')
        DrawBoard()
        if(turn % 2 != 0):
            print("Your turn!")
            Mark = 'X'
            pick = int(input("Where do you want to make your mark 1-9?" + "\n"))
            if pick not in [1,2,3,4,5,6,7,8,9]:
                pick = int(input("Sorry, that's not an option, please try again" + "\n"))
            if board[pick] != ' ':
                pick = int(input("Sorry, that spot is taken" + "\n"))
            board[pick] = Mark
            turn+=1
            checkWin()

        else:
            print("Computer's Turn!")
            time.sleep(1)
            Mark = 'O'
            pick = int(random()*9 + 1)
            while board[pick] != ' ':
                pick = int(random()*9 + 1)
            print("The computer chose", pick)
            time.sleep(1)
            board[pick] = '0'
            turn+=1
            checkWin()

    os.system('clear')
    DrawBoard()
    if(Game==Draw):
        print("Game Draw")
    elif(Game==Win):
        turn-=1
        if(turn%2!=0):
            print("You Won!")
            input()
        else:
            print("Computer Won!")
            input()
