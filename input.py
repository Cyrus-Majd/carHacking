import subprocess
from pynput.keyboard import Key, Controller

proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:

# VALUE OF N: 160 is the middle. anything less is LEFT. anything greater is RIGHT.
keyboard = Controller()
with keyboard.pressed('a'):
    for line in iter(proc.stdout.readline,''):
        s = line.rstrip().decode("UTF-8")
        n = int(s[28:30],16)
        print(n)
        if (n < 140):
            keyboard.release(Key.right)
            keyboard.press(Key.left)
        if(n > 160):
            keyboard.release(Key.left)
            keyboard.press(Key.right)
            
        keyboard.release(Key.left)
        keyboard.release(Key.right)
