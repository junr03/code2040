import register
import requests
import json

# Obtain my token
token = register.token()

# Create the requesting JSON file
data = {'token':token}

# get the string
r = requests.post('http://challenge.code2040.org/api/getstring', data=json.dumps(data))
jsonData = r.json()
string = jsonData['result']

# reverse the string
reversedString = string[::-1]

# Create the verifying JSON file
data = {'token':token, 'string':reversedString}

# verify the reversed string
r = requests.post('http://challenge.code2040.org/api/validatestring', data=json.dumps(data))
jsonData = r.json()
result = jsonData['result']
