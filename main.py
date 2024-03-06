import machine
import time


led_pin = machine.Pin("LED", machine.Pin.OUT)  # GPIO pin 25 controls the onboard LED

while True:
    led_pin.toggle()  # Toggle the LED state
    time.sleep(1)    # Wait for 1 second
