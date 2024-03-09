import pyautogui
import keyboard
import json
import time

coordinates = []
t = True
while t == True:
    if keyboard.is_pressed('u') == True:
        print("Getting the mouse's location")
        x, y = pyautogui.position()
        print(x)
        print(y)
        coordinates.append((x, y))
    elif keyboard.is_pressed('t') == True:
        t = False
    else:
        print('Shift is up')
    time.sleep(0.5)

with open("mines.txt", "w+") as f:
    lr = []
    for x, y in coordinates:
        sss = str(x) + " " + str(y)
        lr.append(sss)
    dr = "\n".join(lr)
    f.write(dr)
f.close()
#for x, y in coordinates:
#    pyautogui.moveTo(x, y, 1)