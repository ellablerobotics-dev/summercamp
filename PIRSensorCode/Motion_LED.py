from machine import Pin
import time

#PIR sensor pin 28
pirPin=28
pir_sensor = Pin(pirPin, Pin.IN)

pinNumber=1  #Pin Number
led = Pin(pinNumber, Pin.OUT)

while True:
    # Check the PIR sensor value
    if pir_sensor.value() == 0:
        print("Monitoring...")  # No motion detected
        #turn OFF LED below
        led.off()
    else:
        print("Somebody here!")  # Motion detected
        #turn ON LED below 
        led.on()
        
    time.sleep(1)