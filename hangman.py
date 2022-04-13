import functions as f
from string import ascii_uppercase

##        A B C D E F G H
##        I J K L M N O P
##        Q R S T U V W X
## ____
##|    |
##|    O   
##|   /|\
##|   / \
##|
##        ___________

def draw(guessed_letters, body, under, tip):
    """Draw the hangman's graphics. Add parts with each miss."""
    guessed_string = ""
          
    for i in range(0, len(guessed_letters)):
        guessed_string += guessed_letters[i]+" "
        if i>0 and i%7 == 0:
            guessed_string += "\n"

    print(guessed_string)

    print(" ____  ")
    print("|    | ")
    print("|    {} ".format(body[0]))
    print("|   {}{}{}".format(body[2], body[1], body[3]))
    print("|   {} {}".format(body[4], body[5]))
    print("|      ")
    print("\t{}".format("".join(under)))
    print("\t{}".format(tip))
    

def increase_miss(body, miss):
    if miss == 1:
        body[0] = "O"
    if miss == 2:
        body[1] = "|"
    if miss == 3:
        body[2] = "/"
    if miss == 4:
        body[3] = "\\"
    if miss == 5:
        body[4] = "/"
    if miss == 6:
        body[5] = "\\"

    return body

def hangman():
    """Main function for the Hangman game."""
    while True:
        body = [" ", " ", " ", " ", " ", " "]
        miss = 0
        guessed_letters = ""

        f.clear()
        word = input("Enter a word: ").upper()
        tip = input("Enter a tip: ")
        under = []

        for i in range(len(word)):
            under.append("_")

        while True:
            guess = ""

            f.clear()
            draw(guessed_letters, body, under, tip)
            
            while len(guess) != 1 or guess not in ascii_uppercase or guess in guessed_letters:
                guess = input("Guess a letter: ").upper()

            guessed_letters += guess
            
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        under[i] = guess
            else:
                miss += 1
                body = increase_miss(body, miss)

            if "_" not in under:
                f.clear()
                draw(guessed_letters, body, under, tip)
                print("You won! :D")
                break
            if miss == 6:
                f.clear()
                draw(guessed_letters, body, under, tip)
                print("You lost! Sorry!")
                print("The word was {}!".format(word))
                break

        print("")
        run = f.playAgain()
        if run == "n" or run == "2":
            break

    f.clear()
            
#hangman()
