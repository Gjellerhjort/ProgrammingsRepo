# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from menu import MainMenu
from gamegui import GameUI
from analysisgui import AnalysisUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kanin Spil")

        # QStackedWidget for switching between main menu and game
        self.stack = QStackedWidget()

        # Create instances of menu and game UI
        self.main_menu = MainMenu(self.show_game, self.show_analysis)
        self.game_ui = GameUI(self.show_main_menu)
        self.analysis_ui = AnalysisUI(self.show_main_menu)
        # Add widgets to the stack
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.game_ui)
        self.stack.addWidget(self.analysis_ui)
        # Set the stack as the central widget
        self.setCentralWidget(self.stack)

    def show_main_menu(self):
        # Switch to the main menu
        self.game_ui.reset_game()  # Reset the game when going back to the main menu
        self.stack.setCurrentWidget(self.main_menu)

    def show_game(self):
        # Switch to the game UI
        self.stack.setCurrentWidget(self.game_ui)

    def show_analysis(self):
        self.stack.setCurrentWidget(self.analysis_ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
