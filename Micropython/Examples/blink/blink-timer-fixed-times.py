from machine import Pin, Timer
import utime

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)

led.value(0)

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

for i in range(0,11):
    # Change the value to a higher value to increase the time to stop the timer.
    utime.sleep(1)

# Timer is stopped
tim.deinit()
led.value(0)
