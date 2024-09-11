
def PrintBoard(board):
    for i in range(0, 8, 3):
        print(board[i]+board[i+1]+board[i+2])

def Win(player):
    print(f"{player["Name"]} won this game of tic tac toe")
    main()

def CheckBoard(player, board):
    # check x win
    for i in range(0,3):
        if board[i] == board[i+1] == board[i+2] != "-":
            Win(player)
        if board[i] == board[i+3] == board[i+6] != "-":
            Win(player)
    if board[0] == board[4] == board[8] != "-":
        Win(player)
    if board[2] == board[4] == board[6] != "-":
        Win(player)

def Boardmove(player, board):
    position = input(f"{player["Name"]} set a {player["playerIcon"]}: ")
    if position == None or not position.isdigit():
        print("Please type a number")
        Boardmove(player, board)
    if board[int(position)-1] == "-":
        board[int(position)-1] = player["playerIcon"]
    else:
        print("You can place here")
        Boardmove(player, board)
    CheckBoard(player, board)

def GameSetup():
    board = ["-", "-", "-", 
             "-", "-", "-", 
             "-", "-", "-"]

    player1 = {"Name" : "", "playerIcon": "x", "plays": []}
    player2 = {"Name": "", "playerIcon": "o", "plays": []}  

    name = input("Player 1 choose a name: ")
    player1["Name"] = name
    name = input("Player 2 choose a name: ")
    player2["Name"] = name
    return board, player1, player2

def main():
    board, player1, player2 = GameSetup()
    PrintBoard(board)
    while True:
        Boardmove(player1, board)
        PrintBoard(board)
        Boardmove(player2, board)
        PrintBoard(board)

main()

