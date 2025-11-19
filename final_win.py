from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *

class FinalWin(QWidget):
   def __init__(self):
       ''' ventana de las respuestas  '''
       super().__init__() 
       self.set_appear()
       self.initUI()
       self.connects() 
       self.show() 

   def initUI(self):
       ''' crea elementos gráficos '''
       self.workh_text = QLabel(txt_workheart) 
       self.workindex_text = QLabel(txt_index)
       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
       self.setLayout(self.layout) 

   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y) 










