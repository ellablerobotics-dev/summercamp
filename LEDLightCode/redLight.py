from machine import Pin
import time

pinNumber=0  #Pin Number
newNumber=15

delayTime=1  #Delay Time in Second

led = Pin(pinNumber, Pin.OUT)
anotherLED = Pin(newNumber, Pin.OUT)

while True:
    led.on()
    anotherLED.on()
    time.sleep(delayTime)
    led.off()
    anotherLED.off()
    time.sleep(delayTime)