import register
import requests
import json
import dateutil.parser
import datetime

# Obtain my token
token = register.token()

# Create the requesting JSON file
data = {'token':token}

# get the dictionary
r = requests.post('http://challenge.code2040.org/api/time', data=json.dumps(data))
jsonData = r.json()
current = jsonData['result']['datestamp']
interval = jsonData['result']['interval']

# get the datetime object
current = dateutil.parser.parse(current)
# this signifies 0 hours and interval seconds in the future
later = current + datetime.timedelta(0,interval)
# format the string
formatedLater = later.isoformat()

# Create the verifying JSON file
data = {'token':token, 'datestamp':formatedLater}

# verify the index
r = requests.post('http://challenge.code2040.org/api/validatetime', data=json.dumps(data))
jsonData = r.json()
result = jsonData['result']