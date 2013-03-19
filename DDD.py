'''
Created on Jan 28, 2013

@author: BookMu
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Greeting_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        
        self.num = 0
        
        layout = QVBoxLayout()
        
        self.name_label = QLabel(" Identification Number : ")
        layout.addWidget(self.name_label)
        
        self.number_entry = QLineEdit()
        layout.addWidget(self.number_entry)
        
        
        
        greeting_button = QPushButton("Go!")
        layout.addWidget(greeting_button)
        
      # self.connect(greeting_button, SIGNAL("clicked()"),self.greeting)
        greeting_button.clicked.connect(self.greeting)
        
        
        self.setLayout(layout)
        
        
        
        
    def put_dash(self,num,a):
        b=""
        while num is not 0:
            b+=a[0]
            a=a[1:]
            num=num-1
            b+="-"
            return b

    def reduce_ar(self,num,a):
        return a[num:]

    def splitnum(self,a):
        a=list(str(a))
        b=""
        num1 = 1
        num2 = 2
        num3 = 2
        num4 = 5
        num5 = 2
        num6 = 1
       # b+=put_dash(num1,a)
      #  a=reduce_ar(num1,a)
      #  b+=put_dash(num2,a)
      #  a=reduce_ar(num2,a)
     #   b+=put_dash(num3,a)
      #  a=reduce_ar(num3,a)
       # b+=put_dash(num4,a)
     #   a=reduce_ar(num4,a)
      #  b+=put_dash(num5,a)
     #   a=reduce_ar(num5,a)
     #   b+=put_dash(num6,a)
     #   a=reduce_ar(num6,a)
        return b[:-1]

     #   print splitnum(1859900118546)       
        

    def greeting(self):
        dialog = QDialog(self)
        
        layout = QVBoxLayout()
        
        label = QLabel("Hi " + self.number_entry.text())
        layout.addWidget(label)
        
       #print self.number_entry[1:3]
        
        
        close_button = QPushButton("Close window")
       # self.connect(close_button, SIGNAL("clicked()"),dialog.close)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        
        dialog.show()
        
def main():
    app = QApplication(sys.argv)
    
    w = Greeting_window()
    w.show()
    
    return app.exec_()

if __name__== "__main__":
    sys.exit(main())
    
     
        