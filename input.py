import subprocess, threading
from pynput.keyboard import Key,Controller

proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:

# VALUE OF N: 160 is the middle. anything less is LEFT. anything greater is RIGHT.
keyboard = Controller()
prev = (-1,-1)
#thread = threading.Thread(target=keyboard.press, args=('a',))
#thread.run()
#keyboard.press('a')
with keyboard.pressed('a'):
	for line in iter(proc.stdout.readline,''):
		keyboard.press('a')
		s = line.rstrip().decode("UTF-8")
		n = int(s[28:30],16)
		sign = int(s[25:27],16)
		turn = 'l' if sign & 0x8 else 'r'
		mag = ((sign & 0x7) << 8) | n
		if (sign, n) != prev:
			print(f"sign:{sign}, val:{n}, turn:{turn}, mag:{mag}")
				
			if (mag > 30 and turn == 'l'):
				keyboard.release(Key.right)
				keyboard.press(Key.left)
			elif(mag > 30 and turn == 'r'):
				keyboard.release(Key.left)
				keyboard.press(Key.right)
			else:    
				keyboard.release(Key.left)
				keyboard.release(Key.right)
			prev = sign, n

