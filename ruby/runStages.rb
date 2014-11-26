require './api'
require './stage1'
require './stage2'
require './stage3'
require './stage4'

token = API.token('jnino1@jhu.edu', 'https://github.com/junr03/code2040')

result1 = Stage1.runstage1(token)
print result1
result2 = Stage2.runstage2(token)
print result2
result3 = Stage3.runstage3(token)
print result3
result4 = Stage4.runstage4(token)
print result4