import json
import unittest
from customer import Customer
#from delhander import DelHandler
from addhandler import AddHandler

customers = Customer()
class addTest(unittest.TestCase):
    def test_add(self):
        result = customers.add_customer('alex', 'london')
        assert result
