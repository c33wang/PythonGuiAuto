import os, pyautogui, time
os.chdir('C:\\Users\\twothree\\Desktop\\PythonGuiAuto')

time.sleep(2)

ApsTab = pyautogui.locateCenterOnScreen('AP_Tab_Icon.PNG' or 'Bold_AP_Tab_Icon.PNG')
pyautogui.click(ApsTab)

time.sleep(1)

DUT = pyautogui.locateCenterOnScreen('DUT.PNG')
pyautogui.click(DUT)

time.sleep(1)

Config = pyautogui.locateCenterOnScreen('Config.PNG')
pyautogui.click(Config)

time.sleep(1)

Radio = pyautogui.locateCenterOnScreen('Radio.PNG')
pyautogui.click(Radio)

time.sleep(1)

Radio5g = pyautogui.locateCenterOnScreen('Radio5G.PNG')
pyautogui.moveTo(Radio5g)
pyautogui.moveRel(0, 60)
pyautogui.moveRel(100, 0)
pyautogui.click()

####//////////////////////////HT20///////////////////////////
##pyautogui.moveRel(0, 28)
##pyautogui.click()

##//////////////////////////HT40///////////////////////////
pyautogui.moveRel(0, 58)
pyautogui.click()

####//////////////////////////HT80///////////////////////////
##pyautogui.moveRel(0, 78)
##pyautogui.click()




