
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
        return self.redirect("http://nightswatch.projets-bx1.fr/")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api', ApiHandler),
    ('/api/add', TestAddHandler),
    ('/api/list', TestListHandler),
], debug=True)
