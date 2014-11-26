import api
import json

def runstage1(token):
	string = api.communicate('getstring', {'token':token})

	# reverse the string
	reversedString = string[::-1]

	# validate result
	return api.communicate('validatestring', {'token':token, 'string':reversedString})


