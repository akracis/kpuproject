# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
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


    def send(self):
        import http.client
        import mysmtplib
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        from xml.etree import ElementTree

        #global value
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        #get data from e-mail gui
        number = self.input_email_number.toPlainText()     # 객체번호
        sender = self.input_email_sender.toPlainText()     # 보내는 사람 email 주소.
        password = self.input_email_password.toPlainText() # 패스워드.
        target = self.input_email_target.toPlainText()     # 받는 사람 email 주소.
        
        #get xml from object number
        key = "VZwF3B6OId9MZtOCoLO8pS5FCjIXGQj3MYkPenIahW0vcGzgC%2Bb8rJHcYoDRPk%2Fc9dsbldkOhJi0mBewN4UBMg%3D%3D"
        conn = http.client.HTTPConnection("data.ekape.or.kr")
        conn.request("GET", "/openapi-data/service/user/animalTrace/traceNoSearch?ServiceKey=" + key + "&traceNo=" + number) #서버에 GET 요청 

        req = conn.getresponse()    #openAPI 서버에서 보내온 요청을 받아옴
        cLen = bytearray(req.getheader("Content-Length"), 'utf-8')    #가져온 데이터 길이

        if int(req.status) == 200 :
            strXml = (req.read().decode('utf-8'))    #요청이 성공이면 book 정보 추출
            strList = ""
            tree = ElementTree.fromstring(strXml)
            
            itemElements = tree.getiterator("item")
            for item in itemElements:
                if (item.find("infoType")).text == "1" :
                    birthYmd = item.find("birthYmd")    #birthYmd 검색
                    cattleNo = item.find("cattleNo")    #cattleNo 검색
                    lsTypeNm = item.find("lsTypeNm")    #lsTypeNm 검색
                    sexNm = item.find("sexNm")          #sexNm 검색
        
                    strList += (str(birthYmd.text) + "\t" + str(cattleNo.text) + "\t" + str(lsTypeNm.text) + "\t" + str(sexNm.text) + "\n")
                
                if (item.find("infoType")).text == "2" :
                    farmAddr = item.find("farmAddr")    		#birthYmd 검색
                    farmerNm = item.find("farmerNm") 		#cattleNo 검색
                    regType = item.find("regType")
                    regYmd = item.find("regYmd")
        
                    strList += (str(farmAddr.text) + "\t" + str(farmerNm.text) + "\t" + str(regType.text) + "\t"+ str(regYmd.text) + "\n")
                
                if (item.find("infoType")).text == "3" :
                    butcheryYmd = item.find("butcheryYmd")              #butcheryYmd 검색
                    butcheryPlaceNm = item.find("butcheryPlaceNm")      #butcheryPlaceNm 검색
                    inspectPassYn = item.find("inspectPassYn")          #inspectPassYn 검색
                    
                    strList += (str(butcheryYmd.text) + "\t" + str(butcheryPlaceNm.text) + "\t" + str(inspectPassYn.text) + "\t")
                    
                if (item.find("infoType")).text == "4" :
                    processPlaceNm = item.find("processPlaceNm")         #processPlaceNm 검색
                    
                    strList += (str(processPlaceNm.text) + "\n")
        
        
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "Animal Husbandry Management xml - " + number
        msg['From'] = sender
        msg['To'] = target

        # MIME 문서를 생성합니다.
        htmlPart = MIMEText(str(strList), 'html', _charset = 'UTF-8')

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(htmlPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender, password)
        s.sendmail(sender, [target], msg.as_string())
        s.close()
    
    
    def save(self):
        import file
        import http.client
        from xml.etree import ElementTree

        
        number = self.input_C_number.toPlainText() 
        
        #get xml from object number
        key = "VZwF3B6OId9MZtOCoLO8pS5FCjIXGQj3MYkPenIahW0vcGzgC%2Bb8rJHcYoDRPk%2Fc9dsbldkOhJi0mBewN4UBMg%3D%3D"
        conn = http.client.HTTPConnection("data.ekape.or.kr")
        conn.request("GET", "/openapi-data/service/user/animalTrace/traceNoSearch?ServiceKey=" + key + "&traceNo=" + number) #서버에 GET 요청 

        req = conn.getresponse()    #openAPI 서버에서 보내온 요청을 받아옴
        cLen = bytearray(req.getheader("Content-Length"), 'utf-8')    #가져온 데이터 길이

        if int(req.status) == 200 :
            strXml = (req.read().decode('utf-8'))    #요청이 성공이면 book 정보 추출
            strList = ""
            tree = ElementTree.fromstring(strXml)
            
            itemElements = tree.getiterator("item")
            for item in itemElements:
                if (item.find("infoType")).text == "1" :
                    birthYmd = item.find("birthYmd")    #birthYmd 검색
                    cattleNo = item.find("cattleNo")    #cattleNo 검색
                    lsTypeNm = item.find("lsTypeNm")    #lsTypeNm 검색
                    sexNm = item.find("sexNm")          #sexNm 검색
        
                    strList += (str(birthYmd.text) + "\t" + str(cattleNo.text) + "\t" + str(lsTypeNm.text) + "\t" + str(sexNm.text) + "\n")
                
                if (item.find("infoType")).text == "2" :
                    farmAddr = item.find("farmAddr")    		#birthYmd 검색
                    farmerNm = item.find("farmerNm") 		#cattleNo 검색
                    regType = item.find("regType")
                    regYmd = item.find("regYmd")
        
                    strList += (str(farmAddr.text) + "\t" + str(farmerNm.text) + "\t" + str(regType.text) + "\t"+ str(regYmd.text) + "\n")
                
                if (item.find("infoType")).text == "3" :
                    butcheryYmd = item.find("butcheryYmd")              #butcheryYmd 검색
                    butcheryPlaceNm = item.find("butcheryPlaceNm")      #butcheryPlaceNm 검색
                    inspectPassYn = item.find("inspectPassYn")          #inspectPassYn 검색
                    
                    strList += (str(butcheryYmd.text) + "\t" + str(butcheryPlaceNm.text) + "\t" + str(inspectPassYn.text) + "\t")
                    
                if (item.find("infoType")).text == "4" :
                    processPlaceNm = item.find("processPlaceNm")         #processPlaceNm 검색
                    
                    strList += (str(processPlaceNm.text) + "\n")
                    
            file.save(strList)
        

