# This example uses a aswitch library from https://github.com/peterhinch/micropython-async

from machine import Pin, Timer
import utime
import uasyncio as asyncio
from aswitch import Pushbutton

async def my_app():
    await asyncio.sleep(600)
# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led_one = Pin(25, Pin.OUT)
led_two = Pin(17, Pin.OUT)

# Pin 16 is configured with internal Pull Up resistor. The pin value will be 1(high) when push button is not pressed.
# If Pull Up is used, pushbutton should be between the GPIO and Ground. If Pull Down is used, pushbutton should be between the GPIO and Vcc(3.3V)
button = Pin(16, Pin.IN, Pin.PULL_UP)

tim = Timer()

def tick(timer):
    global led
    led_two.toggle()

# Function that is called for a short press of the pushbutton
def toggle(led):
    led.toggle()

# Function that is called for double press of the pushbutton
def toggle_two(led):
    tim.deinit()
    led_two.toggle()

# Function that is called for long press of the pushbutton
def start_timer():
    # Frequency is inverse of time.Calculate the frequency based on the duration you want the LED to blink.
    tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)

# Creating the pushbutton instance
pb = Pushbutton(button, suppress=True)

# Pushbutton actions
pb.double_func(toggle_two, (led_two,))

pb.long_func(start_timer)

pb.release_func(toggle, (led_one,))

# Running the main loop
loop = asyncio.get_event_loop()
loop.run_until_complete(my_app())
