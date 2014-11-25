import api
import json

def runstage1(token):
	string = api.getData('getstring', {'token':token})

	# reverse the string
	reversedString = string[::-1]

	# validate result
	return api.verifyResult('validatestring', {'token':token, 'string':reversedString})


