import requests
import base64

with open("test2.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

params = (
    ('secret_key', 'sk_5480c2d505db6bc27544dc20'),
    ('recognize_vehicle', '0'),
    ('country', 'in'),
    ('return_image', '0'),
    ('topn', '10'),
)

data = encoded_string

r = requests.post('https://api.openalpr.com/v2/recognize_bytes', headers=headers, params=params, data=data)
print(r.text)
print('--------')
a = r.json()
print(a)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.post('https://api.openalpr.com/v2/recognize_bytes?secret_key=sk_5480c2d505db6bc27544dc20&recognize_vehicle=0&country=in&return_image=0&topn=10', headers=headers, data=data)
