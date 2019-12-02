from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
RESULTS_DIR = 'jsons'
makedirs(RESULTS_DIR, exist_ok=True)

def make_image_data_list(image_filenames):
    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1
                    }]
            })
    return img_requests

def make_image_data(image_filenames):
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict }).encode()

def request_ocr(api_key, image_filenames):
    response = requests.post(ENDPOINT_URL,
                            data=make_image_data(image_filenames),
                            params={'key': api_key},
                            headers={'Content-Type': 'application/json'})
    return response

if __name__ == '__main__':
    api_key, *image_filenames = argv[1:]
    if not api_key or not image_filenames:
        print("""
	    適切にAPIキーとイメージファイルを指定してください。
  
        $ python cvapi.py api_key image.jpg""")
    else:
        response = request_ocr(api_key, image_filenames)
        if response.status_code != 200 or response.json().get('error'):
            print(response.text)
        else:
            for idx, resp in enumerate(response.json()['responses']):
                imgname = image_filenames[idx]
                jpath = join(RESULTS_DIR, basename(imgname) + '.json')
                print(resp['textAnnotations'][0]['description'])