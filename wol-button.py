from gpiozero import Button
from time import sleep
from wakeonlan import send_magic_packet


button = Button(2)

while True:
	if button.is_pressed:
		send_magic_packet('<MAC-ADDRESS GOES HERE>')
		print("Pressed")
	else:
		pass
	sleep(0.5)
