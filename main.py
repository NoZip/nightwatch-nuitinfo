
import os
import jinja2

import webapp2
from api.handler import ApiHandler
from api.test_handler import TestAddHandler, TestListHandler

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + 'templates/')
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class FormHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('form.html')
        self.response.out.write()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler,
    ('/api', ApiHandler),
    ('/api/add', TestAddHandler),
    ('/api/list', TestListHandler),
], debug=True)
