from machine import Pin
import time

gp1=1
gp2=2
gp3=3

ledGreenLight = Pin(gp1, Pin.OUT)
ledYellowLight = Pin(gp2, Pin.OUT)
ledRedLight = Pin(gp3, Pin.OUT)

while True:
    ledGreenLight.on()
    ledYellowLight.off()
    ledRedLight.off()
    time.sleep(1)
    
    ledGreenLight.off()
    ledYellowLight.on()
    ledRedLight.off()
    time.sleep(1)

    ledGreenLight.off()
    ledYellowLight.off()
    ledRedLight.on()
    time.sleep(1)