from printf import *
import colorama
import os

colorama.init()

def gameover():
	time.sleep(1)
	clear = lambda: os.system('cls')
	clear()

	print "\x1b[32m\x1b[1m\n"  * 27
	printf("\t\t\t\t\t\t\tGAME OVER !")
	time.sleep(2)