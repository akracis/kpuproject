# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(520, 563)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.exp_program_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_program_title.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.exp_program_title.setObjectName(_fromUtf8("exp_program_title"))
        self.btn_search = QtGui.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(380, 10, 91, 31))
        self.btn_search.setObjectName(_fromUtf8("btn_search"))
        self.exp_object_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_title.setGeometry(QtCore.QRect(10, 50, 501, 31))
        self.exp_object_title.setObjectName(_fromUtf8("exp_object_title"))
        self.exp_object_number = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_number.setGeometry(QtCore.QRect(10, 80, 91, 31))
        self.exp_object_number.setObjectName(_fromUtf8("exp_object_number"))
        self.exp_object_type = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_type.setGeometry(QtCore.QRect(10, 110, 91, 31))
        self.exp_object_type.setObjectName(_fromUtf8("exp_object_type"))
        self.info_object_number = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_number.setGeometry(QtCore.QRect(100, 80, 161, 31))
        self.info_object_number.setObjectName(_fromUtf8("info_object_number"))
        self.info_object_type = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_type.setGeometry(QtCore.QRect(100, 110, 161, 31))
        self.info_object_type.setObjectName(_fromUtf8("info_object_type"))
        self.exp_object_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_date.setGeometry(QtCore.QRect(260, 80, 91, 31))
        self.exp_object_date.setObjectName(_fromUtf8("exp_object_date"))
        self.exp_object_sex = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_sex.setGeometry(QtCore.QRect(260, 110, 91, 31))
        self.exp_object_sex.setObjectName(_fromUtf8("exp_object_sex"))
        self.info_object_date = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_date.setGeometry(QtCore.QRect(350, 80, 161, 31))
        self.info_object_date.setObjectName(_fromUtf8("info_object_date"))
        self.info_object_sex = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_sex.setGeometry(QtCore.QRect(350, 110, 161, 31))
        self.info_object_sex.setObjectName(_fromUtf8("info_object_sex"))
        self.input_number = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_number.setGeometry(QtCore.QRect(180, 10, 201, 31))
        self.input_number.setObjectName(_fromUtf8("input_number"))
        self.exp_move_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_title.setGeometry(QtCore.QRect(10, 150, 501, 31))
        self.exp_move_title.setObjectName(_fromUtf8("exp_move_title"))
        self.exp_move_cnt = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_cnt.setGeometry(QtCore.QRect(10, 180, 31, 31))
        self.exp_move_cnt.setObjectName(_fromUtf8("exp_move_cnt"))
        self.exp_move_owner = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_owner.setGeometry(QtCore.QRect(40, 180, 101, 31))
        self.exp_move_owner.setObjectName(_fromUtf8("exp_move_owner"))
        self.exp_move_move = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_move.setGeometry(QtCore.QRect(140, 180, 71, 31))
        self.exp_move_move.setObjectName(_fromUtf8("exp_move_move"))
        self.exp_move_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_date.setGeometry(QtCore.QRect(210, 180, 71, 31))
        self.exp_move_date.setObjectName(_fromUtf8("exp_move_date"))
        self.exp_move_location = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_location.setGeometry(QtCore.QRect(280, 180, 231, 31))
        self.exp_move_location.setObjectName(_fromUtf8("exp_move_location"))
        self.exp_butcher_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_title.setGeometry(QtCore.QRect(10, 400, 501, 31))
        self.exp_butcher_title.setObjectName(_fromUtf8("exp_butcher_title"))
        self.exp_butcher_sex = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_sex.setGeometry(QtCore.QRect(370, 460, 61, 31))
        self.exp_butcher_sex.setObjectName(_fromUtf8("exp_butcher_sex"))
        self.info_butcher_sex = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_sex.setGeometry(QtCore.QRect(430, 460, 81, 31))
        self.info_butcher_sex.setObjectName(_fromUtf8("info_butcher_sex"))
        self.exp_butcher_grade = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_grade.setGeometry(QtCore.QRect(10, 460, 91, 31))
        self.exp_butcher_grade.setObjectName(_fromUtf8("exp_butcher_grade"))
        self.info_butcher_date = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_date.setGeometry(QtCore.QRect(430, 430, 81, 31))
        self.info_butcher_date.setObjectName(_fromUtf8("info_butcher_date"))
        self.exp_butcher_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_date.setGeometry(QtCore.QRect(370, 430, 61, 31))
        self.exp_butcher_date.setObjectName(_fromUtf8("exp_butcher_date"))
        self.exp_butcher_location = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_location.setGeometry(QtCore.QRect(10, 430, 91, 31))
        self.exp_butcher_location.setObjectName(_fromUtf8("exp_butcher_location"))
        self.info_butcher_location = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_location.setGeometry(QtCore.QRect(100, 430, 271, 31))
        self.info_butcher_location.setObjectName(_fromUtf8("info_butcher_location"))
        self.info_butcher_grade = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_grade.setGeometry(QtCore.QRect(100, 460, 271, 31))
        self.info_butcher_grade.setObjectName(_fromUtf8("info_butcher_grade"))
        self.info_butcher_factory = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_factory.setGeometry(QtCore.QRect(100, 490, 411, 31))
        self.info_butcher_factory.setObjectName(_fromUtf8("info_butcher_factory"))
        self.exp_butcher_factory = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_factory.setGeometry(QtCore.QRect(10, 490, 91, 31))
        self.exp_butcher_factory.setObjectName(_fromUtf8("exp_butcher_factory"))
        self.btn_menu = QtGui.QPushButton(self.centralwidget)
        self.btn_menu.setGeometry(QtCore.QRect(470, 10, 41, 31))
        self.btn_menu.setObjectName(_fromUtf8("btn_menu"))
        self.info_move_owner_1 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_1.setGeometry(QtCore.QRect(40, 210, 101, 31))
        self.info_move_owner_1.setObjectName(_fromUtf8("info_move_owner_1"))
        self.info_move_date_1 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_1.setGeometry(QtCore.QRect(210, 210, 71, 31))
        self.info_move_date_1.setObjectName(_fromUtf8("info_move_date_1"))
        self.info_move_cnt_1 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_1.setGeometry(QtCore.QRect(10, 210, 31, 31))
        self.info_move_cnt_1.setObjectName(_fromUtf8("info_move_cnt_1"))
        self.info_move_location_1 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_1.setGeometry(QtCore.QRect(280, 210, 231, 31))
        self.info_move_location_1.setObjectName(_fromUtf8("info_move_location_1"))
        self.info_move_move_1 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_1.setGeometry(QtCore.QRect(140, 210, 71, 31))
        self.info_move_move_1.setObjectName(_fromUtf8("info_move_move_1"))
        self.info_move_cnt_2 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_2.setGeometry(QtCore.QRect(10, 240, 31, 31))
        self.info_move_cnt_2.setObjectName(_fromUtf8("info_move_cnt_2"))
        self.info_move_owner_2 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_2.setGeometry(QtCore.QRect(40, 240, 101, 31))
        self.info_move_owner_2.setObjectName(_fromUtf8("info_move_owner_2"))
        self.info_move_date_2 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_2.setGeometry(QtCore.QRect(210, 240, 71, 31))
        self.info_move_date_2.setObjectName(_fromUtf8("info_move_date_2"))
        self.info_move_location_2 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_2.setGeometry(QtCore.QRect(280, 240, 231, 31))
        self.info_move_location_2.setObjectName(_fromUtf8("info_move_location_2"))
        self.info_move_move_2 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_2.setGeometry(QtCore.QRect(140, 240, 71, 31))
        self.info_move_move_2.setObjectName(_fromUtf8("info_move_move_2"))
        self.info_move_cnt_3 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_3.setGeometry(QtCore.QRect(10, 270, 31, 31))
        self.info_move_cnt_3.setObjectName(_fromUtf8("info_move_cnt_3"))
        self.info_move_owner_3 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_3.setGeometry(QtCore.QRect(40, 270, 101, 31))
        self.info_move_owner_3.setObjectName(_fromUtf8("info_move_owner_3"))
        self.info_move_date_3 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_3.setGeometry(QtCore.QRect(210, 270, 71, 31))
        self.info_move_date_3.setObjectName(_fromUtf8("info_move_date_3"))
        self.info_move_location_3 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_3.setGeometry(QtCore.QRect(280, 270, 231, 31))
        self.info_move_location_3.setObjectName(_fromUtf8("info_move_location_3"))
        self.info_move_move_3 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_3.setGeometry(QtCore.QRect(140, 270, 71, 31))
        self.info_move_move_3.setObjectName(_fromUtf8("info_move_move_3"))
        self.info_move_cnt_4 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_4.setGeometry(QtCore.QRect(10, 300, 31, 31))
        self.info_move_cnt_4.setObjectName(_fromUtf8("info_move_cnt_4"))
        self.info_move_owner_4 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_4.setGeometry(QtCore.QRect(40, 300, 101, 31))
        self.info_move_owner_4.setObjectName(_fromUtf8("info_move_owner_4"))
        self.info_move_date_4 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_4.setGeometry(QtCore.QRect(210, 300, 71, 31))
        self.info_move_date_4.setObjectName(_fromUtf8("info_move_date_4"))
        self.info_move_location_4 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_4.setGeometry(QtCore.QRect(280, 300, 231, 31))
        self.info_move_location_4.setObjectName(_fromUtf8("info_move_location_4"))
        self.info_move_move_4 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_4.setGeometry(QtCore.QRect(140, 300, 71, 31))
        self.info_move_move_4.setObjectName(_fromUtf8("info_move_move_4"))
        self.info_move_cnt_5 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_5.setGeometry(QtCore.QRect(10, 330, 31, 31))
        self.info_move_cnt_5.setObjectName(_fromUtf8("info_move_cnt_5"))
        self.info_move_owner_5 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_5.setGeometry(QtCore.QRect(40, 330, 101, 31))
        self.info_move_owner_5.setObjectName(_fromUtf8("info_move_owner_5"))
        self.info_move_date_5 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_5.setGeometry(QtCore.QRect(210, 330, 71, 31))
        self.info_move_date_5.setObjectName(_fromUtf8("info_move_date_5"))
        self.info_move_location_5 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_5.setGeometry(QtCore.QRect(280, 330, 231, 31))
        self.info_move_location_5.setObjectName(_fromUtf8("info_move_location_5"))
        self.info_move_move_5 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_5.setGeometry(QtCore.QRect(140, 330, 71, 31))
        self.info_move_move_5.setObjectName(_fromUtf8("info_move_move_5"))
        self.info_move_cnt_6 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_cnt_6.setGeometry(QtCore.QRect(10, 360, 31, 31))
        self.info_move_cnt_6.setObjectName(_fromUtf8("info_move_cnt_6"))
        self.info_move_owner_6 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_owner_6.setGeometry(QtCore.QRect(40, 360, 101, 31))
        self.info_move_owner_6.setObjectName(_fromUtf8("info_move_owner_6"))
        self.info_move_date_6 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_date_6.setGeometry(QtCore.QRect(210, 360, 71, 31))
        self.info_move_date_6.setObjectName(_fromUtf8("info_move_date_6"))
        self.info_move_location_6 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_location_6.setGeometry(QtCore.QRect(280, 360, 231, 31))
        self.info_move_location_6.setObjectName(_fromUtf8("info_move_location_6"))
        self.info_move_move_6 = QtGui.QTextBrowser(self.centralwidget)
        self.info_move_move_6.setGeometry(QtCore.QRect(140, 360, 71, 31))
        self.info_move_move_6.setObjectName(_fromUtf8("info_move_move_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.exp_program_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">축산물 이력 추적 시스템</span></p></body></html>", None))
        self.btn_search.setText(_translate("MainWindow", "Search", None))
        self.exp_object_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">개체정보</span></p></body></html>", None))
        self.exp_object_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">개체식별번호</p></body></html>", None))
        self.exp_object_type.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">종류</p></body></html>", None))
        self.info_object_number.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_object_type.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.exp_object_date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">출생일자</p></body></html>", None))
        self.exp_object_sex.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">성별</p></body></html>", None))
        self.info_object_date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_object_sex.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.input_number.setPlainText(_translate("MainWindow", "여기에 일련번호를 입력하세요", None))
        self.exp_move_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">이동정보</span></p></body></html>", None))
        self.exp_move_cnt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> No</p></body></html>", None))
        self.exp_move_owner.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">소유주</p></body></html>", None))
        self.exp_move_move.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">이동안내</p></body></html>", None))
        self.exp_move_date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">이동신고일</p></body></html>", None))
        self.exp_move_location.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">사유지</p></body></html>", None))
        self.exp_butcher_title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">도축 및 가공 정보</span></p></body></html>", None))
        self.exp_butcher_sex.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">성별</p></body></html>", None))
        self.info_butcher_sex.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.exp_butcher_grade.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">도축검사결과</p></body></html>", None))
        self.info_butcher_date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.exp_butcher_date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">도축일자</p></body></html>", None))
        self.exp_butcher_location.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">도축장</p></body></html>", None))
        self.info_butcher_location.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_butcher_grade.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_butcher_factory.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.exp_butcher_factory.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">가공장</p></body></html>", None))
        self.btn_menu.setText(_translate("MainWindow", "Menu", None))
        self.info_move_owner_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_owner_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_owner_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_owner_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_owner_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_cnt_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_owner_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_date_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_location_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_move_move_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

    
        
    def search(self):
        #002086431813, 
        from xml.etree import ElementTree
        import http.client
        
        traceNo = self.input_number.toPlainText()
        print("number" + traceNo)
        
        key = "VZwF3B6OId9MZtOCoLO8pS5FCjIXGQj3MYkPenIahW0vcGzgC%2Bb8rJHcYoDRPk%2Fc9dsbldkOhJi0mBewN4UBMg%3D%3D"
        conn = http.client.HTTPConnection("data.ekape.or.kr")
        conn.request("GET", "/openapi-data/service/user/animalTrace/traceNoSearch?ServiceKey=" + key + "&traceNo=" + traceNo) #서버에 GET 요청 

        req = conn.getresponse()    #openAPI 서버에서 보내온 요청을 받아옴
        cLen = bytearray(req.getheader("Content-Length"), 'utf-8')    #가져온 데이터 길이

        moveCnt = 1;
        
        if int(req.status) == 200 :
            print("Animal data downloading complete!")
            strXml = (req.read().decode('utf-8'))    #요청이 성공이면 book 정보 추출
            tree = ElementTree.fromstring(strXml)
            
            itemElements = tree.getiterator("item")
            for item in itemElements:
                if (item.find("infoType")).text == "1" :
                    birthYmd = item.find("birthYmd")    #birthYmd 검색
                    cattleNo = item.find("cattleNo")    #cattleNo 검색
                    lsTypeNm = item.find("lsTypeNm")    #lsTypeNm 검색
                    sexNm = item.find("sexNm")          #sexNm 검색
                    
                    self.info_object_date.setText(birthYmd.text)
                    self.info_object_number.setText(cattleNo.text)
                    self.info_object_type.setText(lsTypeNm.text)
                    self.info_object_sex.setText(sexNm.text)
                    
                    self.info_butcher_sex.setText(sexNm.text)
                
                
                if (item.find("infoType")).text == "2" :
                    farmAddr = item.find("farmAddr")    		#birthYmd 검색
                    farmerNm = item.find("farmerNm") 		#cattleNo 검색
                    regType = item.find("regType")
                    regYmd = item.find("regYmd")
                    
                    if moveCnt == 1:
                        self.info_move_cnt_1.setText(str(moveCnt))
                        self.info_move_owner_1.setText(farmerNm.text)
                        self.info_move_move_1.setText(regType.text)
                        self.info_move_date_1.setText(regYmd.text)
                        self.info_move_location_1.setText(farmAddr.text)
                    
                    if moveCnt == 2:
                        self.info_move_cnt_2.setText(str(moveCnt))
                        self.info_move_owner_2.setText(farmerNm.text)
                        self.info_move_move_2.setText(regType.text)
                        self.info_move_date_2.setText(regYmd.text)
                        self.info_move_location_2.setText(farmAddr.text)
                    
                    if moveCnt == 3:
                        self.info_move_cnt_3.setText(str(moveCnt))
                        self.info_move_owner_3.setText(farmerNm.text)
                        self.info_move_move_3.setText(regType.text)
                        self.info_move_date_3.setText(regYmd.text)
                        self.info_move_location_3.setText(farmAddr.text)
                        
                    if moveCnt == 4:
                        self.info_move_cnt_4.setText(str(moveCnt))
                        self.info_move_owner_4.setText(farmerNm.text)
                        self.info_move_move_4.setText(regType.text)
                        self.info_move_date_4.setText(regYmd.text)
                        self.info_move_location_4.setText(farmAddr.text)
                        
                    if moveCnt == 5:
                        self.info_move_cnt_5.setText(str(moveCnt))
                        self.info_move_owner_5.setText(farmerNm.text)
                        self.info_move_move_5.setText(regType.text)
                        self.info_move_date_5.setText(regYmd.text)
                        self.info_move_location_5.setText(farmAddr.text)
                        
                    if moveCnt == 6:
                        self.info_move_cnt_6.setText(str(moveCnt))
                        self.info_move_owner_6.setText(farmerNm.text)
                        self.info_move_move_6.setText(regType.text)
                        self.info_move_date_6.setText(regYmd.text)
                        self.info_move_location_6.setText(farmAddr.text)
                    
                    moveCnt += 1;
                        
                
                if (item.find("infoType")).text == "3" :
                    butcheryYmd = item.find("butcheryYmd")              #butcheryYmd 검색
                    butcheryPlaceNm = item.find("butcheryPlaceNm")      #butcheryPlaceNm 검색
                    inspectPassYn = item.find("inspectPassYn")          #inspectPassYn 검색
        
                    self.info_butcher_date.setText(butcheryYmd.text)
                    self.info_butcher_location.setText(butcheryPlaceNm.text)
                    self.info_butcher_grade.setText(inspectPassYn.text)
                    
                    
                if (item.find("infoType")).text == "4" :
                    processPlaceNm = item.find("processPlaceNm")         #processPlaceNm 검색
        
                    self.info_butcher_factory.setText(processPlaceNm.text)
    
