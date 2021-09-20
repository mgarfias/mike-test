from app import app
from flask import request, redirect, Response
import os
import base64


@app.route('/')
def main():
	return( "Hi")
	
@app.route('/bytes/<size>', methods=('GET', 'POST'))
def bytes(size):
	try: 
		s = int(size)
	except ValueError:
		return Response("Invalid argument", status=400)
	d = os.urandom(s)
	return base64.b64encode(d)
	