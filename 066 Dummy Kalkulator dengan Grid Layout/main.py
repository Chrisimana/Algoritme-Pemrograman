from PyQt5.QtWidgets import *

app = QApplication([]

window = QMainWindow()

window.setGeometry(300,300, 500, 300)
window.setWindowTitle("Grid Layout")

grid = QGridLayout()

#Text
ledit_num = QLineEdit(window)
ledit_num.setFixedHeight(50)
ledit_num.setEnabled(False)

def buat_tombol(label):
    qbtn = QPushButton(label, window)
    qbtn.setFixedHeight(100)
    return qbtn

def set0():
    ledit_num.setText(f"{ledit_num.text()}0")
def set1():
    ledit_num.setText(f"{ledit_num.text()}1")
def set2():
    ledit_num.setText(f"{ledit_num.text()}2")
def set3():
    ledit_num.setText(f"{ledit_num.text()}3")
def set4():
    ledit_num.setText(f"{ledit_num.text()}4")
def set5():
    ledit_num.setText(f"{ledit_num.text()}5")
def set6():
    ledit_num.setText(f"{ledit_num.text()}6")
def set7():
    ledit_num.setText(f"{ledit_num.text()}7")
def set8():
    ledit_num.setText(f"{ledit_num.text()}8")
def set9():
    ledit_num.setText(f"{ledit_num.text()}9")
def clear():
    ledit_num.setText("")

deflist = [set0, set1, set2, set3, set4,set5, set6, set7, set8, set9]

#init Button
btn: QPushButton = []
for i in range(10):
    qbtn = buat_tombol(str(i))
    qbtn.clicked.connect(deflist[i])
    btn.append(qbtn

btn_clear = buat_tombol("C")
btn_clear.clicked.connect(clear)
btn_kurang = buat_tombol("-")
btn_tambah = buat_tombol("+")
btn_tambah.setFixedHeight(200)

grid.addWidget(ledit_num, 0,0,1,4)
grid.addWidget(btn_clear, 1, 3)
grid.addWidget(btn_kurang, 2, 3)
grid.addWidget(btn_tambah, 3, 3, 2, 1)

grid.addWidget(btn[7], 1, 0)
grid.addWidget(btn[8], 1, 1)
grid.addWidget(btn[9], 1, 2)

grid.addWidget(btn[4], 2, 0)
grid.addWidget(btn[5], 2, 1)
grid.addWidget(btn[6], 2, 2)

grid.addWidget(btn[1], 3, 0)
grid.addWidget(btn[2], 3, 1)
grid.addWidget(btn[3], 3, 2)

grid.addWidget(btn[0], 4, 1)

widget = QWidget()
widget.setLayout(grid)
window.setCentralWidget(widget)

window.show()
app.exec_()
