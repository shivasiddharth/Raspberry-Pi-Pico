from machine Timer
import board
from digitalio import DigitalInOut, Direction
import time

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = DigitalInOut(board.25)
led.direction = Direction.OUTPUT

tim = Timer()

def tick(timer):
    global led
    global counter
    led.toggle()


# Frequency is inverse of time.Calculate the frequency based on the duration you want the LED to blink.
tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)

# Alternatively, you can use the period directly giving time value in milliseconds.
# The following is used to repeat the blinking activity periodically.
# tim.init(mode=Timer.PERIODIC, period=1000, callback=tick)

# The following is used to carry out the blinking activity once after the set period.
# tim.init(mode=Timer.ONE_SHOT, period=1000, callback=tick)

for i in range(0,11):
    # Change the value to a higher value to increase the time to stop the timer.
    time.sleep(1)

# Timer is stopped
tim.deinit()
