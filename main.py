import pyautogui
import keyboard
import json
import time
time.sleep(4)
x = 660
y = 350
ox = 660
oy = 350
im = pyautogui.screenshot()
for column in range(20):
    for square in range(24):
        pyautogui.moveTo(x, y, 0.05)
        x2 = x
        num = None
        found = False
        tries = 0
        while found != True and tries < 20:
            e = im.getpixel((x2, y))
            x2 += 1
            if e == (162, 209, 73) and found != True:
                print("Unknown")
                found = True
            elif e == (170, 215, 81) and found != True:
                print("Unknown")
                found = True
            elif e == (25, 118, 210) and found != True:
                found = True
                print("Number 1")
            elif e == (212, 66, 62) and found != True:
                found = True
                print("Number 3")
            elif e == (56, 142, 60) and found != True:
                found = True
                print("Number 2")
            elif e == (163, 97, 158) and found != True:
                found = True
                print("Number 4")
            elif e == (255, 143, 0) and found != True:
                found = True
                print("Number 5")
            #elif e == () and found != True:
            #    pass
            #elif e == () and found != True:
            #    pass
            else:
                #print(e)
                tries += 1
        if found == False:
            print("FAILED")
        x += 25
    x = ox 
    y += 25
    pyautogui.moveTo(x, y, 0.05)