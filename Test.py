import os, pyautogui
os.chdir('C:\\Users\\twothree\\Desktop\\PythonGuiAuto')


ApsTab = pyautogui.locateCenterOnScreen('AP_Tab_Icon.PNG')

pyautogui.PAUSE = 5

pyautogui.click(ApsTab, 2)

