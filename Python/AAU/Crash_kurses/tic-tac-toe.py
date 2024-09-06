board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

player1 = {"Name" : "", "playerIcon": "x", "plays": []}
player2 = {"Name": "", "playerIcon": "o", "plays": []}  

def PrintBoard():
    for i in range(0, 8, 3):
        print(board[i]+board[i+1]+board[i+2])

def Win(player):
    print(f"{player["Name"]} won this game of tic tac toe")

def CheckBoard(player):
    # check x win
    for i in range(0,3):
        if board[i] == board[i+1] == board[i+2] != "-":
            Win(player)
        if board[i] == board[i+3] == board[i+5] != "-":
            print(board[i] + board[i+3] + board[i+5])
            Win(player)
        

def Boardmove(position, player):
    board[int(position)-1] = player["playerIcon"]
    CheckBoard(player)

def GameSetup():
    name = input("Player 1 choose a name: ")
    player1["Name"] = name
    name = input("Player 2 choose a name: ")
    player2["Name"] = name

def main():
    GameSetup()
    while True:
        PrintBoard()
        position = input(f"{player1["Name"]} set a x: ")
        Boardmove(position, player1)
        PrintBoard()
        position = input(f"{player2["Name"]} set a o: ")
        Boardmove(position, player2)



main()

