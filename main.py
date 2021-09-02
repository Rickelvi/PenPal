import functions as f
import rps
import tictactoe

def gamesMenu(players):
    """A menu for choosing the available pen and paper games to play."""
    while True:
        print("CHOOSE YOUR GAME:\n")

        if players==1:
            print("1. Rock, Paper, Scissors")
            print("2. Back")

            choice = f.inputInt(4)
            f.clear()
            
            if choice==1:
                rps.rps()
                choice=0
            else:
                break
            
        elif players==2:
            print("1. TicTacToe")
            print("2. Back")

            choice = f.inputInt(4)
            f.clear()
            
            if choice==1:
                tictactoe.tictactoe()
                choice=0
            else:
                break
        
def mainMenu():
    """The game hub main menu, allowing to exit the console."""
    while True:
        print("\t\tPENPAL!\n")
        print("1. One-Player Game")
        print("2. Two-Player Game")
        print("3. Quit")
        
        players = f.inputInt(4)
        f.clear()

        if players in range(1,3):
            gamesMenu(players)
        else:
            break
        
mainMenu()
