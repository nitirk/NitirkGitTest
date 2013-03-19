import sys
from PySide.QtCore import*
from PySide.QtGui import*

class Simple_drawing_window_nitirk(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.setWindowTitle("Simple Drawing")
 

        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

   
        p.end()
        
        
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window_nitirk()
    w.show()
  

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
