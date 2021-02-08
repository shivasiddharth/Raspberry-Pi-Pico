from machine import Pin

# Pin values are GPIO values(numbers) and not physical pin numbers. Please refer the pinout diagram for clarity.
led = Pin(25, Pin.OUT)

# Pin is configured with internal Pull Up resistor. The pin value will be 1(high) when push button is not pressed.
# If Pull Up is used, pushbutton should be between the GPIO and Ground. If Pull Down is used, pushbutton should be between the GPIO and Vcc(3.3V)
on = Pin(16, Pin.IN, Pin.PULL_UP)
off = Pin(18, Pin.IN, Pin.PULL_UP)

# Continuously runs the code under the while loop.
while True:
# Below value should be 0 for PULL_UP and 1 for PULL_DOWN
 if on.value() == 0:
     led.value(1)
 if off.value() == 0:
     led.value(0)
