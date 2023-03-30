from pykeyboard import PyKeyboard
from time import sleep
keyboard = PyKeyboard()

text = "Hi, this is Arabi, typing virtually"

sleep(7)
for t in text:
    keyboard.tap_key(t)
    sleep(0.1)
