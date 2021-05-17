# AllEye_UI
#### UI.ui 파일과 resources_rc.py 파일을 UI.inpyb 또는 UI.py 파일과 같은 디렉토리에 둬야합니다.
#### Image 폴더는 따로 다운로드할 필요가 없습니다.
---
## 0. UI Window
![UI_Window](https://user-images.githubusercontent.com/66766470/118524654-56326080-b779-11eb-9869-69e47f7d37e5.png)


----

### 1. 사용자 버스 번호 입력
- 따로 코드가 없습니다.

----

### 2. 버스 번호 등록
- 사용자가 입력한 버스 번호가 시스템에 저장됩니다.
```
  def input_busnumber(self)
```

----

### 3. 이미지 불러오기
- 사용자가 직접 이미지를 불러올 수 있습니다
- 불러온 이미지의 경로는 openimg에 저장됩니다.
```
  def import_image(self):
    openimg = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "./", "Images(*.png *.xpm *.jpg *.gif)")
```
- 이미지 불러오기 함수 안에 있는 Ouput이미지를 출력하는 함수는 코드를 합치면서 인자값과 위치를 바꿔야 할 것 같습니다.
```
  self.output_image(openimg)
```

----

### 4. Output 이미지 출력
- Yolo5를 사용하여 버스번호를 detect한 화면을 출력합니다.
- openimg[0]에는 이미지 경로가 저장돼 있어 다른 이미지 파일을 출력하고 싶으면 경로를 바꿔야합니다.
```
  def output_image(self, openimg):
     pixmap = QPixmap(openimg[0])
```
- 이미지 출력 함수 안에 있는 버스 번호 출력 함수는 코드를 합치면서 인자값과 위치를 바꿔야 할 것 같습니다.
```
  self.output_busnumber(5626)
```

----

### 5. 버스 번호 출력
- 도착한 버스의 번호를 출력해 줍니다.
```
  def output_busnumber(self, bus_number)
```

----

### 6. 버스 번호 음성 재생
- 도착한 버스의 번호를 음성으로 재생해 줍니다.
- 음성 파일은 .mp3 만 인식됩니다.
```
  def audio(self)
```

----
