from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
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
       
    def results(self):
       if self.exp.age < 7:
           self.index = 0
           return "no hay datos para esta edad"

       self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
           
       if self.exp.age == 7 or self.exp.age == 8:
           if self.index >= 21:
               return txt_res1
           elif self.index < 21 and self.index >= 17:
               return txt_res2
           elif self.index < 17 and self.index >= 12:
               return txt_res3
           elif self.index < 12 and self.index >= 6.5:
               return txt_res4
           else:
               return txt_res5

       if self.exp.age == 9 or self.exp.age == 10:
           if self.index >= 19.5:
               return txt_res1
           elif self.index < 19 and self.index >= 15:
               return txt_res2
           elif self.index < 17 and self.index >= 12:
               return txt_res3
           elif self.index < 12 and self.index >= 6.5:
               return txt_res4
           else:
               return txt_res5






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












