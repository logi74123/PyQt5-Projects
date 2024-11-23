from PyQt5.QtGui import QColor, QFont, QKeySequence, QPainter, QPalette, QPen
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt
import sys
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.hlayout = QHBoxLayout()
        layout = QVBoxLayout()
        self.lineedit = QLineEdit()
        self.lineedit.setText("")
        layout.addWidget(self.lineedit)
        self.hlayout.addLayout(layout)
        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)
        h1layout = QHBoxLayout()
        layout.addLayout(h1layout)
        h2layout = QHBoxLayout()
        layout.addLayout(h2layout)
        basehlayout = QHBoxLayout()
        layout.addLayout(basehlayout)
        vlayout = QVBoxLayout()
        self.hlayout.addLayout(vlayout)
        num_1 = QPushButton("1")
        num_1.clicked.connect(self.num_1_clicked)
        hlayout.addWidget(num_1)
        num_2 = QPushButton("2")
        num_2.clicked.connect(self.num_2_clicked)
        hlayout.addWidget(num_2)
        num_3 = QPushButton("3")
        num_3.clicked.connect(self.num_3_clicked)
        hlayout.addWidget(num_3)
        num_4 = QPushButton("4")
        num_4.clicked.connect(self.num_4_clicked)
        h1layout.addWidget(num_4)
        num_5 = QPushButton("5")
        h1layout.addWidget(num_5)
        num_5.clicked.connect(self.num_5_clicked)
        num_6 = QPushButton("6")
        num_6.clicked.connect(self.num_6_clicked)
        h1layout.addWidget(num_6)
        num_7 = QPushButton("7")
        h2layout.addWidget(num_7)
        num_7.clicked.connect(self.num_7_clicked)
        num_8 = QPushButton("8")
        h2layout.addWidget(num_8)
        num_8.clicked.connect(self.num_8_clicked)
        num_9 = QPushButton("9")
        h2layout.addWidget(num_9)
        num_9.clicked.connect(self.num_9_clicked)
        num_0 = QPushButton("0")
        num_0.clicked.connect(self.num_0_clicked)
        num_0.setMinimumHeight(40)
        basehlayout.addWidget(num_0)
        zero_zero = QPushButton("00")
        zero_zero.clicked.connect(self.zero_zero_clicked)
        zero_zero.setStyleSheet("padding:5px;")
        basehlayout.addWidget(zero_zero)
        clear = QPushButton("c")
        vlayout.addWidget(clear)
        clear.setMinimumHeight(30)
        clear.clicked.connect(self.clear_clicked)
        plus = QPushButton("+")
        vlayout.addWidget(plus)
        plus.setMinimumHeight(30)
        plus.clicked.connect(self.plus_clicked)
        minus = QPushButton("-")
        vlayout.addWidget(minus)
        minus.setMinimumHeight(30)
        minus.clicked.connect(self.minus_clicked)
        multiply = QPushButton("*")
        multiply.setMinimumHeight(30)
        vlayout.addWidget(multiply)
        multiply.clicked.connect(self.multiply_clicked)
        divide = QPushButton("/")
        divide.clicked.connect(self.divide_clicked)
        divide.setMinimumHeight(30)
        vlayout.addWidget(divide)
        equal = QPushButton("=")
        equal.setShortcut(QKeySequence("Enter"))
        equal.setMinimumHeight(20)
        equal.clicked.connect(self.equal_clicked)
        vlayout.addWidget(equal)
        widget = QWidget()
        widget.setLayout(self.hlayout)
        self.setCentralWidget(widget)
        self.setMinimumSize(QSize(200,300))
    def num_1_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "1")
        except:
            pass 
    def num_2_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "2")
        except:
            pass 
    def num_3_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "3")
        except:
            pass
    def num_4_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "4")
        except:
            pass 
    def num_5_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "5")
        except:
            pass
    def num_6_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "6")
        except:
            pass
    def num_7_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "7")
        except:
            pass
    def num_8_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "8")
        except:
            pass
    def num_9_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "9")
        except:
            pass
    def num_0_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "0")
        except:
            pass
    def clear_clicked(self):
        self.lineedit.setText("")
    def plus_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "+")
        except:
            pass
    def minus_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "-")
        except:
            pass
    def multiply_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "*")
        except:
            pass
    def divide_clicked(self):
        try:
            text = self.lineedit.text()
            self.lineedit.setText(text + "/")
        except:
            pass
    def zero_zero_clicked(self):
        text = self.lineedit.text()
        self.lineedit.setText("00")
    def equal_clicked(self):
        try:
            text = self.lineedit.text()
            answer = eval(text)
            self.lineedit.setText(str(answer))
        except ZeroDivisionError:
            self.lineedit.setText("Can't divide by zero!")
        except:
            self.lineedit.setText("Not Valid")
app = QApplication(sys.argv)
stylesheet = """
    QLineEdit{
        font:30px;
        border: 7px solid gray;
        border-style: groove;
        color: #363636;
    }
    QWidget{
        background-color: "#726E72";
    }
    QPushButton{
        color:white;
        font:20px;
        border-radius:8px;
        border: 2px solid gray;
        border-style: groove;
    }
    QPushButton:hover{
        background-color:gray;
    } 
"""
app.setStyleSheet(stylesheet)
window = Mainwindow()
window.show()
app.exec_()