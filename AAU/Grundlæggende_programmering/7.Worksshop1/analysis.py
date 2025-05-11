from gamelogic import Game

class GameSimulation:
    def __init__(self):
        pass

    def run_simulation(self, rounds: int, players: int, game_variant: str) -> list[list[float]]:
        player_won_chance: list[list[float]] = [[] for _ in range(players)]
        players_won_times: list[int] = [0] * players

        for round_number in range(rounds):
            game = Game()
            game.set_variant(game_variant)
            players_won = game.auto_play(players)

            # Update the win count for each player who won in this round
            for player in players_won:
                players_won_times[int(player)] += 1

            # Update each player's chance after this round
            for player_number in range(players):
                won_games = players_won_times[player_number]
                chance = (won_games / (round_number + 1)) * 100 if won_games > 0 else 0
                player_won_chance[player_number].append(chance)

        return player_won_chance
