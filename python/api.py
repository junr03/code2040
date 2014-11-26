# This file contains the code necessary to perform an API
# request to the code2040 API to obtain a unique token, given
# my email is jnino1@jhu.edu and my repository lives
# in https://github.com/junr03/code2040
import requests
import json

def token(email, github):
	data = {'email':email, 'github': github}
	r = requests.post('http://challenge.code2040.org/api/register', data=json.dumps(data))
	jsonData = r.json()
	return jsonData['result']

def communicate(path, data):

	# get the string
	r = requests.post('http://challenge.code2040.org/api/' + path, data=json.dumps(data))
	jsonData = r.json()
	return jsonData['result']