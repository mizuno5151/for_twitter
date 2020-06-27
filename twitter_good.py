# -*- coding: utf-8 -*-

import pyautogui as gui
import time
def click_good(max):
    for i in range(max):
        try:
            x,y = gui.locateCenterOnScreen("good.png", grayscale=True)
            print(x,y)
            gui.click(x,y)
            time.sleep(1)
        except:
            print("例外")
            scroll()
            time.sleep(1)
        


def scroll():
    gui.scroll(-800)
 

time.sleep(1)
while True:    
    click_good(50)
    time.sleep(150)
#print(check_empty_good())