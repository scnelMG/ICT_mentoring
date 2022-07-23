# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 02:58:05 2022

@author: Mgyu
"""
import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import datetime as dt
import time

form_mainclass = uic.loadUiType("C:/Users/Mgyu/PL/financial/qt_design/main_window.ui")[0]
form_secondclass = uic.loadUiType("C:/Users/Mgyu/PL/financial/qt_design/second_window.ui")[0]


class WindowClass(QMainWindow, form_mainclass) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.loadImageFromFile()


    def loadImageFromFile(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        pixmap_word = QPixmap("C:/Users/Mgyu/PL/financial/qt_design/word_cloud.png")
        self.label_word_cloud.setPixmap(QPixmap(pixmap_word))
        pixmap_top = QPixmap("C:/Users/Mgyu/PL/financial/qt_design/top.png")
        self.label_top.setPixmap(QPixmap(pixmap_top))
        self.show()
        
    def btn_main_to_second(self):
        self.hide()                     # 메인윈도우 숨김
        self.second = secondWindowClass()    
        self.second.exec()              # 두번째 창을 닫을 때 까지 기다림
        self.search_space.clear()
        self.show()                     # 두번째 창을 닫으면 다시 첫 번째 창이 보여짐
        
    def search_stock(self):
        global search_word
        search_word = self.search_space.text()
        print(search_word)

        return search_word

        
class secondWindowClass(QDialog,QWidget, form_secondclass):
    def __init__(self) :
        super(secondWindowClass, self).__init__()
        self.initUi()
        self.show()
        self.loadImageFromFile()

    def initUi(self):
        self.setupUi(self)
        self.label_stock_name.setText(f"{search_word} 주가 예측 결과")
        self.label_stock_name.setFont(QFont("", 13)) 
        self.label_stock_name.setAlignment(Qt.AlignCenter)
        self.label_graph_name.setText(f"{search_word} 주가 그래프 ")
        self.label_graph_name.setFont(QFont("", 9)) 
        self.text_result.setFont(QFont("", 11)) 
        self.text_result.append("다음 장에서의 예상 주가는 _____원입니다. ")
        self.label_today.setFont(QFont("", 9))
        self.label_today.setText(f"(오늘 : {self.get_today().date()} )")
            
    def loadImageFromFile(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        pixmap_stockGraph = QPixmap("C:/Users/Mgyu/PL/financial/qt_design/005930.png")
        self.label_stockGraph.setPixmap(QPixmap(pixmap_stockGraph))
        self.show()
        
    def btn_second_to_main(self):
        self.close()  

    def get_today(self):
        today = dt.datetime.now()
        return today
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 

    


