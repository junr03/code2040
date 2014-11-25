import api
import json

def runstage2(token):
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
	return api.verifyResult('validateneedle', {'token':token, 'needle':index})


