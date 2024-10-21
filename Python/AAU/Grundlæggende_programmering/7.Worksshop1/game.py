import random

class Dice:
    def __init__(self, dice_list: list[str] = None) -> None:
        if dice_list is None:
            dice_list = ["green", "blue", "purble", "yellow", "red", "rabit"]
        self._dice_list = dice_list

    def rollDice(self) -> str:
        return random.choice(self._dice_list)
    
    def getDice(self) -> list:
        return self._dice_list
    
    def setDice(self, dice_list: list) -> None:
        self._dice_list = dice_list

'''
class Board(object):
    def __init__(self) -> None:
'''        
class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.ear_length: int = 0
        self.rabits: int = 0
         

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

    def gameRound(self) -> None:
        while self._board["rabits"] > 0:
            player_name = self.player_list[self.player_turn].name
            print(f"{player_name}'s turn")
            menu = input("Game menu\n 1.roll dice\n 2.stop game\n>")
            match menu:
                case "1":
                    options = self.dice.rollDice()
                    print(f"you rolled {options}")
                    if options == "rabit":
                        self.player_list[self.player_turn].rabits + 1
                        self._board["rabits"] = self._board["rabits"]-1
                    else:
                        if self._board[options] == 1:
                            self.player_list[self.player_turn].rabits += 1
                            self._board[options] = 0
                        else:
                            self._board[options] == 1
                    self.nextPlayer()
                case "2":
                    exit()
        print("game finish")

    def nextPlayer(self) -> None:
        if self.player_turn < len(self.player_list)-1:
            self.player_turn = self.player_turn + 1
        else:
            self.player_turn = 0
        print(self.player_turn)
        self.gameRound()



    def gameStart(self) -> None:
        print("Velkommen til kanin spillet")
        self.player_turn = 0
        self.gameRound()


    def createPlayer(self) -> None:
        name = input("Player Name:")
        playerIns = Player(name)
        self.player_list.append(playerIns)
        self.gameSetup()

    def gameSetup(self) -> list[Player]:
        menu = input("Game menu\n 1.create player\n 2.start game\n>")
        match menu:
            case "1":
                self.createPlayer()
            case "2":
                self.gameStart()        

game = Game()
game.gameSetup()
