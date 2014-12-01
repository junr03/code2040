require './api'
require './stage1'
require './stage2'
require './stage3'
require './stage4'

puts "Enter the email associated with your code2040 account:",
email = gets.chomp
puts "Enter the github repo associated with your code2040 account:",
github = gets.chomp

token = API.token('jnino1@jhu.edu', 'https://github.com/junr03/code2040')

puts "RESULTS:"
result1 = Stage1.runstage1(token)
puts result1
result2 = Stage2.runstage2(token)
puts result2
result3 = Stage3.runstage3(token)
puts result3
result4 = Stage4.runstage4(token)
puts result4