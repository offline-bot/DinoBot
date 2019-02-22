import time
from PIL import ImageGrab,ImageOps
import pyautogui
from numpy import *

blackMode = False

last =0
class Cordinates():
    replayBtn = (1452, 824)
    dinoCore = (522, 200, 552, 225)
    colorChecker = (100, 150, 150, 200)

def isLightMode():
    captureBox = (Cordinates.colorChecker[0], Cordinates.colorChecker[1], Cordinates.colorChecker[2], Cordinates.colorChecker[3])
    image = ImageGrab.grab(captureBox)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    if(a.sum() == 2755):
        return True
    else:
        return False



def restartGame():
    pyautogui.click(Cordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    print('jump')
    pyautogui.keyUp('space')

def imageGrab():
    captureBox = (Cordinates.dinoCore[0], Cordinates.dinoCore[1], Cordinates.dinoCore[2], Cordinates.dinoCore[3])
    image = ImageGrab.grab(captureBox)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    if(isLightMode() == False):
        print(a.sum())
    return a.sum()


time.sleep(4)
# restartGame()
# restartGame()
# time.sleep(1)


while True:


    if (isLightMode()):
        if (imageGrab() != 1005):
            print("lolL")
            pressSpace()
    else:
        if (imageGrab() != 750):
            print("lolD")
            pressSpace()






