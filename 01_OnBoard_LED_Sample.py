from machine import Pin
import time

# Use "LED" for Pico W or 25 for the original Pico
led = Pin("LED", Pin.OUT) 

while True:
    led.toggle()      # Switch LED state (on to off, or off to on)
    time.sleep(0.5)   # Wait for 0.5 seconds