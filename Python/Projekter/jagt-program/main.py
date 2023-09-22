# main.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MyApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
