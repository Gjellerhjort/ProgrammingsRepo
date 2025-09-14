from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from gui.widgets import ComparisonWidget
from gui.sidebar import SidebarWidget  # We'll create this next

def launch_app(detectors, video_path):
    import sys
    app = QApplication(sys.argv)
    window = MainWindow(detectors, video_path)
    window.show()
    sys.exit(app.exec())

class MainWindow(QMainWindow):
    def __init__(self, detectors, video_path):
        super().__init__()
        self.setWindowTitle("Model Comparison")

        # Main widget with horizontal layout
        central_widget = QWidget(self)
        layout = QHBoxLayout(central_widget)

        # Sidebar
        self.sidebar = SidebarWidget(self)
        layout.addWidget(self.sidebar)

        # Comparison area
        self.comparison_widget = ComparisonWidget(self, detectors, video_path)
        layout.addWidget(self.comparison_widget, stretch=1)

        self.setCentralWidget(central_widget)

