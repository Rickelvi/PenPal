import tictactoe

def gamesMenu():
    while True:
        print("CHOOSE YOUR GAME:\n")
        print("1. TicTacToe")
        print("2. Back")

        choice = 0
        while choice != 1:
            choice = int(input())

        if choice==1:
            tictactoe.tictactoe()
            choice=0
        else:
            break
        
def main():
    while True:
        print("\t\tPENPAL!\n")
        print("1. Two-Player Game")
        print("2. Quit")

        choice=0
        while choice not in range(1,3):
            choice = int(input())

        if choice==1:
            gamesMenu()
        else:
            break
        
main()
