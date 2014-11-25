import api
import requests
import json

# obtain token once
token = api.token()

# get data
jsonData = api.getData('prefix', {'token':token})

# extract data
word = jsonData['array']
prefix = jsonData['prefix']

# I LOVE the functional paradigms that ruby has borrowed
matches = words.reject { |word| word.start_with? prefix }

# validate result
api.verifyResult('validateprefix', {'token':token, 'array':matches})