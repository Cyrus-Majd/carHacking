### cyrus's attempt at getting keys and doing things.

from re import I
import time
import threading
import pyautogui
import keyboard

quitFlag = False

def threadFunc():
    while(True):
        if (quitFlag == True):
            break
        pyautogui.press('a', presses=50)

# Create a Thread with a function without any arguments
th = threading.Thread(target=threadFunc)
th.start()

## reading data from the car.
import subprocess
proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)

# Print some messages on console
for line in iter(proc.stdout.readline,''):
    s = line.rstrip().decode("UTF-8")
    n = int(s[28:30],16)
    print(n)

    if (n < 140): #turn left
        pyautogui.press('left', presses=10)
    elif (n > 180): # turn right
        pyautogui.press('right', presses=10)

    if keyboard.read_key() == "q":
        print("You pressed q. quitting.")
        quitFlag = True
        break

th.join()