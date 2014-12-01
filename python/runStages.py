import api
import stage1
import stage2
import stage3
import stage4

def main():
	print "Enter the email associated with your code2040 account:",
	email = raw_input()
	print "Enter the github repo associated with your code2040 account:",
	github = raw_input()
	token = api.token(email, github)

	print "RESULTS"
	result1 = stage1.runstage1(token)
	print result1
	result2 = stage2.runstage2(token)
	print result2
	result3 = stage3.runstage3(token)
	print result3
	result4 = stage4.runstage4(token)
	print result4

if __name__ == "__main__":
	main()