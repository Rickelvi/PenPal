import functions as f

def printBoard(board):
    """Print a given TicTacToe board stored in a list onto the console."""
    print("|{}|{}|{}|".format(str(board[0]), str(board[1]), str(board[2])))
    print("|{}|{}|{}|".format(str(board[3]), str(board[4]), str(board[5])))
    print("|{}|{}|{}|".format(str(board[6]), str(board[7]), str(board[8])))

def ask(board, op):
    """Ask the user for a tile in the board between 1 and 9 to set their respective play."""
    while True:
        tile = f.inputInt(10, "Tile {}: ".format(op))-1
        
        if tile in range(9):
            if board[tile]=="_":
                board[tile]=op
                f.clear()
                printBoard(board)
                break
            else:
                print("This tile is already occupied by {}!".format(board[tile]))
        else:
            print("Enter a value between 1 and 9!")

    return board

def checkWin(board):
    """Check if the current board configurates a win for one of the players or a tie.

    True return instructs to keep playing for there was not a win condition or a tie.
    False return instructs to stop playing for there was a win condition or a tie.
    """

    #Chech if the value of the diagonals is not null and equal
    if board[0]==board[4]==board[8]!="_":
        print("{} WON!".format(board[0]))
        return False
    if board[2]==board[4]==board[6]!="_":
        print("{} WON!".format(board[2]))
        return False

    #Check if the value in any row or column is not null and equal
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]!="_":
            print("{} WON!".format(board[i]))
            return False
        if board[i*3]==board[i*3+1]==[i*3+2]!="_":
            print("{} WON!".format(board[i*3]))
            return False

    #Count all the filled tiles, if all the tiles are filled and there is not a win, it has been a tie
    for i in range(9):
        if board[i]=="_":
            x=0
            break
        else:
            x=i
            
    if x==8:
        print("It was a tie!")
        return False
    
    return True

def tictactoe():
    """The main function of the TicTacToe game.

    Declare a list of size 9 filled with underscores for the board.
    Alternate between turns for the X player and the O player.
    Check for win conditions after each turn.
    """
    while True:
        board=["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        printBoard(board)

        while True:
            board = ask(board, "X")

            if checkWin(board)==False:
                break
            
            board = ask(board, "O")
            
            if checkWin(board)==False:
                break

        again = input("Play Again? (Y/N)? ")
        f.clear()
        if again.lower()=="n" or again=="2":
            break

tictactoe()
