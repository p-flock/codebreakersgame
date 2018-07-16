# 2018 Codebreakers
#
import connect4
# import tictactoe
import os

games = {'quit': quit, 'connect4': connect4.play, 'tic-tac-toe': tictactoe.play}


def main():
    while True:
        choice = menu()
        run_game(games[choice])


def run_game(choice):
    choice()
    return


def menu():
    os.system('clear')
    print("Welcome to The Codebreakers Game Extravaganza!!!\n")
    print("What game would you like to play?\n")
    print("1. Connect 4\n")
    print("2. Tic Tac Toe\n")
    print("enter 0 to quit")

    games = ['quit', 'connect4', 'tic-tac-toe']
    while True:
        choice = input("enter the number corresponding to your choice:\t")
        if ((type(int(choice)) != int) or ((int(choice) < 0) or (int(choice) > 2))):
            print("please enter a valid number")
            break
        else:
            return games[int(choice)]


def quit():
    print("Goodbye! Thanks for playing!\n")
    os.exit()


if __name__ == "__main__":
    main()
