from app import app
from flask import request, redirect, Response
import os
import base64


@app.route('/')
def main():
	return( "Hi")
	
# I'd check the requested size param here, but the request doesn't get here without the 
# param appended.  The requested path to this isn't really a good idea, as a REST app 
# should return the same result with the same path.  A better choice would be to pass
# the requested size in as a param like /bytes?size=20
@app.route('/bytes/<size>', methods=('GET', 'POST'))
def bytes(size):
	try: 
		s = int(size)
	except ValueError:
		return Response("Invalid argument", status=400)
	d = os.urandom(s)
	return base64.b64encode(d)
	