from machine import Pin, Timer

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)

tim = Timer()

def tick(timer):
    global led
    led.toggle()

# Frequency is inverse of time.Calculate the frequency based on the duration you want the LED to blink.
tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)

# Alternatively, you can use the period directly giving time value in milliseconds.
# The following is used to repeat the blinking activity periodically.
# tim.init(mode=Timer.PERIODIC, period=1000, callback=tick)

# The following is used to carry trigger the callback function once after the set period.
# tim.init(mode=Timer.ONE_SHOT, period=1000, callback=tick)
