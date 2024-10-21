import sys
from PyQt6.QtCore import QTimer, QEventLoop, Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
    QMessageBox,
    QHBoxLayout,
    QFormLayout,
)
from gamelogic import Game

class GameUI(QWidget):
    def __init__(self, go_back_callback):
        super().__init__()

        self.game = Game()  # Initialize the game instance
        self.setup_ui(go_back_callback)

        # Apply modern styling
        with open("styling\gameUi.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)

    def setup_ui(self, go_back_callback):
        # Main layout for the game screen
        self.game_layout = QVBoxLayout()
        self.game_layout.setContentsMargins(40, 40, 40, 40)
        self.game_layout.setSpacing(20)

        # Back button to return to main menu
        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(go_back_callback)
        self.back_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Create a horizontal layout for the back button
        back_layout = QHBoxLayout()
        back_layout.addWidget(self.back_button)
        back_layout.addStretch()

        # Player name input section
        self.player_name_label = QLabel("Enter Player Name:")
        self.player_name_input = QLineEdit()
        self.player_name_input.setPlaceholderText("e.g. John")

        self.add_player_button = QPushButton("Add Player")
        self.add_player_button.setObjectName("addPlayerButton")
        self.add_player_button.clicked.connect(self.add_player)
        self.add_player_button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.start_game_button = QPushButton("Start Game")
        self.start_game_button.setObjectName("startGameButton")
        self.start_game_button.clicked.connect(self.start_game)
        self.start_game_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Game status display
        self.status_label = QLabel("Welcome to the game!")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Rabbit count display for each player
        self.player_rabbit_labels = []
        self.rabbit_layout = QVBoxLayout()

        # Add layouts and widgets to the main layout
        self.game_layout.addLayout(back_layout)
        self.add_player_input_layout()
        self.game_layout.addWidget(self.status_label)

        # Set the layout
        self.setLayout(self.game_layout)

    def add_player_input_layout(self):
        """Add the player input layout to the main layout."""
        # Form layout for player name input
        input_layout = QFormLayout()
        input_layout.setSpacing(15)

        input_layout.addRow(self.player_name_label, self.player_name_input)
        input_layout.addRow(self.add_player_button, self.start_game_button)

        self.input_layout = input_layout
        self.game_layout.addLayout(self.input_layout)

    def add_player(self):
        """Add a player to the game."""
        player_name = self.player_name_input.text()
        if player_name:
            self.game.add_player(player_name)
            self.player_name_input.clear()
            self.status_label.setText(f"Player {player_name} added!")
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid name!")

    def start_game(self):
        """Start the game if at least one player is added."""
        if not self.game.player_list:
            QMessageBox.warning(self, "Game Error", "Add at least one player before starting!")
            return
        
        self.status_label.setText(f"Game started! {self.game.player_list[0].name}'s turn")
        self.display_rabbit_counts()

        # Hide the input section after starting the game
        self.hide_player_input()

        # Add the rabbit layout to the main game layout
        self.rabbit_layout = QVBoxLayout()
        self.rabbit_layout.addWidget(QLabel("Rabbit Counts:"))
        self.game_layout.addLayout(self.rabbit_layout)

        # Show the roll dice button
        self.roll_dice_button = QPushButton("Roll Dice")
        self.roll_dice_button.clicked.connect(self.roll_dice)
        self.roll_dice_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.game_layout.addWidget(self.roll_dice_button)

        # Refresh the layout to show the updates
        self.game_layout.update()

    def hide_player_input(self):
        """Hide the player input fields."""
        if self.input_layout:
            self.clear_layout(self.input_layout)
            self.input_layout.deleteLater()

    def roll_dice(self):
        """Roll the dice for the current player and update the game state."""
        if not self.game.player_list:
            QMessageBox.warning(self, "Game Error", "Please start the game first!")
            return

        result = self.game.roll_dice()
        self.game.update_board(result)

        if self.game.won_game():
            players_won = self.game.player_with_most_rabbits
            if players_won is None:
                QMessageBox.warning(self, "Game Error", "Something went wrong!")
            else:
                self.display_won_game(players_won)

        current_player = self.game.player_list[self.game.player_turn].name
        self.status_label.setText(f"{current_player} rolled {result}!")
        self.blocking_wait(500)
        self.game.next_player()
        self.display_rabbit_counts()

        next_player = self.game.player_list[self.game.player_turn].name
        self.status_label.setText(f"Next turn: {next_player}")
    
    def display_won_game(self, players):
        QMessageBox.information(self, "Game Over", f"{', '.join(players)} won the game!")
        self.reset_game()

    def display_rabbit_counts(self):
        """Display the current number of rabbits for all players."""
        self.clear_rabbit_labels()

        for player in self.game.player_list:
            rabbit_label = QLabel(f"{player.name} has {player.rabits} rabbits")
            self.rabbit_layout.addWidget(rabbit_label)
            self.player_rabbit_labels.append(rabbit_label)

    def clear_rabbit_labels(self):
        """Clear previous rabbit labels from the layout."""
        for label in self.player_rabbit_labels:
            self.rabbit_layout.removeWidget(label)
            label.deleteLater()
        self.player_rabbit_labels.clear()

    def clear_layout(self, layout):
        """Clear all widgets from a layout."""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def reset_game(self):
        """Reset the game state."""
        self.game = Game()  # Create a new Game instance
        self.clear_rabbit_labels()
        self.status_label.setText("Welcome to the game!")
        self.player_name_input.clear()
        self.add_player_input_layout()

        if hasattr(self, 'roll_dice_button') and self.roll_dice_button:
            self.roll_dice_button.setParent(None)

    def blocking_wait(self, milliseconds):
        loop = QEventLoop()
        QTimer.singleShot(milliseconds, loop.quit)
        loop.exec()
