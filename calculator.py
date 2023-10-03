
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    zmienna = '1'

    def __init__(self):
        super().__init__()
        self.title = 'Kalkulator'
        self.left = 800
        self.top = 400
        self.width = 300
        self.height = 350
        self.initUI()

    def initUI(self):
        self.textbox1 = QLabel("Pierwsza liczba: ", self)
        self.textbox1.move(3,25)

        self.textbox2 = QLabel('Druga liczba: ',self)
        self.textbox2.move(20, 60)

        self.textbox = QLineEdit(self)
        self.textbox.move(100,20)
        self.textbox.resize(200, 30)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(100, 60)
        self.textbox3.resize(200, 30)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(100, 100)
        self.textbox4.resize(200, 30)
        self.textbox4.setText('')

        self.textbox5 = QLabel(self)
        self.textbox5.move(58, 100)
        self.textbox5.resize(80, 30)
        self.textbox5.setText('Wynik: ')

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonm = QPushButton('*', self)
        buttonm.setToolTip('Mnozenie')
        buttonm.move(240, 297)
        buttonm.resize(42,42)
        buttonm.clicked.connect(self.on_click12)

        buttond = QPushButton(' / ', self)
        buttond.setToolTip('dzielenie')
        buttond.move(240, 257)
        buttond.resize(42, 42)
        buttond.clicked.connect(self.on_click13)

        buttono = QPushButton('-', self)
        buttono.setToolTip('Odejmowanie')
        buttono.move(240, 217)
        buttono.resize(42, 42)
        buttono.clicked.connect(self.on_click11)

        buttondo = QPushButton(' + ', self)
        buttondo.setToolTip('Dodawianie')
        buttondo.move(240, 177)
        buttondo.resize(42, 42)
        buttondo.clicked.connect(self.on_click10)



        buttonr = QPushButton('=', self)
        buttonr.setToolTip(' rowna sie')
        buttonr.move(200, 297)
        buttonr.resize(42, 42)
        buttonr.clicked.connect(self.on_click14)

        button3 = QPushButton(' 3 ', self)
        button3.setToolTip('Trzy')
        button3.move(200, 257)
        button3.resize(42, 42)
        button3.clicked.connect(self.on_click3)

        button6 = QPushButton('6', self)
        button6.setToolTip('Szesc')
        button6.move(200, 217)
        button6.resize(42, 42)
        button6.clicked.connect(self.on_click6)

        button9 = QPushButton(' 9 ', self)
        button9.setToolTip('dziewiec')
        button9.move(200, 177)
        button9.resize(42, 42)
        button9.clicked.connect(self.on_click9)



        buttonk = QPushButton('.', self)
        buttonk.setToolTip(' kropka ')
        buttonk.move(160, 297)
        buttonk.resize(42, 42)
        buttonk.clicked.connect(self.on_clickk)

        button2 = QPushButton(' 2 ', self)
        button2.setToolTip(' Dwa')
        button2.move(160, 257)
        button2.resize(42, 42)
        button2.clicked.connect(self.on_click2)

        button5 = QPushButton('5', self)
        button5.setToolTip(' piec ')
        button5.move(160, 217)
        button5.resize(42, 42)
        button5.clicked.connect(self.on_click5)

        button8 = QPushButton(' 8 ', self)
        button8.setToolTip(' Osiem ' )
        button8.move(160, 177)
        button8.resize(42, 42)
        button8.clicked.connect(self.on_click8)



        button0 = QPushButton('0', self)
        button0.setToolTip('zero')
        button0.move(120, 297)
        button0.resize(42, 42)
        button0.clicked.connect(self.on_click0)

        button1 = QPushButton(' 1 ', self)
        button1.setToolTip(' Jeden')
        button1.move(120, 257)
        button1.resize(42, 42)
        button1.clicked.connect(self.on_click1)

        button4 = QPushButton('4', self)
        button4.setToolTip(' cztery ')
        button4.move(120, 217)
        button4.resize(42, 42)
        button4.clicked.connect(self.on_click4)

        button7 = QPushButton(' 7 ', self)
        button7.setToolTip(' siedem ')
        button7.move(120, 177)
        button7.resize(42, 42)
        button7.clicked.connect(self.on_click7)

        buttondr = QPushButton('   Z E R U J ', self)
        buttondr.setToolTip('Reset')
        buttondr.move(120, 137)
        buttondr.resize(162, 42)
        buttondr.clicked.connect(self.on_clickr)
        self.show()

    @pyqtSlot()

    def on_clickr(self):
        self.textbox.setText(' ')
        self.textbox3.setText(' ')
        self.textbox4.setText(' ')

    def on_click0(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '0')
                self.a = (self.textbox.text())
            elif(self.zmienna == '0'):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '0')
                self.b = (self.textbox3.text())
    def on_click1(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '1')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '1')
                self.b = (self.textbox3.text())
    def on_click2(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '2')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '2')
                self.b = (self.textbox3.text())
    def on_click3(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '3')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '3')
                self.b = (self.textbox3.text())
    def on_click4(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '4')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '4')
                self.b = (self.textbox3.text())
    def on_click5(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '5')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '5')
                self.b = (self.textbox3.text())
    def on_click6(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '6')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '6')
                self.b = (self.textbox3.text())
    def on_click7(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '7')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '7')
                self.b = (self.textbox3.text())
    def on_click8(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '8')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '8')
                self.b = (self.textbox3.text())
    def on_click9(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '9')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '9')
                self.b = (self.textbox3.text())
    def on_clickk(self):
            if (self.zmienna =="1"):
                self.a = (self.textbox.text())
                self.textbox.setText(self.a + '.')
                self.a = (self.textbox.text())
            elif(self.zmienna =="0"):
                self.b = (self.textbox3.text())
                self.textbox3.setText(self.b + '.')
                self.b = (self.textbox3.text())
    def on_click10(self):
        self.zmienna='0'
        self.dzialanie='1'
    def on_click11(self):
        self.zmienna = "0"
        self.dzialanie='2'
    def on_click12(self):
        self.zmienna = "0"
        self.dzialanie='3'
    def on_click13(self):
        self.zmienna = "0"
        self.dzialanie='4'
    def on_click14(self):
        self.zmienna = "1"
        if(self.dzialanie=='1'):
            x = float((self.textbox.text()))
            y = float((self.textbox3.text()))
            w = x + y
            self.textbox4.setText(str(w))
        elif (self.dzialanie=='2'):
            x = float((self.textbox.text()))
            y = float((self.textbox3.text()))
            w = x - y
            self.textbox4.setText(str(w))
        elif (self.dzialanie == '3'):
            x = float((self.textbox.text()))
            y = float((self.textbox3.text()))
            w = x * y
            self.textbox4.setText(str(w))
        elif (self.dzialanie=='4'):
            x = float((self.textbox.text()))
            y = float((self.textbox3.text()))
            if y == 0:
                self.textbox4.setText("niewykonalne dzialanie")
            else:
                w = x / y
                self.textbox4.setText(str(w))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())