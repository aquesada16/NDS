from contextlib import contextmanager
from tkinter import Message
import pyautogui
import time
Message = 6
while True > 0:
    time.sleep(2)
    pyautogui.typewrite("vente a cenar")
    time.sleep(1)
    pyautogui.press("enter")
Message = Message - 1
