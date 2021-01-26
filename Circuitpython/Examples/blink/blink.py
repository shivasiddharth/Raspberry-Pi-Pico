import board
import time
from digitalio import DigitalInOut, Direction

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

def toggle(pin):
    if pin.value:
        pin.value = False
    else:
        pin.value = True

# Continuously runs the code under the while loop.
while True:
    toggle(led)
    time.sleep(3)
