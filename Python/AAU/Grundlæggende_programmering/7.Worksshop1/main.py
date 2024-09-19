import random

class Dice:
    def __init__(self, dice_list: list[str] = None) -> None:
        if dice_list is None:
            dice_list = ["green", "blue", "purble", "yellow", "red", "rabit"]
        self._dice_list = dice_list

    def roolDice(self) -> str:
        return random.choice(self._dice_list)
    
    def GetDice(self) -> list:
        return self._dice_list
    
    def SetDice(self, dice_list: list) -> None:
        self._dice_list = dice_list

'''
class Board(object):
    def __init__(self) -> None:
'''        
class Player:
    def __init__(self, name, rabits, ear_length) -> None:
        self.name: str = name
        self.ear_length: int = ear_length
        self.rabits: int = rabits
         

class Game():
    def __init__(self) -> None:
        board = {
                "rabits": 20,
                "green" : 0,
                "blue" : 0,
                "purble": 0,
                "yellow": 0,
                "red": 0
            }
        self._board = board
        self.dice = Dice()
        self.player_list: list[Player] = []


    def choseGameVariant(self, variant: int) -> None:
        self.game_variant = variant

    def nextPlayer() -> None:
        

    def gameStart():
        print("Velkommen til kanin spillet")
        player_turn = 0
    def addPlayer():

    def createPlayer(self, name: str):
        name = input("Player Name")
        playerIns = Player()
        playerIns.name = name
        self.player_list.append(playerIns)
    def gameSetup(self) -> list[Player]:
        menu = input("Game menu\n 1.create player\n 2.start game\n>")
        match menu:
            case 1:
                self.createPlayer()
            case 2:
                self.gameStart()        



'''

if __name__ == "main":
'''