from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum
from ssd1306 import SSD1306_I2C
WIDTH =128 
HEIGHT= 64

i2c=I2C(1,scl=Pin(19),sda=Pin(18),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    time.sleep(2)
    pin = Pin(14, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    oled.fill(0)
    oled.text("Weather Station", 0, 0)
    oled.text("Temp:", 0, 30)
    oled.text(str(t), 40, 30)
    oled.text("Hum:", 0, 40)
    oled.text(str(h), 40, 40)
    oled.pixel(10,30,60)  #(x, y, color)
    
    oled.show()