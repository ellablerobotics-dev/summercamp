from machine import Pin
import time

pinNumber=1  #Pin Number
delayTime=1  #Delay Time in Second

led = Pin(pinNumber, Pin.OUT)

while True:
    led.on()
    time.sleep(delayTime)
    led.off()
    time.sleep(delayTime)