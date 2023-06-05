# Write your code here :-)import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
from adafruit_circuitplayground import cp

a
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    x, y, z = cp.acceleration
    if y < -6:
        kbd.send(Keycode.W)  # Type capital 'A'
        time.sleep(0.1)

    elif y > 6:
        kbd.send(Keycode.S)
        time.sleep(0.1)

    elif x > 3:
        kbd.send(Keycode.D)
        time.sleep(0.1)

    elif x < -3:
        kbd.send(Keycode.A)
        time.sleep(0.1)# Write your code here :-)
