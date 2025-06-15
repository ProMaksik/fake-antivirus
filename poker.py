from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel)
from PyQt5.QtGui import QPixmap
from pathlib import Path
from random import randint

app = QApplication([])

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Покер")
        self.setFixedSize(1000, 500)
        self.counter = 0
        self.cards = []
        self.copyofcards = []
        self.load_card_images()
        self.tasovka()

        self.players = {'you': [],
                        'bot1':[],
                        'bot2':[],
                        'bot3':[]}
        self.add_card()

        self.bot1bet = 0
        self.bot2bet = 0
        self.bot3bet = 0
        self.bank = 0
        self.yourbet = 0

        self.blankcard = QPixmap('images/back.jfif')
        self.blankcard = self.blankcard.scaled(100, 400, Qt.KeepAspectRatio)
        self.your_card1 = QLabel()
        self.your_card2 = QLabel()
        self.bot1_card1 = QLabel()
        self.bot1_card1.setPixmap(self.blankcard)
        self.bot1_card2 = QLabel()
        self.bot1_card2.setPixmap(self.blankcard)
        self.bot2_card1 = QLabel()
        self.bot2_card1.setPixmap(self.blankcard)
        self.bot2_card2 = QLabel()
        self.bot2_card2.setPixmap(self.blankcard)
        self.bot3_card1 = QLabel()
        self.bot3_card1.setPixmap(self.blankcard)
        self.bot3_card2 = QLabel()
        self.bot3_card2.setPixmap(self.blankcard)

        self.bot1lbl = QLabel("Бот 1")
        self.bot2lbl = QLabel("Бот 2")
        self.bot3lbl = QLabel("Бот 3")
        self.bot1money = QLabel("Баланс: 10000")
        self.bot2money = QLabel("Баланс: 10000")
        self.bot3money = QLabel("Баланс: 10000")
        self.bot1bet = QLabel("Ставка: 0")
        self.bot2bet = QLabel("Ставка: 0")
        self.bot3bet = QLabel("Ставка: 0")

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()

        self.v = QVBoxLayout()
        self.vname1 = QVBoxLayout()
        self.vname2 = QVBoxLayout()
        self.vname3 = QVBoxLayout()

        self.vname1.addWidget(self.bot1lbl, alignment=Qt.AlignTop)
        self.vname1.addWidget(self.bot1money, alignment=Qt.AlignTop)
        self.vname1.addWidget(self.bot1bet, alignment=Qt.AlignTop)
        self.vname2.addWidget(self.bot2lbl, alignment=Qt.AlignTop)
        self.vname2.addWidget(self.bot2money, alignment=Qt.AlignTop)
        self.vname2.addWidget(self.bot2bet, alignment=Qt.AlignTop)
        self.vname3.addWidget(self.bot3lbl, alignment=Qt.AlignTop)
        self.vname3.addWidget(self.bot3money, alignment=Qt.AlignTop)
        self.vname3.addWidget(self.bot3bet, alignment=Qt.AlignTop)

        self.h1.addWidget(self.bot1_card1, alignment=Qt.AlignLeft)
        self.h1.addLayout(self.vname1)
        self.h1.addWidget(self.bot1_card2, alignment=Qt.AlignLeft)
        self.h1.addStretch(1)
        self.h1.addWidget(self.bot2_card1, alignment=Qt.AlignCenter)
        self.h1.addLayout(self.vname2)
        self.h1.addWidget(self.bot2_card2, alignment=Qt.AlignCenter)
        self.h1.addStretch(1)
        self.h1.addWidget(self.bot3_card1, alignment=Qt.AlignRight)
        self.h1.addLayout(self.vname3)
        self.h1.addWidget(self.bot3_card2, alignment=Qt.AlignRight)

        self.cardlbl = QLabel('это колода с картами лол')
        self.cardslbl = QLabel()
        self.cardslbl.setPixmap(QPixmap('images/back.jfif'))
        self.card1lbl = QLabel()
        self.card2lbl = QLabel()
        self.card3lbl = QLabel()
        self.card4lbl = QLabel()
        self.card5lbl = QLabel()
        self.banklbl = QLabel("Банк: 0")

        self.h2.addWidget(self.cardlbl)
        self.h2.addWidget(self.cardslbl)
        self.h2.addWidget(self.card1lbl)
        self.h2.addWidget(self.card2lbl)
        self.h2.addWidget(self.card3lbl)
        self.h2.addWidget(self.card4lbl)
        self.h2.addWidget(self.card5lbl)
        self.h2.addWidget(self.banklbl)

        self.your_card_showed1 = self.players['you'][0]['pixmap'].scaled(100, 400, Qt.KeepAspectRatio)
        self.your_card_showed2 = self.players['you'][1]['pixmap'].scaled(100, 400, Qt.KeepAspectRatio)

        self.your_card1.setPixmap(self.your_card_showed1)
        self.your_card2.setPixmap(self.your_card_showed2)
        self.pasbtn = QPushButton("Пасс")
        self.callbtn = QPushButton("Вызов")
        self.raisebtn = QPushButton("Возвысить")
        self.allinbtn = QPushButton("Алл ин")

        self.choosev1 = QVBoxLayout()
        self.choosev2 = QVBoxLayout()

        self.choosev1.addWidget(self.pasbtn)
        self.choosev1.addWidget(self.callbtn)
        self.choosev2.addWidget(self.raisebtn)
        self.choosev2.addWidget(self.allinbtn)

        self.h3.addWidget(self.your_card1)
        self.h3.addWidget(self.your_card2)

        self.h3.addLayout(self.choosev1)
        self.h3.addLayout(self.choosev2)

        self.v.addLayout(self.h1)
        self.v.addLayout(self.h2)
        self.v.addLayout(self.h3)
        self.setLayout(self.v)
        self.show()

    
    def load_card_images(self):
        card_folder = Path("images")
        if self.counter == 0:
            for image_file in card_folder.glob("*.png"):
                if image_file.name != "back.png":  # Пропускаем рубашку
                    # Из имени файла вида "ace_of_spades.png" извлекаем масть и достоинство
                    rank, suit = image_file.stem.split("_of_")
                    
                    self.cards.append({
                        'suit': suit,
                        'rank': rank,
                        'image_path': str(image_file),
                        'pixmap': QPixmap(str(image_file))
                    })
            self.counter = 1
        

    def tasovka(self):
        for i in range(52):
            i = randint(0, len(self.cards) - 1)
            self.copyofcards.append(self.cards[i])
            self.cards.pop(i)
        for a in self.copyofcards:
            #print(a['suit'] + ' : ' + a['rank'])
            pass
    def add_card(self):
        for pl in self.players:
            your_random_card = randint(0, len(self.copyofcards)- 1)
            self.players[pl].append(self.copyofcards[your_random_card])
        for pl in self.players:
            your_random_card = randint(0, len(self.copyofcards)- 1)
            self.players[pl].append(self.copyofcards[your_random_card])
        print(self.players['you'])



        
main = Main()
app.exec_()