# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication, QMainWindow
from test import Ui_MainWindow  # here you need to correct the names

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())