### cyrus's attempt at getting keys and doing things.

from re import I
import time
import threading
import pyautogui
import keyboard

# def left(hold_time):
#     start = time.time()
#     while time.time() - start < hold_time:
#         pyautogui.press('left')

# quitFlag = False

# def threadFunc():
#     while(True):
#         if (quitFlag == True):
#             break
#         # pyautogui.press('a', presses=50)
#         pyautogui.keyDown('a')
#         time.sleep(2)
#         pyautogui.keyUp('a')

# # Create a Thread with a function without any arguments
# th = threading.Thread(target=threadFunc)
# th.start()

## reading data from the car.
import subprocess
proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)

# Print some messages on console
for line in iter(proc.stdout.readline,''):
    s = line.rstrip().decode("UTF-8")
    n = int(s[28:30],16)
    # print(n)

    if (n < 140): #turn left
        # print("left")
        # left(2000)
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')

        # pyautogui.press('left', presses=50)
    if (n > 140): # turn right
        # print("right")
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        # pyautogui.press('right', presses=50)

    time.sleep(2)
#     if keyboard.read_key() == "q":
#         print("You pressed q. quitting.")
#         quitFlag = True
#         break

# th.join()