import requests
import base64
import json

class detection:
    def __init__(self):
        pass

    def licence_plate(self,fname):
        with open(fname, "rb") as image_file:
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
        data_str = r.json().get('results')
        d = data_str[0]
        return(d)
