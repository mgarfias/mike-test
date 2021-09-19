from app import app
from flask import request
import os
import base64


@app.route('/')
def main():
	redirect("/bytes")
	

@app.route('/bytes/<size>', methods=('GET', 'POST'))
def bytes(size):
	s = int(size)
	d = os.urandom(s)
	return base64.b64encode(d)