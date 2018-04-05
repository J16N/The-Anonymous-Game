'''   Copyright 2017 Jishan Bhattacharya

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

import time
import sys
import os
from colorama import init
import winsound
import matrix
import curses
from  printf import *

init()
os.system('mode con: cols=125 lines=55')

def Loading():	
	winsound.PlaySound(None, winsound.SND_PURGE)
	clear = lambda: os.system('cls')
	print "\x1b[47m"
	clear()
	
	def printfl(s):
		for c in s:
			sys.stdout.write('%s' % c)
			sys.stdout.flush()
			time.sleep(0.15)
	
	time.sleep(0.5)
	print "\n\x1b[35m\x1b[1m" * 20
	printf("\t\t\t\t\t\t\tTHE C-GAMES PRESENTS ")
	time.sleep(2)
	n = 1
	while n < 21:
		#printf("*")
		#n = n + 1
		printf("\b" * (n-(n-2)))
		printf(" ")
		n = n + 1
	time.sleep(0.5)
	
	print "\x1b[40m"
	clear()
	
	print "\t\t\t\t\t\t\t\x1b[32m\x1b[1mLOADING",
	
	t_end = time.time() + 15
	
	while time.time() < t_end:
		sys.stdout.write('\x1b[K')
		winsound.Beep(2600, 500)
		printfl("....\b\b\b\b")
	clear()
	matrix.main()
	time.sleep(3)
	clear()