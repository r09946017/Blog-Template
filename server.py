#!/usr/bin/env python

"""server.py -- the main flask server module"""

import json
import random
import time

from base64 import b64decode
from functools import wraps

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flaskext.markdown import Markdown

from util import *

app = Flask(__name__, static_folder='static', static_url_path='')
Markdown(app)

lang = None

@app.route('/error/<msg>')
def error(msg):
	render = render_template('frame.html', lang = lang, 
		page = 'error.html', message = message)
	return make_response(render)

@app.route('/test')
def test():
	render = render_template('frame.html', lang = lang,
		page = 'test_markdown.html')
	return make_response(render)

@app.route('/')
def index():
	render = render_template('frame.html', lang = lang,
		page = 'main.html')
	return make_response(render)

@app.route('/about')
def about():
	render = render_template('frame.html', lang = lang,
		page = 'about.html')
	return make_response(render)

@app.route('/content')
def content():
	articles = get_content()
	render = render_template('frame.html', lang = lang,
                page = 'content.html', articles = articles)
	return make_response(render)

@app.route('/CTF_writeup/<year>/<name>')
def writeup(year, name):
	tasks = get_tasks(year, name)
	if not tasks:
		return redirect('/error/not_found')
	easy_tasks, medium_tasks, hard_tasks = [{"name": "Easy"}], [{"name": "Medium"}], [{"name": "Hard"}]
	for task in tasks:
		if task["Difficulty"] == "Easy":
			easy_tasks += [task]
		elif task["Difficulty"] == "Medium":
			medium_tasks += [task]
		else:
			hard_task += [task]
	grid = [easy_tasks, medium_tasks, hard_tasks]
	render = render_template('frame.html', lang = lang,
		page = 'tasks.html', grid = grid)
	return make_response(render)

if __name__ == '__main__':
	### Configuration
	config_str = open('config.json', 'rb').read()
	config = json.loads(config_str)
	
	lang_str = open(config['language_file'], 'rb').read()
	lang = json.loads(lang_str)
	lang = lang[config['language']]

	app.run(host=config['host'], port=config['port'],
		debug=config['debug'], threaded=True)







