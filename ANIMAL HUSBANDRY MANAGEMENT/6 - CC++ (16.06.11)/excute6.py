# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QDialog
from main6 import Ui_MainWindow  # here you need to correct the names
from menu6 import Ui_Dialog  # here you need to correct the names

#excute mail window
app = QApplication(sys.argv)
window = QMainWindow()
ui_main = Ui_MainWindow()
ui_main.setupUi(window)

#excute e-mail dialog
dialog = QDialog();
ui_menu = Ui_Dialog()
ui_menu.setupUi(dialog)

#set connection from button
ui_main.btn_search.clicked.connect(ui_main.search)
ui_main.btn_menu.clicked.connect(dialog.show)

ui_menu.btn_email_send.clicked.connect(ui_menu.send)
ui_menu.btn_C_save.clicked.connect(ui_menu.save)

#show main window
window.show()
sys.exit(app.exec_())