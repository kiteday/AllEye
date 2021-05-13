# AllEye_UI
---
### 사용 방법
#### UI.ui 파일을 UI.inpyb 또는 UI.py 파일과 같은 디렉토리에 둬야합니다.
- 이미지 불러오기
```
  사용자가 직접 불러온 이미지의 경로가 openimg에 저장됩니다.
  Yolo5에서 테스트할 이미지를 불러와야 할 때 경로대신 openimg[0] 을 입력하면 될 거라고 생각합니다..
``````
- 이미지 출력
```
  dep image_push 안의
  pixmap = QPixmap("SavedImage.jpg") 
  이미지 경로를 YOLO5를 통해 나온 결과 이미지의 경로로 바꾸면 UI화면에 출력이 됩니다. 
``````
---
### 계획
- UI 디자인
- 음성 재생 버튼 만들기
