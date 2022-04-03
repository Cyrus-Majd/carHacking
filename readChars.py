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

time.sleep(2)

# Create a Thread with a function without any arguments
th = threading.Thread(target=threadFunc)
th.start()

# Print some messages on console
while(True):


    if keyboard.read_key() == "q":
        print("You pressed q. quitting.")
        quitFlag = True
        break

th.join()