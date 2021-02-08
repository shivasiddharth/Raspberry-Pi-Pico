# This example is similar to simple-press example. Instead of using a while loop this example uses an interrupt.
from machine import Pin
import utime

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)

# Pin 16 is configured with internal Pull Up resistor. The pin value will be 1(high) when push button is not pressed.
# If Pull Up is used, pushbutton should be between the GPIO and Ground. If Pull Down is used, pushbutton should be between the GPIO and Vcc(3.3V)
button = Pin(16, Pin.IN, Pin.PULL_UP)

# A callback for interrupt. This function will be called when interrupt is triggered.
def led_toggle(irq):
    global led
    led.toggle()

# The interrupt name should take the name of the pushbutton.
# Trigger is normally IRQ_FALLING if PULL_UP is used and IRQ_RISING if PULL_DOWN is used.
button.irq(trigger = Pin.IRQ_FALLING, handler = led_toggle)
