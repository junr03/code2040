import register
import requests
import json

# Obtain my token
token = register.token()

# Create the requesting JSON file
data = {'token':token}

# get the dictionary
r = requests.post('http://challenge.code2040.org/api/haystack', data=json.dumps(data))
jsonData = r.json()
haystack = jsonData['result']['haystack']
needle = jsonData['result']['needle']

# get index, according to instructions it is always there, but lets
# just add some basic error handling
try:
	index = haystack.index(needle)
except:
	print "The needle is not in the haystack"

# Create the verifying JSON file
data = {'token':token, 'needle':index}

# verify the index
r = requests.post('http://challenge.code2040.org/api/validateneedle', data=json.dumps(data))
jsonData = r.json()
result = jsonData['result']


