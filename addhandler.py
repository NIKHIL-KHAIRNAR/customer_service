import tornado.web
import customer
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
        self.customers = customers
        
    def get(self):
        name = self.get_argument('name')
        location = self.get_argument('location')
        result = self.customers.add_customer(name, location)
        self.write(result)
