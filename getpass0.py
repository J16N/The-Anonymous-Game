import sys
import msvcrt
import colorama

colorama.init()

def getpass(s):
	print s,
	passwor = ''
	while True:
		x = msvcrt.getwch()
		if x == '\r':
			break
		elif x == '\b':
			print "\x1b[2K\x1b[1A"
			del passwor
			passwor = ''
			print s,
		else:
			sys.stdout.write('*')
			passwor +=x
	
	print "\n",
	return  passwor