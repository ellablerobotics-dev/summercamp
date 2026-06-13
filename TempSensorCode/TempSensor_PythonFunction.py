from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

checkInterval=5  #check sensor every 5 seconds
signalPin=14     #signal pin for DHT sensor

def checkTemperature():
    pin = Pin(signalPin, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = sensor.temperature
    h = sensor.humidity
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))    

while True:
    time.sleep(checkInterval)
    checkTemperature()
