from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

app = QApplication([])


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фейк антивирус")
        self.setMinimumSize(400, 275)
        self.setMaximumSize(400,275)

        self.nozp = 1
        
        #логин
        self.mailedit = QLineEdit()
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
        self.signinbtn.clicked.connect(self.login)
        self.signinbtn.setMinimumSize(150, 25)
        self.signinbtn.setMaximumSize(150, 25)
        self.emaillbl = QLabel("Укажите свою почту:")
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
        self.piclbl = QLabel("тут")
        self.memlbl = QLabel("Вы под защитой")
        self.checkbtn = QPushButton("🔍\nбыстрая проверка")
        self.checkbtn.clicked.connect(self.secure)
        self.historylbl = QLabel("История")
        self.historylist = QListWidget()
        self.historylist.setMaximumHeight(90)
        self.safepix = QPixmap("safe.jfif")
        self.notsafepix = QPixmap("notsafe.jfif")

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
        self.secpix = QPixmap("freerobux.jpg")
        self.seclbl.setPixmap(self.secpix)
        self.seclbl.hide()
        self.fastcheckbtn = QPushButton("Быстрая проверка")
        self.fastlbl = QLabel("Обычно занимает до 5 минут")
        self.allcheckbtn = QPushButton("Полная проверка")
        self.alllbl = QLabel("Обычно занимает значительное время и может замедлить работу компьютера")
        self.fastcheckbtn.setMinimumHeight(45)
        self.allcheckbtn.setMinimumHeight(45)
        self.fastcheckbtn.hide()
        self.allcheckbtn.hide()
        self.fastlbl.hide()
        self.alllbl.hide()

        self.defV.addWidget(self.seclbl, alignment= Qt.AlignTop)
        self.defV.addWidget(self.fastlbl)
        self.defV.addWidget(self.fastcheckbtn)
        self.defV.addWidget(self.alllbl)
        self.defV.addWidget(self.allcheckbtn)

        #производительность
        self.dupplacebtn = QPushButton("Дупликаты файлов")
        self.bigfilesbtn = QPushButton("Большие файлы")
        self.nouseappsbtn = QPushButton("Неиспользуемые приложения")
        self.trashcan = QPixmap("trashcan.jfif")
        self.trashlbl = QLabel()
        self.trashlbl.setPixmap(self.trashcan)
        self.trashlbl.hide()
        self.dupplacebtn.hide()
        self.bigfilesbtn.hide()
        self.nouseappsbtn.hide()

        self.prodH = QHBoxLayout()

        self.prodH.addWidget(self.dupplacebtn)
        self.prodH.addWidget(self.bigfilesbtn)

        #приватность
        self.privlbl = QLabel()
        self.funnyface = QPixmap("funnymask.jfif")
        self.privlbl.setPixmap(self.funnyface)
        self.privlbl.hide()
        self.vpnbtn = QPushButton("VPN соединение (не настоящее)")
        self.nodatabtn = QPushButton("Поиск утечки данных")
        self.vpnbtn.hide()
        self.nodatabtn.hide()

        self.defV.addWidget(self.privlbl, alignment= Qt.AlignTop)
        self.defV.addWidget(self.vpnbtn, alignment= Qt.AlignCenter)
        self.defV.addWidget(self.nodatabtn, alignment= Qt.AlignCenter)

        #аккаунт
        self.proflbl = QLabel()
        self.profpix = QPixmap("menface.jfif")
        self.proflbl.setPixmap(self.profpix)
        self.proflbl.hide()
        self.profilelbl = QLabel("Здравствуйте, " + self.name)
        self.logoutbtn = QPushButton("Выйти (из приложения)")
        self.infolbl = QLabel("Подписка активна\nистекает неизвестно дней вперед")
        self.profilelbl.hide()
        self.logoutbtn.hide()
        self.infolbl.hide()

        self.profH = QHBoxLayout()

        self.defV.addWidget(self.proflbl, alignment= Qt.AlignTop)
        self.profH.addWidget(self.profilelbl, alignment= Qt.AlignCenter)
        
        self.defV.addLayout(self.profH)
        self.defV.addWidget(self.logoutbtn)
        self.defV.addWidget(self.infolbl)

        #настройки
        self.virus = QCheckBox("Вирусы")
        self.virus.clicked.connect(self.flag)
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
    min-width: 80px;
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

/* Стили для чекбоксов и радиокнопок */
QCheckBox, QRadioButton {
    spacing: 5px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    image: url(:/icons/checkbox_unchecked.png);
}

QCheckBox::indicator:checked {
    image: url(:/icons/checkbox_checked.png);
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
    def login(self):
        self.name = self.mailedit.text()
        self.password = self.passwordedit.text()
        self.nums = '1234567890'
        self.letters = 'qwertyuiopasdfghjklzxcvbnm'
        self.bigletters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.specialchars = '!@#$%^&*()'
        self.loging = False
        if self.password == self.passwordsafety.text() and len(self.password) != 0:
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
            self.profilelbl.setText("Здравствуйте, " + self.mailedit.text())
            self.mailedit.hide()
            self.passwordedit.hide()
            self.passwordsafety.hide()
            self.signinbtn.hide()
            self.emaillbl.hide()
            self.passlbl.hide()
            self.secpasslbl.hide()
            self.message.hide()
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
    min-width: 80px;
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

/* Стили для чекбоксов и радиокнопок */
QCheckBox, QRadioButton {
    spacing: 5px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    image: url(:/icons/checkbox_unchecked.png);
}

QCheckBox::indicator:checked {
    image: url(:/icons/checkbox_checked.png);
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


        


root = Windows()
app.exec_()
    