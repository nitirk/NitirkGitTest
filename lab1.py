import sys
from PySide.QtCore import*
from PySide.QtGui import*

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 200, 0))
        p.drawPolygon([
            QPoint( 200, 100), QPoint(100, 80),
            QPoint(20, 100), QPoint(100, 120),
        ])

        p.setPen(QColor(20, 127, 0))
        p.setBrush(QColor(20, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()


    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

