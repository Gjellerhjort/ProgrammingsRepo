board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]


def PrintBoard() -> None:
    for i in board:
        print(i)


def Win():
    return 0

def CheckBoard():
    # check x win
    for i in board:
        if i[0] == i[1] == i[2]:
            print("win")
            Win()
    



def Boardmove(position, player):
    position = map(int, position.split(","))
    board[position] = player["playerIcon"]
    CheckBoard(player)

def main():

    while True:
        PrintBoard()
        position = input("sæt kryds: ")
        Boardmove(position, player1)
        PrintBoard()
        position = input("sæt bolle: ")
        Boardmove(position, player2)



if __name__ == "main":
    player1 = {"Name" : "", "playerIcon": "x", "plays": []}
    player2 = {"Name": "", "playerIcon": "o", "plays": []}  
    main()