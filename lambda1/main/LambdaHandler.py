from modules import requests
import json

class LambdaHandler():
    def handle(self, event, context):
        res = requests.post('https://httpbin.org/post', data=json.dumps(event), headers={'Authentication':'Bearer xDxDxDxD'})

        return res.json()