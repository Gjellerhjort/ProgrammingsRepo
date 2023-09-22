# ui_main.py
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("HuntersApp")
        MainWindow.setWindowIcon(QtGui.QIcon('resources\img\dog.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.NavigationUI(self)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def  NavigationUI(self, MainWindow):
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setGeometry(QtCore.QRect(0, 0, 800, 600))

        # Create the first grid layout for the top half
        top_grid_layout = QtWidgets.QGridLayout()
        
        layout.setSpacing(10)  # Add spacing between buttons
        
        label = QtWidgets.QLabel(self.centralwidget)
        label.setText("Name:")
        label.setObjectName("label")
        
        label2 = QtWidgets.QLabel(self.centralwidget)
        label2.setText("Level: 192")
        label2.setObjectName("label_2")
        
        top_grid_layout.addWidget(label, 0, 0)  # Span the label across two columns
        top_grid_layout.addWidget(label2, 1, 0)  # Span the second label across two columns
        


        # Create the second grid layout for the bottom half
        bottom_grid_layout = QtWidgets.QGridLayout()
        
        progressBar = QtWidgets.QProgressBar(self.centralwidget)
        progressBar.setGeometry(QtCore.QRect(50, 200, 681, 23))
        progressBar.setProperty("value", 24)
        progressBar.setObjectName("progressBar")
        
        top_grid_layout.addWidget(label2, 3, 0)  # Span the second label across two columns
        

        layout.addLayout(top_grid_layout)

        # creates buttons
        button2 = QtWidgets.QPushButton("Page 2", self.centralwidget)
        button3 = QtWidgets.QPushButton("Page 3", self.centralwidget)
        button4 = QtWidgets.QPushButton("Page 4", self.centralwidget)
        button1 = QtWidgets.QPushButton("Page 1", self.centralwidget)

        #button1.clicked.connect(self.show_page1)
        #button2.clicked.connect(self.show_page2)
        #button3.clicked.connect(self.show_page3)
        #button4.clicked.connect(self.show_page4)
        
        # Set size policy to make buttons fill the cells
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        button1.setSizePolicy(size_policy)
        button2.setSizePolicy(size_policy)
        button3.setSizePolicy(size_policy)
        button4.setSizePolicy(size_policy)

        # Adds buttons to the layout widget
        bottom_grid_layout.addWidget(button1, 0, 0, 1, 1)  # Button 1 takes the top-left quarter
        bottom_grid_layout.addWidget(button2, 0, 1, 1, 1)  # Button 2 takes the top-right quarter
        bottom_grid_layout.addWidget(button4, 1, 0, 1, 1)  # Button 4 takes the bottom-left quarter
        bottom_grid_layout.addWidget(button3, 1, 1, 1, 1)  # Button 3 takes the bottom-right quarter

        layout.addLayout(bottom_grid_layout)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HuntersApp"))

