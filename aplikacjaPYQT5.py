
from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout,QPushButton,QLabel
from PyQt5 import QtCore

import sys

root=QApplication(sys.argv) #stworzenie aplikacji

window=QWidget()
window.setWindowTitle("Kalkulator")    #nazwa okna
window.setGeometry(700,300,50,50) #rozmiary
window.show()#pokazanie okna, mozliwa funkcja ukrycia aplikacji
window.setMaximumHeight(600)
window.setMinimumHeight(600)
window.setMaximumWidth(600)
window.setMinimumWidth(600)
window.setStyleSheet("background-color: white;")

uklad=QGridLayout()#ustawianie layout

window.liczba=QLabel()
window.liczba.readonly=False
window.liczba.setToolTip("Tutaj bedzie twoje dzialanie")
window.liczba.setStyleSheet("border: 1px solid black;border-radius:4;background-color: white ;font-size:18px;")
window.liczba.setMaximumWidth(300)

window.wynik=QLabel()
window.wynik.readonly=True
window.wynik.setToolTip("Tutaj bedzie twoj wynik")
window.wynik.setStyleSheet("border: 1px solid black;border-radius:4;background-color: white;font-size:18px;")
window.wynik.setMaximumWidth(300)

liczba_1=QPushButton("1",window)
liczba_2=QPushButton("2",window)
liczba_3=QPushButton("3",window)
dodawanie=QPushButton("+",window)
liczba_1.setMinimumHeight(120)
liczba_2.setMinimumHeight(120)
liczba_3.setMinimumHeight(120)
dodawanie.setMinimumHeight(120)

liczba_4=QPushButton("4",window)
liczba_5=QPushButton("5",window)
liczba_6=QPushButton("6",window)
odejmowanie=QPushButton("-",window)
liczba_4.setMinimumHeight(120)
liczba_5.setMinimumHeight(120)
liczba_6.setMinimumHeight(120)
odejmowanie.setMinimumHeight(120)

liczba_7=QPushButton("7",window)
liczba_8=QPushButton("8",window)
liczba_9=QPushButton("9",window)
wynik=QPushButton("=",window)
liczba_7.setMinimumHeight(120)
liczba_8.setMinimumHeight(120)
liczba_9.setMinimumHeight(120)
wynik.setMinimumHeight(120)

czyszczenie=QPushButton("Czysc",window)
dzielenie=QPushButton("/",window)
mnozenie=QPushButton("*",window)
wyjdz=QPushButton("Exit",window)
czyszczenie.setMinimumHeight(120)
dzielenie.setMinimumHeight(120)
mnozenie.setMinimumHeight(120)
wyjdz.setMinimumHeight(120)

cos="QPushButton""{""color : black;border:1px solid black;border-radius:6;font-size:20px;""}""QPushButton::pressed""{""background-color : #BDBDBD;""}"
liczba_1.setStyleSheet(cos)
liczba_2.setStyleSheet(cos)
liczba_3.setStyleSheet(cos)
liczba_4.setStyleSheet(cos)
liczba_5.setStyleSheet(cos)
liczba_6.setStyleSheet(cos)
liczba_7.setStyleSheet(cos)
liczba_8.setStyleSheet(cos)
liczba_9.setStyleSheet(cos)
odejmowanie.setStyleSheet(cos)
wynik.setStyleSheet(cos)
dodawanie.setStyleSheet(cos)
czyszczenie.setStyleSheet(cos)
dzielenie.setStyleSheet(cos)
mnozenie.setStyleSheet(cos)
wyjdz.setStyleSheet(cos)

tekst=QLabel("Dzialanie ",window)
tekst_2=QLabel("Wynik ",window)
tekst.setStyleSheet("font:bold;font-size:15px;")
tekst_2.setStyleSheet("font:bold;font-size:15px;")

tekst.setAlignment(QtCore.Qt.AlignCenter)
tekst_2.setAlignment(QtCore.Qt.AlignCenter)

uklad.addWidget(tekst,0,1,1,2)
uklad.addWidget(tekst_2,0,3,1,2)

uklad.addWidget(window.liczba,1,1,1,2)      #pierwszy wiersz
uklad.addWidget(window.wynik,1,3,1,2)

uklad.addWidget(liczba_1,2,1)               #drugi wiersz
uklad.addWidget(liczba_2,2,2)
uklad.addWidget(liczba_3,2,3)
uklad.addWidget(dodawanie,2,4)

uklad.addWidget(liczba_4,3,1)               #trzeci wiersz
uklad.addWidget(liczba_5,3,2)
uklad.addWidget(liczba_6,3,3)
uklad.addWidget(odejmowanie,3,4)

uklad.addWidget(liczba_7,4,1)
uklad.addWidget(liczba_8,4,2)
uklad.addWidget(liczba_9,4,3)
uklad.addWidget(wynik,4,4)

uklad.addWidget(wyjdz,5,4)
uklad.addWidget(czyszczenie,5,3)
uklad.addWidget(mnozenie,5,2)
uklad.addWidget(dzielenie,5,1)

def func(x):
    previous=window.liczba.text()
    
    window.liczba.setText(str(previous)+str(x))

def func_2():
    try:
        cos=(window.liczba.text())
        cos=cos.replace(":","/")
        wynik=eval(cos)
        window.wynik.setText(str(wynik))
    except SyntaxError:
        window.wynik.setText("Syntax Error")

def czysc():
    window.wynik.setText("")
    window.liczba.setText("")

def exit():
    root.destroyed()

liczba_1.clicked.connect(partial(func,1))
liczba_2.clicked.connect(partial(func,2))
liczba_3.clicked.connect(partial(func,3))
liczba_4.clicked.connect(partial(func,4))
liczba_5.clicked.connect(partial(func,5))
liczba_6.clicked.connect(partial(func,6))
liczba_7.clicked.connect(partial(func,7))
liczba_8.clicked.connect(partial(func,8))
liczba_9.clicked.connect(partial(func,9))
dodawanie.clicked.connect(partial(func,"+"))
odejmowanie.clicked.connect(partial(func,"-"))
wynik.clicked.connect(partial(func_2))
czyszczenie.clicked.connect(partial(czysc))
wyjdz.clicked.connect(partial(exit))
mnozenie.clicked.connect(partial(func,"*"))
dzielenie.clicked.connect(partial(func,":"))

for x in range(0,5):
    uklad.setRowMinimumHeight(x,20)
for x in range(1,5):
    uklad.setColumnMinimumWidth(x,150)

window.setLayout(uklad)

root.exec()