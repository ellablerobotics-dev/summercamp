from machine import Pin
import time

#PIR sensor pin 28
pir_sensor = Pin(28, Pin.IN)
ledPin = 1
led = Pin(ledPin, Pin.OUT)

def lightUpLED():
    led.on()

def turnOffLED():
    led.off()

while True:
    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        turnOffLED()
    else:
        print("Somebody here!")  # Motion detected
        lightUpLED()
        
    time.sleep(1)
