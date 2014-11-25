import api
import json

def runstage3(token):
	# get data
	jsonData = api.getData('prefix', {'token':token})

	# extract data
	array = jsonData['array']
	prefix = jsonData['prefix']

	# For a problem like this I like ruby's nice array methods like 'reject' and collect
	# so I will 'simulate them'
	matches = [match for match in array if not match.startswith(prefix)]

	# validate result
	return api.verifyResult('validateprefix', {'token':token, 'array':matches})