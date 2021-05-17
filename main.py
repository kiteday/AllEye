import detect
import bus_number_detect
from gtts import gTTS

if __name__ == '__main__':
    result_path = './runs/detect/result/'

    '''
    이미지 import 해서 원본 사진의 path를 아래처럼
    source 변수에 return 해주세요
    source = <origin_img_path> 
    '''
    source = './data/bus/train/images/51.jpg'   # test

    detect.my_detect(source=source)

    '''
    detect후 ./runs/detect/result/ 아래에 
    아래와 같은 path로 저장돼요
    '''
    box_img_path = result_path + 'box_img.jpg'
    crop_img_path = result_path + 'crop_img.jpg'

    '''
    box_img_path로 image 출력 
    연우님 부탁드려요!
    '''

    # crop image가 존재하지 않으면 assertion 발생
    if crop_img_path:
        text = bus_number_detect.parse_image(crop_img_path)
    else:
        text = ''
        assert 'image가 존재하지 않습니다.'

    text_path = result_path + 'busnumber.mp3'
    txt = f'{text}번 버스가 진입중입니다.'

    tts = gTTS(text=txt, lang='ko')
    tts.save(text_path)

    '''
    text_path에 있는 mp3 파일로 음성 출력 버튼 만들어 주세요!
    '''