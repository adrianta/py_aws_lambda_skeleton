import unittest
import json
from mock import Mock
from lambda2.main.LambdaHandler import LambdaHandler

class LambdaHandler_test(unittest.TestCase):
    def setUp(self):
        print "setUp..."

    def tearDown(self):
        print "tearDown..."


    def test_Returns_Request(self):
        victim = LambdaHandler()
        res = Mock()
        res.json.return_value = json.loads(u'{"wARf" : "cool"}')
        victim.requests = Mock()
        victim.requests.post.return_value = res
        self.assertEquals(victim.handle({'message': 'This is JUST a test'}, None), {"wARf" : "cool"})

    def test_Returns_Request_2(self):
        victim = LambdaHandler()
        self.assertEquals(victim.handle({'message': 'This is JUST a test'}, None), {u'files': {}, u'origin': u'79.66.206.83', u'form': {}, u'url': u'https://httpbin.org/post', u'args': {}, u'headers': {u'Content-Length': u'34', u'Accept-Encoding': u'gzip, deflate', u'Host': u'httpbin.org', u'Accept': u'*/*', u'User-Agent': u'python-requests/2.9.1', u'Authentication': u'Bearer xDxDxDxD'}, u'json': {u'message': u'This is JUST a test'}, u'data': u'{"message": "This is JUST a test"}'})