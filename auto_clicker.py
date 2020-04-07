import pyautogui, time

champx = 800
champy = 500

buyx = 1020
buyy = 800

okx = 1060
oky = 850

for i in range(1, 1000):
    pyautogui.click(champx, champy)
    pyautogui.click(buyx,buyy)
    time.sleep(4)
    pyautogui.click(okx,oky)