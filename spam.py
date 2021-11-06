import pyautogui
import time

message = "GAUSA SPAAMMMMMM"
n = 50

time.sleep(5)

for i in range(n):
    pyautogui.typewrite(message + "\n")