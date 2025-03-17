from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox,QWidget, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QVBoxLayout, QPushButton, QSpinBox, QLabel

# Створення вікна
main_win = QWidget()
main_win.resize(500,500)
main_win.move(500,100)
main_win.setWindowTitle("Memory Card")

# Основні лейаути вікна
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
v_main = QVBoxLayout()

# --------Перший горизонтальний лейаут -----
menu_btn = QPushButton("menu")
rest_btn = QPushButton("rest")
box_time = QSpinBox()
box_time.setValue(30)
h1.addWidget(menu_btn)
h1.addWidget(rest_btn)
h1.addWidget(box_time)
#--------------------------------------------
 
# --------Другий горизонтальний лейаут -----
words =  QLabel("?")
h2.addWidget(words, alignment=Qt.AlignCenter)

# --------Третій горизонтальний лейаут -----
### box1 ###
rad_btn1 = QRadioButton('1')
rad_btn2 = QRadioButton('2')
rad_btn3 = QRadioButton('3')
rad_btn4 = QRadioButton('4')

Ramka= QGroupBox("Варіанти відповідей")
svaz = QButtonGroup()
svaz.addButton(rad_btn1 )
svaz.addButton(rad_btn2 )
svaz.addButton(rad_btn3 )
svaz.addButton(rad_btn4 )

h_dlaySVAZ = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rad_btn1 )
layout_ans2.addWidget(rad_btn2 )

layout_ans3.addWidget(rad_btn3)
layout_ans3.addWidget(rad_btn4)

h_dlaySVAZ.addLayout(layout_ans2)
h_dlaySVAZ.addLayout(layout_ans3)

Ramka.setLayout(h_dlaySVAZ)
h3.addWidget(Ramka)

### boox2 ###
Ramka2 = QGroupBox("Результат теста:")
v_dop = QVBoxLayout()
lab_right_wrong = QLabel("правильно/неправильно")
lab_right1 = QLabel("???")
v_dop.addWidget(lab_right_wrong , alignment=(Qt.AlignLeft | Qt.AlignTop))
v_dop.addWidget(lab_right1, alignment=Qt.AlignCenter)
Ramka2.setLayout(v_dop)
Ramka2.hide()

h3.addWidget(Ramka2)
#--------------------------------------------------------


# --------Четвертий горизонтальний лейаут -----
ans_btn = QPushButton("Answer")
h4.addWidget(ans_btn)






# --- Об'єднуємо всі лейаути -----
v_main.addLayout(h1)
v_main.addLayout(h2)
v_main.addLayout(h3)
v_main.addLayout(h4)

main_win.setLayout(v_main)


#------ CLASS ---------------

class Question():
    def __init__(self, question, t_answer, f_answer1 , f_answer2, f_answer3):
        self.question = question
        self. t_answer = t_answer
        self.f_answer1 = f_answer1
        self.f_answer2 = f_answer2
        self.f_answer3 = f_answer3
        self.popitki = 0
        self.pravilno = 0

