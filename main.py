from PyQt5.QtWidgets import QApplication,QMessageBox
from time import sleep
from random import choice, shuffle
app=QApplication([])

from window import*
from menu import*
main_win.show()
pravilno=0
popitki=0
radio_list=[rad_btn1,rad_btn2,rad_btn3,rad_btn4]
def change_ramka():
    global pravilno, popitki
    if ans_btn.text()=="Answer":
        Ramka.hide()
        check_result()
        Ramka2.show()
        ans_btn.setText("Next question")
     
    elif ans_btn.text()=="Next question" and len(list_questions)>0:
        Ramka2.hide()
        Ramka.show()
        ans_btn.setText("Answer")
        svaz.setExclusive(False)
        rad_btn1.setChecked(False)
        rad_btn2.setChecked(False)
        rad_btn3.setChecked(False)
        rad_btn4.setChecked(False)
        svaz.setExclusive(True)
        menu_window_hide()
    else:
        win_message=QMessageBox()
        win_message.setText("Правильних віпдовідей:"+ str(pravilno)+ "\n Всього відповідей:"+ str(popitki))
        win_message.show()
        win_message.exec_()
def menu_window_show():
    menu_win.show()
    main_win.hide()
def menu_window_hide():
    menu_win.hide()
    shuffle(radio_list)
    random_q=choice(list_questions)
    words.setText(random_q.question)    
    radio_list[0].setText(random_q.t_answer)
    radio_list[1].setText(random_q.f_answer1)
    radio_list[2].setText(random_q.f_answer2)
    radio_list[3].setText(random_q.f_answer3)
    list_questions.remove(random_q)
    main_win.show()

def clears():
    vvod_true.clear()
    vvod_quest.clear()
    vvod_false1.clear()
    vvod_false2.clear()
    vvod_false3.clear()
def rest():
    main_win.hide()
    menu_win.hide()
    sleep(box_time.value()*60)
    main_win.show()

list_questions=[]
def new_question_function():
    new_question=Question(vvod_quest.text(),vvod_true.text(),vvod_false1.text(),vvod_false2.text(),vvod_false3.text())
    list_questions.append(new_question)
def check_result():
    global popitki, pravilno
    correct=radio_list[0].isChecked()
    if correct:
        lab_right_wrong.setText("Вірно")
        lab_right1.setText(radio_list[0].text())
        popitki+=1
        pravilno+=1
    else:
        lab_right_wrong.setText("НеВірно")
        lab_right1.setText(radio_list[0].text())
        popitki+=1

btn_plus.clicked.connect(new_question_function)
rest_btn.clicked.connect(rest)
ans_btn.clicked.connect(change_ramka)

menu_btn.clicked.connect(menu_window_show)
return_btn.clicked.connect(menu_window_hide)
btn_clear.clicked.connect(clears)

app.exec_()