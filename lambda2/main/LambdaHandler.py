from modules import requests
import json

class LambdaHandler():
    def __init__(self):
        self.requests = requests

    def handle(self, event, context):
        res = self.requests.post('https://httpbin.org/post', data=json.dumps(event), headers={'Authentication':'Bearer xDxDxDxD'})

        return res.json()