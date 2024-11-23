from PyQt5.QtGui import QColor, QIcon, QPalette
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QListWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt 
import sys
import close
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do")
        self.layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.listwidget = QListWidget()
        self.layout.addWidget(self.listwidget)
        delete = QPushButton("Incomplete")
        delete.clicked.connect(self.delete_clicked)
        hlayout.addWidget(delete)
        complete = QPushButton("Completed")
        hlayout.addWidget(complete)
        complete.clicked.connect(self.complete_clicked)
        self.layout.addLayout(hlayout)
        self.lineedit = QLineEdit()
        self.layout.addWidget(self.lineedit)
        self.lineedit.textEdited.connect(self.textedited)
        todobutton = QPushButton("Add Todo")
        todobutton.clicked.connect(self.todobutton_clicked)
        self.layout.addWidget(todobutton)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(Qt.gray))
        self.setPalette(palette)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    def textedited(self, text):
        self.text = text
    def todobutton_clicked(self):
        try:
            self.listwidget.addItem(self.text)
            self.lineedit.setText("")
        except: 
            pass
    def delete_clicked(self):
        try:
            item = self.listwidget.currentItem()
            item.setIcon(QIcon(":/icons/close.png"))
        except:
            pass

    def complete_clicked(self):
        try:
            item = self.listwidget.currentItem()
            item.setIcon(QIcon(":/icons/check.png"))
        except:
            pass
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec_()