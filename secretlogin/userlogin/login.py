import os, sys, time, random, socket

import getpass


def login(database="branche//databases//user_db.sql"):




	username = input("username: ")
	logintries = 0



	while True:
		password = getpass("password: ")





		with open(database, "r") as f:
			text = f.read()




		find_account = text.find("|username= " + username + "|password= " + password + "|" + "\n")
	


	
		if find_account != -1:




			with open("branche//logs//user_login.sql", 'a') as f:

				dates = datetime.datetime.now()
				x = socket.gethostbyname(socket.gethostname())

				f.write(f"('logged-user':'{username}', 'login-date':'{dates}', 'logged-ip':'{x}', 'login-tries':'{logintries}')\n")





			with open("branche//databases//user_safe.sql", "w") as f:
				f.write(username)
				f.close()




			with open("branche//logs//command_logs//log_safe.sql", "w") as f:
				f.write(username)
				f.close()




			with open("branche//logs//logged-on//log.sql", "w") as f:
				f.write(f"{dates}")
				f.close()




			with open("etc//user_title.tfx", "r") as f:
				text = f.read()
			os.system(f"title {text}")






			os.system('cls' if os.name == 'nt' else 'clear')




			with open("branding//sections//home_splash.tfx", "r", encoding="utf8") as f:
				print(f.read())

			return
			#main()





		else:




			logintries = logintries + 1

			if logintries == 3:
				with open("branche//errors//login_errors//user_login_error.py") as f:
					exec(f.read())
		


	
			else:
				continue







os.system('cls' if os.name == 'nt' else 'clear')
logintries = 0
dir
login()