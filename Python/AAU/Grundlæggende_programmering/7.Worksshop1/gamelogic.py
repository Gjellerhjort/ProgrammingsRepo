# gamelogic.py
import random

class Dice:
    def __init__(self, dice_list: list[str] = None) -> None:
        if dice_list is None:
            dice_list = ["green", "blue", "purble", "yellow", "red", "rabbit"]
        self._dice_list = dice_list

    def roll_dice(self) -> str:
        return random.choice(self._dice_list)
    
    def get_dice(self) -> list:
        return self._dice_list
    
    def set_dice_faces(self, dice_list: list) -> None:
        self._dice_list = dice_list

    def get_last_rool(self) -> str:
        return self._dice_list[:1]
    


class Player:
    def __init__(self, name) -> None:
        self.name: str = name
        self.ear_length: int = 0 # This is not being used.
        self.rabbits: int = 0

class Game:
    def __init__(self) -> None:
        self._board = {
            "rabbits": 20,
            "green": 0,
            "blue": 0,
            "purble": 0,
            "yellow": 0,
            "red": 0
        }
        self.dice = Dice()
        self.player_list: list[Player] = []
        self.player_turn: int = 0
        self.game_variant: str = "Normal"


    def add_player(self, name: str) -> None:
        player = Player(name)
        self.player_list.append(player)

    def next_player(self) -> None:
        if self.player_turn < len(self.player_list) - 1:
            self.player_turn += 1
        else:
            self.player_turn = 0

    def roll_dice(self) -> str:
        return self.dice.roll_dice()

    def won_game(self) -> bool:
        return self._board["rabbits"] == 0
        
    def get_rabbits_back(self):
        return self._board["rabbits"]
    
    def player_with_most_rabbits(self) -> list[str]:
        if not self.player_list:
            return []  # Return an empty list if there are no players

        # Find the maximum rabbit count
        max_rabbits = max(player.rabbits for player in self.player_list)
        # Find all players who have this max rabbit count
        players_with_max_rabbits = [
            player.name for player in self.player_list if player.rabbits == max_rabbits
        ]
        
        return players_with_max_rabbits

    def set_variant(self, variant: str) -> None:
        self.game_variant = variant

    def _handle_rabbit_result(self) -> None:
        """Handles the game logic for when the dice lands on 'rabbit'."""
        match self.game_variant:
            case "Normal":
                self.player_list[self.player_turn].rabbits += 1
                self._board["rabbits"] -= 1
            case "Fast":
                result = self.roll_dice()
                self.update_board(result)
            case "Slow":
                self.player_list[self.player_turn].rabbits -= 1
                self._board["rabbits"] += 1

    def _handle_color_result(self, color: str) -> None:
        """Handles the game logic for when the dice lands on a specific color."""
        if self._board[color] == 1:
            self.player_list[self.player_turn].rabbits += 1
            self._board["rabbits"] -= 1
            self._board[color] = 0
        else:
            self._board[color] = 1

    def update_board(self, result: str) -> None:
        """
        Updates the board state based on the result of a dice roll.

        Args:
            result (str): The result from the dice roll (e.g., color or 'rabbit').
        """
        if result == "rabbit":
            self._handle_rabbit_result()
        else:
            self._handle_color_result(result)


    def auto_play(self, player_count: int) -> list:
        """
        Automatically simulates a game with a given number of players until a winner is determined.

        Args:
            player_count (int): Number of players to simulate.

        Returns:
            List[str]: List of player names who won the game.
        """
        for player_n in range(player_count):
            self.add_player(str(player_n))

        while not self.won_game():
            dice_result: str = self.roll_dice()
            self.update_board(dice_result)
            self.next_player()
        return self.player_with_most_rabbits()