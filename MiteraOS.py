import os

CMD = ['write', 'set', 'read', 'shutdown', 'help', 'h', 'restart', 'clear']
HELPS = {'write':'write # message', 'set':'set # vartype # varname # varvalue\nvartype: num, text, bin', 'read':'read # var # text(optional)', 'shutdown':'shutdown # y', 'help':'help\nType h # command to get especific help', 'restart':'restart', 'clear':'clear','h':'h # command'}
PROGS = ['calculator']
SIRIUS = "Sirius OS v0.1a"
NUM = {}
TXT = {}
BIN = {}

def toTXT(txt):
	for n in NUM:
		txt = txt.replace('[{}]'.format(n), str(NUM[n]))
	for t in TXT:
		txt = txt.replace('[{}]'.format(t), TXT[t])
	return txt

def toNUM(num):
	for n in NUM:
		num = num.replace(n, str(NUM[n]))
	return eval(num)

def WRITE(m):
	print(toTXT(m))

def SHUTDOWN():
		exit()
	
def RESTART():
	CLEAR()
	MAINLOOP()

def HELP():
	for c in CMD:
		print(c)
	print('Type h # command to get especific help')

def H(cmd):
	if cmd in CMD:
		print(HELPS[cmd])
	else:
		print('{} isn\'t a command'.format(cmd)) 

def CLEAR():
	os.system('cls')

def SET(type, key, value):
	type = type.lower()
	key = key.lower()
	
	if type == 'num':
		NUM[key] = toNUM(value)
		
	elif type == 'text':
		TXT[key] = toTXT(value)
		
	elif type == 'bin':
		if value == '0' or value == 'FALSE':
			value = 0
		elif value == '1' or value == 'TRUE':
			value = 1

		BIN[key] = value

def READ(v):
	read = input()
	if v in NUM:
		NUM[v] = toNUM(read)
	elif v in TXT:		
		TXT[v] = toTXT(read)

def READt(v, m):
	m = toTXT(m)
	read = input(m)
	if v in NUM:
		NUM[v] = toNUM(read)
	elif v in TXT:		
		TXT[v] = toTXT(read)

def COMMANDS(tk):	
	k = tk[0].lower()
	if k == 'write':
		WRITE(tk[1])
	elif k == 'read':
		if len(tk) == 3:
			READt(tk[1], tk[2])
		elif len(tk) == 2:
			READ(tk[1])
		else:
			print('Need a variable to store data')
	elif k == 'clear':
		CLEAR()
	elif k == 'shutdown':
		SHUTDOWN()
	elif k == 'help':
		HELP()
	elif k == 'set':
		SET(tk[1], tk[2], tk[3])
	elif k == 'h':
		H(tk[1])
	elif k == 'restart':
		RESTART()

def MAINLOOP():
	print(SIRIUS)
	print("Type help to see commands")
	while True:
		userin = input(" :: ")
		toks = userin.split("#")
		for t in range(len(toks)):
			toks[t] = toks[t].rstrip().lstrip()
		if toks[0] in CMD:
			COMMANDS(toks)
		elif toks[0] != '':
			print('{} isn\'t a command'.format(toks[0]))


MAINLOOP()