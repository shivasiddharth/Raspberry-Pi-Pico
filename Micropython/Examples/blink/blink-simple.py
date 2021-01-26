from machine import Pin
import utime

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)

# Continuously runs the code under the while loop.
while True:
 led.toggle()
 # Time is set in seconds
 utime.sleep(1)
