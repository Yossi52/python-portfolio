import pyautogui
from PIL import Image
import time
# # pip install opencv-python

# type game address
pyautogui.moveTo(268, 55, duration=0.3)
pyautogui.click()
pyautogui.hotkey("Ctrl", "a")
pyautogui.write('https://elgoog.im/t-rex/', interval=0.05)
pyautogui.press("enter")
time.sleep(3)

# game start
pyautogui.press("up")
# get dino's position.py
time.sleep(2)
dino_cor = pyautogui.locateCenterOnScreen("image/dino.png", confidence=0.9, grayscale=True)
if dino_cor is None:
    dino_cor = pyautogui.locateCenterOnScreen("image/dino2.png", confidence=0.9, grayscale=True)
check_box = (dino_cor[0]+80, dino_cor[1]-25, 70, 35)

while True:
    pyautogui.screenshot("screenshot.jpg", region=check_box)
    with Image.open("screenshot.jpg") as img:
        try:
            if len(img.getcolors()) > 15:
                pyautogui.press("up")
        except TypeError:
            pass
