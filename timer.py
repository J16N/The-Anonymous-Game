import time
import winsound

def timer(times):
	winsound.PlaySound(None, winsound.SND_PURGE)
	
	t_end = time.time() + int(times)
	
	while time.time() < t_end:
		beep = winsound.Beep(1600, 500)
		winsound.PlaySound(beep, winsound.SND_ASYNC | winsound.SND_LOOP)
		
timer(10)