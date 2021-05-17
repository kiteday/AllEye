#!/usr/bin/env python
# coding: utf-8
#pip install pyqt5
#pip install pyqt5-tools
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

import detect

# from pygame import mixer # 음성 재생

Ui_Form = uic.loadUiType("AllEye_UI.ui")[0] # ui 파일 불러오기

class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("All Eye") # 시스템 이름 설정
        self.ImportImg_btn.clicked.connect(self.import_image)
        self.Audio_btn.clicked.connect(self.audio)

    # 파일 열기로 이미지 불러오기
    def import_image(self):
        global oepnimg
        openimg = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "./", "Images(*.png *.xpm *.jpg *.gif)") # img만 불러오기
        # openimg[0]에 이미지 경로 저장

        self.output_image(openimg)

    # Output 이미지 출력
    def output_image(self, openimg):
        pixmap = QPixmap(openimg[0]) # yolo5에서 저장한 이미지 경로 입력하여 불러오기

        # output 이미지 사이즈 변환
        w = int(self.Output_img.width())
        h = int(self.Output_img.height())
        if int(pixmap.width()) > int(pixmap.height()) :
            output = pixmap.scaledToWidth(w)
        else :
            output = pixmap.scaledToHeight(h)

        self.Output_img.setPixmap(output)

        self.output_busnumber(5626) # 버스번호출력, ocr로 얻은 숫자 입력, 다른 곳으로 옮겨야함

    # 버스번호 출력
    def output_busnumber(self, bus_number):
        self.Output_BusNumber.setText(str(bus_number))

    # from gtts import gTTS
    # 오디오 재생 버튼
    def audio(self):
        pass
        # mp3 파일 밖에 못열음
        # mixer.init()
        # mixer.music.load("bus_number.mp3")
        # mixer.music.play()

    def detect(self):
        global openimg

        raw_img_path = openimg[0]
        detect.my_detect(source=raw_img_path, name='result')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
