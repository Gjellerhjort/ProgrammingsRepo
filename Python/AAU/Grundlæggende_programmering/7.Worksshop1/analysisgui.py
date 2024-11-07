import matplotlib as plt
plt.use('QtAgg')

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QFormLayout,
    QComboBox,
)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from analysis import GameSimulation

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class AnalysisUI(QWidget):
    def __init__(self, go_back_callback):
        super().__init__()

        self.setup_ui(go_back_callback)

        # Apply modern styling
        with open("styling/analysisUi.qss", "r") as f:
            _style = f.read()
            self.setStyleSheet(_style)


    def setup_ui(self, go_back_callback):
        # Main layout for the game screen
        self.analysis_layout = QVBoxLayout()
        self.analysis_layout.setContentsMargins(50, 50, 50, 50)
        self.analysis_layout.setSpacing(20)

        # Back button to return to main menu
        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(go_back_callback)
        self.back_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Create a horizontal layout for the back button
        back_layout = QHBoxLayout()
        back_layout.addWidget(self.back_button)
        back_layout.addStretch()

        self.graph_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.analysis_layout.addLayout(back_layout)
        self.analysis_layout.addWidget(self.graph_canvas)
        self.analysis_settings_layout()

        # Set the layout
        self.setLayout(self.analysis_layout)

    def analysis_settings_layout(self):
        # Create form layout for input fields
        settings_layout = QFormLayout()
        settings_layout.setSpacing(15)

        # Number of players input section
        self.player_number_label = QLabel("Enter number of players:")
        self.player_number_input = QLineEdit()
        self.player_number_input.setPlaceholderText("e.g. 4")

        # Number of rounds input section
        self.rounds_number_label = QLabel("Enter number of rounds:")
        self.rounds_number_input = QLineEdit()
        self.rounds_number_input.setPlaceholderText("e.g. 100")

        # Game variant input section
        self.game_variant_label = QLabel("Choose game variant:")
        self.game_variant_input = QComboBox()
        self.game_variant_input.addItems(["Normal", "Fast", "Slow"])

        # Button to update the graph
        self.update_canvas_button = QPushButton("Update Graph")
        self.update_canvas_button.clicked.connect(self.update_canvas)
        self.update_canvas_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Add input fields and button to the form layout
        settings_layout.addRow(self.player_number_label, self.player_number_input)
        settings_layout.addRow(self.rounds_number_label, self.rounds_number_input)
        settings_layout.addRow(self.game_variant_label, self.game_variant_input)
        settings_layout.addRow(self.update_canvas_button)

        self.analysis_layout.addLayout(settings_layout)

    def update_canvas(self):
        # Clear the axes for the new plot
        self.graph_canvas.axes.cla()
        
        # Run Monte Carlo simulation and update the plot
        simulation = GameSimulation()
        rounds = int(self.rounds_number_input.text())
        players = int(self.player_number_input.text())
        game_variant = self.game_variant_input.currentText()

        players_won_chance = simulation.run_simulation(rounds, players, game_variant)
        
        round_list = list(range(rounds))
        i=1
        for player_won_chance in players_won_chance:
            
            label = f"Player {i}"
            i += 1
            self.graph_canvas.axes.plot(round_list, player_won_chance, label=label)
            self.graph_canvas.axes.legend()
         # Add a legend to show player labels

        # Redraw the canvas
        self.graph_canvas.draw()
