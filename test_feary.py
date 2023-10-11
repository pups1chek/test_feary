from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget ,QButtonGroup, QHBoxLayout, QVBoxLayout , QGroupBox,QRadioButton,QPushButton, QLabel
from random import shuffle , randint


class Question():
    def __init__ (self,question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question()
q2 = Question()
question_list.append(q1)
question_list.append(q2)

app = QApplication([])


button = QPushButton('ОТВЕТИК >:)))')
label = QLabel('ТИ НЕФОРЬ? >:))')

box = QGroupBox("Варианты ответов")
a_button = QRadioButton()
a1_button = QRadioButton()
a2_button = QRadioButton()
a3_button = QRadioButton()

RadioGroup = QButtonGroup()
RadioGroup.addButton(a_button)
RadioGroup.addButton(a1_button)
RadioGroup.addButton(a2_button)
RadioGroup.addButton(a3_button)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout2.addWidget(a_button)
layout2.addWidget(a1_button)
layout3.addWidget(a2_button)
layout3.addWidget(a3_button)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
box.setLayout(layout1)


ans_box = QGroupBox('Результат')
label_a = QLabel()
label_c = QLabel()

layout_res = QVBoxLayout()
layout_res.addWidget(label_a, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(label_c, alignment = Qt.AlignCenter, stretch = 2)
ans_box.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(label, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(box)
layout_line2.addWidget(ans_box)
ans_box.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch = 2)
layout_line3.addStretch(1)

layout_card  = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    box.hide()
    ans_box.show()
    button.setText('Следующий вопрос')

def show_question():
    box.show()
    ans_box.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    a_button.setChecked(False)
    a1_button.setChecked(False)
    a2_button.setChecked(False)
    a3_button.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [a_button ,a1_button ,a2_button, a3_button]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.wrong1)
    answers[1].setText(q.wrong2)
    answers[2].setText(q.wrong3)
    answers[3].setText(q.wrong4)
    label.setText(q.question)
    label_c.setText(q.right_answer)
    show_question()
    
def show_correct(res):
    label_a.setText(res)
    show_result()
    

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        a_score += 1
    if answers[1].isChecked():
        show_correct('Правильно!')
        b_score += 1
    if answers[2].isChecked():
        show_correct('Правильно!')
        c_score += 1
    if answers[3].isChecked():
        show_correct('Правильно!')
        d_score += 1

def result():
    if a_score > b_score and a_score > c_score and a_score > d_score: 
        label.setText('блум')
        window1.show()
    if b_score > a_score and b_score > c_score and b_score > d_score: 
        label.setText('текна')
        window1.show()
    if c_score > b_score and c_score > a_score and c_score > d_score: 
        label.setText('муза')
        window1.show()
    if d_score > b_score and d_score > c_score and d_score > a_score: 
        label.setText('флора')
        window1.show()        
    if a_score = b_score : 
        label.setText('стелла')
        window1.show()
    if b_score = c_score:
        label.setText('лейла')
        window1.show()





def next_question():
    window.total += 1
    print(f'Статистика\n Всего вопросов: {window.total} \n Правильных ответов:{window.score}')
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window1 = QWidget()

window.setLayout(layout_card)
window.setWindowTitle('Тест на фею')

window1.setLayout(layout_card)
window1.setWindowTitle('Результат теста')

button.clicked.connect(click_OK)

window.score = 0
window.total = 0 

next_question()
window.resize(400,300)
window.show()

app.exec()
