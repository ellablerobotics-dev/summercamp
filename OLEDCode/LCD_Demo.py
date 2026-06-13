from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime as time
from dht import DHT11, InvalidChecksum

WIDTH =128 
HEIGHT= 64

i2c=I2C(1,scl=Pin(19),sda=Pin(18),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    oled.fill(0)
    oled.text("Environment Lab", 0, 0)
    
    pin = Pin(14, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = sensor.temperature
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    oled.text("Temp:", 20, 30)
    oled.text(str(t), 60, 30)
    
    oled.text("Humi:", 20, 40)
    oled.text(str(h), 60, 40)
    
    oled.pixel(10,30,60)  #(x, y, color)
    
    oled.show()
