# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QDialog
from main5 import Ui_MainWindow  # here you need to correct the names
from email5 import Ui_Dialog  # here you need to correct the names

#excute mail window
app = QApplication(sys.argv)
window = QMainWindow()
ui_main = Ui_MainWindow()
ui_main.setupUi(window)

#excute e-mail dialog
dialog = QDialog();
ui_email = Ui_Dialog()
ui_email.setupUi(dialog)

#set connection from button
ui_main.btn_search.clicked.connect(ui_main.search)
ui_main.btn_mail.clicked.connect(dialog.show)

ui_email.btn_email_send.clicked.connect(ui_email.send)

#show main window
window.show()
sys.exit(app.exec_())