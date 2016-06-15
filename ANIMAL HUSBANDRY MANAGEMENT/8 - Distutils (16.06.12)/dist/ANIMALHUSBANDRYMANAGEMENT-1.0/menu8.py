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
        Dialog.resize(331, 471)
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
        self.input_C_number.setGeometry(QtCore.QRect(110, 210, 211, 31))
        self.input_C_number.setObjectName(_fromUtf8("input_C_number"))
        self.exp_C_number = QtGui.QTextBrowser(Dialog)
        self.exp_C_number.setGeometry(QtCore.QRect(10, 210, 101, 31))
        self.exp_C_number.setObjectName(_fromUtf8("exp_C_number"))
        self.btn_C_save = QtGui.QPushButton(Dialog)
        self.btn_C_save.setGeometry(QtCore.QRect(10, 250, 311, 31))
        self.btn_C_save.setObjectName(_fromUtf8("btn_C_save"))
        self.input_DB_number = QtGui.QPlainTextEdit(Dialog)
        self.input_DB_number.setGeometry(QtCore.QRect(110, 300, 211, 31))
        self.input_DB_number.setObjectName(_fromUtf8("input_DB_number"))
        self.exp_DB_number = QtGui.QTextBrowser(Dialog)
        self.exp_DB_number.setGeometry(QtCore.QRect(10, 300, 101, 31))
        self.exp_DB_number.setObjectName(_fromUtf8("exp_DB_number"))
        self.btn_DB_insert = QtGui.QPushButton(Dialog)
        self.btn_DB_insert.setGeometry(QtCore.QRect(10, 340, 91, 31))
        self.btn_DB_insert.setObjectName(_fromUtf8("btn_DB_insert"))
        self.btn_DB_search = QtGui.QPushButton(Dialog)
        self.btn_DB_search.setGeometry(QtCore.QRect(120, 340, 91, 31))
        self.btn_DB_search.setObjectName(_fromUtf8("btn_DB_search"))
        self.btn_DB_delete = QtGui.QPushButton(Dialog)
        self.btn_DB_delete.setGeometry(QtCore.QRect(230, 340, 91, 31))
        self.btn_DB_delete.setObjectName(_fromUtf8("btn_DB_delete"))
        self.info_DB_status = QtGui.QTextBrowser(Dialog)
        self.info_DB_status.setGeometry(QtCore.QRect(10, 380, 311, 81))
        self.info_DB_status.setObjectName(_fromUtf8("info_DB_status"))
        self.line_1 = QtGui.QFrame(Dialog)
        self.line_1.setGeometry(QtCore.QRect(0, 185, 331, 31))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 331, 21))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "메뉴", None))
        self.btn_email_send.setText(_translate("Dialog", "메일전송", None))
        self.exp_email_number.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">객체식별번호</p></body></html>", None))
        self.exp_email_sender.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E-Mail(Gmail)</p></body></html>", None))
        self.exp_email_password.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">패스워드</p></body></html>", None))
        self.exp_email_target.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">받는 사람</p></body></html>", None))
        self.exp_C_number.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">객체식별번호</p></body></html>", None))
        self.btn_C_save.setText(_translate("Dialog", "파일 저장", None))
        self.exp_DB_number.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">객체식별번호</p></body></html>", None))
        self.btn_DB_insert.setText(_translate("Dialog", "삽입", None))
        self.btn_DB_search.setText(_translate("Dialog", "검색", None))
        self.btn_DB_delete.setText(_translate("Dialog", "삭제", None))


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
            
    
    def insert(self):
        import sqlite3
        import http.client
        from xml.etree import ElementTree
        
        number = self.input_DB_number.toPlainText() 
        con = sqlite3.connect("Husbandry.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS MainList(Number text, Birth text, Type text, Sex text);")
        cur.execute("CREATE TABLE IF NOT EXISTS MoveList(Number text, Address text, Farmer text, Registeration text, Date text);")
        
        #get xml from object number
        key = "VZwF3B6OId9MZtOCoLO8pS5FCjIXGQj3MYkPenIahW0vcGzgC%2Bb8rJHcYoDRPk%2Fc9dsbldkOhJi0mBewN4UBMg%3D%3D"
        conn = http.client.HTTPConnection("data.ekape.or.kr")
        conn.request("GET", "/openapi-data/service/user/animalTrace/traceNoSearch?ServiceKey=" + key + "&traceNo=" + number) #서버에 GET 요청 

        req = conn.getresponse()    #openAPI 서버에서 보내온 요청을 받아옴
        cLen = bytearray(req.getheader("Content-Length"), 'utf-8')    #가져온 데이터 길이

        if int(req.status) == 200 :
            strXml = (req.read().decode('utf-8'))    #요청이 성공이면 book 정보 추출
            tree = ElementTree.fromstring(strXml)
            
            itemElements = tree.getiterator("item")
            for item in itemElements:
                if (item.find("infoType")).text == "1" :
                    birthYmd = item.find("birthYmd")
                    cattleNo = item.find("cattleNo")
                    lsTypeNm = item.find("lsTypeNm")
                    sexNm = item.find("sexNm")
        
                    cur.execute("INSERT INTO MainList VALUES('" + str(number) + "', '" + str(birthYmd.text) + "', '" + str(lsTypeNm.text) + "', '" + str(sexNm.text) + "');")
                
                if (item.find("infoType")).text == "2" :
                    farmAddr = item.find("farmAddr")
                    farmerNm = item.find("farmerNm")
                    regType = item.find("regType")
                    regYmd = item.find("regYmd")
        
                    cur.execute("INSERT INTO MoveList VALUES ('" + str(number) + "', '" + str(farmAddr.text) + "', '" + str(farmerNm.text) + "', '" + str(regType.text) + "', '" + str(regYmd.text) + "');")
        
        con.commit()
        con.close()
        
        
    def search(self):
        import sqlite3
        
        strStatus = ""
        number = self.input_DB_number.toPlainText() 
        
        con = sqlite3.connect("Husbandry.db")
        cur = con.cursor()
        
        cur.execute("SELECT * FROM MainList;")
        for row in cur:
            if row[0] == str(number):
                strStatus += (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n")
        
        cur.execute("SELECT * FROM MoveList;")
        for row in cur:
            if row[0] == str(number):
                strStatus += (str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\n")
        
        self.info_DB_status.setText(strStatus)
        
        con.commit()
        con.close()
        
        
    def delete(self):
        import sqlite3
        
        number = self.input_DB_number.toPlainText() 
        
        con = sqlite3.connect("Husbandry.db")
        cur = con.cursor()
        
        cur.execute("DELETE FROM MainList WHERE Number='" + str(number) + "';")
        cur.execute("DELETE FROM MoveList WHERE Number='" + str(number) + "';")
        
        con.commit()
        con.close()
        