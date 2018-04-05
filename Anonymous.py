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

import Tkinter
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import ctypes
from LOADING import Loading
import time
from  printf import *
from sys import exit
from random import randint
from getpass0 import getpass
import os
from colorama import init
import pickle
import winsound
import matrix
from credits import credits
from gameover import gameover
import datetime

init()

ctypes.windll.kernel32.SetConsoleTitleA("THE ANONYMOUS")
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

def windows():
	bgsound()
	
	class Enduseragreement(object):
	
		def continu(self):
			self.root.destroy()
			time.sleep(1)
			ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5 )
			printf("\n\nYou will be soon prompted with a registration window to complete your profile.")
			ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
			bgsound()
			time.sleep(3)
			
	
		def __init__(self, root):
			self.root = root
			self.root.iconbitmap(default = 'Images/favicon.ico')
			self.root.title('End User Agreement')
			self.root.resizable(0,0)
		
			canvas = Canvas(self.root, height = 500, width = 500, relief = FLAT)
			img = ImageTk.PhotoImage(file = 'Images/img.jpg')
			image = canvas.create_image(250, 250, image = img)
		
			canvas.create_text(250, 30, font = ('NeuropolXRg-Regular', '25', 'bold'), text = 'Terms & Conditions', fill = 'red', activefill = 'green')
			a_text = """
			\nBefore continuing, you must accept terms and conditions. By accepting, you agree to join Anonymous hacking group. Our authority won't responsible if you encounter any trouble. You are always free to join here. You will be taking your own decision and if you wish you may quit now. But you cannot leave once you continue. \n\nRemember hacking is illegal. There's always a chance of getting caught or backtraced which results in severe punishment including lifetime imprisonment and death. \n\nYou are always welcome once you made your mind.
			"""
			canvas.create_text(250, 200, font = ('NeuropolXRg-Regular', '10'), text = a_text, fill = 'green', activefill = 'yellow', width = 500, justify = LEFT)
			canvas.pack()
	
			self.w = 500
			self.h = 500
			self.ws = self.root.winfo_screenwidth() 
			self.hs = self.root.winfo_screenheight()
			self.x = (self.ws/2) - (self.w/2)
			self.y = (self.hs/2) - (self.h/2)
			self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
		
			self.continueimg = ImageTk.PhotoImage(Image.open('Buttons/continue.jpg'))
			self.cont = Button(self.root, font = ('NeuropolXRg-Regular', '8'), image = self.continueimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = self.continu)
			self.cont.pack()
			self.cont.place(height = 50, width = 100, x = 380, y = 430)
			self.cont.config(state = DISABLED)
		
			def callback(*args):
				if self.checkvar.get() == 1:
					self.cont.config(state = NORMAL)
				else:
					self.cont.config(state = DISABLED)
		
			self.checkvar = IntVar()
			self.check = Checkbutton(self.root, font = ('NeuropolXRg-Regular', '6'), text = 'I ACCEPT', variable = self.checkvar, command = callback)
			self.check.place(x = 20, y = 400)
		
			self.root.mainloop()
		
	secondroot = Tk()
	useragreement = Enduseragreement(secondroot)


	class Registration(Label):
		def __init__(self, root, filename):
			im = Image.open(filename)
			seq =  []
			try:
				while 1:
					seq.append(im.copy())
					im.seek(len(seq)) # skip to next frame
			except EOFError:
				pass 

			try:
				self.delay = im.info['duration']
			except KeyError:
				self.delay = 100

			first = seq[0].convert('RGBA')
			self.frames = [ImageTk.PhotoImage(first)]
			Label.__init__(self, root, image=self.frames[0])
		
			temp = seq[0]
		
			for image in seq[1:]:
				temp.paste(image)
				frame = temp.convert('RGBA')
				self.frames.append(ImageTk.PhotoImage(frame))

			self.idx = 0

			self.cancel = self.after(self.delay, self.play)
		
			self.root = root
			self.root.iconbitmap(default = 'Images/favicon.ico')
			self.root.title('Registration')
			self.root.resizable(0,0)
			self.w = 500
			self.h = 500
			self.ws = self.root.winfo_screenwidth() 
			self.hs = self.root.winfo_screenheight()
			self.x = (self.ws/2) - (self.w/2)
			self.y = (self.hs/2) - (self.h/2)
			self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
			self.root.configure(background = 'grey')
			self.image = Image.open('Images/image1.jpg')
			self.photo_image = ImageTk.PhotoImage(self.image)
			self.label = Label(root, image = self.photo_image, bd = 0)
			self.label.pack(side = BOTTOM)
		
			self.name = Label(root, text = 'NAME', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.name.place(width = 50, height = 20, x = 40, y = 280)
			self.namevariable = StringVar()
			vcmd = (root.register(self.validname), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			self.user = Entry(root, width = 30, textvariable = self.namevariable, validate = "key", validatecommand = vcmd)
			self.user.place(x = 100, y = 280)
			self.user.focus()
		
			self.age = Label(root, text = 'AGE', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.age.place(width = 50, height = 20, x = 40, y = 320)
			vcmd = (root.register(self.validage), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			self.agevar = IntVar()
			self.userage = Spinbox(root, from_= 1, to = 100, justify = CENTER, width = 5, validate = "key", validatecommand = vcmd, wrap = True, textvariable = self.agevar)
			self.userage.place(x = 100, y = 320)
		
			self.sexvar = StringVar()
			self.sex = Label(root, text = 'SEX', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.sex.place(width = 50, height = 25, x = 40, y = 360)
			self.male = Radiobutton(root, text = 'Male',  variable = self.sexvar, value = 'Male')
			self.male.place(x = 100, y = 360)
			self.female = Radiobutton(root, text = 'Female', variable = self.sexvar,  value = 'Female')
			self.female.place(x = 165, y = 360)
			self.sexvar.set('Male')
		
			self.dob = Label(root, text = 'D.O.B', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.dob.place(width = 50, height = 20, x = 40, y = 400)
			self.daysvar = IntVar()
			vcmd = (root.register(self.validdays), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			self.days = Spinbox(root, from_ = 1, to = 31, justify = CENTER, width = 5, wrap = True, validate = 'key', validatecommand = vcmd, textvariable = self.daysvar)
			self.days.place(x = 100, y = 400)
			self.monthsvar = StringVar()
			self.months = Spinbox(root, values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'), justify = CENTER, width = 5,wrap = True, state = 'readonly', textvariable = self.monthsvar)
			self.months.place(x = 150, y = 400)
			self.yearsvar = IntVar()
			self.yearsvar.set('2017')
			self.year = Spinbox(root, from_ = 1970, to = 2050, justify = CENTER, width = 5, wrap = True, state = 'readonly', textvariable = self.yearsvar)
			self.year.place(x = 200, y = 400)
		
			self.username = Label(root, text = 'USERNAME', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.username.place(width = 80, height = 20, x = 40, y = 440)
			self.uservariable = StringVar()
			vcmd = (root.register(self.validusername), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			self.entry = Entry(root, width = 30, validate = "key", validatecommand = vcmd, textvariable = self.uservariable)
			self.entry.place(x = 130, y = 440)
		
			self.password = Label(root, text = 'PASSWORD', font = ('Times New Roman', '8', 'bold'), bg = 'black', fg = 'white')
			self.password.place(width = 80, height = 20, x = 40, y = 470)
			self.passvariable = StringVar()
			self.passentry = Entry(root, width = 30, show = '*', textvariable = self.passvariable)
			self.passentry.place(x = 130, y = 470)
			
			self.registerimg = ImageTk.PhotoImage(Image.open('Buttons/register.jpg'))
			self.register = Button(root, font = ('NeuropolXRg-Regular', '8'), image = self.registerimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = self.registration)
			self.register.pack()
			self.register.place(height = 50, width = 100, x = 390, y = 440)
		
		def validname(self, d, i, P, s, S, v, V, W):
			if S in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
				return True
			else:
				self.bell()
				return False
			
		def validage(self, d, i, P, s, S, v, V, W):
			if P in str(range(1, 101)):
				return True
			else:
				self.bell()
				return False
		
		def validdays(self, d, i, P, s, S, v, V, W):
			if P in str(range(1, 32)):
				return True
			else:
				self.bell()
				return False
			
		def validusername(self, d, i, P, s, S, v, V, W):
			if S in 'abcdefghijklmnopqrstuvwxyz1234567890':
				return True
			else:
				self.bell()
				return False
			
		def registration(self):
			if (self.daysvar.get() == 30  or self.daysvar.get() == 31)  and self.monthsvar.get() == 'Feb':
				tkMessageBox.showerror('ERROR', 'Selected day does not exist.')
				
			elif not ' ' in self.namevariable.get():
				tkMessageBox.showerror('ERROR', 'Full name is required')
			
			elif (datetime.datetime.now().year - self.yearsvar.get()) != self.agevar.get():
				tkMessageBox.showerror('ERROR', 'Incorrect D.O.B.')
				
			elif (self.yearsvar.get() % 4 != 0) and self.daysvar.get() == 29:
				tkMessageBox.showerror('ERROR', 'Selected day does not exist.')
			
			else:
				self.after_cancel(self.cancel)
				self.root.destroy()
				winsound.PlaySound(None, winsound.SND_PURGE)
				time.sleep(1)
				ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5)
				clear = lambda: os.system('cls')
				time.sleep(1)
				clear()
				printf('You are successfully registered to the team. \nAccording to the terms and conditions we won\'t be responsible if you encounter any trouble. \nAny illegal actions of yours which void our terms would be lethal for you. \nYou are given a terminal. Get there and explore yourself. \nYou will soon be contacted for a contract.')
				time.sleep(1)
				origame()
			
		def play(self):
			self.config(image=self.frames[self.idx])
			self.idx += 1
			if self.idx == len(self.frames):
				self.idx = 0
			self.cancel = self.after(self.delay, self.play)
		
		
	thirdroot = Tk()
	global user
	global register
	register = Registration(thirdroot, 'Images/tuhin.gif')
	user = register.uservariable.get()
	register.pack()
	thirdroot.mainloop()
	
def origame(): 
	
	print "\x1b[1m\x1b[32m"
	
	global register
	global user
	
	try:
		user = pickle.load(open('savegame0.dat', 'rb'))
	except:
		user = register.uservariable.get()
		
	
	class Scene(object):
		
		def enter(self):
			printf("This scene is not yet configured. Subclass it and implement enter().")
			exit(1)

	class Engine(object):
		
		level = [1]
		
		def __init__(self, scene_map):
			self.scene_map = scene_map
			
		def play(self):
			
			if  os.path.isfile('savegame2.dat') == False:
				current_scene = self.scene_map.opening_scene()
				last_scene = self.scene_map.next_scene('finished')
				death_scene = self.scene_map.next_scene('death')
			else:
				scene_name = pickle.load(open('savegame2.dat', 'rb'))
				current_scene = self.scene_map.next_scene(scene_name)
				last_scene = self.scene_map.next_scene('finished')
				death_scene = self.scene_map.next_scene('death')
			try:
				i = pickle.load(open('savegame1.dat', 'rb'))
			except:
				i = 1
				
			
			while current_scene != last_scene and current_scene != death_scene and i < 9:
				print '\n'
				print "-" * 125
				print "\t\t\t\t\tYOU HAVE SUCCESSFULLY REACHED LEVEL %d" % i
				print "-" * 125
				print '\n'
				pickle.dump(i, open("savegame1.dat", 'wb'))
				if os.path.isfile('savegame0.dat') == False:
					registers = register.uservariable.get()
					pickle.dump(registers, open("savegame0.dat", 'wb'))
				Engine.level.pop()
				Engine.level.append(i)
				next_scene_name = current_scene.enter()
				current_scene = self.scene_map.next_scene(next_scene_name)
				i += 1
			
			current_scene.enter()

				
	class Death(Scene):
		
		quips = [
			"\n\nProbably you failed to uninstall the 'Undelete', so the Anonymous group no longer rely on you.",
			"\n\nThe police couldn't figure out the password anymore and the data permanently got deleted leaving Esta escaped.",
			"\n\nThe security system triggered and you fell in a trap. \nLater the police came and arrested you.",
			"\n\nThe security system located you and you got caught and you spend the rest of your life behind the bars.",
			"\n\nYou lost control of your system and the hacker successfully hacked into your database. \nHe published the anonimity and you spend rest of life behind the bars.",
			"\n\nI have no longer access to your database. Please start a new game."
		]
		
		def enter(self):
			
			if Engine.level == [1]:
				printf(Death.quips[5])
				time.sleep(2)
				gameover()
				return 'death'
				
			elif Engine.level == [3]:
				printf(Death.quips[0])
				time.sleep(3)
				gameover()
				return 'death'
				
			elif Engine.level == [4]:
				printf(Death.quips[1])
				time.sleep(3)
				gameover()
				return 'death'
				
			elif Engine.level == [5]:
				printf(Death.quips[2])
				time.sleep(3)
				gameover()
				return 'death'
				
			elif Engine.level == [6]:
				printf(Death.quips[3])
				time.sleep(3)
				gameover()
				return 'death'
				
			else:
				print "\x1b[32m\x1b[1m"
				printf(Death.quips[4])
				time.sleep(3)
				gameover()
				return 'death'

	class Level1(Scene):
	
		def animate(self, a, b):
			winsound.PlaySound(None, winsound.SND_PURGE)
			def printf0(s):
				for c in s:
					sys.stdout.write('%s' % c)
					sys.stdout.flush()
					time.sleep(0.0203)
			
			print "\n" + a,
		
			t_end = time.time() + b
		
			while time.time() < t_end:
				sys.stdout.write('\x1b[K')
				printf0("......\b\b\b\b\b\b")
			printf0("\n")
			
		def enter(self):
			time.sleep(1)
			print "$Terminal:~ "
			time.sleep(2)
			Level1().animate("Checking your database", 5)
			time.sleep(0.5)
			print "\nChecking database complete."
			time.sleep(1)
			try:
				print "\n"
				printf("\t\t\t--------------------------------------------------------------")
				print  "\n\t\t\t|                        BIODATA                             |"
				printf("\t\t\t--------------------------------------------------------------")
				time.sleep(1)
				print  "\n\t\t\t|NAME                              %s                   " % register.namevariable.get()
				print  "\n\t\t\t|AGE                                    %d                 " % register.agevar.get()
				print  "\n\t\t\t|SEX                                   %s                 " % register.sexvar.get()
				print  "\n\t\t\t|DOB                                 %s %s %d              " % (register.daysvar.get(), register.monthsvar.get(), register.yearsvar.get())
				print  "\n\t\t\t|USERNAME                             %s                 " % register.uservariable.get()
				print  "\n\t\t\t|PASSWORD                             %s                 " % register.passvariable.get()
				printf("\t\t\t--------------------------------------------------------------")
				print  "\n"
				time.sleep(2)
			except:
				return 'death'
			printf('\nHi! I am TX001. I will be going to assist you. I am an AI installed on your terminal. \nI have been programmed to automate various tasks and also to keep a check on you. \nI get activated whenever there\'s a need to deliver an information. \nI may go through your mails and sometimes help you to understand the systems. \nI can also check your system\'s health. \nI run a priority scan whenever I encounter bugged system. \nYou may manually run the scan by \'runsc\' command. \nYou can get the available commands in your system by typing \'help\'. \nSo see you again once you successfully log into your terminal.\n\n')
			time.sleep(1)
			bgsound()
			while True:
				name = raw_input('Username: ')
				password = getpass('Password: ')
				
				if (name == register.uservariable.get()) and (password == register.passvariable.get()):
					winsound.PlaySound(None, winsound.SND_PURGE)
					time.sleep(1)
					print "\nChecking user..."
					time.sleep(1)
					print "User profile matched..."
					time.sleep(1)
					print "%s$Terminal:~ " % user
					time.sleep(1)
					return 'level2'
				else:
					print "\nInvalid username or password.\n"
					

					
	class Level2(Scene):
		def animateupdown(self, a):
			print a,
			x = ["%.3d" % i for i in range(101)]
			for i in x:
				time.sleep(0.2)
				print "[%s]%%\b\b\b\b\b\b\b" % i,
				sys.stdout.flush()
		
		def cmnds(self):
			print "\n"
			print "                       List of available commands"
			print "-----------------------------------------------------------------------------"
			print "|  Commands                                        Descriptions              "
			print "-----------------------------------------------------------------------------"
			print "|   ls                                      lists files and directories"
			print "|  ping <IP>                             Check the status of remote server"
			print "|  mail                                       Launch the mail program"
			print "| forward(-f) mail/SN <IP>                Forwards the given mail to given IP"
			print "| connect<IP>                              Connects to the remote server"
			print "| disconnect                                 Terminates the connection "
			print "|  runsc                                        Runs System Scan"
			print "|  help                                          Show this menu"
			print "|  TX001                                        Acitivates the AI"
			print "|upload(-u) <FileName> <IP>           Upload the current file to the given IP"
			print "|download(-d) <FileName> <IP>         Downloads the current file from given IP"
			print "\n"
			
		def enter(self):
			time.sleep(1)
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			time.sleep(2)
			print "Initializing local modules..."
			time.sleep(3)
			print "Initialization successful."
			time.sleep(1)
			print "Activating TX001..."
			time.sleep(4)
			print "TX001 successfully activated.\n"
			time.sleep(1)
			printf("\nSo you have successfully logged into your terminal. Now to view the available commands type 'help'. \nYou will find some commands are yet unavailable. You will get them in higher levels. \nAs you play and complete the missions you earn achievements and your level increases.\nAs you level up you get difficult systems to hack in. \nInitially during hacking I mask your IP to ensure that no traceback could locate you.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				
				if x == 'help':
					Level2().cmnds()
				elif x == 'ls':
					print "readme.txt"
					time.sleep(1)
					printf("To open any file simply enter its name.\n")
					bgsound()
				elif x == 'readme.txt':
					print "USR: john, PASS: bght234, IP: 451.001.47.123"
				elif x == 'ping':
					print "ping <IP> (Currently this command is unavailable)"
				elif x == 'mail':
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "   SN                        TITLE   "
					print "-------------------------------------"
					print "   01                       UN-NAMED "
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					else:
						print "To view the mail type the serial no."
				elif x == "connect 451.001.47.123":
					try:
						time.sleep(1)
						Level1().animate('Connecting', 7)
						print "\n"
						name = raw_input("Username: ")
						password = getpass("Password: ")
						if name == 'john' and password == 'bght234':
							time.sleep(1)
							print "\nLogin successful."
							print "\n"
							upload = False
							forward = False
							while True:
								y = raw_input('John$Terminal:~ ')
								if y == "help":
									print "\n"
									print "                       List of available commands"
									print "-----------------------------------------------------------------------------"
									print "|  Commands                                        Descriptions              "
									print "-----------------------------------------------------------------------------"
									print "|   ls                                      lists files and directories"
									print "|  ping <IP>                             Check the status of remote server"
									print "|  mail                                       Launch the mail program"
									print "| forward(-f) mail/SN <IP>                Forwards the given mail to given IP"
									print "| connect<IP>                              Connects to the remote server"
									print "| disconnect                                 Terminates the connection "
									print "|  help                                          Show this menu"
									print "|upload(-u) <FileName> <IP>           Upload the current file to the given IP"
									print "|download(-d) <FileName> <IP>         Downloads the current file from given IP"
									print "\n"
								elif y == "ls":
									print "note.txt"
								elif y == "note.txt":
									print "\nThere's my appointment in San Aldern at 8:34 P.M.\n"
								elif y == 'ping':
									print "ping <IP> (Currently this command is unavailable)"
								elif y == "mail":
									time.sleep(1)
									print "\nOpening mail..."
									time.sleep(3)
									print "--------------------------------------"
									print " SN                          TITLE    "
									print "--------------------------------------"
									print " 01                         DRUG-DEAL "
									print " 02                           ANNA    "
									print "--------------------------------------"
									print "\n"
									y = raw_input('John$Terminal/mail:~ ')
									if y == '01':
										print "\nYour deal has already been processed. The cost to be paid is $12034589. See you at 8:34 P.M."
										print "                                                                       ----------From Thomas"
									elif y == '02':
										print "\nHi honey! It's long sice we done up. Would you like to tea at my house at 6:45 P.M. ?\n"
									else:
										print "To view the mail type the serial no."
								elif y == "connect":
									print "Connect <IP>"
								elif y == "disconnect":
									time.sleep(2)
									Level1().animate("Disconnecting", 3)
									print "\nFailed to disconnect you at the moment."
								elif y == "forward" or y == '-f':
									print "Forward(-f) mail/SN <IP>"
								elif (y == "upload note.txt 202.145.785.45" or y == "-u note.txt 202.145.785.45") and forward == False:
									print "\n"
									Level2().animateupdown("Uploading...")
									print "File successfully uploaded.\n"
									upload = True
								elif (y == "forward mail/01 202.145.785.45" or y == "-f mail/01 202.145.785.45") and upload == True:
									Level1().animate("Forwarding", 3)
									print "\n"
									print "Mail successfully forwarded.\n"
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('John$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										print "\n"
										break
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...\n\n")
										break
								elif (y == "forward mail/01 202.145.785.45" or y == "-f mail/01 202.145.785.45") and upload == False:
									print "\n"
									Level1().animate("Forwarding", 3)
									print "\n"
									print "Mail successfully forwarded.\n"
									forward = True
								elif (y == "upload note.txt 202.145.785.45" or y == "-u note.txt 202.145.785.45") and forward == True:
									print "\n"
									Level2().animateupdown("Uploading...")
									print "\n"
									print "File successfully uploaded.\n"
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('\nJohn$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										print "\n"
										time.sleep(1)
										break
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...\n\n")
										time.sleep(1)
										break
								elif y == "download" or y == '-d':
									print "download(-d) <FileName> <IP>"
								elif y == "upload" or y == '-u':
									print "Upload(-u) <FileName> <IP>"
								elif y == '':
									y
								else:
									print "%r command does not exist." % y
							break
						else:
							print "Invalid username or password."
					except Exception:
						print "Failed to connect."
				elif x == 'connect':
					print "Connect <IP>"
				elif x == "disconnect":
					time.sleep(1)
					print "Invalid Request."
				elif x == 'igiveup':
					return 'level3'
				elif x == "runsc":
					time.sleep(1)
					Level2().animateupdown("Running System Scan. Please wait...")
					time.sleep(2)
					print "\n"
					print "System Health: Good"
					print "Status: Clean"
				elif x == "TX001":
					printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % user)
					bgsound()
				elif x == "upload readme.txt 202.145.785.45" or x == "-u readme.txt 202.145.785.45" or x == "upload":
					print "Currently uploading from your system is unavailable."
				elif x == "download" or x == '-d':
					print "Download(-d) <FileName> <IP>"
				elif x == "forward" or x == "-f":
					print "Forward mail/SN <IP>"
				elif x == '':
					x
				else:
					print "%r command does not exist." % x
					
			print '%s$Terminal:~ ' % user
			time.sleep(1)
			printf("\nYou have been successfully disconnected. Type 'mail' to see check your message.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level2().cmnds()
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "   SN                        TITLE   "
					print "-------------------------------------"
					print "   01                       UN-NAMED "
					print "   02                     UN-NAMED(2)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
						time.sleep(2)
						return 'level3'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					print "Your terminal is currently in upgrade. Commands are inaccessible."
					


	class Level3(Scene):
		
		def printinoneline(*s):
			for i in s:
				print '\r',
				time.sleep(2)
				print i,
				sys.stdout.flush()
				sys.stdout.write('\x1b[K')
		
		def enter(self):
			time.sleep(1)
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			print "\n"
			Level3().printinoneline("Getting required modules...", "Applying Updates...", "Activating TX001...", "Checking log files...", "Cleaning junk files...", "Junk files successfully cleaned.")
			printf("\nI found some junk files eating up the space. I cleaned them up. \nAs you level up you get some upgrades for your terminal \nand since I'm the part of your terminal so you get some upgrades for me too ;) \n")
			print "\n"
			Level2().animateupdown("Installing packages...")
			time.sleep(1)
			printf("\nThere's a new mail for you.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				
				if x == 'help':
					Level2().cmnds()
				elif x == 'ping':
					print "ping <IP> (Currently this command is unavailable)"
				elif x == 'mail':
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "   SN                        TITLE   "
					print "-------------------------------------"
					print "   01                       UN-NAMED "
					print "   02                     UN-NAMED(2)"
					print "   03                     UN-NAMED(3)"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					else:
						print "To view the mail type the serial no."
				elif x == 'ls':
					print "kenny.txt"
				elif x == 'kenny.txt':
					print "IP: 785.120.45.012"
				elif x == "disconnect":
					time.sleep(1)
					print "Invalid Request."
				elif x == "runsc":
					time.sleep(1)
					Level2().animateupdown("Running System Scan. Please wait...")
					time.sleep(2)
					print "\n"
					print "System Health: Good"
					print "Status: Clean"
				elif x == 'igiveup':
					return 'level4'
				elif x == "TX001":
					printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % user)
					bgsound()
				elif x == "upload kenny.txt 202.145.785.45" or x == "-u kenny.txt 202.145.785.45" or x == "upload":
					print "Currently uploading from your system is unavailable."
				elif x == "download" or  x == '-d':
					print "Download(-d) <FileName> <IP>"
				elif x == "forward" or x == "-f":
					print "Forward mail/SN <IP>"
				elif x == '':
					x
				elif x == 'connect 785.120.45.012':
					try:
						time.sleep(1)
						Level1().animate('Connecting', 7)
						print "\n"
						name = raw_input("Username: ")
						password = getpass("Password: ")
						if name == 'kenny' and password == 'alice1345':
							print "\nLogin Successful"
							time.sleep(1)
							Level1().animate('System scanning', 10)
							print "\n"
							printf("I found nothing important in the pc. You need to undelete the files and messages to reveal the secret. \nDownload the 'Undelete' from 112.145.10.236 and it would do rest of the things automatically. \nNote that after finishing your job don't forget to uninstall it.\n\n")
							undelete = False
							uninst = False
							upload = False
							forward = False
							while True:
								y = raw_input('kenny$Terminal:~ ')
								if y == "help":
									print "\n"
									print "                     List of available commands"
									print "-----------------------------------------------------------------------------"
									print "|  Commands                                         Descriptions"
									print "-----------------------------------------------------------------------------"
									print "|   ls                                     lists files and directories"
									print "|  ping<IP>                             Check the status of remote server"
									print "|  mail                                      Launch the mail program"
									print "| forward(-f) mail/SN <IP>             Forwards the given mail to given IP"
									print "| connect<IP>                             Connects to the remote server"
									print "| disconnect                                Terminates the connection "
									print "|   help                                         Show this menu"
									print "|upload(-u) <FileName> <IP>          Upload the current file to the given IP"
									print "|download(-d) <FileName> <IP>        Downloads the current file from given IP"
									print "|uninstall <FileName>                           Uninstalls given file"
									print "-----------------------------------------------------------------------------"
									print "\n"
								elif y == "ls" and undelete == False:
									print "Files and Directories inaccessible."
								elif y == 'ping':
									print "ping <IP> (Currently this command is unavailable)"
								elif y == "connect":
									print "Connect <IP>"
								elif y == "disconnect":
									time.sleep(2)
									Level1().animate("Disconnecting", 3)
									print "\nFailed to disconnect you at the moment."
								elif y == "download Undelete 112.145.10.236" or y == "-d Undelete 112.145.10.236":
									time.sleep(1)
									print "\n"
									Level2().animateupdown("Downloading...")
									time.sleep(1)
									print "\n"
									Level2().animateupdown("Installing...")
									time.sleep(1)
									print "\nSuccessfully installed Undelete."
									time.sleep(2)
									print "Initializing...",
									time.sleep(3)
									print "\r",
									sys.stdout.write('\x1b[K')
									Level2().animateupdown("Running a deep scan...")
									time.sleep(0.5)
									print "\nScan successfully completed."
									time.sleep(0.5)
									Level2().animateupdown("Recovering deleted files...")
									time.sleep(1)
									print "\nSuccessfully recovered deleted files.\n"
									undelete = True
								elif y == "uninstall Undelete":
									time.sleep(1)
									Level1().animate("Uninstalling", 6)
									time.sleep(1)
									print "\nSuccessfully uninstalled Undelete."
									uninst = True
								elif y == "mail" and undelete == False:
									time.sleep(1)
									print "\nOpening mail..."
									time.sleep(3)
									print "-------------------------------------"
									print "   SN                        TITLE   "
									print "-------------------------------------"
									print "             NO MESSAGES             "
									print "\n"
								elif y == "ls" and undelete == True:
									print "Diary.txt"
								elif y == 'Diary.txt':
									print "It's been five years since I lost my son :( \nPublicly it was an accident but actually it wasn't. \nAfter five years I found that the my boss, the person, under whom I worked is a curlprit behind all these. \nI won't be allowing him to live peacefully. I'll do something."
									print "                                                                                            Kenny "
								elif y == 'mail' and undelete == True:
									time.sleep(1)
									print "\nOpening mail..."
									time.sleep(3)
									print "-------------------------------------"
									print "   SN                        TITLE   "
									print "-------------------------------------"
									print "   01                         ME     "
									print "   02                        Honey   "
									print "\n"
									y = raw_input('kenny$Terminal/mail:~ ')
									if y == '01':
										print "Hi honey, I'll be arriving late today. Gotta do some important work. Don't wait for me.\n"
									elif y == '02':
										print "Why what happened ?\n"
									else:
										print "To view the mail type the serial no."
								elif (y == "upload Diary.txt 202.145.785.45" or y == "-u Diary.txt 202.145.785.45") and forward == False:
									print "\n"
									Level2().animateupdown("Uploading...")
									print "\n"
									print "File successfully uploaded."
									upload = True
								elif (y == "forward mail/01 202.145.785.45" or y == "-f mail/01 202.145.785.45") and upload == True and uninst == True:
									print "\n"
									Level1().animate("Forwarding", 3)
									print "\n"
									print "Mail successfully forwarded."
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('kenny$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										time.sleep(1)
										break
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...")
										time.sleep(1)
										break
								elif (y == "forward mail/01 202.145.785.45" or y == "-f mail/01 202.145.785.45") and upload == False:
									print "\n"
									Level1().animate("Forwarding", 3)
									print "\n"
									print "Mail successfully forwarded."
									forward = True
								elif y == "upload Diary.txt 202.145.785.45" or y == "-u Diary.txt 202.145.785.45" and forward == True and uninst == True:
									print "\n"
									Level2().animateupdown("Uploading...")
									print "\n"
									print "File successfully uploaded.\n"
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('kenny$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										time.sleep(1)
										break
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...")
										time.sleep(1)
										break
								elif y == '':
									x
								elif (y == "forward mail/01 202.145.785.45" or y == "-f mail/01 202.145.785.45") and upload == True and uninst == False:
									print "\n"
									Level1().animate("Forwarding", 3)
									print "\n"
									print "Mail successfully forwarded."
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('kenny$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										return 'death'
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...")
										time.sleep(1)
										return 'death'
								elif (y == "upload Diary.txt 202.145.785.45" or y == "-u Diary.txt 202.145.785.45") and forward == True and uninst == False:
									print "\n"
									Level2().animateupdown("Uploading...")
									print "\n"
									print "File successfully uploaded.\n"
									time.sleep(1)
									printf("You have successfully completed your mission. You have a new message. \nReturn to your terminal to view it.\n\n")
									y = raw_input('kenny$Terminal:~ ')
									if y == 'disconnect':
										time.sleep(2)
										Level1().animate("Disconnecting", 3)
										time.sleep(1)
										return 'death'
									else:
										printf("After completing the mission you don't have any right to access the terminal. I am disconnecting you...")
										time.sleep(1)
										return 'death'
								else:
									print "%r command does not exist." % y
							break
						else:
							print "Invalid username or password."
					except Exception:
						print "Failed to connect."
				else:
					print "%r command does not exist." % x
					
			time.sleep(2)
			print "\n"
			print '%s$Terminal:~ ' % user
			time.sleep(1)
			printf("\nYou have been successfully disconnected. Type 'mail' to see check your message.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level2().cmnds()
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "   SN                        TITLE   "
					print "-------------------------------------"
					print "   01                       UN-NAMED "
					print "   02                     UN-NAMED(2)"
					print "   03                     UN-NAMED(3)"
					print "   04                     UN-NAMED(4)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
						time.sleep(2)
						return 'level4'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					print "Your terminal is currently in upgrade. Commands are inaccessible."
					
			

	class Level4(Scene):
		
		def breaker(self):
			def printinoneline(*s):
				t_end = time.time() + 5
				print "Password:\t",
				while time.time() < t_end:
					for i in s:
						print "\b\b\b\b\b\b\b",
						time.sleep(0.03)
						print i,
						sys.stdout.flush()
						sys.stdout.write('\x1b[K')
			
			sys.stdout.write('\x1b[A')
			printinoneline('wed34', 'tue78', 'mon23', 'fre34', 'sun56', 'an45d', 'bw34x')
			print "\r",
			printinoneline('bsd34', 'b34df', 'bwe34', 'ba23n', 'b65we', 'b47mn', 'bqt21')
			print "\r",
			printinoneline('bqswr', 'bq3er', 'bq245', 'bq12r', 'bqz1c', 'bq13o', 'bqer5')
			print "\r",
			printinoneline('bq2sr', 'bq2!z', 'bq25c', 'bq2lc', 'bq2oi', 'bq2as', 'bq29@')
			print "\r",
			printinoneline('bq2@e', 'bq2@d', 'bq2@5', 'bq2@m', 'bq2@k', 'bq2@g', 'bq2@l')
			print "\r",
			print "Password:      "
		
		def cmnds(self):
			print "\n"
			print "                     List of available commands"
			print "---------------------------------------------------------------------------------"
			print "|  Commands                                        Descriptions"
			print "---------------------------------------------------------------------------------"
			print "|   ls                                     lists files and directories"
			print "|  ping<IP>                             Check the status of remote server"
			print "|  mail                                      Launch the mail program"
			print "| forward(-f) mail/SN <IP>                  Forwards the given mail to given IP"
			print "| connect<IP>                             Connects to the remote server"
			print "| disconnect                                Terminates the connection "
			print "|  runsc                                       Runs System Scan"
			print "|  help                                         Show this menu"
			print "|  TX001                                       Acitivates the AI"
			print "|upload(-u) <FileName> <IP>          Upload the current file to the given IP"
			print "|download(-d) <FileName> <IP>        Downloads the current file from given IP"
			print "| breaker(-b)                     Attempts to break password (used in pass field)"
			print "\n"
		
		def enter(self):
			time.sleep(1)
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			print "\n"
			Level3().printinoneline("Getting required modules...", "Applying Updates...", "Activating TX001...", "Checking log files...", "Files successfully checked.")
			time.sleep(0.5)
			Level2().animateupdown("\n\nInstalling Breaker...")
			print "\nBreaker successfully installed."
			time.sleep(1)
			printf("\nBreaker is a software used to break in through the passwords. \nYou can access the software by using the command 'breaker' or '-b'. \nNote that these are the official tools downloaded from official servers \nwhich no one has any access to,  other than Anonymous members. \nType 'breaker' in pass field to break passwords using hash algorithm. \n")
			time.sleep(0.5)
			printf("\nThere's a new mail for you.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == 'ping':
					print "ping <IP> (Currently this command is unavailable)"
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					else:
						print "To view the mail type the serial no."
				elif x == 'ls':
					print "esta.txt"
				elif x == 'igiveup':
					return 'level5'
				elif x == 'esta.txt':
					print "IP: 145.741.259.32"
				elif x == "disconnect":
					time.sleep(1)
					print "Invalid Request."
				elif x == "runsc":
					time.sleep(1)
					Level2.animateupdown("Running System Scan. Please wait...")
					time.sleep(1)
					print "\n"
					print "System Health: Good"
					print "Status: Clean"
				elif x == "TX001":
					printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % user)
					bgsound()
				elif x == "upload esta.txt 202.145.785.45" or x == "-u esta.txt 202.145.785.45" or x == "upload":
					print "Currently uploading from your system is unavailable."
				elif x == "download" or x == '-d':
					print "Download(-d) <FileName> <IP>"
				elif x == "forward" or x == "-f":
					print "Forward mail/SN <IP>"
				elif x == '':
					x
				elif x == 'connect 145.741.259.32':
					try:
						time.sleep(1)
						Level1().animate('Connecting', 7)
						time.sleep(1)
						printf("\nYou have 50 seconds to login and reset the password.\n\n")
						t_end = time.time() + 50
						while time.time() < t_end:
							print "\n"
							name = raw_input("Username: ")
							password = getpass("Password: ")
							if name == 'esta' and password == 'breaker' and time.time() < t_end:
								Level4().breaker()
								time.sleep(1)
								print "\nYou have successfully logged in."
								time.sleep(1)
								print "\nOur security systems detected some issues with the login process. \nWould you like to reset the password?\n"
								y = raw_input("esta$Terminal:~ ")
								x = y.lower()
								if x == 'yes' or x == 'yeah' or x == 'yup':
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
								elif x == 'no' or x == 'nope' or x == 'nopes':
									print "Sorry we can't let you access the terminal. You need to set a new password."
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
								elif y == '':
									y
								else:
									print "Sorry, presently any commands are inaccessible. You need to be get verified."
									time.sleep(1)
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
							elif name == 'esta' and password == 'bq2@c' and time.time() < t_end:
								time.sleep(1)
								print "\nYou have successfully logged in."
								time.sleep(1)
								print "\nOur security systems detected some issues with the login process. \nWould you like to reset the password?"
								y = raw_input("esta$Terminal:~ ")
								x = y.lower()
								if x == 'yes' or x == 'yeah' or x == 'yup':
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
								elif x == 'no' or x == 'nope' or x == 'nopes':
									print "Sorry we can't let you access the terminal. You need to set a new password."
									time.sleep(1)
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
								elif y == '':
									y
								else:
									print "Sorry, presently any commands are inaccessible. You need to be get verified."
									time.sleep(1)
									m = raw_input("ENTER NEW PASSWORD: ")
									n = raw_input("CONFIRM NEW PASSWORD: ")
									if m == n and m != 'NONE' and n != 'NONE':
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nYou failed to follow the instruction carefully.\n\n")
										time.sleep(2)
										return 'death'
									elif m == "NONE" and n == "NONE":
										print "Password has been successfully reset."
										time.sleep(1)
										printf("\nWell done. You have a new mail. Disconnect from here to check in your terminal.\n\n")
										y = raw_input("esta$Terminal:~ ")
										if y == 'disconnect':
											time.sleep(2)
											Level1().animate("Disconnecting", 3)
											break
										else:
											printf("Due to some privacy issues you have no right to access the terminal after your job is over. I am disconnecting you...\n\n")
											time.sleep(1)
											break
									elif m != n:
										print "Passwords mismatch. Logging you out..."
										time.sleep(1)
										m
									else:
										print "Enter new password to reset."
										m
							else:
								print "Invalid username or password."
						if time.time()> t_end:
							time.sleep(1)
							printf("You failed to complete the mission. You ran out of time.")
							time.sleep(1)
							return 'death'
						else:
							break
					except Exception:
						print "Failed to connect."
				else:
					print "%r command does not exist." % x
					
			time.sleep(2)
			print '%s$Terminal:~ ' % user
			time.sleep(1)
			printf("\nYou have been successfully disconnected. Type 'mail' to see check your message.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "|  06                     UN-NAMED(6)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
						time.sleep(1)
						return 'level5'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					print "Your terminal is currently in upgrade. Commands are inaccessible."



	class Level5(Scene):

		def breaker(self):
			def printinoneline(*s):
				t_end = time.time() + 5
				print "Password:\t",
				while time.time() < t_end:
					for i in s:
						print "\b\b\b\b\b\b\b",
						time.sleep(0.03)
						print i,
						sys.stdout.flush()
						sys.stdout.write('\x1b[K')
			
			sys.stdout.write('\x1b[A')
			printinoneline('wed34', 'tue78', 'mon23', 'fre34', 'sun56', 'an45d', 'bw34x')
			print "\r",
			printinoneline('asd34', 'a34df', 'awe34', 'aa23n', 'a65we', 'a47mn', 'aqt21')
			print "\r",
			printinoneline('a8swr', 'a83er', 'a8245', 'a812r', 'a8z1c', 'a813o', 'a8er5')
			print "\r",
			printinoneline('a8msr', 'a8m!z', 'a8m5c', 'a8mlc', 'a8moi', 'a8mas', 'a8m9@')
			print "\r",
			printinoneline('a8m1e', 'a8m1d', 'a8m15', 'a8m1m', 'a8m1k', 'a8m1g', 'a8m1n')
			print "\r",
			print "Password:      "

		def enter(self):
			print "\n"
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			print "\n"
			Level3().printinoneline("Getting required modules...", "Applying Updates...", "Activating TX001...", "Checking log files...", "Files successfully checked.")
			time.sleep(0.5)
			Level2().animateupdown("\nInstalling necessary drivers...")
			print "\nDrivers successfully installed."
			time.sleep(1)
			printf("\nCongo! It's a great honour that you have successfully completed the time-trial mission. \nYou have been promoted and some new features in your terminal has been unlocked. \nNow you could able to ping the server to see it's status. \nThere's a new mail awaiting for you.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == 'ping':
					print "ping <IP>"
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "|  06                     UN-NAMED(6)"
					print "|  07                     UN-NAMED(7)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
					elif x == '07':
						print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
					else:
						print "To view the mail type the serial no."
				elif x == 'ping 145.366.74.001':
					time.sleep(1)
					Level1().animate('Pinging 145.366.74.001 with 32 bytes of data', 3)
					print "\nReply from 145.366.74.001: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 145.366.74.001: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 145.366.74.001: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 145.366.74.001: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nPing statistics for 145.366.74.001:"
					print "\tPackets: Sent = 4, Received = 4, Lost = 0 (0% loss)"
					print "Approximate round trip times in milli-seconds:"
					print "\tMinimum = 46ms, Maximum = 47ms, Average = 46ms"
					bgsound()
				elif x == 'ls':
					print "No files or diretories."
				elif x == "disconnect":
					time.sleep(1)
					print "Invalid Request."
				elif x == "runsc":
					time.sleep(1)
					Level2.animateupdown("Running System Scan. Please wait...")
					time.sleep(1)
					print "\n"
					print "System Health: Normal"
					print "Status: Clean"
				elif x == 'igiveup':
					return 'level6'
				elif x == "TX001":
					printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % user)
				elif x == "upload" or x == '-u':
					print "Currently uploading from your system is unavailable."
				elif x == "download" or x == '-d':
					print "Download(-d) <FileName> <IP>"
				elif x == "forward" or x == "-f":
					print "Forward mail/SN <IP>"
				elif x == '':
					x
				elif x == 'connect 145.366.74.001':
					try:
						time.sleep(1)
						Level1().animate('Connecting', 7)
						print "\n"
						print "-----------------------"
						print "WELCOME TO SYNCLINK..."
						print "-----------------------"
						print "Here you may find some authentic articles regarding the deeds of anonymous hackers."
						raw_input("\nPress enter to continue...")
						time.sleep(1)
						printf("\nYou have only 40 seconds to shutdown the site. I am redirecting you to the admin page...\n\n")
						time.sleep(2)
						name = raw_input("Username: ")
						password = getpass("Password: ")
						if name == 'admin' and password == 'breaker':
							Level5().breaker()
							time.sleep(1)
							print "You have successfully logged in."
							time.sleep(1)
							print "Welcome admin."
							t_end = time.time() + 40
							while time.time() < t_end:
								y = raw_input('admin$Terminal:~ ')
								if y == 'help':
									print "\n"
									print "                     List of available commands"
									print "-------------------------------------------------------------------------------"
									print "| Commands                                        Descriptions"
									print "-------------------------------------------------------------------------------"
									print "|   post                                         Posts to wesite"
									print "| shut-down(-s) <IP>                       Shuts down the current website"
									print "-------------------------------------------------------------------------------"
									print "\n"
								elif y == 'post':
									print "\nWhat would you like to post ?"
									raw_input('Post: ')
									print "\nYou post has successfully been posted."
								elif y == 'shut-down 145.366.74.001' or y == '-s 145.366.74.001':
									time.sleep(1)
									Level1().animate('Shutting Down', 5)
									time.sleep(1)
									printf('\nCheck whether the site has been successfully shut or not.\n\n')
									x = raw_input('%s$Terminal:~ ' % user)
									if x == "help":
										Level4().cmnds()
									elif x == 'ping':
										print "ping <IP>"
									elif x == 'ping 145.366.74.001':
										time.sleep(1)
										Level1().animate('Pinging 145.366.74.001 with 32 bytes of data', 2)
										time.sleep(1)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(1)
										print "\nPing statistics for 145.366.74.001:"
										print "\tPackets: Sent = 4, Received = 0, Lost = 4 (100% loss)"
										time.sleep(1)
										break
									elif x == "mail":
										time.sleep(1)
										print "\nOpening mail..."
										time.sleep(3)
										print "-------------------------------------"
										print "|  SN                        TITLE   "
										print "-------------------------------------"
										print "|  01                       UN-NAMED "
										print "|  02                     UN-NAMED(2)"
										print "|  03                     UN-NAMED(3)"
										print "|  04                     UN-NAMED(4)"
										print "|  05                     UN-NAMED(5)"
										print "|  06                     UN-NAMED(6)"
										print "|  07                     UN-NAMED(7)"
										print "-------------------------------------"
										print "\n"
										x = raw_input('%s$Terminal/mail:~ ' % user)
										if x == '01':
											print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
										elif x == '02':
											print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
										elif x == '03':
											print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
										elif x == '04':
											print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
										elif x == '05':
											print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but 	fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
										elif x == '06':
											print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
										elif x == '07':
											print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
										else:
											print "To view the mail type the serial no."
									elif x == 'ls':
										print "No files or diretories."
									elif x == "disconnect":
										time.sleep(1)
										print "Invalid Request."
									elif x == "runsc":
										time.sleep(1)
										Level2.animateupdown("Running System Scan. Please wait...")
										time.sleep(1)
										print "\n"
										print "System Health: Normal"
										print "Status: Clean"
									elif x == "TX001":
										printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % register.namevariable.get())
									elif x == "upload" or x == '-u':
										print "Currently uploading from your system is unavailable."
									elif x == "download" or x == '-d':
										print "Download(-d) <FileName> <IP>"
									elif x == "forward" or x == "-f":
										print "Forward mail/SN <IP>"
									elif x == '':
										x
									elif x == 'connect':
										print "No server to connect at the moment."
									else:
										print "%r command does not exist." % x
								elif y == '':
									y
								else:
									'%r command does not exist.' % y
							if time.time()> t_end:
								time.sleep(1)
								printf("You failed to complete the mission. You ran out of time.")
								time.sleep(1)
								return 'death'
							else:
								break
						elif name == 'admin' and password == 'a8m1n':
							time.sleep(1)
							print "You have successfully logged in."
							time.sleep(1)
							print "Welcome admin."
							t_end = time.time() + 40
							while time.time() < t_end:
								y = raw_input('admin$Terminal:~ ')
								if y == 'help':
									print "\n"
									print "                     List of available commands"
									print "-------------------------------------------------------------------------------"
									print "| Commands                                        Descriptions"
									print "-------------------------------------------------------------------------------"
									print "|   post                                         Posts to wesite"
									print "| shut-down(-s) <IP>                       Shuts down the current website"
									print "-------------------------------------------------------------------------------"
									print "\n"
								elif y == 'post':
									print "\nWhat would you like to post ?"
									raw_input('Post: ')
									print "\nYou post has successfully been posted."
								elif y == 'shut-down 145.366.74.001' or y == '-s 145.366.74.001':
									time.sleep(1)
									Level1().animate('Shutting Down', 5)
									time.sleep(1)
									printf('\nCheck whether the site has been successfully shut or not.\n\n')
									x = raw_input('%s$Terminal:~ ' % user)
									if x == "help":
										Level4().cmnds()
									elif x == 'ping':
										print "ping <IP>"
									elif x == 'ping 145.366.74.001':
										time.sleep(1)
										Level1().animate('Pinging 145.366.74.001 with 32 bytes of data', 2)
										time.sleep(1)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(0.5)
										print "\nRequest timed out"
										time.sleep(1)
										print "\nPing statistics for 145.366.74.001:"
										print "\tPackets: Sent = 4, Received = 0, Lost = 4 (100% loss)"
										time.sleep(1)
										break
									elif x == "mail":
										time.sleep(1)
										print "\nOpening mail..."
										time.sleep(3)
										print "-------------------------------------"
										print "|  SN                        TITLE   "
										print "-------------------------------------"
										print "|  01                       UN-NAMED "
										print "|  02                     UN-NAMED(2)"
										print "|  03                     UN-NAMED(3)"
										print "|  04                     UN-NAMED(4)"
										print "|  05                     UN-NAMED(5)"
										print "|  06                     UN-NAMED(6)"
										print "|  07                     UN-NAMED(7)"
										print "-------------------------------------"
										print "\n"
										x = raw_input('%s$Terminal/mail:~ ' % user)
										if x == '01':
											print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
										elif x == '02':
											print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
										elif x == '03':
											print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
										elif x == '04':
											print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
										elif x == '05':
											print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but 	fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
										elif x == '06':
											print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
										elif x == '07':
											print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
										else:
											print "To view the mail type the serial no."
									elif x == 'ls':
										print "No files or diretories."
									elif x == "disconnect":
										time.sleep(1)
										print "Invalid Request."
									elif x == "runsc":
										time.sleep(1)
										Level2.animateupdown("Running System Scan. Please wait...")
										time.sleep(1)
										print "\n"
										print "System Health: Normal"
										print "Status: Clean"
									elif x == "TX001":
										printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % register.namevariable.get())
									elif x == "upload" or x == '-u':
										print "Currently uploading from your system is unavailable."
									elif x == "download" or x == '-d':
										print "Download(-d) <FileName> <IP>"
									elif x == "forward" or x == "-f":
										print "Forward mail/SN <IP>"
									elif x == '':
										x
									elif x == 'connect':
										print "No server to connect at the moment."
									else:
										print "%r command does not exist." % x
								elif y == '':
									y
								else:
									'%r command does not exist.' % y
							if time.time()> t_end:
								time.sleep(1)
								printf("You failed to complete the mission. You ran out of time.")
								time.sleep(1)
								return 'death'
							else:
								break
						else:
							time.sleep(1)
							print "Invalid username or password."
					except Exception:
						print "Failed to connect."
				else:
					print "%r command does not exist." % x
					
			time.sleep(2)
			print '%s$Terminal:~ ' % user
			time.sleep(1)
			printf("\nYou have successfully shut down the website. You have a new message.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "   SN                        TITLE   "
					print "-------------------------------------"
					print "   01                       UN-NAMED "
					print "   02                     UN-NAMED(2)"
					print "   03                     UN-NAMED(3)"
					print "   04                     UN-NAMED(4)"
					print "   05                     UN-NAMED(5)"
					print "   06                     UN-NAMED(6)"
					print "   07                     UN-NAMED(7)"
					print "   08                     UN-NAMED(8)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45."
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss."
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE."
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community."
					elif x == '07':
						print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently."
					elif x == '08':
						print "\nBravo! The admin doubt that it was we who closed his website. We have given him a warning. \nThe police are trying to trace us. Beware"
						time.sleep(1)
						return 'level6'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					print "Your terminal is currently in upgrade. Commands are inaccessible."
					
					

					
	class Level6(Scene):
		
		def breaker(self):
			def printinoneline(*s):
				t_end = time.time() + 5
				print "Password:\t",
				while time.time() < t_end:
					for i in s:
						print "\b\b\b\b\b\b\b",
						time.sleep(0.03)
						print i,
						sys.stdout.flush()
						sys.stdout.write('\x1b[K')
			
			sys.stdout.write('\x1b[A')
			printinoneline('wed34a', 'tue78q', 'mon23w', 'fre34s', 'sun56x', 'an45dc', 'bw34xf')
			print "\r",
			printinoneline('bsd34e', 'b34df4', 'bwe34f', 'ba23nt', 'b65we6', 'b47mnb', 'bqt21n')
			print "\r",
			printinoneline('bdswr4', 'bd3ert', 'bd245g', 'bd12rh', 'bdz1cv', 'bd13oj', 'bder5b')
			print "\r",
			printinoneline('bdfsr1', 'bdf!z2', 'bdf5cz', 'bdflch', 'bdfoim', 'bdfasv', 'bdf9@p')
			print "\r",
			printinoneline('bdfge2', 'bdfgdr', 'bdfg5e', 'bdfgmi', 'bdfgkl', 'bdfggu', 'bdfg5o')
			print "\r",
			printinoneline('bdfg5q', 'bdfg5k', 'bdfg5o', 'bdfg5$', 'bdfg5l', 'bdfg51', 'bdfg5p')
			print "Password:       "
			
		def breakernum(self):
			def printinoneline(*s):
				t_end = time.time() + 5
				print "Password:\t",
				while time.time() < t_end:
					for i in s:
						print "\b\b\b\b\b\b\b",
						time.sleep(0.03)
						print i,
						sys.stdout.flush()
						sys.stdout.write('\x1b[K')
			
			sys.stdout.write('\x1b[A')
			printinoneline('wed34', 'tue78', 'mon23', 'fre34', 'sun56', 'an45d', 'bw34x')
			print "\r",
			printinoneline('4sd34', '434df', '4we34', '4a23n', '465we', '447mn', '4qt21')
			print "\r",
			printinoneline('45swr', '453er', '45245', '4512r', '45z1c', '4513o', '45er5')
			print "\r",
			printinoneline('451sr', '451!z', '4515c', '451lc', '451oi', '451as', '4519@')
			print "\r",
			printinoneline('4512e', '4512d', '45125', '4512m', '4512k', '4512g', '4512n')
			print "\r",
			print "Password: 45127"
		
		def enter(self):
			time.sleep(1)
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			print "\n"
			Level3().printinoneline("Getting required modules...", "Applying Updates...", "Activating TX001...", "Checking log files...", "Files successfully checked.")
			time.sleep(1)
			printf("\nThe police are trying to trace us. I have a built-in advanced firewall that control every traffics you send and receive. \nI only allow you to receive the authorized traffics and the unauthorized ones are immediately denied. \nBut the police are trying something like DDoS and I don't know how long I could able to hold them back. \nUnfortunately during such amount of request handling I encounter some problem in secured IP masking of your computer. \nFrom now on before you connect to the server you need to first connect to our private proxy \nand then only you will be authorized to connect to the distant server. \nI don't know but maybe you need to continue. without me for next of the levels.\n\n")
			time.sleep(1)
			printf("There's a new mail for you %s\n\n\n" % user)
			time.sleep(1)
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == 'ping':
					print "ping <IP>"
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "|  06                     UN-NAMED(6)"
					print "|  07                     UN-NAMED(7)"
					print "|  08                     UN-NAMED(8)"
					print "|  09                     UN-NAMED(9)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
					elif x == '07':
						print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
					elif x == '08':
						print "\nBravo! The admin doubt that it was we who closed his website. We have given him a warning. \nThe police are trying to trace us. Beware\n"
					elif x == '09':
						print "\nThe corrupted policemen of the community is constantly trying to reach us. They have hired some hackers too. \nFailing all the methods, they are trying something messy like DDoS. \nFor this few of our servers got overloaded with unauthorized client requests and as a result they are down for sometime. \nWe have something like master security which ensures our protection quite for sometime \nbut it could also be hacked either too. We have found that Brian De Luas, the officer in-charge, takes huge amount of bribe. \nHe has two bank a/c. He always keep all his black money in his second bank a/c. \nThe name of the bank is FOU INTERNATIONAL. \nGo and hack his bank a/c and transfer all the money to our temporary a/c under the name 'AnnoTemp'. \nThe IP address of the bank is 205.145.23.452. Since we got the info that TX-001 is unable to mask your IP, \nso you need to connect to our few proxy sites that could mask your IP for a very short period of time \nbefore you can connect to the original server. The bank is highly secured so you may note that \nas soon as you use your password breaker tool the security may fire up traceback process. \nSince our servers are located quite a far away so they will need some time to locate you. \nWithin that time you need to complete your work. \nThe IP of our first and second servers are 120.45.236.12 and 120.36.412.10 respectively. \nGood Luck for your mission.\n"
					else:
						print "To view the mail type the serial no."
				elif x == 'ping 205.145.23.452':
					time.sleep(1)
					Level1().animate('Pinging 205.145.23.452 with 32 bytes of data', 3)
					print "\nReply from 205.145.23.452: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 205.145.23.452: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 205.145.23.452: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nReply from 205.145.23.452: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nPing statistics for 205.145.23.452:"
					print "\tPackets: Sent = 4, Received = 4, Lost = 0 (0% loss)"
					print "Approximate round trip times in milli-seconds:"
					print "\tMinimum = 46ms, Maximum = 47ms, Average = 46ms"
					bgsound()
				elif x == 'ping 120.45.236.12':
					time.sleep(1)
					Level1().animate('Pinging 120.45.236.12 with 32 bytes of data', 3)
					print "Reply from 120.45.236.12: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.45.236.12: bytes=32 time=46ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.45.236.12: bytes=32 time=45ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.45.236.12: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nPing statistics for 120.45.236.12:"
					print "\tPackets: Sent = 4, Received = 4, Lost = 0 (0% loss)"
					print "Approximate round trip times in milli-seconds:"
					print "\tMinimum = 46ms, Maximum = 47ms, Average = 46ms"
					bgsound()
				elif x == 'ping 120.36.412.10':
					time.sleep(1)
					Level1().animate('Pinging 120.36.412.10 with 32 bytes of data', 3)
					print "Reply from 120.36.412.10: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.36.412.10: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.36.412.10: bytes=32 time=45ms TTL=56"
					time.sleep(0.5)
					print "Reply from 120.36.412.10: bytes=32 time=47ms TTL=56"
					time.sleep(0.5)
					print "\nPing statistics for 120.36.412.10:"
					print "\tPackets: Sent = 4, Received = 4, Lost = 0 (0% loss)"
					print "Approximate round trip times in milli-seconds:"
					print "\tMinimum = 46ms, Maximum = 47ms, Average = 46ms"
					bgsound()
				elif x == 'ls':
					print "No files or diretories."
				elif x == 'igiveup':
					return 'level7'
				elif x == "disconnect":
					time.sleep(1)
					print "Invalid Request."
				elif x == "runsc":
					time.sleep(2)
					Level2.animateupdown("Running System Scan. Please wait...")
					time.sleep(1)
					print "\n"
					print "System Health: Normal"
					print "Status: Clean"
				elif x == "TX001":
					printf("\nHi %s. By default I'm already activated and will give you any required info whenever there's a need.\n\n" % user)
				elif x == "upload" or x == '-u':
					print "Currently uploading from your system is unavailable."
				elif x == "download" or x == '-d':
					print "Download(-d) <FileName> <IP>"
				elif x == "forward" or x == "-f":
					print "Forward mail/SN <IP>"
				elif x == '':
					x
				elif x == 'connect 120.36.412.10':
					time.sleep(1)
					print "You need to first connect to the primary proxy 120.45.236.12."
				elif x == 'connect 205.145.23.452':
					time.sleep(1)
					print "Access denied. First connect to any proxy server. Your public IP is exposed."
				elif x == 'connect 120.45.236.12':
					try:
						time.sleep(1)
						Level1().animate('Connecting', 7)
						print "\n"
						y = raw_input("Proxy1:~ ")
						if y == 'connect 120.36.412.10':
							try:
								time.sleep(1)
								Level1().animate('Connecting', 7)
								print "\n"
								z = raw_input("Proxy2:~ ")
								if z == 'connect 205.145.23.452':
									try:
										time.sleep(1)
										Level1().animate('Connecting', 7)
										time.sleep(1)
										print "\nWelcome to FOU INTERNATIONAL\n"
										raw_input("Press enter to continue...")
										t_end = time.time() + 50
										printf("\nYou have 40 seconds to tranfer the money. So be fast.\n\n")
										while time.time() < t_end:
											name = raw_input("Member: ")
											password = getpass("Password: ")
											if name == 'Brian D. Luas' and password == 'breaker':
												Level6().breaker()
												time.sleep(1)
												print "Welcome Brian D. Luas"
												y = raw_input('brian$a/c:~ ')
												if y == 'help':
													print "\n"
													print "                     List of available commands"
													print "------------------------------------------------------------------------------"
													print "| Commands                                        Descriptions"
													print "------------------------------------------------------------------------------"
													print "|   add                                         Add money to your a/c"
													print "| withdraw                                  Withdraw money from your a/c"
													print "| showamt                                Shows amount of money in your a/c"
													print "|transfer(-t) to/from <ID>            Transfer money to/from specified a/c ID"
													print "------------------------------------------------------------------------------"
													print "\n"
												elif y == 'add':
													print "\nSorry sir you have already exceeded the limit. You can't add anymore money to this a/c."
												elif y == 'withdraw':
													print "\nSorry sir you have exceeded your withdraw limit for today. \nCome back tomorrow to withdraw more money."
												elif y == 'showamt':
													print "\nCurrently you have $100.9B in your a/c."
												elif y == 'transfer to AnnoTemp' or y == '-t to AnnoTemp':
													Level1().animate("Processing. Please Wait", 5)
													print "\nFor security we have sent you a digit PIN to your mobile no.\nEnter the PIN to continue.\n"
													z = raw_input('PIN:~ ')
													if z == 'breaker':
														Level6().breakernum()
														time.sleep(2)
														print "PIN matched."
														print "\n"
														Level2().animateupdown('Transferring...')
														print "Transfer Successful."
														time.sleep(1)
														break
													elif z == '45127':
														print "PIN matched."
														print "\n"
														Level2().animateupdown('Transferring...')
														print "Transfer Successful."
														time.sleep(1)
														break
													else:
														print "PIN mistmatch."
														time.sleep(1)
														return 'death'
												elif y == '':
													y
												else:
													print "%r command does not exist." % y
											elif name == 'Brian D. Luas' and password == 'bdfg5$':
												time.sleep(1)
												print "Welcome Brian D. Luas"
												y = raw_input('brian$a/c:~ ')
												if y == 'help':
													print "\n"
													print "                     List of available commands"
													print "------------------------------------------------------------------------------"
													print "| Commands                                        Descriptions"
													print "------------------------------------------------------------------------------"
													print "|   add                                         Add money to your a/c"
													print "| withdraw                                  Withdraw money from your a/c"
													print "| showamt                                Shows amount of money in your a/c"
													print "|transfer(-t) to/from <ID>            Transfer money to/from specified a/c ID"
													print "------------------------------------------------------------------------------"
													print "\n"
												elif y == 'add':
													print "\nSorry sir you have already exceeded the limit. You can't add anymore money to this a/c."
												elif y == 'withdraw':
													print "\nSorry sir you have exceeded your withdraw limit for today. \nCome back tomorrow to withdraw more money."
												elif y == 'showamt':
													print "\nCurrently you have $100.9B in your a/c."
												elif y == 'transfer to AnnoTemp' or y == '-t to AnnoTemp':
													Level1().animate("Processing. Please Wait", 5)
													print "\nFor security we have sent you a digit PIN to your mobile no.\nEnter the PIN to continue.\n"
													z = raw_input('PIN:~ ')
													if z == 'breaker':
														Level6().breakernum()
														time.sleep(2)
														print "PIN matched."
														print "\n"
														Level2().animateupdown('Transferring...')
														print "Transfer Successful."
														time.sleep(1)
														break
													elif z == '45127':
														print "PIN matched."
														print "\n"
														Level2().animateupdown('Transferring...')
														print "Transfer Successful."
														time.sleep(1)
														break
													else:
														print "PIN mistmatch."
														time.sleep(1)
														return 'death'
												elif y == '':
													y
												else:
													print "%r command does not exist." % y
											else:
												print "Invalid username or password."
										if time.time()> t_end:
											time.sleep(1)
											printf("You failed to complete the mission. You ran out of time.")
											time.sleep(1)
											return 'death'
										else:
											break
									except Exception:
										print "Failed to connect."
								else:
									time.sleep(0.5)
									print "Connect to the main server 205.145.23.452."
							except Exception:
								print "Failed to connect."
						else:
							time.sleep(0.5)
							print "Connect to the secondary proxy 120.36.412.10."
					except Exception:
						print "Failed to connect."
				else:
					print "%r command does not exist." % x
					
			time.sleep(2)
			print '%s$Terminal:~ ' % user
			time.sleep(1)
			printf("\nYou have successfully transferred all the money to our community a/c.\n\n")
			bgsound()
			while True:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "|  06                     UN-NAMED(6)"
					print "|  07                     UN-NAMED(7)"
					print "|  08                     UN-NAMED(8)"
					print "|  09                     UN-NAMED(9)"
					print "|  10                    UN-NAMED(10)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
					elif x == '07':
						print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
					elif x == '08':
						print "\nBravo! The admin doubt that it was we who closed his website. We have given him a warning. \nThe police are trying to trace us. Beware\n"
					elif x == '09':
						print "\nThe corrupted policemen of the community is constantly trying to reach us. They have hired some hackers too. \nFailing all the methods, they are trying something messy like DDoS. \nFor this few of our servers got overloaded with unauthorized client requests and as a result they are down for sometime. \nWe have something like master security which ensures our protection quite for sometime \nbut it could also be hacked either too. We have found that Brian De Luas, the officer in-charge, takes huge amount of bribe. \nHe has two bank a/c. He always keep all his black money in his second bank a/c. \nThe name of the bank is FOU INTERNATIONAL. \nGo and hack his bank a/c and transfer all the money to our temporary a/c under the name 'AnnoTemp'. \nThe IP address of the bank is 205.145.23.452. Since we got the info that TX-001 is unable to mask your IP, \nso you need to connect to our few proxy sites that could mask your IP for a very short period of time \nbefore you can connect to the original server. The bank is highly secured so you may note that \nas soon as you use your password breaker tool the security may fire up traceback process. \nSince our servers are located quite a far away so they will need some time to locate you. \nWithin that time you need to complete your work. \nThe IP of our first and second servers are 120.45.236.12 and 120.36.412.10 respectively. \nGood Luck for your mission.\n"
					elif x == '10':
						print "\nWell done! We distributed that money to some charity fund. \nBrian was shocked to lose such a huge amount and probably \bhad been admitted to the hospital for serious heart-attack. Good job!\n"
						time.sleep(1)
						return 'level7'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					print "Your terminal is currently in upgrade. Commands are inaccessible."
					

					
	class Level7(Scene):

		def enter(self):
			time.sleep(1)
			Level1().animate("Local Host System Bootup", 5)
			time.sleep(2)
			print "Bootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			print "\n"
			Level3().printinoneline("Getting required modules...", "Applying Updates...", "Activating TX001...", "Checking log files...", "Files successfully checked.")
			time.sleep(1)
			printf("\nI can't believe that you finally managed to come up here. You have got a system....\n")
			time.sleep(0.5)
			print "\nYou have been logged out of the session.\n\n"
			time.sleep(3)
			Level1().animate('System shutting down', 5)
			time.sleep(2)
			t_end = time.time() + 7
			print "\n"
			while time.time() < t_end:
				for i in ["/","- ","|","\\","|"]:
					print "%s\r" % i,
			print "\n"
			Level1().animate('Local Host System bootup', 5)
			print "\nBootup complete."
			print "Local Host Online at %s." % time.strftime("%d %B %Y %X")
			print "All Rights Reserved."
			time.sleep(2)
			print "\n"
			Level3().printinoneline('Getting required modules...', 'Activating TX001...')
			time.sleep(1)
			print "ERROR 0x111B23"
			time.sleep(1)
			print "\nUnable to locate TX001.\n"
			time.sleep(1)
			x = range(999)
			t_end = time.time() + 10
			while time.time() < t_end:
				for i in x:
					print hex(i),
					
			time.sleep(1)
			clear = lambda: os.system('cls')
			clear()
			time.sleep(1)
			Level1().animate('Activating TX001', 5)
			printf("\n\nWE ARE HACKED!!! There's someone or a some people who's constantly trying to reach you. \nHe/they initially tried DDoS. Unfortunately I failed to handle so much of requests. \nThey inject an undetectable advancely coded virus in your system and the virus automatically multiplied before I detect it. \nThere's no time now. The virus was made to tamper my program and then he/they will gonna hack your database. \nI'm putting a master key to a database which would at least keep them busy for a week or so \nbefore they could successfully hack into it.\n\n")
			time.sleep(1)
			printf("\nI'm bu0x67ged. They ar0x45 trying to reprogra0x6D me. \nSo ensuring your secur0x69ty I'm shutting myself down. Good lu0x63k!\n\n")
			time.sleep(1)
			Level1().animate("TX001 Shutting Down", 5)
			time.sleep(1)
			t_end = time.time() + 90
			print "\n"
			bgsound()
			while time.time() < t_end:
				x = raw_input('%s$Terminal:~ ' % user)
				if x == "help":
					Level4().cmnds()
				elif x == 'igiveup':
					winsound.PlaySound(None, winsound.SND_PURGE)
					return 'level8'
				elif x == "mail":
					time.sleep(1)
					print "\nOpening mail..."
					time.sleep(3)
					print "-------------------------------------"
					print "|  SN                        TITLE   "
					print "-------------------------------------"
					print "|  01                       UN-NAMED "
					print "|  02                     UN-NAMED(2)"
					print "|  03                     UN-NAMED(3)"
					print "|  04                     UN-NAMED(4)"
					print "|  05                     UN-NAMED(5)"
					print "|  06                     UN-NAMED(6)"
					print "|  07                     UN-NAMED(7)"
					print "|  08                     UN-NAMED(8)"
					print "|  09                     UN-NAMED(9)"
					print "|  10                    UN-NAMED(10)"
					print "|  11                    UN-NAMED(11)"
					print "-------------------------------------"
					print "\n"
					x = raw_input('%s$Terminal/mail:~ ' % user)
					if x == '01':
						print "\nJohn Adwik is found to be a very ridiculous man. He run a self organizing business and have some political impact. \nHe soon turned to be a very fucking creature. The local police and politicians are bribed by him. \nHe was totally ruined and his family is struggling by him. \nThere's still no proof against him so that people could file a case. \nGo and hack his computer, if you find anything useful or interesting upload it to us at 202.145.785.45.\n"
					elif x == '02':
						print "\nSo it seems that John has underworld business of drugs. \nHe had an appointment where he is going to meet with one of the famous drug dealer Thomas Ed Alisa. \nThis would help us in suppressing his attitude. \nWell done!\n"
					elif x == '03':
						print "\nKenny Alam works as a Security Incharge in a reputed software company. He does well of his job. He had a family too. \nHis family consists of his wife and his daughter named Alice. \nWith some deep research we also found that 5 years ago his son died in an car accident. The time probably be 13:45. \nThere's nothing bad in him though. He's also very much popular in the social network. \nBut unfortunately everything turned down. \nRecently there's a hack in the that company and the police suspected the incharge of the security. \nAlthough they seized Kenny's computer but no proof has been found realated to it. \nThey anticipate that Kenny has deleted the necessary files from his computer. \nGo and find out what's in this matter and upload it us at 202.145.785.45.\n"
					elif x == '04':
						print "\nSo you did successfully complete the mission. Kenny Alam's boss was the the ex boyfriend of his wife before marriage. \nIt turned out to be that due to her's rejection of his proposal he took the revenge \nby doing the car accident to Kenny's child. \nFive years later by somehow Kenny come to know all about this, hopefully by his trustee which was not known yet, \nand decided to take a revenge by making a breach into the security system \nand publishing all the company's secrets anonymously. \nThis would make a great deal of loss to the company and would ruin the life of it's victim, his boss.\n"
					elif x == '05':
						print "\nJoseph Esta is found guilty on breaching the security of the political community under National Lines. \nUnfortunately he escaped from the police but fortunately police took over his computer, \nbut they got puzzled since none of them can crack the password. He has used something advance in his scripting so that \nfailure to put the correct password within time would result in wiping away off data. \nGo and hack his computer and reset the password to NONE.\n"
					elif x == '06':
						print "\nIt's the matter of proud for us that you successfully completed the mission. \nWe sent the password to the police and they are able to access his computer and found some important documents. \nIt was found that he had been bribed for breaching the security and the police anticipate that \nthere's some people behind this, who were basically the rivals of the community.\n"
					elif x == '07':
						print "\nThis mission might be a little tougher for you. Let's see. \nSyncLink launched a website criticizing the deeds of Anonymous hackers. \nThey even exposed few of the members in our group and made a well documenetd article. \nWe appreciate the hardwork, the admin had in his way to make such a website, but unfortunately we need to close it down. \nThe site address is 145.366.74.001. \nMake sure you completely shut down the website and delete the content of the server permanently.\n"
					elif x == '08':
						print "\nBravo! The admin doubt that it was we who closed his website. We have given him a warning. \nThe police are trying to trace us. Beware\n"
					elif x == '09':
						print "\nThe corrupted policemen of the community is constantly trying to reach us. They have hired some hackers too. \nFailing all the methods, they are trying something messy like DDoS. \nFor this few of our servers got overloaded with unauthorized client requests and as a result they are down for sometime. \nWe have something like master security which ensures our protection quite for sometime \nbut it could also be hacked either too. We have found that Brian De Luas, the officer in-charge, takes huge amount of bribe. \nHe has two bank a/c. He always keep all his black money in his second bank a/c. \nThe name of the bank is FOU INTERNATIONAL. \nGo and hack his bank a/c and transfer all the money to our temporary a/c under the name 'AnnoTemp'. \nThe IP address of the bank is 205.145.23.452. Since we got the info that TX-001 is unable to mask your IP, \nso you need to connect to our few proxy sites that could mask your IP for a very short period of time \nbefore you can connect to the original server. The bank is highly secured so you may note that \nas soon as you use your password breaker tool the security may fire up traceback process. \nSince our servers are located quite a far away so they will need some time to locate you. \nWithin that time you need to complete your work. \nThe IP of our first and second servers are 120.45.236.12 and 120.36.412.10 respectively. \nGood Luck for your mission.\n"
					elif x == '10':
						print "\nWell done! We distributed that money to some charity fund. \nBrian was shocked to lose such a huge amount and probably \bhad been admitted to the hospital for serious heart-attack. Good job!\n"
					elif x == '11':
						print "\nIf you are seeing this message then you are already hacked. \nWe are sorry to say but we have to disconnect from you so that no confidential info goes into public. \nThe hacker is very much genius as well as clever. \nThe hacking was too low-level to get detected by our system. Maybe you became the victim of traceback \nand probably he will gonna match the possible valus with the key to hack your database for your kind info.\nThere's some hidden commands in your terminal. They are generally accessed by putting -h at the commands. \nProbably '.destroy <SysFile>' and '.shtdwn' is mainly used to delete the system generated files and shutting down the system respectively. \nThese commands were basically controlled by TX001 so you didn't need it unless you do something monster hacking in the system. \nIn order to preserve your anonimity you need to escape from that hacker. \n\nRemember 'DO NOT GIVE ANYONE ANY CHANCE TO HACK YOU'. Good Luck!\n"
						time.sleep(10)
						winsound.PlaySound(None, winsound.SND_PURGE)
						return 'level8'
					else:
						print "To view the mail type the serial no."
				elif x == '':
					x
				else:
					time.sleep(1)
					print "Calling commands failed: "
					print "------------------------ACCESS DENIED"
			winsound.PlaySound(None, winsound.SND_PURGE)
			return 'level8'
			
			
			
	class Level8(Scene):
		
		def printinoneline0(*s):
			for i in s:
				print '\r',
				time.sleep(5)
				print i,
				sys.stdout.flush()
				sys.stdout.write('\x1b[K')
		
		def enter(self):
			time.sleep(1)
			clear = lambda: os.system('cls')
			clear()
			init()
			time.sleep(1)
			print "\x1b[31m"
			printf("Hello hacker. Ever thought that you could also get hacked? \nYou are such a novice hacker I've ever seen who don't know that \nestablishing connection with remote server could leave a little bit of trace too. \nYou're just a gooddamned creature. A shit of mine. \nNow look since I've taken control of your terminal I would get your bio within a while \nand publish it in front of whole world....ha ha ha ha ha.....\n\n")
			time.sleep(1)
			printf("\nWell let me challange you. I'll give you three chance to escape. \nI'll ask you three questions and you have to answer me those. \nIf you correctly answer all three I'll give you a chance to escape. \nBut if you fail to answer any one of them then .....ha ha ha ha ha......\n\n")
			time.sleep(1)
			printf('\nYou will only be given 60 seconds to answer all questions. Good luck my shit!\n')
			t_end = time.time() + 60
			print "\x1b[31m\nQ-1) I don't have eyes, but once I did see. Once I had thoughts, but now I'm white and empty. Who am I?\n"
			bgsound()
			while time.time() < t_end:
				x = raw_input('Ans-1) ')
				y = x.lower()
				if y == 'skull' or y == 'a skull' or y == 'the skull':
					print "\x1b[31m\nYou are too lucky to get it right."
					time.sleep(1)
					print "\x1b[31m\nQ-2) What is it that goes up and goes down but does not move?\n"
					a = raw_input('Ans-2) ')
					p = a.lower()
					if p == 'temperature' or p == 'a temperature' or p == 'the temperature':
						printf("\nI won't say that you are sharp but rather I felt some pity on you my shit.\n")
						time.sleep(1)
						printf("\nLet's see if you really can make it.\n")
						time.sleep(1)
						print "\x1b[31m\nQ-3) What has a Heart but no other organs?\n"
						bgsound()
						b = raw_input("ANS-3) ")
						q = b.lower()
						if q == 'a deck of cards' or q == 'a pack of cards' or q == 'cards' or q == 'a trump cards' or q == 'the trump cards' or q == 'trump cards':
							printf("\nWell I won't congradulate you but if you were too smart then you would have pass those sys commands \nwhich you are told in the mail rather than answering my questions. \nHa ha ha ha ha........I just changed the prompt sign....and if you can't really figured it out \nthen you proved yourself a SHIT... \n\n")
							time.sleep(2)
							return 'death'
						elif b == '-h.destroy MY_DATABASE':
							winsound.PlaySound(None, winsound.SND_PURGE)
							time.sleep(1)
							Level8().printinoneline0('Collecting your database...', 'Deleting MY_DATABASE. Please wait...')
							print "\nYour database has been successfully deleted."
							bgsound()
							z = raw_input('sys$Terminal:~ ')
							if z == '-h.shtdwn':
								Level1().animate('Shutting down your system', 7)
								print "\nSystem shut down successfully.\n"
								time.sleep(1)
								return 'finished'
							else:
								"%r command does not exist." % z
						elif b == 'igiveup':
							print "\x1b[32m\x1b[1m"
							printf("\n\nProbably you are using cheat-codes to complete the game and the hacker thus banned you from your system.")
							time.sleep(1)
							return 'death'
						elif q == '':
							b
						else:
							print "\nI was very much sure of your lose, SHIT. \nMaybe you ran out of time.\n"
							time.sleep(1)
							return 'death'
					elif a == '-h.destroy MY_DATABASE':
						winsound.PlaySound(None, winsound.SND_PURGE)
						time.sleep(1)
						Level8().printinoneline0('Collecting your database...', 'Deleting MY_DATABASE. Please wait...')
						print "\nYour database has been successfully deleted.\n"
						bgsound()
						z = raw_input('sys$Terminal:~ ')
						if z == '-h.shtdwn':
							Level1().animate('Shutting down your system', 7)
							print "\nSystem shut down successfully.\n"
							time.sleep(1)
							return 'finished'
						else:
							"%r command does not exist." % z
					elif a == 'igiveup':
						print "\x1b[32m\x1b[1m"
						printf("\n\nProbably you are using cheat-codes to complete the game and the hacker thus banned you from your system.")
						time.sleep(1)
						return 'death'
					elif p == '':
						a
					else:
						print "\nYou will always be dumb as you are.\n"
						time.sleep(1)
						return 'death'
				elif x == '-h.destroy MY_DATABASE':
					winsound.PlaySound(None, winsound.SND_PURGE)
					time.sleep(1)
					Level8().printinoneline0('Collecting your database...', 'Deleting MY_DATABASE. Please wait...')
					print "\nYour database has been successfully deleted.\n"
					bgsound()
					z = raw_input('sys$Terminal:~ ')
					if z == '-h.shtdwn':
						Level1().animate('Shutting down your system', 7)
						print "System shut down successfully."
						time.sleep(1)
						return 'finished'
					else:
						"%r command does not exist." % z
				elif x == 'igiveup':
					print "\x1b[32m\x1b[1m"
					printf("\n\nProbably you are using cheat-codes to complete the game and the hacker thus banned you from your system.")
					time.sleep(1)
					return 'death'
				elif y == '':
					x
				else:
					print "\x1b[31m\nAs usual as a dumb.\n"
					time.sleep(1)
					return 'death'
			printf("\nYou ran out of time, SHIT!")
			return 'death'
			

	class Finished(Scene):

		def enter(self):
			winsound.PlaySound(None, winsound.SND_PURGE)
			print "\nYou are successful in preserving your anonimity. \nLater, you got some other contracts too and got a job in reputable software company."
			time.sleep(3)
			credits()
			os.remove('savegame0.dat')
			os.remove('savegame1.dat')
			os.remove('savegame2.dat')
			return 'finished'
			
			
	class Map(object):

		scenes = {
			'level1': Level1(),
			'level2': Level2(),
			'level3': Level3(),
			'level4': Level4(),
			'level5': Level5(),
			'level6': Level6(),
			'level7': Level7(),
			'level8': Level8(),
			'death': Death(),
			'finished': Finished()
		}
		
		def __init__(self, start_scene):
			self.start_scene = start_scene
			
		def next_scene(self, scene_name):
			if not scene_name == 'death' and not scene_name == 'finished':
				pickle.dump(scene_name, open("savegame2.dat", 'wb'))
			return Map.scenes.get(scene_name)
			
		def opening_scene(self):
			return self.next_scene(self.start_scene)
			
	try:
		scene_name = pickle.load(open('savegame2.dat', 'rb'))
		a_Map = Map(scene_name)
		a_game = Engine(a_Map)
		a_game.play()
	except:
		a_Map = Map('level1')
		a_game = Engine(a_Map)
		a_game.play()


class Anonymous(object):

	bgsound()

	def __init__(self, root):
		self.root = root
		self.root.iconbitmap(default = 'Images/favicon.ico')
		self.root.title('The Anonymous')
		self.root.resizable(0,0)
	
		self.image = Image.open('Images/image.jpg')
		self.photo_image = ImageTk.PhotoImage(self.image)
		self.label = Label(root, image = self.photo_image)
		self.label.pack()
	
		self.w = 500
		self.h = 500
		self.ws = self.root.winfo_screenwidth() 
		self.hs = self.root.winfo_screenheight()
		self.x = (self.ws/2) - (self.w/2)
		self.y = (self.hs/2) - (self.h/2)
		self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
		
		self.playimg = ImageTk.PhotoImage(Image.open('Buttons/play.jpg'))
		self.play = Button(root, font = ('NeuropolXRg-Regular', '8'), image = self.playimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = self.play)
		self.play.pack()
		self.play.place(height = 50, width = 100, x = 200, y = 260)
		
		self.loadimg = ImageTk.PhotoImage(Image.open('Buttons/load.jpg'))
		self.load = Button(root, font = ('NeuropolXRg-Regular', '8'), image = self.loadimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = self.load)
		self.load.pack()
		self.load.place(height = 50, width = 100, x = 200, y = 320)
		
		self.aboutimg = ImageTk.PhotoImage(Image.open('Buttons/about.jpg'))
		self.about = Button(root, font = ('NeuropolXRg-Regular', '8'), image = self.aboutimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = self.showInfo)
		self.about.pack()
		self.about.place(height = 50, width = 100, x = 200, y = 380)
		
		self.quitimg = ImageTk.PhotoImage(Image.open('Buttons/exit.jpg'))
		self.exit = Button(root, font = ('NeuropolXRg-Regular', '8'), image = self.quitimg, bd = 0, activebackground = 'black', activeforeground = 'white', command = root.quit)
		self.exit.pack()
		self.exit.place(height = 50, width = 100, x = 200, y = 440)
		
	def play(self):
		
		x = os.path.isfile('savegame0.dat')
		y = os.path.isfile('savegame1.dat')
		z = os.path.isfile('savegame2.dat')
		
		if x == True and y == True and z == True:
			choice = tkMessageBox.askquestion("CONTINUE", "A saved game has been found. Would you like to continue your saved game?")
			if choice == 'yes':
				root.destroy()
				ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5)
				time.sleep(0.5)
				origame()
			else:
				os.remove('savegame0.dat')
				os.remove('savegame1.dat')
				os.remove('savegame2.dat')
				root.destroy()
				ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5 )
				Loading()
				time.sleep(1)
				printf("Hello there!")
				time.sleep(2)
				printf("\nYou must be thinking who am I.")
				time.sleep(1)
				printf("\nBut that doesn't really matter. \nFor now you can imagine me as GOD who is presently seeing you and has access to your computer and know almost about you.")
				time.sleep(1)
				printf("\nWhat if some day you woke up and find yourself locked into the dark room.")
				time.sleep(2)
				printf("\nWhat if you lost all your families and friends just because they have hardly misunderstood you.")
				printf("\nAnd you don't even know how to make them realize that you aren't guilty.")
				time.sleep(2)
				printf("\nWhat will you gonna do when you know someone will be at danger but can't make them cautious about it.")
				time.sleep(1)
				printf("\nWhat will you do when the society goes down at the lowest level ?")
				time.sleep(2)
				printf("\nThese questions may seems weird but they are actually not.")
				time.sleep(1)
				printf("\nLet me ask you one simple question.")
				time.sleep(0.5)
				printf("\n\nYou are followed by a murderer and you come up on the place where there are three rooms to hide into.")
				printf("\nRoom-1:- This room is full of raging fires.")
				printf("\nRoom-2:- This room contains full of Assassins who are eager to kill any humans who step into here.")
				printf("\nRoom-3:- This room has full of lions who haven't eaten for three months.")
				printf("\nWhich room would you choose ? You can't wait there as you are chased by the murderer.")
				time.sleep(1)
				bgsound()
				while True:
					x = raw_input('\n\nYOU: ')
					y = x.lower()
					
					if y == 'room-1' or y== '1' or y == 'room1':
						printf("\n\nYou got ultimately burnt into the roomand died.")
						printf("\nPoor Man!")
						time.sleep(2)
						exit(1)
					elif y == 'room-2' or y == 'room2' or y == '2':
						printf("\n\nAs soon as you stepped inside the room the Assassins assassinated you.")
						printf("\nPoor Fellow!")
						time.sleep(2)
						exit(1)
					elif y == 'room-3' or y == 'room3' or y == '3':
						printf("\n\nThe lions must be dead since they haven't eaten anything for three months.")
						printf("\nGood job!")
						time.sleep(1)
						printf("\n\nCongradulations! You have successfully passed our test. \nYou can now join our anonymous hacking group.")
						time.sleep(1)
						printf("\n\nI think you are much eager to know who are anonymous hackers if you don't.")
						printf("\nWell to be brief, anonymous hackers are those hackers who does welfare for \nthe common public usually by hacking means.")
						printf("\nWell nowadays since everything is operated by computers so it is easier for us \nto reveal the truth behind some influential political associations, \nwho just wanna conceal their true identity or their misdeeds, usually by hacking \ntheir sites or emails or computers.")
						printf("\nSo we are what it's called hactivists or something like that.")
						printf("For your kind fortune \nlet me know you that from one million users world-wide nwe have choosen you.")
						printf("\nYou may join us and help us to fight the evils against the society.")
						printf("\n\nBest wishes to you")
						print "\n----------------Thank You"
						time.sleep(2)
						printf("\n\nWould you like to join us ?")
						time.sleep(0.5)
						print "\nYes(y) or No(n)"
						bgsound()
						while True:
							x = raw_input('\n\nYOU: ')
							y = x.lower()
							
							if y == 'y' or y == 'yes':
								printf("\n\nThanks for joining us. There's no turning back now. \nYou will soon be prompted with the 'Terms and Conditions' window. \nDo read them carefully before continuing. Good luck!")
								time.sleep(1)
								ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0)
								time.sleep(0.5)
								windows()
							elif y == 'n' or y == 'no':
								printf("\n\nIt's so bad that we are gonna miss you. \nYou can join us anytime if you change your mind. You are always welcome. :)")
								time.sleep(2)
								exit(1)
							elif y == '':
								x
							else:
								printf("\n\nPlease choose either of the following opinion.")
								bgsound()
					elif y == '':			
						x
					else:
						printf("\n\nPlease choose either of the three options or right room no.")
						bgsound()
		else:
			root.destroy()
			ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5 )
			Loading()
			time.sleep(1)
			printf("Hello there!")
			time.sleep(2)
			printf("\nYou must be thinking who am I.")
			time.sleep(1)
			printf("\nBut that doesn't really matter. \nFor now you can imagine me as GOD who is presently seeing you and has access to your computer and know almost about you.")
			time.sleep(1)
			printf("\nWhat if some day you woke up and find yourself locked into the dark room.")
			time.sleep(2)
			printf("\nWhat if you lost all your families and friends just because they have hardly misunderstood you.")
			printf("\nAnd you don't even know how to make them realize that you aren't guilty.")
			time.sleep(2)
			printf("\nWhat will you gonna do when you know someone will be at danger but can't make them cautious about it.")
			time.sleep(1)
			printf("\nWhat will you do when the society goes down at the lowest level ?")
			time.sleep(2)
			printf("\nThese questions may seems weird but they are actually not.")
			time.sleep(1)
			printf("\nLet me ask you one simple question.")
			time.sleep(0.5)
			printf("\n\nYou are followed by a murderer and you come up on the place where there are three rooms to hide into.")
			printf("\nRoom-1:- This room is full of raging fires.")
			printf("\nRoom-2:- This room contains full of Assassins who are eager to kill any humans who step into here.")
			printf("\nRoom-3:- This room has full of lions who haven't eaten for three months.")
			printf("\nWhich room would you choose ? You can't wait there as you are chased by the murderer.")
			time.sleep(1)
			bgsound()
			while True:
				x = raw_input('\n\nYOU: ')
				y = x.lower()
				if y == 'room-1' or y== '1' or y == 'room1':
					printf("\n\nYou got ultimately burnt into the roomand died.")
					printf("\nPoor Man!")
					time.sleep(2)
					exit(1)
				elif y == 'room-2' or y == 'room2' or y == '2':
					printf("\n\nAs soon as you stepped inside the room the Assassins assassinated you.")
					printf("\nPoor Fellow!")
					time.sleep(2)
					exit(1)
				elif y == 'room-3' or y == 'room3' or y == '3':
					printf("\n\nThe lions must be dead since they haven't eaten anything for three months.")
					printf("\nGood job!")
					time.sleep(1)
					printf("\n\nCongradulations! You have successfully passed our test. \nYou can now join our anonymous hacking group.")
					time.sleep(1)
					printf("\n\nI think you are much eager to know who are anonymous hackers if you don't.")
					printf("\nWell to be brief, anonymous hackers are those hackers who does welfare for \nthe common public usually by hacking means.")
					printf("\nWell nowadays since everything is operated by computers so it is easier for us \nto reveal the truth behind some influential political associations, \nwho just wanna conceal their true identity or their misdeeds, usually by hacking \ntheir sites or emails or computers.")
					printf("\nSo we are what it's called hactivists or something like that.")
					printf("For your kind fortune \nlet me know you that from one million users world-wide we have choosen you.")
					printf("\nYou may join us and help us to fight the evils against the society.")
					printf("\n\nBest wishes to you")
					print "\n----------------Thank You"
					time.sleep(2)
					printf("\n\nWould you like to join us ?")
					time.sleep(0.5)
					print "\nYes(y) or No(n)"
					bgsound()
					while True:
						x = raw_input('\n\nYOU: ')
						y = x.lower()
						
						if y == 'y' or y == 'yes':
							printf("\n\nThanks for joining us. There's no turning back now. \nYou will soon be prompted with the 'Terms and Conditions' window. \nDo read them carefully before continuing. Good luck!")
							time.sleep(1)
							ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0)
							time.sleep(0.5)
							windows()
						elif y == 'n' or y == 'no':
							printf("\n\nIt's so bad that we are gonna miss you. \nYou can join us anytime if you change your mind. You are always welcome. :)")
							time.sleep(2)
							exit(1)
						elif y == '':
							x
						else:
							printf("\n\nPlease choose either of the following opinion.")
							bgsound()
				elif y == '':			
					x
				else:
					printf("\n\nPlease choose either of the three options or right room no.")
					bgsound()
		
	def showInfo(self):
		about = '''
		NAME : The Anonymous
		VERSION: 3.0
		
		DEVELOPER: Jishan Bhattacharya
		MUSIC DIRECTOR: Subhrangshu Adhikary
		ART DIRECTOR: Arijit Roy
		
		This is just a hacking simulation game.
		Any character in the game which matches
		with the real world is just a 
		coincidence.
		
		Copyright 2017 Jishan Bhattacharya
		'''
		tkMessageBox.showinfo("ABOUT", about)
		
	def load(self):
		x = os.path.isfile('savegame0.dat')
		y = os.path.isfile('savegame1.dat')
		z = os.path.isfile('savegame2.dat')
		
		if x == True and y == True and z == True:
			choice = tkMessageBox.askquestion("CONTINUE", "A saved game has been found. Would you like to continue your saved game?")
			if choice == 'yes':
				root.destroy()
				ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5)
				time.sleep(0.5)
				origame()
			else:
				os.remove('savegame0.dat')
				os.remove('savegame1.dat')
				os.remove('savegame2.dat')
				root.destroy()
				ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 5 )
				Loading()
				time.sleep(1)
				printf("Hello there!")
				time.sleep(2)
				printf("\nYou must be thinking who am I.")
				time.sleep(1)
				printf("\nBut that doesn't really matter. \nFor now you can imagine me as GOD who is presently seeing you and has access to your computer and know almost about you.")
				time.sleep(1)
				printf("\nWhat if some day you woke up and find yourself locked into the dark room.")
				time.sleep(2)
				printf("\nWhat if you lost all your families and friends just because they have hardly misunderstood you.")
				printf("\nAnd you don't even know how to make them realize that you aren't guilty.")
				time.sleep(2)
				printf("\nWhat will you gonna do when you know someone will be at danger but can't make them cautious about it.")
				time.sleep(1)
				printf("\nWhat will you do when the society goes down at the lowest level ?")
				time.sleep(2)
				printf("\nThese questions may seems weird but they are actually not.")
				time.sleep(1)
				printf("\nLet me ask you one simple question.")
				time.sleep(0.5)
				printf("\n\nYou are followed by a murderer and you come up on the place where there are three rooms to hide into.")
				printf("\nRoom-1:- This room is full of raging fires.")
				printf("\nRoom-2:- This room contains full of Assassins who are eager to kill any humans who step into here.")
				printf("\nRoom-3:- This room has full of lions who haven't eaten for three months.")
				printf("\nWhich room would you choose ? You can't wait there as you are chased by the murderer.")
				time.sleep(1)
				bgsound()
				while True:
					x = raw_input('\n\nYOU: ')
					y = x.lower()
					
					if y == 'room-1' or y== '1' or y == 'room1':
						printf("\n\nYou got ultimately burnt into the roomand died.")
						printf("\nPoor Man!")
						time.sleep(2)
						exit(1)
					elif y == 'room-2' or y == 'room2' or y == '2':
						printf("\n\nAs soon as you stepped inside the room the Assassins assassinated you.")
						printf("\nPoor Fellow!")
						time.sleep(2)
						exit(1)
					elif y == 'room-3' or y == 'room3' or y == '3':
						printf("\n\nThe lions must be dead since they haven't eaten anything for three months.")
						printf("\nGood job!")
						time.sleep(1)
						printf("\n\nCongradulations! You have successfully passed our test. \nYou can now join our anonymous hacking group.")
						time.sleep(1)
						printf("\n\nI think you are much eager to know who are anonymous hackers if you don't.")
						printf("\nWell to be brief, anonymous hackers are those hackers who does welfare for \nthe common public usually by hacking means.")
						printf("\nWell nowadays since everything is operated by computers so it is easier for us \nto reveal the truth behind some influential political associations, \nwho just wanna conceal their true identity or their misdeeds, usually by hacking \ntheir sites or emails or computers.")
						printf("\nSo we are what it's called hactivists or something like that.")
						printf("For your kind fortune \nlet me know you that from one million users world-wide we have choosen you.")
						printf("\nYou may join us and help us to fight the evils against the society.")
						printf("\n\nBest wishes to you")
						print "\n----------------Thank You"
						time.sleep(2)
						printf("\n\nWould you like to join us ?")
						time.sleep(0.5)
						print "\nYes(y) or No(n)"
						bgsound()
						while True:
							x = raw_input('\n\nYOU: ')
							y = x.lower()
							
							if y == 'y' or y == 'yes':
								printf("\n\nThanks for joining us. There's no turning back now. \nYou will soon be prompted with the 'Terms and Conditions' window. \nDo read them carefully before continuing. Good luck!")
								time.sleep(1)
								ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0)
								time.sleep(0.5)
								windows()
							elif y == 'n' or y == 'no':
								printf("\n\nIt's so bad that we are gonna miss you. \nYou can join us anytime if you change your mind. You are always welcome. :)")
								time.sleep(2)
								exit(1)
							elif y == '':
								x
							else:
								printf("\n\nPlease choose either of the following opinion.")
								bgsound()
					elif y == '':			
						x
					else:
						printf("\n\nPlease choose either of the three options or right room no.")
						bgsound()
		else:
			tkMessageBox.showinfo('LOAD','Sorry, could not find any saved game.')
		
		
root = Tk()
The_Anonymous = Anonymous(root)
root.mainloop()
