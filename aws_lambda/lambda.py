__author__ = 'amguerrero'
from main.LambdaHandler import LambdaHandler

def handler(event, context):
    hdl = LambdaHandler()
    return hdl.handle(event, context)

if __name__ == '__main__':
    print handler(None, None)