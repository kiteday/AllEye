#!/usr/bin/env python
# coding: utf-8

#pip install pyqt5
#pip install pyqt5-tools
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

import bus_number_detect.bus_number_detect

Ui_Form = uic.loadUiType("UI.ui")[0] # ui 파일 불러오기

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("All Eye") # 파일 이름 설정
        self.ImportImg_btn.clicked.connect(self.image_push)
      
    def image_push(self):
        # 파일 열기로 이미지 불러오기
        global oepnimg
        openimg = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "./", "Images(*.png *.xpm *.jpg *.gif)") # img만 불러오기
        # openimg[0]에 이미지 경로 저장
        
        pixmap = QPixmap("SavedImage.jpg") # yolo5에서 저장한 이미지 경로 입력하여 불러오기
        
        # output 이미지 사이즈 변환
        w = int(self.Output_img.width())
        h = int(self.Output_img.height())
        if int(pixmap.width()) > int(pixmap.height()) :
            output = pixmap.scaledToWidth(w)
        else :
            output = pixmap.scaledToHeight(h)
            
        #Output 이미지 출력
        self.Output_img.setPixmap(output)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())






