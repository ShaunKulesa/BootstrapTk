import os
import pyautogui
import time

os.system("start cmd")
time.sleep(1)

pyautogui.write('cd C:\\Users\Home\\Desktop\\BootstrapTk')
pyautogui.press('enter')
time.sleep(1)

pyautogui.write('python setup.py bdist_wheel')
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('twine upload dist/*')
pyautogui.press('enter')
time.sleep(5)

