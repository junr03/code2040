import api
import json
import dateutil.parser
import datetime

def runstage4(token):
	# get data
	jsonData = api.communicate('time', {'token':token})

	# extract data
	current = jsonData['datestamp']
	interval = jsonData['interval']

	# get the datetime object
	current = dateutil.parser.parse(current)
	# this signifies 0 hours and interval seconds in the future
	later = current + datetime.timedelta(0,interval)
	# format the string
	formatedLater = later.isoformat()

	# validate result
	return api.communicate('validatetime', {'token':token, 'datestamp':formatedLater})