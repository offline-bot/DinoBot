import time
from PIL import ImageGrab,ImageOps
import pyautogui
from numpy import *

class Cordinates():
    colorChecker = (540, 200, 570, 225)

time.sleep(5)

captureBox = (Cordinates.colorChecker[0], Cordinates.colorChecker[1], Cordinates.colorChecker[2], Cordinates.colorChecker[3])
image = ImageGrab.grab(captureBox)
grayImage = ImageOps.grayscale(image)
a = array(grayImage.getcolors())
print(a.sum())
image.show()