import pyautogui
#import pyperclip
import time

link = "www.globo.com"

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(3)

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
