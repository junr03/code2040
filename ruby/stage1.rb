require 'http'
require './api'

module Stage1
	def self.runstage1(token)
		string = API.communicate('getstring', {"token" => token})
		# Reversing the string. With the (!) command
		# we san do it in place. That is s is now the reversed
		# string
		string.reverse!
		puts API.communicate('validatestring', {'token' => token, 'string' => string})
	end
end