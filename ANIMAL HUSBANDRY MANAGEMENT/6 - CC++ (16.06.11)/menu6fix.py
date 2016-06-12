# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu6.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(331, 301)
        self.input_email_sender = QtGui.QPlainTextEdit(Dialog)
        self.input_email_sender.setGeometry(QtCore.QRect(110, 50, 211, 31))
        self.input_email_sender.setObjectName(_fromUtf8("input_email_sender"))
        self.input_email_password = QtGui.QPlainTextEdit(Dialog)
        self.input_email_password.setGeometry(QtCore.QRect(110, 80, 211, 31))
        self.input_email_password.setPlainText(_fromUtf8(""))
        self.input_email_password.setObjectName(_fromUtf8("input_email_password"))
        self.input_email_number = QtGui.QPlainTextEdit(Dialog)
        self.input_email_number.setGeometry(QtCore.QRect(110, 10, 211, 31))
        self.input_email_number.setObjectName(_fromUtf8("input_email_number"))
        self.btn_email_send = QtGui.QPushButton(Dialog)
        self.btn_email_send.setGeometry(QtCore.QRect(10, 160, 311, 31))
        self.btn_email_send.setObjectName(_fromUtf8("btn_email_send"))
        self.input_email_target = QtGui.QPlainTextEdit(Dialog)
        self.input_email_target.setGeometry(QtCore.QRect(110, 120, 211, 31))
        self.input_email_target.setObjectName(_fromUtf8("input_email_target"))
        self.exp_email_number = QtGui.QTextBrowser(Dialog)
        self.exp_email_number.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.exp_email_number.setObjectName(_fromUtf8("exp_email_number"))
        self.exp_email_sender = QtGui.QTextBrowser(Dialog)
        self.exp_email_sender.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.exp_email_sender.setObjectName(_fromUtf8("exp_email_sender"))
        self.exp_email_password = QtGui.QTextBrowser(Dialog)
        self.exp_email_password.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.exp_email_password.setObjectName(_fromUtf8("exp_email_password"))
        self.exp_email_target = QtGui.QTextBrowser(Dialog)
        self.exp_email_target.setGeometry(QtCore.QRect(10, 120, 101, 31))
        self.exp_email_target.setObjectName(_fromUtf8("exp_email_target"))
        self.input_C_number = QtGui.QPlainTextEdit(Dialog)
        self.input_C_number.setGeometry(QtCore.QRect(110, 220, 211, 31))
        self.input_C_number.setObjectName(_fromUtf8("input_C_number"))
        self.exp_C_number = QtGui.QTextBrowser(Dialog)
        self.exp_C_number.setGeometry(QtCore.QRect(10, 220, 101, 31))
        self.exp_C_number.setObjectName(_fromUtf8("exp_C_number"))
        self.btn_C_save = QtGui.QPushButton(Dialog)
        self.btn_C_save.setGeometry(QtCore.QRect(10, 260, 311, 31))
        self.btn_C_save.setObjectName(_fromUtf8("btn_C_save"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btn_email_send.setText(_translate("Dialog", "Send e-mail data from \'Object number\'", None))
        self.exp_email_number.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Object Number</p></body></html>", None))
        self.exp_email_sender.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E-mail(Gmail)</p></body></html>", None))
        self.exp_email_password.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Password</p></body></html>", None))
        self.exp_email_target.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Target E-mail</p></body></html>", None))
        self.exp_C_number.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Object Number</p></body></html>", None))
        self.btn_C_save.setText(_translate("Dialog", "Save data from \'Object number\'", None))

