from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget ,QButtonGroup, QHBoxLayout, QVBoxLayout , QGroupBox,QRadioButton,QPushButton, QLabel
from random import shuffle , randint

class Question():
    def __init__ (self,question, ans1, ans2, ans3, ans4):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4

question_list = []
q1 = Question("какой у тебя любимый цвет ", 
            "красный,синий,оранжевый ",
            "зеленый,фиолетовый,голубой",
            "черный, розовый,пурпурный",
            "бирюзовый,золотой,охра")

q2 = Question(" какой у тебя знак зодиака ",
            "овен, стрелец, лев,"
            ,"близнецы, весы, водолей"
            ,"рак,рыбы,скорпион"
            ,"телец, дева,козерог")

q3 = Question("какую музыку ты предпочитаешь",
            "металл",
            "классическая",
            "джаз",
            "панк-рок")

q4 = Question("на какое бы вы занятие пошли в алфеи",
            "метаморфосимбиоз",
            "зельеварение",
            "природная магия",
            "магическая гимнастика")

q5 = Question("как у тебя в учебе",
            "троишница",
            "отличница",
            "хорошистка",
            "не люблю учиться")

q6 = Question("выбери волчью цитату",
            "Лучше иметь друга, чем друг друга",
            "Не важно кто, важно кто",
            "Работа не wolk, работа work",
            "Если волк молчит, лучше его не перебивать")

q7 = Question("Какое Ваше любимое время года?",
            "Зима",
            "Весна",
            "Лето",
            "Осень")

q8 = Question("Выберите время суток",
            "Раннее утро",
            "Позднее утро",
            "День",
            "Поздний вечер")  

q9 = Question(" что для вас важнее?",
            "Любовь",
            "Семья",
            "Дружба",
            "Деньги")

q10 = Question("выберите цветочек",
                "Ирис",
                "Ромашка",
                "Роза",
                "Подсолнух")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)


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
#    ans_box.show()
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

#счетчики
a_score = 0
b_score = 0
c_score = 0
d_score = 0


def ask(q: Question):
    answers[0].setText(q.ans1)
    answers[1].setText(q.ans2)
    answers[2].setText(q.ans3)
    answers[3].setText(q.ans4)
    label.setText(q.question)
#    label_c.setText(q.right_answer) 
    show_question()
    
"""def show_correct(res):
    label_a.setText(res)
    show_result()"""
    

def check_answer():
    if answers[0].isChecked():
        global a_score
        a_score += 1
        show_result()
    if answers[1].isChecked():
        global b_score
        b_score += 1
        show_result()
    if answers[2].isChecked():
        global c_score
        c_score += 1
        show_result()
    if answers[3].isChecked():
        global d_score
        d_score += 1
        show_result()

def result():
    if a_score > b_score and a_score > c_score and a_score > d_score: 
        label.setText('блум /n  смелые и решительные, быстро примете верное решение в опасной ситуации. часто берёте лидерство на себя. не верите в себя, но ваши друзья постоянно доказывают вам обратнoe.')
        
    if b_score > a_score and b_score > c_score and b_score > d_score: 
        label.setText('текна /n вы тот человек, которыйшутит с лицом без эмоций.терпеливы, но всегда поставите на место, если это нужно. вы невероятно умны, скорее всего математик. ')
        
    if c_score > b_score and c_score > a_score and c_score > d_score: 
        label.setText('муза  /n я хочу вас обнять ((( . очень ранимы и импульсивны, вам трудно понимать шутки ваших друзей. немного капризны. в любом случае, вы солнышки')
    if d_score > b_score and d_score > c_score and d_score > a_score: 
        label.setText('флора /n как бы то не звучало, вы сразу любители природы. любите маленькие подарочки. храните фотографию любимых под чехлом')        
   



counter_q = 0

def next_question():
    global counter_q
    if counter_q <= 9:
        q = question_list[counter_q]
        counter_q += 1
        ask(q)
    else
        result()


def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Тест на фею')
button.clicked.connect(click_OK)
window.score = 0


next_question()
window.resize(400,300)
window.show()

app.exec()
