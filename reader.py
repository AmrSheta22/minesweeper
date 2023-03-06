from logic import *
from game import *
import cv2
import os
import time
# take a screenshot of the screen and open it
# return the image
def take_screenshot():
    os.system("adb shell screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png")
    img = cv2.imread("screenshot.png")
    return img
# detect which window is open on the screen
import win32gui
game = "Minesweeper Online"
while True:
    window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    window = window.split(" - ")[1]
    print(window)
    if window == game:
        img = take_screenshot()
        break
    else:
        print("game is not open")
        time.sleep(1)
# detect the board
# def detect_board(img):
    # detect the board
    # return the board


