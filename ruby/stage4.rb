require 'http'
require './api'
require 'time'

module Stage4
	def self.runstage4(token)
		# get data
		data = API.communicate('time', {'token' => token})

		# extract data
		current = data['datestamp']
		interval = data['interval']

		time = (Time.parse(current) + interval).iso8601

		# validate result
		API.communicate('validatetime', {'token' => token, 'datestamp' => time})
	end
end