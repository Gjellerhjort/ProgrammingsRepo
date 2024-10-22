import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()