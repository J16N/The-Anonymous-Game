import colorama
import time
from printf import *
import os
import winsound

colorama.init()

def credits():

	clear = lambda: os.system('cls')
	clear()
	
	winsound.PlaySound('Sounds/credits.wav', winsound.SND_ASYNC)
	
	credits = '''\t\t\t\t\t\x1b[1m\x1b[33mThe C-G@MES presents THE ANONYMOUS
		\n\n\t\t\t\t\t\x1b[36mDeveloped by Jishan Bhattacharya
		\n\t\t\t\t\tMusic Directed by Subhrangshu Adhikary
		\n\t\t\t\t\tArt designed and edited by Arijit Roy'''
		
	print "\n" * 55
	print credits

	t_end = time.time() + 11

	while time.time() < t_end:
		print '\n'
		time.sleep(0.5)
		
	time.sleep(2)
	clear()

	print "\x1b[32m\n"  * 27
	printf("\t\t\t\tCONGRADULATIONS! YOU HAVE SUCCESSFULLY COMPLETED THE GAME.")
	time.sleep(2)