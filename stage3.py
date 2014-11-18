import register
import requests
import json

# Obtain my token
token = register.token()

# Create the requesting JSON file
data = {'token':token}

# get the dictionary
r = requests.post('http://challenge.code2040.org/api/prefix', data=json.dumps(data))
jsonData = r.json()
array = jsonData['result']['array']
prefix = jsonData['result']['prefix']

# For a problem like this I like ruby's nice array methods like 'reject' and collect
# so I will 'simulate them'
matches = [match for match in array if not match.startswith(prefix)]

# Create the verifying JSON file
data = {'token':token, 'array':matches}

# verify the index
r = requests.post('http://challenge.code2040.org/api/validateprefix', data=json.dumps(data))
jsonData = r.json()
result = jsonData['result']