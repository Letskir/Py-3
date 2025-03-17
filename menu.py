from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton , QLabel , QVBoxLayout, QLineEdit, QHBoxLayout, QSpinBox, QRadioButton, QGroupBox,QButtonGroup

menu_win=QWidget()
menu_win.setWindowTitle('Memory Card')
menu_win.move(600,0)
menu_win.resize(600,500)
lab1=QLabel("Введіть запитання:")
lab2=QLabel("Введіть вірну відповідь:")
lab3=QLabel("Введіть першу хибну відповідь:")
lab4=QLabel("Введіть другу хибну відповідь:")
lab5=QLabel("Введіть третю хибну відповідь:")

vvod_quest=QLineEdit()
vvod_true=QLineEdit()
vvod_false1=QLineEdit()
vvod_false2=QLineEdit()
vvod_false3=QLineEdit()

btn_plus=QPushButton("Додати запитання")
btn_clear=QPushButton("Очистити")

stata=QLabel("Статистика")

return_btn=QPushButton("Назад")


V_line_dop1=QVBoxLayout()
V_line_dop2=QVBoxLayout()
V_line_dop3=QVBoxLayout()
H_line1=QHBoxLayout()
H_line2=QHBoxLayout()
V_line=QVBoxLayout()

V_line_dop1.addWidget(lab1)
V_line_dop1.addWidget(lab2)
V_line_dop1.addWidget(lab3)
V_line_dop1.addWidget(lab4)
V_line_dop1.addWidget(lab5)

V_line_dop2.addWidget(vvod_quest)
V_line_dop2.addWidget(vvod_true)
V_line_dop2.addWidget(vvod_false1)
V_line_dop2.addWidget(vvod_false2)
V_line_dop2.addWidget(vvod_false3)

V_line_dop3.addWidget(stata)
V_line_dop3.addWidget(return_btn)

H_line1.addLayout(V_line_dop1)
H_line1.addLayout(V_line_dop2)

H_line2.addWidget(btn_plus)
H_line2.addWidget(btn_clear)

V_line.addLayout(H_line1)
V_line.addLayout(H_line2)
V_line.addLayout(V_line_dop3)


menu_win.setLayout(V_line)
