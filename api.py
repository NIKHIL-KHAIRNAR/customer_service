import tornado.ioloop
import tornado.web
from customer import Customer
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from searchhandler import SearchHandler

customers = Customer()
# This is is the main handler that class
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Customers Microservice v1.1")

#This will fork out to the specific handlers based on the request
def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcustomer", AddHandler, dict(customers = customers)),
        (r"/v1/delcustomer", DelHandler, dict(customers = customers)),
        (r"/v1/getcustomers", GetHandler, dict(customers = customers)),
         (r"/v1/searchcustomer", SearchHandler, dict(customers = customers)),
        ])
#This is the deamon that listens on port 8888 for http requests
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
