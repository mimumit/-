from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit


class okno1(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('буквы')
        self.label2 = QLabel('буквыбуквы')
        self.btn = QPushButton('кнопка')
        self.resize(700,500)
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.label1)
        self.v1.addWidget(self.label2)
        self.v1.addWidget(self.btn)
        self.setLayout(self.v1)
        self.show()
        self.btn.clicked.connect(self.next)

    def next(self):
        self.hide()
        self.window = okno2()


app = QApplication([])

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
        self.pole1 = QLineEdit()
        self.pole2 = QLineEdit()
        self.pole3 = QLineEdit()
        self.pole4 = QLineEdit()
        self.pole5 = QLineEdit()
        self.resize(700,500)
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.label1)
        self.v1.addWidget(self.pole1)
        self.v1.addWidget(self.label2)
        self.v1.addWidget(self.pole2)
        self.v1.addWidget(self.label3)
        self.v1.addWidget(self.but1)
        self.v1.addWidget(self.pole3)
        self.v1.addWidget(self.label4)
        self.v1.addWidget(self.but2)
        self.v1.addWidget(self.label5)
        self.v1.addWidget(self.but3)
        self.v1.addWidget(self.pole4)
        self.v1.addWidget(self.pole5)
        self.v1.addWidget(self.but4)
        
        self.setLayout(self.v1)
        self.show()
        self.but4.clicked.connect(self.next)

    def next(self):
        self.hide()
        self.window = okno3()
        

window2 = okno2()
window2.show()
#app.exec_()


class okno3(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel('резы')
        self.label2 = QLabel('буквы')
        self.resize(700,500)
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.label1)
        self.v1.addWidget(self.label2)
        self.setLayout(self.v1)
        self.show()

window3 = okno3()
window2.show()
app.exec_()