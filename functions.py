from os import system

console = 0

def clear():
    """Using a system function to clear the console.

    It is not implemented in the interpreter.
    Whether or not it is on the interpreter or console is defined with the test variable console.
    """
    if console==1:
        system('cls')
    else:
        print("")

def inputInt(lim, prompt=""):
    """Ask the player for an integer within a determined bound catching ValueErrors."""
    while True:
        try:
            choice = 0
            while choice not in range(1, lim):
                choice = int(input(prompt))
                if choice not in range(1,lim):
                    print("Please, enter a value between 1 and {}!".format(lim-1))
            break
        #If the value is not an integer
        except ValueError:
            print("Please, enter a value between 1 and {}!".format(lim-1))

    return choice

def playAgain():
    """Ask the player whether to play again or not."""
    valid, run = "yn12", "0"
    while run[0].lower() not in valid:
        run = input("Play Again? (Y/N)? ")

    return run
