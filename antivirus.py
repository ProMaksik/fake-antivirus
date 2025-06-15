from PyQt5.QtCore import (Qt, QRegularExpression)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QPixmap, QRegularExpressionValidator)
import json
from random import randint

app = QApplication([])

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фейк антивирус")
        self.setMinimumSize(400, 275)
        self.setMaximumSize(400,275)

        self.nozp = 1
        self.dlyavirusov = []
        self.counter = 0

        #логин
        self.mailedit = QLineEdit()
        validator = QRegularExpressionValidator(
        QRegularExpression("[a-zA-Z]+"))
        self.mailedit.setValidator(validator)
        self.name = self.mailedit.text()
        self.mailedit.setMinimumSize(150, 25)
        self.mailedit.setMaximumSize(150, 25)
        self.passwordedit = QLineEdit()
        self.passwordedit.setEchoMode(QLineEdit.Password)
        self.passwordedit.setMinimumSize(150, 25)
        self.passwordedit.setMaximumSize(150, 25)
        self.passwordsafety = QLineEdit()
        self.passwordsafety.setEchoMode(QLineEdit.Password)
        self.passwordsafety.setMinimumSize(150, 25)
        self.passwordsafety.setMaximumSize(150, 25)
        self.signinbtn = QPushButton("Зарегестрироваться")
        self.signinbtn.clicked.connect(self.register)
        self.signinbtn.setMinimumSize(150, 25)
        self.signinbtn.setMaximumSize(150, 25)
        self.gotologinbtn = QPushButton("Есть аккаунт?\n тыкайте сюда!")
        self.gotologinbtn.clicked.connect(self.nologin)
        self.gotologinbtn.setMaximumWidth(150)
        self.emaillbl = QLabel("Укажите свой ник (на английском):")
        self.passlbl = QLabel("Укажите пароль:")
        self.secpasslbl = QLabel("Подтвердите пароль:")
        self.message = QLabel()

        self.layoutV = QVBoxLayout()
        self.layoutLogin = QHBoxLayout()

        self.layoutV.addWidget(self.emaillbl)
        self.layoutV.addWidget(self.mailedit)
        self.layoutV.addWidget(self.passlbl)
        self.layoutV.addWidget(self.passwordedit)
        self.layoutV.addWidget(self.secpasslbl)
        self.layoutV.addWidget(self.passwordsafety)
        self.layoutV.addWidget(self.signinbtn)
        self.layoutV.addWidget(self.message)
        self.layoutV.addWidget(self.gotologinbtn)

        self.layoutLogin.addLayout(self.layoutV)

        #главная
        self.frontbtn = QPushButton("Главная")
        self.frontbtn.clicked.connect(self.main)
        self.frontbtn.setMinimumSize(150, 35)
        self.frontbtn.setMaximumSize(150, 35)
        self.securbtn = QPushButton("Безопасность")
        self.securbtn.clicked.connect(self.secure)
        self.securbtn.setMinimumSize(150, 35)
        self.securbtn.setMaximumSize(150, 35)
        self.workbtn = QPushButton("Производительность")
        self.workbtn.clicked.connect(self.productivity)
        self.workbtn.setMinimumSize(150, 35)
        self.workbtn.setMaximumSize(150, 35)
        self.privbtn = QPushButton("Приватность")
        self.privbtn.clicked.connect(self.privacy)
        self.privbtn.setMinimumSize(150, 35)
        self.privbtn.setMaximumSize(150, 35)
        self.profilebtn = QPushButton("Профиль")
        self.profilebtn.clicked.connect(self.profile)
        self.profilebtn.setMinimumSize(150, 35)
        self.profilebtn.setMaximumSize(150, 35)
        self.setbtn = QPushButton("⚙")
        self.setbtn.clicked.connect(self.settings)
        self.setbtn.setMinimumSize(35, 35)
        self.setbtn.setMaximumSize(35, 35)

        self.frontbtn.hide()
        self.securbtn.hide()
        self.workbtn.hide()
        self.privbtn.hide()
        self.profilebtn.hide()
        self.setbtn.hide()

        self.layoutVMenu = QVBoxLayout()
        self.layoutMain = QHBoxLayout()

        self.layoutVMenu.addWidget(self.frontbtn, alignment= Qt.AlignTop)
        self.layoutVMenu.addWidget(self.securbtn, alignment= Qt.AlignTop)
        self.layoutVMenu.addWidget(self.workbtn, alignment= Qt.AlignTop)
        self.layoutVMenu.addWidget(self.privbtn, alignment= Qt.AlignTop)
        self.layoutVMenu.addWidget(self.profilebtn, alignment= Qt.AlignTop)
        self.layoutVMenu.addWidget(self.setbtn, alignment= Qt.AlignBottom)

        self.frontlbl = QLabel("Главная")
        self.frontlbl.hide()
        self.piclbl = QLabel()
        self.memlbl = QLabel("Вы под защитой")
        self.checkbtn = QPushButton("🔍\nбыстрая проверка")
        self.checkbtn.clicked.connect(self.secure)
        self.historylbl = QLabel("История")
        self.historylist = QListWidget()
        self.historylist.setMaximumHeight(90)
        self.safepix = QPixmap("forAntivirus/safe.jfif")
        self.notsafepix = QPixmap("forAntivirus/notsafe.jfif")

        self.piclbl.setPixmap(self.safepix)

        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()

        self.defH = QHBoxLayout()
        self.defV = QVBoxLayout()

        self.defV.addWidget(self.frontlbl, alignment= Qt.AlignTop)
        self.defH.addWidget(self.piclbl, alignment= Qt.AlignCenter)
        self.defH.addWidget(self.memlbl, alignment= Qt.AlignCenter)
        self.defV.addLayout(self.defH)
        self.defV.addWidget(self.checkbtn)
        self.defV.addWidget(self.historylbl, alignment= Qt.AlignBottom)
        self.defV.addWidget(self.historylist, alignment= Qt.AlignBottom)

        #безопасность
        self.seclbl = QLabel()
        self.secpix = QPixmap("forAntivirus/freerobux.jpg")
        self.seclbl.setPixmap(self.secpix)
        self.seclbl.hide()
        self.fastcheckbtn = QPushButton("Быстрая проверка")
        self.fastcheckbtn.clicked.connect(self.show_afigetkakaybolshayaproverka)
        self.fastlbl = QLabel("Обычно занимает до 5 минут")
        self.allcheckbtn = QPushButton("Полная проверка")
        self.allcheckbtn.clicked.connect(self.show_afigetkakaybolshayaproverka)
        self.alllbl = QLabel("Обычно занимает значительное время\n и может замедлить работу компьютера")
        self.ofigetkakayabolshayaproverkabtn = QPushButton("Афигет какая большая\n и полнейшая проверка чтобы\n ты смог поскучать")
        self.ofigetkakayabolshayaproverkabtn.clicked.connect(self.progress)
        self.ofigetkakayabolshayaproverkabtn.hide()
        self.ofigetkakoybolshoytext = QLabel("Обычно занимает как минимум 10\n минут и ничего не делает кроме как находит\n плохие программы на компьютере")
        self.ofigetkakoybolshoytext.hide()
        self.fastcheckbtn.setMinimumHeight(45)
        self.allcheckbtn.setMinimumHeight(45)
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()

        self.progress_label = QLabel()
        self.progress_label.hide()
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(600)
        self.progress_bar.hide()

        self.defV.addWidget(self.progress_label, alignment= Qt.AlignTop)
        self.defV.addWidget(self.progress_bar, alignment= Qt.AlignTop)

        self.defV.addWidget(self.seclbl, alignment= Qt.AlignTop)
        self.defV.addWidget(self.ofigetkakayabolshayaproverkabtn)
        self.defV.addWidget(self.ofigetkakoybolshoytext)
        self.defV.addWidget(self.fastlbl)
        self.defV.addWidget(self.fastcheckbtn)
        self.defV.addWidget(self.alllbl)
        self.defV.addWidget(self.allcheckbtn)

        #производительность
        self.speed = 1
        self.dupplacebtn = QPushButton("Ускорить ПК")
        self.dupplacebtn.clicked.connect(self.morespeed)
        self.bigfilesbtn = QPushButton("Большие файлы")
        self.bigfilesbtn.clicked.connect(self.bigfiles)
        self.nouseappsbtn = QPushButton("Неиспользуемые приложения")
        self.trashcan = QPixmap("forAntivirus/trashcan.jfif")
        self.trashlbl = QLabel()
        self.trashlbl.setPixmap(self.trashcan)
        self.trashlbl.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.listofbigfiles = QListWidget()
        self.listofbigfiles.addItem("pagefile.sys - больше 2 гигабайт")
        self.listofbigfiles.addItem("ntoskrnl.exe - 1 гигабайт")
        self.listofbigfiles.addItem("MEMORY.DMP - 1.5 гигабайта")
        self.listofbigfiles.hide()
        self.gobackbtn = QPushButton("Не понятно")
        self.gobackbtn.clicked.connect(self.productivity)
        self.gobackbtn.hide()

        self.prodH = QHBoxLayout()

        self.prodH.addWidget(self.dupplacebtn)
        self.prodH.addWidget(self.bigfilesbtn)

        #приватность
        self.privlbl = QLabel()
        self.funnyface = QPixmap("forAntivirus/funnymask.jfif")
        self.privlbl.setPixmap(self.funnyface)
        self.privlbl.hide()
        self.vpnbtn = QPushButton("VPN (не настоящий)")
        self.vpnbtn.clicked.connect(self.vpn)
        self.nodatabtn = QPushButton("Поиск утечки данных")
        self.nodatabtn.clicked.connect(self.nodata)
        self.vpnbtn.hide()
        self.nodatabtn.hide()

        self.defV.addWidget(self.privlbl, alignment= Qt.AlignTop)
        self.defV.addWidget(self.vpnbtn, alignment= Qt.AlignCenter)
        self.defV.addWidget(self.nodatabtn, alignment= Qt.AlignCenter)

        #аккаунт
        self.proflbl = QLabel()
        self.profpix = QPixmap("forAntivirus/menface.jfif")
        self.proflbl.setPixmap(self.profpix)
        self.proflbl.hide()
        self.profilelbl = QLabel("Здравствуйте, " + self.name)
        self.logoutbtn = QPushButton("Выйти (из приложения)")
        self.logoutbtn.clicked.connect(lambda: self.close())
        self.infolbl = QLabel("Подписка активна\nистекает неизвестно дней вперед")
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()

        self.profH = QHBoxLayout()

        self.defV.addWidget(self.proflbl, alignment= Qt.AlignTop)
        self.profH.addWidget(self.profilelbl, alignment= Qt.AlignCenter)
        
        self.defV.addWidget(self.listofbigfiles)
        self.defV.addWidget(self.gobackbtn)
        self.defV.addLayout(self.profH)
        self.defV.addWidget(self.logoutbtn)
        self.defV.addWidget(self.infolbl)

        #настройки
        self.virus = QCheckBox("Вирусы")
        self.virus.clicked.connect(self.flag)
        self.notsafe = QCheckBox("Убрать безопасность")
        self.notsafe.clicked.connect(self.nosecure)
        self.notsafe.hide()
        self.idc = QCheckBox("Я не несу ответственности за ваше\n оборудование и файлы и т. д.")
        self.idc.setChecked(True)
        self.idc.setEnabled(False)
        self.idc.hide()
        self.virus.hide()
        self.nozplbl = QPushButton("Урезать Костяну зарплату на "+ str(self.nozp)+" рублей")
        self.nozplbl.clicked.connect(self.minuszp)
        self.nozplbl.hide()
        self.switchthemes = QComboBox()
        self.switchthemes.addItem("Светлая тема")
        self.switchthemes.addItem("Менее светлая тема")
        self.switchthemes.addItem("Темный Тёма")
        self.switchthemes.addItem("Черный Тёма")
        self.switchthemes.addItem("Отсылка на одно видео где так и было лол")
        self.switchthemes.hide()
        self.switchthemes.currentTextChanged.connect(self.change_style)
        self.activatevirus = QPushButton("Активировать вирусы")
        self.activatevirus.hide()

        self.defV.addWidget(self.switchthemes, alignment= Qt.AlignTop)
        self.defV.addWidget(self.virus, alignment= Qt.AlignTop)
        self.defV.addWidget(self.notsafe, alignment= Qt.AlignCenter)
        self.defV.addWidget(self.idc, alignment= Qt.AlignCenter)
        self.defV.addWidget(self.nozplbl, alignment= Qt.AlignCenter)
        self.defV.addWidget(self.activatevirus, alignment= Qt.AlignBottom)

        self.layoutMain.addLayout(self.layoutVMenu)
        self.layoutMain.addLayout(self.defV)

        self.defV.addWidget(self.trashlbl, alignment= Qt.AlignCenter)
        self.defV.addLayout(self.prodH)
        self.defV.addWidget(self.nouseappsbtn, alignment= Qt.AlignCenter)

        self.layoutMain.addLayout(self.layoutLogin)

        self.setLayout(self.layoutMain)
        self.setStyleSheet('''QWidget {
    background-color: #f5f5f5;
    color: #333333;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Стили для главного окна */
QMainWindow {
    background-color: #ffffff;
}

/* Стили для заголовков */
QLabel#title {
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
}

/* Стили для кнопок */
QPushButton {
    background-color: #3498db;
    color: white;
    border: 1px solid #2980b9;
    border-radius: 4px;
    padding: 5px 10px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #2980b9;
}

QPushButton:pressed {
    background-color: #1d6fa5;
}

QPushButton:disabled {
    background-color: #bdc3c7;
    border-color: #95a5a6;
}

/* Стили для кнопок сканирования */
QPushButton.scan-button {
    background-color: #2ecc71;
    border-color: #27ae60;
}

QPushButton.scan-button:hover {
    background-color: #27ae60;
}

QPushButton.scan-button:pressed {
    background-color: #219653;
}

/* Стили для кнопок карантина/удаления */
QPushButton.danger-button {
    background-color: #e74c3c;
    border-color: #c0392b;
}

QPushButton.danger-button:hover {
    background-color: #c0392b;
}

QPushButton.danger-button:pressed {
    background-color: #a93226;
}

/* Стили для QLineEdit */
QLineEdit {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    padding: 5px;
}

QLineEdit:focus {
    border: 1px solid #3498db;
}

/* Стили для QComboBox */
QComboBox {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #3498db;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #bdc3c7;
    border-left-style: solid;
}

/* Стили для QTabWidget */
QTabWidget::pane {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    margin-top: 5px;
}

QTabBar::tab {
    background-color: #ecf0f1;
    border: 1px solid #bdc3c7;
    border-bottom: none;
    padding: 5px 15px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:selected {
    background-color: #ffffff;
    border-bottom-color: #ffffff;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background-color: #d6eaf8;
}

/* Стили для QProgressBar */
QProgressBar {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    text-align: center;
    background-color: white;
}

QProgressBar::chunk {
    background-color: #2ecc71;
    width: 10px;
}

/* Стили для QListWidget и QTreeWidget */
QListWidget, QTreeWidget {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    alternate-background-color: #f8f9fa;
}

QListWidget::item:hover, QTreeWidget::item:hover {
    background-color: #e3f2fd;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background-color: #3498db;
    color: white;
}

/* Стили для QScrollBar */
QScrollBar:vertical {
    border: none;
    background: #ecf0f1;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #bdc3c7;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #95a5a6;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
}

/* Стили для статусбара */
QStatusBar {
    background-color: #ecf0f1;
    border-top: 1px solid #bdc3c7;
}

/* Стили для группы элементов */
QGroupBox {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    margin-top: 10px;
    padding-top: 15px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QCheckBox::indicator:checked {
    background-color: #3498db;
    border: 2px solid #3498db;
    image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="white" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>');
}

QRadioButton::indicator:unchecked {
    image: url(:/icons/radiobutton_unchecked.png);
}

QRadioButton::indicator:checked {
    image: url(:/icons/radiobutton_checked.png);
}

/* Стили для иконок состояния */
QLabel.status-icon {
    qproperty-alignment: AlignCenter;
}

QLabel.status-safe {
    color: #2ecc71;
}

QLabel.status-warning {
    color: #f39c12;
}

QLabel.status-danger {
    color: #e74c3c;
}''')

        self.show()
    def register(self):
        self.password = self.passwordedit.text()
        self.nums = '1234567890'
        self.letters = 'qwertyuiopasdfghjklzxcvbnm'
        self.bigletters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.specialchars = '!@#$%^&*()'
        self.loging = False
        if self.password == self.passwordsafety.text() and len(self.password) != 0:
            self.name = self.mailedit.text()
            self.profilelbl.setText("Здравствуйте, " + self.mailedit.text())
            self.message.setText("")
            for char in self.password:
                if (char in self.nums) or (char in self.letters) or (char in self.bigletters) or (char in self.specialchars):
                    self.loging = True
                else:
                    self.loging = False
                    self.message.setText("недопусимый символ: " + char)
                    break
                    
        else:
            self.message.setText("Ошибка в паролях")
        if self.loging:
            self.mailedit.hide()
            self.passwordedit.hide()
            self.passwordsafety.hide()
            self.signinbtn.hide()
            self.emaillbl.hide()
            self.passlbl.hide()
            self.secpasslbl.hide()
            self.message.hide()
            self.gotologinbtn.hide()
            self.frontlbl.show()
            self.frontbtn.show()
            self.securbtn.show()
            self.workbtn.show()
            self.privbtn.show()
            self.profilebtn.show()
            self.setbtn.show()
            self.piclbl.show()
            self.memlbl.show()
            self.checkbtn.show()
            self.historylbl.show()
            self.historylist.show()

    def main(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.frontbtn.text())
        self.frontlbl.setText("Главная")
        self.piclbl.show()
        self.memlbl.show()
        self.checkbtn.show()
        self.historylbl.show()
        self.historylist.show()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.hide()
        self.privlbl.hide()
        self.proflbl.hide()
        self.seclbl.hide()
        self.notsafe.hide()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def secure(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.securbtn.text())
        self.frontlbl.setText("Безопасность")
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.fastcheckbtn.show()
        self.allcheckbtn.show()
        self.fastlbl.show()
        self.alllbl.show()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.hide()
        self.privlbl.hide()
        self.proflbl.hide()
        self.seclbl.show()
        self.notsafe.hide()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def productivity(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.workbtn.text())
        self.frontlbl.setText("Производительность")
        self.dupplacebtn.show()
        self.bigfilesbtn.show()
        self.nouseappsbtn.show()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.show()
        self.privlbl.hide()
        self.proflbl.hide()
        self.seclbl.hide()
        self.notsafe.hide()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def privacy(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.privbtn.text())
        self.frontlbl.setText("Приватность")
        self.vpnbtn.show()
        self.nodatabtn.show()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.hide()
        self.privlbl.show()
        self.proflbl.hide()
        self.seclbl.hide()
        self.notsafe.hide()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def profile(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.profilebtn.text())
        self.frontlbl.setText("Профиль")
        self.profilelbl.show()
        self.logoutbtn.show()
        self.infolbl.show()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.hide()
        self.privlbl.hide()
        self.proflbl.show()
        self.seclbl.hide()
        self.notsafe.hide()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def settings(self):
        self.historylist.addItem("Ты нажал на кнопку " + self.setbtn.text())
        self.frontlbl.setText("На стройки")
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.virus.show()
        self.switchthemes.show()
        self.idc.show()
        self.nozplbl.show()
        self.trashlbl.hide()
        self.privlbl.hide()
        self.proflbl.hide()
        self.seclbl.hide()
        self.notsafe.show()
        self.listofbigfiles.hide()
        self.gobackbtn.hide()
        self.progress_bar.hide()
    def flag(self):
        if self.virus.isChecked():
            self.activatevirus.show()
        else: self.activatevirus.hide()
    def minuszp(self):
        self.nozp *= 2
        self.nozplbl.setText("Урезать Костяну зарплату на "+str(self.nozp)+" рублей")
    def change_style(self):
        if self.switchthemes.currentIndex() == 0:
            self.setStyleSheet("")
            self.piclbl.setPixmap(self.safepix)
            self.setStyleSheet('''QWidget {
    background-color: #f5f5f5;
    color: #333333;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Стили для главного окна */
QMainWindow {
    background-color: #ffffff;
}

/* Стили для заголовков */
QLabel#title {
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
}

/* Стили для кнопок */
QPushButton {
    background-color: #3498db;
    color: white;
    border: 1px solid #2980b9;
    border-radius: 4px;
    padding: 5px 10px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #2980b9;
}

QPushButton:pressed {
    background-color: #1d6fa5;
}

QPushButton:disabled {
    background-color: #bdc3c7;
    border-color: #95a5a6;
}

/* Стили для кнопок сканирования */
QPushButton.scan-button {
    background-color: #2ecc71;
    border-color: #27ae60;
}

QPushButton.scan-button:hover {
    background-color: #27ae60;
}

QPushButton.scan-button:pressed {
    background-color: #219653;
}

/* Стили для кнопок карантина/удаления */
QPushButton.danger-button {
    background-color: #e74c3c;
    border-color: #c0392b;
}

QPushButton.danger-button:hover {
    background-color: #c0392b;
}

QPushButton.danger-button:pressed {
    background-color: #a93226;
}

/* Стили для QLineEdit */
QLineEdit {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    padding: 5px;
}

QLineEdit:focus {
    border: 1px solid #3498db;
}

/* Стили для QComboBox */
QComboBox {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #3498db;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #bdc3c7;
    border-left-style: solid;
}

/* Стили для QTabWidget */
QTabWidget::pane {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    margin-top: 5px;
}

QTabBar::tab {
    background-color: #ecf0f1;
    border: 1px solid #bdc3c7;
    border-bottom: none;
    padding: 5px 15px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:selected {
    background-color: #ffffff;
    border-bottom-color: #ffffff;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background-color: #d6eaf8;
}

/* Стили для QProgressBar */
QProgressBar {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    text-align: center;
    background-color: white;
}

QProgressBar::chunk {
    background-color: #2ecc71;
    width: 10px;
}

/* Стили для QListWidget и QTreeWidget */
QListWidget, QTreeWidget {
    background-color: white;
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    alternate-background-color: #f8f9fa;
}

QListWidget::item:hover, QTreeWidget::item:hover {
    background-color: #e3f2fd;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background-color: #3498db;
    color: white;
}

/* Стили для QScrollBar */
QScrollBar:vertical {
    border: none;
    background: #ecf0f1;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #bdc3c7;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #95a5a6;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
}

/* Стили для статусбара */
QStatusBar {
    background-color: #ecf0f1;
    border-top: 1px solid #bdc3c7;
}

/* Стили для группы элементов */
QGroupBox {
    border: 1px solid #bdc3c7;
    border-radius: 3px;
    margin-top: 10px;
    padding-top: 15px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QCheckBox::indicator:checked {
    background-color: #3498db;
    border: 2px solid #3498db;
    image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="white" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>');
}

QRadioButton::indicator:unchecked {
    image: url(:/icons/radiobutton_unchecked.png);
}

QRadioButton::indicator:checked {
    image: url(:/icons/radiobutton_checked.png);
}

/* Стили для иконок состояния */
QLabel.status-icon {
    qproperty-alignment: AlignCenter;
}

QLabel.status-safe {
    color: #2ecc71;
}

QLabel.status-warning {
    color: #f39c12;
}

QLabel.status-danger {
    color: #e74c3c;
}''')
        elif self.switchthemes.currentIndex() == 1:
            self.setStyleSheet("")
            self.piclbl.setPixmap(self.safepix)
            self.setStyleSheet('''/* Основные стили для полутемной темы антивируса */
QWidget {
    background-color: #e0e0e0;
    color: #333333;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Стили для главного окна */
QMainWindow {
    background-color: #f0f0f0;
    border: 1px solid #cccccc;
}

/* Стили для заголовков */
QLabel#title {
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
}

/* Стили для кнопок */
QPushButton {
    background-color: #5d9cec;
    color: white;
    border: 1px solid #4a89dc;
    border-radius: 4px;
    padding: 5px 10px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #4a89dc;
}

QPushButton:pressed {
    background-color: #3b7dd8;
}

QPushButton:disabled {
    background-color: #aab2bd;
    border-color: #999999;
}

/* Стили для кнопок сканирования */
QPushButton.scan-button {
    background-color: #48cfad;
    border-color: #37bc9b;
}

QPushButton.scan-button:hover {
    background-color: #37bc9b;
}

QPushButton.scan-button:pressed {
    background-color: #2ca189;
}

/* Стили для кнопок карантина/удаления */
QPushButton.danger-button {
    background-color: #ed5565;
    border-color: #da4453;
}

QPushButton.danger-button:hover {
    background-color: #da4453;
}

QPushButton.danger-button:pressed {
    background-color: #c23342;
}

/* Стили для QLineEdit */
QLineEdit {
    background-color: white;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    padding: 5px;
}

QLineEdit:focus {
    border: 1px solid #5d9cec;
}

/* Стили для QComboBox */
QComboBox {
    background-color: white;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #5d9cec;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #d0d0d0;
    border-left-style: solid;
}

/* Стили для QTabWidget */
QTabWidget::pane {
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    margin-top: 5px;
    background-color: #f5f5f5;
}

QTabBar::tab {
    background-color: #e6e6e6;
    border: 1px solid #d0d0d0;
    border-bottom: none;
    padding: 5px 15px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:selected {
    background-color: #f5f5f5;
    border-bottom-color: #f5f5f5;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background-color: #d9edf7;
}

/* Стили для QProgressBar */
QProgressBar {
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    text-align: center;
    background-color: white;
}

QProgressBar::chunk {
    background-color: #48cfad;
    width: 10px;
}

/* Стили для QListWidget и QTreeWidget */
QListWidget, QTreeWidget {
    background-color: white;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    alternate-background-color: #f8f9fa;
}

QListWidget::item:hover, QTreeWidget::item:hover {
    background-color: #e3f2fd;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background-color: #5d9cec;
    color: white;
}

/* Стили для QScrollBar */
QScrollBar:vertical {
    border: none;
    background: #e6e6e6;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #b5b5b5;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #999999;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
}

/* Стили для статусбара */
QStatusBar {
    background-color: #e6e6e6;
    border-top: 1px solid #d0d0d0;
    color: #555555;
}

/* Стили для группы элементов */
QGroupBox {
    border: 1px solid #d0d0d0;
    border-radius: 3px;
    margin-top: 10px;
    padding-top: 15px;
    font-weight: bold;
    background-color: #f5f5f5;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #3a3a3a;
}

/* Стили для чекбоксов и радиокнопок */
QCheckBox, QRadioButton {
    spacing: 5px;
    color: #333333;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
    background-color: white;
    border: 1px solid #d0d0d0;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    image: url(:/icons/checkbox_checked.png);
    background-color: #5d9cec;
    border: 1px solid #4a89dc;
}

QRadioButton::indicator {
    border-radius: 8px;
}

QRadioButton::indicator:checked {
    image: url(:/icons/radiobutton_checked.png);
    background-color: #5d9cec;
    border: 1px solid #4a89dc;
}

/* Стили для иконок состояния */
QLabel.status-icon {
    qproperty-alignment: AlignCenter;
}

QLabel.status-safe {
    color: #48cfad;
}

QLabel.status-warning {
    color: #ffaa00;
}

QLabel.status-danger {
    color: #ed5565;
}

/* Стили для разделителей */
QFrame[frameShape="4"], QFrame[frameShape="5"] { /* HLine и VLine */
    color: #d0d0d0;
}

/* Стили для меню */
QMenuBar {
    background-color: #e6e6e6;
    border-bottom: 1px solid #d0d0d0;
}

QMenuBar::item {
    background: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background: #d9edf7;
}

QMenu {
    background-color: #f5f5f5;
    border: 1px solid #d0d0d0;
}

QMenu::item:selected {
    background-color: #5d9cec;
    color: white;
}''')
        elif self.switchthemes.currentIndex() == 2:
            self.setStyleSheet("")
            self.piclbl.setPixmap(self.safepix)
            self.setStyleSheet('''/* Основные стили для тёмной темы антивируса */
QWidget {
    background-color: #2d2d2d;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Стили для главного окна */
QMainWindow {
    background-color: #252525;
    border: 1px solid #3a3a3a;
}

/* Стили для заголовков */
QLabel#title {
    font-size: 18px;
    font-weight: bold;
    color: #5d9cec;
}

/* Стили для кнопок */
QPushButton {
    background-color: #3a3f4b;
    color: #e0e0e0;
    border: 1px solid #4a515f;
    border-radius: 4px;
    padding: 5px 10px;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #4a515f;
    border-color: #5a6270;
}

QPushButton:pressed {
    background-color: #2a303a;
}

QPushButton:disabled {
    background-color: #353535;
    border-color: #454545;
    color: #707070;
}

/* Стили для кнопок сканирования */
QPushButton.scan-button {
    background-color: #2a7d5f;
    border-color: #1e6b50;
    color: #e0e0e0;
}

QPushButton.scan-button:hover {
    background-color: #1e6b50;
}

QPushButton.scan-button:pressed {
    background-color: #155a43;
}

/* Стили для кнопок карантина/удаления */
QPushButton.danger-button {
    background-color: #7d2a2a;
    border-color: #6b1e1e;
    color: #e0e0e0;
}

QPushButton.danger-button:hover {
    background-color: #6b1e1e;
}

QPushButton.danger-button:pressed {
    background-color: #5a1515;
}

/* Стили для QLineEdit */
QLineEdit {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #4a4a4a;
    border-radius: 3px;
    padding: 5px;
    selection-background-color: #5d9cec;
    selection-color: white;
}

QLineEdit:focus {
    border: 1px solid #5d9cec;
}

/* Стили для QComboBox */
QComboBox {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #4a4a4a;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border: 1px solid #5d9cec;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #4a4a4a;
    border-left-style: solid;
}

QComboBox QAbstractItemView {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #5d9cec;
    selection-background-color: #5d9cec;
    selection-color: white;
}

/* Стили для QTabWidget */
QTabWidget::pane {
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    margin-top: 5px;
    background-color: #2d2d2d;
}

QTabBar::tab {
    background-color: #353535;
    color: #b0b0b0;
    border: 1px solid #3a3a3a;
    border-bottom: none;
    padding: 5px 15px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

QTabBar::tab:selected {
    background-color: #2d2d2d;
    color: #e0e0e0;
    border-bottom-color: #2d2d2d;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background-color: #3d3d3d;
    color: #e0e0e0;
}

/* Стили для QProgressBar */
QProgressBar {
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    text-align: center;
    background-color: #353535;
    color: #e0e0e0;
}

QProgressBar::chunk {
    background-color: #2a7d5f;
    width: 10px;
}

/* Стили для QListWidget и QTreeWidget */
QListWidget, QTreeWidget {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    alternate-background-color: #3a3a3a;
}

QListWidget::item:hover, QTreeWidget::item:hover {
    background-color: #4a515f;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background-color: #5d9cec;
    color: white;
}

/* Стили для QScrollBar */
QScrollBar:vertical {
    border: none;
    background: #353535;
    width: 10px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #5a5a5a;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #6a6a6a;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
}

/* Стили для статусбара */
QStatusBar {
    background-color: #353535;
    border-top: 1px solid #3a3a3a;
    color: #b0b0b0;
}

/* Стили для группы элементов */
QGroupBox {
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    margin-top: 10px;
    padding-top: 15px;
    font-weight: bold;
    background-color: #2d2d2d;
    color: #e0e0e0;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #b0b0b0;
}

/* Стили для чекбоксов и радиокнопок */
QCheckBox, QRadioButton {
    spacing: 5px;
    color: #e0e0e0;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
    background-color: #353535;
    border: 1px solid #4a4a4a;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    image: url(:/icons/checkbox_checked_dark.png);
    background-color: #5d9cec;
    border: 1px solid #4a89dc;
}

QRadioButton::indicator {
    border-radius: 8px;
}

QRadioButton::indicator:checked {
    image: url(:/icons/radiobutton_checked_dark.png);
    background-color: #5d9cec;
    border: 1px solid #4a89dc;
}

/* Стили для иконок состояния */
QLabel.status-icon {
    qproperty-alignment: AlignCenter;
}

QLabel.status-safe {
    color: #48cfad;
}

QLabel.status-warning {
    color: #f6bb42;
}

QLabel.status-danger {
    color: #ed5565;
}

/* Стили для разделителей */
QFrame[frameShape="4"], QFrame[frameShape="5"] { /* HLine и VLine */
    color: #3a3a3a;
}

/* Стили для меню */
QMenuBar {
    background-color: #353535;
    color: #e0e0e0;
    border-bottom: 1px solid #3a3a3a;
}

QMenuBar::item {
    background: transparent;
    padding: 5px 10px;
}

QMenuBar::item:selected {
    background: #4a515f;
}

QMenu {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
}

QMenu::item:selected {
    background-color: #5d9cec;
    color: white;
}

/* Стили для QToolTip */
QToolTip {
    background-color: #454545;
    color: #e0e0e0;
    border: 1px solid #5a5a5a;
    padding: 3px;
    border-radius: 3px;
    opacity: 230;
}

/* Стили для QHeaderView (заголовки таблиц) */
QHeaderView::section {
    background-color: #3a3a3a;
    color: #e0e0e0;
    padding: 5px;
    border: 1px solid #2d2d2d;
}

QHeaderView::section:hover {
    background-color: #4a4a4a;
}

/* Стили для QTableView */
QTableView {
    background-color: #353535;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    gridline-color: #3a3a3a;
    alternate-background-color: #3a3a3a;
}

QTableView::item:hover {
    background-color: #4a515f;
}

QTableView::item:selected {
    background-color: #5d9cec;
    color: white;
}''')
        elif self.switchthemes.currentIndex() == 3:
            self.setStyleSheet("")
            self.piclbl.setPixmap(self.safepix)
            self.setStyleSheet('''/* Основные стили для чёрной темы */
QWidget {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    border: none;
}

/* Главное окно */
QMainWindow {
    background-color: #000000;
    border: 1px solid #333333;
}

/* Заголовки */
QLabel#title {
    font-size: 18px;
    font-weight: bold;
    color: #4a90e2;
    text-shadow: 0 0 5px rgba(74, 144, 226, 0.3);
}

/* Кнопки */
QPushButton {
    background-color: #222222;
    color: #e0e0e0;
    border: 1px solid #333333;
    border-radius: 4px;
    padding: 6px 12px;
    min-width: 100px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #2a2a2a;
    border-color: #444444;
}

QPushButton:pressed {
    background-color: #1a1a1a;
}

QPushButton:disabled {
    background-color: #181818;
    color: #606060;
    border-color: #282828;
}

/* Кнопки сканирования */
QPushButton.scan-button {
    background-color: #1e5631;
    border-color: #2a7042;
}

QPushButton.scan-button:hover {
    background-color: #2a7042;
}

QPushButton.scan-button:pressed {
    background-color: #134826;
}

/* Опасные кнопки */
QPushButton.danger-button {
    background-color: #5c1a1a;
    border-color: #7a2323;
}

QPushButton.danger-button:hover {
    background-color: #7a2323;
}

QPushButton.danger-button:pressed {
    background-color: #4a1515;
}

/* Поля ввода */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #181818;
    color: #e0e0e0;
    border: 1px solid #333333;
    border-radius: 3px;
    padding: 5px;
    selection-background-color: #4a90e2;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a90e2;
}

/* Выпадающие списки */
QComboBox {
    background-color: #181818;
    color: #e0e0e0;
    border: 1px solid #333333;
    border-radius: 3px;
    padding: 5px;
    min-width: 100px;
}

QComboBox:hover {
    border-color: #444444;
}

QComboBox::drop-down {
    border-left: 1px solid #333333;
}

QComboBox QAbstractItemView {
    background-color: #181818;
    color: #e0e0e0;
    border: 1px solid #4a90e2;
}

/* Вкладки */
QTabWidget::pane {
    border: 1px solid #333333;
    background-color: #121212;
}

QTabBar::tab {
    background-color: #222222;
    color: #b0b0b0;
    border: 1px solid #333333;
    padding: 6px 12px;
}

QTabBar::tab:selected {
    background-color: #121212;
    color: #e0e0e0;
    border-bottom: 1px solid #121212;
}

QTabBar::tab:hover {
    background-color: #2a2a2a;
}

/* Прогресс-бар */
QProgressBar {
    border: 1px solid #333333;
    border-radius: 3px;
    background-color: #181818;
    text-align: center;
    color: #e0e0e0;
}

QProgressBar::chunk {
    background-color: #2a7042;
    border-radius: 2px;
}

/* Списки и деревья */
QListWidget, QTreeWidget, QTableView {
    background-color: #181818;
    color: #e0e0e0;
    border: 1px solid #333333;
    alternate-background-color: #1a1a1a;
}

QListWidget::item:hover, QTreeWidget::item:hover {
    background-color: #2a2a2a;
}

QListWidget::item:selected, QTreeWidget::item:selected {
    background-color: #4a90e2;
    color: white;
}

/* Полосы прокрутки */
QScrollBar:vertical {
    background: #181818;
    width: 12px;
}

QScrollBar::handle:vertical {
    background: #333333;
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #444444;
}

/* Статусбар */
QStatusBar {
    background-color: #181818;
    color: #b0b0b0;
    border-top: 1px solid #333333;
}

/* Группы */
QGroupBox {
    border: 1px solid #333333;
    border-radius: 3px;
    margin-top: 12px;
    padding-top: 18px;
    background-color: #181818;
    color: #e0e0e0;
}

QGroupBox::title {
    color: #b0b0b0;
    subcontrol-origin: margin;
    left: 10px;
}

/* Чекбоксы и радиокнопки */
QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
    background-color: #181818;
    border: 1px solid #333333;
}

QCheckBox::indicator:checked {
    background-color: #4a90e2;
    border: 1px solid #5aa0f2;
}

QRadioButton::indicator:checked {
    background-color: #4a90e2;
    border: 1px solid #5aa0f2;
}

/* Меню */
QMenuBar {
    background-color: #181818;
    color: #e0e0e0;
}

QMenuBar::item:selected {
    background-color: #2a2a2a;
}

QMenu {
    background-color: #181818;
    color: #e0e0e0;
    border: 1px solid #333333;
}

QMenu::item:selected {
    background-color: #4a90e2;
    color: white;
}

/* ToolTip */
QToolTip {
    background-color: #222222;
    color: #e0e0e0;
    border: 1px solid #4a90e2;
    padding: 4px;
    border-radius: 3px;
}

/* Разделители */
QFrame[frameShape="4"], QFrame[frameShape="5"] {
    color: #333333;
}

/* Иконки состояния */
QLabel.status-icon {
    qproperty-alignment: AlignCenter;
}

QLabel.status-safe {
    color: #2a7042;
}

QLabel.status-warning {
    color: #e6a23c;
}

QLabel.status-danger {
    color: #f56c6c;
}

/* Специальные эффекты */
QPushButton.important-button {
    background-color: #4a90e2;
    color: white;
    border: 1px solid #5aa0f2;
}

QPushButton.important-button:hover {
    background-color: #5aa0f2;
}''')
        elif self.switchthemes.currentIndex() == 4:
            self.piclbl.setPixmap(QPixmap("forAntivirus/lol.png"))
            self.main()
    def nosecure(self):
        if self.notsafe.isChecked():
            self.securbtn.hide()
            self.memlbl.setText("вы не под защитой")
            self.piclbl.setPixmap(self.notsafepix)
            self.main()
        else: 
            self.securbtn.show()
            self.piclbl.setPixmap(self.safepix)
            self.memlbl.setText("вы под защитой")
    def nologin(self):
        QMessageBox.information(None, "лол", "я не смог сделать работу с JSON файлами чтобы сохранять дату, и изза этого ты можешь только регаться")
    def vpn(self):
        newip = str(randint(1,9999)) + '.' + str(randint(1,9999)) + '.' + str(randint(1,9999)) + '.' + str(randint(1,9999))
        QMessageBox.information(None, "vpn", "Ваш новый IP адрес: " + newip)
    def nodata(self):
        QMessageBox.information(None, "Поиск утечки данных", "Ваши даные сливаются через интернет")
    def morespeed(self):
        QMessageBox.information(None, "Скорость", "Скорость: " + str(self.speed) + "км/ч")
        self.speed = str(int(self.speed) * 2)
    def bigfiles(self):
        self.piclbl.hide()
        self.memlbl.hide()
        self.checkbtn.hide()
        self.historylbl.hide()
        self.historylist.hide()
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()
        self.vpnbtn.hide()
        self.nodatabtn.hide()
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()
        self.virus.hide()
        self.switchthemes.hide()
        self.activatevirus.hide()
        self.idc.hide()
        self.nozplbl.hide()
        self.trashlbl.hide()
        self.privlbl.hide()
        self.proflbl.hide()
        self.seclbl.hide()
        self.notsafe.hide()
        self.listofbigfiles.show()
        self.gobackbtn.show()
    def progress(self):
        files = ["atieclxx.exe", 'atiumd6a.cap', 'AUDIOKSE.dll', 'auditpol.exe', 'AuthHost.exe', 'AxInstUI.exe', 'explorer.exe', 'bcdedit.exe', 'bdeunlock.exe', 'resmon.exe', 'taskmgr.exe', 'BOOTVID.DLL',
        'bthudtask.exe', 'C_850.NLS', 'certreq.exe', 'choice.exe', 'cic.dll', 'cleanmgr.exe', 'ClipRenew.exe', 'cmd.exe', 'cmmon32.exe', 'DeviceEject.exe', 'dgtrayicon.exe', 'Dism.exe', 'wsl.exe', 'chrome.exe', 'svhost.exe', 'poker.exe', 'taiwan is a free countery.exe', ':D', 'D:', '\(O_O)/'] * 100
        self.progress_label.show()
        self.progress_bar.show()
        self.ofigetkakayabolshayaproverkabtn.hide()
        self.ofigetkakoybolshoytext.hide()
    def show_afigetkakaybolshayaproverka(self):
        if self.counter == 1:
            self.allcheckbtn.hide()
        if self.counter == 0:
            self.fastcheckbtn.hide()
            self.ofigetkakayabolshayaproverkabtn.show()
            self.ofigetkakoybolshoytext.show()
            self.counter = 1
            self.fastlbl.hide()
            self.alllbl.hide()
        


       



root = Windows()
app.exec_()
    