#The main routing module
import webapp2
from views import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create', CreateHandler),
    ('/edit', EditHandler),
    ('/index2', Main2Handler),
    ('/create2', Create2Handler),
    ('/edit2', Edit2Handler)
], debug=True)
