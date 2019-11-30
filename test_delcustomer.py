import json
import unittest
from customer import Customer
#from delhander import DelHandler
from addhandler import AddHandler

customers = Customer()
class addTest(unittest.TestCase):
    def test_del(self):
        result1 = customers.add_customer('alexa', 'New jersey')
        result2 = customers.del_customer('alexa')
        assert result2
