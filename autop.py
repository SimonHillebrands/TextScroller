import pyautogui
import time
import sys
import os
import inspirobot

try:
	if(sys.argv[1] == "I"):
		text = ""
		flow = inspirobot.flow()
		for quote in flow:
			text = text + quote.text
		print(text)
		command = 'python test.py ' '"' + text + ' "'
	else:
		command = 'python test.py ' + '"' + sys.argv[1] + ' "'
except IndexError:
	print("Your forgot to add an argument")
os.system(command)

