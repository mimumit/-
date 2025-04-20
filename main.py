from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

app = QApplication([])

class okno1(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('буквы')
        self.label2 = QLabel('буквыбуквы')
        self.btn = QPushButton('кнопка')
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.label1)
        self.v1.addWidget(self.label2)
        self.v1.addWidget(self.btn)
        self.setLayout(self.v1)


window = okno1()
window.show()
#app.exec_()


class okno2(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('буквы')
        self.label2 = QLabel('буквыбуквы')
        self.label3 = QLabel('буквы3')
        self.label4 = QLabel('буквы4')
        self.label5 = QLabel('буквы5')
        self.but1 = QPushButton('кнопка1')
        self.but2 = QPushButton('кнопка2')
        self.but3 = QPushButton('кнопка3')
        self.but4 = QPushButton('кнопка4')
        

window2 = okno2()
window2.show()
app.exec_()
