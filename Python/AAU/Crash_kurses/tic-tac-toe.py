
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
plays = [None, None, None]
player1 = {"Name" : "", "playerIcon": "x", "plays": plays}
player2 = {"Name": "", "playerIcon": "o", "plays": plays}

def PrintBoard():
    for i in board:
        print(i)

def CheckBoard():
    # check x win
    for i in board:
        if i[0] == i[1] == i[2]:
            print("win")
    



def Boardmove(move, player):
    x,y = map(int, move.split(","))
    board[y-1][x-1] = player["playerIcon"]
    CheckBoard()

while True:
    PrintBoard()
    move = input("sæt kryds: ")
    Boardmove(move, player1)
    PrintBoard()
    move = input("sæt bolle: ")
    Boardmove(move, player2)



