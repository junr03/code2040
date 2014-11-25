# For this file just need to change the requests to the ruby module


import api
import requests
import json

# obtain token once
token = api.token()

# get data
jsonData = api.getData('haystack', {'token':token})

# extract data
haystack = jsonData['haystack']
needle = jsonData['needle']

# get index, according to instructions it is always there, but lets
# just add some basic error handling
try:
	index = haystack.index(needle)
except:
	print "The needle is not in the haystack"

# validate result
api.verifyResult('validateneedle', {'token':token, 'needle':index})


