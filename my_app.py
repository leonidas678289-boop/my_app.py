from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

class MainWin(QWidget):
   def __init__(self):
       ''' la ventana en donde se encuentra el saludo  '''
       super().__init__() 
       self.set_appear()
       self.initUI()
       self.connects() 
       self.show() 

   def initUI(self):
       ''' crea elementos gráficos '''
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)
