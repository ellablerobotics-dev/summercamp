from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH =128 
HEIGHT= 64

i2c=I2C(1,scl=Pin(19),sda=Pin(18),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    oled.fill(0)
    oled.text("DIY PROJECTS LAB", 0, 0)
    oled.text("Tutorial", 20, 30)
    oled.pixel(10,30,60)  #(x, y, color)
    
    oled.show()