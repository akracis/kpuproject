# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication, QMainWindow
from test2 import Ui_MainWindow  # here you need to correct the names

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.btn_search.clicked.connect(ui.search)

window.show()
sys.exit(app.exec_())