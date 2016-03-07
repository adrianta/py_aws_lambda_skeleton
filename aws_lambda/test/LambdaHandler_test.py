import unittest
from aws_lambda.main.LambdaHandler import LambdaHandler

class LambdaHandler_test(unittest.TestCase):
    def setUp(self):
        print "setUp..."

    def tearDown(self):
        print "tearDown..."

    def test_Returns_Request(self):
        victim = LambdaHandler()
        victim.handle(None, None)