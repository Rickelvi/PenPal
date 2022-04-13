import functions as f
from random import randint

def intToPlay(play):
    """Given the player or computer play as an int, returns its value as a string."""
    if play == 1:
        playStr = "Rock"
    elif play == 2:
        playStr = "Paper"
    elif play == 3:
        playStr = "Scissors"

    return playStr

def rule(c, p):
    """Given two plays, returns the win rule for that set of plays."""
    if c==p:
        pass
    elif (c==1 and p==2) or (c==2 and p==1):
        print("Paper covers Rock!")
    elif (c==1 and p==3) or (c==3 and p==1):
        print("Rock breaks Scissors!")
    elif (c==2 and p==3) or (c==3 and p==2):
        print("Scissors cut Paper!")
        
        
def rpsCompare(comp, player):
    """Compares the two plays and gives their result as a tie, win or loss for the player."""
    rule(comp, player)
    
    if comp == player:
        print("It was a tie!")
    elif comp == player+1 or comp == player-2:
        print("You lost! :c")
    elif player == comp+1 or player == comp-2:
        print("You win! :D")

def rps():
    """Main function to run the Rock, Paper, Scissors.

    Assigns a random play for the computer and asks the player for a play.
    Evaluates the two plays given the rule of evaluation and the result.
    """
    while True:
        comp = randint(1,3)
        
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player = f.inputInt(4)

        print("")
        print("You played {}!".format(intToPlay(player)))
        print("The computer played {}!".format(intToPlay(comp)))
        rpsCompare(comp, player)

        print("")
        run = f.playAgain()
        if run == "n" or run == "2":
            break

    f.clear()

#rps()
