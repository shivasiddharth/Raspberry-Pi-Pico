import board
import time
from digitalio import DigitalInOut, Direction

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = DigitalInOut(board.25)
led.direction = Direction.OUTPUT

# Continuously runs the code under the while loop.
while True:
 led.toggle()
 # Time is set in seconds
 time.sleep(1)
