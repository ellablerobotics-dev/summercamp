from machine import Pin
import time

#PIR sensor pin 28
pir_sensor = Pin(28, Pin.IN)

while True:
    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
    else:
        print("Somebody here!")  # Motion detected
    
    time.sleep(1)