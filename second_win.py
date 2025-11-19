from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *

class TextWin(QWidget):
   def __init__(self):
       ''' en donde se realizan las preguntas  '''
       super().__init__() 
       self.set_appear()
       self.initUI()
       self.connects() 
       self.show() 


