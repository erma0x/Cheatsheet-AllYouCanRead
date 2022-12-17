#! usr/bin/python3
import time
import pyautogui    
import keyboard
recorded = keyboard.record(until='esc') # STOP with Exit button

wait_seconds = 6 # wait between 2 clicks

x_pos = 250 # x position
y_pos = 250 # y position

def start():
    sec = 0 # starting second
    
    while True:
            # used try so that if user pressed other 
            #than the given key error will not be shown
            if keyboard.is_pressed('p'):
                exit(0)

            print(recorded) 
                                    
            pyautogui.click(x_pos , y_pos)   # click
               
            time.sleep(wait_seconds) # wait
        
if __name__=='__main__':
    start()
