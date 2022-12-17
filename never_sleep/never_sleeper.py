import time
import pyautogui

while True:
    screenWidth, screenHeight = pyautogui.size()
    width_height = pyautogui.size()
    pyautogui.moveTo(10,200) 
    time.sleep(2)
    pyautogui.moveTo(10,220)
    time.sleep(2) 
