require 'http'
require './api'

module Stage3
	def self.runstage3(token)
		# get data
		data = API.communicate('prefix', {'token'=> token})

		# extract data
		words = data['array']
		prefix = data['prefix']

		# I LOVE the functional paradigms that ruby has borrowed
		matches = words.reject { |word| word.start_with? prefix }

		# validate result
		API.communicate('validateprefix', {'token'=> token, 'array'=> matches})
	end
end