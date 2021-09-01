def printBoard(board):
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")

def ask(board, op):
    while True:
        casa = int(input("Casa do "+op+": "))-1
        if casa in range(9) and board[casa]=="_":
            board[casa]=op
            printBoard(board)
            break
        else:
            print("Comando inválido")

    return board

def checkWin(board):
    x=0
    for i in range(9):
        if board[i]=="_":
            break
        else:
            x=i

    if x==8:
        print("Foi empate!")
        return False
    
    if board[0]==board[4]==board[8]!="_":
        print(board[0] + " venceu!")
        return False
    if board[2]==board[4]==board[6]!="_":
        print(board[2] + " venceu!")
        return False

    for i in range(3):
        if board[i]==board[i+3]==board[i+6]!="_":
            print(board[i] + " venceu!")
            return False
        if board[i*3]==board[i*3+1]==[i*3+2]!="_":
            print(board[i*3] + " venceu!")
            return False
        
    return True

run=True
while run==True:
    board=["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    printBoard(board)

    gameRun=True;
    while gameRun==True:
        board = ask(board, "X")
        
        gameRun = checkWin(board)
        if gameRun==False:
            break
        
        board = ask(board, "O")
        
        gameRun = checkWin(board)

    again = input("Jogar de novo (S/N)? ")
    if again.lower()=="n" or again=="2":
        run=False
