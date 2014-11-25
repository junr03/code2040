# This file contains the code necessary to perform an API
# request to the code2040 API to obtain a unique token, given
# my email is jnino1@jhu.edu and my repository lives
# in https://github.com/junr03/code2040
require 'http'

module Api
	def self.token
		r = HTTP.post "http://challenge.code2040.org/api/register", :json => {:email => 'jnino1@jhu.edu', :github => 'https://github.com/junr03/code2040'}
		data = JSON.parse(r.to_s)
		data['result']
	end
end