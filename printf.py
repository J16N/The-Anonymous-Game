import time
import sys
import winsound

def printf(s):
	winsound.PlaySound('Sounds/text_audio.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
	for c in s:
		sys.stdout.write('%s' % c)
		sys.stdout.flush()
		time.sleep(0.0203)
	winsound.PlaySound(None, winsound.SND_PURGE)
	
def bgsound():	
	winsound.PlaySound('Sounds/audio0.wav', winsound.SND_ASYNC | winsound.SND_LOOP)