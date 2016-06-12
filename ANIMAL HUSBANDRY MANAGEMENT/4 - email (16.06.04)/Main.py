# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:09:46 2016

@author: M.K Jung Won Shin
@author: Abraham Kim
"""


#import
from xml.etree import ElementTree
import http.client


#function
def extractBookData(strXml):    #strXml은 OpenAPI 검색 결과 XML 문자열
    tree = ElementTree.fromstring(strXml)
    #Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")    #item 엘리먼트 리스트 추출
    print(itemElements)
    for item in itemElements:
        if (item.find("infoType")).text == "1" :
            birthYmd = item.find("birthYmd")    #birthYmd 검색
            cattleNo = item.find("cattleNo")    #cattleNo 검색
            lsTypeNm = item.find("lsTypeNm")    #lsTypeNm 검색
            sexNm = item.find("sexNm")          #sexNm 검색
        
            print(str(birthYmd.text) + "\t" + str(cattleNo.text) + "\t" + str(lsTypeNm.text) + "\t" + str(sexNm.text))
            
        elif (item.find("infoType")).text == "2" :
            farmAddr = item.find("farmAddr")    #farmAddr 검색
            farmerNm = item.find("farmerNm")    #farmerNm 검색
            regType = item.find("regType")      #regType 검색
            regYmd = item.find("regYmd")        #regYmd 검색
        
            print(str(farmAddr.text) + "\t" + str(farmerNm.text) + "\t" + str(regType.text) + "\t" + str(regYmd.text))


#main code
print("\n축산물 통합조회 서비스 (xml version)") 
key = "VZwF3B6OId9MZtOCoLO8pS5FCjIXGQj3MYkPenIahW0vcGzgC%2Bb8rJHcYoDRPk%2Fc9dsbldkOhJi0mBewN4UBMg%3D%3D"
traceNo = str(input("개체식별번호: "))
#traceNo = "002098106199"
#traceNo = "002059936536"

conn = http.client.HTTPConnection("data.ekape.or.kr")
conn.request("GET", "/openapi-data/service/user/animalTrace/traceNoSearch?ServiceKey=" + key + "&traceNo=" + traceNo) #서버에 GET 요청 

req = conn.getresponse()    #openAPI 서버에서 보내온 요청을 받아옴
print(req.status)
cLen = bytearray(req.getheader("Content-Length"), 'utf-8')    #가져온 데이터 길이

if int(req.status) == 200 :
    print("Animal data downloading complete!")
    extractBookData(req.read().decode('utf-8'))    #요청이 성공이면 book 정보 추출
else:
    print ("OpenAPI request has been failed! Please retry.")
        

