from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class SidebarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Sidebar"))
        # Add any buttons or info you want in the sidebar
        self.info_label = QLabel("Frame info here")
        layout.addWidget(self.info_label)
        self.button1 = QPushButton("Action 1")
        layout.addWidget(self.button1)
        self.button2 = QPushButton("Action 2")
        layout.addWidget(self.button2)
        layout.addStretch()
