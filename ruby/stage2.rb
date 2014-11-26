require 'http'
require './api'

module Stage2
	def self.runstage2(token)
		data = API.communicate('haystack', {"token" => token})

		haystack = data['haystack']
		needle = data['needle']

		index = haystack.index(needle)
		API.communicate('validateneedle', {'token' => token, 'needle' => index})
	end
end