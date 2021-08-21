from api.entity import Update
from config import WEBHOOK_URL, DATABASE_URI
from utils.debug import debug
import handlers

from flask import Flask, request

import os.path, pkgutil, importlib
import json


app = Flask(__name__)

pkg_path = os.path.dirname(handlers.__file__)
handler_func_name = 'handler'
handler_funcs = []
for _, module_name, _ in pkgutil.iter_modules([pkg_path]):
	m = importlib.import_module('handlers.' + module_name)
	handler_funcs.append(getattr(m, handler_func_name))


@app.route(WEBHOOK_URL, methods=['POST'])
def post():
	update = Update(request.get_json())
	handle(update)
	return 'ok'


def handle(update):
	for handler in handler_funcs:
		try:
			result = handler(update)
			if result:
				break
		except Exception as e:
			debug(handler.__module__ + '\n' + repr(e))


debug("I'm alive!")
