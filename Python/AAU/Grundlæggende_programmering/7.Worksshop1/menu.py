# menu.py
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget

# menu.py
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainMenu(QWidget):
    def __init__(self, show_game_callback, show_analysis_callback):
        super().__init__()

        # Set the main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)
        
        # Customize buttons
        self.button = QPushButton("Spil kanin")
        self.button.setObjectName("gameButton")
        self.button.clicked.connect(show_game_callback)
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.button2 = QPushButton("Analyse")
        self.button2.setObjectName("analysisButton")
        self.button2.clicked.connect(show_analysis_callback)
        self.button2.setCursor(Qt.CursorShape.PointingHandCursor)

        # Add buttons to layout
        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        self.setLayout(layout)

        # Apply a modern stylesheet
        with open("styling\menuUi.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)


        # Optional: Set window size and title
        self.setWindowTitle("Main Menu")
        self.resize(400, 300)

