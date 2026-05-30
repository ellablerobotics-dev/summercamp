from machine import Pin
import time

gp1=1
gp2=2

ledGreenLight = Pin(gp1, Pin.OUT)
ledYellowLight = Pin(gp2, Pin.OUT)

while True:
    ledGreenLight.on()
    ledYellowLight.on()
    time.sleep(1)
    
    ledGreenLight.off()
    ledYellowLight.off()
    time.sleep(1)
