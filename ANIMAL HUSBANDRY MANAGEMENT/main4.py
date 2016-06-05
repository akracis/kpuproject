# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from email4 import Ui_Dialog

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
        MainWindow.resize(520, 554)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.exp_program_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_program_title.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.exp_program_title.setObjectName(_fromUtf8("exp_program_title"))
        self.btn_search = QtGui.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(380, 10, 91, 31))
        self.btn_search.setObjectName(_fromUtf8("btn_search"))
        self.exp_object_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_title.setGeometry(QtCore.QRect(10, 40, 501, 31))
        self.exp_object_title.setObjectName(_fromUtf8("exp_object_title"))
        self.exp_object_number = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_number.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.exp_object_number.setObjectName(_fromUtf8("exp_object_number"))
        self.exp_object_type = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_type.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.exp_object_type.setObjectName(_fromUtf8("exp_object_type"))
        self.info_object_number = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_number.setGeometry(QtCore.QRect(100, 70, 161, 31))
        self.info_object_number.setObjectName(_fromUtf8("info_object_number"))
        self.info_object_type = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_type.setGeometry(QtCore.QRect(100, 100, 161, 31))
        self.info_object_type.setObjectName(_fromUtf8("info_object_type"))
        self.exp_object_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_date.setGeometry(QtCore.QRect(260, 70, 91, 31))
        self.exp_object_date.setObjectName(_fromUtf8("exp_object_date"))
        self.exp_object_sex = QtGui.QTextBrowser(self.centralwidget)
        self.exp_object_sex.setGeometry(QtCore.QRect(260, 100, 91, 31))
        self.exp_object_sex.setObjectName(_fromUtf8("exp_object_sex"))
        self.info_object_date = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_date.setGeometry(QtCore.QRect(350, 70, 161, 31))
        self.info_object_date.setObjectName(_fromUtf8("info_object_date"))
        self.info_object_sex = QtGui.QTextBrowser(self.centralwidget)
        self.info_object_sex.setGeometry(QtCore.QRect(350, 100, 161, 31))
        self.info_object_sex.setObjectName(_fromUtf8("info_object_sex"))
        self.input_number = QtGui.QPlainTextEdit(self.centralwidget)
        self.input_number.setGeometry(QtCore.QRect(180, 10, 201, 31))
        self.input_number.setObjectName(_fromUtf8("input_number"))
        self.exp_move_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_title.setGeometry(QtCore.QRect(10, 130, 501, 31))
        self.exp_move_title.setObjectName(_fromUtf8("exp_move_title"))
        self.exp_move_cnt = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_cnt.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.exp_move_cnt.setObjectName(_fromUtf8("exp_move_cnt"))
        self.exp_move_owner = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_owner.setGeometry(QtCore.QRect(40, 160, 71, 31))
        self.exp_move_owner.setObjectName(_fromUtf8("exp_move_owner"))
        self.exp_move_move = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_move.setGeometry(QtCore.QRect(110, 160, 81, 31))
        self.exp_move_move.setObjectName(_fromUtf8("exp_move_move"))
        self.exp_move_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_date.setGeometry(QtCore.QRect(190, 160, 91, 31))
        self.exp_move_date.setObjectName(_fromUtf8("exp_move_date"))
        self.exp_move_location = QtGui.QTextBrowser(self.centralwidget)
        self.exp_move_location.setGeometry(QtCore.QRect(280, 160, 231, 31))
        self.exp_move_location.setObjectName(_fromUtf8("exp_move_location"))
        self.exp_butcher_title = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_title.setGeometry(QtCore.QRect(10, 380, 501, 31))
        self.exp_butcher_title.setObjectName(_fromUtf8("exp_butcher_title"))
        self.exp_butcher_sex = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_sex.setGeometry(QtCore.QRect(370, 440, 61, 31))
        self.exp_butcher_sex.setObjectName(_fromUtf8("exp_butcher_sex"))
        self.info_butcher_sex = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_sex.setGeometry(QtCore.QRect(430, 440, 81, 31))
        self.info_butcher_sex.setObjectName(_fromUtf8("info_butcher_sex"))
        self.exp_butcher_grade = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_grade.setGeometry(QtCore.QRect(10, 440, 91, 31))
        self.exp_butcher_grade.setObjectName(_fromUtf8("exp_butcher_grade"))
        self.info_butcher_date = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_date.setGeometry(QtCore.QRect(430, 410, 81, 31))
        self.info_butcher_date.setObjectName(_fromUtf8("info_butcher_date"))
        self.exp_butcher_date = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_date.setGeometry(QtCore.QRect(370, 410, 61, 31))
        self.exp_butcher_date.setObjectName(_fromUtf8("exp_butcher_date"))
        self.exp_butcher_location = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_location.setGeometry(QtCore.QRect(10, 410, 91, 31))
        self.exp_butcher_location.setObjectName(_fromUtf8("exp_butcher_location"))
        self.info_butcher_location = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_location.setGeometry(QtCore.QRect(100, 410, 271, 31))
        self.info_butcher_location.setObjectName(_fromUtf8("info_butcher_location"))
        self.info_butcher_grade = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_grade.setGeometry(QtCore.QRect(100, 440, 271, 31))
        self.info_butcher_grade.setObjectName(_fromUtf8("info_butcher_grade"))
        self.info_butcher_factory = QtGui.QTextBrowser(self.centralwidget)
        self.info_butcher_factory.setGeometry(QtCore.QRect(100, 470, 411, 31))
        self.info_butcher_factory.setObjectName(_fromUtf8("info_butcher_factory"))
        self.exp_butcher_factory = QtGui.QTextBrowser(self.centralwidget)
        self.exp_butcher_factory.setGeometry(QtCore.QRect(10, 470, 91, 31))
        self.exp_butcher_factory.setObjectName(_fromUtf8("exp_butcher_factory"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 190, 501, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 189))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalScrollBar = QtGui.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(481, 0, 16, 191))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_mail = QtGui.QPushButton(self.centralwidget)
        self.btn_mail.setGeometry(QtCore.QRect(470, 10, 41, 31))
        self.btn_mail.setObjectName(_fromUtf8("btn_mail"))
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
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_butcher_grade.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.info_butcher_factory.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.exp_butcher_factory.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">가공장</p></body></html>", None))
        self.btn_mail.setText(_translate("MainWindow", "Mail", None))
        
        
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
        
                    print(str(birthYmd.text) + "\t" + str(cattleNo.text) + "\t" + str(lsTypeNm.text) + "\t" + str(sexNm.text))
                    
                    self.info_object_date.setText(birthYmd.text)
                    self.info_object_number.setText(cattleNo.text)
                    self.info_object_type.setText(lsTypeNm.text)
                    self.info_object_sex.setText(sexNm.text)
                    
                    self.info_butcher_sex.setText(sexNm.text)
                
                if (item.find("infoType")).text == "3" :
                    butcheryYmd = item.find("butcheryYmd")              #butcheryYmd 검색
                    butcheryPlaceNm = item.find("butcheryPlaceNm")      #butcheryPlaceNm 검색
                    inspectPassYn = item.find("inspectPassYn")          #inspectPassYn 검색
        
                    print(str(butcheryYmd.text) + "\t" + str(butcheryPlaceNm.text) + "\t" + str(inspectPassYn.text))
                    
                    self.info_butcher_date.setText(butcheryYmd.text)
                    self.info_butcher_location.setText(butcheryPlaceNm.text)
                    self.info_butcher_grade.setText(inspectPassYn.text)
                    
                if (item.find("infoType")).text == "4" :
                    processPlaceNm = item.find("processPlaceNm")         #processPlaceNm 검색
        
                    print(str(processPlaceNm.text))
                    
                    self.info_butcher_factory.setText(processPlaceNm.text)
    
