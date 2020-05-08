import pyperclip
import time

response = ''


while len(pyperclip.paste()) <= 1:
	pyperclip.copy()
	pyperclip.paste()
