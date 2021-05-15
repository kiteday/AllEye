import requests
import json

from pprint import pprint
import IPython.display as ipd

# Define Functions to Send Image to OCR Space API
# Please don't steal the API key, it's fine to use here but don't use it for other things (just get another)
def ocr_space_file(filename, overlay=False, api_key='5fbfe9786f88957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': 1
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

# request ocr
def parse_image(img_name):
    response = ocr_space_file(img_name)
    result = json.loads(response)
    # pprint(result)
    text = result["ParsedResults"][0]["ParsedText"]
    text = text.split("\n")[0]
    return text
