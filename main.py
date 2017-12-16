from api.entity import Update
from config import WEBHOOK_URL
from utils.debug import debug
import handlers

from google.appengine.api import urlfetch
import webapp2

import os.path, pkgutil, importlib
import json


pkg_path = os.path.dirname(handlers.__file__)
handler_func_name = 'handler'  # name of the main function in handlers
handler_funcs = []

for _, module_name, _ in pkgutil.iter_modules([pkg_path]):
    m = importlib.import_module('handlers.' + module_name)
    handler_funcs.append(getattr(m, handler_func_name))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        update = Update(json.loads(self.request.body))
        handle(update)


def handle(update):
    for handler in handler_funcs:
        try:
            result = handler(update)
            if result:
                break
        except Exception as e:
            debug(handler.__module__ + '\n' + repr(e))


app = webapp2.WSGIApplication([(WEBHOOK_URL, WebhookHandler)], debug=True)

debug("I'm alive!")
