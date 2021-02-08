from machine import Pin

# Pin 16 is configured with internal Pull Up resistor. The pin value will be 1(high) when push button is not pressed.
# If Pull Up is used, pushbutton should be between the GPIO and Ground. If Pull Down is used, pushbutton should be between the GPIO and Vcc(3.3V)
button = Pin(16, Pin.IN, Pin.PULL_UP)

# Continuously runs the code under the while loop.
while True:
# Below value should be 0 for PULL_UP and 1 for PULL_DOWN
 if button.value() == 0:
     print("Button Pressed......")
     print(button.value())
