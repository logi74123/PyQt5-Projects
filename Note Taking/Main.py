from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QAction, QComboBox, QFontComboBox, QFrame, QHBoxLayout, QLabel, QMainWindow, QApplication, QPlainTextEdit, QPushButton, QSizePolicy, QTextEdit, QVBoxLayout, QWidget
import sys 
import resource_image
import MagicOwl
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.window = QMainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.layout.addLayout(self.top_layout)
        layout_window_title = QHBoxLayout()
        layout_window_title.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.top_layout.addLayout(layout_window_title)
        layout_close = QHBoxLayout()
        layout_close.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.top_layout.addLayout(layout_close)
        self.window_title_font = QFontDatabase()
        self.window_title_font.addApplicationFont(":/resources/MagicOwl.otf")
        window_title = QLabel("nopap")
        window_title.setFont(QFont("Magic Owl", 18))
        window_title_stylesheet = """
        QLabel{
            color:#12355B;
            padding-top:2px;
            padding-right:10px;}"""
        window_title.setStyleSheet(window_title_stylesheet)
        layout_window_title.addWidget(window_title)
        minimize_button = QPushButton("🗕")
        minimize_button.clicked.connect(self.minimize_button_clicked)
        stylesheet_minimize_button = """
        QPushButton{ 
            font-color:gray;                                                                                                                                                                                                                     
            font-size:15px;
            background-color:khaki;
            border:2px solid khaki;
            padding-right:5px;}
        QPushButton::pressed{
            padding-top:2px;}"""
        minimize_button.setStyleSheet(stylesheet_minimize_button)

        close_button = QPushButton("X")
        close_button.clicked.connect(self.close_button_clicked)
        stylesheet_close_button = """
        QPushButton{
            font-color:gray;
            font-size:15px;
            background-color:khaki;
            border:2px solid khaki;}
        QPushButton::pressed{
            padding-top:2px;}"""
        close_button.setStyleSheet(stylesheet_close_button)
        layout_close.addWidget(minimize_button)
        layout_close.addWidget(close_button)
        layout_toolbar = QHBoxLayout()
        self.layout.addLayout(layout_toolbar)
        layout_toolbar.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout_toolbar.setGeometry(QRect(1,2,500,50))
        font_combobox = QFontComboBox()
        font_combobox.currentFontChanged.connect(self.font_combobox_font_changed)
        font_combobox.setFixedSize(120,25)
        font_combobox_stylesheet = """
        QFontComboBox{
            border:2px solid khaki;
            border-radius:5px;}
        QFontComboBox::drop-down{
            border-right:2px solid white;
            border-bottom:2px solid white;}
        QFontComboBox::down-arrow{
            image: url(:/icons/drop down.png);
            width:10px;}
        QFontComboBox::down-arrow::pressed{
            padding-top:5px;}"""
        font_combobox.setStyleSheet(font_combobox_stylesheet)
        layout_toolbar.addWidget(font_combobox)
        size_combobox = QComboBox()
        size_combobox.setEditable(True)
        size_combobox.addItems(["1","2","3","5","8","11","15","20","25","35","45","60","80","90"])
        size_combobox.currentTextChanged.connect(self.size_combobox_text_changed)
        size_combobox.resize(40,20)
        size_combobox_stylesheet = """
        QComboBox{
            border:1px solid khaki;
            border-radius:2px;
            width:30px;}
        QComboBox::drop-down{
            border-right:2px solid white;
            border-bottom:2px solid white;}
        QComboBox::down-arrow{
            image: url(:/icons/drop down.png);
            width:10px;}
        QComboBox::down-arrow::pressed{
            padding-top:5px;}"""
        size_combobox.setStyleSheet(size_combobox_stylesheet)
        layout_toolbar.addWidget(size_combobox)
        bold_button = QPushButton("𝗕")
        bold_button.setFixedWidth(25)
        bold_button_stylesheet = """
        QPushButton{
            font-size:18px;
            border:2px solid khaki;}
        QPushButton::pressed{
            font-size:16px;}"""
        bold_button.setStyleSheet(bold_button_stylesheet)
        layout_toolbar.addWidget(bold_button)
        italic_button = QPushButton("𝐼")
        italic_button.setFixedWidth(25)
        italic_button.clicked.connect(self.italic_button_clicked)
        italic_button_stylesheet = """
        QPushButton{
            font-size:18px;
            border: 2px solid khaki;}
        QPushButton::pressed{
            font-size:16px;}"""
        italic_button.setStyleSheet(italic_button_stylesheet)
        layout_toolbar.addWidget(italic_button)
        underline_button= QPushButton("U̲")
        underline_button.pressed.connect(self.underline_button_clicked)
        underline_button.setFixedWidth(25)
        
        underline_button_stylesheet = """
        QPushButton{
            font-size:18px;
            border: 2px solid khaki;}
        QPushButton::pressed{
            font-size:16px;}"""
        underline_button.setStyleSheet(underline_button_stylesheet)
        layout_toolbar.addWidget(underline_button)
        layout_plaintext = QVBoxLayout()
        self.layout.addLayout(layout_plaintext)
        self.textedit = QTextEdit()
        textedit_stylesheet = """
        QTextEdit{
        border:3px solid #4F7CAC;
        border-radius:5px;}"""
        self.textedit.setStyleSheet(textedit_stylesheet)
        bold_button.clicked.connect(lambda x: self.textedit.setFontWeight(QFont.Bold if x else QFont.Normal))
        bold_button.setCheckable(True)
        layout_plaintext.addWidget(self.textedit)
        w = QWidget()
        w.setLayout(self.layout)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        stylesheet_window= """
        QMainWindow{
            background-color:khaki;
            border:5px solid khaki;
            border-radius:8px;}"""
        self.window.setStyleSheet(stylesheet_window)
        self.window.setMinimumSize(350,450)
        self.setCentralWidget(self.window)
        self.window.setCentralWidget(w)
        self.show()
    def close_button_clicked(self):
        self.close()
    def minimize_button_clicked(self):
        self.showMinimized()
    def size_combobox_text_changed(self, s):
        self.size_changed = s
        self.textedit.setFontPointSize(int(s))
    def font_combobox_font_changed(self, f):
        try:
            self.textedit.setCurrentFont(f)
            self.textedit.setFontPointSize(int(self.size_changed))
        except: 
            pass
    def underline_button_clicked(self):
        text = self.textedit.fontUnderline()
        self.textedit.setFontUnderline(not text)
    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept() 
    def italic_button_clicked(self):
        text = self.textedit.fontItalic()
        self.textedit.setFontItalic(not text)
app = QApplication(sys.argv)
window = Mainwindow()
app.exec_()