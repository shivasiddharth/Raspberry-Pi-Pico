# Switching using multiple button presses is demonstrated in this example.
# A single press toggles the LED, while a double press makes the LED blink.

from machine import Pin, Timer
import utime

# Variable for storing last interrupt time.
last_interrupt = 0

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)
led_two = Pin(17, Pin.OUT)

# Pin 16 is configured with internal Pull Up resistor. The pin value will be 1(high) when push button is not pressed.
# If Pull Up is used, pushbutton should be between the GPIO and Ground. If Pull Down is used, pushbutton should be between the GPIO and Vcc(3.3V)
button = Pin(16, Pin.IN, Pin.PULL_UP)

tim = Timer()

def tick(timer):
    global led
    led.toggle()


# Function be called for single or simple press
def led_toggle():
    global led
    led.toggle()

def press_check(irq):
    global last_interrupt

    # Get the current time in milliseconds
    current_time_ms = utime.ticks_ms()

    # Calculate the elapsed time since the last interrupt
    delay_time = utime.ticks_diff(current_time_ms, last_interrupt)

    # The value below is the debounce time. Change it according to your pushbutton.
    if (delay_time < 175):
        return

    # Update the time of interrupt
    last_interrupt = current_time_ms

    # Use the printed time as a reference below for the calls.
    print(delay_time)


    # If the delay is greater than 500, it is taken as simple press. Change it according to your project or pushbutton.
    if delay_time > 500:
        led_toggle()
    # If the delay is shorter than 500, it is taken as double press. Change it according to your project or pushbutton.
    else:
        led_two.toggle()

# Interrupt is set to Falling, because of using PULL_UP, if PULL_DOWN is used the interrupt should be set to Rising.
button.irq(trigger = machine.Pin.IRQ_FALLING, handler = press_check)
