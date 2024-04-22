import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def init(self, *args, **kwargs):
        super(MainWindow, self).init(*args, **kwargs)
        uic.loadUi("svetofor.ui", self)

        self.pushButton_2.clicked.connect(self.first)

    def first(self):
        self.tableWidget_2.setStyleSheet("""
            QTableWidget {
                background-color: red;
                border-radius: 40px;
            }
        """)
        self.tableWidget_3.setStyleSheet("""
            QTableWidget {
                background-color: yellow;
                border-radius: 40px;
            }
        """)
        self.tableWidget_4.setStyleSheet("""
            QTableWidget {
                background-color: green;
                border-radius: 40px;
            }
        """)

        self.pushButton.clicked.connect(self.v)

    def v(self):
        self.tableWidget_2.setStyleSheet("""
                QToolButton {
                    background-color: rgb(113, 113, 113);
                    border-radius: 40px;
                }
            """)
        self.tableWidget_3.setStyleSheet("""
                QToolButton {
                    background-color: rgb(113, 113, 113);
                    border-radius: 40px;
                }
            """)
        self.tableWidget_4.setStyleSheet("""
                QToolButton {
                    background-color: rgb(113, 113, 113);
                    border-radius: 40px;
                }
            """)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()